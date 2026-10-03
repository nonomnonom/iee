# Rive CLI documentation workflow

The installed Rive CLI is the documentation source for the CLI and RML version in use. This file ships with the plugin; it does not depend on a sibling repository or a fixed machine path.

1. Locate the project's CLI and inspect its version and help. If `rive` is absent from PATH, check the documented local install, commonly `~/.rive/bin/rive` (`rive.exe` on Windows), before declaring it missing. Use the resolved executable consistently. Run `rive docs` to discover its bundled documentation interface. Follow the CLI's own help or topic listing for the exact topic syntax; do not guess a topic identifier, flag, or URL.
2. Find the smallest relevant topic by concept. Read the conceptual guidance, then the RML or command reference and examples for the construct you will use. Confirm required fields, nesting, defaults, supported versions, and output format.
3. If a topic is absent or its syntax differs from an example, use the installed version's help and diagnostics. State the gap. Only then consult official online Rive docs, and verify that the example applies to the installed CLI before using it.
4. Run the documented validation or build command and inspect the rendered scene. A successful parse proves syntax, not correct hierarchy, appearance, interaction, or export.

Reuse the version and topics already inspected in this session. A version change invalidates that assumption. Search within relevant docs rather than dumping the whole manual into context. CLI examples are technical references; adapt their visual and interaction choices to the user's brief.

For agent review, use a one-shot headless command such as `--screenshot`; the bare project command opens a persistent preview window. Use the live preview when the user needs it or a check requires it, and manage its lifetime explicitly. Publishing and push are remote operations, not preview commands. Confirm output files rather than relying only on a process exit code.

Keep captures, reports, test helpers, and backups outside the project. CLI 1.3.0 discovers assets recursively; script-only projects can bundle unfamiliar files as blobs, while RML projects can omit unreferenced assets. Discovery alone does not prove embedding. A `.bak` extension avoids parsing a second RML source but does not exclude that file from discovery. If evidence must live inside the project, configure `exclude` using installed `project/rive-yaml` docs and inspect the resulting asset list/output size. `excludeFromRev` governs backup content and is not a substitute for excluding accidental runtime assets.

| What the task needs | Concepts to locate through `rive docs` |
| --- | --- |
| Scene structure | artboards, components, groups, hierarchy, draw order, transforms, origin |
| Vector design | shapes, paths, vertices, fills, strokes, opacity, clipping, masks |
| Responsive UI | constraints, layouts, sizing, alignment, text behavior |
| Assets | image, SVG, font, audio, library or component references |
| Motion | design versus animate mode, timeline, keyframes, easing, draw-order animation |
| Interaction | state machines, states, transitions, inputs, listeners, events |
| Data | view models, instances, properties, binding, converters, lists |
| Delivery | runtime export, native backup, names exposed to runtimes, supported features, publishing |

If `rive docs` is unavailable, report that dependency clearly. Do not silently substitute a workspace-specific docs path. Work from the skill's conceptual guidance and available Editor inspection for safe analysis, but do not invent RML syntax or claim version-specific support.
