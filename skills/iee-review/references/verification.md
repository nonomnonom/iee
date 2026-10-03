# Verification matrix

Run only checks relevant to the work. Use paths that exist; screenshot paths resolve from the current working directory. Inspect the images, not only command exit codes.

| Claim to verify | Evidence to collect |
| --- | --- |
| The project compiles | `rive <dir> --verify` completes without errors |
| The intended objects and links exist | `rive inspect <dir> --summary`; query `--json` for the specific artboard, animation, binding, or state |
| The authored rest pose reads clearly | `rive <dir> --screenshot=rest.png` and visual inspection; this is before the state machine advances |
| The opening animated frame appears | Capture with `--advance=1` and compare with the rest pose |
| Animation reaches the intended pose | Capture with `--advance=<frames>` at an expressive point and after settling |
| A control changes and returns | Capture rest, after an input, and after the reverse input; advance between gestures when the state machine needs a frame |
| Data drives the intended display | Render with `--data=<path=value>`; read back with `--data-dump=-` when the scene computes values |
| Layout reflows | Capture the same state with narrow and wide `--viewport=<WxH>` values |
| Script logic works | `rive <dir> --test` for authored tests, then render the script attached to its scene |
| Keyboard and semantics work | Send `--key=<key>` to a focused target; inspect semantic labels/actions where authored |
| Performance fits the target | Use `--bench=<frames>` and a target device or renderer when performance is part of the brief |

`--verify` does not run scripts or inspect pixels. `inspect` does not type-check scripts and may show authored objects that do not behave as intended. A screenshot of one frame does not prove an interaction. If a check fails, fix the cause and repeat the specific evidence that exposed it.
