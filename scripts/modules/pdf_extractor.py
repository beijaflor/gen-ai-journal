"""PDF text extraction with fail-closed quality gating.

Issue #141: When the HTML pipeline mishandles a PDF, the LLM ends up
fabricating a summary from the URL slug. The fix splits PDF handling
into its own pipeline:

  download -> extract via pypdf -> verify quality -> hand to call-gemini

This module owns the middle three steps. ``call-gemini.py`` (and the
``summarize-pdf`` skill) consume the high-level API:

  ``extract_pdf_from_url(url, dest_dir) -> ExtractionResult``

The result carries either a successful ``text`` payload + ``metrics``,
or a structured ``error`` describing why extraction was refused. Callers
MUST check ``result.ok`` and surface a blocked-stub on failure — that is
the "never allow generation from filename, URL slug, or partial binary
artifacts" guarantee from the issue's outside review.
"""

from __future__ import annotations

import logging
import os
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


# Quality thresholds. Tuned conservatively: a 1-page PDF that yields
# fewer than ~200 chars is almost certainly an image-only scan or a
# corrupted download. The full-document threshold catches the case
# where pypdf produced a handful of glyphs across many pages (a typical
# failure mode for PDFs whose text layer is encoded with custom CMaps).
PDF_MIN_TOTAL_CHARS = 400
PDF_MIN_CHARS_PER_NONEMPTY_PAGE = 50

# Maximum chars sent to Gemini in one prompt. Gemini-3-flash-preview can
# accept much more, but our prompts also include the schema description,
# the editorial persona, and the scoring framework — keeping the article
# body bounded keeps the round-trip cheap and well within the context
# window. When a PDF exceeds this, we truncate to the first N pages and
# annotate the truncation in metrics so the editor can audit.
PDF_MAX_CHARS = 60_000


@dataclass(frozen=True)
class PdfMetrics:
    """Per-extraction quality signals, recorded for audit."""

    page_count: int
    used_page_count: int
    total_chars: int
    raw_bytes: int
    truncated: bool
    nonempty_pages: int

    def describe(self) -> str:
        """Human-readable one-liner for stderr / report blocks."""
        return (
            f"{self.page_count} pages, used {self.used_page_count}, "
            f"{self.total_chars} chars from {self.raw_bytes} bytes "
            f"(nonempty pages: {self.nonempty_pages}"
            + (", truncated" if self.truncated else "")
            + ")"
        )


@dataclass
class ExtractionResult:
    """Outcome of an end-to-end PDF extraction.

    On success: ``ok=True``, ``text`` populated, ``metrics`` populated.
    On failure: ``ok=False``, ``error`` populated with a reason.
    The temp file is cleaned up by ``extract_pdf_from_url`` before return,
    so callers don't have to manage it. ``metrics`` may be populated
    even on failure (e.g. successful download but failed extraction).
    """

    ok: bool
    text: str = ""
    metrics: Optional[PdfMetrics] = None
    error: str = ""
    raw_bytes: int = 0


def download_pdf(url: str, dest_path: str, timeout: int = 120) -> Tuple[bool, str, int]:
    """Download ``url`` to ``dest_path`` via curl.

    Returns ``(ok, error_message, byte_count)``. The byte count is 0 on
    failure. We use curl rather than ``requests`` for the same HTTP/2
    + Connection-header reasons documented in ``call-gemini.py``.
    """
    try:
        result = subprocess.run(
            [
                "curl",
                "-sL",
                "--max-time",
                str(timeout),
                "-A",
                (
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
                ),
                "-o",
                dest_path,
                url,
            ],
            capture_output=True,
            text=True,
            timeout=timeout + 10,
        )
    except subprocess.TimeoutExpired:
        return False, f"download timed out after {timeout}s", 0
    except Exception as exc:  # noqa: BLE001
        return False, f"download failed: {exc}", 0

    if result.returncode != 0:
        return (
            False,
            f"curl exit {result.returncode}: {result.stderr.strip()[:200]}",
            0,
        )

    try:
        size = os.path.getsize(dest_path)
    except OSError as exc:
        return False, f"could not stat downloaded file: {exc}", 0

    if size == 0:
        return False, "downloaded file is empty", 0

    return True, "", size


