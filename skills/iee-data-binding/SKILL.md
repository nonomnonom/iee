---
name: iee-data-binding
description: Connect Rive View Models, instances, properties, converters, and scene bindings so data visibly drives the intended artwork.
---

# Bind data to the scene

Define the smallest View Model that expresses the scene's actual state. Name properties for their meaning to the work, bind an instance to the artboard, and connect each property to the specific target field it owns. Use converters only when a direct binding cannot express the transformation.

For RML, read `rive docs data` and `rive docs format`; discover target property keys with `rive schema <Type> --bindable`. Bind paths are references, not display labels. Confirm that the artboard's View Model instance matches the path used by its children. For Editor work, use the [data binding overview](https://rive.app/docs/editor/data-binding/overview) and inspect the created instances and bindings through MCP.

Run `rive inspect <dir> --summary` for binding problems, then exercise the binding with `--data=<path=value>` and render the result. Read the values back with `--data-dump=-` when the scene computes data. A misspelled `--data` path can leave the authored value in place without failing the build; a two-way bind can also overwrite an injected value. Confirm the value that actually landed and the expected visual change after advancing the scene.

For interaction-driven values, coordinate listener or state machine writes with `iee-state-machines`. For script-backed conversion, use `iee-luau` or `iee-animascript` according to the project's scripting mode.
