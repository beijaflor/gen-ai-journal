#!/usr/bin/env python3
"""
Shift journal_date for summaries when journals were mis-dated.

Corrects the 2026-04-25 skipped-week shift: each affected journal_date is
moved back 7 days. Processed in ASCENDING order so each target date is free.

Usage:
    uv run scripts/shift_journal_date.py --dry-run   # read-only: show counts
    uv run scripts/shift_journal_date.py --apply     # perform the shift (prompts)
"""

import os
import sys
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

# (old_date, new_date) — MUST stay ascending by old_date so targets are free.
SHIFTS = [
    ("2026-05-02", "2026-04-25"),
    ("2026-05-09", "2026-05-02"),
    ("2026-05-16", "2026-05-09"),
    ("2026-05-23", "2026-05-16"),
    ("2026-05-30", "2026-05-23"),
]


def count(date_str):
    r = supabase.table("summary_metadata").select("id", count="exact").eq(
        "journal_date", date_str).execute()
    return r.count if r.count is not None else (len(r.data) if r.data else 0)


def show_distribution(label):
    print(f"\n=== {label} ===")
    dates = ["2026-04-25", "2026-05-02", "2026-05-09", "2026-05-16",
             "2026-05-23", "2026-05-30"]
    for d in dates:
        print(f"  journal_date={d}: {count(d)} rows")


def main():
    mode = sys.argv[1] if len(sys.argv) == 2 else None
    if mode not in ("--dry-run", "--apply"):
        print("Usage: uv run scripts/shift_journal_date.py [--dry-run|--apply]")
        sys.exit(1)

    show_distribution("CURRENT distribution (before)")

    print("\nPlanned shifts (ascending):")
    for old, new in SHIFTS:
        print(f"  {old} -> {new}")

    if mode == "--dry-run":
        print("\n(dry-run) No changes made.")
        return

    confirm = input("\nApply these journal_date shifts to production Supabase? (yes/no): ")
    if confirm.lower() not in ("yes", "y"):
        print("Cancelled.")
        sys.exit(0)

    total = 0
    for old, new in SHIFTS:
        r = supabase.table("summary_metadata").update(
            {"journal_date": new}).eq("journal_date", old).execute()
        n = len(r.data) if r.data else 0
        total += n
        print(f"  {old} -> {new}: {n} rows updated")

    print(f"\n✅ Shifted {total} rows total.")
    show_distribution("NEW distribution (after)")


if __name__ == "__main__":
    main()
