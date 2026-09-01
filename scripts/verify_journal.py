#!/usr/bin/env python3
"""STEP_09 verify — one exit code for a whole cycle's quality gate.

Runs the same checks the human ran by hand this cycle, over the assembled
weekly + annex journals:

  * coverage   — the weekly's 参考リンク IDs equal the curated main set, and
                 every curated source URL appears as plain text in its journal.
  * leaks      — no 原題 or score-object keys in the weekly; no recovery-URL
                 hosts (news.ycombinator / web.archive.org / fortune.com) in
                 either journal.
  * hierarchy  — exactly one H1 per journal and no skipped heading levels;
                 counts reported.
  * encoding   — no U+FFFD replacement chars or stray control characters.
  * URL health — concurrent check of the curated main+annex URLs, bucketed
                 ok (2xx) / blocked (401/403/429 anti-bot, non-fatal) /
                 broken (everything else, fatal). Skip with --skip-urls.

Exit code is non-zero on any real failure, so it drops straight into CI or a
pre-archive gate. Verify-only: it never writes anything.

Usage:
    uv run scripts/verify_journal.py 2026-08-22
    uv run scripts/verify_journal.py 2026-08-22 --skip-urls   # offline checks only
    uv run scripts/verify_journal.py 2026-08-22 --journals-dir tests/fixtures/mini-journal
"""

import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from workflow.urls import extract_urls  # noqa: E402
from workflow.partition import read_ids  # noqa: E402

# Tokens that must never appear in the finished weekly (they belong to the raw
# JSON summaries or the annex catalog format, not the edited main journal).
WEEKLY_ONLY_LEAK_TOKENS = [
    "原題",
    '"mainJournal"',
    '"annexPotential"',
    '"antiHype"',
    '"oneSentenceSummary"',
    '"summaryBody"',
    '"scores"',
]

# "Recovery" hosts used during summarization that must never reach either
# published journal.
RECOVERY_HOSTS = ["news.ycombinator", "web.archive.org", "fortune.com"]

# Control chars that indicate an encoding/copy-paste accident (excludes \t \n \r).
_CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


class Report:
    def __init__(self):
        self.failures = []
        self.notes = []

    def check(self, ok, label, detail=""):
        mark = "✅" if ok else "❌"
        line = f"{mark} {label}" + (f" — {detail}" if detail else "")
        self.notes.append(line)
        if not ok:
            self.failures.append(label)
        return ok

    def note(self, line):
        self.notes.append(line)

    @property
    def ok(self):
        return not self.failures


def _resolve_files(date, journals_dir):
    """Return (weekly, annex, curated_main, curated_annex) paths.

    Prefer the archived tree (``<journals_dir>/<date>/``); fall back to the
    live workdesk filenames so this also gates a pre-archive cycle.
    """
    us = date.replace("-", "_")
    arc = Path(journals_dir) / date
    if (arc / f"00_weekly_journal_{us}.md").exists():
        return (
            arc / f"00_weekly_journal_{us}.md",
            arc / f"01_annex_journal_{us}.md",
            arc / "sources" / "curated_journal_sources.md",
            arc / "sources" / "curated_annex_selected.md",
        )
    wd = Path("workdesk")
    return (
        wd / f"weekly_journal_{us}.md",
        wd / f"annex_journal_{us}.md",
        wd / "curated_journal_sources.md",
        wd / "curated_annex_selected.md",
    )


def _norm(u):
    return u.rstrip("/").lower()


def check_coverage(rep, date, weekly, annex, main_src, annex_src):
    wk = weekly.read_text(encoding="utf-8")
    an = annex.read_text(encoding="utf-8")

    main_ids = read_ids(main_src)
    ref_ids = set(re.findall(rf"/journals/{re.escape(date)}/(\d+)/", wk))
    rep.check(
        ref_ids == main_ids,
        "coverage: 参考リンク IDs == curated main",
        f"{len(ref_ids)} ref vs {len(main_ids)} curated"
        + (f"; diff={sorted(ref_ids ^ main_ids)}" if ref_ids != main_ids else ""),
    )

    # Original-case URLs (health-checking must keep case — e.g. Google Drive
    # file IDs are case-sensitive); normalized sets are only for the subset
    # comparison below.
    main_orig = extract_urls(main_src.read_text(encoding="utf-8"))
    annex_orig = extract_urls(annex_src.read_text(encoding="utf-8"))

    wk_urls = {_norm(u) for u in extract_urls(wk)}
    an_urls = {_norm(u) for u in extract_urls(an)}
    main_urls = {_norm(u) for u in main_orig}
    annex_urls = {_norm(u) for u in annex_orig}

    miss_main = main_urls - wk_urls
    rep.check(not miss_main, "coverage: every curated main URL present in weekly",
              f"missing={sorted(miss_main)}" if miss_main else f"{len(main_urls)} URLs")
    miss_annex = annex_urls - an_urls
    rep.check(not miss_annex, "coverage: every curated annex URL present in annex",
              f"missing={sorted(miss_annex)}" if miss_annex else f"{len(annex_urls)} URLs")

    # De-dup by original URL, preserving one canonical-case form each.
    return list(dict.fromkeys(main_orig + annex_orig))


