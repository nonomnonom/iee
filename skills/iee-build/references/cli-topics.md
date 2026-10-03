# Find the relevant CLI topic

Use this only when the topic is not already known. The installed CLI is the syntax and API reference; IEE supplies the scene model, working decisions, and acceptance criteria directly in its skills. Read the relevant section, not every topic in this map.

`rive docs --list` lists the installed topics. `rive docs --search <term>` finds a concept or failure. `rive schema --search <term>` finds a type; `rive schema <Type>` returns its exact properties. Prefer installed help if a command or topic differs by version.

| Question | Local reference |
| --- | --- |
| RML document, IDs, nesting, keyframes | `rive docs format`; search `rive docs gotchas` for the current construct |
| First complete scene | `rive docs skeleton`, `rive samples` |
| Shapes, paint, transforms, text | `rive docs drawing`, `rive docs transforms`, `rive docs text` |
| Layout and resizing | `rive docs layout` |
| View Models and binding | `rive docs data` |
| Interaction, focus, accessibility | `rive docs state-machines`, `rive docs focus`, `rive docs semantics` |
| Animation and easing | `rive docs easing` |
| Bones, meshes, constraints | `rive docs rigging` |
| Luau | `rive docs luau/protocols`, relevant `rive docs luau/api/<topic>` |
| AnimaScript | `rive docs animascript/protocols`, relevant `rive docs animascript/api/<module>` |
| Shaders | GPU API topic for the chosen scripting language |
| Project settings and output | `rive docs project/rive-yaml`, `rive docs publishing` |
| Verification and silent failures | `rive docs workflow`, relevant `rive docs gotchas` section |
| Desktop Editor operations | Discover connected MCP tool schemas and inspect the document; use [Editor workflow](editor.md) |

For an Editor-only task, use the skills' direct guidance and the live server's capabilities. Do not install the CLI solely to read a concept already explained in a skill. If a specific capability or API fact remains unknown, state that gap and consult a version-compatible official source; web browsing is a fallback for that question, not the starting workflow.