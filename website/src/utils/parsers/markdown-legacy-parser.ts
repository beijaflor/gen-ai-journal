/**
 * Markdown Legacy Parser
 *
 * Parses traditional markdown summaries with regex-based metadata extraction.
 * This is the existing parsing logic extracted into a dedicated parser class.
 */

import type { SummaryParser, SummaryFormat } from '../summary-parser';
import type { SummaryEntry } from '../content-parser';
import { readFileSync } from 'node:fs';

export class MarkdownLegacyParser implements SummaryParser {
  readonly format: SummaryFormat = 'markdown-legacy';

  /**
   * Parse markdown summary using regex extraction
   *
   * This is the original parseSummaryFile logic from content-parser.ts
   */
  parse(filePath: string, journalDate: string, content?: string): SummaryEntry | null {
    try {
      // Read content if not provided
      const markdownContent = content || readFileSync(filePath, 'utf-8');

      const filename = filePath.split('/').pop() || '';
      const parsedFilename = this.parseSummaryFilename(filename);

      if (!parsedFilename) {
        return null;
      }

      const title = this.extractTitleFromMarkdown(markdownContent);
      const wordCount = this.countWords(markdownContent);
      const readingTime = this.calculateReadingTime(wordCount);
      const excerpt = this.extractExcerpt(markdownContent, 150);
      const slug = this.generateSlug(title);
      const language = this.extractLanguage(markdownContent);
      const originalTitle = this.extractOriginalTitle(markdownContent);

      return {
        id: parsedFilename.id,
        date: journalDate,
        filename,
        sourceUrl: parsedFilename.url,
        domain: parsedFilename.domain,
        title,
        content: markdownContent,
        status: 'omitted', // Will be determined later by parent parser
        slug,
        wordCount,
        readingTime,
        excerpt,
        language,
        originalTitle,
      };
    } catch (error) {
      console.error(`Failed to parse markdown summary ${filePath}:`, error);
      return null;
    }
  }

  /**
   * Parse filename to extract metadata (legacy format)
   */
  private parseSummaryFilename(filename: string): {
    id: string;
    domain: string;
    path: string;
    url: string;
  } | null {
    try {
      // Remove .md extension
      const nameWithoutExt = filename.replace(/\.md$/, '');

      // Try new format first: 001_domain_com_path.md
      const newFormatMatch = nameWithoutExt.match(/^(\d{3})_(.+)$/);
      if (newFormatMatch) {
        const [, id, urlPart] = newFormatMatch;

        // Parse domain and path
        const parts = urlPart.split('_');
        if (parts.length < 1) {
          return null;
        }

        const domain = parts[0].replace(/_/g, '.');
        const path = parts.slice(1).join('/');

        // Reconstruct URL
        const url = `https://${domain}${path ? `/${path}` : ''}`;

        return { id, domain, path, url };
      }

      // Try old format: domain_com_path.md (without numeric prefix)
      const parts = nameWithoutExt.split('_');
      if (parts.length < 1) {
        return null;
      }

      const domain = parts[0].replace(/_/g, '.');
      const path = parts.slice(1).join('/');

      // Generate a hash-based ID for consistent ordering
      let hash = 0;
      for (let i = 0; i < nameWithoutExt.length; i++) {
        hash = ((hash << 5) - hash + nameWithoutExt.charCodeAt(i)) & 0xffffff;
      }
      const id = String(Math.abs(hash % 1000)).padStart(3, '0');

      // Reconstruct URL
      const url = `https://${domain}${path ? `/${path}` : ''}`;

      return { id, domain, path, url };
    } catch (error) {
      console.error(`Failed to parse summary filename ${filename}:`, error);
      return null;
    }
  }

  /**
   * Extract title from markdown content
   */
  private extractTitleFromMarkdown(content: string): string {
    // Try to find first heading
    const titleMatch = content.match(/^#\s+(.+)$/m);
    if (titleMatch) {
      return titleMatch[1].trim();
    }

    // Fallback to first non-empty line
    const lines = content.split('\n');
    for (const line of lines) {
      const trimmed = line.trim();
      if (trimmed && !trimmed.startsWith('---')) {
        return trimmed.substring(0, 100); // Limit length
      }
    }

    return 'Untitled';
  }

  /**
   * Extract excerpt from markdown content
   */
  private extractExcerpt(content: string, maxLength: number = 200): string {
    // Remove markdown headers and get first paragraph
    const withoutHeaders = content.replace(/^#{1,6}\s+.+$/gm, '');
    const paragraphs = withoutHeaders.split('\n\n');

    for (const paragraph of paragraphs) {
      const trimmed = paragraph.trim();
      if (trimmed && trimmed.length > 10) {
        return trimmed.length > maxLength ? `${trimmed.substring(0, maxLength)}...` : trimmed;
      }
    }

    return `${content.substring(0, maxLength)}...`;
  }

  /**
   * Count words (Japanese + English)
   */
  private countWords(text: string): number {
    // Count both Japanese characters and English words
    const japaneseChars = (text.match(/[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]/g) || []).length;
    const englishWords = (text.match(/\b[A-Za-z]+\b/g) || []).length;

    // Approximate: 1 Japanese character ≈ 0.5 words
    return Math.round(japaneseChars * 0.5 + englishWords);
  }

  /**
   * Calculate reading time
   */
  private calculateReadingTime(wordCount: number): number {
    // 200 words per minute for mixed Japanese/English content
    return Math.max(1, Math.ceil(wordCount / 200));
  }

  /**
   * Generate slug from title
   */
  private generateSlug(title: string): string {
    return title
      .toLowerCase()
      .replace(/[^\w\s\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF-]/g, '')
      .replace(/\s+/g, '-')
      .replace(/-+/g, '-')
      .substring(0, 50)
      .trim();
  }

  /**
   * Extract language metadata from markdown
   */
  private extractLanguage(content: string): 'ja' | 'en' | 'other' | undefined {
    const match = content.match(/\*\*Language\*\*:\s*(ja|en|other)/);
    return match ? (match[1] as 'ja' | 'en' | 'other') : undefined;
  }

  /**
   * Extract original title from markdown
   */
  private extractOriginalTitle(content: string): string | undefined {
    const match = content.match(/\*\*Original Title\*\*:\s*(.+)$/m);
    return match ? match[1].trim() : undefined;
  }
}
