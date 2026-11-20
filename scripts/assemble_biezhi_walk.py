"""Replace the incorrectly facing boots in the two Biezhi walk rows."""

import argparse
import json
from pathlib import Path
import statistics
import subprocess
import sys

from PIL import Image, ImageChops, ImageDraw


def cell(atlas, row, col):
    return atlas.crop((col * 192, row * 208, (col + 1) * 192, (row + 1) * 208))


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

    original = Image.open(args.atlas).convert("RGBA")
    assert original.size == (1536, 2288)
    key = (0, 255, 255)
    source = remove_chroma_background(Image.open(args.strip).convert("RGBA"), key, 96)
    shots = []
    for row in range(2):
        strip = source.crop((0, row * source.height // 2, source.width,
                             (row + 1) * source.height // 2))
        groups = component_frame_groups(strip, 4)
        if groups is None:
            raise ValueError(f"Expected four distinct poses in source row {row + 1}")
        for group in groups:
            pose = component_group_image(strip, group)
            shots.append(pose.crop(pose.getbbox()))

    idle = cell(original, 0, 0).getbbox()
    assert idle is not None
    baseline = idle[3]
    scale = min((baseline - idle[1]) / statistics.median(p.height for p in shots),
                (baseline - 3) / max(p.height for p in shots))
    cleaned = []
    for pose in shots:
        img = pose.resize((round(pose.width * scale), round(pose.height * scale)),
                          Image.Resampling.LANCZOS)
        if img.width >= 184:
            raise ValueError("Source pose would clip the cell")
        frame = Image.new("RGBA", (192, 208))
        frame.paste(img, ((192 - img.width) // 2, baseline - img.height))
        frame, _ = decontaminate_image(frame, chroma_key=key, strength=1,
                                       edge_radius=5, spill_tolerance=.15)
        cleaned.append(frame)

    # Preserve the original head and outfit. Match the revised leg roots to the
    # old silhouette around the skirt hem before joining the lower half.
    orders = (0, 1, 1, 2, 2, 3, 3, 0)
    source_columns = (0, 1, 3, 5)
    atlas = original.copy()
    decisions = []
    comparison = Image.new("RGB", (768, 880), "#3a434f")
    label = ImageDraw.Draw(comparison)
    for i, state in enumerate(("running-right", "running-left")):
        sprites = []
        row = i + 1
        for pose, col in enumerate(source_columns):
            before = cell(original, row, col)
            new = cleaned[i * 4 + pose]
            before_a = before.getchannel("A").point(lambda a: 255 if a > 128 else 0)
            new_a = new.getchannel("A").point(lambda a: 255 if a > 128 else 0)
            def seam_measure(y, offset):
                old_band = before_a.crop((0, y - 2, 192, y + 2))
                new_band = new_a.crop((-offset, y - 2, 192 - offset, y + 2))
                return sum(ImageChops.difference(old_band, new_band).histogram()[1:])

            score, _, _, y, dx = min(
                (seam_measure(y, dx), abs(y - 169), abs(dx), y, dx)
                for y in range(163, 178) for dx in range(-8, 9))
            joined = before.copy()
            joined.paste(new.crop((-dx, y, 192 - dx, 208)), (0, y))
            sprites.append(joined)
            decisions.append({"row": row, "pose": pose + 1, "seam_y": y,
                              "offset_x": dx, "seam_alpha_difference": score})
            for level, frame in enumerate((before, joined)):
                py = (i * 2 + level) * 220
                label.text((5, py + 2), f"{state} {'candidate' if level else 'original'}",
                           fill="white")
                comparison.paste(frame, (pose * 192, py + 12), frame)
        for col, pose in enumerate(orders):
            atlas.paste(sprites[pose], (col * 192, 208 * row))
        save_preview([sprites[j] for j in orders], ROW_DURATIONS[state],
                     args.output / f"{state}.gif")

    sheet = args.output / "spritesheet.webp"
    atlas.save(sheet, lossless=True, exact=True, method=6)
    encoded = Image.open(sheet).convert("RGBA")
    assert encoded.tobytes() == atlas.tobytes()
    changed = [r for r in range(11) if encoded.crop((0, 208*r, 1536, 208*(r+1))).tobytes()
               != original.crop((0, 208*r, 1536, 208*(r+1))).tobytes()]
    assert changed == [1, 2]
    comparison.save(args.output / "walk-comparison.png")
    (args.output / "walk-foot-direction.json").write_text(
        json.dumps({"changed_rows": changed, "baseline": baseline, "pose_joins": decisions},
                   indent=2) + "\n", encoding="utf-8")
    for script, options in (
        ("validate_atlas.py", ["--require-v2", "--chroma-key", "#00FFFF",
                               "--json-out", str(args.output / "validation.json")]),
        ("make_contact_sheet.py", ["--output", str(args.output / "contact-sheet.png")]),
    ):
        subprocess.run([sys.executable, str(args.skill_scripts / script), str(sheet), *options],
                       check=True, stdout=subprocess.DEVNULL)


if __name__ == "__main__":
    main()
