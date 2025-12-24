#!/usr/bin/env python3
"""
Batch process all unchecked URLs in sources.md to generate summaries.
"""
import re
import subprocess
import sys
import time
from pathlib import Path

def parse_sources(sources_file):
    """Parse sources.md and return unchecked entries."""
    unchecked = []
    with open(sources_file, 'r') as f:
        for line in f:
            match = re.match(r'-\s*\[\s*\]\s*(\d+)\.\s*(.+)', line.strip())
            if match:
                id_num, url = match.groups()
                unchecked.append((id_num.zfill(3), url))
    return unchecked

def generate_summary(id_num, url, output_dir, enable_cache=False):
    """Generate summary for a single URL."""
    output_file = output_dir / f"{id_num}_temp.md"
    print(f"Processing {id_num}: {url}")

    try:
        cmd = ['uv', 'run', 'scripts/call-gemini.py', '--url', url, '--output', str(output_file)]
        if enable_cache:
            cmd.append('--enable-context-cache')

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120
        )

        if result.returncode == 0:
            print(f"✓ Completed {id_num}")
            return True
        else:
            print(f"✗ Failed {id_num}: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print(f"✗ Timeout {id_num}")
        return False
    except Exception as e:
        print(f"✗ Error {id_num}: {e}")
        return False

def mark_as_processed(sources_file, id_num):
    """Mark an entry as processed in sources.md."""
    with open(sources_file, 'r') as f:
        content = f.read()

    # Convert - [ ] to - [x] for this ID
    pattern = rf'-\s*\[\s*\]\s*{int(id_num)}\.'
    replacement = f'- [x] {int(id_num)}.'
    content = re.sub(pattern, replacement, content)

    with open(sources_file, 'w') as f:
        f.write(content)

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Batch process summaries for unchecked URLs')
    parser.add_argument('--enable-cache', action='store_true', default=True,
                       help='Enable explicit context caching for cost savings (enabled by default)')
    parser.add_argument('--disable-cache', action='store_true',
                       help='Disable explicit context caching')
    args = parser.parse_args()

    base_dir = Path(__file__).parent.parent
    sources_file = base_dir / 'workdesk' / 'sources.md'
    summaries_dir = base_dir / 'workdesk' / 'summaries'

    summaries_dir.mkdir(exist_ok=True)

    unchecked = parse_sources(sources_file)
    total = len(unchecked)

    # Determine if caching should be enabled
    enable_caching = args.enable_cache and not args.disable_cache

    cache_status = "WITH context caching" if enable_caching else "WITHOUT context caching"
    print(f"Found {total} unchecked URLs to process ({cache_status})\n")

    success_count = 0
    fail_count = 0

    for i, (id_num, url) in enumerate(unchecked, 1):
        print(f"[{i}/{total}] ", end='')

        if generate_summary(id_num, url, summaries_dir, enable_cache=enable_caching):
            mark_as_processed(sources_file, id_num)
            success_count += 1
        else:
            fail_count += 1

        # Rate limiting
        if i < total:
            time.sleep(2)

    print(f"\n{'='*60}")
    print(f"Processing complete!")
    print(f"Success: {success_count}")
    print(f"Failed: {fail_count}")
    print(f"Total: {total}")

if __name__ == '__main__':
    main()
