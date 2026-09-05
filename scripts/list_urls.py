#!/usr/bin/env python3
"""
Script to extract urls from a file

Usage:
    python list_urls.py <file_path>

Arguments:
    file_path: Path to the file to extract urls from

Output:
    Prints the urls to the console

The URL regex and cleaning live in scripts/workflow/urls.py so this script and
remove_urls.py can never disagree about what counts as a URL.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from workflow.urls import extract_urls  # noqa: E402


def extract_urls_from_file(file_path):
    """Extract all cleaned URLs from a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return extract_urls(content)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []


def main():
    if len(sys.argv) != 2:
        print("Usage: python list_urls.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    urls = extract_urls_from_file(file_path)

    if urls:
        for url in urls:
            print(url)
    else:
        print("No URLs found.")


if __name__ == "__main__":
    main()
