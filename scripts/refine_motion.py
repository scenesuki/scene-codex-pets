"""Build a reviewable motion pass from an existing, unmodified pet atlas."""

import argparse
from hashlib import sha256
import json
from pathlib import Path
import shutil
import subprocess
import sys

from PIL import Image


STATES = ("idle", "running-right", "running-left", "waving", "jumping",
          "failed", "waiting", "running", "review")
ORDERS = {
    "scene": {4: (0, 1, 1, 3, 0), 6: (0, 1, 2, 3, 3, 4),
              7: (0, 1, 2, 2, 4, 5), 8: (0, 1, 4, 4, 1, 0)},
    "scene-biezhi": {4: (0, 1, 1, 3, 0), 6: (0, 1, 1, 3, 4, 4),
                     7: (0, 1, 2, 3, 3, 5), 8: (0, 1, 3, 3, 4, 0)},
    "scene-new-terrain": {4: (0, 1, 1, 3, 0), 5: (0, 1, 2, 2, 2, 6, 7, 0),
                          6: (0, 1, 1, 3, 3, 0), 7: (0, 1, 2, 2, 3, 5),
                          8: (0, 1, 3, 3, 1, 0)},
}


def cell(atlas, row, column):
    x, y = 192 * column, 208 * row
    return atlas.crop((x, y, x + 192, y + 208))


def refine(frame, stride):
    # Keep ground contact fixed. Make room for the face above the shoulders.
    anchors = [(0, 0, 1), (8, 8, 1.02), (48, 45, 1.07),
               (88, 82, 1.06), (112, 107, 1.02), (145, 142, 1),
               (171, 169, stride), (203, 203, stride), (208, 208, stride)]
    mesh = []
    for (top, source_top, top_scale), (bottom, source_bottom, bottom_scale) in zip(anchors, anchors[1:]):
        def bounds(scale):
            return 96 - 96 / scale, 96 + 96 / scale

        left_top, right_top = bounds(top_scale)
        left_bottom, right_bottom = bounds(bottom_scale)
        mesh.append(((0, top, 192, bottom), (left_top, source_top, left_bottom, source_bottom,
                                             right_bottom, source_bottom, right_top, source_top)))
    result = frame.transform(frame.size, Image.Transform.MESH, mesh, Image.Resampling.BICUBIC)
    # Strip interpolated RGB from fully transparent pixels.
    alpha = result.getchannel("A")
    result.paste((0, 0, 0, 0), mask=alpha.point(lambda value: 255 if value == 0 else 0))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--skill-scripts", required=True, type=Path)
    args = parser.parse_args()
    sys.path.insert(0, str(args.skill_scripts))
    from render_animation_previews import ROW_DURATIONS, save_preview

    source = args.project
    output = args.output
    old = Image.open(source / "spritesheet.webp").convert("RGBA")
    assert old.size == (1536, 2288)
    atlas = Image.new("RGBA", old.size)
    orders = ORDERS[source.name]
    stride = {"scene": .92, "scene-biezhi": .81, "scene-new-terrain": .85}[source.name]
    occupied = 0
    for row in range(11):
        for col in range(8):
            original = cell(old, row, col)
            if not original.getbbox():
                continue
            order = orders.get(row, ())
            frame = cell(old, row, order[col]) if col < len(order) else original
            adjusted = refine(frame, stride if row in (1, 2) else 1)
            assert adjusted.getbbox(), (row, col)
            assert not any(adjusted.getpixel(point)[3] for point in ((0, 0), (0, 207), (191, 0), (191, 207)))
            atlas.paste(adjusted, (col * 192, row * 208))
            occupied += 1

    output.mkdir(parents=True, exist_ok=True)
    sheet = output / "spritesheet.webp"
    atlas.save(sheet, lossless=True, exact=True, method=6)
    assert Image.open(sheet).convert("RGBA").tobytes() == atlas.tobytes()
    assert all(bool(cell(atlas, r, c).getbbox()) == bool(cell(old, r, c).getbbox())
               for r in range(11) for c in range(8))
    shutil.copy2(source / "pet.json", output / "pet.json")
    for row, state in enumerate(STATES):
        durations = ROW_DURATIONS[state]
        frames = [cell(atlas, row, c) for c in range(len(durations))]
        save_preview(frames, durations, output / "preview" / f"{state}.gif")
        if row in orders or row in (1, 2):
            # Compare at desktop scale with the same timeline for both versions.
            small = []
            for c, frame in enumerate(frames):
                canvas = Image.new("RGB", (192, 100), "#242832")
                for x, sprite in ((4, cell(old, row, c)), (100, frame)):
                    sprite = sprite.resize((88, 96), Image.Resampling.LANCZOS)
                    canvas.paste(sprite, (x, 2), sprite)
                small.append(canvas)
            save_preview(small, durations, output / "compare" / f"{state}.gif")

    key = json.loads((source / "source/pet_request.json").read_text(encoding="utf-8"))["chroma_key"]["hex"]
    for script, options in (
        ("validate_atlas.py", ["--require-v2", "--chroma-key", key, "--json-out", str(output / "validation.json")]),
        ("make_contact_sheet.py", ["--output", str(output / "preview/contact-sheet.png")]),
        ("make_direction_qa_sheet.py", ["--output", str(output / "preview/look-directions.png")]),
    ):
        subprocess.run([sys.executable, str(args.skill_scripts / script), str(sheet), *options], check=True)
    (output / "motion-refinement.json").write_text(json.dumps({
        "source_rgba_sha256": sha256(old.tobytes()).hexdigest(),
        "output_rgba_sha256": sha256(atlas.tobytes()).hexdigest(),
        "occupied_cells": occupied,
        "stride_scale": stride,
        "frame_orders_zero_based": {STATES[r]: order for r, order in orders.items()},
    }, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
