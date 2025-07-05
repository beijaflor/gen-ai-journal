## [LangGraphを使ったGemini Deep Search MCPサーバを作ってClaude Codeから呼び出す](https://qiita.com/zawatti/items/48046809f41d20f99cfc?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items)

**ClaudeがGeminiの頭脳で深く探る！LangGraph製Deep Searchサーバー構築術**

本記事では、AIエージェント「Claude Code」の検索能力を強化するため、GoogleのGeminiとLangGraphを利用した「Deep Search MCPサーバ」の構築方法が紹介されています。公式のDeepSearchプロジェクトを基に、FastMCPを介して外部エージェントから呼び出せるように調整されています。

著者は実際にこのサーバをClaude Codeに接続し、競合ツールである「Gemini-CLI」や「Codex CLI」について詳細な調査を行わせるデモンストレーションを実施。内部で多数の検索と生���を繰り返すため、レスポンスに1分以上かかるものの、非常に詳細なレポートが生成されることが確認されました。

この試みは、AIエージェントが持つ能力の限界を、特化した外部ツール（MCPサーバ）を連携させることで補い、より高度なタスクを実現できる可能性を示しています。今後のAI開発において、エージェント同士をツールとして呼び出し合うアーキテクチャの重要性を提示する内容です。