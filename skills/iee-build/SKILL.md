---
name: iee-build
description: Use when building or editing a Rive artifact from a clear brief, including RML projects, open Editor files, animation, layout, bindings, rigging, and scripts.
---

# Build the Rive artifact

**Principle:** change the owner of the result, then observe what it produced.

## Establish source and ownership

Identify the artifact and available tools. Use the CLI for a local RML project and connected MCP for an open Editor document. Discover exact CLI syntax from installed help/docs/schema and Editor operations from live tool schemas. Editor work does not require a CLI installation.

Before mutation, inspect the affected artboard/component tree, coordinates, draw order, assets, and property owner. Distinguish a base value from animation, layout, bindings, or scripts that overwrite it. Use the [scene model](references/scene-model.md) only for concepts the task needs.

Preserve recoverable source before builds that assign IDs, broad changes, imports, or tool handoffs. Store CLI backups outside discovered source roots, or with non-source extensions: an in-project backup ending in `.rml` can compile twice and cause duplicate IDs. Re-read after concurrent user/tool edits. Preserve stable IDs, names, interfaces, and unrelated work. For `.rev` imports, keep the original and use a new destination.

Push replaces linked remote content; pull overwrites local source. Identify both sides and preserve pending edits before either. Remote writes, signing, and publication require a requested outcome and destination; reuse existing authorization.

## Read only the reference needed now

| Work | Reference |
| --- | --- |
| CLI discovery and version-specific syntax | [CLI workflow](references/cli-docs.md); [topic index](references/cli-topics.md) only if needed |
| Editable markup and wiring | [RML](references/rml.md) |
| Connected Editor operations | [Editor](references/editor.md) |
| Timing, easing, loops | [Motion](references/motion.md) |
| Inputs, states, transitions | [State machines](references/state-machines.md) |
| View Models and binding | [Data](references/data-binding.md) |
| Reflow and scrolling | [Layouts](references/layouts.md) |
| Deformation and pose controls | [Rigging](references/rigging.md) |
| Computed behavior | [Luau](references/luau.md) or [AnimaScript](references/animascript.md), matching the project |
| Effects requiring a shader | [WGSL](references/wgsl.md) |

Do not read the whole table's references. Principles and failure modes are written here; exact API facts come from the installed version. Use web docs only for a specific unresolved fact, checking compatibility.

## Implement and inspect

Make the smallest coherent change in its owner. For new work, build structure and silhouette before detail. Prefer editable native objects for fixed artwork and scripts for computation. Preserve the project's scripting lane.

After a meaningful pass, compile or run Editor diagnostics, inspect the changed relationships, and render/preview the affected state. For headless review, use one-shot captures; the bare CLI project command opens a persistent window. Set the command's project working directory and explicit output paths so evidence stays with its artifact.

If behavior is wrong, use `iee-debug` before adding more fixes. When the intended result is present, use `iee-review` and carry forward current evidence. A missing tool limits the claims you can make; report the gap and continue work that does not depend on it.
