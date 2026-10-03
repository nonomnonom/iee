---
name: iee-wgsl
description: Create or refine a Rive WGSL shader effect when native drawing and ordinary scripts cannot produce the intended visual result.
---

# Create Rive shader effects

Use a shader for a visual effect that benefits from GPU rendering, such as procedural pixels or image distortion. Check whether Rive shapes, fills, strokes, clipping, feathering, or a path effect already achieve the intended result with a more editable scene.

Read the [Rive WGSL guide](https://rive.app/docs/scripting/wgsl-shaders) and the installed CLI's GPU API topic for the chosen scripting lane. Keep the shader, its render target, and its scene attachment clear. Match bind group and binding indices on the WGSL and script sides; supply uniforms and textures in the declared types. Rive supports vertex and fragment shaders with platform restrictions. Check `rive docs project/rive-yaml` for `shaderOutputs` and include the backends needed by the requested deliverable.

Compile with `rive <dir> --verify`, then render the effect at meaningful times and input values. Verify that the shader actually contributes visible pixels and that animated uniforms change the result. Test the output on the target renderer when possible; a successful build alone does not establish visual parity.
