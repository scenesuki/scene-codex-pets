"""Register two edited heads while retaining existing walk bodies and timing."""

import argparse
import json
from pathlib import Path
import statistics
import sys

from PIL import Image, ImageChops, ImageDraw


def cell(atlas, row, col):
    return atlas.crop((col * 192, row * 208, (col + 1) * 192, (row + 1) * 208))


def join_head(body, replacement):
    """Find a low-difference collar seam without moving the destination body."""
    def score(y, dx, dy):
        previous = body.crop((40, y - 2, 152, y + 3)).convert("RGBa")
        new = replacement.crop((40-dx, y-2-dy, 152-dx, y+3-dy)).convert("RGBa")
        delta = ImageChops.difference(previous.convert("RGBA"), new.convert("RGBA"))
        alpha = delta.getchannel("A").histogram()
        errors = sum(i * count for i, count in enumerate(delta.convert("L").histogram()))
        return errors + sum(i * count * 2 for i, count in enumerate(alpha)) + (abs(dx)+abs(dy))*180

    _, seam, dx, dy = min((score(y, x, dy), y, x, dy)
                         for y in range(94, 106) for x in range(-6, 7) for dy in range(-4, 5))
    top = replacement.crop((-dx, -dy, 192-dx, seam-dy))
    frame = body.copy()
    frame.paste(top, (0, 0))
    assert frame.crop((0,seam,192,208)).tobytes()==body.crop((0,seam,192,208)).tobytes()
    return frame, {"seam_y": seam, "offset": [dx,dy]}


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
    source = remove_chroma_background(Image.open(args.strip).convert("RGBA"), (0,255,255), 96)
    groups = component_frame_groups(source, 2)
    if groups is None:
        raise ValueError("Expected distinct right- and left-walking references")
    poses = [component_group_image(source, group) for group in groups]
    poses = [im.crop(im.getbbox()) for im in poses]
    scale = min(197 / statistics.median(p.height for p in poses),
                199 / max(p.height for p in poses))
    out = args.output
    out.mkdir(parents=True, exist_ok=True)
    atlas = original.copy()
    comparisons = Image.new("RGB", (1152, 880), "#333e4a")
    draw = ImageDraw.Draw(comparisons)
    report = []
    for i, name in enumerate(("running-right", "running-left")):
        row = i+1
        posed = poses[i]
        sprite = posed.resize((round(posed.width*scale),round(posed.height*scale)),
                              Image.Resampling.LANCZOS)
        reference = Image.new("RGBA", (192,208))
        reference.paste(sprite, ((192-sprite.width)//2,203-sprite.height))
        reference, _ = decontaminate_image(reference, chroma_key=(0,255,255),
                                          strength=1, edge_radius=6, spill_tolerance=.25)
        frames = []
        for col in range(8):
            before = cell(original,row,col)
            after, decision = join_head(before, reference)
            assert after.crop((0,106,192,208)).tobytes()==before.crop((0,106,192,208)).tobytes()
            frames.append(after)
            atlas.paste(after,(192*col,208*row))
            report.append({"row":row,"column":col,**decision})
        for level in (0,1):
            y=(2*i+level)*220
            draw.text((4,y+4),name+(" after" if level else " before"),fill="white")
            for c,j in enumerate((0,1,2,3,4,6)):
                frame=frames[j] if level else cell(original,row,j)
                comparisons.paste(frame,(192*c,y+12),frame)
        save_preview(frames, ROW_DURATIONS[name], out / f"{name}.gif")
    atlas.save(out/"spritesheet.webp",lossless=True,exact=True,method=6)
    saved=Image.open(out/"spritesheet.webp").convert("RGBA")
    assert saved.tobytes()==atlas.tobytes()
    for row in range(11):
        if row not in (1,2):
            box=(0,208*row,1536,208*(row+1))
            assert saved.crop(box).tobytes()==original.crop(box).tobytes()
    comparisons.save(out/"angle-comparison.png")
    (out/"walk-head-angles.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")


if __name__ == "__main__":
    main()
