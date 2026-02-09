## リモートMCPサーバーの現在地を調べてみた

https://qiita.com/goroneko/items/00f1c99ac91d0c495cf7

リモート環境における **Model Context Protocol (MCP)** サーバー実装の技術的課題を整理し、現実的な構成指針を提示する。

**Content Type**: Technical Reference
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 81/100 | **Overall**: 80/100

**Topics**: [[Model Context Protocol, Remote MCP Server, Streamable HTTP, OAuth 2.1, Server-Sent Events]]

リモート環境における **Model Context Protocol (MCP)** サーバー実装の技術的課題と、現時点での現実的な構成指針を詳説している。ローカルの標準入出力とは異なるトランスポート層（**Server Sent Events (SSE)** や最新の **Streamable HTTP**）の仕組みを解説し、ロードバランサー配下での水平スケーリングを阻むステート管理の難点を指摘する。

主要な知見として、現時点では **Sampling** 等のステートフルな機能を削ぎ落とし、**Tools** や **Resources** の提供に特化したステートレス構成を採用するのが最も合理的であると提言している。認可面では、最新のMCP仕様が求める **OAuth 2.1** や **RFC 8707 (Resource Indicators)** への主要 **IdP (Keycloak等)** の対応が遅れている実態を明示。回避策として、静的クライアント登録の利用や **FastMCP** によるプロキシ構成、**MCP Gateway** の活用を推奨している。さらに、**OpenTelemetry (OTel)** を用いた可観測性や、JSON-RPC特有のエラーハンドリングについても実践的な知見を共有している。

MCPサーバーをローカル実行から一歩進め、クラウド上での外部公開やプロダクション運用を検討しているエンジニアにとって、仕様の理想と実装のギャップを埋めるための具体的なガイドとなる内容だ。