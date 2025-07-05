## [【コーディング無し】既存 API サーバーを MCP サーバーに一瞬で変える方法](https://zenn.dev/microsoft/articles/expose-mcp-server-in-apim)

**既存APIをコーディング無しでMCPサーバーに！Azure APIM新機能プレビュー**

Azure API Management (APIM) に、既存のREST APIをコーディングなしでModel Context Protocol (MCP) サーバーとして公開できる新機能がプレビューで登場しました。この機能を使えば、APIMにAPIをインポートするだけで、GitHub CopilotなどのAIエージェントから利用可能なツールとしてAPIを公開できます。

主な利点は、コード改修が不要である点、そしてAPIMが提供する認証、レート制限、ログ収集といった堅牢な機能をそのまま活用できる点です。これにより、既存のAPI資産を活かしつつ、迅速に生成AIエコシステムに対応させることが可能になります。

設定は、特定の価格レベル（Basic, Standard, Premium v1）のAPIMインスタンスを作成し、更新グループを「AIゲートウェイ先行アクセス」に変更後、専用URLからポータルにアクセスして行います。APIをインポートし、新設された「MCP」ブレードから数クリックでサーバーを公開できます。公開したサーバーは、MCP InspectorやVS Code上のGitHub Copilotから接続して動作確認が可能です。

この機能により、開発者は既存のサービスを容易にAIエージェントと連携させ、新たな価値創出を加速できます。