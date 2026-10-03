---
name: iee-review
description: Use when assessing a Rive artifact, preparing a source or export handoff, or about to claim its appearance, animation, interaction, or delivery is complete.
---

# Verify the claim against the artifact

**Principle:** claim only what current evidence demonstrates.

## Establish the review

Identify the brief, current source or Editor state, relevant sizes/states, and requested deliverable. Reuse evidence from this revision. After an edit, regenerate only checks affected by it or by unresolved concerns.

For review-only requests, inspect without implementing fixes. Preserve the original before validation that can assign IDs; use a review copy when needed. For completion tasks, route a failed behavior to `iee-debug` and a clear visual revision to `iee-build`.

## Collect the necessary evidence

Use the relevant rows of the [verification matrix](references/verification.md), not every possible check.

| Claim | Required evidence |
| --- | --- |
| Structure is valid | Compilation/Editor diagnostics plus inspection of intended objects and links |
| Appearance meets the brief | Viewed captures or preview of the authored rest pose, opening playback, and meaningful states |
| Interaction works | Actual input/data sequences over the intended hit/focus region, visible response and relevant values, plus return/repeat/interruption and outside/disabled cases where applicable |
| Handoff is usable | Current output file/source, required assets and exposed names, and opening/playback in the available destination |

A file existing is not visual inspection. An empty problems list does not prove wiring. A passing script test does not prove the attached scene works.

## Judge craft

Compare silhouette, hierarchy, spacing, contrast, typography, clipping, and motion character with the brief. Name defects by location and state. Inspect intermediate poses and loop boundaries; use playback when timing or feel cannot be judged from captures.

Separate three conclusions: **brief compliance**, **craft quality**, and **handoff readiness**. Working input is evidence for behavior, not artistic polish. For craft concerns, identify the visible defect, its effect on the brief, and the smallest useful correction. Do not invent defects or extra features to justify more work. If a claim depends on a supplied reference, compare matching scale and state.

Check responsive sizes, keyboard/focus/semantics, and reduced motion when relevant to the work. Headless captures do not prove high-DPI behavior, every platform's accessibility, or target-device performance. Measure performance when the brief or an observed issue requires it.

## Deliver with a clear boundary

Report the artifact location, verified outcomes, and material gaps. Distinguish **verified**, **failed**, and **not exercised**. A blocked check stays unverified; continue independent work and name the concrete missing capability.

Deliver the requested editable source and/or export. A project preview does not independently test a standalone exported file. Check installed publishing docs for script signing and native-export requirements, preserving the requested destination and existing authorization. Do not substitute a hosted link for a local deliverable.

Completion requires the relevant claims above to be supported. If a required check cannot run, hand over useful work with its limitation explicitly stated.