def check_leaks(rep, weekly, annex):
    wk = weekly.read_text(encoding="utf-8")
    an = annex.read_text(encoding="utf-8")

    leaked = [t for t in WEEKLY_ONLY_LEAK_TOKENS if t in wk]
    rep.check(not leaked, "leaks: no 原題/score-object tokens in weekly",
              f"found={leaked}" if leaked else "clean")

    for name, text in (("weekly", wk), ("annex", an)):
        hosts = [h for h in RECOVERY_HOSTS if h in text]
        rep.check(not hosts, f"leaks: no recovery-URL hosts in {name}",
                  f"found={hosts}" if hosts else "clean")


def _heading_counts(text):
    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    levels = []
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+\S", line)
        if m:
            lvl = len(m.group(1))
            counts[lvl] += 1
            levels.append(lvl)
    return counts, levels


def check_hierarchy(rep, name, path):
    counts, levels = _heading_counts(path.read_text(encoding="utf-8"))
    rep.check(counts[1] == 1, f"hierarchy: {name} has exactly one H1",
              f"H1×{counts[1]}")
    # no skipped levels (e.g. ## directly to ####)
    skips = []
    prev = 0
    for lvl in levels:
        if prev and lvl > prev + 1:
            skips.append((prev, lvl))
        prev = lvl
    rep.check(not skips, f"hierarchy: {name} no skipped levels",
              f"skips={skips}" if skips else "well-formed")
    shown = " ".join(f"#×{counts[1]}" if i == 1 else f"{'#'*i}×{counts[i]}"
                     for i in range(1, 5))
    rep.note(f"   {name} headings: {shown}")
    return counts


def check_encoding(rep, name, path):
    text = path.read_text(encoding="utf-8")
    fffd = text.count("�")
    ctrl = len(_CONTROL_RE.findall(text))
    rep.check(fffd == 0, f"encoding: {name} no U+FFFD", f"count={fffd}")
    rep.check(ctrl == 0, f"encoding: {name} no stray control chars", f"count={ctrl}")


def _check_url(url, timeout=20, retries=1):
    """Return an HTTP status int, or 0 on a connection-level failure.

    Retries once on a connection-level error to smooth over transient blips on
    a live check (anti-bot resets, slow TLS) before declaring a link broken.
    """
    import requests

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "ja,en;q=0.8",
    }
    for attempt in range(retries + 1):
        try:
            r = requests.get(url, headers=headers, timeout=timeout,
                             allow_redirects=True, stream=True)
            return r.status_code
        except Exception:
            if attempt == retries:
                return 0
    return 0


def check_urls(rep, urls, workers=16):
    ok, blocked, broken = [], [], []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        results = list(ex.map(_check_url, urls))
    for url, status in zip(urls, results):
        if 200 <= status < 400:
            ok.append((url, status))
        elif status in (401, 403, 429):
            blocked.append((url, status))
        else:
            broken.append((url, status))
    rep.note(f"   URL health: {len(ok)}×2xx/3xx, {len(blocked)}×blocked(anti-bot), "
             f"{len(broken)}×broken")
    for url, status in blocked:
        rep.note(f"     · blocked {status}: {url}")
    for url, status in broken:
        rep.note(f"     · BROKEN {status or 'conn-error'}: {url}")
    rep.check(not broken, "url-health: 0 broken links",
              f"{len(broken)} broken" if broken else f"{len(ok)} ok / {len(blocked)} blocked")


def verify(date, journals_dir="journals", skip_urls=False):
    rep = Report()
    weekly, annex, main_src, annex_src = _resolve_files(date, journals_dir)

    for label, p in (("weekly", weekly), ("annex", annex),
                     ("curated main", main_src), ("curated annex", annex_src)):
        if not p.exists():
            rep.check(False, f"input present: {label}", f"missing {p}")
    if not rep.ok:
        return rep

    all_urls = check_coverage(rep, date, weekly, annex, main_src, annex_src)
    check_leaks(rep, weekly, annex)
    check_hierarchy(rep, "weekly", weekly)
    check_hierarchy(rep, "annex", annex)
    check_encoding(rep, "weekly", weekly)
    check_encoding(rep, "annex", annex)

    if skip_urls:
        rep.note("   URL health: skipped (--skip-urls)")
    else:
        check_urls(rep, sorted(all_urls))

    return rep


def main():
    args = sys.argv[1:]
    skip_urls = "--skip-urls" in args
    journals_dir = "journals"
    if "--journals-dir" in args:
        i = args.index("--journals-dir")
        journals_dir = args[i + 1]
        del args[i:i + 2]
    positional = [a for a in args if not a.startswith("--")]
    if len(positional) != 1:
        print("Usage: uv run scripts/verify_journal.py <YYYY-MM-DD> "
              "[--skip-urls] [--journals-dir DIR]")
        sys.exit(1)

    rep = verify(positional[0], journals_dir=journals_dir, skip_urls=skip_urls)
    print("\n".join(rep.notes))
    if rep.ok:
        print("\n✅ verify_journal: all checks passed")
        sys.exit(0)
    print(f"\n❌ verify_journal: {len(rep.failures)} check(s) failed: "
          + ", ".join(rep.failures))
    sys.exit(1)


if __name__ == "__main__":
    main()
