#!/usr/bin/env python3
"""
Process and combine summaries for omitted sources.

This script reads the omitted_sources.md file and finds the corresponding
summary files for each URL, then combines them into a single file.

Usage:
    python process_omitted_summaries.py <directory_path>

Arguments:
    directory_path: Path to a journal directory containing:
        - sources/omitted_sources.md: List of omitted source URLs
        - summaries/: Directory containing individual summary .md files

Output:
    - omitted_summaries.md: Combined summaries separated by --- dividers
    - sources/error_sources.md: URLs without corresponding summaries (if any)

The script matches URLs by searching for them within summary files, as each
summary file contains exactly one URL.

Example:
    python process_omitted_summaries.py journals/2025-07-09
"""
import sys
import os
import re

if len(sys.argv) != 2:
    print("Usage: python process_omitted_summaries.py <directory_path>")
    sys.exit(1)

directory = sys.argv[1]
sources_dir = os.path.join(directory, "sources")
summaries_dir = os.path.join(directory, "summaries")

# Read omitted sources
omitted_sources_file = os.path.join(sources_dir, "omitted_sources.md")
with open(omitted_sources_file, 'r') as f:
    content = f.read()
    omitted_urls = re.findall(r'https://[^\s\]]+', content)

# Build URL to content mapping from summaries
url_to_content = {}
for filename in os.listdir(summaries_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(summaries_dir, filename)
        with open(filepath, 'r') as f:
            content = f.read()
            # Find URL in the content
            urls = re.findall(r'https://[^\s\]]+', content)
            if urls:
                # Take the first URL found (each summary should have only one)
                url = urls[0]
                url_to_content[url] = content

# Process omitted URLs
found_summaries = []
error_urls = []

for url in omitted_urls:
    if url in url_to_content:
        found_summaries.append(url_to_content[url])
    else:
        error_urls.append(url)

# Write omitted summaries
output_file = os.path.join(directory, "omitted_summaries.md")
with open(output_file, 'w') as f:
    f.write("\n\n---\n\n".join(found_summaries))

# Write error sources
if error_urls:
    error_file = os.path.join(sources_dir, "error_sources.md")
    with open(error_file, 'w') as f:
        for url in error_urls:
            f.write(f"- {url}\n")
    print(f"Created {error_file} with {len(error_urls)} missing summaries")

print(f"Created {output_file} with {len(found_summaries)} summaries")