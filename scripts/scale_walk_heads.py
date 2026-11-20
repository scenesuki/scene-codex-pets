"""Scale right- and left-walking heads about the collar; preserve the body."""

import argparse
from pathlib import Path
import sys

from PIL import Image, ImageDraw


def resize_head(frame, scale):
    # Taper back to the original pixels at the collar to avoid a hard seam.
    collar = 106
    neck = frame.getchannel("A").crop((0, 99, 192, 104)).getbbox()
    assert neck is not None
    center = (neck[0] + neck[2]) / 2

    def inverse(y):
        source_scale = scale if y <= 78 else scale + (1 - scale) * (y - 78) / (collar - 78)
        return center - center / source_scale, center + (192-center) / source_scale, collar + (y-collar) / source_scale

    mesh = []
    bands = (0, 78, 85, 92, 99, collar)
    for y1, y2 in zip(bands,bands[1:]):
        l1, r1, source1 = inverse(y1)
        l2, r2, source2 = inverse(y2)
        mesh.append(((0,y1,192,y2), (l1,source1,l2,source2,r2,source2,r1,source1)))
    patch = frame.transform((192,collar), Image.Transform.MESH, mesh, Image.Resampling.BICUBIC)
    transparent = patch.getchannel("A").point(lambda a: 255 if not a else 0)
    patch.paste((0,0,0,0), mask=transparent)
    result = frame.copy()
    result.paste(patch, (0,0))
    assert result.crop((0,collar,192,208)).tobytes() == frame.crop((0,collar,192,208)).tobytes()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("atlas", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--scale", type=float, required=True)
    parser.add_argument("--skill-scripts", type=Path, required=True)
    args = parser.parse_args()
    if not .90 <= args.scale < 1:
        parser.error("--scale must be between 0.90 and 1, excluding 1")
    sys.path.insert(0,str(args.skill_scripts))
    from render_animation_previews import ROW_DURATIONS, save_preview

    original = Image.open(args.atlas).convert("RGBA")
    assert original.size == (1536,2288)
    atlas = original.copy()
    out = args.output
    out.mkdir(parents=True,exist_ok=True)
    comparison = Image.new("RGB",(768,880),"#313a45")
    draw = ImageDraw.Draw(comparison)
    for row, state in enumerate(("running-right","running-left"), start=1):
        frames = []
        for col in range(8):
            x, y = col*192, row*208
            before = original.crop((x,y,x+192,y+208))
            after = resize_head(before,args.scale)
            atlas.paste(after,(x,y))
            frames.append(after)
            if col in (0,1,4,6):
                slot = (0,1,4,6).index(col)
                for version, frame in enumerate((before,after)):
                    yout = ((row-1)*2+version)*220
                    if slot == 0:
                        draw.text((5,yout+3),state+(" adjusted" if version else " current"),fill="white")
                    comparison.paste(frame,(slot*192,yout+10),frame)
        save_preview(frames,ROW_DURATIONS[state],out/f"{state}.gif")
    sheet = out/"spritesheet.webp"
    atlas.save(sheet,lossless=True,exact=True,method=6)
    encoded = Image.open(sheet).convert("RGBA")
    assert encoded.tobytes() == atlas.tobytes()
    for row in range(11):
        box = (0,row*208+(106 if row in (1,2) else 0),1536,(row+1)*208)
        assert encoded.crop(box).tobytes() == original.crop(box).tobytes()
    comparison.save(out/"head-size-comparison.png")


if __name__ == "__main__":
    main()
