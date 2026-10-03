# IEE Core

IEE Core is a portable [Agent Plugin](https://agent-plugins.org/specification) for making original interactive work in Rive. Its 13 [Agent Skills](https://agentskills.io/specification) guide an agent through visual direction, scene structure, scripting, motion, state machines, data, layouts, rigging, Editor work, and review. The package also declares the Rive desktop Editor MCP connection.

IEE is a curated creative workflow. It helps an agent make and check a Rive artifact using the tools available in its environment. It does not provide host application runtime integration or bundle the Rive CLI, Editor, or documentation.

## Install

The repository root is the plugin root. Choose the install path for your agent:

### Claude Code

```sh
claude plugin marketplace add nonomnonom/iee
claude plugin install iee-core@iee
```

Start a new session and invoke `/iee-core:iee`, or let Claude select a focused skill. Claude Code loads the native `.mcp.json` connection when the Rive desktop Editor is running. [Claude Code plugin installation](https://code.claude.com/docs/en/plugin-marketplaces)

### Codex

```sh
codex plugin marketplace add nonomnonom/iee
codex plugin add iee-core@iee
```

Start a new session and invoke `$iee`, or ask Codex to use IEE for a Rive work. Codex reads the portable `plugin.json`, `skills/`, and `mcp.json`. [Codex plugin packaging and marketplaces](https://developers.openai.com/plugins/build/plugins)

### GitHub Copilot CLI and VS Code

```sh
copilot plugin install nonomnonom/iee
```

In VS Code, run **Chat: Install Plugin From Source** and enter `https://github.com/nonomnonom/iee`. Both clients support the root Agent Plugins manifest. [Copilot CLI install reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference) · [VS Code install guide](https://code.visualstudio.com/docs/agent-customization/agent-plugins)

### Other agents

Use the client's Agent Plugins installer with `https://github.com/nonomnonom/iee`, or clone the repository and point the client at the directory containing `plugin.json`:

```sh
git clone https://github.com/nonomnonom/iee.git
```

For a client that supports Agent Skills but not full plugins, install just the skills with `npx skills add nonomnonom/iee` or import the desired directories under `skills/`. A skills-only install does not configure Editor MCP; add `http://127.0.0.1:9791/mcp` separately in that client. [Skills CLI](https://www.skills.sh/docs/cli) · [Compatible Agent Plugins clients](https://agent-plugins.org/compatible-clients)

## Before authoring

- For a text project, install the [Rive CLI](https://rive.app/docs/cli/getting-started) and give the agent filesystem and shell access. The installed CLI is the version-matched technical reference: use `rive docs --list`, relevant `rive docs` topics, and `rive schema` before authoring.
- For an open Editor file, run the [Rive desktop Editor MCP server](https://rive.app/docs/editor/ai/mcp) and use a client that supports Streamable HTTP MCP. `mcp.json` connects to `http://127.0.0.1:9791/mcp`.

Start with the `iee` skill for a complete work. Use a focused skill for a specific craft task.

## Skills

| Skill | Scope |
| --- | --- |
| `iee` | Direct a complete Rive work and choose the authoring surface |
| `iee-design` | Visual direction and composition |
| `iee-rml` | Editable scene structure in Rive Markup Language |
| `iee-luau` | Luau scripting |
| `iee-animascript` | AnimaScript and WebAssembly scripting |
| `iee-wgsl` | Shader effects |
| `iee-motion` | Timing and animation craft |
| `iee-state-machines` | Interaction states and transitions |
| `iee-data-binding` | Data models and bindings |
| `iee-layouts` | Responsive scene layout |
| `iee-rigging` | Bones and deformation |
| `iee-mcp` | Editing through the desktop Editor MCP |
| `iee-review` | Visual, behavior, and delivery verification |

## Compatibility

An Agent Plugins client with skills support can load all 13 skills. MCP support is optional; an unavailable Editor connection does not invalidate the skills. A client that supports only MCP can connect to the Editor but cannot load the IEE instructions. Other agents need their own import or adapter.

`127.0.0.1` refers to the machine running the agent client. A cloud agent cannot reach a desktop Editor on the user's machine through this URL by default. CLI workflows need a Rive CLI installation and local file access. Client capabilities and permissions remain client-specific.

## Repository layout

```text
plugin.json        Agent Plugins 1.0.0 manifest
mcp.json           Optional Rive Editor MCP connection
skills/            Portable skill packages and task-specific references
.github/workflows/ Package validation
.agents/plugins/    Codex marketplace catalog
.claude-plugin/    Claude Code marketplace and manifest
.mcp.json         Claude Code's Editor MCP configuration
```

This repository contains only `iee-core`. Future IEE plugins for particular styles or kinds of work are separate repositories and packages. Agent Plugins 1.0.0 has no portable dependency field between packages.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the source and validation rules. IEE is an independent project and is not affiliated with Rive.

## License

Copyright 2026 nonomnonom. IEE Core is licensed under the [GNU Affero General Public License v3.0 only](LICENSE). Contributions are accepted under the same license.
