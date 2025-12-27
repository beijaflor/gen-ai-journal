#!/usr/bin/env python3
"""
Check a link before adding to the GenAI journal workflow.
This script:
1. Accepts a URL as input
2. Sanitizes the URL (removes UTM params and fragments)
3. Follows HTTP redirects to get the final destination URL
4. Checks for duplicates in existing summaries (both original and final URLs)
"""

import sys
import re
import ipaddress
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from pathlib import Path
import requests
from requests.exceptions import RequestException

def validate_url(url):
    """
    Validate that the URL is a public URL and not localhost or private IP.
    Returns (is_valid, error_message) tuple.
    """
    parsed = urlparse(url)
    hostname = parsed.hostname

    if not hostname:
        return False, "Invalid URL: no hostname found"

    # Check for localhost
    localhost_patterns = ['localhost', '127.', '0.0.0.0', '::1']
    if any(hostname.startswith(pattern) for pattern in localhost_patterns):
        return False, "localhost URLs are not allowed"

    # Check if hostname is an IP address
    try:
        ip = ipaddress.ip_address(hostname)

        # Check if it's a private IP address
        if ip.is_private:
            return False, f"Private IP address not allowed: {hostname}"

        # Check if it's a loopback address
        if ip.is_loopback:
            return False, f"Loopback IP address not allowed: {hostname}"

        # Check if it's link-local
        if ip.is_link_local:
            return False, f"Link-local IP address not allowed: {hostname}"

        # Public IP addresses are discouraged (prefer domain names)
        print(f"Warning: Using IP address {hostname} instead of domain name")

    except ValueError:
        # Not an IP address, which is good - it's a domain name
        pass

    return True, None

def sanitize_url(url):
    """Removes tracking parameters and fragments from a URL."""
    parsed_url = urlparse(url)

    # Sites where query parameters should be preserved completely
    preserve_params_sites = ['lukew.com', 'en.wikipedia.org']

    # If this is a site where we should preserve params, keep original query
    if any(site in parsed_url.netloc for site in preserve_params_sites):
        sanitized_query = parsed_url.query
    else:
        # Parse and filter query parameters for other sites
        query_params = parse_qs(parsed_url.query)
        tracking_params = ['utm_', 'fbclid', 'gclid', 'mc_', 'ref', 'source']
        sanitized_params = {
            k: v for k, v in query_params.items()
            if not any(k.startswith(prefix) for prefix in tracking_params)
        }
        sanitized_query = urlencode(sanitized_params, doseq=True)

    # Reconstruct the URL, removing the fragment
    sanitized_url = urlunparse(parsed_url._replace(query=sanitized_query, fragment=''))
    return sanitized_url


def follow_redirects(url, timeout=10):
    """
    Follow HTTP redirects and return the final destination URL.
    Returns (final_url, redirect_chain) or (None, None) if unable to follow.
    """
    try:
        # Make HEAD request to avoid downloading content
        response = requests.head(
            url,
            allow_redirects=True,
            timeout=timeout,
            headers={'User-Agent': 'Mozilla/5.0 (GenAI Journal Link Checker)'}
        )

        final_url = response.url

        # Build redirect chain
        redirect_chain = []
        if response.history:
            for resp in response.history:
                redirect_chain.append(resp.url)
            redirect_chain.append(final_url)

        return final_url, redirect_chain
    except RequestException as e:
        # If HEAD fails, try GET (some servers don't support HEAD)
        try:
            response = requests.get(
                url,
                allow_redirects=True,
                timeout=timeout,
                stream=True,  # Don't download content
                headers={'User-Agent': 'Mozilla/5.0 (GenAI Journal Link Checker)'}
            )
            response.close()

            final_url = response.url
            redirect_chain = []
            if response.history:
                for resp in response.history:
                    redirect_chain.append(resp.url)
                redirect_chain.append(final_url)

            return final_url, redirect_chain
        except RequestException:
            # Unable to follow redirects
            return None, None


