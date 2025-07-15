#!/usr/bin/env python3
"""
Process omitted sources from journal entries.

This script identifies URLs that are present in the main sources.md file
but have not been included in either of the curated source lists.

Usage:
    python process_omitted_sources.py <directory_path>

Arguments:
    directory_path: Path to a directory containing:
        - sources.md: Complete list of source URLs
        - curated_journal_sources.md: Curated main journal sources
        - curated_annex_journal_sources.md: Curated annex journal sources

Output:
    Creates omitted_sources.md in the same directory with URLs that were
    not included in either curated list, formatted as a markdown list.

Example:
    python process_omitted_sources.py journals/2025-07-09/sources
"""
import sys
import re
import os

if len(sys.argv) != 2:
    print("Usage: python process_omitted_sources.py <directory_path>")
    sys.exit(1)

directory = sys.argv[1]

# Read all URLs from sources.md
sources_file = os.path.join(directory, "sources.md")
with open(sources_file, 'r') as f:
    sources_content = f.read()

# Extract URLs from sources.md
all_urls = re.findall(r'https://[^\s\]]+', sources_content)

# Read curated URLs
curated_urls = set()

# Read from curated_journal_sources.md
curated_file1 = os.path.join(directory, "curated_journal_sources.md")
with open(curated_file1, 'r') as f:
    content = f.read()
    curated_urls.update(re.findall(r'https://[^\s\]]+', content))

# Read from curated_annex_journal_sources.md
curated_file2 = os.path.join(directory, "curated_annex_journal_sources.md")
with open(curated_file2, 'r') as f:
    content = f.read()
    curated_urls.update(re.findall(r'https://[^\s\]]+', content))

# Find omitted URLs (in sources but not in curated)
omitted_urls = [url for url in all_urls if url not in curated_urls]

# Write omitted URLs to file
output_file = os.path.join(directory, "omitted_sources.md")
with open(output_file, 'w') as f:
    for url in omitted_urls:
        f.write(f"- {url}\n")

print(f"Created {output_file} with {len(omitted_urls)} omitted URLs")