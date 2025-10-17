## Chrome DevTools MCPを試してみた：Gemini CLIからGoogle Cloudをブラウザから操作する

https://zenn.dev/chishiro_shiro/articles/4dd51a9d3a2e6e

Chrome DevTools MCPがGemini CLIと連携し、Google Cloudコンソールを自然言語でブラウザから直接操作できる、AIによるタスク自動化の新たな境地を切り拓きます。

**Content Type**: Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[Chrome DevTools MCP, Gemini CLI, Google Cloud Automation, Browser Automation, AI in Operations]]

「Chrome DevTools MCP」は、AIがウェブブラウザを直接操作可能にする画期的なツールとして公開プレビューが開始されました。従来のAIコーディングアシスタントがコードエディタ内で完結していたのに対し、MCPはGemini CLIのようなAIに自然言語で指示を与えるだけで、Chromeブラウザを介した複雑なタスクを実行させます。これは、Seleniumのような自動操作をAIが日本語で解釈し実行するようなもので、ウェブアプリケーション開発者にとって、運用やテストのあり方を大きく変える可能性を秘めています。

筆者はGemini CLIとMCPを組み合わせ、Google CloudコンソールでCloud Runサービスの作成や、公式ドキュメントに従ったCloud Storageバケットの作成を自動実行できることを実証しました。特筆すべきは、AIが曖昧な指示でも意図を汲み取り、また詳細な手順書通りに正確に操作できる点です。

この技術が重要である理由は、主に以下の3点です。第一に、開発者はこれまで手動で行っていたブラウザ上の操作（例：クラウドサービスのデプロイ、設定変更、パフォーマンス分析データ収集）を、自然言語の指示で自動化できるようになります。これにより、日々の運用タスクの効率が飛躍的に向上します。第二に、AIがドキュメントを読み込んでタスクを実行する「ドキュメント駆動開発」の次世代形を提示します。AIが迷わないよう、より明確で曖昧さのない手順書の作成が求められる時代が到来し、ドキュメントの品質が直接生産性に影響します。第三に、フロントエンド開発において、UIテストの自動化やパフォーマンス分析の取得、さらにはスクリーンショットの自動生成など、手作業の多いプロセスをAIが代替する道を開きます。

Chrome DevTools MCPはまだプレビュー版ですが、AIによるブラウザ操作が当たり前になる「映画のような」未来の片鱗を示しており、ウェブアプリケーション開発における自動化と生産性の可能性を大きく広げるでしょう。