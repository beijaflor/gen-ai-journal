import { existsSync, readdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

export interface WorkdeskSummary {
  id: string; // 3-digit ID from filename
  filename: string; // Original filename
  title: string; // Extracted from markdown
  excerpt: string; // Brief summary
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

    const filename = filePath.split('/').pop() || '';
    const parsedFilename = parseSummaryFilename(filename);

    if (!parsedFilename) {
      return null;
    }

    const content = readFileSync(filePath, 'utf-8');
    const stats = statSync(filePath);
    
    const title = extractTitleFromMarkdown(content);
    const excerpt = extractExcerpt(content);
    const fullContent = extractFullContent(content);
    const url = extractUrlFromContent(content) || parsedFilename.url;
    const wordCount = countWords(content);
    const scores = extractScores(content);
    const topics = extractTopics(content);

    return {
      id: parsedFilename.id,
      filename,
      title,
      excerpt,
      fullContent,
      url,
      domain: parsedFilename.domain,
      modifiedAt: stats.mtime,
      wordCount,
      scores,
      topics,
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
      file.endsWith('.md') && 
      /^\d{3}_/.test(file) // Only files starting with 3-digit ID
    );

    const summaries = summaryFiles
      .map(file => {
        const filePath = join(summariesPath, file);
        return parseWorkdeskSummaryFile(filePath);
      })
      .filter((summary): summary is WorkdeskSummary => summary !== null);

    // Sort by modification time (latest first)
    summaries.sort((a, b) => b.modifiedAt.getTime() - a.modifiedAt.getTime());

    return summaries;
  } catch (error) {
    console.warn('Failed to read workdesk summaries directory:', error);
    return [];
  }
}