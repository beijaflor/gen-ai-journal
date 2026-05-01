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

    # Use a longer per-URL check timeout (default: 60 seconds)
    uv run scripts/bulk_add_links.py urls.txt --check-timeout 90

    # Retry URLs from the previous run that timed out / errored
    uv run scripts/bulk_add_links.py --retry-failures
"""

import sys
import argparse
import subprocess
import re
import time
from datetime import datetime
from pathlib import Path
from typing import List, Tuple, Dict

# Default per-URL check_link.py subprocess timeout (seconds).
# check_link.py itself uses ~10s HEAD + ~10s GET fallback plus a filesystem
# scan, so anything below ~25s leaves no headroom for slow hosts.
DEFAULT_CHECK_TIMEOUT = 60

# File where URLs that timed out / errored are written for retry.
FAILURES_FILE_RELATIVE = Path('workdesk') / '.bulk_add_failures.txt'

# Failure categories returned by check_url().
CATEGORY_UNIQUE = 'unique'
CATEGORY_DUPLICATE = 'duplicate'
CATEGORY_VALIDATION_ERROR = 'validation_error'
CATEGORY_TIMEOUT = 'timeout'
CATEGORY_ERROR = 'error'

# Substrings that identify a validation rejection from check_link.py
# (localhost / private IP / loopback / link-local).
VALIDATION_ERROR_MARKERS = (
    'localhost URLs are not allowed',
    'Private IP address not allowed',
    'Loopback IP address not allowed',
    'Link-local IP address not allowed',
)


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


def _classify_check_output(returncode: int, output: str) -> str:
    """
    Classify a completed check_link.py invocation into a category.

    Returns one of CATEGORY_UNIQUE / CATEGORY_DUPLICATE /
    CATEGORY_VALIDATION_ERROR / CATEGORY_ERROR.
    """
    lowered = output.lower()

    # Successful unique add: check_link.py prints
    # "✅ URL is unique and ready to be added"
    if 'unique' in lowered and 'ready to be added' in lowered:
        return CATEGORY_UNIQUE

    # Real duplicate: check_link.py prints "URL already exists!" before exit(1)
    if 'url already exists' in lowered:
        return CATEGORY_DUPLICATE

    # Validation rejection (localhost / private IP / etc.) -> exit(1) early
    if any(marker in output for marker in VALIDATION_ERROR_MARKERS):
        return CATEGORY_VALIDATION_ERROR

    # Catch-all: non-zero exit, network failure inside check_link.py, etc.
    return CATEGORY_ERROR


def check_url(
    url: str,
    timeout: int = DEFAULT_CHECK_TIMEOUT,
) -> Tuple[str, str, str]:
    """
    Check if URL is valid and unique using check_link.py.

    On `subprocess.TimeoutExpired`, automatically retries once after a short
    sleep before giving up. This handles transient slow-host hiccups that
    would otherwise be silently bucketed as duplicates.

    Returns:
        (category, sanitized_url, message)

    `category` is one of:
        - 'unique'           -> URL passed validation and dedup
        - 'duplicate'        -> URL already exists in workdesk / journals
        - 'validation_error' -> localhost / private-IP rejection
        - 'timeout'          -> subprocess.TimeoutExpired (after retry)
        - 'error'            -> any other failure
    """
    cmd = ['uv', 'run', 'scripts/check_link.py', url]

    def _run_once() -> Tuple[str, str]:
        """Run check_link.py once. Returns (category, message). May raise TimeoutExpired."""
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        # check_link.py writes everything to stdout; include stderr just in case.
        output = result.stdout + (result.stderr or '')
        return _classify_check_output(result.returncode, output), output

    try:
        category, output = _run_once()
    except subprocess.TimeoutExpired:
        # Auto-retry once on timeout — slow-host failures are often transient.
        time.sleep(2)
        try:
            category, output = _run_once()
        except subprocess.TimeoutExpired:
            return CATEGORY_TIMEOUT, url, f"ERROR: Timeout after {timeout}s (retried once)"
        except Exception as e:
            return CATEGORY_ERROR, url, f"ERROR (on retry): {e}"
    except Exception as e:
        return CATEGORY_ERROR, url, f"ERROR: {e}"

    # Extract sanitized URL from check_link.py stdout when available.
    sanitized_url = url
    for line in output.split('\n'):
        if 'Sanitized URL:' in line:
            sanitized_url = line.split('Sanitized URL:')[1].strip()
            break

    return category, sanitized_url, output


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


def write_failures_file(failures_file: Path, failed_urls: List[str]) -> None:
    """
    Write recoverable failures (timeouts / errors) to disk so they can be
    retried via `--retry-failures`. Real duplicates and validation errors are
    NOT written — those won't succeed on retry.
    """
    failures_file.parent.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(failures_file, 'w') as f:
        f.write(
            f"# bulk_add_links.py failures written at {timestamp}\n"
            f"# Re-run with: uv run scripts/bulk_add_links.py --retry-failures\n"
        )
        for url in failed_urls:
            f.write(f"{url}\n")


def read_failures_file(failures_file: Path) -> List[str]:
    """Read URLs to retry from the failures file (skipping comment lines)."""
    if not failures_file.exists():
        return []
    urls = []
    with open(failures_file, 'r') as f:
        for line in f:
            url = line.strip()
            if url and not url.startswith('#'):
                urls.append(url)
    return urls


def clear_failures_file(failures_file: Path) -> None:
    """Remove the failures file (used after a clean retry run)."""
    try:
        if failures_file.exists():
            failures_file.unlink()
    except Exception as e:
        print(f"WARNING: could not remove {failures_file}: {e}")


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
    parser.add_argument(
        '--check-timeout',
        type=int,
        default=DEFAULT_CHECK_TIMEOUT,
        help=(
            f'Per-URL timeout (seconds) for check_link.py subprocess. '
            f'Default: {DEFAULT_CHECK_TIMEOUT}. check_link.py uses 10s HEAD + '
            f'10s GET fallback, so anything above ~25s is safe.'
        ),
    )
    parser.add_argument(
        '--retry-failures',
        action='store_true',
        help=(
            f'Read URLs from {FAILURES_FILE_RELATIVE} (timeouts/errors from a '
            'previous run) instead of from an input file. Cannot be combined '
            'with a positional input file.'
        ),
    )

    args = parser.parse_args()

    # Setup paths early so we can resolve the failures file regardless of input mode.
    base_dir = Path(__file__).parent.parent
    sources_file = base_dir / 'workdesk' / 'sources.md'
    summaries_dir = base_dir / 'workdesk' / 'summaries'
    summaries_dir.mkdir(exist_ok=True, parents=True)
    failures_file = base_dir / FAILURES_FILE_RELATIVE

    # Determine input source.
    if args.retry_failures:
        if args.input:
            print("ERROR: --retry-failures cannot be combined with an input file.")
            sys.exit(2)
        if not failures_file.exists():
            print(f"ERROR: no failures file found at {failures_file}")
            sys.exit(1)
        print(f"Reading URLs from failures file: {failures_file}")
        urls = read_failures_file(failures_file)
        if not urls:
            print("Failures file is empty — nothing to retry.")
            sys.exit(0)
    else:
        if args.input:
            input_source = args.input
        elif not sys.stdin.isatty():
            input_source = sys.stdin
        else:
            print("ERROR: No input provided. Provide a file or pipe URLs to stdin.")
            parser.print_help()
            sys.exit(1)

        print("Reading URLs...")
        urls = read_urls_from_input(input_source)

    print(f"Found {len(urls)} URLs to process\n")

    if not urls:
        print("No URLs found.")
        sys.exit(0)

    # Process URLs strictly sequentially in input order.
    #
    # Ordering guarantee (see issue #120):
    # - URLs are validated and appended to sources.md one at a time, in the
    #   exact order received from the input.
    # - Duplicates, validation errors, timeouts, and other errors are skipped
    #   WITHOUT consuming an ID.
    # - The next ID is only assigned and incremented after the previous URL
    #   has been committed to sources.md, so assigned IDs strictly increase
    #   in input order.
    #
    # Failure categorization (see issue #126):
    # - Each non-unique outcome is bucketed into one of:
    #     duplicate, validation_error, timeout, error
    # - Recoverable failures (timeouts + errors) are written to
    #   workdesk/.bulk_add_failures.txt so the user can iterate via
    #   `--retry-failures`. Duplicates and validation errors are NOT written,
    #   since they will not succeed on retry.
    results: Dict[str, dict] = {}
    next_id = get_next_id(sources_file)

    print("=" * 60)
    print("Processing URLs (sequential, input order preserved)")
    print("=" * 60)

    for url in urls:
        print(f"\nChecking: {url}")
        category, sanitized_url, message = check_url(url, timeout=args.check_timeout)

        if args.verbose:
            print(message)

        if category != CATEGORY_UNIQUE:
            results[url] = {
                'unique': False,
                'category': category,
                'sanitized': sanitized_url,
                'message': message,
            }
            if category == CATEGORY_DUPLICATE:
                print("✗ DUPLICATE (already in workdesk or prior journal — no ID consumed)")
            elif category == CATEGORY_VALIDATION_ERROR:
                print("✗ VALIDATION_ERROR (localhost / private IP — no ID consumed)")
            elif category == CATEGORY_TIMEOUT:
                print(
                    f"✗ TIMEOUT (will be written to {FAILURES_FILE_RELATIVE} — no ID consumed)"
                )
            else:  # CATEGORY_ERROR
                print(
                    f"✗ ERROR (will be written to {FAILURES_FILE_RELATIVE} — no ID consumed)"
                )
            continue

        # URL is unique. Reserve the next ID and append immediately so that
        # subsequent URLs see this entry when computing duplicates / next ID.
        assigned_id = next_id
        data = {
            'unique': True,
            'category': CATEGORY_UNIQUE,
            'sanitized': sanitized_url,
            'id': assigned_id,
            'added': False,
            'summarized': False,
            'marked': False,
        }
        results[url] = data
        print(f"✓ UNIQUE - Assigning ID {assigned_id:03d}")

        if args.dry_run:
            # In dry-run we still increment so the printed sequence reflects
            # the IDs that WOULD be assigned, in input order.
            next_id += 1
            continue

        if add_url_to_sources(sources_file, sanitized_url, assigned_id):
            data['added'] = True
            next_id += 1
            print(f"✓ Added to sources.md as {assigned_id:03d}")
        else:
            print(f"✗ Failed to add to sources.md (ID {assigned_id:03d} not consumed)")
            # Do NOT increment next_id: the append failed, so the ID is free
            # for the next URL. This preserves the contiguous ordering
            # guarantee for IDs that actually land in sources.md.
            # Treat this as an error so the URL ends up in the retry file.
            data['unique'] = False
            data['category'] = CATEGORY_ERROR
            continue

        # Generate summary inline (still sequential per URL) unless suppressed.
        if not args.no_summarize:
            print(f"[{assigned_id:03d}] Generating summary: {sanitized_url}")
            success, result = generate_summary(sanitized_url, assigned_id, summaries_dir)

            if success:
                data['summarized'] = True
                print(f"✓ Summary saved: {result}")

                if mark_as_processed(sources_file, assigned_id):
                    data['marked'] = True
                    print(f"✓ Marked as processed")
            else:
                print(f"✗ Failed: {result}")

    # Tally results by category.
    total = len(urls)
    unique_urls = [u for u, d in results.items() if d.get('category') == CATEGORY_UNIQUE]
    duplicates = [u for u, d in results.items() if d.get('category') == CATEGORY_DUPLICATE]
    validation_errors = [
        u for u, d in results.items() if d.get('category') == CATEGORY_VALIDATION_ERROR
    ]
    timeouts = [u for u, d in results.items() if d.get('category') == CATEGORY_TIMEOUT]
    errors = [u for u, d in results.items() if d.get('category') == CATEGORY_ERROR]

    recoverable_failures = timeouts + errors

    print(f"\n{len(unique_urls)} unique URLs to add")

    # Persist (or clear) the failures file. Dry-run never mutates the file.
    if not args.dry_run:
        if args.retry_failures:
            # Retry runs always rewrite so the file reflects the latest state:
            # URLs that succeeded are dropped, ones that still fail remain.
            if recoverable_failures:
                write_failures_file(failures_file, recoverable_failures)
            else:
                clear_failures_file(failures_file)
        elif recoverable_failures:
            # Normal run: only write the file when there ARE recoverable failures.
            write_failures_file(failures_file, recoverable_failures)

    if args.dry_run:
        print("\nDRY RUN - No changes made")
        sys.exit(0)

    added = sum(1 for data in results.values() if data.get('added', False))
    summarized = sum(1 for data in results.values() if data.get('summarized', False))

    # Final summary.
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Total URLs processed:  {total:>4}")
    print(f"Unique URLs added:     {added:>4}")
    print(f"Real duplicates:       {len(duplicates):>4}    (already in prior journal)")
    print(f"Validation failures:   {len(validation_errors):>4}")
    if recoverable_failures:
        print(
            f"Timeouts / errors:     {len(recoverable_failures):>4}"
            f"    (RETRY THESE — see {FAILURES_FILE_RELATIVE})"
        )
        print(
            f"  - timeouts: {len(timeouts)}, other errors: {len(errors)}"
        )
    else:
        print(f"Timeouts / errors:     {0:>4}")

    if not args.no_summarize:
        print(f"Summaries generated:   {summarized:>4}")
        print(f"Marked as processed:   {summarized:>4}")

    print("\nDone! ✓")


if __name__ == '__main__':
    main()
