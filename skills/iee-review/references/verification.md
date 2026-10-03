# Verification matrix

Run only checks relevant to the work. Use paths that exist; screenshot paths resolve from the current working directory. Inspect the images, not only command exit codes.

These commands were checked against Rive CLI 1.3.0. Confirm their syntax in the installed version. Preserve source before a build that may assign IDs, and keep captures from the same revision as the final artifact. Store evidence outside the project or explicitly exclude it from asset discovery. For an Editor-only workflow, collect equivalent evidence through the connected tools and identify any unavailable check.

| Claim to verify | Evidence to collect |
| --- | --- |
| The project compiles | `rive <dir> --verify` completes without errors |
| The intended objects and links exist | `rive inspect <dir> --summary`; query `--json` for the specific artboard, animation, binding, or state |
| The authored rest pose reads clearly | `rive <dir> --screenshot=rest.png` and visual inspection; this is before the state machine advances |
| The reference or brief is visually met | Compare matching scale/state for silhouette, proportions, negative space, overlap, and focal contrast; name concrete differences rather than assigning an uncalibrated style score |
| The opening animated frame appears | Capture with `--advance=1` and compare with the rest pose |
| Animation reaches the intended pose | Capture with `--advance=<frames>` at an expressive point and after settling |
| A loop or transition is continuous | Compare frames on both sides of the boundary and inspect playback when timing/feel matters |
| A control changes and returns | Capture rest, after an input, and after the reverse input; advance between gestures when the state machine needs a frame |
| The advertised hit region works | Drive representative interior/edge points on the intended target and an outside point; inspect missed hits and double activation from overlaps |
| Data drives the intended display | Render with `--data=<path=value>`; read back with `--data-dump=-` when the scene computes values |
| Layout reflows | Capture the same state with narrow and wide `--viewport=<WxH>` values |
| Script logic works | `rive <dir> --test` for authored tests, then render the script attached to its scene |
| Keyboard and semantics work | Send `--key=<key>` to a focused target; inspect semantic labels/actions where authored |
| Reduced motion preserves feedback | Exercise the authored preference with the same input and compare the quieter response |
| Performance fits the target | Use `--bench=<frames>` and a target device or renderer when performance is part of the brief |
| The handoff is usable | Check current output path, size, required source/assets and exposed names; open or run that artifact in the available destination |

`--verify` does not run scripts or inspect pixels. `inspect` does not type-check scripts and may show authored objects that do not behave as intended. A screenshot of one frame does not prove an interaction. If a check fails, fix the cause and repeat the specific evidence that exposed it.

## Reproduce a state

Record the project/artboard, viewport, data, input sequence, and advances with each capture. CLI input and advance flags form an ordered sequence. Use the actual target's coordinates and allow a state machine to advance between gestures. For example, adapt this to a real control:

```sh
rive <dir> --screenshot=active.png --advance=1 --pointer=click@120,60 --advance=30
rive <dir> --screenshot=returned.png --advance=1 --pointer=click@120,60 --advance=30 --pointer=click@120,60 --advance=30
```

Do not infer behavior from changed file hashes alone: a rendering can change for an unrelated reason. Inspect the captures and read back relevant values. Conversely, data changing without a visible response does not prove the artwork reacts correctly.

## Evidence limits

- Headless captures run at a particular scale and renderer. They cannot prove high-DPI behavior or parity on every platform.
- `--test` proves only the tests that actually ran; a project without authored tests needs behavioral evidence from the scene.
- A project preview rebuilds source. Rive CLI 1.3.0 does not open a standalone `.riv`, so that preview does not independently verify an exported file in its destination runtime.
- Local unsigned script playback does not prove web readiness. Consult installed publishing docs and retain the user's destination/authorization boundary.
- CLI focus defaults can conceal missing focus acquisition in an embedded scene. Check the authored focus path and exercise keyboard input in the actual destination when claiming keyboard-ready delivery.
- If a renderer, Editor operation, account session, or target runtime is unavailable, mark that check **not exercised**, explain the gap, and deliver only the claims supported by the available evidence.

## Craft review record

For a substantial visual review, record the brief/reference, viewed states, and concrete findings. Keep separate verdicts for compliance, craft, and handoff. A finding should identify an observed location/state, why it matters, and the correction or evidence needed. If no defect is demonstrated, say so; stylistic alternatives are suggestions, not failed requirements. A contact sheet supports pose comparison, but does not replace playback for timing judgments.
