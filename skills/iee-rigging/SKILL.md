---
name: iee-rigging
description: Rig and animate Rive characters or deformable artwork using bones, meshes, constraints, joysticks, and solos.
---

# Rig deformable artwork

Choose the control that fits the intended motion. Use bones and weighted meshes for bending, constraints for relationships or inverse kinematics, joysticks for reusable pose control, and solos for discrete alternatives such as skins or drawn frames. Keep the rig understandable from its hierarchy and names.

Read `rive docs rigging` for RML authoring, or the [bones](https://rive.app/docs/editor/manipulating-shapes/bones), [meshes](https://rive.app/docs/editor/manipulating-shapes/meshes), and [constraints](https://rive.app/docs/editor/constraints/constraints-overview) guides when working in the Editor. Look up exact RML types and references with `rive schema`; rigging has multiple linked objects that can compile while deforming incorrectly.

Test extreme and intermediate poses, not only the neutral pose. Look for collapsing joints, pinched weights, unwanted stretching, overlapping shapes, and conflicting joystick channels. Render or preview the full motion and check the exported scene at the intended size. Keep repeated geometry and heavy deformation proportionate to the visual result.

Use `iee-motion` for timing and `iee-state-machines` when the pose changes through interaction.
