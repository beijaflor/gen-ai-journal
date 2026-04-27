#!/usr/bin/env python3
"""
Post-generation review table for Gemini summaries (Issue #108, Layer 2).

Scans a directory of v1.0 JSON summary files and prints a compact table:

    ID  | Domain              | Title                          | One-Sentence Summary
    001 | github.com          | GitHub Copilot の新機能...        | GitHub Copilotが...
    164 | tokenstree.com      | TokensTree: 自律型AIエージェント...  | AIエージェント同士が...  <- suspicious

Suspicious rows are flagged when the generated summary "smells like" a guess
made from the domain rather than from the article body. Heuristics:

  * Summary describes a site/service rather than an article — the text mentions
    "プラットフォーム / platform / サービス / service / 企業 / company" without
    any specific event, release, or finding.
  * Title is generic: just the domain stem, just a company name, or extremely
    short (< 12 characters of meaningful content).
  * Title and one-sentence summary share unusually heavy domain-name overlap.

This is a heuristic — it surfaces candidates for human review, not a
hard reject. Use Layer 3 (re-summarize skill) to fix flagged entries.

Usage:
    uv run scripts/summary_review.py workdesk/summaries/
    uv run scripts/summary_review.py journals/2026-04-18/summaries/
    uv run scripts/summary_review.py workdesk/summaries/ --only-suspicious
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

# Heuristic vocabulary: words that, when present without a specific event,
# suggest the summary is describing a service/site rather than an article.
SITE_DESCRIPTOR_KEYWORDS = (
    "プラットフォーム",
    "platform",
    "サービス",
    "service",
    "企業",
    "company",
    "ソリューション",
    "solution",
    "ベンチャー",
    "startup",
    "提供しています",
    "提供する企業",
)

# Words that indicate an actual event/release/finding — their presence
# downgrades the "site-descriptor" signal.
EVENT_KEYWORDS = (
    "発表",
    "リリース",
    "公開",
    "ローンチ",
    "launched",
    "released",
    "announced",
    "introduces",
    "introducing",
    "公開しました",
    "発表しました",
    "提唱",
    "報告",
    "解説",
    "明らかに",
    "判明",
    "示した",
    "述べている",
    "論じている",
    "version",
    "v1.",
    "v2.",
    "v3.",
    "アップデート",
    "新機能",
    "new feature",
    "blog post",
    "記事",
    "ブログ",
    "ガイド",
    "tutorial",
    "チュートリアル",
)


def _domain_for(url: str) -> str:
    try:
        host = urlparse(url).netloc or url
    except Exception:
        host = url
    return host.replace("www.", "")


def _domain_stem(domain: str) -> str:
    """Return the second-level label of a hostname (e.g. github.com -> github)."""
    parts = domain.split(".")
    if len(parts) >= 2:
        return parts[-2].lower()
    return domain.lower()


def _truncate(text: str, width: int) -> str:
    text = (text or "").strip().replace("\n", " ")
    if len(text) <= width:
        return text
    return text[: max(0, width - 1)] + "…"


def _load_summary(path: Path) -> Optional[Dict[str, Any]]:
    """Load a v1.0 JSON summary file. Returns None on parse error."""
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return None


def _looks_like_site_description(one_sentence: str, summary_body: str) -> bool:
    """True when the summary describes a site/service rather than an article."""
    blob = f"{one_sentence}\n{summary_body}"
    blob_lower = blob.lower()

    has_descriptor = any(kw.lower() in blob_lower for kw in SITE_DESCRIPTOR_KEYWORDS)
    has_event = any(kw.lower() in blob_lower for kw in EVENT_KEYWORDS)

    # Site-descriptor language without a concrete event/release is the danger zone.
    return has_descriptor and not has_event


def _title_looks_generic(title: str, domain: str) -> bool:
    """True when the title doesn't carry article-specific content."""
    if not title:
        return True
    cleaned = title.strip()
    if len(cleaned) < 12:
        return True

    stem = _domain_stem(domain)
    if not stem:
        return False

    # Exact "GitHub" or "TokensTree" as title with nothing else is a red flag.
    # Heuristic: title is mostly the domain stem if removing it leaves <8 chars.
    pattern = re.compile(re.escape(stem), re.IGNORECASE)
    leftover = pattern.sub("", cleaned).strip(" :：-—–|・,.")
    if len(leftover) < 8:
        return True

    return False


