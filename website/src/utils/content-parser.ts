import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

// Base types for journal content
export interface JournalEntry {
  date: string; // YYYY-MM-DD
  type: 'main' | 'annex'; // Journal type
  title: string; // Extracted from markdown
  content: string; // Full markdown content
  slug: string; // URL slug
  wordCount: number; // Word count
  readingTime: number; // Minutes
  excerpt: string; // First paragraph or summary
  summaryCount: number; // Associated summaries count
  metadata: {
    publishedAt: Date;
    tags?: string[];
  };
}

export interface SummaryEntry {
  id: string; // 3-digit ID
  date: string; // Parent journal date
  filename: string; // Original filename
  sourceUrl: string; // Reconstructed URL
  domain: string; // Source domain
  title: string; // Extracted title
  content: string; // Markdown content
  status: 'main' | 'annex' | 'omitted'; // Inclusion status
  slug: string; // URL slug
  wordCount: number; // Word count
  readingTime: number; // Minutes
  excerpt: string; // Brief summary
}

export interface JournalArchive {
  date: string; // YYYY-MM-DD
  mainJournal: JournalEntry | null;
  annexJournal: JournalEntry | null;
  summaries: SummaryEntry[];
  stats: {
    totalSummaries: number;
    mainSummaries: number;
    annexSummaries: number;
    omittedSummaries: number;
  };
}

export interface JournalMetadata {
  date: string;
  totalSummaries: number;
  statistics: {
    mainSummaries: number;
    annexSummaries: number;
    omittedSummaries: number;
  };
}

