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
        urls_to_remove = set(urls_input.split('\n'))
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
    
    # Filter lines - remove any line containing any URL
    filtered_lines = []
    for line in lines:
        contains_url = any(url in line for url in urls_to_remove if url)
        if not contains_url:
            filtered_lines.append(line)
    
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
