# Author editable RML

Use RML for fixed scene structure; attach scripts where imagery or behavior is computed. Preserve the user's artboards, assets, scripting lane, IDs, and external interfaces.

## Inspect before writing

Identify the project, installed CLI executable/version, source files, assets, and requested output. If `rive` is absent from PATH, check the project's documented executable or the standard local installation before declaring it unavailable. Do not update or switch versions just to fit a remembered example.

Establish the affected hierarchy and property ownership; consult the [scene model](scene-model.md) only for missing concepts. Follow the [CLI workflow](cli-docs.md) when the installation or documentation interface is unfamiliar. Read `rive docs format` for unfamiliar markup, then the relevant topic, example, and `rive schema <Type>`. Search gotchas for the current feature or symptom. For new work, inspect `rive docs skeleton` or a relevant installed sample. Reuse docs already read for this version.

Use official web documentation only for a concrete gap and check version compatibility. Never invent an element, attribute, nesting rule, property key, or command flag.

## Make a coherent edit

1. Inspect existing changes and preserve recoverable source before the first build/import or surface change. A build can write generated IDs and state nodes into RML. Review that diff before further edits. Re-read source if the user or another tool has changed it.
2. Establish artboard dimensions, parent/child ownership, draw order, transforms, and clipping. Build dependencies before their consumers. Add only the layout, animation, state machine, or data wiring the brief needs.
3. Keep one `<Rive version="1" kind="fragment">` root per `.rml` file and IDs unique across the project. Confirm this with the installed format docs. Keep project settings in `rive.yaml`; specify the main artboard when the project needs a default among several.
4. Use stable names where later editing or consumers depend on them. Create explicit IDs for referenced objects; preserve generated IDs. Keep reusable geometry in its owning component. Do not duplicate an object to avoid tracing its references.
5. Query exact animatable/bindable properties through schema. Check style links, default state machine, component assets, View Model instances, binding targets, and script attachments. An object existing in `inspect` does not prove that it is wired.

If this CLI cannot represent a required feature, preserve the native source and identify the supported Editor or scripting path. Do not flatten or regenerate the file merely to make a compile pass.

## Verify each meaningful pass

Use documented commands for the installed version: `rive <dir> --verify`, then `rive inspect <dir> --json` for the intended objects and problems. Render visible changes and inspect the images. Exercise affected timelines, inputs, and data after advancing the scene. Read another craft reference only when its decision is needed.

Use `iee-review` for the final evidence. If exporting, check the actual produced file and its required behavior; a successful build or a preview of a previous revision is insufficient. Keep editable source in the handoff and report anything that could not be exercised.
