#!/usr/bin/env python3
"""
Bulk generate summaries for unchecked URLs in workdesk/sources.md.

This script scans workdesk/sources.md for unchecked entries (- [ ]), generates
summaries for each, and marks them as checked (- [x]) after successful generation.

Usage:
    # Generate summaries for all unchecked URLs
    uv run scripts/bulk_summarize.py

    # Verbose output
    uv run scripts/bulk_summarize.py --verbose

    # Dry run (check what would be processed)
    uv run scripts/bulk_summarize.py --dry-run
"""

import sys
import argparse
import subprocess
import re
from pathlib import Path
from typing import List, Tuple, Dict
from urllib.parse import urlparse

def find_unchecked_urls(sources_file: Path) -> List[Tuple[int, str]]:
    """
    Find all unchecked URLs in sources.md.

    Returns:
        List of (id, url) tuples for unchecked entries
    """
    unchecked = []

    if not sources_file.exists():
        print(f"ERROR: {sources_file} not found")
        return unchecked

    with open(sources_file, 'r') as f:
        for line in f:
            # Match lines like: - [ ] 001. https://...
            match = re.match(r'-\s*\[\s*\]\s*(\d+)\.\s*(https?://\S+)', line.strip())
            if match:
                url_id = int(match.group(1))
                url = match.group(2)
                unchecked.append((url_id, url))

    return unchecked

def generate_summary(url: str, url_id: int, summaries_dir: Path) -> Tuple[bool, str]:
    """Generate summary for URL."""
    try:
        # Create filename from URL
        parsed = urlparse(url)
        domain = parsed.netloc.replace('www.', '').replace('.', '_')

        # Simple filename: ID_domain.md
        filename = f"{url_id:03d}_{domain}.md"
        output_path = summaries_dir / filename

        # Check if summary already exists (skip if so)
        if output_path.exists():
            return True, f"Summary already exists: {output_path}"

        # Generate summary
        result = subprocess.run(
            ['uv', 'run', 'scripts/call-gemini.py', '--url', url, '--output', str(output_path)],
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode == 0 and output_path.exists():
            return True, str(output_path)
        else:
            return False, f"ERROR: {result.stderr}"

    except subprocess.TimeoutExpired:
        return False, "ERROR: Timeout generating summary"
    except Exception as e:
        return False, f"ERROR: {str(e)}"

def mark_as_checked(sources_file: Path, url_id: int) -> bool:
    """Mark URL as checked in sources.md."""
    try:
        with open(sources_file, 'r') as f:
            content = f.read()

        # Replace - [ ] XXX. with - [x] XXX.
        pattern = rf'-\s*\[\s*\]\s*{url_id:03d}\.'
        replacement = f'- [x] {url_id:03d}.'
        updated_content = re.sub(pattern, replacement, content)

        with open(sources_file, 'w') as f:
            f.write(updated_content)

        return True
    except Exception as e:
        print(f"ERROR marking as checked: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description='Bulk generate summaries for unchecked URLs in sources.md'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be processed without generating summaries'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )

    args = parser.parse_args()

    # Setup paths
    base_dir = Path(__file__).parent.parent
    sources_file = base_dir / 'workdesk' / 'sources.md'
    summaries_dir = base_dir / 'workdesk' / 'summaries'
    summaries_dir.mkdir(exist_ok=True, parents=True)

    # Find unchecked URLs
    print("Scanning workdesk/sources.md for unchecked URLs...")
    unchecked_urls = find_unchecked_urls(sources_file)

    if not unchecked_urls:
        print("\n✓ No unchecked URLs found. All sources are already processed!")
        sys.exit(0)

    print(f"Found {len(unchecked_urls)} unchecked URLs\n")

    if args.dry_run:
        print("=" * 60)
        print("DRY RUN - Would process these URLs:")
        print("=" * 60)
        for url_id, url in unchecked_urls:
            print(f"[{url_id:03d}] {url}")
        print(f"\nTotal: {len(unchecked_urls)} URLs")
        print("\nRun without --dry-run to generate summaries")
        sys.exit(0)

    # Process unchecked URLs
    results: Dict[int, dict] = {}

    print("=" * 60)
    print("Generating summaries")
    print("=" * 60)

    for url_id, url in unchecked_urls:
        print(f"\n[{url_id:03d}] Processing: {url}")

        success, result = generate_summary(url, url_id, summaries_dir)

        if success:
            print(f"✓ Summary generated: {result}")

            # Mark as checked
            if mark_as_checked(sources_file, url_id):
                print(f"✓ Marked as checked in sources.md")
                results[url_id] = {'success': True, 'path': result}
            else:
                print(f"✗ Failed to mark as checked")
                results[url_id] = {'success': False, 'error': 'Failed to mark as checked'}
        else:
            print(f"✗ Failed: {result}")
            results[url_id] = {'success': False, 'error': result}

    # Final summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    total = len(unchecked_urls)
    successful = sum(1 for data in results.values() if data.get('success', False))
    failed = total - successful

    print(f"Total URLs processed: {total}")
    print(f"Summaries generated: {successful}")
    print(f"Failed: {failed}")

    if failed > 0:
        print("\nFailed IDs:")
        for url_id, data in results.items():
            if not data.get('success', False):
                print(f"  [{url_id:03d}] {data.get('error', 'Unknown error')}")

    print("\nDone! ✓")

    if failed > 0:
        sys.exit(1)

if __name__ == '__main__':
    main()
