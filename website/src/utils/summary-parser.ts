/**
 * Summary Parser Registry
 *
 * Handles format detection and routing to appropriate parsers for both
 * JSON (structured) and Markdown (legacy) summary formats.
 */

import { JsonV1Parser } from './parsers/json-v1-parser';
import { MarkdownLegacyParser } from './parsers/markdown-legacy-parser';
import type { SummaryEntry } from './content-parser';

export type SummaryFormat = 'json-v1' | 'markdown-legacy' | 'unknown';

export interface FormatDetectionResult {
  format: SummaryFormat;
  confidence: 'high' | 'medium' | 'low';
  version?: string;
}

/**
 * Detects summary format based on file extension and content inspection
 *
 * Priority order:
 * 1. File extension (.json vs .md)
 * 2. Content inspection (JSON.parse + version field)
 * 3. Fallback to markdown legacy
 */
export function detectSummaryFormat(
  filePath: string,
  content?: string
): FormatDetectionResult {
  // Strategy 1: File extension (99% of cases)
  if (filePath.endsWith('.json')) {
    return {
      format: 'json-v1',
      confidence: 'high',
      version: '1.0'
    };
  }

  if (filePath.endsWith('.md')) {
    return {
      format: 'markdown-legacy',
      confidence: 'high'
    };
  }

  // Strategy 2: Content inspection (if content provided)
  if (content) {
    try {
      const parsed = JSON.parse(content);
      if (parsed.metadata?.version === '1.0') {
        return {
          format: 'json-v1',
          confidence: 'medium',
          version: '1.0'
        };
      }
    } catch {
      // Not JSON, continue to fallback
    }
  }

  // Strategy 3: Fallback to markdown
  return {
    format: 'markdown-legacy',
    confidence: 'low'
  };
}

/**
 * Parser interface that all format parsers must implement
 */
export interface SummaryParser {
  readonly format: SummaryFormat;
  readonly version?: string;

  /**
   * Parse summary file and convert to unified SummaryEntry
   */
  parse(filePath: string, journalDate: string, content: string): SummaryEntry | null;

  /**
   * Validate summary structure (optional)
   */
  validate?(content: string): boolean;
}

/**
 * Parser Registry
 *
 * Maps format+version to parser implementation.
 * Handles routing and parser lifecycle.
 */
export class ParserRegistry {
  private parsers: Map<string, SummaryParser> = new Map();

  constructor() {
    // Register built-in parsers
    this.register(new JsonV1Parser());
    this.register(new MarkdownLegacyParser());
  }

  /**
   * Register a parser for a specific format
   */
  register(parser: SummaryParser): void {
    const key = parser.version
      ? `${parser.format}-${parser.version}`
      : parser.format;
    this.parsers.set(key, parser);
  }

  /**
   * Get parser for a specific format
   */
  getParser(format: SummaryFormat, version?: string): SummaryParser | null {
    // Try format + version first
    if (version) {
      const key = `${format}-${version}`;
      const parser = this.parsers.get(key);
      if (parser) return parser;
    }

    // Fallback to format only
    return this.parsers.get(format) || null;
  }

  /**
   * Parse summary file using appropriate parser
   *
   * Main entry point for parsing summaries.
   */
  parseSummary(
    filePath: string,
    journalDate: string,
    content: string
  ): SummaryEntry | null {
    // Detect format
    const detection = detectSummaryFormat(filePath, content);

    // Get appropriate parser
    const parser = this.getParser(detection.format, detection.version);

    if (!parser) {
      console.error(`No parser found for format: ${detection.format}`);
      return null;
    }

    // Validate if parser supports validation
    if (parser.validate && !parser.validate(content)) {
      console.error(`Validation failed for ${filePath}`);
      return null;
    }

    // Parse and return
    try {
      return parser.parse(filePath, journalDate, content);
    } catch (error) {
      console.error(`Failed to parse ${filePath}:`, error);
      return null;
    }
  }
}

// Singleton instance
export const summaryParsers = new ParserRegistry();
