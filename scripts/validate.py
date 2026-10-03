"""Validate the portable IEE package from the repository root."""

import json
import re
import sys
from pathlib import Path
from urllib.request import urlopen

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
ERRORS = []
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
LOCAL_LINK = re.compile(r"\]\(([^)]+)\)")
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
FIELDS = {"name", "description", "license", "allowed-tools", "metadata"}


def fail(location, message):
    ERRORS.append(f"{location}: {message}")


def validate_json(filename):
    path = ROOT / filename
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        schema_url = data["$schema"]
        if schema_url != f"https://agent-plugins.org/schemas/1.0.0/{filename.replace('json', 'schema.json')}":
            raise ValueError("unexpected Agent Plugins schema version")
        with urlopen(schema_url, timeout=15) as response:
            schema = json.load(response)
        jsonschema.validate(data, schema)
    except (OSError, ValueError, KeyError, jsonschema.ValidationError) as exc:
        fail(filename, str(exc))


def validate_skill(directory):
    path = directory / "SKILL.md"
    if not path.is_file():
        fail(directory.relative_to(ROOT), "missing SKILL.md")
        return
    content = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    match = FRONTMATTER.match(content)
    if not match:
        fail(path.relative_to(ROOT), "missing YAML frontmatter")
        return
    try:
        meta = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        fail(path.relative_to(ROOT), f"invalid YAML: {exc}")
        return
    if not isinstance(meta, dict):
        fail(path.relative_to(ROOT), "frontmatter must be an object")
        return
    unknown = set(meta) - FIELDS
    if unknown:
        fail(path.relative_to(ROOT), f"unsupported cross-client fields: {sorted(unknown)}")
    name = meta.get("name")
    if not isinstance(name, str) or len(name) > 64 or not NAME.fullmatch(name) or name != directory.name:
        fail(path.relative_to(ROOT), "name must match its lowercase skill directory")
    description = meta.get("description")
    if not isinstance(description, str) or not 1 <= len(description) <= 1024:
        fail(path.relative_to(ROOT), "description must be 1–1024 characters")


def validate_files():
    for path in ROOT.rglob("*"):
        if any(part in {".git", ".venv", "__pycache__"} for part in path.relative_to(ROOT).parts):
            continue
        resolved = path.resolve()
        if not resolved.is_relative_to(ROOT):
            fail(path.relative_to(ROOT), "path escapes plugin root")
        if not path.is_file() or path.suffix.lower() != ".md":
            continue
        skill_root = next((skill for skill in SKILLS.iterdir() if skill.is_dir() and path.is_relative_to(skill)), None)
        for target in LOCAL_LINK.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            destination = (path.parent / target.split("#", 1)[0]).resolve()
            if not destination.is_file() or (skill_root and not destination.is_relative_to(skill_root)):
                fail(path.relative_to(ROOT), f"invalid local link: {target}")


def validate_adapters():
    try:
        portable = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        mcp = json.loads((ROOT / "mcp.json").read_text(encoding="utf-8"))
        claude = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        claude_mcp = json.loads((ROOT / ".mcp.json").read_text(encoding="utf-8"))
        claude_market = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        codex_market = json.loads((ROOT / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
        if (claude["name"], claude["version"]) != (portable["name"], portable["version"]):
            fail(".claude-plugin/plugin.json", "name or version differs from portable manifest")
        if claude_mcp["mcpServers"]["rive-editor"]["url"] != mcp["mcpServers"]["rive-editor"]["url"]:
            fail(".mcp.json", "Editor URL differs from portable MCP configuration")
        for location, market in ((".claude-plugin/marketplace.json", claude_market), (".agents/plugins/marketplace.json", codex_market)):
            if market["plugins"][0]["name"] != portable["name"]:
                fail(location, "plugin name differs from portable manifest")
    except (OSError, ValueError, KeyError, IndexError, TypeError) as exc:
        fail("client adapters", str(exc))


def main():
    validate_json("plugin.json")
    validate_json("mcp.json")
    if not SKILLS.is_dir():
        fail("skills", "missing skill directory")
    else:
        for directory in sorted(SKILLS.iterdir()):
            if directory.is_dir():
                validate_skill(directory)
    validate_files()
    validate_adapters()
    for error in ERRORS:
        print(error, file=sys.stderr)
    if ERRORS:
        return 1
    print("Valid Agent Plugins manifests, skills, package paths, and local links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
