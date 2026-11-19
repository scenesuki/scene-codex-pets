"""Build a candidate atlas from a four-column, five-row revision sheet."""

import argparse
import json
from pathlib import Path
import statistics
import sys

from PIL import Image, ImageChops, ImageFilter


ROWS = (1, 2, 6, 7, 8)
WALK = (0, 1, 1, 2, 2, 3, 3, 0)
GESTURE = (0, 1, 2, 2, 3, 0)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("atlas", type=Path)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--skill-scripts", type=Path, required=True)
    parser.add_argument("--swap-walk-directions", action="store_true")
    parser.add_argument("--trim-floor-line", action="store_true")
    args = parser.parse_args()
    sys.path.insert(0, str(args.skill_scripts))
    from despill_chroma_edges import decontaminate_image
    from extract_strip_frames import connected_components, component_group_image, remove_chroma_background
    from render_animation_previews import ROW_DURATIONS, save_preview

    before = Image.open(args.atlas).convert("RGBA")
    assert before.size == (1536, 2288)
    key = (0, 255, 255)
    guide = remove_chroma_background(Image.open(args.source).convert("RGBA"), key, 96)
    components = connected_components(guide)
    seeds = sorted(components, key=lambda item: item["area"], reverse=True)[:20]
    if len(seeds) != 20 or min(s["area"] for s in seeds) < .24 * max(s["area"] for s in seeds):
        raise ValueError("Expected twenty independent sprite silhouettes")
    seeds.sort(key=lambda item: (item["bbox"][1] + item["bbox"][3]) / 2)
    groups = [[seed] for seed in seeds]
    seed_ids = {id(s) for s in seeds}
    noise = max(s["area"] for s in seeds) * .002
    for item in components:
        if id(item) in seed_ids or item["area"] < noise:
            continue
        center_y = (item["bbox"][1] + item["bbox"][3]) / 2
        closest = min(range(20), key=lambda i:
                      (seeds[i]["center_x"] - item["center_x"]) ** 2
                      + ((seeds[i]["bbox"][1] + seeds[i]["bbox"][3]) / 2 - center_y) ** 2)
        groups[closest].append(item)

    rows = []
    for offset in range(0, 20, 4):
        ordered = sorted(groups[offset:offset + 4], key=lambda group: group[0]["center_x"])
        poses = [component_group_image(guide, group) for group in ordered]
        rows.append([pose.crop(pose.getbbox()) for pose in poses])

    if args.swap_walk_directions:
        rows[0], rows[1] = rows[1], rows[0]

    idle = before.crop((0, 0, 192, 208)).getbbox()
    assert idle is not None
    baseline = idle[3]
    heights = [pose.height for row in rows for pose in row]
    max_width = max(pose.width for row in rows for pose in row)
    scale = min((baseline - idle[1]) / statistics.median(heights),
                (baseline - 3) / max(heights), 182 / max_width)
    if statistics.median(heights) * scale < (baseline - idle[1]) * .90:
        raise ValueError("Source poses vary too much in height or width")

    atlas = before.copy()
    dest = args.output
    dest.mkdir(parents=True, exist_ok=True)
    names = ("running-right", "running-left", "waiting", "running", "review")
    for row, name, poses in zip(ROWS, names, rows):
        ordered = WALK if row < 3 else GESTURE
        sprites = []
        for pose in poses:
            sprite = pose.resize((round(pose.width * scale), round(pose.height * scale)),
                                 Image.Resampling.LANCZOS)
            frame = Image.new("RGBA", (192, 208))
            frame.paste(sprite, ((192 - sprite.width) // 2, baseline - sprite.height))
            if args.trim_floor_line:
                # Keep the sole edges where the boots extend into the final two scanlines.
                alpha = frame.getchannel("A")
                feet = alpha.crop((0, baseline - 3, 192, baseline - 2))
                footprint = feet.resize((192, 2)).filter(ImageFilter.MaxFilter(5))
                keep = Image.new("L", alpha.size, 255)
                keep.paste(footprint, (0, baseline - 2))
                frame.putalpha(ImageChops.multiply(alpha, keep))
            frame, _ = decontaminate_image(frame, chroma_key=key, strength=1,
                                           edge_radius=5, spill_tolerance=.15)
            sprites.append(frame)
        row_atlas = Image.new("RGBA", (1536, 208))
        for col, index in enumerate(ordered):
            row_atlas.paste(sprites[index], (col * 192, 0))
        atlas.paste(row_atlas, (0, row * 208))
        save_preview([sprites[i] for i in ordered], ROW_DURATIONS[name], dest / f"{name}.gif")

    path = dest / "spritesheet.webp"
    atlas.save(path, lossless=True, exact=True, method=6)
    finished = Image.open(path).convert("RGBA")
    assert finished.tobytes() == atlas.tobytes()
    changed = [r for r in range(11) if finished.crop((0, r * 208, 1536, (r + 1) * 208)).tobytes()
               != before.crop((0, r * 208, 1536, (r + 1) * 208)).tobytes()]
    assert changed == list(ROWS)
    (dest / "assembly.json").write_text(json.dumps({
        "changed_rows": changed, "shared_scale": scale, "baseline": baseline,
        "frame_orders_zero_based": {"walk": WALK, "gestures": GESTURE},
    }, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
