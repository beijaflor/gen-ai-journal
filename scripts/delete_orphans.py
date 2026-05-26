#!/usr/bin/env python3
"""Delete true-orphan summary_metadata rows (url in NO journal archive,
even after normalization). Guarded against bad index builds.

  uv run scripts/delete_orphans.py --apply
"""
import os, json, glob, re, sys
from collections import defaultdict, Counter
from pathlib import Path
from dotenv import load_dotenv
from supabase import create_client

load_dotenv(Path(__file__).parent / ".env")
sb = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY"))
apply = (len(sys.argv) == 2 and sys.argv[1] == "--apply")

URLRE = re.compile(r'https?://[^\s\)\]]+')
def norm(u):
    if not u: return None
    u = u.strip().split("#")[0]
    u = re.sub(r'^https?://', '', u, flags=re.I)
    u = re.sub(r'^www\.', '', u, flags=re.I)
    return u.rstrip('/').rstrip('.,;)\'"').lower()

idx = set()
for f in glob.glob("journals/*/summaries/*.json"):
    try: c = json.load(open(f)).get("content", {})
    except Exception: continue
    for u in (c.get("url"), c.get("contentSourceUrl")):
        k = norm(u)
        if k: idx.add(k)
for f in glob.glob("journals/*/99_unified_summaries.md") + glob.glob("journals/*/sources/sources.md"):
    try: txt = open(f, encoding="utf-8").read()
    except Exception: continue
    for u in URLRE.findall(txt):
        k = norm(u)
        if k: idx.add(k)

# SAFETY: index must be healthy or we abort (prevents mass-delete on build failure)
assert len(idx) > 3000, f"index too small ({len(idx)}) — aborting to avoid mass delete"

rows = []
start = 0
while True:
    r = sb.table("summary_metadata").select("id,url,journal_date").range(start, start+999).execute()
    rows.extend(r.data)
    if len(r.data) < 1000: break
    start += 1000

orphans = [r for r in rows if norm(r["url"]) not in idx]
print(f"index size: {len(idx)} | total rows: {len(rows)} | true orphans: {len(orphans)}")
print("by current journal_date:", dict(sorted(Counter(r['journal_date'] or 'NULL' for r in orphans).items())))

# SAFETY: refuse if the orphan set is implausibly large
assert len(orphans) < 400, f"orphan count {len(orphans)} unexpectedly high — aborting"

print("\n--- rows to delete (audit dump) ---")
for r in orphans:
    print(f"{r['id']}\t{r['journal_date']}\t{r['url']}")

if not apply:
    print(f"\n(dry-run) would delete {len(orphans)} rows. Re-run with --apply.")
    sys.exit(0)

ids = [r["id"] for r in orphans]
done = 0
for i in range(0, len(ids), 100):
    sb.table("summary_metadata").delete().in_("id", ids[i:i+100]).execute()
    done += len(ids[i:i+100])
print(f"\n✅ Deleted {done} orphan rows.")

# verify
after = sb.table("summary_metadata").select("id", count="exact").limit(1).execute()
print(f"summary_metadata total now: {after.count}")
