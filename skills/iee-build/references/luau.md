# Script Rive behavior with Luau

Use Luau for work computed at run time: procedural geometry, particles, simulation, custom layout behavior, path effects, converters, listener actions, and transition conditions. Keep text, ordinary controls, and fixed visual structure in RML or the Editor so designers can still edit them.

Use the installed `rive docs luau/protocols` and relevant `rive docs luau/api/<topic>` for exact hooks and API signatures. In an Editor-only session, inspect the existing script's protocol and the connected tools' scripting reference and diagnostics; identify a specific missing API fact before seeking another source. Return the protocol factory with the exact lifecycle hooks it defines. Type every function parameter and model fields that may start as `nil` explicitly; the CLI checks scripts in strict mode. Hook names are case sensitive and an unknown hook may be silently ignored.

Attach the script to the intended RML or Editor object and bind inputs deliberately. For CLI work, use `rive <dir> --verify` to check types and compilation, then `--test` for authored logic tests. In the Editor, use available compilation and diagnostics. Render or preview the attached scene to expose runtime errors and missing callbacks; `rive inspect` does not evaluate Luau. Confirm that the script affects the specific state or frame it was meant to change.

If the project uses `scripting: wasm` and `.as` sources, follow [animascript reference](animascript.md) instead of introducing a Luau file that needs a separate VM blob. For shader-driven rendering, also read [wgsl reference](wgsl.md).