def _extract_text_from_local_pdf(
    path: str, max_pages: Optional[int] = None
) -> Tuple[List[str], int]:
    """Run pypdf via a subprocess to keep the import optional.

    Returns ``(per_page_text, total_page_count)``. ``per_page_text`` only
    contains the pages we actually extracted (capped at ``max_pages``);
    ``total_page_count`` reports the document's full length so callers
    can decide whether truncation happened.

    The subprocess is invoked via ``uv run --with pypdf`` so the
    dependency is added on-demand without bloating the project's
    pyproject.toml — the rest of the pipeline never imports pypdf, and
    the only consumer is this one helper. This matches the manual
    recipe documented in issue #141.
    """
    helper = (
        "import sys, json\n"
        "from pypdf import PdfReader\n"
        "path = sys.argv[1]\n"
        "limit = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2] else 0\n"
        "reader = PdfReader(path)\n"
        "total = len(reader.pages)\n"
        "pages_to_read = reader.pages if limit <= 0 else reader.pages[:limit]\n"
        "out = []\n"
        "for p in pages_to_read:\n"
        "    try:\n"
        "        out.append(p.extract_text() or '')\n"
        "    except Exception as exc:\n"
        "        out.append('')\n"
        "json.dump({'total': total, 'pages': out}, sys.stdout, ensure_ascii=False)\n"
    )

    cmd = [
        "uv",
        "run",
        "--with",
        "pypdf",
        "python3",
        "-c",
        helper,
        path,
        str(max_pages or 0),
    ]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=180,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"pypdf extraction timed out: {exc}") from exc

    if result.returncode != 0:
        raise RuntimeError(
            f"pypdf extraction failed (exit {result.returncode}): "
            f"{result.stderr.strip()[:300]}"
        )

    try:
        import json

        payload = json.loads(result.stdout)
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(
            f"pypdf produced unparseable output: {exc}; first 200 chars: "
            f"{result.stdout[:200]!r}"
        ) from exc

    pages: List[str] = list(payload.get("pages", []))
    total: int = int(payload.get("total", 0))
    return pages, total


def _join_pages(pages: List[str]) -> str:
    """Join per-page text with form-feed separators that survive Gemini's prompt.

    We use literal newlines (not \f) because some templates strip control
    characters. Two blank lines per page boundary is enough for the LLM
    to recognise structural breaks without ballooning the prompt.
    """
    return "\n\n".join(page.strip() for page in pages if page is not None)


def _truncate_to_char_budget(pages: List[str], char_budget: int) -> Tuple[List[str], bool]:
    """Keep only as many leading pages as fit under ``char_budget``."""
    used: List[str] = []
    running = 0
    for page in pages:
        page_len = len(page) + 2  # account for the blank-line separator
        if used and running + page_len > char_budget:
            return used, True
        used.append(page)
        running += page_len
    return used, False


