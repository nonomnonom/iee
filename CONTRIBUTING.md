# Contributing

IEE Core turns Rive's authoring documentation into concise, task-focused guidance for agents. Contributions should improve decisions an agent makes while creating or checking a Rive artifact.

## Scope

- Keep the plugin focused on Rive artifact creation. Host application runtime integration belongs elsewhere.
- Keep each `SKILL.md` short enough to load for its task. Put conditional detail in a local `references/` file and link it from the skill.
- Route exact, version-dependent syntax to the installed Rive CLI (`rive docs` and `rive schema`) or an official Rive page. Do not copy entire manuals into skills.
- Keep `plugin.json`, `mcp.json`, and `skills/` portable. Put client-specific metadata only in the corresponding adapter files.
- Keep Claude Code and Codex marketplace metadata in their separate adapter files. When changing the package name, version, or Editor URL, update the matching adapter values too.
- Treat Rive Editor MCP tool names and capabilities as discoverable at connection time; do not invent a fixed tool catalog.

## Validation

Run `python scripts/validate.py` from the repository root after changing a manifest, skill, or reference. The script checks both manifests against the canonical Agent Plugins 1.0.0 schemas, skill frontmatter, adapter consistency, package boundaries, and local Markdown links. Run `claude plugin validate .` when changing the Claude Code adapter. The GitHub Actions workflow runs the portable check on pushes and pull requests.

For a change involving RML or scripting instructions, also verify the relevant command or syntax with a current Rive CLI. A valid package alone does not establish that an authored Rive scene compiles or behaves correctly.

Contributions submitted to this repository are offered under the repository's [AGPL-3.0-only license](LICENSE).
