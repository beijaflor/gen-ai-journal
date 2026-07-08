// Unit tests for the platform's pure logic (run: npm test in platform/).
// D1/DO/HTTP paths are covered by production e2e; these pin the invariants
// that silently corrupting would hurt most.

import { describe, expect, it } from "vitest";
import { sanitizeUrl, validateUrl } from "../functions/_lib/util";
import { blockedStubUrl, displayTitle, inspectSummary, isBlockedStub } from "../functions/_lib/summaries";
import { renderLinkPage, type LinkRow, type SummaryRow } from "../functions/_lib/summary_page";
import { tokensFromUsage } from "../worker/src/core";

describe("sanitizeUrl (mirrors scripts/check_link.py)", () => {
  it("strips tracking params and fragments, keeps real params", () => {
    expect(sanitizeUrl("https://example.com/a?utm_source=x&id=42#sec")).toBe("https://example.com/a?id=42");
    expect(sanitizeUrl("https://example.com/a?fbclid=1&gclid=2&mc_eid=3&ref=t&source=s&hl=ja")).toBe(
      "https://example.com/a",
    );
  });
  it("preserves params on allowlisted hosts", () => {
    expect(sanitizeUrl("https://en.wikipedia.org/w/index.php?title=LLM&utm_source=x")).toContain("utm_source=x");
  });
});

describe("validateUrl", () => {
  it("rejects local/private/non-http", () => {
    for (const u of ["http://localhost:3000/x", "http://127.0.0.1/", "http://10.0.0.5/", "http://192.168.1.1/", "ftp://example.com/"]) {
      expect(validateUrl(u)).not.toBeNull();
    }
  });
  it("accepts public https", () => {
    expect(validateUrl("https://example.com/article")).toBeNull();
  });
});

const VALID = JSON.stringify({
  metadata: { version: "1.0", generatedAt: "t", generatedBy: "m" },
  content: { title: "T", url: "https://e.com", summaryBody: "B", language: "ja" },
});

describe("summary classification", () => {
  it("valid summary-v1 passes inspection", () => {
    expect(inspectSummary(VALID).error).toBeUndefined();
    expect(inspectSummary(VALID).url).toBe("https://e.com");
  });
  it("missing fields fail with a reason", () => {
    expect(inspectSummary("{}").error).toBeTruthy();
    expect(inspectSummary("not json").error).toContain("neither");
  });
  it("BLOCKED stubs are detected and carry their URL", () => {
    const stub = "BLOCKED: nope\n\n- URL: https://x.com/a.pdf\n- Reason: r\n";
    expect(isBlockedStub(stub)).toBe(true);
    expect(isBlockedStub(VALID)).toBe(false);
    expect(blockedStubUrl(stub)).toBe("https://x.com/a.pdf");
  });
  it("displayTitle handles all three shapes", () => {
    expect(displayTitle(VALID)).toBe("T");
    expect(displayTitle("BLOCKED: reason here")).toContain("BLOCKED");
    expect(displayTitle("garbage")).toBe("(unparseable)");
  });
});

