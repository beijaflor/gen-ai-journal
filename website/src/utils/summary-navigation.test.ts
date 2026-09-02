import { describe, expect, it } from 'vitest';
import { getSummaryNeighbours } from './summary-navigation';

const summary = (id: string) => ({ id, title: `Summary ${id}` });

const ascending = [summary('001'), summary('002'), summary('003')]; // published journal order
const descending = [...ascending].reverse(); // workdesk order

describe('getSummaryNeighbours', () => {
  describe.each([
    ['ascending input (published journal)', ascending],
    ['descending input (workdesk)', descending],
  ])('with %s', (_label, list) => {
    it('resolves prev as the lower ID and next as the higher ID', () => {
      const { prev, next } = getSummaryNeighbours(list, '002');
      expect(prev?.id).toBe('001');
      expect(next?.id).toBe('003');
    });

    it('has no prev on the lowest ID', () => {
      const { prev, next } = getSummaryNeighbours(list, '001');
      expect(prev).toBeNull();
      expect(next?.id).toBe('002');
    });

    it('has no next on the highest ID', () => {
      const { prev, next } = getSummaryNeighbours(list, '003');
      expect(prev?.id).toBe('002');
      expect(next).toBeNull();
    });
  });

  it('returns no neighbours when the ID is not in the list', () => {
    expect(getSummaryNeighbours(ascending, '999')).toEqual({ prev: null, next: null });
  });

  it('returns no neighbours for an empty list', () => {
    expect(getSummaryNeighbours([], '001')).toEqual({ prev: null, next: null });
  });

  it('orders by numeric ID, not lexicographically', () => {
    const list = [summary('100'), summary('009'), summary('010')];
    const { prev, next } = getSummaryNeighbours(list, '010');
    expect(prev?.id).toBe('009');
    expect(next?.id).toBe('100');
  });

  it('does not mutate the input list', () => {
    const list = [...descending];
    getSummaryNeighbours(list, '002');
    expect(list.map((s) => s.id)).toEqual(['003', '002', '001']);
  });
});
