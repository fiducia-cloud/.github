import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_opportunity_readiness", ROOT / "tools" / "validate_opportunity_readiness.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class OpportunityReadinessValidationTests(unittest.TestCase):
    def test_current_document_is_valid(self):
        text = (ROOT / "docs" / "OPPORTUNITY_READINESS.md").read_text(encoding="utf-8")
        self.assertEqual([], MODULE.validate(text))

    def test_rejects_credential_shaped_material(self):
        text = "\n".join(MODULE.REQUIRED_HEADINGS) + "\nunverified\nDo not accept terms\nghp_1234567890abcdef"
        self.assertTrue(any("credential" in error for error in MODULE.validate(text)))

    def test_requires_unverified_state(self):
        text = "\n".join(MODULE.REQUIRED_HEADINGS) + "\nDo not accept terms"
        self.assertIn("missing explicit unverified-facts state", MODULE.validate(text))

    def test_requires_commitment_guardrail(self):
        text = "\n".join(MODULE.REQUIRED_HEADINGS) + "\nunverified"
        self.assertIn("missing consequential-commitment guardrail", MODULE.validate(text))


if __name__ == "__main__":
    unittest.main()
