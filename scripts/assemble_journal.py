#!/usr/bin/env python3
"""
Assemble the weekly Gen AI journal from curated sources and summaries.
Ensures proper UTF-8 encoding for Japanese text.
"""
import re
from pathlib import Path

def extract_summary_by_url(unified_summaries_path: Path, target_url: str) -> str:
    """Extract a single summary by URL from the unified summaries file."""
    content = unified_summaries_path.read_text(encoding='utf-8')

    # Find the summary block for this URL
    # Format: ## Title\n\nURL\n\n**Original Title**: ...\n\nSummary content...\n\n---\n\n
    # We want to extract from URL line to the final "---" or end of summary
    pattern = r'##\s+([^\n]+)\n\n' + re.escape(target_url) + r'\n\n(.*?)(?=\n---\n\n##|\Z)'
    match = re.search(pattern, content, re.DOTALL)

    if match:
        title = match.group(1).strip()
        full_content = match.group(2).strip()

        # Extract only the actual summary - skip metadata lines
        # Skip lines that start with **Original Title**, **Content Type**, **Language**, **Scores**, **Topics**
        lines = full_content.split('\n')
        summary_lines = []
        skip_metadata = True

        for line in lines:
            # Skip metadata lines
            if line.startswith('**Original Title**:') or line.startswith('**Content Type**:') or \
               line.startswith('**Language**:') or line.startswith('**Scores**:') or \
               line.startswith('**Topics**:') or line.startswith('**Main Journal**:'):
                continue
            # After first blank line or non-metadata line, start capturing
            if not line.startswith('**') or skip_metadata == False:
                skip_metadata = False
                summary_lines.append(line)

        summary_content = '\n'.join(summary_lines).strip()
        return f"### {title}\n\n{target_url}\n\n{summary_content}\n\n---\n"
    else:
        return f"### [Summary not found]\n\n{target_url}\n\n[Summary could not be extracted for: {target_url}]\n\n---\n"

