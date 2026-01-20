## Vercel Agentのコードレビューがリポジトリ独自のガイドラインに準拠

https://vercel.com/changelog/vercel-agent-code-reviews-now-follow-your-code-guidelines

**Original Title**: Vercel Agent code reviews now follow your code guidelines

連携する設定ファイルを自動検出し、プロジェクト固有のコーディング規約に基づいたAIレビューをCI/CDプロセスで実現する。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:2/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 52/100 | **Annex Potential**: 50/100 | **Overall**: 72/100

**Topics**: [[Vercel, Vercel Agent, Code Review, .cursorrules, LLM Instructions]]

Vercelは、同社のAIエージェント機能「Vercel Agent」において、リポジトリ内のコーディングガイドラインを自動的に検出し、それに沿ったコードレビューを行う機能をリリースした。これまでAIによるコードレビューは汎用的なベストプラクティスに基づいたものが中心であったが、今回のアップデートにより、プロジェクト固有の命名規則やアーキテクチャ方針、特定のライブラリの使用制限といった「チーム独自の文脈」をレビューに反映させることが可能になった。

本機能の最大の特徴は、独自形式の `AGENTS.md` だけでなく、すでにエンジニアの間で普及している `CLAUDE.md`、`.cursorrules`、`.github/copilot-instructions.md` といった既存の設定ファイルを自動的に認識して適用する点にある。これにより、エンジニアはVercel Agent専用のルールを再定義する手間を省き、CursorやGitHub Copilotなどの開発ツール向けに整備していた指示書をそのままCI/CDプロセスでのレビュー品質向上に転用できる。

著者は、追加の設定なしにエージェントがコンテキストを理解し、適切なフィードバックを提供できる点を強調している。開発チームにとって、独自規約を逸脱したコードの早期発見が自動化されることは、人間によるレビュー負荷の軽減と、コードベース全体の一貫性維持に直結する。既存のAI開発ツール向け設定資産をそのまま活用できる、実用性の高いアップデートと言える。