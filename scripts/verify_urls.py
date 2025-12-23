#!/usr/bin/env python3
"""
Verify URLs in journal files are accessible.
"""
import sys
import time
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError

def check_url(url: str, timeout: int = 10) -> tuple[bool, int, str]:
    """Check if a URL is accessible. Returns (success, status_code, message)."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        req = Request(url, headers=headers)
        with urlopen(req, timeout=timeout) as response:
            return (True, response.status, "OK")
    except HTTPError as e:
        return (False, e.code, f"HTTP {e.code}: {e.reason}")
    except URLError as e:
        return (False, 0, f"URL Error: {e.reason}")
    except Exception as e:
        return (False, 0, f"Error: {str(e)}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python verify_urls.py <url_file>")
        sys.exit(1)

    url_file = Path(sys.argv[1])
    if not url_file.exists():
        print(f"Error: {url_file} not found")
        sys.exit(1)

    urls = url_file.read_text(encoding='utf-8').strip().split('\n')
    urls = [u.strip() for u in urls if u.strip()]

    print(f"Checking {len(urls)} URLs from {url_file.name}...")
    print()

    success_count = 0
    failed_urls = []

    for i, url in enumerate(urls, 1):
        success, status, message = check_url(url)

        if success:
            print(f"✓ [{i}/{len(urls)}] {url}")
            success_count += 1
        else:
            print(f"✗ [{i}/{len(urls)}] {url}")
            print(f"  └─ {message}")
            failed_urls.append((url, message))

        # Be nice to servers - small delay between requests
        if i < len(urls):
            time.sleep(0.5)

    print()
    print("=" * 70)
    print(f"Results: {success_count}/{len(urls)} URLs accessible")

    if failed_urls:
        print(f"\n{len(failed_urls)} failed URLs:")
        for url, msg in failed_urls:
            print(f"  - {url}")
            print(f"    {msg}")
        sys.exit(1)
    else:
        print("✓ All URLs are accessible!")
        sys.exit(0)

if __name__ == "__main__":
    main()
