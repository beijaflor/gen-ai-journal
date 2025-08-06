## MCPの認証と認可の現在と未来

https://hi120ki.github.io/ja/blog/posts/20250728/

MCPの認証・認可における企業利用の課題を分析し、将来自動化されたAIエージェントの安全な利用を可能にする新たな仕様と集中管理型IDプロバイダーの役割を提示する。

**Content Type**: Research & Analysis

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 93/100 | **Annex Potential**: 92/100 | **Overall**: 92/100

**Topics**: [[MCP, OAuth, AI Agent Security, Enterprise Authentication, Identity Management]]

MCP（AIエージェントプラットフォーム）はCursorやClaude Codeといったクライアントから日常的に利用されるようになり、そのエコシステムは拡大しています。しかし、現在のMCPの認証・認可の仕様、特にOAuth 2.1ベースのDynamic Client Registration（DCR）は、企業環境での導入において大きな課題を抱えています。

**現行仕様の課題点**:
1.  **Dynamic Client Registrationのセキュリティと互換性**: DCRは手軽な一方で、エンタープライズのセキュリティポリシー（事前登録必須など）に合致せず、OktaやGoogleのような主要なIdPが認証なしのDCRを直接サポートしていません。Atlassianのような独自実装は複雑性とセキュリティリスクを伴います。
2.  **バックエンドサービスへの認可の不明瞭さ**: MCPサーバーが社内リソース（データベース、ナレッジベースなど）へ安全にアクセスするためのベストプラクティスが未確立です。安易なマシンユーザー利用は「Confused deputy problem」を引き起こし、既存のアクセス境界を破壊する恐れがあります。ユーザーごとのOAuthフローが理想的ですが、現行MCPでは実装が困難です。

**将来の解決策とOktaの役割**:
これらの課題を解決するため、「Enterprise-Managed Authorization Profile for MCP」仕様が提案されています。これはIdentity Assertion Authorization Grantに基づき、IdP（Okta、Googleなど）を認可の中心に据える新しいフローです。
ユーザーはIdPに一度ログインするだけで、MCPクライアントがブラウザを介さずに、そのユーザーの権限に応じたサービスごとのアクセストークンを自動取得できるようになります。これにより、エンタープライズ管理者はアクセストークンの発行を一元的に管理・可視化でき、各サービスで独自に行われていたAPIキー発行プロセスを置き換え、ユーザー体験を向上させることができます。

**エンジニアへの影響**:
この仕様の進化は、企業内でAIエージェントをセキュアに展開する上で不可欠です。既存のセキュリティ境界を維持しつつ、AIエージェントが個々のユーザー権限に基づいて機密性の高い社内リソースにアクセスできる道を開きます。現時点では各サービスの対応状況やMCPクライアントの事前登録など懸念点は残りますが、本稿は今後のAIエージェントの安全な利用と管理のロードマップ策定に役立つ重要な知見を提供します。