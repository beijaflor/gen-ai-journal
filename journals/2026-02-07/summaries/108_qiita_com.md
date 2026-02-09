## 混乱しました。AWS MCP ServersとAWS MCP Serverの違いを徹底解説

https://qiita.com/sh_fukatsu/items/93719d61d3251df07a59

AIエージェント向けの**AWS MCP Server**について、OSS版との違いや統合された**Agent SOPs**の実効性を検証する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 83/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[AWS, MCP, AI Agent, CloudTrail, Agent SOPs]]

2025年末にPreview公開されたマネージド版**AWS MCP Server**について、従来のOSS版（**AWS MCP Servers**）との名称や機能構成の決定的な差異を解説しています。主な内容は、**AWS Knowledge**（ドキュメント検索）、**AWS API**（リソース操作）、そして新機能の**Agent SOPs**（定型ワークフロー）が単一のエンドポイントに統合されたことによる構成の簡素化です。

技術面では、**mcp-proxy-for-aws**を用いた**SigV4**署名によるセキュアな接続や、**CloudTrail**の`invokedBy`フィールドにより「どのMCP経由で実行されたか」を追跡可能にする監査体制の強化について詳述されています。著者は具体例として「アプリケーション障害のトラブルシューティングSOP」を検証し、ログ分析から優先順位付きのアクションプラン生成までを自動化する高い実用性を確認しています。一方で、マネージド環境特有の通信遅延など、Preview版ゆえの課題にも触れています。

AIエージェントを自社のAWS環境へ安全かつ迅速に導入し、運用フローを自動化したいプラットフォームエンジニアやSREに最適なガイドです。