#!/usr/bin/env python3
"""List paywalled / proxy-summarized sources for human review (STEP_02 gate).

`validate_summary.py` (schema) and `check_summary_format.py` (rendering) both
pass a summary whose *content* came from a paywall workaround. Those workarounds
are editorial decisions, not mechanical ones: a Hacker News thread is not the
article, and a reader who clicks a paywalled link hits a wall. This tool surfaces
every such source so a human decides how to handle each one (keep / drop / fetch
full text / annotate), rather than letting the automatic fallback chain decide
silently.

It classifies each checked source into three buckets:

  A. hn-proxy   — the summary's ``content.url`` is a Hacker News thread while the
                  source URL is not: the article was paywalled/blocked and got
                  summarized from the HN discussion instead (SKILL.md Step 3).
                  The summary describes a comment thread, not the article.
  B. blocked    — the summary file is a fail-closed ``BLOCKED:`` stub (non-JSON):
                  the fetch never returned usable content and no proxy was found.
                  (A dead 404 link also lands here.)
  C. paywall-domain — the source host is a known paywalled/metered publisher but
                  a real (non-proxy, non-stub) summary was produced. The summary
                  is usually fine (metered first view); flagged because the
                  reader-facing link is gated, and because a subtle block-page
                  summary can hide here — a body-text heuristic marks suspects.

Usage:
    uv run scripts/list_paywalled_sources.py                      # workdesk/
    uv run scripts/list_paywalled_sources.py --sources workdesk/sources.md \\
        --summaries workdesk/summaries
    uv run scripts/list_paywalled_sources.py --out workdesk/paywall_review.md
    uv run scripts/list_paywalled_sources.py journals/2026-09-19   # an archive

Exit 0 always (this is a report, not a gate); prints a Markdown review sheet to
stdout, or writes it to ``--out``. Feed the sheet to the human-review-gate skill.
"""

import argparse
import glob
import json
import os
import re
import sys
from urllib.parse import urlparse

# Known paywalled / metered publishers. Conservative on purpose: a false flag
# only asks a human to glance, but the list should not sweep in open blogs.
# Medium (and its publications, e.g. uxdesign.cc) meters after a few views.
KNOWN_PAYWALL_HOSTS = {
    "www.reuters.com", "reuters.com",
    "www.wsj.com", "wsj.com",
    "www.nytimes.com", "nytimes.com",
    "www.economist.com", "economist.com",
    "www.bloomberg.com", "bloomberg.com",
    "www.ft.com", "ft.com",
    "www.science.org", "science.org",
    "www.nature.com", "nature.com",
    "www.scmp.com", "scmp.com",
    "www.businessinsider.com", "businessinsider.com", "www.businessinsider.jp",
    "www.technologyreview.com", "technologyreview.com",
    "www.wired.com", "wired.com",
    "www.theinformation.com", "theinformation.com",
    "www.washingtonpost.com", "washingtonpost.com",
    "www.theatlantic.com", "theatlantic.com",
    "medium.com", "uxdesign.cc",
}

# Telltales that a body summarizes a block/paywall page instead of the article.
_BLOCKPAGE = re.compile(
    r"(cloudflare|アクセスブロック|アクセス遮断|just a moment|subscribe to (read|continue)|"
    r"sign in to (read|continue)|create a free account|register to (read|continue)|"
    r"paywall|akamai|verify you are human|お使いのブラウザ|being rate limited|"
    r"request rate threshold)",
    re.I,
)


def _host(url: str) -> str:
    return urlparse(url).netloc.lower()


def parse_sources(sources_path: str) -> dict:
    """Return {id: (checkstate, url)} for every '- [ ]/[x] NNN. url' line."""
    out = {}
    with open(sources_path, encoding="utf-8") as f:
        for line in f:
            m = re.match(r"^- \[(.)\] (\d{3})\. (\S+)", line)
            if m:
                out[m.group(2)] = (m.group(1), m.group(3))
    return out