def check_duplicate(sanitized_url, final_url=None):
    """
    Check if URL already exists in sources or summaries.
    Checks both the sanitized URL and final URL (if different after redirects).
    Returns (is_duplicate, duplicate_locations) tuple.
    """
    duplicate_locations = []
    urls_to_check = [sanitized_url]

    # If we have a final URL from redirects and it's different, check both
    if final_url and final_url != sanitized_url:
        urls_to_check.append(final_url)

    # Check in workdesk/sources.md
    sources_file = Path("workdesk/sources.md")
    if sources_file.exists():
        try:
            with open(sources_file, 'r') as f:
                content = f.read()
                for url in urls_to_check:
                    if url in content:
                        duplicate_locations.append(("workdesk/sources.md", url))
        except:
            pass

    # Check in workdesk/summaries directory
    summaries_dir = Path("workdesk/summaries")
    if summaries_dir.exists():
        for file in summaries_dir.glob("*.md"):
            try:
                with open(file, 'r') as f:
                    content = f.read()
                    for url in urls_to_check:
                        if url in content:
                            duplicate_locations.append((f"workdesk/summaries/{file.name}", url))
            except:
                continue

    # Check in published journals (journals/*/sources/*.md)
    journals_dir = Path("journals")
    if journals_dir.exists():
        for sources_file in journals_dir.glob("*/sources/*.md"):
            try:
                with open(sources_file, 'r') as f:
                    content = f.read()
                    for url in urls_to_check:
                        if url in content:
                            duplicate_locations.append((str(sources_file), url))
            except:
                continue

    return (True, duplicate_locations) if duplicate_locations else (False, None)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/check_link.py <URL>")
        print("Example: python3 scripts/check_link.py https://example.com/article")
        sys.exit(1)

    url = sys.argv[1]

    # Step 1: Accept URL as input
    print(f"Original URL: {url}")

    # Step 1.5: Validate URL (reject localhost and private IPs)
    is_valid, error_message = validate_url(url)
    if not is_valid:
        print(f"\n❌ Error: {error_message}")
        print("\nOnly public URLs with domain names are allowed.")
        print("Examples of rejected URLs:")
        print("  - http://localhost:3000")
        print("  - http://127.0.0.1:8080")
        print("  - http://192.168.1.1")
        print("  - http://10.0.0.1")
        sys.exit(1)

    # Step 2: Sanitize URL
    sanitized_url = sanitize_url(url)
    print(f"Sanitized URL: {sanitized_url}")

    if url != sanitized_url:
        print("Note: URL was modified (removed tracking params/fragments)")

    # Step 3: Follow redirects
    print("\nFollowing redirects...")
    final_url, redirect_chain = follow_redirects(sanitized_url)

    if final_url:
        if redirect_chain:
            print(f"Final URL (after redirects): {final_url}")
            print(f"Redirect chain ({len(redirect_chain)} hops):")
            for i, redirect_url in enumerate(redirect_chain, 1):
                print(f"  {i}. {redirect_url}")
        else:
            print(f"No redirects detected")
            final_url = sanitized_url
    else:
        print("Warning: Unable to follow redirects (network error or timeout)")
        print("Will check for duplicates using sanitized URL only")
        final_url = None

    # Step 4: Check for duplicates (both sanitized and final URLs)
    is_duplicate, duplicates = check_duplicate(sanitized_url, final_url)

    if is_duplicate:
        print(f"\n❌ Error: URL already exists!")
        print("\nDuplicates found:")
        for location, matched_url in duplicates:
            if matched_url != sanitized_url:
                print(f"  - {location}")
                print(f"    Matched via redirect: {matched_url}")
            else:
                print(f"  - {location}")
        sys.exit(1)
    else:
        print("\n✅ URL is unique and ready to be added")

if __name__ == "__main__":
    main()