def evaluate_suspicion(content: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Score a summary's content. Returns (is_suspicious, reasons)."""
    reasons: List[str] = []

    title = content.get("title", "") or ""
    one_sentence = content.get("oneSentenceSummary", "") or ""
    summary_body = content.get("summaryBody", "") or ""
    url = content.get("url", "") or ""
    domain = _domain_for(url)

    if _title_looks_generic(title, domain):
        reasons.append("generic-title")

    if _looks_like_site_description(one_sentence, summary_body):
        reasons.append("site-descriptor")

    # Very short summary body is another tell (Gemini gave up early).
    # The schema enforces >= 100 chars but anything below ~200 is worth a look.
    if 0 < len(summary_body) < 200:
        reasons.append("short-body")

    return (len(reasons) > 0, reasons)


def gather_rows(directory: Path) -> List[Dict[str, Any]]:
    """Scan a directory of summary JSON files and return per-file rows."""
    rows: List[Dict[str, Any]] = []

    if not directory.exists():
        print(f"ERROR: {directory} does not exist", file=sys.stderr)
        return rows

    files = sorted(directory.glob("[0-9][0-9][0-9]_*.json"))

    for path in files:
        try:
            file_id = int(path.name[:3])
        except ValueError:
            continue

        data = _load_summary(path)
        if data is None:
            rows.append({
                "id": file_id,
                "domain": "(unparseable)",
                "title": path.name,
                "one_sentence": "",
                "suspicious": True,
                "reasons": ["json-parse-error"],
                "path": str(path),
            })
            continue

        content = data.get("content", {}) or {}
        url = content.get("url", "") or ""
        domain = _domain_for(url)

        suspicious, reasons = evaluate_suspicion(content)

        rows.append({
            "id": file_id,
            "domain": domain,
            "title": content.get("title", "") or "",
            "one_sentence": content.get("oneSentenceSummary", "") or "",
            "suspicious": suspicious,
            "reasons": reasons,
            "path": str(path),
        })

    return rows


def render_table(
    rows: List[Dict[str, Any]],
    *,
    only_suspicious: bool = False,
    domain_width: int = 24,
    title_width: int = 36,
    summary_width: int = 60,
) -> str:
    """Render the table as a single string."""
    if only_suspicious:
        rows = [r for r in rows if r["suspicious"]]

    if not rows:
        return "(no rows)"

    header = (
        f"{'ID':<4}| {'Domain':<{domain_width}}| "
        f"{'Title':<{title_width}}| {'One-Sentence Summary':<{summary_width}}"
    )
    separator = "-" * len(header)
    out_lines: List[str] = [header, separator]

    for r in rows:
        marker = "  <- suspicious" if r["suspicious"] else ""
        line = (
            f"{r['id']:03d} | "
            f"{_truncate(r['domain'], domain_width - 1):<{domain_width - 1}} | "
            f"{_truncate(r['title'], title_width - 1):<{title_width - 1}} | "
            f"{_truncate(r['one_sentence'], summary_width)}"
            f"{marker}"
        )
        out_lines.append(line)
        if r["suspicious"] and r["reasons"]:
            out_lines.append(f"     reasons: {', '.join(r['reasons'])}")

    out_lines.append("")
    suspicious_count = sum(1 for r in rows if r["suspicious"])
    out_lines.append(
        f"Total: {len(rows)} rows, {suspicious_count} flagged for review"
    )
    return "\n".join(out_lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Print a review table for generated JSON summaries (Issue #108, Layer 2)"
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default="workdesk/summaries",
        help="Directory of XXX_*.json summary files (default: workdesk/summaries)",
    )
    parser.add_argument(
        "--only-suspicious",
        action="store_true",
        help="Show only rows the heuristics flagged for review",
    )

    args = parser.parse_args()
    directory = Path(args.directory)

    rows = gather_rows(directory)
    if not rows:
        print(f"(no summary files found in {directory})", file=sys.stderr)
        return 1

    print(render_table(rows, only_suspicious=args.only_suspicious))
    return 0


if __name__ == "__main__":
    sys.exit(main())
