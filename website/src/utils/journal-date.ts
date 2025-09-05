import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';

/**
 * Extract the next journal date from workdesk/sources.md title
 * Expected format: "# Sources for Journal YYYY-MM-DD"
 */
export function getNextJournalDate(): string {
  const workdeskPath = join(process.cwd(), '../workdesk');
  const sourcesPath = join(workdeskPath, 'sources.md');

  if (!existsSync(sourcesPath)) {
    console.warn(`Workdesk sources file not found: ${sourcesPath}`);
    return getDefaultNextJournalDate();
  }

  try {
    const content = readFileSync(sourcesPath, 'utf-8');
    
    // Match title pattern: "# Sources for Journal 2025-08-30"
    const titleMatch = content.match(/^#\s+Sources for Journal\s+(\d{4}-\d{2}-\d{2})/m);
    
    if (titleMatch && titleMatch[1]) {
      const date = titleMatch[1];
      
      // Validate date format
      if (isValidDateFormat(date)) {
        return date;
      } else {
        console.warn(`Invalid date format in sources.md: ${date}`);
      }
    } else {
      console.warn('Could not find journal date in sources.md title');
    }
  } catch (error) {
    console.warn('Failed to read workdesk/sources.md:', error);
  }

  // Fallback to calculated next date
  return getDefaultNextJournalDate();
}

/**
 * Check if the given date is the next journal date
 */
export function isNextJournalDate(date: string): boolean {
  return date === getNextJournalDate();
}

/**
 * Get journal status based on date
 */
export function getJournalStatus(date: string): 'published' | 'draft' {
  return isNextJournalDate(date) ? 'draft' : 'published';
}

/**
 * Get status label for display
 */
export function getJournalStatusLabel(date: string): string {
  if (isNextJournalDate(date)) {
    return `次号掲載予定 (${date}号)`;
  } else {
    return `掲載済み (${date}号)`;
  }
}

/**
 * Validate YYYY-MM-DD date format
 */
function isValidDateFormat(dateString: string): boolean {
  const dateRegex = /^\d{4}-\d{2}-\d{2}$/;
  if (!dateRegex.test(dateString)) {
    return false;
  }

  // Check if it's a valid date
  const date = new Date(dateString);
  return date.toISOString().startsWith(dateString);
}

/**
 * Calculate default next journal date (next Friday)
 * This is used as fallback when sources.md is not available or parseable
 */
function getDefaultNextJournalDate(): string {
  const today = new Date();
  const nextFriday = new Date(today);
  
  // Calculate next Friday (assuming journals are published on Fridays)
  const daysUntilFriday = (5 - today.getDay() + 7) % 7;
  const daysToAdd = daysUntilFriday === 0 ? 7 : daysUntilFriday; // If today is Friday, get next Friday
  
  nextFriday.setDate(today.getDate() + daysToAdd);
  
  return nextFriday.toISOString().split('T')[0];
}

/**
 * Format date for display in Japanese
 */
export function formatJapaneseDateDisplay(date: string): string {
  try {
    const dateObj = new Date(date);
    return dateObj.toLocaleDateString('ja-JP', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      weekday: 'long',
    });
  } catch (error) {
    console.warn('Failed to format Japanese date:', error);
    return date;
  }
}