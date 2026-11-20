"""Register a four-pose right-walk strip in the original pet's right-walk row."""

import argparse
import hashlib
import json
from pathlib import Path
import statistics
import subprocess
import sys

from PIL import Image, ImageDraw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("atlas", type=Path)
    parser.add_argument("strip", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--skill-scripts", type=Path, required=True)
    args = parser.parse_args()
    sys.path.insert(0, str(args.skill_scripts))
    from despill_chroma_edges import decontaminate_image
    from extract_strip_frames import (component_frame_groups, component_group_image,
                                      remove_chroma_background)
    from render_animation_previews import ROW_DURATIONS, save_preview

    before = Image.open(args.atlas).convert("RGBA")
    if before.size != (1536, 2288):
        raise ValueError("Expected a v2 atlas")
    key = (0, 255, 255)
    strip = remove_chroma_background(Image.open(args.strip).convert("RGBA"), key, 96)
    groups = component_frame_groups(strip, 4)
    if groups is None:
        raise ValueError("Expected four separate right-facing poses")
    poses = [component_group_image(strip, group) for group in groups]
    poses = [pose.crop(pose.getbbox()) for pose in poses]
    idle = before.crop((0, 0, 192, 208)).getbbox()
    assert idle is not None
    baseline = idle[3]
    scale = min((baseline - idle[1]) / statistics.median(f.height for f in poses),
                (baseline - 3) / max(f.height for f in poses))

    frames = []
    for pose in poses:
        sprite = pose.resize((round(pose.width * scale), round(pose.height * scale)),
                             Image.Resampling.LANCZOS)
        if sprite.width >= 184:
            raise ValueError("Pose is too wide for its cell")
        frame = Image.new("RGBA", (192, 208))
        frame.paste(sprite, ((192 - sprite.width) // 2, baseline - sprite.height))
        frame, _ = decontaminate_image(frame, chroma_key=key, strength=1,
                                       edge_radius=5, spill_tolerance=.15)
        assert frame.getbbox()[3] == baseline
        frames.append(frame)

    order = (0, 1, 1, 2, 2, 3, 3, 0)
    atlas = before.copy()
    for col, index in enumerate(order):
        atlas.paste(frames[index], (col * 192, 208))
    output = args.output
    output.mkdir(parents=True, exist_ok=True)
    sheet = output / "spritesheet.webp"
    atlas.save(sheet, lossless=True, exact=True, method=6)
    encoded = Image.open(sheet).convert("RGBA")
    assert encoded.tobytes() == atlas.tobytes()
    changed = [row for row in range(11)
               if encoded.crop((0, row * 208, 1536, (row + 1) * 208)).tobytes()
               != before.crop((0, row * 208, 1536, (row + 1) * 208)).tobytes()]
    assert changed == [1]
    for script, options in (
        ("validate_atlas.py", ["--require-v2", "--chroma-key", "#00FFFF",
                               "--json-out", str(output / "validation.json")]),
        ("make_contact_sheet.py", ["--output", str(output / "contact-sheet.png")]),
    ):
        subprocess.run([sys.executable, str(args.skill_scripts / script), str(sheet), *options],
                       check=True, stdout=subprocess.DEVNULL)
    save_preview([frames[i] for i in order], ROW_DURATIONS["running-right"],
                 output / "running-right.gif")
    comparison = Image.new("RGB", (768, 440), "#303640")
    label = ImageDraw.Draw(comparison)
    for row, (name, version) in enumerate((("Before", before), ("After", encoded))):
        label.text((6, 220 * row + 4), name, fill="white")
        for slot, col in enumerate((0, 1, 3, 5)):
            frame = version.crop((col * 192, 208, (col + 1) * 192, 416))
            comparison.paste(frame, (slot * 192, 220 * row + 10), frame)
    comparison.save(output / "face-comparison.png")
    report = {
        "changed_rows": changed,
        "frame_source_order": order,
        "baseline": baseline,
        "before_rgba_sha256": hashlib.sha256(before.tobytes()).hexdigest(),
        "after_rgba_sha256": hashlib.sha256(encoded.tobytes()).hexdigest(),
    }
    (output / "walk-right-face.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
