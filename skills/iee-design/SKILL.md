---
name: iee-design
description: Define and refine the visual direction of an original Rive scene, component, character, or interactive graphic before or during authoring.
---

# Design a Rive work

Establish a short design brief from the user's purpose, audience, content, target sizes, and any supplied references. Choose whether the work is a control, character, illustration, display, or small scene; that choice changes how much information and interaction one artboard should carry. Record the intended focal point, shape language, palette, typography, composition, and motion character. Preserve supplied brand assets and direction; do not invent claims or realistic content to fill space.

Choose the scene structure from the content. Use artboards for distinct scenes, components for repeated visual parts, and layouts for elements that must resize or reflow. Prefer native shapes, text, fills, strokes, clipping, and other Rive objects for editable graphics. Use imported raster, font, and audio assets when they serve the design, while keeping their dimensions and output cost proportionate.

Build in visible passes: overall silhouette and major regions, then hierarchy and content, then detail and motion. Inspect a rendered frame after each meaningful pass. A Rive work must read at its authored rest pose and after the state machine starts; check both. Judge spacing, hierarchy, legibility, alignment, color, and whether each interaction state is recognizable without relying on motion alone. Capture narrow and wide sizes when responsive behavior matters. Remove details that obscure the focal action or make the scene harder to edit.

Use the [work-specific design checks](references/work-types.md) for controls, characters, displays, scenes, and procedural pieces. Apply only the checks that fit the user's work.

For scene primitives and assets, consult `rive docs drawing`, `rive docs text`, `rive docs assets`, and `rive docs transforms`. The [Editor fundamentals](https://rive.app/docs/editor/fundamentals/overview) explain the same concepts in the desktop workflow. Route implementation details to `iee-rml` or `iee-mcp`, and motion design to `iee-motion`.
