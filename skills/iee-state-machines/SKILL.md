---
name: iee-state-machines
description: Build and verify Rive state machines for interactive animation, including states, transitions, inputs, listeners, and layered behavior.
---

# Build interactive state machines

Describe the behavior as a small state graph before editing: starting state, input or event, transition condition, visible response, and route back. Add layers only for behavior that needs to run independently. Prefer a predictable graph over many nearly identical states.

In CLI-authored scenes, read `rive docs state-machines` and look up exact types with `rive schema`. Ensure each layer has an entry path and the artboard points to the intended `defaultStateMachineId`; otherwise playback may differ by host. Use the Editor's [state machine guide](https://rive.app/docs/editor/state-machine/state-machine) when building through MCP.

Create listeners and input wiring at the object that should receive the gesture. Coordinate view model conditions with `iee-data-binding`; use the installed `rive docs focus` and `rive docs semantics` topics for keyboard focus and semantic actions.

Inspect the resolved graph and its problems. Then drive representative sequences with the CLI's `--pointer`, `--key`, `--data`, and `--advance` flags or through the Editor preview. Capture rest, activated, and return states. Check both the visible transition and the underlying value when one is expected to change. A state graph that compiles but never receives an input is unfinished.
