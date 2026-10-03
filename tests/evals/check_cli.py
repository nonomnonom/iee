"""Exercise installed Rive samples in a new directory; never mutate the installation.

Requires Pillow for pixel comparisons. These are tool capability checks, not agent
or artistic-quality evaluations. Captures still need visual review.
"""

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageChops


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rive", required=True)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.exists():
        parser.error("output must be a new directory")
    rive = str(Path(args.rive).resolve())
    samples = Path(subprocess.check_output([rive, "samples", "--path"], text=True).strip())
    output.mkdir(parents=True)
    report = {"version": subprocess.check_output([rive, "--version"], text=True).strip(),
              "kind": "installed-tool-capabilities", "checks": [], "commands": []}

    def run(sample, label, *flags, expected_exit=0):
        command = [rive, str(output / sample), *flags]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=180)
        (output / f"{label}.log").write_text(result.stdout + result.stderr, encoding="utf-8")
        report["commands"].append({"label": label, "argv": command, "exit_code": result.returncode})
        if result.returncode != expected_exit:
            raise RuntimeError(f"{label} failed: see {label}.log")
        return result.stdout + result.stderr

    def check(label, condition):
        report["checks"].append({"label": label, "passed": bool(condition)})
        if not condition:
            raise AssertionError(label)

    def capture(sample, label, *flags):
        run(sample, label, *flags, f"--screenshot={output / (label + '.png')}",
            f"--data-dump={output / (label + '.json')}")
        return json.loads((output / f"{label}.json").read_text(encoding="utf-8"))

    def pixels_differ(a, b):
        with Image.open(output / f"{a}.png") as first, Image.open(output / f"{b}.png") as second:
            return ImageChops.difference(first.convert("RGB"), second.convert("RGB")).getbbox() is not None

    def value(data, name):
        return next(p["value"] for p in data["viewModel"]["properties"] if p["path"] == name)

    try:
        for sample in ("keyboard_menu", "rml_vm_input", "wavy_effect_as", "tests_demo", "hello_rive"):
            shutil.copytree(samples / sample, output / sample)
            run(sample, sample + "-verify", "--verify")
        capture("keyboard_menu", "menu-rest", "--advance=1")
        selected = capture("keyboard_menu", "menu-down", "--advance=1", "--key=tab", "--key=down", "--advance=2",
                           f"--semantics={output / 'menu-semantics.json'}")
        check("focused down selects Options", value(selected, "index") == 1 and value(selected, "selectedLabel") == "Options")
        check("keyboard changes rendered selection", pixels_differ("menu-rest", "menu-down"))
        returned = capture("keyboard_menu", "menu-return", "--advance=1", "--key=tab", "--key=down", "--advance=2", "--key=up", "--advance=2")
        check("up returns to Play", value(returned, "index") == 0 and value(returned, "selectedLabel") == "Play")
        automatic = capture("keyboard_menu", "menu-auto-focus", "--advance=1", "--key=down", "--advance=2")
        check("authored entry focus accepts down without Tab", value(automatic, "index") == 1)
        semantics = json.loads((output / "menu-semantics.json").read_text())
        check("menu semantic label exposed", any(n["label"] == "Menu" and n["role"] == "list" for n in semantics["roots"]))
        for label, frames in (("vm-start", 1), ("vm-later", 30)):
            data = capture("rml_vm_input", label, "--data=settings/speed=2", f"--advance={frames}")
            nested = value(data, "settings")
            check(label + " receives nested speed", next(p["value"] for p in nested["properties"] if p["path"] == "settings/speed") == 2)
        check("Luau script advances visible geometry", pixels_differ("vm-start", "vm-later"))
        for label, frames in (("vm-zero-start", 1), ("vm-zero-later", 30)):
            capture("rml_vm_input", label, "--data=settings/speed=0", f"--advance={frames}")
        check("zero bound speed stops geometry", not pixels_differ("vm-zero-start", "vm-zero-later"))
        for label, frames in (("wasm-start", 1), ("wasm-later", 30)):
            capture("wavy_effect_as", label, f"--advance={frames}")
        check("AnimaScript path effect changes pixels", pixels_differ("wasm-start", "wasm-later"))
        failure = run("tests_demo", "authored-tests-red", "--test", expected_exit=6)
        check("test runner detects deliberate failure", "FAIL intentional failure" in failure and "6/7 passed" in failure)
        test_path = output / "tests_demo/mathutil_test.luau"
        source = test_path.read_text(encoding="utf-8")
        broken = "expect(mathutil.clamp(10, 0, 5)).is(10)"
        check("known negative fixture still matches", source.count(broken) == 1)
        test_path.write_text(source.replace(broken, "expect(mathutil.clamp(10, 0, 5)).is(5)"), encoding="utf-8")
        passed = run("tests_demo", "authored-tests-green", "--test")
        check("corrected fixture runs all seven tests", "7/7 passed" in passed)
        run("keyboard_menu", "native-export", "--once")
        artifact = output / "keyboard_menu/build/keyboard_menu.riv"
        check("native export exists", artifact.is_file() and artifact.stat().st_size > 0)
        report["export_sha256"] = hashlib.sha256(artifact.read_bytes()).hexdigest()
        run("hello_rive", "assets-clean", "--once")
        scripted_export = output / "hello_rive/build/hello_rive.riv"
        clean = scripted_export.read_bytes()
        (output / "hello_rive/review.txt").write_text("Private review evidence.\n" * 200, encoding="utf-8")
        run("hello_rive", "assets-with-report", "--once")
        check("script-only project bundles report without exclusion", scripted_export.stat().st_size > len(clean))
        config = output / "hello_rive/rive.yaml"
        config.write_text(config.read_text(encoding="utf-8") + "\nexclude:\n  - review.txt\n", encoding="utf-8")
        run("hello_rive", "assets-excluded", "--once")
        check("exclusion restores exact clean export", scripted_export.read_bytes() == clean)
        report["status"] = "passed"
    except (OSError, subprocess.SubprocessError, AssertionError, RuntimeError, KeyError, StopIteration) as exc:
        report["status"] = "failed"
        report["error"] = str(exc)
    finally:
        (output / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
