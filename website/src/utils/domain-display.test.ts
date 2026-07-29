import { describe, expect, it } from 'vitest';
import { extractDomain, formatDomainDisplay } from './domain-display';

describe('formatDomainDisplay', () => {
  describe('domains that show the first path segment', () => {
    it.each([
      ['https://zenn.dev/karaage0703/articles/abc123', 'zenn.dev/karaage0703'],
      ['https://qiita.com/user1/items/xyz789', 'qiita.com/user1'],
      ['https://github.com/anthropics/claude-code', 'github.com/anthropics'],
      ['https://note.com/writer/n/n1234567890ab', 'note.com/writer'],
      ['https://sizu.me/someone/posts/xyz123', 'sizu.me/someone'],
    ])('%s → %s', (url, expected) => {
      expect(formatDomainDisplay(url)).toBe(expected);
    });

    it.each([
      ['https://www.zenn.dev/user/articles/abc', 'zenn.dev/user'],
      ['https://www.github.com/org/repo', 'github.com/org'],
      ['https://www.sizu.me/someone', 'sizu.me/someone'],
    ])('strips www prefix: %s → %s', (url, expected) => {
      expect(formatDomainDisplay(url)).toBe(expected);
    });

    it.each([
      ['https://zenn.dev/', 'zenn.dev'],
      ['https://qiita.com', 'qiita.com'],
      ['https://github.com/', 'github.com'],
      ['https://note.com', 'note.com'],
      ['https://sizu.me/', 'sizu.me'],
    ])('falls back to bare domain without a path: %s → %s', (url, expected) => {
      expect(formatDomainDisplay(url)).toBe(expected);
    });

    it('keeps only the first segment of deep paths', () => {
      expect(formatDomainDisplay('https://github.com/a/b/c/d/e')).toBe('github.com/a');
    });

    it('does not apply to subdomains of listed domains', () => {
      expect(formatDomainDisplay('https://gist.github.com/user/abc')).toBe('gist.github.com');
    });
  });

  describe('general domains', () => {
    it('returns the bare domain and ignores the path', () => {
      expect(formatDomainDisplay('https://example.com/some/deep/path')).toBe('example.com');
    });

    it('strips the www prefix', () => {
      expect(formatDomainDisplay('https://www.example.com/page')).toBe('example.com');
    });

    it('lowercases the hostname', () => {
      expect(formatDomainDisplay('https://EXAMPLE.COM/Page')).toBe('example.com');
    });

    it('accepts http URLs', () => {
      expect(formatDomainDisplay('http://example.com/page')).toBe('example.com');
    });
  });

  describe('domain-only input (no protocol)', () => {
    it('handles a bare domain', () => {
      expect(formatDomainDisplay('example.com')).toBe('example.com');
    });

    it('handles a bare special domain with a path', () => {
      expect(formatDomainDisplay('zenn.dev/user/articles/abc')).toBe('zenn.dev/user');
    });
  });

  describe('unparseable input', () => {
    it('falls back to cleaning up the string', () => {
      expect(formatDomainDisplay('https://')).toBe('https://');
    });
  });
});

describe('extractDomain', () => {
  it('extracts the hostname without www', () => {
    expect(extractDomain('https://www.example.com/some/path')).toBe('example.com');
  });

  it('keeps the full hostname for special domains (no path segment)', () => {
    expect(extractDomain('https://zenn.dev/user/articles/abc')).toBe('zenn.dev');
  });

  it('falls back to string cleanup for unparseable input', () => {
    expect(extractDomain('not a url')).toBe('not a url');
  });
});
