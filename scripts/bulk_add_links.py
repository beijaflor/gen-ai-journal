#!/usr/bin/env python3
"""
Bulk add links to workdesk/sources.md and generate summaries.

This script automates the complete add-link workflow for multiple URLs:
1. Validates and sanitizes each URL
2. Checks for duplicates
3. Adds unique URLs to sources.md
4. Generates summaries for each URL
5. Marks URLs as processed

Usage:
    # Add URLs from a file (one URL per line)
    uv run scripts/bulk_add_links.py urls.txt

    # Add URLs from stdin
    cat urls.txt | uv run scripts/bulk_add_links.py

    # Add URLs directly
    echo "https://example.com" | uv run scripts/bulk_add_links.py

    # Dry run (check without adding)
    uv run scripts/bulk_add_links.py urls.txt --dry-run

    # Skip summary generation
    uv run scripts/bulk_add_links.py urls.txt --no-summarize
"""

import sys
import argparse
import subprocess
import re
from pathlib import Path
from typing import List, Tuple, Dict

def read_urls_from_input(input_source) -> List[str]:
    """Read URLs from file or stdin."""
    urls = []

    if input_source == sys.stdin:
        # Reading from stdin
        for line in input_source:
            url = line.strip()
            if url and not url.startswith('#'):
                urls.append(url)
    else:
        # Reading from file
        with open(input_source, 'r') as f:
            for line in f:
                url = line.strip()
                if url and not url.startswith('#'):
                    urls.append(url)

    return urls

def check_url(url: str) -> Tuple[bool, str, str]:
    """
    Check if URL is valid and unique using check_link.py.

    Returns:
        (is_unique, sanitized_url, message)
    """
    try:
        result = subprocess.run(
            ['uv', 'run', 'scripts/check_link.py', url],
            capture_output=True,
            text=True,
            timeout=30
        )

        output = result.stdout

        # Parse check_link.py output
        is_unique = 'UNIQUE' in output or 'Ready to add' in output

        # Extract sanitized URL
        sanitized_url = url
        for line in output.split('\n'):
            if 'Sanitized URL:' in line:
                sanitized_url = line.split('Sanitized URL:')[1].strip()

        return is_unique, sanitized_url, output

    except subprocess.TimeoutExpired:
        return False, url, "ERROR: Timeout checking URL"
    except Exception as e:
        return False, url, f"ERROR: {str(e)}"

def get_next_id(sources_file: Path) -> int:
    """Get the next available ID from sources.md."""
    if not sources_file.exists():
        return 1

    max_id = 0
    with open(sources_file, 'r') as f:
        for line in f:
            # Match lines like: - [ ] 001. https://...
            match = re.match(r'-\s*\[.\]\s*(\d+)\.', line.strip())
            if match:
                id_num = int(match.group(1))
                max_id = max(max_id, id_num)

    return max_id + 1

def add_url_to_sources(sources_file: Path, url: str, url_id: int) -> bool:
    """Add URL to sources.md with proper formatting."""
    try:
        # Read current content
        if sources_file.exists():
            with open(sources_file, 'r') as f:
                content = f.read()
        else:
            content = "# Sources for Journal\n\n## Main List\n\n"

        # Format the new entry
        new_entry = f"- [ ] {url_id:03d}. {url}\n"

        # Find the Main List section and add after it
        if "## Main List" in content:
            parts = content.split("## Main List", 1)
            # Insert after the header, preserving any existing content
            updated_content = parts[0] + "## Main List\n\n" + new_entry + parts[1].lstrip()
        else:
            # Append to end if Main List section doesn't exist
            updated_content = content + f"\n## Main List\n\n{new_entry}"

        # Write back
        with open(sources_file, 'w') as f:
            f.write(updated_content)

        return True
    except Exception as e:
        print(f"ERROR adding to sources.md: {e}")
        return False

def generate_summary(url: str, url_id: int, summaries_dir: Path) -> Tuple[bool, str]:
    """Generate summary for URL."""
    try:
        # Create filename from URL
        from urllib.parse import urlparse
        parsed = urlparse(url)
        domain = parsed.netloc.replace('www.', '').replace('.', '_')

        # Simple filename: ID_domain.md
        filename = f"{url_id:03d}_{domain}.md"
        output_path = summaries_dir / filename

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

