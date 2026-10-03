---
name: iee-animascript
description: Write or repair AnimaScript .as files for Rive projects configured to compile scripting to WebAssembly.
---

# Script Rive behavior with AnimaScript

Use this skill for `.as` sources in a Rive project with `scripting: wasm` in `rive.yaml`. Authoring requires filesystem and shell access and a Rive CLI version with AnimaScript support. AnimaScript uses TypeScript-like syntax with WebAssembly types; it is a distinct scripting lane from Luau. Do not translate Luau examples mechanically.

Read `rive docs animascript/protocols` and the relevant `rive docs animascript/api/<module>` from the installed CLI. Export a class extending the protocol base for the intended role, such as `Layout`, `Node`, `PathEffect`, `Converter`, or `Tests`. Mark lifecycle hooks `override` and implement each required abstract hook. Check numeric widths and conversions, nullable class references, and module imports against the API reference.

Keep editable scene structure in RML and attach the scripted part through the matching scene object. Run `rive <dir> --verify` after small changes. A successful compile does not run the script: render a frame or drive the interaction to reveal traps, missing attachments, or incorrect output. Use CLI tests for logic that can be tested independently.

Consult `iee-rml` for scene wiring and `iee-review` for visual and behavioral verification.