def classify(sources_path: str, summaries_dir: str) -> dict:
    """Return {'hn': [...], 'blocked': [...], 'paywall_domain': [...]}."""
    src = parse_sources(sources_path)
    hn, blocked, paywall_domain = [], [], []
    for fp in sorted(glob.glob(os.path.join(summaries_dir, "*.json"))):
        fid = os.path.basename(fp)[:3]
        checkstate, url = src.get(fid, ("?", "?"))
        try:
            with open(fp, encoding="utf-8") as f:
                content = json.load(f).get("content", {})
        except (json.JSONDecodeError, OSError):
            blocked.append({"id": fid, "url": url})
            continue
        content_url = content.get("url", "")
        if "news.ycombinator.com" in content_url and "news.ycombinator.com" not in _host(url):
            hn.append({"id": fid, "url": url, "proxy": content_url})
        elif _host(url) in KNOWN_PAYWALL_HOSTS:
            body = " ".join(
                str(content.get(k, "")) for k in ("title", "oneSentenceSummary", "summaryBody")
            )
            paywall_domain.append(
                {"id": fid, "url": url, "host": _host(url),
                 "suspect_blockpage": bool(_BLOCKPAGE.search(body))}
            )
    return {"hn": hn, "blocked": blocked, "paywall_domain": paywall_domain}


def render(buckets: dict) -> str:
    hn, blocked, pd = buckets["hn"], buckets["blocked"], buckets["paywall_domain"]
    n = len(hn) + len(blocked) + len(pd)
    lines = [
        "# Paywalled-source review (STEP_02 gate)",
        "",
        f"{n} source(s) need a human decision. For each, mark a decision inline: "
        "`keep` / `drop` / `full-text` (you supply the article text) / `annotate` "
        "(note the paywall for readers).",
        "",
        "## A. Paywalled → summarized from a Hacker News thread (NOT the article)",
        "_The summary describes an HN discussion, not the source article. Decide: "
        "keep the HN-proxy summary, drop the source, or supply full text to re-summarize._",
        "",
    ]
    if hn:
        for r in hn:
            lines.append(f"- [ ] **{r['id']}** — {r['url']}")
            lines.append(f"      proxy: {r['proxy']}  → decision: ____")
    else:
        lines.append("- (none)")
    lines += [
        "",
        "## B. Unfetchable — fail-closed BLOCKED stub / dead link",
        "_No usable content and no proxy. Decide: drop, or supply a corrected URL / full text._",
        "",
    ]
    if blocked:
        for r in blocked:
            lines.append(f"- [ ] **{r['id']}** — {r['url']}  → decision: ____")
    else:
        lines.append("- (none)")
    lines += [
        "",
        "## C. Paywalled-domain link — real summary, but the reader link is gated",
        "_Summary content is real (metered first view). Decide: keep as-is, annotate "
        "the paywall for readers, or drop. Items marked ⚠ may actually be block-page "
        "summaries — verify the body._",
        "",
    ]
    if pd:
        for r in pd:
            warn = " ⚠ possible block-page — verify" if r["suspect_blockpage"] else ""
            lines.append(f"- [ ] **{r['id']}** — [{r['host']}] {r['url']}{warn}  → decision: ____")
    else:
        lines.append("- (none)")
    lines.append("")
    return "\n".join(lines)


def main(argv: list) -> int:
    p = argparse.ArgumentParser(description="List paywalled sources for human review.")
    p.add_argument("journal_dir", nargs="?", default=None,
                   help="An archived journal dir (uses <dir>/sources/sources.md + "
                        "<dir>/summaries). Overridden by --sources/--summaries.")
    p.add_argument("--sources", default=None)
    p.add_argument("--summaries", default=None)
    p.add_argument("--out", default=None, help="Write the sheet here instead of stdout.")
    args = p.parse_args(argv)

    if args.journal_dir:
        sources = args.sources or os.path.join(args.journal_dir, "sources", "sources.md")
        summaries = args.summaries or os.path.join(args.journal_dir, "summaries")
    else:
        sources = args.sources or "workdesk/sources.md"
        summaries = args.summaries or "workdesk/summaries"

    if not os.path.exists(sources) or not os.path.isdir(summaries):
        print(f"Error: sources '{sources}' or summaries '{summaries}' not found",
              file=sys.stderr)
        return 2

    sheet = render(classify(sources, summaries))
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(sheet + "\n")
        print(f"Wrote paywall review sheet to {args.out}")
    else:
        print(sheet)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
