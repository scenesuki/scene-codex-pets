Create one horizontal animation strip for Codex pet `scene-new-terrain`, state `running-right`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 8 full-body frames in one left-to-right row on flat pure magenta #FF00FF. Treat the row as 8 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Arknights Scene (稀音) in the VITAFIELD/Rewilder New Terrain (新地形) outfit, faithful infrastructure SD chibi proportions. Cream-white shoulder-length tousled hair with cool gray-blue underlayers, golden sleepy eyes, and a brown field cap with a small gold flower/compass emblem. Oversized olive-green outdoor poncho with broad sleeves, charcoal shoulder panels, white-gray geometric stripe bands near the hem, and a bold mustard-yellow lower border; white shirt and dark navy neck scarf underneath. Compact wood-brown camera hangs securely at the center chest as one connected prop. Dark blue utility shorts with a tan anatomical-left cargo pouch. Strong asymmetry: anatomical-right leg is mostly bare with a short dark navy thigh band/short sock area, while anatomical-left leg wears a full dark charcoal-gray thigh-high stocking with a diagonal darker panel. Matching tan-brown lace-up hiking boots. Calm reserved expression. Single human character only; no rover, tent, crates, birds, animals, grill, chair, grass, sky, scenery, detached camera, straps, or floating decorations. Preserve anatomical left/right, legwear asymmetry, cargo pouch side, camera attachment, and clothing motifs; never mirror the outfit.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Faithful Arknights infrastructure SD chibi, head about half body height, compact tiny body, restrained sleepy expression, clean polished 2D anime sprite rendering, not pixel art. Keep the geometric hem bands, yellow border, chest camera, cap emblem, and asymmetric legwear simplified but unmistakable at pet scale..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Dragging-right loop: show directional movement to the right through body and limb poses only.

State requirements:
- Show directional drag movement to the right through body, limb, and prop movement only.
- The row must unmistakably face and travel right.
- The movement cadence must alternate visibly across the 8 frames instead of repeating one nearly static stride.
- Do not draw speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.
