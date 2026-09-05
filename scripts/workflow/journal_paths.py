#!/usr/bin/env python3
"""Canonical file paths and public URLs for a journal cycle.

One place decides that the archive lives at ``journals/2026-08-22/`` with
underscore-dated filenames (``00_weekly_journal_2026_08_22.md``) while the URL
path segment stays hyphenated (``.../journals/2026-08-22/main/``). Every script
that references these paths goes through ``Paths`` so the two conventions never
get crossed.
"""

import re
from pathlib import Path

REPO_WEB = "https://github.com/beijaflor/gen-ai-journal"
PAGES_BASE = "https://beijaflor.github.io/gen-ai-journal"

_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class Paths:
    """Resolve every path/URL for a cycle from its hyphenated date string."""

    def __init__(self, date, root=Path(".")):
        if not _DATE_RE.match(date):
            raise ValueError(f"date must be YYYY-MM-DD, got {date!r}")
        self.date = date  # 2026-08-22 (dirs, tags, URL segments)
        self.us = date.replace("-", "_")  # 2026_08_22 (filenames)
        self.root = Path(root)

    # -- directories ---------------------------------------------------------
    @property
    def dir(self):
        return self.root / "journals" / self.date

    @property
    def summaries(self):
        return self.dir / "summaries"

    @property
    def sources(self):
        return self.dir / "sources"

    # -- assembled files (underscore-dated) ----------------------------------
    @property
    def weekly(self):
        return self.dir / f"00_weekly_journal_{self.us}.md"

    @property
    def annex(self):
        return self.dir / f"01_annex_journal_{self.us}.md"

    @property
    def omitted(self):
        return self.dir / "02_omitted_summaries.md"

    @property
    def plan(self):
        return self.dir / f"50_editorial_plan_{self.us}.md"

    @property
    def unified(self):
        return self.dir / "99_unified_summaries.md"

    @property
    def metadata(self):
        return self.dir / "journal-metadata.json"

    # -- public URLs ---------------------------------------------------------
    def blob(self, name):
        """A github.com blob URL pinned to the release tag (== the date).

        ``name`` is a repo-relative path, e.g.
        ``journals/2026-08-22/00_weekly_journal_2026_08_22.md``.
        """
        return f"{REPO_WEB}/blob/{self.date}/{name}"

    def pages(self, section):
        """A GitHub Pages URL. ``section`` is main / annex / summaries."""
        return f"{PAGES_BASE}/journals/{self.date}/{section}/"

    # convenience: the six links every release lists
    @property
    def pages_links(self):
        return [self.pages(s) for s in ("main", "annex", "summaries")]

    @property
    def blob_links(self):
        base = f"journals/{self.date}"
        return [
            self.blob(f"{base}/00_weekly_journal_{self.us}.md"),
            self.blob(f"{base}/01_annex_journal_{self.us}.md"),
            self.blob(f"{base}/02_omitted_summaries.md"),
        ]
