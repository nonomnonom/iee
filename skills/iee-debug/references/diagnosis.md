# Diagnose the first broken relationship

Use this when compilation succeeds but the work does not match its intended state. Reproduce with the smallest input/data sequence and retain a baseline capture or value. Consult the installed docs for exact properties; this table identifies what to investigate, not syntax to paste.

| Symptom | Trace | Evidence that distinguishes causes |
| --- | --- | --- |
| Geometry is missing or behind the wrong object | Parent → transform/layout → geometry → paint → clip/draw order | Resolved tree plus a capture of the affected region; inspect dimensions and masks before adding a replacement |
| Base value changes but playback stays the same | Base property → animation/layout/binding/script owner | Compare rest and advanced poses; isolate the writer on a preserved copy |
| Data logs an assignment but pixels do not change | Model → selected instance → property path → converter → target | Read back the landed value after advancing; inspect competing two-way writes and target property type |
| Script compiles but has no visible effect | Asset → scene attachment → input names/types → lifecycle callback → drawn output | Compare input names on both sides, runtime logs, and a frame with a deliberately distinct supported input |
| A click appears dead or changes twice | Hit target → overlapping targets → listener → state/value → feedback | Compare one click and repeated clicks; check transparent/hidden hit areas and multiple writers |
| Pointer works, keyboard does not | Focusable owner → acquired focus → key phase/filter → listener | Confirm the focused target, send one key, and read its value; visual focus alone is insufficient |
| Responsive content disappears or clips | Container size → child participation → sizing/style links → text/data extent | Same state at two meaningful sizes and long/empty data |
| Loop flashes or transition jumps | Authored pose → first advanced pose → transition/loop boundary → rest | Captures just before/after the boundary and playback; inspect mismatched initial values or easing |
| Preview works but export fails | Actual output file → included assets/scripts → signing → target support | Open the produced artifact in the available destination; local tooling playback does not prove a web runtime accepts scripts |

## Repair loop

1. State expected versus observed behavior with the exact state and reproduction.
2. Inspect the owning relationship and relevant source/schema. Separate a missing link from a conflicting writer.
3. Make one coherent correction. Preserve interfaces and unrelated artwork.
4. Repeat the original reproduction, then the nearest affected return/repeat or alternate data case.
5. Inspect the diff and current captures. If the hypothesis failed, gather new evidence before another patch.

Stop repeating a command when the same failure provides no new information. Switch to an available evidence source or report the specific dependency and the checks left open. Restore temporary probes you introduced; preserve the user's edits.