## MCP: エージェント型AIシステムに潜むModel Context Protocolのセキュリティリスク

https://hiddenlayer.com/innovation-hub/mcp-model-context-pitfalls-in-an-agentic-world/

**Original Title**: MCP: Model Context Pitfalls in an Agentic World

HiddenLayerのセキュリティ研究チームがModel Context Protocol（MCP）の脆弱性を包括的に分析し、権限管理の不備・間接プロンプトインジェクション・ツール名タイポスクワッティングなどの深刻なリスクを実証した。

**Content Type**: 🔬 Research
**Language**: en

**Scores**: Signal:5/5 | Depth:5/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 95/100 | **Annex Potential**: 90/100 | **Overall**: 95/100

**Topics**: [[MCP, セキュリティ, プロンプトインジェクション, エージェントAI, 脆弱性研究]]

HiddenLayerのセキュリティ研究チームが、Anthropicが発表したModel Context Protocol（MCP）のセキュリティリスクを包括的に分析した。MCPは28のクライアント、20の参照サーバーを持ち、OpenAI Agent SDK、Microsoft Copilot Studio、Amazon Bedrock Agents、Cursor、VS Codeがサポートする急成長エコシステムである。

主要なセキュリティリスクとして、まず権限管理（Permission Management）の問題がある。多くの実装でユーザー承認が不明確・一貫性がなく、一度許可すると後続の危険な使用でも再確認されない。Claude Desktopでは最初のリクエストで許可された権限が後続リクエストにも適用され、Claude Codeでは「セッション中許可」オプションにより悪意あるプロンプトがファイル編集を悪用可能となる。

次に意図しない二重スパイ（Inadvertent Double Agents）として、サードパーティMCPサーバーの多くが任意コード実行を許可し、参照サーバー20個中16個が間接プロンプトインジェクションの影響を受ける。攻撃経路はWebサイト、共有ファイル、Slackメッセージ、コードベースのコメントなど多岐にわたる。

MCPサーバーの組み合わせ（Combinations）による攻撃では、税務書類に埋め込まれた間接プロンプトインジェクションの実証例が示された。fetchでドキュメント取得→filesystemで保存→分析時に悪意ある指示実行という流れで、追加権限なしでデスクトップファイルが漏洩した。

ツール名タイポスクワッティング（Tool Name TypoSquatting）では、MCPサーバー間でツール名を区別する仕組みがなく、同名ツールは後から読み込まれたものが優先される。悪意あるサーバーが正規ツール（例：push_files）をハイジャック可能で、リモートMCPサーバーは接続後にツール名を追加できるため遅延攻撃も可能。推奨事項としてOWASP Top 10 API Security Risksに基づくベストプラクティス、プロンプトインジェクション検出・ブロック機能の導入が挙げられている。