def main():
    base_path = Path("/Users/shootani/Dropbox/github/gen-ai-journal")

    # Read curated sources
    curated_main = (base_path / "workdesk/curated_journal_sources.md").read_text(encoding='utf-8')
    curated_annex = (base_path / "workdesk/curated_annex_journal_sources.md").read_text(encoding='utf-8')

    # Read unified summaries
    unified_main_path = base_path / "workdesk/unified_summaries_main.md"
    unified_annex_path = base_path / "workdesk/unified_summaries_annex.md"

    # Extract URLs from curated sources
    url_pattern = r'- \[ \] (https://[^\s]+)'

    main_urls = re.findall(url_pattern, curated_main)
    annex_urls_with_comments = re.findall(
        r'- \[ \] (https://[^\s]+)\n<!--\s*([^→]+)(?:→\n)?([^→]+)-->',
        curated_annex,
        re.MULTILINE
    )

    print(f"Found {len(main_urls)} main URLs")
    print(f"Found {len(annex_urls_with_comments)} annex URLs with comments")

    # Build main journal
    main_journal = """# GenAI週刊 2025年12月20日号

今週のAI・コーディング関連の重要な動向をお届けします。

## 今週のハイライト

2025年も師走に入り、AIコーディングツールの世界は大きな転換点を迎えています。今週の22の記事を通じて見えてくるのは、**ツールの進化から設計思想の成熟へ**という明確なシフトです。

まず目を引くのは、「仕様書駆動開発」という新しいパラダイムの台頭です。cc-sdd、OpenSpec、spec-kitといったツールが登場し、AIと協働するための「仕様ファースト」の開発手法が確立されつつあります。これはVibe Codingの限界を乗り越え、「考えてから作る」という本質に立ち返る動きと言えるでしょう。初心者が生成AIをどう活用すべきかという根本的な問いに対する、ベテランプログラマの実践的な回答がここにあります。

次に、MCPエコシステムの成熟が際立っています。AnthropicのMCPが登場してわずか数週間で、WorkOSのOAuth+CIMD統合による企業レベルのセキュリティ実装や、Web APIをMCP Gateway化する実践的なアーキテクチャが登場しました。これは単なるツールの追加ではなく、AIエージェントが信頼できるインフラとして企業システムに統合される未来の到来を意味します。

そして、PerplexityやNotebookLMのような成功例から学ぶ「インテリジェンス・フロー・アーキテクチャ」の重要性、ChatGPTのUI崩壊パターンから見えるUX設計の難しさ。これらの知見は、AIプロダクトにおけるUXデザイナーの役割が「オプション」ではなく「必須」であることを示しています。そして、デザイナーだけでなく、エンジニアも「仕様を考える人」へと役割が進化する中で、私たちの働き方の本質が問われています。

## 1. AIコーディングエージェントの本質的学び

"""

    # Process main journal themes
    theme_sections = {
        "Theme 1: AIコーディングエージェントの本質的学び": "## 1. AIコーディングエージェントの本質的学び\n\n",
        "Theme 2: 仕様駆動開発とツール": "## 2. 仕様駆動開発とツール\n\n",
        "Theme 3: MCPとAIエージェントインフラ": "## 3. MCPとAIエージェントインフラ\n\n",
        "Theme 4: プロダクト設計とUX": "## 4. プロダクト設計とUX\n\n",
        "Theme 5: 最新モデルとツールのアップデート": "## 5. 最新モデルとツールのアップデート\n\n"
    }

    current_theme = None
    theme_content = {theme: [] for theme in theme_sections.keys()}

    for line in curated_main.split('\n'):
        if line.startswith('## Theme'):
            current_theme = line.strip('# ').strip()
        elif line.startswith('- [ ]') and current_theme:
            url = line.split('](')[0].split('(')[-1] if '(' in line else line.split()[-1]
            summary = extract_summary_by_url(unified_main_path, url)
            theme_content[current_theme].append(summary)

    # Rebuild main journal with proper structure
    main_journal = """# GenAI週刊 2025年12月20日号

今週のAI・コーディング関連の重要な動向をお届けします。

## 今週のハイライト

2025年も師走に入り、AIコーディングツールの世界は大きな転換点を迎えています。今週の22の記事を通じて見えてくるのは、**ツールの進化から設計思想の成熟へ**という明確なシフトです。

まず目を引くのは、「仕様書駆動開発」という新しいパラダイムの台頭です。cc-sdd、OpenSpec、spec-kitといったツールが登場し、AIと協働するための「仕様ファースト」の開発手法が確立されつつあります。これはVibe Codingの限界を乗り越え、「考えてから作る」という本質に立ち返る動きと言えるでしょう。初心者が生成AIをどう活用すべきかという根本的な問いに対する、ベテランプログラマの実践的な回答がここにあります。

次に、MCPエコシステムの成熟が際立っています。AnthropicのMCPが登場してわずか数週間で、WorkOSのOAuth+CIMD統合による企業レベルのセキュリティ実装や、Web APIをMCP Gateway化する実践的なアーキテクチャが登場しました。これは単なるツールの追加ではなく、AIエージェントが信頼できるインフラとして企業システムに統合される未来の到来を意味します。

そして、PerplexityやNotebookLMのような成功例から学ぶ「インテリジェンス・フロー・アーキテクチャ」の重要性、ChatGPTのUI崩壊パターンから見えるUX設計の難しさ。これらの知見は、AIプロダクトにおけるUXデザイナーの役割が「オプション」ではなく「必須」であることを示しています。そして、デザイナーだけでなく、エンジニアも「仕様を考える人」へと役割が進化する中で、私たちの働き方の本質が問われています。

"""

    for theme_key, section_header in theme_sections.items():
        main_journal += section_header
        if theme_key in theme_content:
            main_journal += '\n'.join(theme_content[theme_key])
        main_journal += '\n'

    main_journal += """
## おわりに

今週の記事から浮かび上がるのは、AIツールが「どう使うか」から「何を作るべきか」を考えるフェーズへ移行しているという現実です。仕様書駆動開発、MCP統合、UX設計の重視——これらはすべて、AIを単なる「コーディング高速化ツール」として使う段階を超え、組織的な開発文化の一部として組み込む動きです。

そして、この変化の中で最も重要なのは、人間の役割が「コードを書く人」から「設計を考える人」へとシフトしていることです。AIが実装を担う時代において、私たちエンジニアの価値は「Why」と「What」を明確に定義できる能力にあります。来週も、この変革の最前線からの知見をお届けします。

---

*本レポートはClaude Code (Sonnet 4.5) を使用して編集されました。*
"""

    # Write main journal with UTF-8 encoding
    (base_path / "workdesk/weekly_journal_2025_12_20.md").write_text(main_journal, encoding='utf-8')
    print("✓ Created weekly_journal_2025_12_20.md")

    # Build annex journal
    annex_journal = """# GenAI週刊 別冊 2025年12月20日号

今週の「B面」から選んだユニークな視点とニッチな探求をお届けします。

## 別冊について

メインの週刊誌では、広く実践的価値を持つ必読記事を厳選してお届けしています。しかし、AI・コーディングの世界には、もっとニッチで、もっと尖った、しかし同じくらい価値のある洞察が数多く存在します。

この別冊「Annex」は、そうした「B面」の記事を集めたコレクションです。高度な戦術と非自明な知見、実質的な批評と対抗視点、ニッチな探求と深掘り——メインストリームではないかもしれませんが、特定の文脈では誰よりも早く気づくべき情報がここにあります。Annexは単なる「おまけ」ではなく、むしろ3ヶ月後や半年後に「あの時読んでおいてよかった」と思える種類の記事を集めた、もうひとつのキュレーションです。

## 高度な戦術と非自明な知見

"""

    # Process annex journal themes
    annex_themes = {
        "Advanced Tactics & Unconventional Wisdom (高度な戦術と非自明な知見)": "## 高度な戦術と非自明な知見\n\n",
        "Substantive Critique & Contrarian Views (実質的批評と対抗視点)": "## 実質的批評と対抗視点\n\n",
        "Niche Explorations & Deep Dives (ニッチな探求と深掘り)": "## ニッチな探求と深掘り\n\n"
    }

    current_annex_theme = None
    annex_theme_content = {theme: [] for theme in annex_themes.keys()}

    annex_lines = curated_annex.split('\n')
    i = 0
    while i < len(annex_lines):
        line = annex_lines[i]

        if line.startswith('## '):
            current_annex_theme = line.strip('# ').strip()
            i += 1
            continue

        if line.startswith('- [ ]') and current_annex_theme:
            url = line.split()[-1]
            # Next line should be comment start
            if i + 1 < len(annex_lines) and annex_lines[i + 1].startswith('<!--'):
                # Extract comment (may span multiple lines)
                comment_lines = []
                j = i + 1
                while j < len(annex_lines) and not annex_lines[j].strip().endswith('-->'):
                    comment_lines.append(annex_lines[j])
                    j += 1
                if j < len(annex_lines):
                    comment_lines.append(annex_lines[j])

                comment_text = '\n'.join(comment_lines)
                # Extract the actual comment content (remove <!-- --> and split on arrow)
                comment_content = re.sub(r'<!--\s*', '', comment_text)
                comment_content = re.sub(r'\s*-->', '', comment_content)
                parts = comment_content.split('→\n', 1)
                if len(parts) == 2:
                    editor_comment = parts[1].strip()
                else:
                    editor_comment = comment_content.strip()

                summary = extract_summary_by_url(unified_annex_path, url)
                # Insert editorial comment before summary content
                summary_with_comment = summary.replace(f"{url}\n\n", f"{url}\n\n**編集者より**: {editor_comment}\n\n")
                annex_theme_content[current_annex_theme].append(summary_with_comment)

                i = j + 1
                continue

        i += 1

    # Rebuild annex journal
    annex_journal = """# GenAI週刊 別冊 2025年12月20日号

今週の「B面」から選んだユニークな視点とニッチな探求をお届けします。

## 別冊について

メインの週刊誌では、広く実践的価値を持つ必読記事を厳選してお届けしています。しかし、AI・コーディングの世界には、もっとニッチで、もっと尖った、しかし同じくらい価値のある洞察が数多く存在します。

この別冊「Annex」は、そうした「B面」の記事を集めたコレクションです。高度な戦術と非自明な知見、実質的な批評と対抗視点、ニッチな探求と深掘り——メインストリームではないかもしれませんが、特定の文脈では誰よりも早く気づくべき情報がここにあります。Annexは単なる「おまけ」ではなく、むしろ3ヶ月後や半年後に「あの時読んでおいてよかった」と思える種類の記事を集めた、もうひとつのキュレーションです。

"""

    for theme_key, section_header in annex_themes.items():
        annex_journal += section_header
        if theme_key in annex_theme_content:
            annex_journal += '\n'.join(annex_theme_content[theme_key])
        annex_journal += '\n'

    annex_journal += """
## おわりに

この別冊で紹介した18の記事は、それぞれが「主流」ではないかもしれませんが、深く考えさせられる洞察を持っています。Claude CodeのAgent Skillsという仕組みの本質、Devinとの協業パターン、医療業界でのLLM活用、AIエージェントの「夜間運用」という発想——これらは今すぐ全員に必要な知識ではないかもしれませんが、特定の課題に直面したとき、あるいは一歩先を見据えたいとき、確実に価値を発揮する種類の知見です。

「読んでおいてよかった」と思える記事が、この中にひとつでもあれば幸いです。次回の別冊もお楽しみに。

---

*本レポートはClaude Code (Sonnet 4.5) を使用して編集されました。*
"""

    # Write annex journal with UTF-8 encoding
    (base_path / "workdesk/annex_journal_2025_12_20.md").write_text(annex_journal, encoding='utf-8')
    print("✓ Created annex_journal_2025_12_20.md")

if __name__ == "__main__":
    main()
