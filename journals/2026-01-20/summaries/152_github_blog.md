## GitHub Copilot SDKがテクニカルプレビューとして公開

https://github.blog/changelog/2026-01-14-copilot-sdk-in-technical-preview/

**Original Title**: Copilot SDK in technical preview

GitHub Copilot CLIの機能をプログラムから直接利用可能にする多言語対応SDKのテクニカルプレビューを開始した。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 85/100 | **Overall**: 84/100

**Topics**: [[GitHub Copilot, SDK, CLI, AI Agents, Developer Tools]]

GitHubは、GitHub Copilot CLIの機能をアプリケーションや自作ツールにプログラムレベルで統合するための「Copilot SDK」をテクニカルプレビューとして公開した。これまでチャットUIやCLIコマンドとしての利用が主だったCopilotを、開発者が自身のワークフローに合わせたカスタムエージェントや自動化ツールの中に、APIとして直接組み込むことが可能になる。

本SDKはNode.js/TypeScript、Python、Go、.NETという主要な4言語に対応しており、いずれも一貫したAPI設計がなされている。主な機能として、文脈を維持したやり取りを可能にする「マルチターン対話（セッション履歴管理）」、AIモデルが独自のカスタムツールを呼び出せる「ツール実行（Tool Execution）」、そしてクライアントとセッションのライフサイクルを細かく管理できるコントロール機能が提供される。

著者は、このSDKの提供により、Copilotの強力な推論能力を特定の開発プロセスにシームレスに組み込めるようになる点に大きな意義があると主張している。Webアプリケーションエンジニアにとっては、IDE外での定型業務の自動化や、自社専用の高度なAIアシスタントの構築において、GitHub公式の信頼性と柔軟性を備えたバックエンドを直接叩けるようになったことが、開発者体験（DX）を大きく向上させる鍵となるだろう。