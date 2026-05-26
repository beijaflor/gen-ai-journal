#!/usr/bin/env python3
"""
Mark this week's summaries as published by setting their journal_date.

By default this is SCOPED to the current journal's own summaries (matched by
URL against journals/<date>/summaries/*.json, with a workdesk/ fallback), so
it can NOT sweep a backlog of unrelated unmarked rows into this week — the bug
that caused the 2026-04-25 mega-bucket.

Usage:
    uv run scripts/mark_published.py 2026-05-30            # scoped (recommended)
    uv run scripts/mark_published.py 2026-05-30 --all-null # legacy blanket behavior (escape hatch)

Arguments:
    journal_date: The date of the journal in YYYY-MM-DD format
"""

import os
import sys
import json
import glob
import re
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv(Path(__file__).parent / ".env")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
if not SUPABASE_URL or not SUPABASE_KEY:
    print("Error: SUPABASE_URL and SUPABASE_SERVICE_KEY must be set in scripts/.env")
    sys.exit(1)
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def validate_date_format(date_str: str) -> bool:
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', date_str))


def norm(u):
    """Canonicalize a URL for matching (scheme/www/trailing-slash/fragment-insensitive)."""
    if not u:
        return None
    u = u.strip().split("#")[0]
    u = re.sub(r'^https?://', '', u, flags=re.I)
    u = re.sub(r'^www\.', '', u, flags=re.I)
    return u.rstrip('/').rstrip('.,;)\'"').lower()


def collect_week_urls(journal_date: str):
    """URLs for THIS journal, from the archived summaries (preferred) or workdesk."""
    sources = sorted(glob.glob(f"journals/{journal_date}/summaries/*.json")) or \
        sorted(glob.glob("workdesk/summaries/*.json"))
    urls = set()
    for f in sources:
        try:
            c = json.load(open(f)).get("content", {})
        except Exception:
            continue
        for u in (c.get("url"), c.get("contentSourceUrl")):
            k = norm(u)
            if k:
                urls.add((k, u))  # keep one raw form for the IN filter
    return sources, urls


def mark_scoped(journal_date: str) -> int:
    _, week = collect_week_urls(journal_date)
    if not week:
        print("❌ Found no summaries for this journal (checked journals/<date>/summaries/ "
              "and workdesk/summaries/). Refusing to run. Use --all-null to force legacy behavior.")
        sys.exit(1)
    # Fetch all rows once; match by normalized URL, then update by id (precise).
    rows = []
    start = 0
    while True:
        r = supabase.table("summary_metadata").select("id,url,journal_date").range(start, start + 999).execute()
        rows.extend(r.data)
        if len(r.data) < 1000:
            break
        start += 1000
    week_norm = {k for k, _ in week}
    ids = [row["id"] for row in rows
           if norm(row["url"]) in week_norm and (row["journal_date"] or None) != journal_date]
    print(f"This journal has {len(week_norm)} distinct URLs; {len(ids)} matching rows need journal_date={journal_date}.")
    for i in range(0, len(ids), 100):
        supabase.table("summary_metadata").update({"journal_date": journal_date}).in_("id", ids[i:i + 100]).execute()
    return len(ids)


def mark_all_null(journal_date: str) -> int:
    response = supabase.table("summary_metadata").update(
        {"journal_date": journal_date}).is_("journal_date", "null").execute()
    return len(response.data) if response.data else 0


def main():
    args = sys.argv[1:]
    all_null = "--all-null" in args
    args = [a for a in args if a != "--all-null"]
    if len(args) != 1:
        print("Usage: uv run scripts/mark_published.py YYYY-MM-DD [--all-null]")
        sys.exit(1)
    journal_date = args[0]
    if not validate_date_format(journal_date):
        print(f"❌ Invalid date format: {journal_date}  (expected YYYY-MM-DD)")
        sys.exit(1)

    mode = "ALL journal_date IS NULL rows (legacy blanket)" if all_null \
        else "only THIS journal's summaries (scoped by URL)"
    print(f"Marking as published for journal date: {journal_date}")
    print(f"Mode: {mode}")
    if all_null:
        print("⚠️  --all-null can sweep unrelated unmarked rows into this date. Use only intentionally.")
    print("")
    confirm = input(f"Set journal_date={journal_date} for {mode}? Continue? (yes/no): ")
    if confirm.lower() not in ["yes", "y"]:
        print("Cancelled.")
        sys.exit(0)

    try:
        count = (mark_all_null if all_null else mark_scoped)(journal_date)
        print(f"\n✅ Successfully marked {count} summaries as published")
        print(f"   Journal date: {journal_date}")
        if count == 0:
            print("\n⚠️  Nothing to update — summaries may already be marked.")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
