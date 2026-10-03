---
name: iee-luau
description: Write or repair Luau scripts for computed drawing, effects, simulation, interaction, converters, or tests in a Rive project.
---

# Script Rive behavior with Luau

Use Luau for work computed at run time: procedural geometry, particles, simulation, custom layout behavior, path effects, converters, listener actions, and transition conditions. Keep text, ordinary controls, and fixed visual structure in RML or the Editor so designers can still edit them.

Read `rive docs luau/protocols` and the relevant `rive docs luau/api/<topic>` before choosing a protocol or calling an API. Return the protocol factory with the exact lifecycle hooks it defines. Type every function parameter and model fields that may start as `nil` explicitly; the CLI checks scripts in strict mode. Hook names are case sensitive and an unknown hook may be silently ignored.

Attach the script to the intended RML or Editor object and bind inputs deliberately. Use `rive <dir> --verify` to check types and compilation. Then run `--test` for pure logic and render or preview the attached scene to expose runtime errors and missing callbacks; `rive inspect` does not evaluate Luau. Confirm that the script affects the specific state or frame it was meant to change.

If the project uses `scripting: wasm` and `.as` sources, follow `iee-animascript` instead of introducing a Luau file that needs a separate VM blob. For shader-driven rendering, also read `iee-wgsl`.
