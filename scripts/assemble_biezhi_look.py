"""Register two eight-pose gaze strips and replace only the atlas's gaze rows."""

import argparse
import hashlib
import json
from pathlib import Path
import statistics
import subprocess
import sys

from PIL import Image


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("atlas", type=Path)
    parser.add_argument("right_strip", type=Path)
    parser.add_argument("left_strip", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--skill-scripts", type=Path, required=True)
    args = parser.parse_args()
    sys.path.insert(0, str(args.skill_scripts))
    from despill_chroma_edges import decontaminate_image
    from extract_strip_frames import (component_frame_groups, component_group_image,
                                      remove_chroma_background)
    from render_animation_previews import save_preview

    original = Image.open(args.atlas).convert("RGBA")
    assert original.size == (1536, 2288)
    key = (0, 255, 255)
    poses = []
    for path in (args.right_strip, args.left_strip):
        strip = remove_chroma_background(Image.open(path).convert("RGBA"), key, 96)
        groups = component_frame_groups(strip, 8)
        if groups is None:
            raise ValueError(f"{path.name} does not contain eight separate poses")
        for group in groups:
            pose = component_group_image(strip, group)
            bbox = pose.getbbox()
            assert bbox is not None
            poses.append(pose.crop(bbox))

    idle_box = original.crop((0, 0, 192, 208)).getbbox()
    assert idle_box is not None
    baseline = idle_box[3]
    scale = (idle_box[3] - idle_box[1]) / statistics.median(pose.height for pose in poses)
    gaze = Image.new("RGBA", (1536, 416))
    for index, pose in enumerate(poses):
        sprite = pose.resize((round(pose.width * scale), round(pose.height * scale)),
                             Image.Resampling.LANCZOS)
        if sprite.height >= baseline or sprite.width >= 184:
            raise ValueError(f"Pose {index * 22.5:g} exceeds the cell")
        row, col = divmod(index, 8)
        gaze.paste(sprite, (col * 192 + (192 - sprite.width) // 2,
                            row * 208 + baseline - sprite.height))
    gaze, _ = decontaminate_image(gaze, chroma_key=key, strength=1, edge_radius=5,
                                  spill_tolerance=.15, minimum_saturation=.1)
    final = original.copy()
    final.paste(gaze, (0, 1872))
    args.output.mkdir(parents=True, exist_ok=True)
    sheet = args.output / "spritesheet.webp"
    final.save(sheet, lossless=True, exact=True, method=6)
    encoded = Image.open(sheet).convert("RGBA")
    assert encoded.tobytes() == final.tobytes()
    unchanged = (0, 0, 1536, 1872)
    assert encoded.crop(unchanged).tobytes() == original.crop(unchanged).tobytes()

    for script, options in (
        ("validate_atlas.py", ["--require-v2", "--chroma-key", "#00FFFF",
                               "--json-out", str(args.output / "validation.json")]),
        ("measure_direction_continuity.py", ["--json-out", str(args.output / "continuity.json")]),
        ("make_contact_sheet.py", ["--output", str(args.output / "contact-sheet.png")]),
        ("make_direction_qa_sheet.py", ["--output", str(args.output / "look-directions.png")]),
    ):
        subprocess.run([sys.executable, str(args.skill_scripts / script), str(sheet), *options], check=True)
    comparisons = []
    for index in range(16):
        row, col = divmod(index, 8)
        box = (192 * col, 208 * (row + 9), 192 * (col + 1), 208 * (row + 10))
        canvas = Image.new("RGB", (192, 106), "#242832")
        for x, atlas in ((4, original), (100, encoded)):
            sprite = atlas.crop(box).resize((88, 96), Image.Resampling.LANCZOS)
            canvas.paste(sprite, (x, 5), sprite)
        comparisons.append(canvas)
    save_preview(comparisons, [160] * 16, args.output / "look-comparison.gif")
    report = {"before_rgba_sha256": hashlib.sha256(original.tobytes()).hexdigest(),
              "after_rgba_sha256": hashlib.sha256(encoded.tobytes()).hexdigest(),
              "animation_rows_0_to_8_pixel_identical": True,
              "shared_scale": scale, "baseline": baseline}
    (args.output / "assembly.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
