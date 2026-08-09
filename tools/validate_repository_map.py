#!/usr/bin/env python3
"""Validate the public fiducia-cloud repository routing map.

This validator intentionally checks only organization routing metadata. It does not
claim implementation, deployment, release, security, or maturity status.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

ALLOWED_CATEGORIES = {
    "organization",
    "site",
    "core-runtime",
    "platform-service",
    "agent-control",
    "interface-tooling",
    "infra-test",
}
ALLOWED_VISIBILITIES = {"public", "private"}
EXPECTED_ARCHIVED = {"fiducia-customer-ui.web"}
EXPECTED_GITHUB_PROJECT_URL = "https://github.com/orgs/fiducia-cloud/projects/1"
EXPECTED_LINEAR_PROJECT_URL = (
    "https://linear.app/denman/project/fiducia-cloud-8fd5e1bec9d3"
)
ROOT_KEYS = {
    "schemaVersion",
    "generatedAt",
    "organization",
    "canonicalGitHubProject",
    "canonicalLinearProject",
    "totals",
    "repositories",
}
REPOSITORY_KEYS = {"name", "visibility", "archived", "defaultBranch", "category"}
SECRET_PATTERNS = (
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{20,}"),
    re.compile(r"(?i)bearer\s+[A-Za-z0-9._~-]{12,}"),
    re.compile(r"(?i)(?:access[_-]?token|api[_-]?key|password|secret)\s*[:=]\s*\S+"),
)


class ValidationError(ValueError):
    """Raised when repository routing metadata violates the public contract."""


def _require_exact_keys(value: dict[str, Any], expected: set[str], label: str) -> None:
    actual = set(value)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise ValidationError(f"{label} keys mismatch; missing={missing}, extra={extra}")


def _require_public_https_url(value: Any, expected: str, label: str) -> None:
    if value != expected:
        raise ValidationError(f"{label} must be exactly {expected}")
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
        raise ValidationError(f"{label} must be a credential-free HTTPS URL")
    if parsed.query or parsed.fragment:
        raise ValidationError(f"{label} must not contain query parameters or fragments")


def _reject_secrets(value: Any, path: str = "$") -> None:
    if isinstance(value, dict):
        for key, child in value.items():
            _reject_secrets(child, f"{path}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _reject_secrets(child, f"{path}[{index}]")
    elif isinstance(value, str):
        for pattern in SECRET_PATTERNS:
            if pattern.search(value):
                raise ValidationError(f"credential-shaped value found at {path}")


def validate_repository_map(document: dict[str, Any]) -> None:
    if not isinstance(document, dict):
        raise ValidationError("root must be an object")
    _reject_secrets(document)
    _require_exact_keys(document, ROOT_KEYS, "root")

    if document["schemaVersion"] != 1:
        raise ValidationError("schemaVersion must be 1")
    if document["generatedAt"] != "2026-08-05":
        raise ValidationError("generatedAt must be the audited snapshot date 2026-08-05")
    if document["organization"] != "fiducia-cloud":
        raise ValidationError("organization must be fiducia-cloud")

    github_project = document["canonicalGitHubProject"]
    if not isinstance(github_project, dict):
        raise ValidationError("canonicalGitHubProject must be an object")
    _require_exact_keys(github_project, {"number", "url"}, "canonicalGitHubProject")
    if github_project["number"] != 1:
        raise ValidationError("canonical GitHub Project number must be 1")
    _require_public_https_url(
        github_project["url"], EXPECTED_GITHUB_PROJECT_URL, "canonicalGitHubProject.url"
    )

    linear_project = document["canonicalLinearProject"]
    if not isinstance(linear_project, dict):
        raise ValidationError("canonicalLinearProject must be an object")
    _require_exact_keys(linear_project, {"name", "url"}, "canonicalLinearProject")
    if linear_project["name"] != "fiducia-cloud":
        raise ValidationError("canonical Linear project name must be fiducia-cloud")
    _require_public_https_url(
        linear_project["url"], EXPECTED_LINEAR_PROJECT_URL, "canonicalLinearProject.url"
    )

    totals = document["totals"]
    if not isinstance(totals, dict):
        raise ValidationError("totals must be an object")
    _require_exact_keys(totals, {"repositories", "active", "archived"}, "totals")
    for key, value in totals.items():
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValidationError(f"totals.{key} must be a non-negative integer")

    repositories = document["repositories"]
    if not isinstance(repositories, list) or not repositories:
        raise ValidationError("repositories must be a non-empty array")

    names: list[str] = []
    archived_names: set[str] = set()
    for index, repository in enumerate(repositories):
        if not isinstance(repository, dict):
            raise ValidationError(f"repositories[{index}] must be an object")
        _require_exact_keys(repository, REPOSITORY_KEYS, f"repositories[{index}]")

        name = repository["name"]
        if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9._-]+", name):
            raise ValidationError(f"repositories[{index}].name is invalid")
        names.append(name)

        if repository["visibility"] not in ALLOWED_VISIBILITIES:
            raise ValidationError(f"repository {name} has invalid visibility")
        if not isinstance(repository["archived"], bool):
            raise ValidationError(f"repository {name} archived must be boolean")
        if repository["defaultBranch"] != "main":
            raise ValidationError(f"repository {name} defaultBranch must be main")
        if repository["category"] not in ALLOWED_CATEGORIES:
            raise ValidationError(f"repository {name} has invalid category")
        if repository["archived"]:
            archived_names.add(name)

    if names != sorted(names):
        raise ValidationError("repositories must be sorted by name")
    if len(names) != len(set(names)):
        raise ValidationError("repository names must be unique")
    if archived_names != EXPECTED_ARCHIVED:
        raise ValidationError(
            f"archived repository set must be {sorted(EXPECTED_ARCHIVED)}, got {sorted(archived_names)}"
        )

    actual_total = len(repositories)
    actual_archived = len(archived_names)
    actual_active = actual_total - actual_archived
    expected_totals = {
        "repositories": actual_total,
        "active": actual_active,
        "archived": actual_archived,
    }
    if totals != expected_totals:
        raise ValidationError(f"totals mismatch; expected {expected_totals}, got {totals}")


def load_and_validate(path: Path) -> dict[str, Any]:
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValidationError(f"unable to read valid JSON from {path}: {error}") from error
    validate_repository_map(document)
    return document


def main(argv: list[str]) -> int:
    path = Path(argv[1]) if len(argv) > 1 else Path("docs/repository-map.json")
    try:
        document = load_and_validate(path)
    except ValidationError as error:
        print(f"repository map validation failed: {error}", file=sys.stderr)
        return 1
    print(
        "repository map valid: "
        f"{document['totals']['repositories']} total, "
        f"{document['totals']['active']} active, "
        f"{document['totals']['archived']} archived"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