def mark_as_processed(sources_file: Path, url_id: int) -> bool:
    """Mark URL as processed in sources.md."""
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
        print(f"ERROR marking as processed: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description='Bulk add links and generate summaries for Gen AI journal'
    )
    parser.add_argument(
        'input',
        nargs='?',
        help='File containing URLs (one per line), or read from stdin if not provided'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Check URLs without adding them'
    )
    parser.add_argument(
        '--no-summarize',
        action='store_true',
        help='Add URLs but skip summary generation'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )

    args = parser.parse_args()

    # Determine input source
    if args.input:
        input_source = args.input
    elif not sys.stdin.isatty():
        input_source = sys.stdin
    else:
        print("ERROR: No input provided. Provide a file or pipe URLs to stdin.")
        parser.print_help()
        sys.exit(1)

    # Setup paths
    base_dir = Path(__file__).parent.parent
    sources_file = base_dir / 'workdesk' / 'sources.md'
    summaries_dir = base_dir / 'workdesk' / 'summaries'
    summaries_dir.mkdir(exist_ok=True, parents=True)

    # Read URLs
    print("Reading URLs...")
    urls = read_urls_from_input(input_source)
    print(f"Found {len(urls)} URLs to process\n")

    if not urls:
        print("No URLs found.")
        sys.exit(0)

    # Process URLs
    results: Dict[str, dict] = {}
    next_id = get_next_id(sources_file)

    print("=" * 60)
    print("PHASE 1: Validating URLs")
    print("=" * 60)

    for url in urls:
        print(f"\nChecking: {url}")
        is_unique, sanitized_url, message = check_url(url)

        if args.verbose:
            print(message)

        if is_unique:
            results[url] = {
                'unique': True,
                'sanitized': sanitized_url,
                'id': next_id,
                'added': False,
                'summarized': False,
                'marked': False
            }
            print(f"✓ UNIQUE - Will add as ID {next_id:03d}")
            next_id += 1
        else:
            results[url] = {
                'unique': False,
                'sanitized': sanitized_url,
                'message': message
            }
            print(f"✗ DUPLICATE or ERROR")

    # Count unique URLs
    unique_urls = [url for url, data in results.items() if data.get('unique', False)]
    print(f"\n{len(unique_urls)} unique URLs to add")

    if args.dry_run:
        print("\nDRY RUN - No changes made")
        sys.exit(0)

    if not unique_urls:
        print("\nNo URLs to add.")
        sys.exit(0)

    # Add URLs to sources.md
    print("\n" + "=" * 60)
    print("PHASE 2: Adding to sources.md")
    print("=" * 60)

    for url in unique_urls:
        data = results[url]
        print(f"\n[{data['id']:03d}] Adding: {data['sanitized']}")

        if add_url_to_sources(sources_file, data['sanitized'], data['id']):
            data['added'] = True
            print(f"✓ Added to sources.md")
        else:
            print(f"✗ Failed to add")

    # Generate summaries
    if not args.no_summarize:
        print("\n" + "=" * 60)
        print("PHASE 3: Generating summaries")
        print("=" * 60)

        for url in unique_urls:
            data = results[url]
            if not data['added']:
                continue

            print(f"\n[{data['id']:03d}] Generating summary: {data['sanitized']}")
            success, result = generate_summary(data['sanitized'], data['id'], summaries_dir)

            if success:
                data['summarized'] = True
                print(f"✓ Summary saved: {result}")

                # Mark as processed
                if mark_as_processed(sources_file, data['id']):
                    data['marked'] = True
                    print(f"✓ Marked as processed")
            else:
                print(f"✗ Failed: {result}")

    # Final summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    total = len(urls)
    unique = len(unique_urls)
    duplicates = total - unique
    added = sum(1 for data in results.values() if data.get('added', False))
    summarized = sum(1 for data in results.values() if data.get('summarized', False))

    print(f"Total URLs processed: {total}")
    print(f"Unique URLs: {unique}")
    print(f"Duplicates skipped: {duplicates}")
    print(f"Added to sources.md: {added}")

    if not args.no_summarize:
        print(f"Summaries generated: {summarized}")
        print(f"Marked as processed: {summarized}")

    print("\nDone! ✓")

if __name__ == '__main__':
    main()
