import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { summaryParsers } from './summary-parser';

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

  // JSON-specific metadata (optional, only present for JSON summaries)
  contentType?: string; // Content category (e.g., "🔬 Research & Analysis")
  oneSentence?: string; // One sentence summary
  topics?: string[]; // Topic tags (1-5 tags)
  scores?: {
    signal: number;
    depth: number;
    uniqueness: number;
    practical: number;
    antiHype: number;
    mainJournal: number;
    annexPotential: number;
    overall: number;
  };
  metadata?: {
    version: string;
    generatedAt: string;
    generatedBy: string;
    format: 'json' | 'markdown';
  };
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


function parseSummaryFile(filePath: string, date: string): SummaryEntry | null {
  try {
    if (!existsSync(filePath)) {
      return null;
    }

    const content = readFileSync(filePath, 'utf-8');

    // Use parser registry to handle both JSON and markdown formats
    return summaryParsers.parseSummary(filePath, date, content);
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
        (file.endsWith('.md') || file.endsWith('.json')) &&
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
