#!/usr/bin/env python3
"""
Check a link before adding to the GenAI journal workflow.
This script:
1. Accepts a URL as input
2. Sanitizes the URL (removes UTM params and fragments)
3. Checks for duplicates in existing summaries
"""

import sys
import re
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from pathlib import Path

def sanitize_url(url):
    """Removes UTM parameters and fragments from a URL."""
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    # Remove UTM parameters
    sanitized_params = {k: v for k, v in query_params.items() if not k.startswith('utm_')}
    
    # Reconstruct the query string
    sanitized_query = urlencode(sanitized_params, doseq=True)
    
    # Reconstruct the URL, removing the fragment
    sanitized_url = urlunparse(parsed_url._replace(query=sanitized_query, fragment=''))
    return sanitized_url


def check_duplicate(sanitized_url):
    """Check if URL already exists in sources or summaries."""
    duplicate_locations = []
    
    # Check in sources.md
    sources_file = Path("workdesk/sources.md")
    if sources_file.exists():
        try:
            with open(sources_file, 'r') as f:
                content = f.read()
                if sanitized_url in content:
                    duplicate_locations.append("workdesk/sources.md")
        except:
            pass
    
    # Check in summaries directory
    summaries_dir = Path("workdesk/summaries")
    if summaries_dir.exists():
        for file in summaries_dir.glob("*.md"):
            try:
                with open(file, 'r') as f:
                    content = f.read()
                    if sanitized_url in content:
                        duplicate_locations.append(f"workdesk/summaries/{file.name}")
            except:
                continue
    
    return duplicate_locations if duplicate_locations else None


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/check_link.py <URL>")
        print("Example: python3 scripts/check_link.py https://example.com/article")
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Step 1: Accept URL as input
    print(f"Original URL: {url}")
    
    # Step 2: Sanitize URL
    sanitized_url = sanitize_url(url)
    print(f"Sanitized URL: {sanitized_url}")
    
    if url != sanitized_url:
        print("Note: URL was modified (removed UTM params/fragments)")
    
    # Step 3: Check for duplicates
    duplicates = check_duplicate(sanitized_url)
    if duplicates:
        print(f"\nError: URL already exists in:")
        for location in duplicates:
            print(f"  - {location}")
        sys.exit(1)
    else:
        print("\nURL is unique and ready to be added")

if __name__ == "__main__":
    main()