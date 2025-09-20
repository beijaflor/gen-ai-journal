## Codex CLIにClaude Codeから手軽に設定を移行する方法

https://zenn.dev/karaage0703/articles/aabaa01cb71647

本記事は、Claude CodeからCodex CLIへMCPサーバー設定やスラッシュコマンドを効率的に移行する方法を、自作ツール`ccmcp`や`mmcp`を活用して解説します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 92/100 | **Annex Potential**: 93/100 | **Overall**: 92/100

**Topics**: [[AIコーディングアシスタント, Codex CLI, Claude Code, MCP, 開発環境構築]]

記事は、人気が高まるCodex CLIへClaude Codeから設定を効率的に移行する具体的な手順を提供します。これは、GPT-5の登場や既存ツールの変化に伴い、複数のAIコーディングアシスタントを併用したり、将来的に乗り換えを検討しているWebアプリケーションエンジニアにとって非常に重要な情報です。特に、MCP（Model Context Protocol）サーバー設定の移行は、Claude CodeがJSON形式、Codex CLIがTOML形式と異なるため手間がかかります。本記事では、この課題に対し、著者自身が開発した`ccmcp`と、複数のAIエージェント設定を一元管理できる`mmcp`という革新的なツールを活用する実践的な方法を提示します。

具体的には、`npm install`コマンドでこれらのツールを導入後、`ccmcp export-to-mmcp`と`mmcp apply`を実行するだけで、複雑なMCPサーバー設定が効率的に同期されます。このアプローチは、ベンダー固有の機能に過度に依存せず、MCPのようなオープンな規格を利用することで、開発環境の柔軟性を確保し、将来的なAIエージェント間の移行コストを大幅に削減できるという重要な示唆を与えています。さらに、日々の開発に欠かせないスラッシュコマンドの移行方法（`~/.claude/commands`から`~/.codex/prompts`へのコピー）や、Codex CLIがスラッシュコマンドのサブディレクトリ構造に未対応であるといった具体的な注意点も解説されており、開発者が直面する細かな課題に対する実践的な解決策を提示します。この記事は、AIエージェント間の相互運用性を高め、変化の速いAI開発ツール環境下で、効率的かつポータブルな開発ワークフロー構築に貢献するでしょう。