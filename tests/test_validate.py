import importlib.util
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location(
    "validate", Path(__file__).resolve().parents[1] / "scripts" / "validate.py"
)
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class PackageBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.skills = self.root / "skills"
        self.skills.mkdir()
        self.errors = []
        self.patch = patch.multiple(
            validator, ROOT=self.root, SKILLS=self.skills, ERRORS=self.errors
        )
        self.patch.start()
        self.addCleanup(self.patch.stop)

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return target

    def test_local_reference_checkout_does_not_become_plugin_content(self):
        self.write(".refrence/example/README.md", "[example](does-not-exist.md)")
        validator.validate_files()
        self.assertEqual(self.errors, [])

    def test_broken_packaged_reference_still_fails(self):
        self.write("skills/example/SKILL.md", "[guide](references/missing.md)")
        validator.validate_files()
        self.assertEqual(len(self.errors), 1)
        self.assertIn("invalid local link: references/missing.md", self.errors[0])

    def test_reference_named_folder_inside_skill_is_still_validated(self):
        self.write("skills/example/.refrence/guide.md", "[guide](missing.md)")
        validator.validate_files()
        self.assertEqual(len(self.errors), 1)

    def test_skill_cannot_depend_on_a_sibling_checkout(self):
        self.write(".refrence/example/README.md", "External reference")
        self.write("skills/example/SKILL.md", "[guide](../../.refrence/example/README.md)")
        validator.validate_files()
        self.assertEqual(len(self.errors), 1)

    def test_packaged_skill_local_reference_remains_valid(self):
        self.write("skills/example/SKILL.md", "[guide](references/guide.md#section)")
        self.write("skills/example/references/guide.md", "# Section")
        validator.validate_files()
        self.assertEqual(self.errors, [])

    def test_root_document_cannot_depend_on_a_file_outside_package(self):
        self.write("outside.md", "Not packaged")
        package = self.root / "plugin"
        (package / "skills").mkdir(parents=True)
        (package / "README.md").write_text("[guide](../outside.md)", encoding="utf-8")
        with patch.multiple(validator, ROOT=package, SKILLS=package / "skills"):
            validator.validate_files()
        self.assertEqual(len(self.errors), 1)

    def test_missing_skills_reports_failure_without_crashing(self):
        self.skills.rmdir()
        self.write("README.md", "Package documentation")
        with (patch.object(validator, "validate_json"),
              patch.object(validator, "validate_adapters"),
              patch("sys.stderr", new_callable=io.StringIO) as stderr):
            status = validator.main()
        self.assertEqual(status, 1)
        self.assertIn("skills: missing skill directory", self.errors)
        self.assertIn("skills: missing skill directory", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
