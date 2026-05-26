#!/usr/bin/env python3
"""READ-ONLY investigation of summary_metadata journal_date distribution
and the 2026-04-25 over-count. Makes no writes."""
import os, sys, json, glob
from collections import Counter, defaultdict
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client

load_dotenv(Path(__file__).parent / ".env")
sb = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY"))

# 1. Build url -> set(journal archive dates) from archived summaries
url2dates = defaultdict(set)
for f in glob.glob("journals/*/summaries/*.json"):
    date = f.split("/")[1]
    try:
        c = json.load(open(f)).get("content", {})
    except Exception:
        continue
    for key in ("url",):
        u = c.get(key)
        if u:
            url2dates[u].add(date)
    # also index alt source url if present (HN-keyed fallbacks)
    alt = c.get("contentSourceUrl")
    if alt:
        url2dates[alt].add(date)
print(f"Archived summaries indexed: {len(url2dates)} distinct URLs across {len(set(glob.glob('journals/*/summaries')))} dirs")

# 2. Fetch ALL summary_metadata rows (paginated)
rows = []
start = 0
while True:
    r = sb.table("summary_metadata").select(
        "id,summary_id,url,journal_date,created_at").range(start, start+999).execute()
    rows.extend(r.data)
    if len(r.data) < 1000:
        break
    start += 1000
print(f"Total summary_metadata rows: {len(rows)}")

# 3. Full journal_date distribution
dist = Counter((row["journal_date"] or "NULL") for row in rows)
print("\n=== journal_date distribution (all) ===")
for d, n in sorted(dist.items()):
    print(f"  {d}: {n}")

# 4. Whole-table health: compare each row's current journal_date to its "correct"
#    date (the archive whose summaries/ contains the row's url).
def correct_date(row):
    ds = url2dates.get(row["url"], set())
    if not ds:
        return None  # orphan
    return sorted(ds)[0]  # (urls map to a single archive in practice)

correct_cnt = 0
orphan_rows = []
mismatch = Counter()  # (current, correct) -> n
true_by_date = Counter()  # correct date -> n (what each journal SHOULD have)
for row in rows:
    cur = row["journal_date"] or "NULL"
    cor = correct_date(row)
    if cor is None:
        orphan_rows.append(row); continue
    true_by_date[cor] += 1
    if cur == cor:
        correct_cnt += 1
    else:
        mismatch[(cur, cor)] += 1

print(f"\n=== Whole-table health ===")
print(f"  correctly placed: {correct_cnt}")
print(f"  mis-placed:       {sum(mismatch.values())}")
print(f"  orphan (url in no archive): {len(orphan_rows)}")

print("\n=== Mis-placements: current journal_date -> correct date (count) ===")
for (cur, cor), n in sorted(mismatch.items(), key=lambda x: -x[1]):
    print(f"  {cur:>12}  ->  {cor:<12}  {n}")

print("\n=== Per-archive: how many Supabase rows SHOULD carry each date (by url) ===")
for d, n in sorted(true_by_date.items()):
    print(f"  {d}: {n}")

print(f"\n=== Orphans: {len(orphan_rows)} (url in NO archived journal) ===")
om = Counter((r['created_at'] or '')[:7] for r in orphan_rows)
for m, n in sorted(om.items()):
    print(f"  created {m}: {n}")
for row in orphan_rows[:10]:
    print(f"    {row.get('summary_id')}  {(row.get('created_at') or '')[:10]}  jd={row['journal_date']}  {row['url'][:70]}")
