#!/usr/bin/env python3
"""Reclassify orphan rows using a NORMALIZED URL index built from
summaries/*.json + 99_unified_summaries.md (出典) + sources/sources.md.
Re-assigns rows that deterministically map to one journal; reports the
true remainder.

  uv run scripts/remediate_orphans.py --dry-run
  uv run scripts/remediate_orphans.py --apply
"""
import os, json, glob, re, sys
from collections import defaultdict, Counter
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client

load_dotenv(Path(__file__).parent / ".env")
sb = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY"))
mode = sys.argv[1] if len(sys.argv) == 2 else None
if mode not in ("--dry-run", "--apply"):
    print("Usage: remediate_orphans.py [--dry-run|--apply]"); sys.exit(1)

URLRE = re.compile(r'https?://[^\s\)\]]+')

def norm(u):
    if not u: return None
    u = u.strip().split("#")[0]
    u = re.sub(r'^https?://', '', u, flags=re.I)
    u = re.sub(r'^www\.', '', u, flags=re.I)
    u = u.rstrip('/').rstrip('.,;)\'"')
    return u.lower()

idx = defaultdict(set)  # norm(url) -> {dates}
# strict: summaries/*.json
for f in glob.glob("journals/*/summaries/*.json"):
    d = f.split("/")[1]
    try: c = json.load(open(f)).get("content", {})
    except Exception: continue
    for u in (c.get("url"), c.get("contentSourceUrl")):
        k = norm(u)
        if k: idx[k].add(d)
# legacy: 99_unified 出典 + sources.md
for f in glob.glob("journals/*/99_unified_summaries.md") + glob.glob("journals/*/sources/sources.md"):
    d = f.split("/")[1]
    try: txt = open(f, encoding="utf-8").read()
    except Exception: continue
    for u in URLRE.findall(txt):
        k = norm(u)
        if k: idx[k].add(d)

rows = []
start = 0
while True:
    r = sb.table("summary_metadata").select("id,url,journal_date").range(start, start+999).execute()
    rows.extend(r.data);
    if len(r.data) < 1000: break
    start += 1000

plan = defaultdict(list); multi = 0; true_orphan = []
for row in rows:
    ds = idx.get(norm(row["url"]), set())
    if not ds:
        true_orphan.append(row); continue
    if len(ds) > 1:
        multi += 1; continue
    cor = next(iter(ds))
    if (row["journal_date"] or None) != cor:
        plan[cor].append(row["id"])

total = sum(len(v) for v in plan.values())
print(f"Indexed {len(idx)} normalized URLs. Multi-mapped rows skipped: {multi}")
print(f"\nDeterministic re-assignments (post-normalization): {total}")
for d, ids in sorted(plan.items()):
    print(f"  -> {d}: {len(ids)}")
print(f"\nTrue remaining orphans (no match even normalized): {len(true_orphan)}")
om = Counter((r['journal_date'] or 'NULL') for r in true_orphan)
print("  truly-orphan by current journal_date:", dict(sorted(om.items())))

if mode == "--dry-run":
    print("\n(dry-run) no writes."); sys.exit(0)

confirm = input(f"\nApply {total} re-assignments? (truly-orphan {len(true_orphan)} left untouched) (yes/no): ")
if confirm.lower() not in ("yes", "y"):
    print("Cancelled."); sys.exit(0)
done = 0
for d, ids in sorted(plan.items()):
    for i in range(0, len(ids), 100):
        sb.table("summary_metadata").update({"journal_date": d}).in_("id", ids[i:i+100]).execute()
        done += len(ids[i:i+100])
    print(f"  set {d}: {len(ids)}")
print(f"\n✅ Re-assigned {done}. Truly-orphan remaining (untouched): {len(true_orphan)}")
