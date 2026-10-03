# Rive fundamentals

Rive is an editable scene graph of vector artwork and other assets. The same scene can be animated, controlled by a state machine, bound to data, and exported for a runtime. Treat those as connected layers of one artifact. A valid file can still look wrong or behave wrong, so inspect the rendered result and its behavior.

Read the section relevant to the current scene decision. For CLI work, use [the local documentation workflow](cli-docs.md) for exact syntax. For Editor work, inspect the connected tool schemas and scene objects. This reference explains ownership; it does not add a second mandatory workflow.

## 1. The scene and its ownership tree

An **artboard** defines a scene's working area and provides a root for its content. A file can contain multiple artboards. A **component** is reusable scene content, often instantiated in another artboard. A **group** organizes children under a shared parent. A **shape** or **path** supplies geometry; paints give it visible fill and/or stroke. Images, text, and other assets can also appear in the hierarchy. An instance is not the same object as its reusable definition.

Sketch the actual parent-child tree before editing. Every visible object has a parent context. A child moves, scales, rotates, clips, and may inherit properties according to that context. Reparenting can change the result even when the child's own numbers stay the same. Keep reusable elements in the component that owns them; place scene-specific elements in the containing artboard. Preserve the references that animations, state machines, data bindings, and code use when renaming or moving objects.

The **hierarchy** answers both ownership and visual stacking. Sibling order influences which artwork appears in front where shapes overlap. The exact direction shown by an Editor panel or RML list must be checked in the current tool; never infer it from indentation alone. Clipping and masks limit what is visible; they do not replace correct stacking. A hidden or transparent object is still an object in the tree. Do not assume it has been removed from interaction or layout.

### Position and transforms

- An artboard has its own coordinate space. A child position is interpreted in the coordinate space of its parent. Distinguish local coordinates, artboard coordinates, and the final position on screen.
- Position, rotation, scale, and origin/pivot are separate concepts. Rotation and scale happen around an origin. Check `freeze and origin` and transform-space behavior before changing a pivot or reparenting.
- The final appearance depends on the chain of parent transforms and on layout or constraints. A shape at `(0, 0)` need not sit at the artboard's top-left after those are applied.
- Design-mode values are a base pose. Animated values, state-machine output, data binding, constraints, and layout can change the rendered pose. If a property looks correct in the source but wrong in playback, identify the current owner of that property rather than repeatedly changing its base value.
- When using responsive layouts, identify the container, sizing rules, constraints, alignment, padding, and clipping. Check both the intended artboard size and at least one materially different size.

### Transparency and visibility

Treat fill alpha, object opacity, parent/group opacity, and visibility as different controls. An alpha value changes a paint's contribution; opacity can affect an object or subtree; visibility affects whether it draws. Exact compositing and hit-testing behavior must be checked in the installed version, especially with overlapping children or masks. A fully transparent fill may be intentional geometry; deleting it, hiding it, or removing its paint can change clipping or interaction. Always inspect the rendered overlap rather than assuming the numerical opacity gives the desired look.

## 2. Build vector artwork deliberately

Plan the silhouette and major masses first. Then add interior geometry, fills, strokes, gradients, highlights, shadows, text, and small detail in a deliberate draw order. Use a primitive or procedural shape for a regular form; use a path and vertices when the contour needs custom geometry. Keep paths editable when future deformation or animation requires it. A stroke is not the same as a filled outline: width, joins, caps, and trim affect appearance.

For each visual element answer: What geometry creates it? Which fill or stroke paints it? What is its parent? Where is it stacked? Which coordinate space positions it? Is it clipped? Does another system animate or bind it? A visually similar screenshot does not prove these relationships are correct.

Use groups for shared transforms or organization, components for genuine reuse, and separate shapes when they need independent animation, clipping, or paint. Avoid flattening editable vectors or rasterizing them merely to make the current frame look right. Use bones, meshes, joysticks, solos, and trim paths only where their distinct behavior is needed and supported by the target runtime.

Concrete example: a button artboard can contain a background shape below a label and an icon, all under one button group. The group's transform positions the entire button; the label's position is local to that group. A hover animation may alter the background paint and icon transform, while a state machine chooses when that animation runs. A bound text property may set the label. Moving the label to the artboard root changes its positioning and may break animation or binding references even if one static frame still looks similar.

## 3. Assets and reusable content

Inventory images, fonts, SVGs, audio, scripts, and library or component references before editing. Distinguish an imported asset from an instance using it. Check whether assets are embedded, linked, or otherwise required at runtime, and whether the export includes the needed content. Use existing assets and components when they fit. Preserve names and reference paths that runtime code, animation targets, and bindings rely on. Inspect typography with the actual font and text content; text width, wrapping, and clipping can change with data.

## 4. Motion and interaction

A **linear animation** is a timeline of property changes and keyframes. The timeline, interpolation/easing, duration, loop behavior, and animated draw order determine what is seen. Verify initial pose and each important key pose, not just the endpoint. Check what happens when two animations target the same property.

A **state machine** chooses and blends behavior through states, transitions, layers, and inputs. A listener or event can connect user action to state-machine behavior. Map each user action or condition to an input, transition, and visible outcome. Test entry, exit, repeat, and interruption. Do not treat a timeline alone as proof of interaction. Do not infer click behavior from a transparent shape or visual hit area; test the actual input/listener wiring.

Animation and interaction are different responsibilities: artwork provides drawable objects, animation changes properties over time, and the state machine decides which behavior plays. Identify the system that owns each property at runtime to avoid conflicting control.

## 5. Data binding

A **view model** defines typed data that can drive a scene; an **instance** supplies values. Bindings connect properties to visible objects or component behavior. Property types, enums, lists, converters, and stateful components have distinct roles. Confirm the model type, instance selection, property path, conversion, and target. Test with at least two meaningfully different values, including text of different lengths or a list with different counts when relevant. A model that exists in a file but is not bound to a visible target does not satisfy a data-driven request.

Keep data ownership separate from visual ownership: the view model supplies a value, the bound object displays it, and animation or state-machine logic may react to it. Trace that full chain whenever the result appears stuck or inconsistent.

## 6. Source, export, and publishing

Identify the requested deliverable before exporting. RML is editable source for the CLI workflow; the native editor document and a runtime `.riv` serve different purposes. An interactive runtime export differs from a static image or video. Do not call a render, editor save, runtime export, hosted share link, and publication the same thing.

Verify names exposed to runtime consumers, included artboards and components, assets and fonts, input and view-model interfaces, and target-runtime feature support. Test the exported artifact in the intended runtime or a documented preview. Preserve an editable source or backup when the workflow requires future editing. Publishing or uploading is a separate action: use the requested destination, confirm the produced version, and report what was actually shared.

