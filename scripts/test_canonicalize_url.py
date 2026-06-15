#!/usr/bin/env python3
"""
Tests for canonicalize_url.

Run:
    python3 scripts/test_canonicalize_url.py
    # or:
    uv run scripts/test_canonicalize_url.py

All tests are offline — parse_canonical_signals takes raw HTML, and
fetch_canonical is exercised by injecting a fake `requests.get` via
unittest.mock so we never hit the network.
"""

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonicalize_url import (  # noqa: E402
    fetch_canonical,
    parse_canonical_signals,
)


class _FakeResponse:
    """Minimal stand-in for requests.Response."""

    def __init__(self, *, text: str, status_code: int = 200, final_url: str | None = None):
        self.text = text
        self.status_code = status_code
        # When the server redirects to an English landing page, response.url
        # reflects the post-redirect URL — relative hrefs must resolve against it.
        self.url = final_url


# ---------------------------------------------------------------------------
# parse_canonical_signals — pure parser tests
# ---------------------------------------------------------------------------

class ParseCanonicalSignalsTests(unittest.TestCase):
    def test_x_default_wins_over_canonical_and_og(self):
        html = """
        <html><head>
          <link rel="alternate" hrefLang="x-default" href="https://example.com/en/foo/">
          <link rel="canonical" href="https://example.com/ja-jp/foo/">
          <meta property="og:url" content="https://example.com/og-foo/">
        </head><body></body></html>
        """
        url, source = parse_canonical_signals(html, "https://example.com/ja-jp/foo/")
        self.assertEqual(url, "https://example.com/en/foo/")
        self.assertEqual(source, "hreflang=x-default")

    def test_canonical_used_when_no_x_default(self):
        html = """
        <html><head>
          <link rel="canonical" href="https://example.com/en/foo/">
          <meta property="og:url" content="https://example.com/og-foo/">
        </head></html>
        """
        url, source = parse_canonical_signals(html, "https://example.com/ja-jp/foo/")
        self.assertEqual(url, "https://example.com/en/foo/")
        self.assertEqual(source, "rel=canonical")

    def test_og_url_used_when_canonical_missing(self):
        html = """
        <html><head>
          <meta property="og:url" content="https://example.com/en/foo/">
        </head></html>
        """
        url, source = parse_canonical_signals(html, "https://example.com/ja-jp/foo/")
        self.assertEqual(url, "https://example.com/en/foo/")
        self.assertEqual(source, "og:url")

    def test_no_signals_returns_none(self):
        html = "<html><head><title>foo</title></head></html>"
        url, source = parse_canonical_signals(html, "https://example.com/foo/")
        self.assertIsNone(url)
        self.assertIsNone(source)

    def test_relative_href_resolves_against_base(self):
        html = """
        <html><head>
          <link rel="canonical" href="/en/foo/">
        </head></html>
        """
        url, source = parse_canonical_signals(html, "https://example.com/ja-jp/foo/")
        self.assertEqual(url, "https://example.com/en/foo/")
        self.assertEqual(source, "rel=canonical")

    def test_non_http_scheme_skipped(self):
        # If the only candidate is javascript: or mailto:, treat as no signal.
        html = """
        <html><head>
          <link rel="canonical" href="javascript:void(0)">
        </head></html>
        """
        url, source = parse_canonical_signals(html, "https://example.com/foo/")
        self.assertIsNone(url)
        self.assertIsNone(source)

    def test_cross_domain_canonical_is_kept(self):
        # Per issue #145: syndicated posts may point at a different domain
        # (Medium → personal blog). We should surface the canonical and let
        # the caller decide.
        html = """
        <html><head>
          <link rel="canonical" href="https://author.example/originals/foo/">
        </head></html>
        """
        url, source = parse_canonical_signals(
            html, "https://medium.com/@author/foo-abc123"
        )
        self.assertEqual(url, "https://author.example/originals/foo/")
        self.assertEqual(source, "rel=canonical")

    def test_amp_canonical_to_desktop(self):
        # Per issue #145: /amp/ pages typically canonical-point at the desktop URL.
        html = """
        <html><head>
          <link rel="canonical" href="https://news.example/article/123/">
        </head></html>
        """
        url, source = parse_canonical_signals(
            html, "https://news.example/article/123/amp/"
        )
        self.assertEqual(url, "https://news.example/article/123/")
        self.assertEqual(source, "rel=canonical")

    def test_signals_outside_head_ignored(self):
        # A canonical-like tag in <body> shouldn't be picked up (avoids the
        # rare case where article body contains structured-data fragments).
        html = """
        <html>
          <head><title>page</title></head>
          <body>
            <link rel="canonical" href="https://wrong.example/">
          </body>
        </html>
        """
        url, source = parse_canonical_signals(html, "https://example.com/foo/")
        self.assertIsNone(url)
        self.assertIsNone(source)

    def test_first_x_default_wins(self):
        # If a page declares multiple x-default alternates (multilingual sites
        # occasionally do this by mistake), take the first.
        html = """
        <html><head>
          <link rel="alternate" hrefLang="x-default" href="https://example.com/en/foo/">
          <link rel="alternate" hrefLang="x-default" href="https://example.com/de/foo/">
        </head></html>
        """
        url, _ = parse_canonical_signals(html, "https://example.com/ja-jp/foo/")
        self.assertEqual(url, "https://example.com/en/foo/")

    def test_self_referencing_canonical_returned_as_is(self):
        # parse_canonical_signals doesn't enforce self-reference policy —
        # that's check_link.py's job (it re-sanitizes and compares).
        html = """
        <html><head>
          <link rel="canonical" href="https://example.com/foo/">
        </head></html>
        """
        url, source = parse_canonical_signals(html, "https://example.com/foo/")
        self.assertEqual(url, "https://example.com/foo/")
        self.assertEqual(source, "rel=canonical")


