import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_opportunity_operations", ROOT / "tools" / "validate_opportunity_operations.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class OpportunityOperationsPolicyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.valid = (ROOT / "docs" / "OPPORTUNITY_OPERATIONS.md").read_text(encoding="utf-8")

    def test_current_document_is_valid(self):
        self.assertEqual([], MODULE.validate(self.valid))

    def test_requires_every_heading(self):
        text = self.valid.replace("## Approval boundary", "## Removed")
        self.assertTrue(any("Approval boundary" in error for error in MODULE.validate(text)))

    def test_rejects_github_token(self):
        self.assert_rejected("ghp_123456789012345678901234567890123456", "GitHub token")

    def test_rejects_linear_token(self):
        self.assert_rejected("lin_api_123456789012345678901234567890", "Linear token")

    def test_rejects_cloudflare_token(self):
        self.assert_rejected("cfat_123456789012345678901234567890", "Cloudflare token")

    def test_rejects_aws_access_key(self):
        self.assert_rejected("AKIA1234567890ABCDEF", "AWS access key")

    def test_rejects_private_key(self):
        self.assert_rejected("-----BEGIN PRIVATE KEY-----", "private key")

    def test_rejects_mailbox_headers(self):
        self.assert_rejected("Subject: private application reply", "mailbox header")

    def test_rejects_currency_amounts(self):
        self.assert_rejected("A provider offers $10000.", "currency amount")

    def test_rejects_dated_provider_facts(self):
        self.assert_rejected("Verified on 2026-08-19.", "dated provider fact")

    def test_rejects_static_opportunity_table(self):
        self.assert_rejected("| Opportunity | Value |", "static opportunity table")

    def test_rejects_mailbox_authentication_overclaim(self):
        self.assert_rejected("hello@fiducia.cloud is directly authenticated", "mailbox authentication overclaim")

    def test_requires_one_official_contact(self):
        text = self.valid.replace("`hello@fiducia.cloud`", "the company mailbox")
        self.assertIn("official company contact must appear exactly once", MODULE.validate(text))

    def test_requires_stale_approval_boundary(self):
        text = self.valid.replace(
            "Approval for one revision does not authorize a changed revision",
            "An approval is reusable",
        )
        self.assertIn("missing stale-approval rejection boundary", MODULE.validate(text))

    def assert_rejected(self, injected: str, expected: str):
        errors = MODULE.validate(self.valid + "\n" + injected + "\n")
        self.assertTrue(any(expected in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
