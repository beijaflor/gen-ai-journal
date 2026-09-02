/**
 * Prev/next neighbour lookup for summary detail pages.
 *
 * The two summary sources are sorted in opposite directions:
 *   - workdesk summaries (`getAllWorkdeskSummaries`) are newest-first (descending ID)
 *   - published journal summaries (`parseJournalByDate`) are oldest-first (ascending ID)
 *
 * Navigation must not depend on which parser produced the list, so neighbours
 * are always resolved against a canonical ascending-by-ID order:
 *   - "前のサマリー" (prev) is the summary with the next lower ID
 *   - "次のサマリー" (next) is the summary with the next higher ID
 */

export interface NavigableSummary {
  id: string; // 3-digit ID, e.g. "005"
  title: string;
}

export interface SummaryNeighbours<T extends NavigableSummary> {
  prev: T | null;
  next: T | null;
}

export function getSummaryNeighbours<T extends NavigableSummary>(
  summaries: readonly T[],
  currentId: string
): SummaryNeighbours<T> {
  const ordered = [...summaries].sort(
    (a, b) => Number.parseInt(a.id, 10) - Number.parseInt(b.id, 10)
  );
  const index = ordered.findIndex((summary) => summary.id === currentId);

  if (index === -1) {
    return { prev: null, next: null };
  }

  return {
    prev: index > 0 ? ordered[index - 1] : null,
    next: index < ordered.length - 1 ? ordered[index + 1] : null,
  };
}
