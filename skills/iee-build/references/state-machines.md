# Build interactive state machines

Describe the behavior as a small state graph before editing: starting state, input or event, transition condition, visible response, and route back. Add layers only for behavior that needs to run independently. Prefer a predictable graph over many nearly identical states.

In CLI-authored scenes, read `rive docs state-machines` and look up exact types with `rive schema`. Ensure each layer has an entry path and the artboard points to the intended `defaultStateMachineId`; otherwise playback may differ by host. In the Editor, inspect the entry state, transition conditions, animation assignments, and active state machine through MCP before editing them.

Create listeners and input wiring at the object that should receive the gesture. Coordinate view model conditions with [data-binding reference](data-binding.md); use the installed `rive docs focus` and `rive docs semantics` topics for keyboard focus and semantic actions.

Focusability and focus acquisition are separate. Author the entry focus or traversal behavior the control needs, then test it in the destination. CLI 1.3.0 can focus the first focusable node automatically, masking a missing authored focus action. A keyboard test passing in that player alone does not establish embedded keyboard behavior. Check a visible focus cue when the user can traverse between controls, and give semantic actions the same state-change owner as pointer and keyboard input.

Define the intended hit region from the affordance. If the whole illustrated object should respond, a working center click does not establish coverage of its visible parts. Inspect hit geometry and test representative interior and edge points, plus an outside point that should do nothing. Check overlapping targets for double activation and disabled/hidden states for unintended input. Use one coherent input owner where possible so enlarging coverage does not toggle a value twice.

Inspect the resolved graph and its problems. Then drive representative sequences with the CLI's `--pointer`, `--key`, `--data`, and `--advance` flags or through the Editor preview. Capture rest, activated, and return states. Repeat the action and interrupt or reverse it when the interaction allows that. Check both the visible transition and the underlying value when one is expected to change. A state graph that compiles but never receives an input is unfinished.
