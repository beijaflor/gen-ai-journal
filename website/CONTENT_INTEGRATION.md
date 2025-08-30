# Content Integration Specification

## Overview

This document specifies how the Astro website integrates with the existing journal content structure, including parsing logic, data transformation, and URL generation strategies.

## Source Content Structure

### Directory Layout
```
../journals/
├── 2025-06-29/
│   ├── 00_weekly_journal_2025_06_29.md
│   ├── 01_annex_journal_2025_06_29.md
│   ├── 02_omitted_summaries.md
│   ├── 99_unified_summaries.md
│   ├── sources/
│   │   ├── sources.md
│   │   ├── curated_journal_sources.md
│   │   ├── curated_annex_journal_sources.md
│   │   └── omitted_sources.md
│   └── summaries/
│       ├── 001_note_com_npaka_n_n50cacd92648f.md
│       ├── 002_qiita_com_akira_papa_AI_items_15314a5bf1dd109053c2.md
│       └── ...
├── 2025-07-09/
├── 2025-07-12/
└── ...
```

### File Naming Conventions

#### Journal Files
- **Main Journal**: `00_weekly_journal_YYYY_MM_DD.md`
- **Annex Journal**: `01_annex_journal_YYYY_MM_DD.md`
- **Omitted Summaries**: `02_omitted_summaries.md`
- **Unified Summaries**: `99_unified_summaries.md` (reference only)

#### Summary Files
- **Pattern**: `{ID}_{domain}_{path_segments}.md`
- **ID**: 3-digit number (001, 002, etc.)
- **Domain**: Original domain with dots replaced by underscores
- **Path**: URL path segments separated by underscores

#### Examples
```
001_note_com_npaka_n_n50cacd92648f.md
→ ID: 001
→ Domain: note.com
→ Path: npaka/n/n50cacd92648f
→ URL: https://note.com/npaka/n/n50cacd92648f

002_qiita_com_akira_papa_AI_items_15314a5bf1dd109053c2.md
→ ID: 002
→ Domain: qiita.com
→ Path: akira_papa_AI/items/15314a5bf1dd109053c2
→ URL: https://qiita.com/akira_papa_AI/items/15314a5bf1dd109053c2
```

## Content Parsing Logic

### Date Extraction
```typescript
function extractDateFromPath(journalPath: string): string {
  const dateMatch = journalPath.match(/(\d{4}-\d{2}-\d{2})/);
  if (!dateMatch) {
    throw new Error(`Invalid journal path: ${journalPath}`);
  }
  return dateMatch[1];
}

// Example: "../journals/2025-08-16/" → "2025-08-16"
```

### Summary ID and URL Parsing
```typescript
function parseSummaryFilename(filename: string): {
  id: string;
  domain: string;
  path: string;
  url: string;
} {
  // Remove .md extension
  const nameWithoutExt = filename.replace(/\.md$/, '');
  
  // Extract ID (first 3 digits)
  const idMatch = nameWithoutExt.match(/^(\d{3})_(.+)$/);
  if (!idMatch) {
    throw new Error(`Invalid summary filename: ${filename}`);
  }
  
  const [, id, urlPart] = idMatch;
  
  // Parse domain and path
  const parts = urlPart.split('_');
  const domain = parts[0].replace(/_/g, '.');
  const path = parts.slice(1).join('/');
  
  // Reconstruct URL
  const url = `https://${domain}/${path}`;
  
  return { id, domain, path, url };
}

// Example: "001_note_com_npaka_n_n50cacd92648f.md"
// → { id: "001", domain: "note.com", path: "npaka/n/n50cacd92648f", url: "https://note.com/npaka/n/n50cacd92648f" }
```

### Markdown Content Processing
```typescript
interface MarkdownFrontmatter {
  title?: string;
  date?: string;
  tags?: string[];
  status?: 'main' | 'annex' | 'omitted';
}

function parseMarkdownContent(content: string): {
  frontmatter: MarkdownFrontmatter;
  body: string;
  title: string;
  wordCount: number;
  readingTime: number;
} {
  // Parse frontmatter if present
  const frontmatterMatch = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  
  let frontmatter: MarkdownFrontmatter = {};
  let body = content;
  
  if (frontmatterMatch) {
    frontmatter = parseYaml(frontmatterMatch[1]);
    body = frontmatterMatch[2];
  }
  
  // Extract title from first heading or frontmatter
  const title = frontmatter.title || extractTitleFromMarkdown(body);
  
  // Calculate reading metrics
  const wordCount = countWords(body);
  const readingTime = Math.ceil(wordCount / 200); // 200 words per minute
  
  return { frontmatter, body, title, wordCount, readingTime };
}

