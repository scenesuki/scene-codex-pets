"""Assemble an imagegen hover strip into row 4, preserving all other atlas pixels."""

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import statistics
import subprocess
import sys

from PIL import Image


def save_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--skill-scripts", required=True, type=Path)
    args = parser.parse_args()
    project = args.project.resolve()
    source = project / "source"
    sys.path.insert(0, str(args.skill_scripts))
    from extract_strip_frames import extract_state, parse_hex_color
    from despill_chroma_edges import decontaminate_image, save_image
    from render_animation_previews import save_preview, ROW_DURATIONS

    request = json.loads((source / "pet_request.json").read_text(encoding="utf-8"))
    key = request["chroma_key"]["hex"]
    old = Image.open(project / "spritesheet.webp").convert("RGBA")
    assert old.size == (1536, 2288)
    old_hash = hashlib.sha256(old.tobytes()).hexdigest()
    idle_boxes = [old.crop((i * 192, 0, (i + 1) * 192, 208)).getbbox() for i in range(6)]
    target_height = round(statistics.median(b[3] - b[1] for b in idle_boxes))
    baseline = round(statistics.median(b[3] for b in idle_boxes))
    qa = source / "qa" / "hover-calm"
    qa.mkdir(parents=True, exist_ok=True)
    result = extract_state(source / "decoded" / "hover-calm.png", "jumping",
                           qa / "extracted", parse_hex_color(key), 96, "stable-slots")
    frames = [Image.open(path).convert("RGBA") for path in result["frames"]]
    boxes = [frame.getbbox() for frame in frames]
    scale = target_height / statistics.median(b[3] - b[1] for b in boxes)
    assert max((b[2] - b[0]) * scale for b in boxes) < 182, "hover sprite too wide"
    row = Image.new("RGBA", (1536, 208))
    for i, (frame, bbox) in enumerate(zip(frames, boxes)):
        sprite = frame.crop(bbox)
        sprite = sprite.resize((round(sprite.width * scale), round(sprite.height * scale)), Image.Resampling.LANCZOS)
        row.alpha_composite(sprite, (i * 192 + (192 - sprite.width) // 2, baseline - sprite.height))
    cleaned, cleanup = decontaminate_image(row, chroma_key=parse_hex_color(key), strength=1,
                                          edge_radius=5, spill_tolerance=.15, minimum_saturation=.1)
    save_json(qa / "chroma-despill.json", {"ok": True, **cleanup})
    atlas = old.copy()
    atlas.paste(cleaned, (0, 4 * 208))
    for r in range(11):
        if r != 4:
            region = (0, r * 208, 1536, (r + 1) * 208)
            assert old.crop(region).tobytes() == atlas.crop(region).tobytes()
    save_image(atlas, project / "spritesheet.webp")
    decoded_check = Image.open(project / "spritesheet.webp").convert("RGBA")
    assert decoded_check.tobytes() == atlas.tobytes(), "WebP roundtrip changed pixels"
    save_image(atlas, source / "final" / "spritesheet-extended.png")
    shutil.copy2(project / "spritesheet.webp", source / "final" / "spritesheet-extended.webp")
    standard = atlas.crop((0, 0, 1536, 1872))
    standard.paste(Image.new("RGBA", (192, 208)), (6 * 192, 0))
    save_image(standard, source / "final" / "spritesheet.png")
    save_image(standard, source / "final" / "spritesheet.webp")
    frame_dir = source / "frames" / "jumping"
    final_frames = []
    for i in range(5):
        frame = atlas.crop((i * 192, 832, (i + 1) * 192, 1040))
        frame.save(frame_dir / f"{i:02d}.png")
        final_frames.append(frame)
    final_boxes = [frame.getbbox() for frame in final_frames]
    assert len({box[3] for box in final_boxes}) == 1, "feet baseline must stay fixed"
    assert len({hashlib.sha256(frame.tobytes()).hexdigest() for frame in final_frames}) >= 3
    final_frames[0].save(qa / "first-frame.png")
    idle = old.crop((0, 0, 192, 208))
    comparison = Image.new("RGBA", (6 * 192, 208))
    comparison.paste(idle, (0, 0))
    for i, frame in enumerate(final_frames):
        comparison.paste(frame, ((i + 1) * 192, 0))
    comparison.save(qa / "idle-and-hover.png")
    save_preview(final_frames, ROW_DURATIONS["jumping"], project / "preview" / "hover-calm.gif")
    shutil.copy2(project / "preview" / "hover-calm.gif", source / "qa" / "previews" / "jumping.gif")
    shutil.copy2(source / "decoded" / "hover-calm.png", source / "decoded" / "jumping.png")
    shutil.copy2(source / "prompts" / "rows" / "hover-calm.md", source / "prompts" / "rows" / "jumping.md")
    for row_spec in request["rows"]:
        if row_spec["state"] == "jumping":
            row_spec["purpose"] = "grounded quiet hover acknowledgement: blink and slight nod, no jumping"
    save_json(source / "pet_request.json", request)
    save_json(qa / "repair.json", {
        "date": "2026-10-10", "row": 4, "runtime_state": "jumping", "action": "calm hover acknowledgement",
        "frames": 5, "durations_ms": ROW_DURATIONS["jumping"], "baseline": baseline,
        "bounding_boxes": final_boxes, "before_rgba_sha256": old_hash,
        "after_rgba_sha256": hashlib.sha256(atlas.tobytes()).hexdigest(),
        "other_rows_pixel_identical": True, "webp_roundtrip_pixel_identical": True,
        "timing_note": "Native Codex row timing; personality adjustment is in poses, not runtime speed."
    })
    subprocess.run([sys.executable, str(args.skill_scripts / "validate_atlas.py"), str(project / "spritesheet.webp"),
                    "--require-v2", "--chroma-key", key, "--json-out", str(project / "validation.json")], check=True,
                   stdout=subprocess.DEVNULL)
    shutil.copy2(project / "validation.json", source / "final" / "validation-extended.json")
    for destination in [project / "preview" / "contact-sheet.png", source / "qa" / "contact-sheet-extended.png"]:
        subprocess.run([sys.executable, str(args.skill_scripts / "make_contact_sheet.py"), str(project / "spritesheet.webp"),
                        "--output", str(destination)], check=True, stdout=subprocess.DEVNULL)
    print(json.dumps({"project": project.name, "ok": True, "baseline": baseline, "height": target_height}))


if __name__ == "__main__":
    main()
