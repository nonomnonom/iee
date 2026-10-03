# Create Rive shader effects

Use a shader for a visual effect that benefits from GPU rendering, such as procedural pixels or image distortion. Check whether Rive shapes, fills, strokes, clipping, feathering, or a path effect already achieve the intended result with a more editable scene.

Use the installed GPU API topic for the chosen scripting lane and `rive docs project/rive-yaml` for exact syntax and `shaderOutputs`. In an Editor-only session, inspect the existing shader attachment, script inputs, and available shader diagnostics. Keep the shader, its render target, and its scene attachment clear. Match bind group and binding indices on the WGSL and script sides; supply uniforms and textures in the declared types. Rive supports vertex and fragment shaders with platform restrictions; include the backends needed by the requested deliverable.

Match uniform offsets, alignment, and buffer size to the WGSL layout; a valid buffer with wrong offsets can produce incorrect pixels without a compiler error. Derive the pipeline color format from its render target. Allocate reusable GPU resources during initialization and update changing uniforms during advance, rather than recreating the pipeline every frame.

For CLI work, compile with `rive <dir> --verify`; in the Editor, use available shader compilation and diagnostics. Then render the effect at meaningful times and input values. Verify that the shader actually contributes visible pixels and that animated uniforms change the result. Test the output on the target renderer when possible; a successful build alone does not establish visual parity.