describe("renderLinkPage (#173 detail page, keyed by link id)", () => {
  const mkSummary = (over: Partial<SummaryRow> = {}): SummaryRow => ({
    id: "042",
    journal_date: null,
    url: "https://e.com/a",
    content: JSON.stringify({
      metadata: { version: "1.0", generatedAt: "t", generatedBy: "m" },
      content: {
        title: "見出し <script>alert(1)</script>",
        originalTitle: "Original & <Title>",
        url: "https://e.com/a",
        language: "en",
        contentType: "news",
        oneSentenceSummary: "一文要約。",
        summaryBody: "SECRET-BODY-MARKER 段落1。\n\n段落2。",
        topics: ["agents", "<b>xss</b>"],
        scores: { signal: 4, depth: 3, uniqueness: 2, practical: 4, antiHype: 5, mainJournal: 3, annexPotential: 4, overall: 4 },
      },
    }),
    status: "workdesk",
    pushed_at: "2026-07-06T00:00:00Z",
    updated_at: "2026-07-06T00:00:00Z",
    ...over,
  });
  const link: LinkRow = {
    id: 7,
    url: "https://e.com/a",
    note: null,
    status: "summarized",
    error: null,
    summary_id: "042",
    submitted_at: "2026-07-06T00:00:00Z",
    processed_at: "2026-07-06T00:01:00Z",
    fetch_ms: 500,
    ai_ms: 12000,
    tokens_in: 9000,
    tokens_out: 800,
  };

  it("summarized: renders content with all user text HTML-escaped, shows both ids", () => {
    const html = renderLinkPage(link, mkSummary());
    expect(html).toContain("SECRET-BODY-MARKER");
    expect(html).toContain("原題: Original &amp; &lt;Title&gt;");
    expect(html).toContain("&lt;script&gt;alert(1)&lt;/script&gt;");
    expect(html).not.toContain("<script>alert(1)</script>");
    expect(html).toContain("&lt;b&gt;xss&lt;/b&gt;");
    expect(html).toContain("re-summarize"); // summarized link → re-summarize action
    expect(html).toContain("L7"); // primary key…
    expect(html).toContain("NNN 042"); // …and the editorial number stays visible
    expect(html).toContain('"summaryId":"042"'); // events merged with the NNN history
  });

  it("section order: result overview → log → content → link", () => {
    const html = renderLinkPage(link, mkSummary());
    const result = html.indexOf('<section id="result"');
    const log = html.indexOf('<section id="log">');
    const content = html.indexOf("SECRET-BODY-MARKER");
    const linkSec = html.indexOf("<h2>Link</h2>");
    expect(result).toBeGreaterThan(-1);
    expect(result).toBeLessThan(log); // outcome first
    expect(log).toBeLessThan(content); // log before summary content
    expect(content).toBeLessThan(linkSec); // link section last
    expect(html).toContain("last run"); // run metrics live in the overview now
    const actions = html.indexOf('class="actions"');
    expect(actions).toBeGreaterThan(result); // actions live inside the result…
    expect(actions).toBeLessThan(log); // …section, not down in the link card
    expect(html).toContain('id="result" class="st-summarized"'); // outcome tint hook
  });

  it("dismissed: hides the body but keeps metadata + re-open", () => {
    const html = renderLinkPage({ ...link, status: "dismissed" }, mkSummary({ status: "dismissed" }));
    expect(html).not.toContain("SECRET-BODY-MARKER");
    expect(html).toContain("hidden while dismissed");
    expect(html).toContain("re-open");
    expect(html).not.toContain("re-summarize");
    expect(html).toContain("L7");
  });

  it("blocked, no NNN: shows the escaped reason, retry, and no content section", () => {
    const html = renderLinkPage(
      { ...link, status: "blocked", summary_id: null, error: "PDF detected <fail-closed>" },
      null,
    );
    expect(html).toContain("PDF detected &lt;fail-closed&gt;");
    expect(html).not.toContain("<fail-closed>");
    expect(html).toContain("no NNN allocated");
    expect(html).not.toContain("Scores"); // no content section rendered
    expect(html).toContain("retry");
    expect(html).toContain('"summaryId":null'); // events filtered by link_id only
  });
});

describe("tokensFromUsage", () => {
  it("reads Gemini and Workers AI shapes", () => {
    expect(tokensFromUsage({ promptTokenCount: 10, candidatesTokenCount: 2 })).toEqual({ tokensIn: 10, tokensOut: 2 });
    expect(tokensFromUsage({ prompt_tokens: 5, completion_tokens: 1 })).toEqual({ tokensIn: 5, tokensOut: 1 });
    expect(tokensFromUsage(undefined)).toEqual({ tokensIn: null, tokensOut: null });
  });
});
