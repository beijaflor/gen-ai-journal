#!/usr/bin/env python3
"""
Pull new links from the cloud inbox into workdesk/sources.md (issue #159).

Fetches links with status=new from the platform API, runs the same
validation / sanitization / canonical-resolution / duplicate checks as the
add-url skill (reusing scripts/check_link.py), appends unique URLs to the
"## Main List" section of sources.md with sequential zero-padded IDs, and
marks them consumed (duplicates → dismissed) via the API.

Usage:
    uv run scripts/pull_inbox.py [--dry-run] [--sources workdesk/sources.md]

Env (scripts/.env):
    PLATFORM_API_TOKEN  bearer token (required)
    PLATFORM_API_URL    default: https://gen-ai-journal.pages.dev
"""

import argparse
import os
import re
import sys
from pathlib import Path

import requests
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_link import check_duplicate, follow_redirects, sanitize_url, validate_url  # noqa: E402
from canonicalize_url import fetch_canonical  # noqa: E402

load_dotenv(Path(__file__).parent / ".env")

API_URL = os.environ.get("PLATFORM_API_URL", "https://gen-ai-journal.pages.dev").rstrip("/")
TOKEN = os.environ.get("PLATFORM_API_TOKEN")

ENTRY_RE = re.compile(r"^- \[[ x]\] (\d{3})\. ", re.MULTILINE)


def api(method: str, path: str, **kwargs):
    resp = requests.request(
        method,
        f"{API_URL}{path}",
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
        timeout=30,
        **kwargs,
    )
    resp.raise_for_status()
    return resp.json()


def next_id(sources_text: str) -> int:
    ids = [int(m) for m in ENTRY_RE.findall(sources_text)]
    return (max(ids) + 1) if ids else 1


def resolve_dedup_url(url: str) -> str:
    """Mirror check_link.py main(): sanitize, then swap to canonical if declared."""
    sanitized = sanitize_url(url)
    canonical_url, _source = fetch_canonical(sanitized)
    if canonical_url:
        canonical_sanitized = sanitize_url(canonical_url)
        if canonical_sanitized != sanitized:
            return canonical_sanitized
    return sanitized


def main() -> int:
    parser = argparse.ArgumentParser(description="Pull cloud inbox links into sources.md")
    parser.add_argument("--dry-run", action="store_true", help="report actions without writing or PATCHing")
    parser.add_argument("--sources", default="workdesk/sources.md", help="path to sources.md")
    args = parser.parse_args()

    if not TOKEN:
        print("Error: PLATFORM_API_TOKEN must be set in scripts/.env")
        return 1

    sources_path = Path(args.sources)
    if not sources_path.exists():
        print(f"Error: {sources_path} not found — start the journal cycle first (STEP_01 creates it).")
        return 1
    text = sources_path.read_text()
    if "## Main List" not in text:
        print(f"Error: {sources_path} has no '## Main List' section.")
        return 1

    data = api("GET", "/api/links?status=new")
    links = data["links"]
    print(f"Inbox: {len(links)} new link(s)")
    if not links:
        return 0

    added, dup, failed = [], [], []
    for link in links:
        lid, raw_url = link["id"], link["url"]
        prefix = f"[inbox #{lid}] {raw_url}"

        is_valid, err = validate_url(raw_url)
        if not is_valid:
            print(f"✗ {prefix} — invalid: {err}")
            failed.append(lid)
            continue

        dedup_url = resolve_dedup_url(raw_url)
        final_url, _chain = follow_redirects(dedup_url)
        is_dup, locations = check_duplicate(dedup_url, final_url)
        in_target = dedup_url in text
        if not is_dup and not in_target:
            nid = next_id(text)
            entry = f"- [ ] {nid:03d}. {dedup_url}\n"
            # Append at the end of the Main List section (end of file in practice).
            text = text.rstrip("\n") + "\n" + entry
            print(f"✓ {prefix} → added as {nid:03d}" + (f" (canonicalized: {dedup_url})" if dedup_url != raw_url else ""))
            added.append((lid, nid, dedup_url))
            if not args.dry_run:
                sources_path.write_text(text)
                api("PATCH", f"/api/links/{lid}", json={"status": "consumed"})
        elif in_target:
            # Already in this cycle's list (e.g. a re-run after a crash between
            # file write and PATCH) — it was consumed, not rejected.
            print(f"– {prefix} — already in {sources_path.name}; marking consumed")
            dup.append(lid)
            if not args.dry_run:
                api("PATCH", f"/api/links/{lid}", json={"status": "consumed"})
        else:
            where = locations[0][0] if locations else "archives"
            print(f"– {prefix} — duplicate ({where}); dismissing")
            dup.append(lid)
            if not args.dry_run:
                api("PATCH", f"/api/links/{lid}", json={"status": "dismissed"})

    print(f"\nDone: {len(added)} added, {len(dup)} duplicates dismissed, {len(failed)} failed"
          + (" (dry run — nothing written)" if args.dry_run else ""))
    if added:
        print(f"IDs {added[0][1]:03d}–{added[-1][1]:03d} appended to {sources_path}. Next: summarize-source skill (STEP_02).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
