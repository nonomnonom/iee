# Build responsive Rive layouts

Choose which regions resize, wrap, scroll, or retain a fixed size. Make that sizing model explicit before filling the scene with details. Use layout components for regions and layout participants for drawable leaves; keep the object's own geometry and its layout participation distinct.

Read the relevant section of `rive docs layout` for CLI syntax. In the Editor, inspect container direction, sizing, alignment, padding, gaps, and each child's participation through the connected tools. Confirm required style links and the artboard's layout setup rather than relying on a successful compile. Use a layout script only when native sizing and arrangement cannot express the behavior.

Render the same state at a narrow and a wide CLI `--viewport` size, or equivalent Editor preview sizes. With the CLI's layout fit, the viewport changes the artboard's layout size; other fit modes can scale the scene instead. Compare actual reflow, legibility, clipping, and spacing. Also check long text and changed bound values if they affect size. Verify scrolling through a gesture, not only a static frame.

Preserve the brief's typography and visual hierarchy. For scripted layout, read the [Luau](luau.md) or [AnimaScript](animascript.md) reference matching the project's lane.
