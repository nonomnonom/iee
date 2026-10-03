---
name: iee-rml
description: Author or revise editable Rive scenes in Rive Markup Language, including artboards, drawing, animation, components, and references.
---

# Author RML scenes

Use RML for fixed scene structure: artboards, shapes, text, layouts, view models, animations, and state machines. CLI authoring requires filesystem and shell access and a supported Rive CLI installation. Keep calculated imagery or behavior in a small attached script. Preserve existing artboards, IDs, and relationships when revising a scene.

Before writing unfamiliar markup, read `rive docs format` and use `rive docs --search <term>` to find relevant gotchas. Use `rive schema --search <term>` to find a type, then `rive schema <Type>` for exact property names, enum values, and property keys. Never infer a key or field name from a visual label. For a new project, inspect `rive samples` and `rive docs skeleton` before building from an empty file.

Each `.rml` file has one `<Rive version="1" kind="fragment">` root. A project may split the scene across files; IDs must remain unique across them. Put project defaults and build settings in `rive.yaml`, and name the default artboard with `main` when more than one artboard exists. Create an ID only where another object needs a reference. Confirm nesting and explicit reference rules in `rive docs format`.

Check the links that often look valid while doing nothing: the artboard's style and default state machine, a layout's style, a bind's actual target property, the script asset's attached node, and the `ComponentAsset` for a nested component artboard. Query the intended objects in `inspect --json` rather than accepting only an empty `problems` list.

Edit in small passes. The first CLI build may write generated IDs into the RML; review that diff before further editing. After each structural change, run `rive <dir> --verify` and `rive inspect <dir> --summary`; inspect the resolved objects and `problems` for the intended wiring. Render a screenshot for visible changes. A clean compile or inspect result does not prove that a bind, animation, or pixel output behaves correctly.

Use `iee-motion`, `iee-state-machines`, `iee-data-binding`, `iee-layouts`, and `iee-rigging` for their respective scene decisions. The [RML overview](https://rive.app/docs/runtimes/advanced-topic/rml) explains the text format; the installed CLI provides the detailed authoring reference.
