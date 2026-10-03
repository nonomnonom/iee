---
name: iee-layouts
description: Build responsive Rive artboards and components with layout sizing, flow, constraints, scrolling, and visual checks at multiple sizes.
---

# Build responsive Rive layouts

Choose which regions resize, wrap, scroll, or retain a fixed size. Make that sizing model explicit before filling the scene with details. Use layout components for regions and layout participants for drawable leaves; keep the object's own geometry and its layout participation distinct.

Read `rive docs layout` for the CLI version in use and the [Editor layouts overview](https://rive.app/docs/editor/layouts/layouts-overview) for visual authoring. Confirm required style links and the artboard's layout setup rather than relying on a successful compile. Use a layout script only when native sizing and arrangement cannot express the behavior.

Render the same state at a narrow and a wide `--viewport` size. The viewport changes the artboard's layout size, so compare the actual reflow, legibility, clipping, and spacing. Also check long text and changed bound values if they affect size. Verify scrolling through a gesture, not only a static frame.

Coordinate typography and visual hierarchy with `iee-design`, and scripted layout behavior with the project's Luau or AnimaScript skill.
