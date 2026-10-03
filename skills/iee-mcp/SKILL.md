---
name: iee-mcp
description: Author and revise an open Rive file through the desktop Editor's MCP tools, including scene structure, animation, data, scripts, and shaders.
---

# Work through the Rive Editor MCP

Use this path when the user is working in a Rive desktop Editor file and the Editor MCP connection is available. The [Rive MCP documentation](https://rive.app/docs/editor/ai/mcp) describes a local desktop connection and the broad editing capabilities; tool names and supported operations must be discovered from the connected server at run time.

Identify the active file and inspect its selected artboard, hierarchy, and relevant properties before changing them. Translate the requested visual or behavioral result into a short sequence of scene edits. Apply related edits in small groups so the Editor state can be checked between them. Reuse existing components and View Models where they fit the work.

After each meaningful group, inspect the changed objects, run available diagnostics or script recompilation, and preview the affected state. Do not infer success from an MCP call returning without an error: verify the scene and the visible result. If a required capability is missing from the connected server, use the Rive CLI path where the artifact can be edited as a project, or report the specific gap.

Editor MCP availability depends on the desktop app. Do not invent MCP tool names from documentation examples. Consult the relevant IEE craft skill for the actual design, motion, data, or rigging decision.