# ---------------------------------------------------------------------------
# fetch_canonical — network behavior tests (via mocked requests.get)
# ---------------------------------------------------------------------------

class FetchCanonicalTests(unittest.TestCase):
    @patch("canonicalize_url.requests.get")
    def test_openai_localized_returns_english_canonical(self, mock_get):
        # The motivating example from issue #145: localized OpenAI page
        # declares its English canonical via hreflang=x-default.
        html = """
        <html><head>
          <link rel="alternate" hrefLang="x-default"
                href="https://openai.com/index/frontier-safety-blueprint/">
          <link rel="alternate" hrefLang="en"
                href="https://openai.com/index/frontier-safety-blueprint/">
          <link rel="canonical"
                href="https://openai.com/ja-JP/index/frontier-safety-blueprint/">
        </head></html>
        """
        mock_get.return_value = _FakeResponse(
            text=html,
            status_code=206,
            final_url="https://openai.com/ja-JP/index/frontier-safety-blueprint/",
        )
        url, source = fetch_canonical(
            "https://openai.com/ja-JP/index/frontier-safety-blueprint/"
        )
        self.assertEqual(
            url, "https://openai.com/index/frontier-safety-blueprint/"
        )
        self.assertEqual(source, "hreflang=x-default")

    @patch("canonicalize_url.requests.get")
    def test_network_failure_returns_none_none(self, mock_get):
        # Per issue: fall back gracefully on network failure.
        from requests.exceptions import ConnectionError

        mock_get.side_effect = ConnectionError("boom")
        url, source = fetch_canonical("https://example.com/foo/")
        self.assertIsNone(url)
        self.assertIsNone(source)

    @patch("canonicalize_url.requests.get")
    def test_404_returns_none_none(self, mock_get):
        mock_get.return_value = _FakeResponse(text="not found", status_code=404)
        url, source = fetch_canonical("https://example.com/foo/")
        self.assertIsNone(url)
        self.assertIsNone(source)

    @patch("canonicalize_url.requests.get")
    def test_empty_body_returns_none_none(self, mock_get):
        mock_get.return_value = _FakeResponse(
            text="", status_code=200, final_url="https://example.com/foo/"
        )
        url, source = fetch_canonical("https://example.com/foo/")
        self.assertIsNone(url)
        self.assertIsNone(source)

    @patch("canonicalize_url.requests.get")
    def test_relative_href_uses_post_redirect_base(self, mock_get):
        # If a request to /ja-jp/foo/ followed a redirect to /jp/foo/ and then
        # the body declared <link rel="canonical" href="/foo/">, the canonical
        # should resolve against the post-redirect URL.
        html = """
        <html><head>
          <link rel="canonical" href="/foo/">
        </head></html>
        """
        mock_get.return_value = _FakeResponse(
            text=html,
            status_code=200,
            final_url="https://example.com/jp/foo/",
        )
        url, source = fetch_canonical("https://example.com/ja-jp/foo/")
        self.assertEqual(url, "https://example.com/foo/")
        self.assertEqual(source, "rel=canonical")


# ---------------------------------------------------------------------------
# Dedup integration scenario — proves the issue #145 acceptance test:
# "localized variant of an existing URL is correctly flagged as duplicate"
# ---------------------------------------------------------------------------

class DedupScenarioTest(unittest.TestCase):
    """End-to-end shape: a localized URL must dedup against an English URL
    already in sources by virtue of resolving to the same canonical."""

    @patch("canonicalize_url.requests.get")
    def test_localized_variant_resolves_to_same_canonical_as_english(self, mock_get):
        # Imagine: English URL was added in a previous cycle. New cycle:
        # someone tries to add the ja-JP URL. fetch_canonical on the ja-JP
        # URL should return the English canonical, which will match the
        # existing entry under string equality.
        english = "https://openai.com/index/frontier-safety-blueprint/"
        ja = "https://openai.com/ja-JP/index/frontier-safety-blueprint/"
        html_ja = f"""
        <html><head>
          <link rel="alternate" hrefLang="x-default" href="{english}">
          <link rel="canonical" href="{ja}">
        </head></html>
        """
        mock_get.return_value = _FakeResponse(
            text=html_ja, status_code=200, final_url=ja
        )
        canonical, source = fetch_canonical(ja)
        self.assertEqual(canonical, english)
        self.assertEqual(source, "hreflang=x-default")
        # And the canonical is NOT the input — so check_link.py would swap.
        self.assertNotEqual(canonical, ja)


if __name__ == "__main__":
    unittest.main()
