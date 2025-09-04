// Utility to handle base path for GitHub Pages deployment

/**
 * Creates a URL with the proper base path for deployment
 * @param path - The path to append to the base (should start with /)
 * @returns The full path with base path included
 */
export function withBase(path: string): string {
  // In Astro, we can access the base URL via import.meta.env.BASE_URL
  const base = import.meta.env.BASE_URL || '/';

  // If path already starts with the base, return as is
  if (path.startsWith(base)) {
    return path;
  }

  // If path is just '/', use base directly but ensure it ends with /
  if (path === '/') {
    return base.endsWith('/') ? base : `${base}/`;
  }

  // Ensure proper path concatenation
  const cleanBase = base.endsWith('/') ? base.slice(0, -1) : base;
  const cleanPath = path.startsWith('/') ? path : `/${path}`;

  return `${cleanBase}${cleanPath}`;
}
