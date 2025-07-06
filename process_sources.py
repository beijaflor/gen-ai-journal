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
    """Reads links from a file, sanitizes them, removes duplicates, and writes back."""
    with open(file_path, 'r') as f:
        content = f.read()

    lines = content.splitlines()
    processed_lines = []
    seen_sanitized_urls = set()
    
    for line in lines:
        # Corrected regex to correctly capture the URL by using non-greedy match
        match = re.match(r'^(- \[([ x])\]\s*)(https?://.*)', line)
        if match:
            prefix = match.group(1)
            original_url = match.group(3).strip() # This should now correctly capture the URL
            sanitized_url = sanitize_url(original_url)
            
            if sanitized_url not in seen_sanitized_urls:
                seen_sanitized_urls.add(sanitized_url)
                processed_lines.append(f"{prefix}{sanitized_url}")
        else:
            processed_lines.append(line) # Keep non-link lines as is

    new_content = "\n".join(processed_lines)

    with open(file_path, 'w') as f:
        f.write(new_content)
    
    print(f"Processed and updated: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_sources.py <path_to_sources_md>")
        sys.exit(1)
    
    sources_file = sys.argv[1]
    process_sources_file(sources_file)
