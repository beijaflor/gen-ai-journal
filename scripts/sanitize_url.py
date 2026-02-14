#!/usr/bin/env python3
"""
Script to sanitize URLs by removing tracking parameters and fragments

Usage:
    python sanitize_url.py <url>
    echo <url> | python sanitize_url.py

Arguments:
    url: URL to sanitize (can be provided as argument or via stdin)

Output:
    Prints the sanitized URL without tracking parameters or fragments

Example:
    python sanitize_url.py "https://example.com/page?utm_source=twitter&id=123#section"
    # Output: https://example.com/page?id=123
"""

import sys
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

def sanitize_url(url):
    """Removes tracking parameters and fragments from a URL."""
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    
    # Remove common tracking parameters
    tracking_params = ['utm_', 'fbclid', 'gclid', 'mc_', 'ref', 'source', 'hl']
    sanitized_params = {
        k: v for k, v in query_params.items()
        if not any(k.startswith(prefix) for prefix in tracking_params)
    }
    
    # Reconstruct the query string
    sanitized_query = urlencode(sanitized_params, doseq=True)
    
    # Reconstruct the URL, removing the fragment
    sanitized_url = urlunparse(parsed_url._replace(query=sanitized_query, fragment=''))
    return sanitized_url

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # URL provided as argument
        url = sys.argv[1]
    else:
        # Read from stdin
        url = sys.stdin.read().strip()
    
    if url:
        print(sanitize_url(url))
    else:
        print("Usage: python3 sanitize_url.py <URL>")
        print("   or: echo <URL> | python3 sanitize_url.py")
        sys.exit(1)