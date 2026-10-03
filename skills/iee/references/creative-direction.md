# Design a Rive work

Translate the brief into visible decisions that can be judged in a rendered scene. Preserve supplied references, brand assets, content, and user preferences. Keep technical implementation details out of the viewer's experience.

## Define the visual target

Identify the purpose, audience, content, target sizes, and interaction. Infer these from the request and existing project; ask only for a choice that materially changes the outcome.

Record a short direction: focal point, silhouette/shape language, palette, typography when relevant, composition, and motion character. Tie each major choice to the work. “A compact status control readable at 32 px, with a distinct active silhouette” guides authoring better than “make it premium.”

When a reference is supplied, inspect its proportions, negative space, overlap, contrast, and key poses. Distinguish requested fidelity from elements open to interpretation. When no reference exists, choose a coherent direction suited to the brief and make assumptions visible. Do not invent brands, claims, testimonials, or realistic content to fill the scene.

Turn the direction into a few concrete decisions before final geometry: the dominant mass and counterweight, the contour character, the strongest value contrast, and how the main action changes the pose. A character might be recognized by a broad upper silhouette and a tucked lower body; a control by a stable outline and a clearly moving indicator. Choose decisions that belong to this brief, not a stock recipe.

For an unfamiliar or ambiguous visual problem, compare rough alternatives cheaply before detailing one. Vary a meaningful decision such as proportion or staging, rather than only swapping colors. Do this within the authorized task; do not require the user to approve every sketch. Skip exploration when an existing direction or supplied reference already resolves the choice.

## Build a readable first pass

Choose artboards for distinct scenes, components for actual reuse, and layouts for reflow. Establish parent/child and property ownership with `iee-build` before substantial authoring. Use native editable shapes, paths, text, paints, and clipping when they fit; use raster/font/audio assets for a deliberate visual or content need.

Build the overall silhouette and major regions before detail. Render at the intended size. Compare the focal point, balance, proportions, and negative space with the direction. Correct the large relationships before adding highlights or decoration.

Then add content and detail within that structure. Preserve independently animatable parts and useful names. Avoid solving a structural problem by flattening artwork.

Build contours around changes in direction and curvature. Add vertices because the contour needs them; extra points make editing and deformation harder. Inspect unintended corners, tangent breaks, uneven stroke weight, and tiny gaps at joins at both authored and actual display size. Check the unadorned silhouette before relying on interior lines or a glow to establish identity. These are diagnosis tools, not a ban on deliberate roughness, sharp corners, or asymmetry.

Treat negative space and overlap as designed shapes. Keep important facial features, labels, or controls from merging into nearby contours. Decide which parts are in front and preserve that relationship through the intended poses. Add depth only when it clarifies form or staging; align highlights and shadows with the chosen lighting logic.

## Design states as part of the artwork

For interactive work, define how rest, activation, completion, and return read. Include disabled, empty, or error states only when the work needs them. Distinguish important states through more than motion alone.

Inspect the authored rest pose and first advanced pose; a state machine can immediately change the composition. For responsive work, compare meaningful sizes and content extremes. For characters, check expressive poses and transitions, not just a polished neutral frame.

Use [work-specific checks](work-types.md) for the relevant kind of work. State a concrete visual defect and revise it; “add polish” is not an actionable review. Stop optional refinement when the brief is satisfied and remaining defects are resolved.

## Compare, correct, and stop

Evaluate the rendered result in this order: overall reading, proportions and composition, state clarity, then edge/detail quality. When matching a reference, compare at the same visible scale and state. Identify the largest discrepancy and change the geometry, spacing, or pose that causes it; decorative detail cannot compensate for a wrong silhouette.

Keep the acceptance boundary explicit. Meeting a simple brief can produce a deliberately simple artifact. A claim of professional polish needs a relevant visual standard and review of its actual delivery context. Do not infer broad artistic capability from one successful illustration. If missing information prevents a meaningful comparison, state the assumption instead of inventing a brand standard.

Use `iee-build` for the needed authoring reference and `iee-review` for final evidence. Retrieve technical drawing/text/assets/transforms docs only for the construct being authored.
