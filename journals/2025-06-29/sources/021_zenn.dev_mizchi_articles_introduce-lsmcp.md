## [lsmcp - 汎用的な LSP の MCP サーバーを作った](https://zenn.dev/mizchi/articles/introduce-lsmcp)

**AIエージェント開発を加速させる、言語汎用MCPサーバー「lsmcp」**

本稿では、任意の言語サーバープロトコル（LSP）と連携可能な、汎用MCP（Machine-Readable Command Palette）サーバー「lsmcp」を紹介します。これは、以前のTypeScriptに特化した実装を一般化し、Rust、Python、Goなど多様な言語に対応させたものです。ヘッドレス環境やエディタを起動していない状況でも、AIエージェントが自律的にLSPの機能（型チェック、リント、リネームなど）にアクセスできる基盤を提供することを目的としています。これにより、人間が介在しない状況でのコードベースの理解や操作がより効率的になり、AIエージェ���トによる開発タスクの自動化を大きく前進させます。既存のLSPという標準技術を活用することで、車輪の再発明を避けつつ、AIエージェントが必要とする高度な機能を実現しています。