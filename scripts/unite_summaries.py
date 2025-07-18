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

# Extract URLs from input file
with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()
    input_urls = re.findall(r'https://[^\s\]]+', content)

# Build URL to content mapping from summaries
url_to_content = {}
for filename in os.listdir(summaries_dir):
    if filename.endswith('.md'):
        filepath = os.path.join(summaries_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            summary_content = f.read()
            # Find URL in the summary content
            urls = re.findall(r'https://[^\s\]]+', summary_content)
            if urls:
                # Take the first URL found (each summary should have only one)
                url = urls[0]
                url_to_content[url] = summary_content

# Process input URLs
found_summaries = []
missing_urls = []

for url in input_urls:
    if url in url_to_content:
        found_summaries.append(url_to_content[url])
    else:
        missing_urls.append(url)

# Write unified summaries
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n\n---\n\n'.join(found_summaries))

# Report results
print(f"Created {output_file} with {len(found_summaries)} summaries")
if missing_urls:
    print(f"Missing summaries ({len(missing_urls)}):")
    for url in missing_urls:
        print(f"  - {url}")
else:
    print("All summaries found!")
