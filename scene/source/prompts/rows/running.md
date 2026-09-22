Create one horizontal animation strip for Codex pet `scene`, state `running`.

Use the attached canonical base for identity. Use the attached layout guide only for slot count, spacing, centering, and padding; do not draw the guide.

Output exactly 6 full-body frames in one left-to-right row on flat pure cyan #00FFFF. Treat the row as 6 invisible equal-width slots: one centered complete pose per slot, evenly spaced, with no overlap, clipping, empty slots, labels, or borders.

Identity: same pet in every frame: Arknights Scene (稀音), original outfit, faithful base-building chibi proportions. Cream white bob, small side ponytail and flower hairclip on character left, golden sleepy eyes. White coat with vivid lime lining, beige vest, red tie, black skirt, asymmetric stockings (black thigh-high on character left leg), black boots with lime trim, olive shoulder camera bag at character left hip, camera attached by neck strap. Single human character only, no separate rover. Calm reserved photographer. Preserve anatomical left/right for all poses; do not mirror asymmetric costume.. Preserve silhouette, face, proportions, markings, palette, material, style, and props.
Style: Pet-safe sprite: compact full-body mascot, readable in a 192x208 cell, clear silhouette, simple face, stable palette/materials, and crisp edges for chroma-key extraction. Style `auto`: Infer the most appropriate pet-safe style from the user request and reference images, then keep that exact style consistent across every row. User style notes: Faithful Arknights infrastructure SD chibi, large head about half body height, tiny body, restrained sleepy expression, clean detailed 2D anime sprite rendering, not pixel art..
Animation continuity: keep apparent pet scale and baseline stable within the row unless the state itself intentionally changes vertical position, such as `jumping`. Move the pose within the slot instead of redrawing the pet larger or smaller frame to frame.

State action: Working loop: focused active-task processing, thinking, typing, scanning, or effortful concentration; not literal foot-running, jogging, sprinting, treadmill motion, raised knees, long steps, pumping arms, or directional travel.

State requirements:
- Show the pet actively working or processing, as if running a task: focused posture, busy hands or paws, purposeful bobbing, thinking motion, tool or prop motion only if already part of the pet identity, or other non-locomotion activity.
- Do not show literal foot-running, jogging, sprinting, treadmill motion, raised knees, long steps, pumping arms, directional travel, speed lines, dust clouds, floor shadows, motion trails, or detached motion effects.

Clean extraction: crisp opaque edges, safe padding, no scenery, text, guide marks, checkerboard, shadows, glows, motion blur, speed lines, dust, detached effects, stray pixels, or chroma-key colors inside the pet.

Scene-specific action: feet remain planted, gently adjust the existing camera controls with both hands while looking down attentively; continuous small finger, wrist and head changes, no photography flash.
