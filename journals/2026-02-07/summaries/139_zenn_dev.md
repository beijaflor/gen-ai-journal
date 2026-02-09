## MCP Apps を実装してわかったこと ─ UIをチャットに埋めるまでの試行錯誤

https://zenn.dev/naokky/articles/202601-mcpapp-sample

Pythonを用いた**MCP Apps**の実装過程で遭遇した**UI Resource**表示の落とし穴とその解決策を詳述する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 85/100 | **Overall**: 84/100

**Topics**: [[Model Context Protocol (MCP), Python (FastMCP), UI Resource, CSP/CORS, AI Agent]]

Python環境下で**MCP Apps**の**UI Resource**機能を実装する際の実践的なトラブルシューティングを詳解している。公式の**basic-host**と**FastMCP**（Python SDK）を組み合わせ、カラーピッカーなどのインタラクティブなUIをチャットインターフェースに埋め込むプロセスを辿る内容だ。

技術的な核心として、UIが表示されない主な原因が**mimeType**の設定不備（`;profile=mcp-app`の欠落）にあることや、**CSP（Content Security Policy）**および**CORS**が**Host**と**MCP Server**間の内部通信として動作する特異な仕様を明らかにしている。著者は、**MCP Apps**を単なるUIフレームワークではなく、エージェントの自律的な処理フローに「人間の判断（Human-in-the-loop）」を安全に介在させるための「確認の隙間」を埋める技術として定義している。

Web APIの常識が通用しないデバッグの難しさについても触れられており、**Python**で**MCP**サーバーを構築し、ツール実行時に動的なUI表示を統合したい開発者にとって、実用性の高い指針となっている。