"""Parity tests for the evals/ prompt bridge.

Guards against the eval harness silently diverging from production
prompt assembly: build_current() must produce byte-identical output to
calling _build_url_mode_prompt_with_text directly, and the prompt_path
override must actually swap the template.

Run:
    uv run python -m unittest tests.test_promptfoo_bridge
"""

import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "evals" / "lib"))
sys.path.insert(0, str(REPO_ROOT / "evals" / "prompts"))

MANIFEST_PATH = REPO_ROOT / "evals" / "fixtures" / "manifest.json"


class TestPromptParity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not MANIFEST_PATH.exists():
            raise unittest.SkipTest(
                "fixtures/manifest.json not built — run "
                "`uv run --with pyyaml,pypdf evals/fixtures/build_fixtures.py`"
            )
        cls.manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    def test_build_current_matches_production_builder(self):
        from call_gemini_bridge import SCRIPTS_DIR, load_call_gemini
        import build_prompt

        cg = load_call_gemini()
        for fx in self.manifest[:3]:
            article_path = REPO_ROOT / "evals" / fx["article_text_path"]
            context = {
                "vars": {
                    "url": fx["url"],
                    "article_text_path": str(article_path),
                }
            }
            via_promptfoo = build_prompt.build_current(context)
            direct = cg._build_url_mode_prompt_with_text(
                fx["url"],
                article_path.read_text(encoding="utf-8"),
                str(SCRIPTS_DIR),
            )
            self.assertEqual(
                via_promptfoo,
                direct,
                f"fixture {fx['id']}: bridge output diverged from production builder",
            )

    def test_prompt_path_default_unchanged(self):
        """Explicitly passing the production template equals the default."""
        from call_gemini_bridge import SCRIPTS_DIR, load_call_gemini

        cg = load_call_gemini()
        fx = self.manifest[0]
        article_text = (REPO_ROOT / "evals" / fx["article_text_path"]).read_text(
            encoding="utf-8"
        )
        default = cg._build_url_mode_prompt_with_text(
            fx["url"], article_text, str(SCRIPTS_DIR)
        )
        explicit = cg._build_url_mode_prompt_with_text(
            fx["url"],
            article_text,
            str(SCRIPTS_DIR),
            prompt_path=str(REPO_ROOT / "prompts" / "summarize-json.prompt"),
        )
        self.assertEqual(default, explicit)

    def test_prompt_path_override_swaps_template(self):
        from call_gemini_bridge import SCRIPTS_DIR, load_call_gemini

        cg = load_call_gemini()
        fx = self.manifest[0]
        with tempfile.NamedTemporaryFile(
            "w", suffix=".prompt", delete=False, encoding="utf-8"
        ) as tmp:
            tmp.write("VARIANT MARKER\n\n# Article Content\n\n{{fetch:\"{{url}}\"}}")
            tmp_path = tmp.name
        try:
            result = cg._build_url_mode_prompt_with_text(
                fx["url"], "dummy article text", str(SCRIPTS_DIR), prompt_path=tmp_path
            )
        finally:
            Path(tmp_path).unlink()
        self.assertIn("VARIANT MARKER", result)
        self.assertIn("dummy article text", result)


if __name__ == "__main__":
    unittest.main()
