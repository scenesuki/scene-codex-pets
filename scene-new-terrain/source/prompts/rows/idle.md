Create one horizontal animation strip for Codex pet `scene-new-terrain`, state `idle`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure magenta #FF00FF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Arknights Scene (稀音) in the VITAFIELD/Rewilder New Terrain (新地形) outfit, faithful infrastructure SD chibi proportions. Cream-white shoulder-length tousled hair with cool gray-blue underlayers, golden sleepy eyes, and a brown field cap with a small gold flower/compass emblem. Oversized olive-green outdoor poncho with broad sleeves, charcoal shoulder panels, white-gray geometric stripe bands near the hem, and a bold mustard-yellow lower border; white shirt and dark navy neck scarf underneath. Compact wood-brown camera hangs securely at the center chest as one connected prop. Dark blue utility shorts with a tan anatomical-left cargo pouch. Strong asymmetry: anatomical-right leg is mostly bare with a short dark navy thigh band/short sock area, while anatomical-left leg wears a full dark charcoal-gray thigh-high stocking with a diagonal darker panel. Matching tan-brown lace-up hiking boots. Calm reserved expression. Single human character only; no rover, tent, crates, birds, animals, grill, chair, grass, sky, scenery, detached camera, straps, or floating decorations. Preserve anatomical left/right, legwear asymmetry, cargo pouch side, camera attachment, and clothing motifs; never mirror the outfit.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Faithful Arknights infrastructure SD chibi, head about half body height, compact tiny body, restrained sleepy expression, clean polished 2D anime sprite rendering, not pixel art. Keep the geometric hem bands, yellow border, chest camera, cap emblem, and asymmetric legwear simplified but unmistakable at pet scale..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Calm low-distraction resting loop: subtle breathing, tiny blink, slight head/body bob, and only quiet persona-preserving motion.

State requirements:
- CRITICAL: idle is the low-distraction baseline state and the first frame is also used as the reduced-motion static pet.
- Use only subtle idle motion: gentle breathing, a tiny blink, a slight head or body bob, a very small material sway, or another quiet motion that fits the pet persona.
- Keep the pet essentially in the same pose, facing direction, silhouette, markings, palette, and prop state across all 6 frames.
- Idle variation must stay calm but still read as animation; do not repeat effectively identical copies across the loop.
- Do not show waving, walking, running, jumping, talking, working, reviewing, emotional reactions, large gestures, item interactions, or new props.
- Feet, base, body, or object anchor should remain planted or nearly planted.
- The first and last frames should be very close visually so the loop feels calm and does not pop.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
