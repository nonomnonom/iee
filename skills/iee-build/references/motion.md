# Shape motion in Rive

Decide what motion communicates before placing keys: arrival, response, continuity, emphasis, or change in state. Identify the rest pose and the meaningful end poses. Keep timing consistent with the work's visual character and avoid movement that hides content or weakens feedback.

For a performance, block the key poses and their timing before polishing curves. For a control, establish when input is acknowledged, when the value changes, and when movement settles. An easing preset does not decide those moments for you.

Inspect spacing as well as duration: evenly spaced positions read as constant speed; changing spacing conveys acceleration or deceleration. Choose where motion leads and where it follows. Use anticipation, overshoot, settling, or a brief hold when they communicate weight or intent, and omit them when they delay feedback. Secondary motion should follow the main action rather than competing for attention.

For character motion, track the path of the head, hands, and other focal parts through intermediate poses. Preserve intended contacts and the apparent volume of deforming forms. When several parts move, offset them according to the action instead of assigning identical easing and timing everywhere. Keep a clean silhouette through extremes and turns.

Use timeline animation for property changes and a state machine when playback depends on interaction or data. In RML, property keys come from `rive schema <Type> --animatable`; match each keyframe element to the property's type. Animation duration is in frames at its `fps`, while transition durations are in milliseconds. Confirm the distinction in the installed `rive docs format` and `rive docs easing` for the CLI version in use.

Check the rest pose, an early frame, the most expressive pose, and the settled state with screenshots or the live preview. Look for abrupt jumps, unwanted interpolation, conflicting keys, and loops that continue after the work should rest. Use the graph and interpolation tools in the Editor when a curve needs visual tuning. For substantial decorative motion, expose a View Model property such as `prefersReducedMotion` and provide a shorter, quieter, or static feedback path; Rive does not apply this preference automatically.

For loops, compare the last and first playback poses and the movement across that boundary. For interactive transitions, test reversal or interruption before settling. A few key poses do not establish timing or feel: inspect playback when that judgment matters, and report the limitation if only still captures are available. Preserve the project's existing reduced-motion interface when one exists.

Matching loop endpoints is insufficient if velocity jumps at the join. Check neighboring frames on both sides, and inspect repeated playback for an unintended pause or snap. For interactive reversals, begin from the current pose where the intended behavior requires continuity; an abrupt reset to the authored pose is a defect unless the brief calls for it.

In the Editor, inspect the selected timeline's frame rate, keyed properties, interpolation, and playback range through the available tools. Route conditional playback to [state-machines reference](state-machines.md) and complex deformation to [rigging reference](rigging.md).
