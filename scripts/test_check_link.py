#!/usr/bin/env python3
"""
Tests for check_link — specifically the zenn.dev slug-level dedup added
because Zenn cross-posts the same article under both an author path
(zenn.dev/{user}/articles/{slug}) and a company/publication path
(zenn.dev/{publication}/articles/{slug}) with an identical article slug.
Comparing full sanitized URL strings missed this (issue: aki1990 vs
peoplex_blog both publishing articles/1bc5c181ad19f0).

Run:
    python3 scripts/test_check_link.py
    # or:
    uv run scripts/test_check_link.py
"""

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_link import (  # noqa: E402
    _content_has_duplicate,
    check_duplicate,
    zenn_article_slug,
)


AKI_URL = "https://zenn.dev/aki1990/articles/1bc5c181ad19f0"
PEOPLEX_URL = "https://zenn.dev/peoplex_blog/articles/1bc5c181ad19f0"


class ZennArticleSlugTests(unittest.TestCase):
    def test_extracts_slug_from_author_path(self):
        self.assertEqual(zenn_article_slug(AKI_URL), "1bc5c181ad19f0")

    def test_extracts_slug_from_publication_path(self):
        self.assertEqual(zenn_article_slug(PEOPLEX_URL), "1bc5c181ad19f0")

    def test_tolerates_trailing_slash(self):
        self.assertEqual(
            zenn_article_slug("https://zenn.dev/aki1990/articles/1bc5c181ad19f0/"),
            "1bc5c181ad19f0",
        )

    def test_non_zenn_host_returns_none(self):
        self.assertIsNone(
            zenn_article_slug("https://qiita.com/aki1990/items/1bc5c181ad19f0")
        )

    def test_zenn_non_article_path_returns_none(self):
        self.assertIsNone(zenn_article_slug("https://zenn.dev/aki1990"))
        self.assertIsNone(zenn_article_slug("https://zenn.dev/aki1990/scraps/abc123"))


class ContentHasDuplicateTests(unittest.TestCase):
    def test_positive_zenn_cross_post_slug_match(self):
        """The concrete failing case: aki1990 vs peoplex_blog, same slug."""
        content = f"- [ ] 187. {AKI_URL}\n"
        self.assertTrue(_content_has_duplicate(content, PEOPLEX_URL))

    def test_negative_different_zenn_slugs_do_not_collide(self):
        content = f"- [ ] 187. {AKI_URL}\n"
        other_article = "https://zenn.dev/peoplex_blog/articles/deadbeef1234"
        self.assertFalse(_content_has_duplicate(content, other_article))

    def test_guard_non_zenn_url_unaffected(self):
        """A non-zenn URL must fall back to plain substring matching only —
        no slug-based collision logic kicks in for other hosts."""
        qiita_url = "https://qiita.com/someuser/items/1bc5c181ad19f0"
        other_qiita_url = "https://qiita.com/otheruser/items/1bc5c181ad19f0"
        content = f"- [ ] 042. {qiita_url}\n"
        # Different Qiita authors with the same trailing id must NOT be
        # treated as duplicates — Qiita item ids are not modeled here.
        self.assertFalse(_content_has_duplicate(content, other_qiita_url))
        # Exact match still works via plain substring containment.
        self.assertTrue(_content_has_duplicate(content, qiita_url))

    def test_exact_url_match_still_works(self):
        content = f"- [ ] 187. {AKI_URL}\n"
        self.assertTrue(_content_has_duplicate(content, AKI_URL))

    def test_unrelated_url_is_not_a_duplicate(self):
        content = f"- [ ] 187. {AKI_URL}\n"
        self.assertFalse(
            _content_has_duplicate(content, "https://example.com/unrelated")
        )


class CheckDuplicateIntegrationTests(unittest.TestCase):
    """Exercise check_duplicate() end-to-end against a real workdesk/sources.md
    fixture on disk, since it reads files directly rather than taking content
    as a parameter."""

    def setUp(self):
        import shutil
        import tempfile

        self._tmpdir = tempfile.mkdtemp()
        self._orig_cwd = Path.cwd()
        workdesk = Path(self._tmpdir) / "workdesk"
        workdesk.mkdir()
        (workdesk / "sources.md").write_text(
            f"# Sources for Journal 2026-09-26\n\n- [ ] 187. {AKI_URL}\n"
        )
        self._shutil = shutil
        import os

        os.chdir(self._tmpdir)

    def tearDown(self):
        import os

        os.chdir(self._orig_cwd)
        self._shutil.rmtree(self._tmpdir, ignore_errors=True)

    def test_cross_post_detected_as_duplicate(self):
        is_dup, locations = check_duplicate(PEOPLEX_URL)
        self.assertTrue(is_dup)
        self.assertTrue(any(loc[0] == "workdesk/sources.md" for loc in locations))

    def test_different_zenn_article_is_not_a_duplicate(self):
        is_dup, _locations = check_duplicate(
            "https://zenn.dev/peoplex_blog/articles/deadbeef1234"
        )
        self.assertFalse(is_dup)


if __name__ == "__main__":
    unittest.main()
