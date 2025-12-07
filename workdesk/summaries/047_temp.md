## GitHub Copilotにカスタムエージェントを導入：可観測性、IaC、セキュリティにおけるチームのルールを適用

https://github.blog/news-insights/product-news/your-stack-your-rules-introducing-custom-agents-in-github-copilot-for-observability-iac-and-security/

**Original Title**: Your stack, your rules: Introducing custom agents in GitHub Copilot for observability, IaC, and security

GitHub Copilotは、可観測性、IaC、セキュリティといった分野でチーム独自のルールやツールを統合するカスタムエージェントを導入し、開発ワークフロー全体を強化します。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[GitHub Copilot, カスタムエージェント, 可観測性, IaC, セキュリティ]]

GitHub Copilotが、開発チームが日々のワークフローで利用する多様なツールや標準を統合する「カスタムエージェント」の提供を開始しました。これは、Copilotが単にコード作成を支援するだけでなく、ソフトウェア開発ライフサイクル全体を管理できるよう機能を拡張するものです。

カスタムエージェントは、Markdown形式で定義されるドメインエキスパートであり、既存のCopilotコーディングエージェントの機能を拡張します。例えば、JFrogのセキュリティアナリスト、PagerDutyのインシデント対応者、MongoDBのデータベースパフォ​​ーマンススペシャリストといった役割を果たすことができます。これにより、開発者はTerraformモジュールの構造、信頼するダッシュボード、データベースの移行ルールなど、チーム固有の慣習や規則をCopilotに組み込むことが可能になります。

これらのエージェントは、Copilot CLI、VS CodeのCopilot Chat、github.comのCopilotパネルといった、Copilotが利用可能なあらゆる場所で機能します。エージェントはリポジトリの`.github/agents/`ディレクトリにMarkdownファイルとして追加するだけで、すぐに利用でき、組織やエンタープライズレベルでの定義も可能です。

GitHubは、Dynatrace、JFrog、MongoDB、Neon、PagerDutyなど、幅広いパートナー企業と協力してカスタムエージェントのエコシステムを構築しています。これにより、以下のような具体的な開発ワークフローをCopilotを通じて実行できます。

*   **インシデント対応**: PagerDutyエージェントがアクティブなインシデントの概要と次の調査ステップを提案。
*   **セキュリティ強化**: JFrogセキュリティエージェントが脆弱な依存関係をスキャンし、安全なアップグレードパスを提供。
*   **データベース管理**: Neon移行スペシャリストがスキーマ移行の安全性とベストプラクティスをレビュー。
*   **プロダクト実験**: Amplitude実験実装エージェントがA/Bテストの統合やトラッキングイベントの生成を支援。

著者は、カスタムエージェントが重要である理由として、チームのパターン（Terraformの慣習、データベースルール、セキュリティ標準など）を一貫して維持できること、コンテキストの繰り返しを避け、期待値を一度定義して再利用できること、専門知識を自動的に共有しチーム全体でベストプラクティスを遵守できること、そしてModel Context Protocol (MCP)サーバーを使用してDevOps、セキュリティ、可観測性システムから直接データを引き出し、既存のツールと深く連携できることを挙げています。

この機能により、Copilotは「コードを書くのを手伝う」から「チームがソフトウェアを構築する方法でソフトウェアを構築するのを手伝う」へと進化します。カスタムエージェントは全てのGitHub Copilotユーザーが利用可能であり、`copilot --agent=<agent-name> --prompt "<task>"`コマンドで簡単に試すことができます。