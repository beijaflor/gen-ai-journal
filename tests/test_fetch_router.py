#!/usr/bin/env python3
"""Tests for `scripts/modules/fetch_router.py` (Issue #121).

Asserts that:

1. ``needs_spa_render`` routes the SPA-render allowlist through the headless
   path AND keeps the ``developers.openai.com`` happy path on the curl path.
2. ``looks_blocked`` fires on each captured failure-mode fixture (SPA shell
   from qwen.ai, SPA shell from *.notion.site, anti-bot interstitial from
   openai.com/index/*) but does NOT fire on the happy-path fixture
   (server-rendered developers.openai.com article).
3. ``build_blocked_stub`` produces a body that humans cannot miss when
   scrolling through ``workdesk/summaries/`` (must contain the literal
   ``BLOCKED:`` marker, the URL, the reason, and the byte/char counts).

Run from the repo root:

    uv run python -m unittest tests.test_fetch_router
    # or via pytest, if you have it:
    uv run pytest tests/test_fetch_router.py
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

from bs4 import BeautifulSoup

# Make ``scripts/`` importable without packaging.
REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from modules.fetch_router import (  # noqa: E402
    BLOCKED_MIN_CHARS,
    build_blocked_stub,
    looks_blocked,
    needs_spa_render,
)

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "fetch"


def _extract_text_like_call_gemini(html: str) -> str:
    """Replicate the BeautifulSoup extraction that ``call-gemini.py`` does.

    This is intentionally a local copy of the curl-path extraction logic in
    ``scripts/call-gemini.py::fetch_url_content`` (strip script/style, get
    text, collapse whitespace) so the test exercises exactly the same input
    the LLM would otherwise see.
    """
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()
    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    return " ".join(chunk for chunk in chunks if chunk)


class NeedsSpaRenderTest(unittest.TestCase):
    """Router decides which URLs go through the SPA path."""

    def test_qwen_routed_to_spa(self) -> None:
        self.assertTrue(needs_spa_render("https://qwen.ai/some/page"))

    def test_chat_qwen_routed_to_spa(self) -> None:
        self.assertTrue(needs_spa_render("https://chat.qwen.ai/c/abc123"))

    def test_notion_site_subdomain_routed_to_spa(self) -> None:
        self.assertTrue(
            needs_spa_render("https://example-team.notion.site/Some-Page-abc")
        )

    def test_openai_index_routed_to_spa(self) -> None:
        self.assertTrue(needs_spa_render("https://openai.com/index/introducing-gpt-5-5/"))

    def test_openai_business_routed_to_spa(self) -> None:
        self.assertTrue(needs_spa_render("https://openai.com/business/workspace-agents/"))

    def test_developers_openai_NOT_routed_to_spa(self) -> None:
        # This is the load-bearing happy-path assertion: the curl path must
        # not be replaced with Playwright for this host.
        self.assertFalse(
            needs_spa_render("https://developers.openai.com/codex/memories/chronicle")
        )

    def test_unrelated_domain_NOT_routed_to_spa(self) -> None:
        self.assertFalse(needs_spa_render("https://example.com/article"))
        self.assertFalse(needs_spa_render("https://qiita.com/user/items/abc"))

    def test_invalid_url_does_not_crash(self) -> None:
        # Defensive: malformed input must not raise.
        self.assertFalse(needs_spa_render(""))
        self.assertFalse(needs_spa_render("not-a-url"))


class LooksBlockedFixtureTest(unittest.TestCase):
    """Guard fires on captured failure-mode fixtures, not on the happy path."""

    def _extracted(self, fixture_name: str) -> str:
        path = FIXTURES / fixture_name
        self.assertTrue(path.exists(), f"missing fixture: {path}")
        return _extract_text_like_call_gemini(path.read_text(encoding="utf-8"))

    def test_openai_index_antibot_is_blocked(self) -> None:
        text = self._extracted("openai_index_antibot.html")
        blocked, reason = looks_blocked(text)
        self.assertTrue(blocked, msg=f"expected blocked, got reason={reason!r}, text={text!r}")
        # Either the interstitial signature OR the length check must trip.
        self.assertTrue(
            "Enable JavaScript" in reason or "too short" in reason,
            msg=f"unexpected reason: {reason!r}",
        )

    def test_qwen_spa_shell_is_blocked(self) -> None:
        text = self._extracted("qwen_spa_shell.html")
        blocked, reason = looks_blocked(text)
        self.assertTrue(blocked, msg=f"expected blocked, got reason={reason!r}, text={text!r}")
        self.assertIn("too short", reason)

    def test_notion_spa_shell_is_blocked(self) -> None:
        text = self._extracted("notion_site_spa_shell.html")
        blocked, reason = looks_blocked(text)
        self.assertTrue(blocked, msg=f"expected blocked, got reason={reason!r}, text={text!r}")
        self.assertIn("too short", reason)

    def test_developers_openai_happy_path_is_NOT_blocked(self) -> None:
        text = self._extracted("developers_openai_happy.html")
        # Sanity check: the happy-path fixture must actually have substantial
        # extracted text — otherwise the test would pass for the wrong reason.
        self.assertGreaterEqual(
            len(text),
            BLOCKED_MIN_CHARS,
            msg=(
                f"happy-path fixture extracted only {len(text)} chars; "
                f"that is below the {BLOCKED_MIN_CHARS}-char threshold and "
                "would falsely look blocked. The fixture itself is wrong."
            ),
        )
        blocked, reason = looks_blocked(text)
        self.assertFalse(
            blocked,
            msg=f"happy path should NOT be blocked but was: {reason!r}",
        )


class LooksBlockedSignatureTest(unittest.TestCase):
    """Guard catches well-known interstitial signatures even on long-ish pages."""

    def test_cloudflare_just_a_moment(self) -> None:
        # Pad the rest of the body so it is over the length threshold —
        # the signature alone must still trigger the block.
        text = "Just a moment..." + (" filler" * 200)
        blocked, reason = looks_blocked(text)
        self.assertTrue(blocked)
        self.assertIn("Just a moment", reason)

    def test_cloudflare_checking_your_browser(self) -> None:
        text = "Checking your browser before accessing site" + (" filler" * 200)
        blocked, reason = looks_blocked(text)
        self.assertTrue(blocked)
        self.assertIn("Checking your browser", reason)

    def test_empty_text_is_blocked(self) -> None:
        blocked, reason = looks_blocked("")
        self.assertTrue(blocked)
        self.assertIn("empty", reason)


class BuildBlockedStubTest(unittest.TestCase):
    """Stub body must be obvious-on-sight in workdesk/summaries/."""

    def test_stub_has_BLOCKED_marker_first(self) -> None:
        stub = build_blocked_stub(
            url="https://openai.com/index/foo",
            reason="interstitial signature detected",
            extracted_chars=41,
            raw_bytes=9949,
            fetcher="curl+bs4",
        )
        first_line = stub.splitlines()[0]
        self.assertTrue(
            first_line.startswith("BLOCKED:"),
            msg=f"expected BLOCKED: marker on first line, got {first_line!r}",
        )

    def test_stub_records_url_reason_and_counts(self) -> None:
        stub = build_blocked_stub(
            url="https://qwen.ai/article",
            reason="extracted text too short (12 chars)",
            extracted_chars=12,
            raw_bytes=4567,
            fetcher="curl+bs4",
        )
        self.assertIn("https://qwen.ai/article", stub)
        self.assertIn("extracted text too short", stub)
        self.assertIn("12", stub)
        self.assertIn("4567", stub)
        self.assertIn("curl+bs4", stub)


if __name__ == "__main__":
    unittest.main()
