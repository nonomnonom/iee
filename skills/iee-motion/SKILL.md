---
name: iee-motion
description: Animate a Rive work with timelines, keyframes, easing, loops, and transitions that support its visual and interaction intent.
---

# Shape motion in Rive

Decide what motion communicates before placing keys: arrival, response, continuity, emphasis, or change in state. Identify the rest pose and the meaningful end poses. Keep timing consistent with the work's visual character and avoid movement that hides content or weakens feedback.

Use timeline animation for property changes and a state machine when playback depends on interaction or data. In RML, property keys come from `rive schema <Type> --animatable`; match each keyframe element to the property's type. Animation duration is in frames at its `fps`, while transition durations are in milliseconds. Confirm the distinction in the installed `rive docs format` and `rive docs easing` for the CLI version in use.

Check the rest pose, an early frame, the most expressive pose, and the settled state with screenshots or the live preview. Look for abrupt jumps, unwanted interpolation, conflicting keys, and loops that continue after the work should rest. Use the graph and interpolation tools in the Editor when a curve needs visual tuning. For substantial decorative motion, expose a View Model property such as `prefersReducedMotion` and provide a shorter, quieter, or static feedback path; Rive does not apply this preference automatically.

Read the [Editor animation guide](https://rive.app/docs/editor/animate-mode/animate-mode-overview) for timeline concepts. Route conditional playback to `iee-state-machines` and complex deformation to `iee-rigging`.
