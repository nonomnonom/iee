---
name: iee-review
description: Review a Rive artifact for visual craft, working interaction, responsive layout, script behavior, accessibility, and deliverable integrity.
---

# Review the Rive work

Review the artifact against its brief, not only against whether it builds. Identify the intended focal point, content hierarchy, rest state, animated states, input paths, data variants, and target sizes. Report concrete defects with the state and evidence that exposed them, then fix them when the task includes completion of the work.

For a CLI project with shell access and Rive CLI installed, use three separate checks: `rive <dir> --verify` for compilation, `rive inspect <dir> --summary` or `--json` for resolved scene structure and problems, and rendered captures for appearance. Use `--test` for script logic, `--data-dump=-` for data changes, and `--pointer`, `--key`, `--data`, `--advance`, and `--viewport` to reproduce relevant states. Read `rive docs workflow` and `rive docs gotchas` for version-specific limits of these checks.

Use the [verification matrix](references/verification.md) to select checks for the artifact's actual features.

Inspect visual quality in the rendered output: alignment, text legibility, contrast, clipping, hierarchy, motion timing, and whether each action gives clear feedback. Check keyboard focus and semantic information when the work accepts keyboard or accessibility actions. Verify that a reduced-motion property changes the animation while preserving feedback. Use `rive docs semantics` and the [Editor accessibility guides](https://rive.app/docs/editor/accessibility/semantics) for available mechanisms. Runtime semantics support varies by platform, so check the target's feature support before claiming screen-reader behavior.

Use `--bench` or target-device preview when performance is a concrete concern. Describe what was actually tested; do not equate a clean compile, empty `problems`, or one screenshot with a finished interactive experience.
