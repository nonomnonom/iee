---
name: iee-debug
description: Use when a Rive scene renders incorrectly, ignores input or data, deforms unexpectedly, fails compilation, or loses behavior during export, including failures after a clean build.
---

# Find the first broken relationship

**Principle:** reproduce the discrepancy and locate its cause before patching.

## 1. Reproduce

State expected versus observed behavior. Identify the source, relevant artboard, size, input/data sequence, and tool version. Preserve the original before commands that may mutate it; keep backup copies out of compiler input discovery. Capture the failing state or diagnostic.

Read errors fully. For a clean build with wrong behavior, inspect the actual rendered state and landed values. If the failure cannot be reproduced, gather the missing state or evidence before guessing a repair.

## 2. Trace ownership

Follow the signal from its source to the first disagreement:

- Appearance: parent/transform/layout → geometry/paint → clip/draw order.
- Data: model/instance → property path/converter → target → competing writer.
- Interaction: hit/focus target → listener/input → transition/value → visible feedback.
- Script: asset → attachment → input names/types → callback → output.
- Export: actual file → assets/scripts → signing → target support.

Use the relevant row of [diagnosis](references/diagnosis.md) for a concrete probe. Read only the needed technical reference through `iee-build` when syntax or ownership is unfamiliar. Do not start a new design process for a broken link.

## 3. Test one explanation

Name a hypothesis supported by the evidence. Change the responsible relationship while preserving artwork, interfaces, and unrelated behavior. Check that it fixes the original reproduction. Restore temporary probes you introduced.

If the hypothesis fails, inspect the new evidence before another edit. Do not stack compensating geometry, duplicate listeners, or arbitrary base values. Do not retry an unchanged unavailable command repeatedly.

## 4. Close the regression

Repeat the original case, then the nearest affected alternate value, return/repeat, or interruption. Confirm both the visible response and underlying value when relevant. Inspect the diff for unintended changes.

Use `iee-review` to assess the evidence already collected and the requested handoff; do not rerun valid checks merely to satisfy a second checklist. Report the cause, correction, proof, and material unverified behavior. If tools prevent verification, name the exact remaining check without claiming the defect is fixed.
