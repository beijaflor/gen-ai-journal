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
  fullExcerpt?: string; // Full first paragraph (no truncation)
  language?: 'ja' | 'en' | 'other'; // Source language
  originalTitle?: string; // Original title (for non-Japanese articles)
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

export interface JournalParsingConfig {
  titleOverride?: {
    main?: string;
    annex?: string;
  };
  excerptOverride?: {
    main?: string;
    annex?: string;
  };
  contentStructure?: {
    titlePattern?: string; // Custom regex pattern for title extraction
    excerptSection?: string; // Specific section to use for excerpt
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
  parsing?: JournalParsingConfig; // Optional parsing configuration
}

// Utility functions
function extractTitleFromMarkdown(
  content: string, 
  config?: JournalParsingConfig,
  journalType?: 'main' | 'annex'
): string {
  // Check for override first
  if (config?.titleOverride && journalType) {
    const override = config.titleOverride[journalType];
    if (override) {
      return override;
    }
  }

  // Use custom pattern if specified
  if (config?.contentStructure?.titlePattern) {
    const customMatch = content.match(new RegExp(config.contentStructure.titlePattern, 'm'));
    if (customMatch?.[1]) {
      return customMatch[1].trim();
    }
  }

  // Default: try to find first heading
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

function extractExcerpt(
  content: string,
  maxLength: number = 200,
  config?: JournalParsingConfig,
  journalType?: 'main' | 'annex'
): string {
  // Check for override first
  if (config?.excerptOverride && journalType) {
    const override = config.excerptOverride[journalType];
    if (override) {
      return override;
    }
  }

  // Use specific section if specified
  if (config?.contentStructure?.excerptSection) {
    const sectionMatch = content.match(
      new RegExp(`#{1,6}\\s+${config.contentStructure.excerptSection}[\\s\\S]*?\\n([\\s\\S]*?)(?=\\n#{1,6}|$)`, 'i')
    );
    if (sectionMatch?.[1]) {
      const sectionContent = sectionMatch[1].trim();
      return sectionContent.length > maxLength ? `${sectionContent.substring(0, maxLength)}...` : sectionContent;
    }
  }

  // Default: remove markdown headers and get first paragraph
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

function shouldSkipLine(line: string): boolean {
  const trimmed = line.trim();
  if (!trimmed) return true;
  if (trimmed.startsWith('#')) return true;
  if (trimmed.startsWith('http://') || trimmed.startsWith('https://')) return true;
  // Skip metadata lines like **Content Type**: but not summary lines like **分析する**：
  if (/^\*\*[A-Za-z\s]+\*\*:/.test(trimmed)) return true;
  if (trimmed.startsWith('[[')) return true;
  return false;
}

function extractFullFirstParagraph(content: string): string {
  // Strategy 1: Paragraph-based extraction
  const withoutHeaders = content.replace(/^#{1,6}\s+.+$/gm, '');
  const paragraphs = withoutHeaders.split('\n\n');

  for (const paragraph of paragraphs) {
    const trimmed = paragraph.trim();
    if (trimmed.length < 15) continue;

    const firstLine = trimmed.split('\n')[0];
    if (shouldSkipLine(firstLine)) continue;

    // Accept if contains Japanese or is substantial English
    if (/[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]/.test(trimmed)) {
      return trimmed;
    }
    if (trimmed.length > 30) {
      return trimmed;
    }
  }

  // Strategy 2: Line-by-line fallback
  const lines = content.split('\n');
  const contentLines: string[] = [];

  for (const line of lines) {
    if (shouldSkipLine(line)) continue;

    const trimmed = line.trim();
    if (trimmed.length > 10) {
      contentLines.push(trimmed);
      if (contentLines.join(' ').length > 50) {
        return contentLines.join(' ');
      }
    }
  }

  return contentLines.join(' ') || '';
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

function extractLanguage(content: string): 'ja' | 'en' | 'other' | undefined {
  const match = content.match(/\*\*Language\*\*:\s*(ja|en|other)/);
  return match ? (match[1] as 'ja' | 'en' | 'other') : undefined;
}

function extractOriginalTitle(content: string): string | undefined {
  const match = content.match(/\*\*Original Title\*\*:\s*(.+)$/m);
  return match ? match[1].trim() : undefined;
}

// File parsing functions
function parseJournalFile(
  filePath: string,
  type: 'main' | 'annex',
  date: string,
  parsingConfig?: JournalParsingConfig
): JournalEntry | null {
  try {
    if (!existsSync(filePath)) {
      return null;
    }

    const content = readFileSync(filePath, 'utf-8');
    const title = extractTitleFromMarkdown(content, parsingConfig, type);
    const wordCount = countWords(content);
    const readingTime = calculateReadingTime(wordCount);
    const excerpt = extractExcerpt(content, 200, parsingConfig, type);
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
    // Generate sequential ID based on alphabetical order
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
    const fullExcerpt = extractFullFirstParagraph(content);
    const slug = generateSlug(title);
    const language = extractLanguage(content);
    const originalTitle = extractOriginalTitle(content);

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
      fullExcerpt,
      language,
      originalTitle,
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
    const parsingConfig = metadata.parsing;
    
    let mainJournal = parseJournalFile(
      join(journalDir, `00_weekly_journal_${dateFormatted}.md`),
      'main',
      date,
      parsingConfig
    );

    // Fallback to older naming convention if not found
    if (!mainJournal) {
      mainJournal = parseJournalFile(
        join(journalDir, `weekly_journal_${dateFormatted}.md`),
        'main',
        date,
        parsingConfig
      );
    }

    // Try both naming conventions for annex journal
    let annexJournal = parseJournalFile(
      join(journalDir, `01_annex_journal_${dateFormatted}.md`),
      'annex',
      date,
      parsingConfig
    );

    // Fallback to older naming convention if not found
    if (!annexJournal) {
      annexJournal = parseJournalFile(
        join(journalDir, `annex_journal_${dateFormatted}.md`),
        'annex',
        date,
        parsingConfig
      );
    }

    // Parse summaries (but assign status based on metadata)
    // Try both 'summaries' and 'sources' directories for backward compatibility
    let summariesDir = join(journalDir, 'summaries');
    let summaries: SummaryEntry[] = [];

    // Fallback to 'sources' directory for older journal structure
    if (!existsSync(summariesDir)) {
      summariesDir = join(journalDir, 'sources');
    }

    if (existsSync(summariesDir)) {
      const allFiles = readdirSync(summariesDir);
      const summaryFiles = allFiles.filter((file) => 
        file.endsWith('.md') && 
        !file.includes('sources.md') && 
        !file.includes('omitted_sources.md')
      );

      // Parse and sort by numeric ID from filename
      const summariesWithIds = summaryFiles
        .map((file) => {
          const filePath = join(summariesDir, file);
          const summary = parseSummaryFile(filePath, date);
          
          if (summary) {
            // Extract numeric ID from filename for proper sorting
            const numericId = parseInt(summary.id, 10);
            return { summary, numericId, filename: file };
          }
          return null;
        })
        .filter((item): item is { summary: SummaryEntry; numericId: number; filename: string } => item !== null);

      // Sort by numeric ID, then by filename for consistent ordering of duplicates
      summariesWithIds.sort((a, b) => {
        if (a.numericId !== b.numericId) {
          return a.numericId - b.numericId;
        }
        // For duplicate IDs, sort alphabetically by filename
        return a.filename.localeCompare(b.filename);
      });

      // Assign status based on metadata counts and sorted position
      summaries = summariesWithIds.map(({ summary }, sortedIndex) => {
        if (sortedIndex < metadata.statistics.mainSummaries) {
          summary.status = 'main';
        } else if (sortedIndex < metadata.statistics.mainSummaries + metadata.statistics.annexSummaries) {
          summary.status = 'annex';
        } else {
          summary.status = 'omitted';
        }
        return summary;
      });

      // Validate that we have the expected number of summaries
      if (summaries.length !== metadata.totalSummaries) {
        console.warn(
          `Summary count mismatch for ${date}: found ${summaries.length} files, expected ${metadata.totalSummaries}`
        );
      }
    }

    // Use actual parsed summaries count as single source of truth
    const mainCount = summaries.filter(s => s.status === 'main').length;
    const annexCount = summaries.filter(s => s.status === 'annex').length;
    const omittedCount = summaries.filter(s => s.status === 'omitted').length;
    
    const stats = {
      totalSummaries: summaries.length,
      mainSummaries: mainCount,
      annexSummaries: annexCount,
      omittedSummaries: omittedCount,
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
