## Claude Skills でエージェントに専門的なタスクを実行させる

https://azukiazusa.dev/blog/claude-skills-custom-skills-for-claude/

Claude Skillsは、カスタムスキルを通じてClaudeエージェントの能力を拡張し、段階的なコンテキスト読み込み設計でコンテキストウィンドウの効率を大幅に向上させます。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Claude Skills, LLMエージェント, コンテキストウィンドウ最適化, Playwright, カスタムツール開発]]

記事は、Anthropicが新たに発表した「Claude Skills」機能について、その仕組み、作成方法、および従来のMCPツールとの違いを解説しています。Claude Skillsは、Code Execution Toolを活用してJavaScriptやPythonなどのコードを実行できるカスタムスキルをClaudeエージェントに提供するもので、これによりエージェントがより専門的かつ高度なタスクを実行できるようになると著者は述べています。

この機能の核心は、スキルの情報が段階的にClaudeに提供されるアーキテクチャです。具体的には、まずスキルの「name」と「description」が読み込まれ、Claudeがスキルを使用すると判断した場合にのみ、より詳細な「SKILL.md」ファイル本文や関連スクリプトがコンテキストに追加されます。著者はこの設計が、MCPツールで課題となっていたコンテキストウィンドウの圧迫とそれに伴うClaudeの性能低下を防ぐ上で極めて重要であると強調しています。コンテキストの最適化のため、「name」と「description」には文字数制限が設けられ、「SKILL.md」本文も500行以下に抑えることが推奨されています。

具体的なスキル作成例として、Playwrightとpdf-libを使用してウェブページのスクリーンショットをPDFに変換するスキルが紹介されており、そのための「SKILL.md」、スクリーンショット取得用のJavaScriptコード、PDF変換用のスクリプトの作成手順が詳細に解説されています。作成したスキルはZIPアーカイブとして圧縮し、Claudeアプリの設定画面からアップロードすることで利用可能になります。著者は、コード実行権限を伴うためセキュリティリスクに注意し、信頼できるコードのみを使用するよう警告しています。これにより、WebアプリケーションエンジニアはClaudeの機能を柔軟に拡張し、特定のワークフローに特化したエージェントを構築できるようになります。