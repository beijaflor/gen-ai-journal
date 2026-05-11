## GLM Coding Plan入門 〜APIキー取得からopencodeやClaude Codeを駆動するまで〜

https://zenn.dev/robustonian/articles/glm_coding_plan

高性能なGLM-4.7モデルを安価に利用できるGLM Coding Planを導入し、opencodeやClaude Codeから呼び出すための環境構築手順を解説する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 100/100 | **Overall**: 80/100

**Topics**: [[GLM-4.7, Claude Code, opencode, AI Agent, LLM Pricing]]

本書は、コーディング性能の高さが話題の**GLM-4.7**を、年額約26ドルという破格のコストで利用可能にする「**GLM Coding Plan**」の導入手順を解説したガイドです。APIキーの取得方法から、オープンソースのエージェントツール**opencode**のセットアップ、さらに話題の**Claude Code**のバックエンドとしてGLMを駆動させるための具体的な設定ファイルを公開しています。

技術的なハイライトは、**Claude Code**の設定ファイル（`~/.claude/settings.json`）を編集し、**ANTHROPIC_BASE_URL**をZ.aiのプロキシエンドポイントへ向ける手法です。これにより、**Claude Code**特有の**AskUserQuestionTool**といったエージェント機能を活用しながら、裏側のモデルのみをGLMへと差し替えることが可能になります。また、記事ではシェル（.zshrc/.bashrc）の**alias**機能を使い、環境変数を動的に注入することで、標準の**Claude**と**GLM**を即座に切り替えて起動する実用的な運用 Tips も紹介されています。

サブスクリプションのコストを最適化しつつ、エージェントワークフローにおいて**Claude 3.5 Sonnet**に匹敵する性能を試したい、Webアプリケーションエンジニアにとって必読の導入資料といえます。