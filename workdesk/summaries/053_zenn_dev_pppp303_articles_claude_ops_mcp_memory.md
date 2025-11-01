## Claude Codeに自分の記憶を持ってもらうMCPサーバーを作った話

https://zenn.dev/pppp303/articles/claude-ops-mcp-memory

開発者は、Claude Codeが自身の操作履歴を「記憶」し参照できるように、Model Context Protocol（MCP）サーバーを開発しました。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 91/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[Claude Code, Model Context Protocol, AIエージェント, 開発ツール, ログ管理]]

本記事は、Claude Codeが自身の操作履歴を記憶し、参照するためのModel Context Protocol（MCP）サーバー「claude-ops-mcp」の開発について詳述しています。著者は、Claude Codeが`/rewind`コマンドで会話を巻き戻せるものの、自身が行った作業内容を根本的に「理解（記憶）」していないという問題意識からこのツールを開発しました。これにより、「何をしたのか？」という質問に対し、Claudeが推論ではなく自身のログを遡って正確に回答できるようになり、開発体験が向上します。

仕組みとしては、Claude Codeがセッションログを記録する`~/.claude/projects/<projectHash>/<sessionId>.jsonl`ファイルを読み取り、その操作履歴をMCPサーバーとして提供します。具体的には、ログファイルの自動検出、JSONLパースによる操作抽出とインデックス化、ファイルパスや操作種別による効率的な検索、セッション検出結果をキャッシュする機構を通じてパフォーマンスを最適化しています。

提供されるMCPツールは以下の4つです。
1. `listFileChanges`: 特定のファイルやパスパターンの変更履歴（CREATE/UPDATE/DELETE）を取得します。
2. `listBashHistory`: セッション内で実行されたBashコマンドの履歴とサマリーを取得します。
3. `showBashResult`: `listBashHistory`で取得した操作IDを使って、特定のコマンドのstdout/stderrや終了コードの詳細を取得します。
4. `showOperationDiff`: `listFileChanges`や`listBashHistory`の操作IDを用いて、詳細な差分をdiff形式で取得します。

インストールはnpmでグローバルに行い、プロジェクトルートに`.mcp.json`ファイルを作成して設定を記述することで、Claude Codeに統合されます。記事では、ファイル編集履歴の確認、差分の確認、特定ファイルの変更履歴、コマンド実行結果の確認、失敗したコマンドの調査など、具体的な使用例も豊富に紹介されており、Claude Codeとの対話における具体的なメリットが示されています。

著者は、この基本的な記憶機能がなぜClaude Code本体に存在しないのか疑問を呈しており、ループ発生やコンテクスト消費のリスクを推測しつつも、現状では問題なく便利に使用できると述べています。また、MCP開発におけるClaude Codeの再起動の煩雑さなど、開発体験の改善点についても言及しています。このツールにより、Claude Codeが自身の行動を「確実な記憶」に基づいて回答できるようになることは、開発者にとって大きなメリットをもたらします。