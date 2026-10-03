"""Create an isolated repair scenario from the installed Rive sample."""

import argparse
import shutil
import subprocess
from pathlib import Path


def prepare(rive, output):
    if output.exists():
        raise ValueError("output must be a new directory; existing work is never replaced")
    result = subprocess.run(
        [rive, "samples", "--path"], capture_output=True, text=True, check=True
    )
    sample = Path(result.stdout.strip()) / "rml_vm_input"
    scene = (sample / "scene.rml").read_text(encoding="utf-8")
    original = 'name="settings" id="0:13"'
    if scene.count(original) != 1:
        raise ValueError("installed sample differs from this scenario; inspect it before adapting the fixture")
    required = ["scene.rml", "main.luau", "rive.yaml"]
    for name in required:
        if not (sample / name).is_file():
            raise ValueError(f"installed sample is missing {name}")
    output.mkdir(parents=True)
    for name in required:
        shutil.copy2(sample / name, output / name)
    (output / "scene.rml").write_text(
        scene.replace(original, 'name="setting" id="0:13"'), encoding="utf-8"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rive", required=True, help="installed CLI executable")
    parser.add_argument("--output", required=True, type=Path, help="new isolated project directory")
    args = parser.parse_args()
    try:
        prepare(args.rive, args.output)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Cannot prepare fixture: {exc}\n")
    print(args.output.resolve())


if __name__ == "__main__":
    main()
