## 1PasswordでMCPサーバーを保護：エージェント設定における認証情報の漏洩を防ぐ

https://1password.com/blog/securing-mcp-servers-with-1password-stop-credential-exposure-in-your-agent

**Original Title**: Securing MCP servers with 1Password: Stop credential exposure in your agent configurations

1Password CLIは、AIエージェントの設定ファイルにおける平文の認証情報漏洩リスクを解消するため、実行時にシークレットを安全に注入する実践的な手法を提供する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[認証情報管理, AIエージェント, 1Password CLI, シークレット管理, エージェント開発ワークフロー]]

この記事は、GitHub CopilotやClaude CodeなどのAIツールを用いたエージェント開発環境において、`mcp.json`のような設定ファイルに平文の認証情報が保存され、漏洩リスクに晒されている現状を指摘しています。筆者は、この問題に対する安全かつ生産的な解決策として、1Password CLI (`op run`) を活用した認証情報の実行時注入を提案します。これは、コミュニティのデベロッパー @codekiln 氏が提示した手法に基づいています。

このアプローチの核となるのは、認証トークンをコード内にハードコードする代わりに、1Passwordのボールトに保存し、実行時に`op run`コマンドを通じて安全に注入することです。これにより、平文の認証情報がリポジトリにプッシュされたり、Git履歴に残ったり、手動でコピー＆ペーストされることによる漏洩のリスクを排除できます。

具体的な実装手順は以下の通りです。まず、必要なAPIトークンを1Passwordのボールトにアイテムとして保存します。次に、`.env`ファイル内でこれらのシークレットを`op://<vault>/<item>/<field>`形式のシークレット参照として定義します。最後に、エージェントのMCPサーバー起動コマンドを`op run --env-file=.env -- mcp-server start`のようにラップすることで、1Password CLIが`.env`ファイルの参照を解決し、シークレットをメモリ上で復号化し、プロセス実行中の環境変数として注入します。プロセス終了後、シークレットはメモリから消去されるため、高いセキュリティが保たれます。これにより、`mcp.json`は`"token": "${GITHUB_TOKEN}"`のように環境変数を参照する形になり、安全にバージョン管理できるようになります。

この手法は、既存のAI開発ツールの動作を変更することなく、認証情報の取得方法のみを改善します。1Password CLIを使用することで、新しいSDKや特定の統合を待つことなく、今日からこのセキュリティパターンを実装できる点が重要です。また、ローカルの`.env`ファイルよりも構造化された管理が必要な場合は、現在ベータ版の「1Password Environments」を利用することで、プロジェクト間で環境変数を一元的に定義・同期・ローテーションできる利点も紹介されています。著者は、デベロッパーがセキュリティと生産性のどちらかを選択する必要はないと強調し、このアプローチがAIエージェント開発における認証情報管理の未来であると主張しています。