// Utility functions
function extractTitleFromMarkdown(content: string): string {
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

function extractExcerpt(content: string, maxLength: number = 200): string {
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

function countWords(text: string): number {
  // Count both Japanese characters and English words
  const japaneseChars = (text.match(/[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]/g) || []).length;
  const englishWords = (text.match(/\b[A-Za-z]+\b/g) || []).length;

  // Approximate: 1 Japanese character ≈ 0.5 words
  return Math.round(japaneseChars * 0.5 + englishWords);
}

function calculateReadingTime(wordCount: number): number {
  // 200 words per minute for mixed Japanese/English content
  return Math.max(1, Math.ceil(wordCount / 200));
}

function generateSlug(title: string): string {
  return title
    .toLowerCase()
    .replace(/[^\w\s\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .substring(0, 50)
    .trim();
}

// File parsing functions
function parseJournalFile(
  filePath: string,
  type: 'main' | 'annex',
  date: string
): JournalEntry | null {
  try {
    if (!existsSync(filePath)) {
      return null;
    }

    const content = readFileSync(filePath, 'utf-8');
    const title = extractTitleFromMarkdown(content);
    const wordCount = countWords(content);
    const readingTime = calculateReadingTime(wordCount);
    const excerpt = extractExcerpt(content);
    const slug = generateSlug(title);

    return {
      date,
      type,
      title,
      content,
      slug,
      wordCount,
      readingTime,
      excerpt,
      summaryCount: 0, // Will be populated later
      metadata: {
        publishedAt: new Date(date),
        tags: [],
      },
    };
  } catch (error) {
    console.warn(`Failed to parse journal file ${filePath}:`, error);
    return null;
  }
}

function parseSummaryFilename(filename: string): {
  id: string;
  domain: string;
  path: string;
  url: string;
} | null {
  try {
    // Remove .md extension
    const nameWithoutExt = filename.replace(/\.md$/, '');

    // Extract ID (first 3 digits)
    const idMatch = nameWithoutExt.match(/^(\d{3})_(.+)$/);
    if (!idMatch) {
      return null;
    }

    const [, id, urlPart] = idMatch;

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
  } catch (error) {
    console.warn(`Failed to parse summary filename ${filename}:`, error);
    return null;
  }
}

function parseSummaryFile(filePath: string, date: string): SummaryEntry | null {
  try {
    if (!existsSync(filePath)) {
      return null;
    }

    const filename = filePath.split('/').pop() || '';
    const parsedFilename = parseSummaryFilename(filename);

    if (!parsedFilename) {
      return null;
    }

    const content = readFileSync(filePath, 'utf-8');
    const title = extractTitleFromMarkdown(content);
    const wordCount = countWords(content);
    const readingTime = calculateReadingTime(wordCount);
    const excerpt = extractExcerpt(content, 150);
    const slug = generateSlug(title);

    return {
      id: parsedFilename.id,
      date,
      filename,
      sourceUrl: parsedFilename.url,
      domain: parsedFilename.domain,
      title,
      content,
      status: 'omitted', // Will be determined later
      slug,
      wordCount,
      readingTime,
      excerpt,
    };
  } catch (error) {
    console.warn(`Failed to parse summary file ${filePath}:`, error);
    return null;
  }
}

// Metadata loading functions
function loadJournalMetadata(journalDir: string): JournalMetadata {
  const metadataPath = join(journalDir, 'journal-metadata.json');
  
  if (!existsSync(metadataPath)) {
    throw new Error(`Missing required journal-metadata.json in ${journalDir}`);
  }

  try {
    const metadataContent = readFileSync(metadataPath, 'utf-8');
    const metadata: JournalMetadata = JSON.parse(metadataContent);
    
    // Validate metadata structure
    if (!metadata.date || !metadata.statistics) {
      throw new Error(`Invalid metadata structure in ${metadataPath}`);
    }
    
    return metadata;
  } catch (error) {
    throw new Error(`Failed to parse metadata from ${metadataPath}: ${error}`);
  }
}

// Main parsing functions
export function getJournalsPath(): string {
  // Point to the journals directory in the current repository
  return join(process.cwd(), '../journals');
}

export function getAllJournalDates(): string[] {
  const journalsPath = getJournalsPath();

  try {
    if (!existsSync(journalsPath)) {
      console.warn(`Journals directory not found: ${journalsPath}`);
      return [];
    }

    const entries = readdirSync(journalsPath);

    return entries
      .filter((entry) => {
        const fullPath = join(journalsPath, entry);
        return statSync(fullPath).isDirectory() && /^\d{4}-\d{2}-\d{2}$/.test(entry);
      })
      .sort()
      .reverse(); // Latest first
  } catch (error) {
    console.warn('Failed to read journals directory:', error);
    return [];
  }
}

export function parseJournalByDate(date: string): JournalArchive | null {
  const journalsPath = getJournalsPath();
  const journalDir = join(journalsPath, date);

  if (!existsSync(journalDir)) {
    return null;
  }

  try {
    // Load required metadata
    const metadata = loadJournalMetadata(journalDir);

    // Try both naming conventions for main journal
    const dateFormatted = date.replace(/-/g, '_');
    let mainJournal = parseJournalFile(
      join(journalDir, `00_weekly_journal_${dateFormatted}.md`),
      'main',
      date
    );

    // Fallback to older naming convention if not found
    if (!mainJournal) {
      mainJournal = parseJournalFile(
        join(journalDir, `weekly_journal_${dateFormatted}.md`),
        'main',
        date
      );
    }

    // Try both naming conventions for annex journal
    let annexJournal = parseJournalFile(
      join(journalDir, `01_annex_journal_${dateFormatted}.md`),
      'annex',
      date
    );

    // Fallback to older naming convention if not found
    if (!annexJournal) {
      annexJournal = parseJournalFile(
        join(journalDir, `annex_journal_${dateFormatted}.md`),
        'annex',
        date
      );
    }

    // Parse summaries (but assign status based on metadata)
    const summariesDir = join(journalDir, 'summaries');
    let summaries: SummaryEntry[] = [];

    if (existsSync(summariesDir)) {
      const summaryFiles = readdirSync(summariesDir)
        .filter((file) => file.endsWith('.md'))
        .sort();

      summaries = summaryFiles
        .map((file, index) => {
          const summary = parseSummaryFile(join(summariesDir, file), date);
          if (summary) {
            // Assign status based on metadata counts and order
            if (index < metadata.statistics.mainSummaries) {
              summary.status = 'main';
            } else if (index < metadata.statistics.mainSummaries + metadata.statistics.annexSummaries) {
              summary.status = 'annex';
            } else {
              summary.status = 'omitted';
            }
          }
          return summary;
        })
        .filter((summary): summary is SummaryEntry => summary !== null);
    }

    // Use metadata statistics directly
    const stats = {
      totalSummaries: metadata.totalSummaries,
      mainSummaries: metadata.statistics.mainSummaries,
      annexSummaries: metadata.statistics.annexSummaries,
      omittedSummaries: metadata.statistics.omittedSummaries,
    };

    // Update summary counts in journals
    if (mainJournal) {
      mainJournal.summaryCount = stats.totalSummaries;
    }
    if (annexJournal) {
      annexJournal.summaryCount = stats.totalSummaries;
    }

    return {
      date,
      mainJournal,
      annexJournal,
      summaries,
      stats,
    };
  } catch (error) {
    console.warn(`Failed to parse journal for date ${date}:`, error);
    return null;
  }
}

export function getLatestJournal(): JournalArchive | null {
  const dates = getAllJournalDates();
  if (dates.length === 0) {
    return null;
  }

  return parseJournalByDate(dates[0]);
}

export function getAllJournals(): JournalArchive[] {
  const dates = getAllJournalDates();

  return dates
    .map((date) => parseJournalByDate(date))
    .filter((journal): journal is JournalArchive => journal !== null);
}
