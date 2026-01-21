import {
  type SummaryMetadata,
  getJournalMetadata,
  getWorkdeskMetadata,
} from './supabase';

/**
 * Build-time cache for Supabase metadata
 * Ensures we only query Supabase once during static site generation
 */

type CacheKey = string; // Format: "{summary_id}:{url}"
type MetadataCache = Map<CacheKey, SummaryMetadata>;

// Global cache (persists during entire build)
const journalCache: Map<string, MetadataCache> = new Map();
let workdeskCache: MetadataCache | null = null;
let isWorkdeskCacheLoaded = false;

/**
 * Generate cache key from summary ID and URL
 */
function makeCacheKey(summaryId: string, url: string): CacheKey {
  return `${summaryId}:${url}`;
}

/**
 * Load all workdesk metadata into cache (called once during build)
 */
async function loadWorkdeskCache(): Promise<void> {
  if (isWorkdeskCacheLoaded) {
    return;
  }

  console.log('[supabase-cache] Loading workdesk metadata...');

  try {
    const metadata = await getWorkdeskMetadata();
    workdeskCache = new Map();

    for (const item of metadata) {
      const key = makeCacheKey(item.summary_id, item.url);
      workdeskCache.set(key, item);
    }

    isWorkdeskCacheLoaded = true;
    console.log(
      `[supabase-cache] Loaded ${metadata.length} workdesk summaries`
    );
  } catch (error) {
    console.error('[supabase-cache] Failed to load workdesk metadata:', error);
    workdeskCache = new Map();
    isWorkdeskCacheLoaded = true; // Prevent retry loops
  }
}

/**
 * Load all metadata for a specific journal into cache
 */
async function loadJournalCache(journalDate: string): Promise<void> {
  if (journalCache.has(journalDate)) {
    return;
  }

  console.log(`[supabase-cache] Loading metadata for journal ${journalDate}...`);

  try {
    const metadata = await getJournalMetadata(journalDate);
    const cache = new Map();

    for (const item of metadata) {
      const key = makeCacheKey(item.summary_id, item.url);
      cache.set(key, item);
    }

    journalCache.set(journalDate, cache);
    console.log(
      `[supabase-cache] Loaded ${metadata.length} summaries for ${journalDate}`
    );
  } catch (error) {
    console.error(
      `[supabase-cache] Failed to load metadata for ${journalDate}:`,
      error
    );
    journalCache.set(journalDate, new Map()); // Empty cache to prevent retry
  }
}

/**
 * Get metadata for a workdesk summary (cached)
 */
export async function getWorkdeskSummaryMetadata(
  summaryId: string,
  url: string
): Promise<SummaryMetadata | null> {
  // Ensure cache is loaded
  if (!isWorkdeskCacheLoaded) {
    await loadWorkdeskCache();
  }

  const key = makeCacheKey(summaryId, url);
  return workdeskCache?.get(key) || null;
}

/**
 * Get metadata for a published journal summary (cached)
 */
export async function getJournalSummaryMetadata(
  journalDate: string,
  summaryId: string,
  url: string
): Promise<SummaryMetadata | null> {
  // Ensure cache is loaded for this journal
  if (!journalCache.has(journalDate)) {
    await loadJournalCache(journalDate);
  }

  const cache = journalCache.get(journalDate);
  if (!cache) {
    return null;
  }

  const key = makeCacheKey(summaryId, url);
  return cache.get(key) || null;
}

/**
 * Get all cached workdesk metadata (after cache is loaded)
 */
export async function getAllWorkdeskMetadata(): Promise<SummaryMetadata[]> {
  if (!isWorkdeskCacheLoaded) {
    await loadWorkdeskCache();
  }

  return Array.from(workdeskCache?.values() || []);
}

/**
 * Get all cached metadata for a journal (after cache is loaded)
 */
export async function getAllJournalMetadata(
  journalDate: string
): Promise<SummaryMetadata[]> {
  if (!journalCache.has(journalDate)) {
    await loadJournalCache(journalDate);
  }

  const cache = journalCache.get(journalDate);
  return Array.from(cache?.values() || []);
}

/**
 * Clear all caches (useful for testing or manual refresh)
 */
export function clearAllCaches(): void {
  journalCache.clear();
  workdeskCache = null;
  isWorkdeskCacheLoaded = false;
  console.log('[supabase-cache] All caches cleared');
}

/**
 * Preload all metadata for better performance
 * Call this at the start of your build process
 */
export async function preloadAllMetadata(journalDates: string[]): Promise<void> {
  console.log('[supabase-cache] Preloading all metadata...');

  // Load workdesk metadata
  await loadWorkdeskCache();

  // Load all journal metadata in parallel
  await Promise.all(journalDates.map((date) => loadJournalCache(date)));

  console.log('[supabase-cache] All metadata preloaded');
}
