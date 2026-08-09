from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_repository_map", ROOT / "tools" / "validate_repository_map.py"
)
assert SPEC is not None and SPEC.loader is not None
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class RepositoryMapTest(unittest.TestCase):
    def setUp(self) -> None:
        self.document = json.loads(
            (ROOT / "docs" / "repository-map.json").read_text(encoding="utf-8")
        )

    def assert_validation_error(self, document: dict, message: str) -> None:
        with self.assertRaisesRegex(validator.ValidationError, message):
            validator.validate_repository_map(document)

    def test_current_map_is_valid(self) -> None:
        validator.validate_repository_map(self.document)

    def test_duplicate_repository_name_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        document["repositories"][1]["name"] = document["repositories"][0]["name"]
        document["repositories"].sort(key=lambda item: item["name"])
        self.assert_validation_error(document, "unique")

    def test_totals_mismatch_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        document["totals"]["active"] -= 1
        self.assert_validation_error(document, "totals mismatch")

    def test_unexpected_archived_repository_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        for repository in document["repositories"]:
            if repository["name"] == "fiducia-admin.rs":
                repository["archived"] = True
        document["totals"]["active"] -= 1
        document["totals"]["archived"] += 1
        self.assert_validation_error(document, "archived repository set")

    def test_secret_shaped_value_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        document["canonicalLinearProject"]["name"] = "ghp_abcdefghijklmnopqrstuvwxyz123456"
        self.assert_validation_error(document, "credential-shaped")

    def test_wrong_github_project_url_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        document["canonicalGitHubProject"]["url"] = (
            "https://github.com/orgs/fiducia-cloud/projects/2"
        )
        self.assert_validation_error(document, "must be exactly")

    def test_wrong_linear_project_identity_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        document["canonicalLinearProject"]["name"] = "github.com/fiducia-cloud"
        self.assert_validation_error(document, "project name")

    def test_invalid_category_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        document["repositories"][0]["category"] = "invented"
        self.assert_validation_error(document, "invalid category")

    def test_unsorted_repositories_are_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        document["repositories"][0], document["repositories"][1] = (
            document["repositories"][1],
            document["repositories"][0],
        )
        self.assert_validation_error(document, "sorted")

    def test_non_main_default_branch_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        document["repositories"][0]["defaultBranch"] = "master"
        self.assert_validation_error(document, "defaultBranch must be main")


if __name__ == "__main__":
    unittest.main()
