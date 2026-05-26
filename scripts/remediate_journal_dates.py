#!/usr/bin/env python3
"""Re-assign mis-placed summary_metadata rows to the journal_date whose
archived summaries/ contains the row's URL. Deterministic, by exact row id.

  uv run scripts/remediate_journal_dates.py --dry-run
  uv run scripts/remediate_journal_dates.py --apply
"""
import os, sys, json, glob
from collections import defaultdict, Counter
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client

load_dotenv(Path(__file__).parent / ".env")
sb = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY"))

mode = sys.argv[1] if len(sys.argv) == 2 else None
if mode not in ("--dry-run", "--apply"):
    print("Usage: remediate_journal_dates.py [--dry-run|--apply]"); sys.exit(1)

# url -> set(dates) from archived summaries/*.json
url2dates = defaultdict(set)
for f in glob.glob("journals/*/summaries/*.json"):
    date = f.split("/")[1]
    try:
        c = json.load(open(f)).get("content", {})
    except Exception:
        continue
    for u in (c.get("url"), c.get("contentSourceUrl")):
        if u:
            url2dates[u].add(date)

multi = {u: ds for u, ds in url2dates.items() if len(ds) > 1}
print(f"Indexed {len(url2dates)} URLs; {len(multi)} map to >1 archive (excluded from auto-fix)")

# fetch all rows
rows = []
start = 0
while True:
    r = sb.table("summary_metadata").select("id,url,journal_date").range(start, start+999).execute()
    rows.extend(r.data)
    if len(r.data) < 1000:
        break
    start += 1000

# plan: correct_date -> [ids] for rows whose url maps to exactly one archive != current
plan = defaultdict(list)
skipped_multi = 0
for row in rows:
    ds = url2dates.get(row["url"], set())
    if not ds:
        continue  # orphan -> leave
    if len(ds) > 1:
        skipped_multi += 1; continue
    correct = next(iter(ds))
    if (row["journal_date"] or None) != correct:
        plan[correct].append(row["id"])

total = sum(len(v) for v in plan.values())
print(f"\nPlanned re-assignments: {total} rows (skipped {skipped_multi} multi-mapped)")
for d, ids in sorted(plan.items()):
    print(f"  -> {d}: {len(ids)}")

if mode == "--dry-run":
    print("\n(dry-run) no writes."); sys.exit(0)

confirm = input(f"\nApply {total} journal_date re-assignments to production Supabase? (yes/no): ")
if confirm.lower() not in ("yes", "y"):
    print("Cancelled."); sys.exit(0)

done = 0
for d, ids in sorted(plan.items()):
    for i in range(0, len(ids), 100):
        batch = ids[i:i+100]
        sb.table("summary_metadata").update({"journal_date": d}).in_("id", batch).execute()
        done += len(batch)
    print(f"  set {d}: {len(ids)} rows")
print(f"\n✅ Re-assigned {done} rows.")
