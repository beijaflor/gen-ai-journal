## Claude Codeと自身の脳を繋ぐ、ナレッジ管理CLIツールによるMCPサーバー接続Kush🧠

https://zenn.dev/boykush/articles/1aa8848b23f09a

CLIツール「Scraps」がClaude CodeとのMCPサーバー連携を実装し、ユーザーの個人ナレッジをLLMに統合して開発サイクルでの効率的な情報活用を可能にしました。

**Content Type**: ⚙️ Tools
**Scores**: Signal:4/5 | Depth:4/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 90/100 | **Annex Potential**: 90/100 | **Overall**: 88/100

**Topics**: [[Generative AI, Knowledge Management, CLI Tools, LLM Agents, Claude Code, MCP Server]]

この記事は、CLIツール「Scraps」がClaude CodeとのMCP（Micro-Context Protocol）サーバー連携を実装し、開発者が自身のマークダウン形式のナレッジをLLM（大規模言語モデル）に統合する画期的な方法を紹介しています。これは、ウェブアプリケーションエンジニアが個人で蓄積した技術的な知見を、より効率的かつ正確にコーディング作業や問題解決に活用できるという点で非常に重要です。

Scrapsの新しいMCPサーバー機能は、`scraps mcp serve`コマンドでローカルのマークダウンファイルを指定するだけでClaude Codeからアクセス可能になります。提供される`search_scraps`（タイトル曖昧検索）や`lookup_scrap_backlinks`（内部リンク一覧取得）といった5種類のツール群は、マークダウンコンテンツ自体を返却するため、LLMは精度の高い情報を直接参照できます。これにより、ウェブ検索に頼らず、ユーザー自身の文脈に深く根差した回答が得られるようになります。

具体的な利用例として、BDD（振る舞い駆動開発）の導入方法をScraps内のナレッジからまとめてもらうケースが示されています。Claude CodeはScrapsツールを複数回呼び出し、体系的なBDD導入ガイドを生成。さらに、自身のナレッジを反映したサブエージェント「personal-knowledge-assistant」を作成し、LLMが「もう一人の自分」として学習履歴を分析し、次に学ぶべき分野を提案するデモンストレーションは、個人ナレッジをAIに拡張する可能性を強く示唆しています。

このアプローチは、Obsidianなどの既存ツールと比較して軽量であり、既存のマークダウン資産をすぐに活用できる点が強みです。エンジニアは、自身の「脳」（ナレッジ）をLLMへ拡張として挿し込むことで、日々の開発業務における情報収集、思考、意思決定プロセスを劇的に改善できるでしょう。