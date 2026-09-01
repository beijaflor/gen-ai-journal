#!/usr/bin/env python3
"""
Script to remove lines containing URLs from a file, preserving exact formatting of remaining lines.

Usage:
    python list_urls.py source.txt | python remove_urls.py <input_file> <output_file>

Arguments:
    input_file: Path to the file to process
    output_file: Path to write the filtered result

Input:
    URLs to remove are read from stdin (one per line), typically piped from list_urls.py

Output:
    A new file with lines containing any of the URLs completely removed.
    All remaining lines are preserved exactly as-is (no formatting changes).
"""

import sys
import re

# Same URL pattern list_urls.py uses, so the two scripts agree on what a URL is.
URL_PATTERN = r'https?://[^\s\[\]()]+(?:\([^\)]*\))?[^\s\[\]()]*'


def clean_url(url):
    """Strip trailing punctuation, matching list_urls.py's cleaning."""
    return re.sub(r'[.,;:!?)]+$', '', url)


def urls_in_line(line):
    """Extract cleaned URLs contained in a line."""
    return [clean_url(u) for u in re.findall(URL_PATTERN, line)]


def filter_lines(lines, urls_to_remove):
    """Return the lines that do NOT contain an exact-match removal URL.

    A line is removed only when one of the URLs it actually contains is an
    exact member of ``urls_to_remove``. This avoids the prefix-collision bug
    of substring matching (``".../A95B"`` wrongly matching ``".../A95B-FP8"``).
    """
    remove = {clean_url(u) for u in urls_to_remove}
    kept = []
    for line in lines:
        if not any(u in remove for u in urls_in_line(line)):
            kept.append(line)
    return kept


def main():
    if len(sys.argv) != 3:
        print("Usage: python remove_urls.py <input_file> <output_file>")
        print("URLs to remove should be provided via stdin (pipe from list_urls.py)")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    # Read URLs from stdin
    try:
        urls_input = sys.stdin.read().strip()
        if not urls_input:
            print("No URLs provided via stdin.")
            sys.exit(1)
        # Clean the removal URLs the same way, so exact matching lines up
        # regardless of any trailing punctuation on either side.
        urls_to_remove = {clean_url(u.strip()) for u in urls_input.split('\n')}
        urls_to_remove.discard('')  # Remove empty strings
    except Exception as e:
        print(f"Error reading URLs from stdin: {e}")
        sys.exit(1)
    
    # Read input file preserving exact formatting
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)
    
    # Filter lines - remove a line only if one of the URLs it contains is an
    # EXACT match for a removal URL. Substring matching (the old behaviour)
    # wrongly dropped lines whose URL merely had a removal URL as a prefix
    # (e.g. ".../model-A95B" is a prefix of ".../model-A95B-FP8").
    filtered_lines = filter_lines(lines, urls_to_remove)
    
    # Write filtered result preserving exact formatting
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.writelines(filtered_lines)
        print(f"Processed {len(lines)} lines, removed {len(lines) - len(filtered_lines)} lines containing URLs.")
        print(f"Result written to '{output_file}'.")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
