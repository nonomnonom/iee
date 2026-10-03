# Work in the Rive Editor

Discover the connected server's tools, input schemas, and capabilities. Do not invent tool names or assume that CLI commands are Editor operations. The live server determines what this session can do. Inspect its returned objects and diagnostics for the current document rather than opening a web guide as routine preparation.

## Establish the source

Identify the active file and artboard, selection, relevant hierarchy, and properties. Resolve ambiguous file identity before mutation. Preserve recoverable state through the available save, copy, or revision mechanism before a broad structural change. Respect edits already in the document.

Start with the available session/file inspection. A connected server with no open document is not an editable file; report that missing context before issuing artboard operations. Read the hierarchy shallowly, then inspect the affected branch instead of requesting the entire document at maximum depth.

For creation or substantial changes, establish the affected ownership tree; consult the [scene model](scene-model.md) for missing concepts. CLI installation is not required for this path. Read only the relevant craft reference when a motion, layout, binding, or rigging decision requires it.

## Edit and observe

Translate the request into related edits to the owning objects. Apply a meaningful group, inspect its resulting properties, run available diagnostics or script compilation, and preview the affected state. Reuse components and View Models where they fit.

Reinspect before another mutation when the file, selection, or object state may have changed. Resolve objects from the current document; do not reuse stale IDs after a reload or replacement. If a call partially succeeds, inspect what changed before retrying.

Read property units and enum values from the connected schema. RML/runtime values and Editor display values can differ: an opacity may be normalized in one surface and a percentage in another. Do not transfer numbers blindly between them. Inspect per-object or per-property errors as well as the overall tool result; retrying an entire partially successful batch can apply an edit twice.

An MCP success response does not prove the result looks or behaves correctly. Verify the requested state and input path through available preview/capture tools. For a review-only task, report findings without editing.

## Handle missing capabilities

If the connected tools cannot perform a required operation, identify the specific gap. Use a CLI project only when a supported source handoff is available: preserve the native file, import into a new destination, and establish which copy owns further edits. Never overwrite local or Editor work merely to change tools.

Use `iee-review` before delivery. Report the actual file/artboard, observed results, and checks the available tools could not exercise. Export or publish only the requested outcome and destination; use existing authorization.
