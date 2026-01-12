#!/usr/bin/env python3
"""
Mark workdesk summaries as published by setting their journal_date.

This script updates all workdesk summaries (journal_date IS NULL) to have
a specific journal date, indicating they've been published in that week's journal.

Usage:
    uv run scripts/mark_published.py 2025-12-27

Arguments:
    journal_date: The date of the journal in YYYY-MM-DD format
"""

import os
import sys
from pathlib import Path
from typing import List
from dotenv import load_dotenv
from supabase import create_client, Client
import re

# Load environment variables
load_dotenv(Path(__file__).parent / ".env")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    print("Error: SUPABASE_URL and SUPABASE_SERVICE_KEY must be set in scripts/.env")
    print("See scripts/.env.example for configuration")
    sys.exit(1)

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


def validate_date_format(date_str: str) -> bool:
    """Validate that date is in YYYY-MM-DD format."""
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    return bool(re.match(pattern, date_str))


def mark_as_published(journal_date: str) -> int:
    """
    Mark all workdesk summaries as published for the given journal date.

    Args:
        journal_date: The journal date in YYYY-MM-DD format

    Returns:
        Number of summaries updated
    """
    # Update all summaries where journal_date is NULL
    response = supabase.table("summary_metadata").update(
        {"journal_date": journal_date}
    ).is_("journal_date", "null").execute()

    return len(response.data) if response.data else 0


def main():
    """Main execution function."""
    if len(sys.argv) != 2:
        print("Usage: uv run scripts/mark_published.py YYYY-MM-DD")
        print("")
        print("Example:")
        print("  uv run scripts/mark_published.py 2025-12-27")
        sys.exit(1)

    journal_date = sys.argv[1]

    # Validate date format
    if not validate_date_format(journal_date):
        print(f"❌ Invalid date format: {journal_date}")
        print("   Date must be in YYYY-MM-DD format")
        sys.exit(1)

    print(f"Marking workdesk summaries as published for journal date: {journal_date}")
    print("")

    # Confirm with user
    confirm = input(f"This will set journal_date={journal_date} for ALL workdesk summaries. Continue? (yes/no): ")

    if confirm.lower() not in ["yes", "y"]:
        print("Cancelled.")
        sys.exit(0)

    try:
        count = mark_as_published(journal_date)
        print(f"\n✅ Successfully marked {count} summaries as published")
        print(f"   Journal date: {journal_date}")

        if count == 0:
            print("\n⚠️  No workdesk summaries found. Either:")
            print("   - No summaries have been created yet")
            print("   - All summaries have already been marked as published")

    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
