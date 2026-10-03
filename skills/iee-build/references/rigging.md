# Rig deformable artwork

Choose the control that fits the intended motion. Use bones and weighted meshes for bending, constraints for relationships or inverse kinematics, joysticks for reusable pose control, and solos for discrete alternatives such as skins or drawn frames. Keep the rig understandable from its hierarchy and names.

For CLI syntax, read the relevant section of `rive docs rigging` and look up exact types with `rive schema`. In the Editor, inspect bone parents, mesh vertices and weights, constraint targets, and control channels through MCP. Keep the neutral pose recoverable before changing a rig. Rigging has multiple linked objects that can compile while deforming incorrectly.

Test extreme and intermediate poses, not only the neutral pose. Look for collapsing joints, pinched weights, unwanted stretching, overlapping shapes, and conflicting joystick channels. Render or preview the full motion and check the exported scene at the intended size. Keep repeated geometry and heavy deformation proportionate to the visual result.

Use [motion reference](motion.md) for timing and [state-machines reference](state-machines.md) when the pose changes through interaction.
