#!/usr/bin/env python3
from pathlib import Path
import re
import sys

DOC = Path(__file__).resolve().parents[1] / "docs" / "OPPORTUNITY_READINESS.md"

FORBIDDEN_PATTERNS = {
    "credential": re.compile(r"(?:ghp_|sk-|lin_api_|cfat_)[A-Za-z0-9_-]{8,}"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}

REQUIRED_HEADINGS = [
    "# Fiducia startup-program and OSS-funding readiness",
    "## Safety boundary",
    "## Evidence required before claims",
    "## Workflow",
]


def validate(text: str) -> list[str]:
    errors: list[str] = []
    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"missing required heading: {heading}")
    for name, pattern in FORBIDDEN_PATTERNS.items():
        if pattern.search(text):
            errors.append(f"forbidden {name}-shaped material found")
    if "unverified" not in text:
        errors.append("missing explicit unverified-facts state")
    if "Do not accept terms" not in text:
        errors.append("missing consequential-commitment guardrail")
    return errors


def main() -> int:
    text = DOC.read_text(encoding="utf-8")
    errors = validate(text)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("opportunity readiness document passed fail-closed validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