def extract_pdf_from_url(
    url: str,
    dest_dir: Optional[str] = None,
    pages: Optional[int] = None,
    timeout: int = 120,
) -> ExtractionResult:
    """Download ``url``, extract text, verify quality.

    ``pages`` optionally caps the number of pages read from the document
    (front-matter mode for huge reports like the Stanford HAI Index).
    When omitted, all pages are read but the final string is truncated
    to ``PDF_MAX_CHARS`` so the prompt stays bounded.

    The returned result is fail-closed: if extraction produces less than
    ``PDF_MIN_TOTAL_CHARS`` of text, ``ok`` is False and the caller MUST
    emit a blocked stub rather than continue to the LLM.
    """
    dest_dir = dest_dir or os.path.join(os.getcwd(), ".playwright-mcp")
    try:
        os.makedirs(dest_dir, exist_ok=True)
    except OSError as exc:
        return ExtractionResult(ok=False, error=f"cannot create dest dir {dest_dir}: {exc}")

    with tempfile.NamedTemporaryFile(
        prefix="pdf_", suffix=".pdf", dir=dest_dir, delete=False
    ) as tmp:
        tmp_path = tmp.name

    try:
        ok, err, raw_bytes = download_pdf(url, tmp_path, timeout=timeout)
        if not ok:
            return ExtractionResult(ok=False, error=err, raw_bytes=raw_bytes)

        try:
            per_page, total_pages = _extract_text_from_local_pdf(tmp_path, max_pages=pages)
        except RuntimeError as exc:
            return ExtractionResult(
                ok=False,
                error=str(exc),
                raw_bytes=raw_bytes,
            )

        nonempty_pages = sum(1 for p in per_page if len(p.strip()) >= PDF_MIN_CHARS_PER_NONEMPTY_PAGE)
        used_pages, truncated = _truncate_to_char_budget(per_page, PDF_MAX_CHARS)
        text = _join_pages(used_pages)
        metrics = PdfMetrics(
            page_count=total_pages,
            used_page_count=len(used_pages),
            total_chars=len(text),
            raw_bytes=raw_bytes,
            truncated=truncated or (pages is not None and pages < total_pages),
            nonempty_pages=nonempty_pages,
        )

        # Fail-closed quality gate. The thresholds here are the answer to
        # the issue's "never allow generation from filename, URL slug,
        # or partial binary artifacts" requirement.
        if metrics.total_chars < PDF_MIN_TOTAL_CHARS:
            return ExtractionResult(
                ok=False,
                metrics=metrics,
                raw_bytes=raw_bytes,
                error=(
                    f"extracted only {metrics.total_chars} chars from {total_pages}-page PDF "
                    f"({metrics.nonempty_pages} non-empty pages); "
                    "below PDF_MIN_TOTAL_CHARS threshold — likely scanned/image-only PDF"
                ),
            )

        if metrics.nonempty_pages == 0:
            return ExtractionResult(
                ok=False,
                metrics=metrics,
                raw_bytes=raw_bytes,
                error="no extractable text pages — likely scanned/image-only PDF",
            )

        return ExtractionResult(ok=True, text=text, metrics=metrics, raw_bytes=raw_bytes)
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass


def build_pdf_blocked_stub(
    url: str,
    reason: str,
    metrics: Optional[PdfMetrics],
    raw_bytes: int,
) -> str:
    """Render a blocked stub for a failed PDF extraction.

    Same shape as ``fetch_router.build_blocked_stub`` so downstream
    tooling (summary_review.py, the editor's eyeballs) treats them
    uniformly: first line is the ``BLOCKED:`` marker, body lists
    diagnostic counters.
    """
    metric_line = metrics.describe() if metrics else "no metrics captured"
    return (
        "BLOCKED: PDF summary suppressed — extraction did not meet the quality bar.\n"
        "\n"
        f"- URL: {url}\n"
        f"- Reason: {reason}\n"
        f"- Fetcher: pdf_extractor (pypdf)\n"
        f"- Raw bytes: {raw_bytes}\n"
        f"- Extraction metrics: {metric_line}\n"
        "\n"
        "This stub was emitted by scripts/modules/pdf_extractor.py to prevent\n"
        "the LLM from hallucinating a summary against an image-only / scanned\n"
        "PDF or a corrupted download. See Issue #141 for context.\n"
        "\n"
        "Action required: re-fetch this URL manually (OCR the PDF, snapshot\n"
        "a HTML rendering, or curate the URL out of the journal).\n"
    )


def _stderr(message: str) -> None:
    print(message, file=sys.stderr)


__all__ = [
    "ExtractionResult",
    "PdfMetrics",
    "PDF_MAX_CHARS",
    "PDF_MIN_TOTAL_CHARS",
    "build_pdf_blocked_stub",
    "download_pdf",
    "extract_pdf_from_url",
]
