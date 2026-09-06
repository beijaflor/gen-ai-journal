"""Tests for check_summary_format.lint_body / check_path."""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_summary_format import check_path, lint_body  # noqa: E402


def test_clean_body_has_no_defects():
    body = (
        "本記事は分析である。3つの時代に分けて検証している。\n\n"
        "- **初期**: 説明。\n"
        "- **推論**: 説明。\n\n"
        "結論として、傾向が確認された。"
    )
    assert lint_body(body) == []


def test_line_start_headings_are_allowed():
    # A body that uses ### headings with real line breaks renders fine.
    body = "### 検証の概要\n\n本文が続く。\n\n### 主な結果\n\n- **項目**: 説明。"
    assert lint_body(body) == []


def test_plain_prose_one_line_is_clean():
    body = "これは普通の一文の要約で、マークダウン構造を含まないため問題ない。"
    assert lint_body(body) == []


def test_escaped_newline_flagged():
    body = "## 概要\\nApple Silicon で検証。\\n\\n## 結果\\n- **速度**: 速い。"
    assert "escaped-newline" in lint_body(body)


def test_single_prose_mention_of_backslash_n_not_flagged():
    # One incidental mention of \n in prose should not trip the escaped check.
    body = "改行コード \\n をテキストに挿入する方法を、実例とともに丁寧に解説した記事。"
    assert "escaped-newline" not in lint_body(body)


def test_mashed_single_line_flagged():
    body = "### 概要 本文が続く 1. **項目**: 説明 2. **項目**: 説明 結論。"  # no newline
    assert lint_body(body) == ["mashed-single-line"]


def test_mashed_numbered_bold_list_without_header():
    body = "導入文。 1. **A**: 説明。 2. **B**: 説明。"  # numbered-bold list, one line
    assert "mashed-single-line" in lint_body(body)


def test_inline_header_mid_line_flagged():
    # A header jammed after text on a line that DOES have other real newlines.
    body = "導入の段落。\n本文 ### 見出し がここに紛れている。\n結び。"
    assert "inline-header" in lint_body(body)


def test_csharp_prose_not_flagged_as_header():
    body = "C# と F# を比較する記事。\n実務での使い分けを解説している。"
    assert lint_body(body) == []


def _write(dirpath, name, body):
    doc = {"content": {"summaryBody": body}}
    with open(os.path.join(dirpath, name), "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False)


def test_check_path_counts_and_skips_non_json(tmp_path):
    d = str(tmp_path)
    _write(d, "001_ok.json", "きれいな要約。構造なし。")
    _write(d, "002_bad.json", "### 見出し 本文 1. **項目**: 説明")  # mashed
    # a non-JSON stub (e.g. BLOCKED) must be skipped, not crash or counted
    with open(os.path.join(d, "003_blocked.txt"), "w", encoding="utf-8") as f:
        f.write("BLOCKED: fetch failed")
    total, n_flagged, flagged = check_path(d)
    assert total == 2  # only the two .json parsed
    assert n_flagged == 1
    assert flagged[0][0].endswith("002_bad.json")
