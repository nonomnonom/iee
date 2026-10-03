# Design checks by work type

Use the relevant row as a critique lens, not as a template for the artwork. The user's reference and brief decide the style.

| Work | Decisions that shape it | Review the rendered result for |
| --- | --- | --- |
| Interactive control or icon | Visual role, small-size silhouette, rest/active/disabled states, pointer and keyboard feedback | Each state reads at target size; activation has a visible result; labels and semantics match the action |
| Character or mascot | Distinct silhouette, pose range, rig controls, expression changes, timing | Identity survives motion; extreme poses do not collapse; transitions show intent rather than arbitrary movement |
| Data-driven display | Meaningful value range, units, hierarchy, empty or extreme values, update motion | Values remain legible; the graphic reflects injected data; large changes do not clip or mislead |
| Interactive scene or illustration | Focal action, stage depth, draw order, entry and exit states, response to input | The viewer knows where to look and what can be touched; changes are visible without losing scene coherence |
| Procedural effect | Inputs, randomness, time behavior, resolution, performance target | It remains stable at relevant sizes and parameter extremes; it supports the scene rather than hiding its content |

Across types, prefer a small number of deliberate shapes, colors, and motion ideas. A new effect earns its place by making the work clearer or more distinctive in a rendered state.
