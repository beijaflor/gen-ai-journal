#!/usr/bin/env python3
"""
Script to gather summaries from a list of links. Summaries are stored in a directory.

Usage:
    python unite_summaries.py <file_path> <summaries_dir_path> <output_file_path>

Arguments:
    file_path: Path to the file to extract urls from
    summaries_dir_path: Path to the directory containing summaries
    output_file_path: Path to the file to output the result to

Output:
    A new file with the summaries of the links in the input file
    Reports missing summaries to console
"""
import sys
import os
import re

if len(sys.argv) != 4:
    print("Usage: python unite_summaries.py <file_path> <summaries_dir_path> <output_file_path>")
    sys.exit(1)

input_file = sys.argv[1]
summaries_dir = sys.argv[2]
output_file = sys.argv[3]

import json

# Parse the sources file into ordered (id, url) entries. Matching is by the
# NNN_ id prefix (authoritative), NOT by content.url: a summary produced via a
# paywall fallback (e.g. an HN-thread swap) has content.url pointing at the
# proxy, so URL-based matching would silently drop it. The id prefix ties each
# summary file to its sources line regardless of what content.url ended up being,
# and is also immune to trailing-slash / canonicalization drift.
entries = []  # (id, source_url) in sources-file order
with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        m = re.match(r'^\s*- \[.\] (\d{3})\. (\S+)', line)
        if m:
            entries.append((m.group(1), m.group(2)))

# Render each summary file, keyed by its NNN id prefix.
summary_by_id = {}
for filename in sorted(os.listdir(summaries_dir)):
    m = re.match(r'(\d{3})_', filename)
    if not m:
        continue
    fid = m.group(1)
    filepath = os.path.join(summaries_dir, filename)

    if filename.endswith('.json'):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, OSError):
            continue  # non-JSON (e.g. a fail-closed BLOCKED stub) -> treated as missing
        c = data.get('content', {})
        url = c.get('url', '')
        title = c.get('title', 'Untitled')
        original_title = c.get('originalTitle')
        one_sentence = c.get('oneSentenceSummary', '')
        summary_body = c.get('summaryBody', '')
        markdown = f"## {title}\n\n{url}\n\n"
        if original_title:
            markdown += f"**Original Title**: {original_title}\n\n"
        markdown += f"{one_sentence}\n\n{summary_body}"
        summary_by_id[fid] = markdown

    elif filename.endswith('.md'):
        with open(filepath, 'r', encoding='utf-8') as f:
            summary_by_id[fid] = f.read()

# Assemble in sources-file order, matching by id.
found_summaries = []
missing = []  # (id, url)
for fid, url in entries:
    if fid in summary_by_id:
        found_summaries.append(summary_by_id[fid])
    else:
        missing.append((fid, url))

# Write unified summaries
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n\n---\n\n'.join(found_summaries))

# Report results
print(f"Created {output_file} with {len(found_summaries)} summaries")
if missing:
    print(f"Missing summaries ({len(missing)}):")
    for fid, url in missing:
        print(f"  - {fid}: {url}")
else:
    print("All summaries found!")
