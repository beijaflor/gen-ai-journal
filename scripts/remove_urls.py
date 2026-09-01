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

The URL regex, cleaning, and exact-match filtering live in scripts/workflow/urls.py
so this script and list_urls.py share one definition of a URL. The names
``clean_url``, ``urls_in_line`` and ``filter_lines`` are re-exported here for the
existing test suite (scripts/test_remove_urls.py).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from workflow.urls import URL_PATTERN, clean_url, urls_in_line, exact_filter  # noqa: E402,F401

# Backwards-compatible name: the exact-match line filter.
filter_lines = exact_filter


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
