#!/usr/bin/env python3
"""Fail-closed validator for the public Fiducia opportunity-operations policy."""

from __future__ import annotations

from pathlib import Path
import re
import sys

DOC = Path(__file__).resolve().parents[1] / "docs" / "OPPORTUNITY_OPERATIONS.md"

REQUIRED_HEADINGS = (
    "# Fiducia opportunity operations policy",
    "## Ownership",
    "## Public-data boundary",
    "## Evidence states",
    "## Mailbox identity boundary",
    "## Approval boundary",
    "## Update workflow",
)

REQUIRED_PHRASES = (
    "fiducia-cloud/fiducia-infra",
    "approved-private-application-control-plane",
    "Linear is authoritative",
    "deterministic exact-revision identity",
    "Presence in To/Cc",
    "does not prove sender authentication",
    "Alex has approved that exact revision",
)

FORBIDDEN_PATTERNS = (
    ("GitHub token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")),
    ("Linear token", re.compile(r"\blin_api_[A-Za-z0-9]{20,}\b")),
    ("Cloudflare token", re.compile(r"\bcfat_[A-Za-z0-9_-]{20,}\b")),
    ("OpenAI-style key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
    ("AWS access key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("private key", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("credentialed URL", re.compile(r"https?://[^\s/@:]+:[^\s/@]+@")),
    (
        "secret assignment",
        re.compile(
            r"\b(?:password|passwd|secret|api[_ -]?key|access[_ -]?token|refresh[_ -]?token)\b"
            r"\s*[:=]\s*[\"']?[A-Za-z0-9/+_.=-]{12,}",
            re.IGNORECASE,
        ),
    ),
    ("mailbox header", re.compile(r"^(?:From|To|Cc|Bcc|Subject|Message-ID|Return-Path|Received):", re.MULTILINE)),
    ("currency amount", re.compile(r"(?<!\w)(?:US?\$|[$€£¥])\s?\d[\d,]*(?:\.\d+)?|\b\d[\d,]*(?:\.\d+)?\s*(?:USD|EUR|GBP|JPY)\b", re.IGNORECASE)),
    ("dated provider fact", re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")),
    ("static opportunity table", re.compile(r"\|\s*Opportunity\s*\|", re.IGNORECASE)),
    (
        "mailbox authentication overclaim",
        re.compile(r"hello@fiducia\.cloud\s+(?:is|was|has been)\s+(?:directly\s+)?(?:authenticated|connected)", re.IGNORECASE),
    ),
)


def validate(text: str) -> list[str]:
    errors: list[str] = []

    if "\r" in text:
        errors.append("CR characters are forbidden")

    for heading in REQUIRED_HEADINGS:
        if heading not in text:
            errors.append(f"missing required heading: {heading}")

    for phrase in REQUIRED_PHRASES:
        if phrase not in text:
            errors.append(f"missing required boundary phrase: {phrase}")

    for name, pattern in FORBIDDEN_PATTERNS:
        if pattern.search(text):
            errors.append(f"forbidden {name} material found")

    if text.count("hello@fiducia.cloud") != 1:
        errors.append("official company contact must appear exactly once")

    if "Do not duplicate provider-specific values" not in text:
        errors.append("missing provider-specific state ownership boundary")

    if "Approval for one revision does not authorize a changed revision" not in text:
        errors.append("missing stale-approval rejection boundary")

    return errors


def main() -> int:
    text = DOC.read_text(encoding="utf-8")
    errors = validate(text)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("opportunity operations policy passed fail-closed validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
