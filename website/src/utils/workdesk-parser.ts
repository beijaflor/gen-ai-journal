import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';
import { summaryParsers } from './summary-parser';

export interface WorkdeskSummary {
  id: string; // 3-digit ID from filename
  filename: string; // Original filename
  title: string; // Extracted from markdown
  excerpt: string; // Brief summary
  fullExcerpt?: string; // Full first paragraph (no truncation)
  fullContent: string; // Full markdown content body
  url: string; // Reconstructed URL
  domain: string; // Source domain
  modifiedAt: Date; // File modification time
  wordCount: number; // Word count
  scores?: {
    signal?: number;
    depth?: number;
    unique?: number;
    practical?: number;
    antiHype?: number;
    mainJournal?: number;
    annexPotential?: number;
    overall?: number;
  };
  topics?: string[];
  language?: 'ja' | 'en' | 'other'; // Source language
  originalTitle?: string; // Original title (for non-Japanese articles)
}

function extractTitleFromMarkdown(content: string): string {
  // Look for first heading (## title format)
  const titleMatch = content.match(/^##\s+(.+)$/m);
  if (titleMatch) {
    return titleMatch[1].trim();
  }

  // Fallback to first non-empty line
  const lines = content.split('\n');
  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed && !trimmed.startsWith('##') && !trimmed.startsWith('https://')) {
      return trimmed.substring(0, 100);
    }
  }

  return 'Untitled';
}

