## AIエージェントのためのブラウザ自動化インフラ「Vibium」

https://github.com/VibiumDev/vibium

**Original Title**: Browser automation for AI agents and humans

AIエージェントによるブラウザ操作のセットアップを極限まで簡略化し、MCP経由でシームレスな自動化環境を提供します。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[ブラウザ自動化, AIエージェント, MCP (Model Context Protocol), Claude Code, WebDriver BiDi]]

AIエージェント、特にClaude CodeなどのMCP（Model Context Protocol）対応ツールに「ブラウザ操作能力」を付与する作業は、これまでWebDriverの管理やブラウザバイナリのパス設定といった環境構築の煩雑さが障壁となっていた。Vibiumは、これらすべての要素を単一のGoバイナリ（Clicker）に集約し、AIエージェントと人間の双方にとって「ドラマ（面倒な作業）」のない自動化を実現するインフラである。

著者は、現代のAIエージェントワークフローにおける「ブラウザの直接操作」の重要性を説き、そのための最短経路を提供することを目指している。最大の特徴は、MCPサーバーを内蔵している点だ。これにより、エンジニアは`claude mcp add`コマンドを実行するだけで、Claude Codeにブラウザを閲覧・操作する能力を即座に提供できる。内部的には次世代のブラウザ操作標準プロトコルである「WebDriver BiDi」を採用しており、WebSocketを介した効率的かつ双方向の通信を可能にしている。

開発者向けの利便性も高く、JS/TSクライアントを通じて同期（Sync）および非同期（Async）の両方のAPIを提供している。特筆すべきは、`npm install`時に実行プラットフォーム（Windows/macOS/Linux）に応じた最適なChrome for Testingとchromedriverを自動的にダウンロード・配置する仕組みだ。これにより、開発者は低レイヤーの環境差異に悩まされることなく、ブラウザ操作ロジックの実装に集中できる。

著者は、Vibiumが単なるスクレイピングツールではなく、AIエージェントの「手」として機能することを重視している。要素の検索、クリック、テキスト入力、スクリーンショット撮影といった基本アクションがMCPツールとして抽象化されており、LLMが直感的に操作を指示できる設計となっている。今後のロードマップでは、AIによる要素特定（ロケーター）の最適化やビデオ録画機能の追加も予定されており、エージェント駆動型開発（Agentic Workflow）におけるブラウザ操作の標準スタックを目指す筆者の強い意志が反映されている。