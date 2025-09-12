/**
 * Utility functions for formatting domain names for display
 */

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
    const hostname = urlObj.hostname.toLowerCase();
    const pathname = urlObj.pathname;

    // Special handling for zenn.dev and qiita.com
    if (hostname === 'zenn.dev' || hostname === 'www.zenn.dev') {
      // Extract first path segment: /hoge/muge → /hoge
      const pathSegments = pathname.split('/').filter(segment => segment.length > 0);
      if (pathSegments.length > 0) {
        return `zenn.dev/${pathSegments[0]}`;
      }
      return 'zenn.dev';
    }

    if (hostname === 'qiita.com' || hostname === 'www.qiita.com') {
      // Extract first path segment: /user/articles/123 → /user
      const pathSegments = pathname.split('/').filter(segment => segment.length > 0);
      if (pathSegments.length > 0) {
        return `qiita.com/${pathSegments[0]}`;
      }
      return 'qiita.com';
    }

    // General case: remove www prefix and return clean domain
    return hostname.replace(/^www\./, '');
    
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