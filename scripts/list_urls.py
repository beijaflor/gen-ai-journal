#!/usr/bin/env python3
"""
Script to extract urls from a file

Usage:
    python list_urls.py <file_path>

Arguments:
    file_path: Path to the file to extract urls from

Output:
    Prints the urls to the console
"""

import sys
import re

def extract_urls(file_path):
    """Extract all URLs from a file."""
    urls = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Regular expression to match URLs
        url_pattern = r'https?://[^\s\[\]()]+(?:\([^\)]*\))?[^\s\[\]()]*'
        urls = re.findall(url_pattern, content)
        
        # Clean up URLs (remove trailing punctuation)
        cleaned_urls = []
        for url in urls:
            # Remove trailing punctuation
            url = re.sub(r'[.,;:!?)]+$', '', url)
            cleaned_urls.append(url)
            
        return cleaned_urls
        
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
    urls = extract_urls(file_path)
    
    if urls:
        for url in urls:
            print(url)
    else:
        print("No URLs found.")

if __name__ == "__main__":
    main()