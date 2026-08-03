from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "policy_validator", ROOT / "scripts" / "validate_semantic_conflict_policy.py"
)
assert SPEC is not None and SPEC.loader is not None
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


FIXTURE_PATHS = tuple(
    dict.fromkeys(
        (
            *validator.HUMAN_POLICY_FILES,
            *validator.COMMUNITY_FILES,
            *validator.REUSABLE_WORKFLOWS,
            Path("README.md"),
            Path("project-context.yaml"),
            Path("org-context-manifest.json"),
            Path("organization-policy.json"),
            Path(".github/workflows/org-context-integrity.yml"),
        )
    )
)


class OrganizationPolicyValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        for relative in FIXTURE_PATHS:
            source = ROOT / relative
            target = self.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _json(self, relative: str) -> dict[str, object]:
        path = self.root / relative
        return json.loads(path.read_text(encoding="utf-8"))

    def _write_json(self, relative: str, payload: object) -> None:
        (self.root / relative).write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")

    def assertFailureContains(self, expected: str) -> None:  # noqa: N802
        errors = validator.validate_repository(self.root)
        self.assertTrue(
            any(expected.casefold() in error.casefold() for error in errors),
            f"expected {expected!r} in {errors!r}",
        )

    def test_accepts_complete_policy_bundle(self) -> None:
        self.assertEqual(validator.validate_repository(self.root), [])

    def test_rejects_missing_primary_agent_instructions(self) -> None:
        (self.root / "AGENTS.md").unlink()
        self.assertFailureContains("missing required file: AGENTS.md")

    def test_rejects_symlinked_primary_agent_instructions(self) -> None:
        agents = self.root / "AGENTS.md"
        agents.unlink()
        agents.symlink_to(self.root / "CONTRIBUTING.md")
        self.assertFailureContains("must be a regular file: AGENTS.md")

    def test_rejects_missing_exact_merge_directive(self) -> None:
        path = self.root / "AGENTS.md"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "avoid git rebase in favor of git merge", "prefer merging"
            ),
            encoding="utf-8",
        )
        self.assertFailureContains("avoid git rebase in favor of git merge")

    def test_rejects_weakened_history_window(self) -> None:
        payload = self._json("project-context.yaml")
        payload["git_conflict_resolution"]["history_lookback_commits"]["minimum"] = 1
        self._write_json("project-context.yaml", payload)
        self.assertFailureContains("exact 3–10 commit history contract")

    def test_rejects_missing_external_repository_scope(self) -> None:
        payload = self._json("project-context.yaml")
        payload["git_conflict_resolution"]["context_scope"].remove(
            "relevant_external_github_organization_repositories"
        )
        self._write_json("project-context.yaml", payload)
        self.assertFailureContains("relevant_external_github_organization_repositories")

    def test_rejects_wholesale_side_selection_shortcut(self) -> None:
        payload = self._json("project-context.yaml")
        payload["git_conflict_resolution"]["forbidden_shortcuts"].remove("wholesale_theirs")
        self._write_json("project-context.yaml", payload)
        self.assertFailureContains("wholesale_theirs")

    def test_rejects_manifest_drift(self) -> None:
        path = self.root / "profile" / "README.md"
        path.write_text(path.read_text(encoding="utf-8") + "drift\n", encoding="utf-8")
        self.assertFailureContains("manifest hash mismatch: profile/README.md")

    def test_rejects_unresolved_conflict_marker(self) -> None:
        path = self.root / "CONTRIBUTING.md"
        path.write_text("<<<<<<< HEAD\n" + path.read_text(encoding="utf-8"), encoding="utf-8")
        self.assertFailureContains("unresolved Git conflict marker")

    def test_rejects_incomplete_pull_request_checklist(self) -> None:
        path = self.root / ".github/PULL_REQUEST_TEMPLATE.md"
        path.write_text("Semantic full context ours theirs conceptual merge 3–10 organization external tests\n- [ ] one\n", encoding="utf-8")
        self.assertFailureContains("at least twelve checklist items")

    def test_rejects_missing_lowercase_pull_request_template(self) -> None:
        (self.root / ".github/pull_request_template.md").unlink()
        self.assertFailureContains("missing required file: .github/pull_request_template.md")

    def test_rejects_missing_linear_tracking_language(self) -> None:
        path = self.root / "CONTRIBUTING.md"
        path.write_text(path.read_text(encoding="utf-8").replace("Linear", "tracker"), encoding="utf-8")
        self.assertFailureContains("linear")

    def test_rejects_untracked_drive_by_changes(self) -> None:
        payload = self._json("organization-policy.json")
        payload["work_tracking"]["untracked_drive_by_changes"] = "allowed"
        self._write_json("organization-policy.json", payload)
        self.assertFailureContains("untracked_drive_by_changes")

    def test_rejects_false_inheritance_claim(self) -> None:
        payload = self._json("organization-policy.json")
        payload["policy_inheritance"][
            "organization_dotgithub_agent_instructions_are_automatically_inherited"
        ] = True
        self._write_json("organization-policy.json", payload)
        self.assertFailureContains("automatically_inherited")

    def test_rejects_removed_destructive_git_command(self) -> None:
        payload = self._json("organization-policy.json")
        payload["safe_change_policy"]["prohibited_git_commands"].remove("git clean")
        self._write_json("organization-policy.json", payload)
        self.assertFailureContains("git clean")

    def test_rejects_removed_destructive_filesystem_command(self) -> None:
        payload = self._json("organization-policy.json")
        payload["safe_change_policy"]["prohibited_filesystem_commands"].remove("sed")
        self._write_json("organization-policy.json", payload)
        self.assertFailureContains("sed")

    def test_rejects_removed_destructive_data_operation(self) -> None:
        payload = self._json("organization-policy.json")
        payload["safe_change_policy"]["prohibited_data_operations"].remove("TRUNCATE")
        self._write_json("organization-policy.json", payload)
        self.assertFailureContains("TRUNCATE")

    def test_rejects_removed_destructive_infrastructure_operation(self) -> None:
        payload = self._json("organization-policy.json")
        payload["safe_change_policy"]["prohibited_infrastructure_operations"].remove(
            "terraform destroy"
        )
        self._write_json("organization-policy.json", payload)
        self.assertFailureContains("terraform destroy")

    def test_rejects_removed_governance_bypass(self) -> None:
        payload = self._json("organization-policy.json")
        payload["safe_change_policy"]["prohibited_release_governance_operations"].remove(
            "--no-verify"
        )
        self._write_json("organization-policy.json", payload)
        self.assertFailureContains("--no-verify")

    def test_rejects_unpinned_checkout_in_reusable_workflow(self) -> None:
        path = self.root / ".github/workflows/reusable-organization-policy.yml"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
                "actions/checkout@main",
            ),
            encoding="utf-8",
        )
        self.assertFailureContains("full commit SHA")

    def test_rejects_unpinned_checkout_in_compatibility_workflow(self) -> None:
        path = self.root / ".github/workflows/agent-policy.yml"
        path.write_text(
            path.read_text(encoding="utf-8").replace(
                "actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1",
                "actions/checkout@v4",
            ),
            encoding="utf-8",
        )
        self.assertFailureContains("agent-policy.yml must pin")

    def test_rejects_write_all_permissions(self) -> None:
        path = self.root / ".github/workflows/agent-policy.yml"
        path.write_text(path.read_text(encoding="utf-8") + "\npermissions: write-all\n", encoding="utf-8")
        self.assertFailureContains("write-all")

    def test_rejects_missing_security_fallback(self) -> None:
        (self.root / "SECURITY.md").unlink()
        self.assertFailureContains("missing required file: SECURITY.md")

    def test_rejects_missing_compatibility_workflow(self) -> None:
        (self.root / ".github/workflows/agent-policy.yml").unlink()
        self.assertFailureContains("missing required file: .github/workflows/agent-policy.yml")


if __name__ == "__main__":
    unittest.main()
