import re
import sys
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode

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

def process_sources_file(file_path):
    """Reads links from a structured file, sanitizes them, removes duplicates, assigns IDs, and writes back."""
    with open(file_path, 'r') as f:
        content = f.read()

    lines = content.splitlines()
    processed_lines = []
    seen_sanitized_urls = set()
    link_counter = 1
    
    for line in lines:
        # Check if line is a section header (starts with ##)
        if line.strip().startswith('##'):
            processed_lines.append(line)
            continue
            
        # Check for numbered checkbox links: - [ ] 001. https://...
        numbered_match = re.match(r'^(- \[([ x])\]\s*)(\d+\.\s*)(https?://.*)', line)
        if numbered_match:
            checkbox_prefix = numbered_match.group(1)
            original_url = numbered_match.group(4).strip()
            sanitized_url = sanitize_url(original_url)
            
            if sanitized_url not in seen_sanitized_urls:
                seen_sanitized_urls.add(sanitized_url)
                # Assign new sequential ID
                new_id = f"{link_counter:03d}."
                processed_lines.append(f"{checkbox_prefix}{new_id} {sanitized_url}")
                link_counter += 1
            continue
            
        # Check for unnumbered checkbox links: - [ ] https://...
        unnumbered_match = re.match(r'^(- \[([ x])\]\s*)(https?://.*)', line)
        if unnumbered_match:
            checkbox_prefix = unnumbered_match.group(1)
            original_url = unnumbered_match.group(3).strip()
            sanitized_url = sanitize_url(original_url)
            
            if sanitized_url not in seen_sanitized_urls:
                seen_sanitized_urls.add(sanitized_url)
                # Assign new sequential ID
                new_id = f"{link_counter:03d}."
                processed_lines.append(f"{checkbox_prefix}{new_id} {sanitized_url}")
                link_counter += 1
            continue
            
        # Keep non-link lines as is (empty lines, other content)
        processed_lines.append(line)

    new_content = "\n".join(processed_lines)

    with open(file_path, 'w') as f:
        f.write(new_content)
    
    print(f"Processed and updated: {file_path}")
    print(f"Assigned IDs to {link_counter - 1} unique links")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_sources.py <path_to_sources_md>")
        sys.exit(1)
    
    sources_file = sys.argv[1]
    process_sources_file(sources_file)
