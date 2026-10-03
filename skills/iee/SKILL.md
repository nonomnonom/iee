---
name: iee
description: Direct the creation and refinement of an original interactive Rive work using RML, Rive scripting, the CLI, or the Editor MCP. Use for Rive scene authoring, animation, and interaction design; skip runtime integration requests.
---

# Interactive Experience Engine

Create or refine an original Rive work from the user's visual and interaction brief. Decide what the viewer sees, what responds to input or data, and how motion communicates the change. For a small repair, preserve the existing direction. Keep the result coherent across artboards and states.

## Route the work

- Use `iee-design` to set the visual direction before substantial scene work.
- Use `iee-rml` for editable scene structure. Use `iee-luau` or `iee-animascript` for computed behavior. Use `iee-wgsl` for GPU effects.
- Use `iee-motion`, `iee-state-machines`, `iee-data-binding`, `iee-layouts`, or `iee-rigging` for the relevant craft problem.
- Use `iee-mcp` when editing an open file through the Rive desktop Editor. Use `iee-review` before delivery.

## Source of truth

Choose the authoring surface from the artifact: a local RML project uses the CLI; an open desktop Editor file can use MCP; a `.rev` can be imported into a new CLI project when text editing is needed. Preserve the user's existing source before crossing between surfaces. A CLI build can add generated IDs to RML, `rive pull` overwrites local source, and `rive push` replaces the linked Editor file's live content. Use push, pull, and publication only when the user requested that outcome.

In a CLI project, read the installed CLI's topic-specific `rive docs` page and `rive schema` for exact syntax and object properties. The installed version is more reliable than memorized examples or this plugin. Read `rive docs format` before unfamiliar RML; search `rive docs gotchas` for the feature or failure at hand. Load only the relevant reference. If the CLI is unavailable, follow the [official installation guide](https://rive.app/docs/cli/getting-started) when CLI authoring is needed; use the [official Rive documentation](https://rive.app/docs) for planning until it is available.

Use the [source map](references/source-map.md) when selecting a CLI topic or a fallback Editor page.

Use RML for fixed, editable scene structure. Add scripting where behavior or imagery is computed. Keep an existing project's scripting lane: Luau uses `.luau`; AnimaScript uses `.as` with `scripting: wasm`. The work is the Rive artifact, not a host application integration.

Review the actual result: compile it, inspect its resolved structure, render meaningful states, and exercise its input and data paths. Deliver the requested source project, Editor file, or export. Local `.riv` builds containing scripts are unsigned and may not run on web; publishing or an Editor `.rev` requires a Rive login. Report the artifact, the checks performed, and any remaining limitation.
