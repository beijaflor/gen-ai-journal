## Web Bot Auth

https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/

Cloudflareは、IETFドラフトに基づく暗号署名を利用し、自動化されたボットのリクエストを正当に検証する「Web Bot Auth」の実装方法を詳細に解説します。

**Content Type**: 🛠️ Technical Reference

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 96/100 | **Annex Potential**: 94/100 | **Overall**: 96/100

**Topics**: [[ボット認証, HTTPメッセージ署名, 暗号鍵管理, AIエージェント開発, ウェブセキュリティ]]

Cloudflareが提供する「Web Bot Auth」は、自動化されたボットが正当なリクエスト元であることを暗号署名を用いて検証する画期的な方法を提示します。これは、IETFドラフトに基づいた標準的なアプローチであり、ウェブアプリケーションエンジニアが開発するAIエージェントやクローラーが、Cloudflareのようなボット管理システムによって誤ってブロックされるリスクを軽減するために非常に重要です。

Web Bot Authの導入は、大きく分けて以下のステップで構成されます。まず、Ed25519プライベートキーとパブリックキーを生成し、パブリックキーをJWK（JSON Web Key）形式に変換します。次に、このJWKを含むキーディレクトリを`.well-known/http-message-signatures-directory`にHTTPSでホストし、ディレクトリ自体もHTTPメッセージ署名で認証します。最後に、Cloudflareダッシュボードを通じてボットとキーディレクトリを登録し、検証を待ちます。

検証が完了すれば、ボットは今後のHTTPリクエストに`Signature-Input`、`Signature`、`Signature-Agent`といった必要なヘッダーを付与し、暗号署名を組み込むことで、自身の身元を証明できます。この技術は、AIを利用したサービスが安定してウェブアプリケーションと連携するために不可欠です。ボットが自身を「検証済み」として提示できるため、悪意のあるボットと区別され、信頼性の高い自動化されたワークフローを構築できます。特に、厳格なボット対策が施された環境で、AIエージェントが意図した通りに動作することを保証する上で、この標準化された暗号認証は非常に価値があります。