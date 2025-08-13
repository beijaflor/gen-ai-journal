## 開いているブラウザの内容を読める MCP サーバー

https://blog.pokutuna.com/entry/pokutuna-mcp-chrome-tabs

開発者は既存のLLM向けブラウザ操作ツールの課題を解決するため、現在開いているChrome/Safariタブの内容を効率的にLLMへ渡す軽量MCPサーバーを開発しました。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 91/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[LLM Tools, Browser Automation, MCP Protocol, Developer Workflow, AI Agent Integration]]

ぽくつな氏が、大規模言語モデル（LLM）に現在開いているブラウザのタブ内容を効率的に読ませるための軽量MCP（Multi-Console Protocol）サーバー「@pokutuna/mcp-chrome-tabs」を開発しました。既存のLLM向けブラウザ操作ツールは高機能である一方、不要なツール群がLLMのコンテキストを圧迫したり、Chromeのデバッグポート開放、特定のユーザーディレクトリ使用、ブリッジ拡張機能の導入といった面倒なセットアップが必要で、日常的な利用には不向きという課題がありました。また、URLをLLMに渡しても`robots.txt`に阻まれたり、認証情報がないために内容を読めなかったり、長大なページで「Prompt too long」エラーが発生したりと、開発者が「今見ているページを読ませたい」というシンプルな要求すら満たしにくい状況でした。

本ツールは、macOSのAppleScriptを通じてブラウザタブのコンテンツを直接取得するというユニークなアプローチを採用しています。これにより、HTTPリクエストを介さずに、`robots.txt`や認証の制約を回避して、ユーザーが閲覧中のページ内容をそのままLLMに提供できます。さらに、`@mozilla/readability`の代替として`defuddle`ライブラリを用いて、ページの本文部分のみを抽出し、Markdown形式に変換することで、冗長な情報を削減し、LLMへの入力トークン数を最適化します。

提供される機能は、`list_tabs`による現在開いているタブの一覧取得、`read_tab_content`による指定タブの本文（Markdown形式）取得、そしてAI側からユーザーのブラウザでURLを開ける`open_in_new_tab`の3つに絞られており、軽量さと日常使いを重視しています。特にClaude Codeとの連携を強化するため、MCP Resourcesプロトコルに対応し、`@`補完でタブ候補を表示させるといった統合性の高さも特徴です。議事録の決定事項抽出、LLMが知らない最新ドキュメントに基づくコーディング支援、設計ドキュメントの要約など、具体的なユースケースが紹介されており、開発者の情報収集とLLM連携のワークフローを格段にスムーズにする、実用性の高いツールとして注目されます。