function extractTitleFromMarkdown(markdown: string): string {
  const titleMatch = markdown.match(/^#\s+(.+)$/m);
  return titleMatch ? titleMatch[1].trim() : 'Untitled';
}

function countWords(text: string): number {
  // Count both Japanese characters and words
  const japaneseChars = (text.match(/[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]/g) || []).length;
  const englishWords = (text.match(/\b[A-Za-z]+\b/g) || []).length;
  
  // Approximate: 1 Japanese character ≈ 0.5 words
  return Math.round(japaneseChars * 0.5 + englishWords);
}
```

## Data Structures

### TypeScript Interfaces
```typescript
interface JournalEntry {
  date: string;           // YYYY-MM-DD
  type: 'main' | 'annex'; // Journal type
  title: string;          // Extracted from markdown
  content: string;        // Full markdown content
  html: string;           // Rendered HTML
  slug: string;           // URL slug
  wordCount: number;      // Word count
  readingTime: number;    // Minutes
  summaryCount: number;   // Associated summaries count
  metadata: {
    publishedAt: Date;
    tags?: string[];
    excerpt?: string;
  };
}

interface SummaryEntry {
  id: string;            // 3-digit ID
  date: string;          // Parent journal date
  filename: string;      // Original filename
  sourceUrl: string;     // Reconstructed URL
  domain: string;        // Source domain
  title: string;         // Extracted title
  content: string;       // Markdown content
  html: string;          // Rendered HTML
  status: 'main' | 'annex' | 'omitted'; // Inclusion status
  slug: string;          // URL slug
  wordCount: number;     // Word count
  readingTime: number;   // Minutes
  metadata: {
    tags?: string[];
    excerpt?: string;
  };
}

interface JournalArchive {
  date: string;          // YYYY-MM-DD
  mainJournal: JournalEntry;
  annexJournal: JournalEntry;
  summaries: SummaryEntry[];
  stats: {
    totalSummaries: number;
    mainSummaries: number;
    annexSummaries: number;
    omittedSummaries: number;
  };
}
```

## Status Determination Logic

### Summary Inclusion Status
```typescript
function determineSummaryStatus(
  summaryId: string,
  date: string,
  curatedSources: string[]
): 'main' | 'annex' | 'omitted' {
  // Read curated source files to determine status
  const mainSources = readCuratedSources(date, 'main');
  const annexSources = readCuratedSources(date, 'annex');
  
  const summaryUrl = reconstructUrlFromId(summaryId, date);
  
  if (mainSources.includes(summaryUrl)) {
    return 'main';
  } else if (annexSources.includes(summaryUrl)) {
    return 'annex';
  } else {
    return 'omitted';
  }
}

function readCuratedSources(date: string, type: 'main' | 'annex'): string[] {
  const filename = type === 'main' 
    ? 'curated_journal_sources.md'
    : 'curated_annex_journal_sources.md';
  
  const sourcesPath = `../journals/${date}/sources/${filename}`;
  const content = readFileSync(sourcesPath, 'utf-8');
  
  // Extract URLs from markdown links
  const urlMatches = content.match(/\[.+?\]\((.+?)\)/g) || [];
  return urlMatches.map(match => {
    const urlMatch = match.match(/\]\((.+?)\)/);
    return urlMatch ? urlMatch[1] : '';
  }).filter(Boolean);
}
```

## URL Generation Strategy

### Website URL Structure
```typescript
interface UrlMapping {
  // Journal pages
  journalOverview: `/journals/${date}/`;
  mainJournal: `/journals/${date}/main/`;
  annexJournal: `/journals/${date}/annex/`;
  summariesList: `/journals/${date}/summaries/`;
  
  // Individual summaries
  summary: `/summaries/${date}/${id}/`;
  
  // Archive and navigation
  homepage: '/';
  archive: '/archive/';
}

function generateSummaryUrl(summaryEntry: SummaryEntry): string {
  return `/summaries/${summaryEntry.date}/${summaryEntry.id}/`;
}

