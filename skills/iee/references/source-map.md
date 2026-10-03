# Rive source map

Use this map to find a version-matched reference. Read only the topic needed for the current work. `rive docs --list` shows what the installed CLI actually provides; a newer or older CLI may differ from this map. Use `rive schema --search <term>` and `rive schema <Type>` for exact RML type and property names.

| Authoring question | CLI reference | Editor or public docs fallback |
| --- | --- | --- |
| RML document, IDs, nesting, and keyframes | `rive docs format`, `rive docs gotchas` | [RML overview](https://rive.app/docs/runtimes/advanced-topic/rml) |
| First complete scene | `rive docs skeleton`, `rive samples` | [Rive CLI](https://rive.app/docs/cli/overview) |
| Shapes, paint, transforms, text | `rive docs drawing`, `rive docs transforms`, `rive docs text` | [Editor fundamentals](https://rive.app/docs/editor/fundamentals/overview) |
| Layout and resizing | `rive docs layout` | [Editor layouts](https://rive.app/docs/editor/layouts/layouts-overview) |
| View Models and binding | `rive docs data` | [Data Binding](https://rive.app/docs/editor/data-binding/overview) |
| Interaction and focus | `rive docs state-machines`, `rive docs focus`, `rive docs semantics` | [State Machines](https://rive.app/docs/editor/state-machine/state-machine) |
| Animation and easing | `rive docs easing` | [Animate Mode](https://rive.app/docs/editor/animate-mode/animate-mode-overview) |
| Bones, meshes, constraints | `rive docs rigging` | [Bones](https://rive.app/docs/editor/manipulating-shapes/bones) |
| Luau scripting | `rive docs luau/protocols`, `rive docs luau/api/<topic>` | [Scripting](https://rive.app/docs/scripting/getting-started) |
| AnimaScript scripting | `rive docs animascript/protocols`, `rive docs animascript/api/<module>` | Use the installed CLI reference; check feature availability in that version |
| Shader effects | CLI GPU API for the chosen script language | [WGSL Shaders](https://rive.app/docs/scripting/wgsl-shaders) |
| Project settings and output | `rive docs project/rive-yaml`, `rive docs publishing` | [CLI project config](https://rive.app/docs/cli/reference/project-config) |
| Build and behavior checks | `rive docs workflow`, `rive docs gotchas` | [CLI examples](https://rive.app/docs/cli/examples) |
| Desktop Editor automation | Discover connected MCP tools | [Rive MCP](https://rive.app/docs/editor/ai/mcp) |

CLI documentation and schema are technical references. IEE skills supply the creative workflow and acceptance criteria. Do not copy the CLI reference into a skill, and do not use an older cached property name when the installed CLI reports a different one.