function extractExcerpt(content: string, maxLength: number = 150): string {
  // Find the main Japanese summary paragraph (usually after the first URL)
  const lines = content.split('\n');
  let foundUrl = false;

  for (const line of lines) {
    const trimmed = line.trim();

    // Skip until after URL and metadata
    if (trimmed.startsWith('https://')) {
      foundUrl = true;
      continue;
    }

    if (trimmed.startsWith('**') || trimmed.startsWith('[[')) {
      continue;
    }

    // Look for substantial Japanese content
    if (foundUrl && trimmed.length > 20 && /[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]/.test(trimmed)) {
      return trimmed.length > maxLength ? `${trimmed.substring(0, maxLength)}...` : trimmed;
    }
  }

  // Fallback: get first paragraph with Japanese characters
  const paragraphs = content.split('\n\n');
  for (const paragraph of paragraphs) {
    const trimmed = paragraph.trim();
    if (trimmed.length > 20 && /[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]/.test(trimmed)) {
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

function extractUrlFromContent(content: string): string {
  // Look for URL in the content (usually the first https:// line)
  const urlMatch = content.match(/^https?:\/\/[^\s]+$/m);
  if (urlMatch) {
    return urlMatch[0];
  }
  
  return '';
}

function extractScores(content: string): WorkdeskSummary['scores'] {
  const scores: WorkdeskSummary['scores'] = {};
  
  // Extract scores line: **Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:3/5 | Anti-Hype:5/5
  const scoresMatch = content.match(/\*\*Scores\*\*:\s*(.+)$/m);
  if (scoresMatch) {
    const scoresLine = scoresMatch[1];
    
    const signalMatch = scoresLine.match(/Signal:(\d+)\/5/);
    if (signalMatch) scores.signal = parseInt(signalMatch[1], 10);
    
    const depthMatch = scoresLine.match(/Depth:(\d+)\/5/);
    if (depthMatch) scores.depth = parseInt(depthMatch[1], 10);
    
    const uniqueMatch = scoresLine.match(/Unique:(\d+)\/5/);
    if (uniqueMatch) scores.unique = parseInt(uniqueMatch[1], 10);
    
    const practicalMatch = scoresLine.match(/Practical:(\d+)\/5/);
    if (practicalMatch) scores.practical = parseInt(practicalMatch[1], 10);
    
    const antiHypeMatch = scoresLine.match(/Anti-Hype:(\d+)\/5/);
    if (antiHypeMatch) scores.antiHype = parseInt(antiHypeMatch[1], 10);
  }
  
  // Extract journal scores: **Main Journal**: 77/100 | **Annex Potential**: 79/100 | **Overall**: 76/100
  const journalMatch = content.match(/\*\*Main Journal\*\*:\s*(\d+)\/100.*?\*\*Annex Potential\*\*:\s*(\d+)\/100.*?\*\*Overall\*\*:\s*(\d+)\/100/);
  if (journalMatch) {
    scores.mainJournal = parseInt(journalMatch[1], 10);
    scores.annexPotential = parseInt(journalMatch[2], 10);
    scores.overall = parseInt(journalMatch[3], 10);
  }
  
  return scores;
}

function extractTopics(content: string): string[] {
  // Extract topics: **Topics**: [[AI Hype, ソフトウェア品質, 開発者の生産性, リソース配分, オープンソース]]
  const topicsMatch = content.match(/\*\*Topics\*\*:\s*\[\[(.+?)\]\]/);
  if (topicsMatch) {
    return topicsMatch[1].split(',').map(topic => topic.trim());
  }

  return [];
}

function extractLanguage(content: string): 'ja' | 'en' | 'other' | undefined {
  const match = content.match(/\*\*Language\*\*:\s*(ja|en|other)/);
  return match ? (match[1] as 'ja' | 'en' | 'other') : undefined;
}

function extractOriginalTitle(content: string): string | undefined {
  const match = content.match(/\*\*Original Title\*\*:\s*(.+)$/m);
  return match ? match[1].trim() : undefined;
}

function extractFullContent(content: string): string {
  // Find the end of the metadata section (after **Topics** line)
  // The main content body starts after the empty line following topics
  const lines = content.split('\n');
  let contentStartIndex = -1;
  
  // Find the topics line
  for (let i = 0; i < lines.length; i++) {
    if (lines[i].match(/\*\*Topics\*\*:/)) {
      // Look for the next non-empty line after topics (skip empty lines)
      for (let j = i + 1; j < lines.length; j++) {
        if (lines[j].trim() !== '') {
          contentStartIndex = j;
          break;
        }
      }
      break;
    }
  }
  
  // If topics line not found, look for content after URL and basic metadata
  if (contentStartIndex === -1) {
    for (let i = 0; i < lines.length; i++) {
      const line = lines[i];
      // Skip title, URL, content type, scores lines
      if (line.startsWith('##') || 
          line.match(/^https?:\/\//) ||
          line.match(/\*\*Content Type\*\*:/) ||
          line.match(/\*\*Scores\*\*:/) ||
          line.match(/\*\*Main Journal\*\*:/) ||
          line.match(/\*\*Topics\*\*:/) ||
          line.trim() === '') {
        continue;
      }
      
      // Found first content line
      contentStartIndex = i;
      break;
    }
  }
  
  if (contentStartIndex === -1) {
    return '';
  }
  
  // Extract content from the start index to the end
  const contentLines = lines.slice(contentStartIndex);
  return contentLines.join('\n').trim();
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

    // Parse format: 001_domain_com_path.md
    const match = nameWithoutExt.match(/^(\d{3})_(.+)$/);
    if (match) {
      const [, id, urlPart] = match;

      // Parse domain and path
      const parts = urlPart.split('_');
      if (parts.length < 1) {
        return null;
      }

      // Reconstruct domain (replace first underscore back to dot)
      const domain = `${parts[0]}.${parts[1]}`;
      const path = parts.slice(2).join('/');

      // Reconstruct URL
      const url = `https://${domain}${path ? `/${path}` : ''}`;

      return { id, domain, path, url };
    }

    return null;
  } catch (error) {
    console.warn(`Failed to parse summary filename ${filename}:`, error);
    return null;
  }
}

function countWords(text: string): number {
  // Count both Japanese characters and English words
  const japaneseChars = (text.match(/[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]/g) || []).length;
  const englishWords = (text.match(/\b[A-Za-z]+\b/g) || []).length;

  // Approximate: 1 Japanese character ≈ 0.5 words
  return Math.round(japaneseChars * 0.5 + englishWords);
}

function parseWorkdeskSummaryFile(filePath: string): WorkdeskSummary | null {
  try {
    if (!existsSync(filePath)) {
      return null;
    }

    const content = readFileSync(filePath, 'utf-8');
    const stats = statSync(filePath);

    // Detect format and parse accordingly
    if (filePath.endsWith('.json')) {
      // Use parser registry for JSON format
      const parsed = summaryParsers.parseSummary(filePath, 'workdesk', content);

      if (!parsed) {
        return null;
      }

      // Convert to WorkdeskSummary format
      return {
        id: parsed.id,
        filename: parsed.filename,
        title: parsed.title,
        excerpt: parsed.excerpt || parsed.oneSentence || '',
        fullExcerpt: parsed.fullExcerpt || parsed.oneSentence || '', // Use fullExcerpt or oneSentence
        fullContent: parsed.content,
        url: parsed.sourceUrl,
        domain: parsed.domain,
        modifiedAt: stats.mtime,
        wordCount: parsed.wordCount,
        scores: parsed.scores ? {
          signal: parsed.scores.signal,
          depth: parsed.scores.depth,
          unique: parsed.scores.uniqueness,
          practical: parsed.scores.practical,
          antiHype: parsed.scores.antiHype,
          mainJournal: parsed.scores.mainJournal,
          annexPotential: parsed.scores.annexPotential,
          overall: parsed.scores.overall
        } : undefined,
        topics: parsed.topics,
        language: parsed.language,
        originalTitle: parsed.originalTitle,
      };
    }

    // Legacy markdown parsing (keep existing logic for backward compatibility)
    const filename = filePath.split('/').pop() || '';
    const parsedFilename = parseSummaryFilename(filename);

    if (!parsedFilename) {
      return null;
    }

    const title = extractTitleFromMarkdown(content);
    const excerpt = extractExcerpt(content);
    const fullExcerpt = extractFullFirstParagraph(content);
    const fullContent = extractFullContent(content);
    const url = extractUrlFromContent(content) || parsedFilename.url;
    const wordCount = countWords(content);
    const scores = extractScores(content);
    const topics = extractTopics(content);
    const language = extractLanguage(content);
    const originalTitle = extractOriginalTitle(content);

    return {
      id: parsedFilename.id,
      filename,
      title,
      excerpt,
      fullExcerpt,
      fullContent,
      url,
      domain: parsedFilename.domain,
      modifiedAt: stats.mtime,
      wordCount,
      scores,
      topics,
      language,
      originalTitle,
    };
  } catch (error) {
    console.warn(`Failed to parse workdesk summary file ${filePath}:`, error);
    return null;
  }
}

export function getWorkdeskPath(): string {
  // Point to the workdesk directory relative to the website directory
  return join(process.cwd(), '../workdesk');
}

export function getAllWorkdeskSummaries(): WorkdeskSummary[] {
  const workdeskPath = getWorkdeskPath();
  const summariesPath = join(workdeskPath, 'summaries');

  try {
    if (!existsSync(summariesPath)) {
      console.warn(`Workdesk summaries directory not found: ${summariesPath}`);
      return [];
    }

    const files = readdirSync(summariesPath);
    const summaryFiles = files.filter(file =>
      (file.endsWith('.md') || file.endsWith('.json')) &&
      /^\d{3}_/.test(file) // Only files starting with 3-digit ID
    );

    const summaries = summaryFiles
      .map(file => {
        const filePath = join(summariesPath, file);
        return parseWorkdeskSummaryFile(filePath);
      })
      .filter((summary): summary is WorkdeskSummary => summary !== null);

    // Sort by ID number (descending order: 122, 121, 120...)
    summaries.sort((a, b) => parseInt(b.id, 10) - parseInt(a.id, 10));

    return summaries;
  } catch (error) {
    console.warn('Failed to read workdesk summaries directory:', error);
    return [];
  }
}