function generateJournalUrl(journal: JournalEntry): string {
  return `/journals/${journal.date}/${journal.type}/`;
}
```

### SEO-Friendly Slugs
```typescript
function generateSlug(title: string): string {
  return title
    .toLowerCase()
    .replace(/[^\w\s\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF-]/g, '') // Keep alphanumeric and Japanese
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .trim();
}

// Example: "AI開発ツールの実用性革命" → "ai開発ツールの実用性革命"
```

## Error Handling

### Content Validation
```typescript
function validateJournalStructure(journalPath: string): ValidationResult {
  const errors: string[] = [];
  const warnings: string[] = [];
  
  // Check required files
  const requiredFiles = [
    '00_weekly_journal_*.md',
    '01_annex_journal_*.md'
  ];
  
  for (const pattern of requiredFiles) {
    if (!fileExists(path.join(journalPath, pattern))) {
      errors.push(`Missing required file: ${pattern}`);
    }
  }
  
  // Check summaries directory
  const summariesPath = path.join(journalPath, 'summaries');
  if (!directoryExists(summariesPath)) {
    warnings.push('No summaries directory found');
  } else {
    const summaryFiles = glob.sync('*.md', { cwd: summariesPath });
    if (summaryFiles.length === 0) {
      warnings.push('No summary files found');
    }
  }
  
  return { errors, warnings, isValid: errors.length === 0 };
}

interface ValidationResult {
  errors: string[];
  warnings: string[];
  isValid: boolean;
}
```

### Graceful Degradation
```typescript
function safeParseContent(filePath: string): ParseResult {
  try {
    const content = readFileSync(filePath, 'utf-8');
    return {
      success: true,
      data: parseMarkdownContent(content)
    };
  } catch (error) {
    console.warn(`Failed to parse ${filePath}:`, error.message);
    return {
      success: false,
      error: error.message,
      data: {
        title: 'Content Unavailable',
        content: 'This content could not be loaded.',
        html: '<p>This content could not be loaded.</p>'
      }
    };
  }
}

interface ParseResult {
  success: boolean;
  data: any;
  error?: string;
}
```

## Astro Content Collections

### Collection Definitions
```typescript
// src/content/config.ts
import { defineCollection, z } from 'astro:content';

const journalsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.string(),
    type: z.enum(['main', 'annex']),
    tags: z.array(z.string()).optional(),
    excerpt: z.string().optional(),
  }),
});

const summariesCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.string(),
    sourceUrl: z.string(),
    domain: z.string(),
    status: z.enum(['main', 'annex', 'omitted']),
    tags: z.array(z.string()).optional(),
  }),
});

export const collections = {
  journals: journalsCollection,
  summaries: summariesCollection,
};
```

### Dynamic Content Loading
```typescript
// src/utils/content-loader.ts
import { getCollection } from 'astro:content';

export async function getAllJournals(): Promise<JournalEntry[]> {
  const journals = await getCollection('journals');
  return journals
    .map(transformJournalEntry)
    .sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime());
}

export async function getJournalsByDate(date: string): Promise<{
  main: JournalEntry | null;
  annex: JournalEntry | null;
}> {
  const journals = await getCollection('journals', 
    ({ data }) => data.date === date
  );
  
  return {
    main: journals.find(j => j.data.type === 'main') || null,
    annex: journals.find(j => j.data.type === 'annex') || null,
  };
}

export async function getSummariesByDate(date: string): Promise<SummaryEntry[]> {
  const summaries = await getCollection('summaries',
    ({ data }) => data.date === date
  );
  
  return summaries
    .map(transformSummaryEntry)
    .sort((a, b) => parseInt(a.id) - parseInt(b.id));
}
```

## Performance Optimization

### Build-Time Processing
- All content parsing happens at build time
- Generated static pages for all journal and summary entries
- Pre-computed summary statistics and relationships

### Caching Strategy
```typescript
// Cache parsed content during build
const contentCache = new Map<string, any>();

function getCachedContent(key: string, loader: () => any): any {
  if (!contentCache.has(key)) {
    contentCache.set(key, loader());
  }
  return contentCache.get(key);
}
```

### Incremental Updates
- Only regenerate pages when source content changes
- Astro's built-in change detection for hot reloading
- Efficient build process for large numbers of summaries

---

This content integration specification ensures reliable, performant access to all journal content while maintaining data integrity and providing excellent developer experience.