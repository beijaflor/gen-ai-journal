/**
 * Utility functions for formatting domain names for display
 */

/**
 * Domains where the first path segment identifies the author/org,
 * displayed as e.g. zenn.dev/username instead of the bare domain.
 */
const FIRST_PATH_SEGMENT_DOMAINS = new Set([
  'zenn.dev',
  'qiita.com',
  'github.com',
  'note.com',
  'sizu.me',
]);

/**
 * Formats a URL's domain for display with special handling for certain domains
 * @param url - The full URL or domain string
 * @returns Formatted domain string for display
 */
export function formatDomainDisplay(url: string): string {
  try {
    // Handle both full URLs and domain-only strings
    let urlToProcess: string;

    if (url.startsWith('http://') || url.startsWith('https://')) {
      urlToProcess = url;
    } else {
      // If it's just a domain, add https:// for URL parsing
      urlToProcess = `https://${url}`;
    }

    const urlObj = new URL(urlToProcess);
    const hostname = urlObj.hostname.toLowerCase().replace(/^www\./, '');

    if (FIRST_PATH_SEGMENT_DOMAINS.has(hostname)) {
      const firstSegment = urlObj.pathname
        .split('/')
        .find(segment => segment.length > 0);
      if (firstSegment) {
        return `${hostname}/${firstSegment}`;
      }
    }

    return hostname;
  } catch (error) {
    // Fallback: if URL parsing fails, try to clean up the input string
    console.warn(`Failed to parse URL for domain display: ${url}`, error);

    // Remove common prefixes and protocols as fallback
    const cleaned = url
      .replace(/^https?:\/\//, '')
      .replace(/^www\./, '')
      .split('/')[0]; // Take only the domain part

    return cleaned || url;
  }
}

/**
 * Extract domain from a URL for storage/comparison purposes
 * @param url - The full URL
 * @returns Domain string (without special formatting)
 */
export function extractDomain(url: string): string {
  try {
    const urlObj = new URL(url);
    return urlObj.hostname.replace(/^www\./, '');
  } catch (error) {
    console.warn(`Failed to extract domain from URL: ${url}`, error);

    // Fallback: extract domain from string
    const cleaned = url
      .replace(/^https?:\/\//, '')
      .replace(/^www\./, '')
      .split('/')[0];

    return cleaned || url;
  }
}
