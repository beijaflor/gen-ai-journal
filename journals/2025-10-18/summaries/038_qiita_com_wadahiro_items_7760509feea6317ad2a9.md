## OAuthによるMCPサーバの保護（MCP Version 2025-06-18版）

https://qiita.com/wadahiro/items/7760509feea6317ad2a9

Model Context Protocol (MCP) サーバーをGo言語とKeycloakを用いてOAuth 2.1でセキュアにする具体的な実装手順と、関連する最新仕様の動向を詳細に解説する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 94/100 | **Annex Potential**: 92/100 | **Overall**: 92/100

**Topics**: [[Model Context Protocol, OAuth 2.1, Keycloak, Go言語, 認証・認可]]

本記事は、MCP (Model Context Protocol) Version 2025-06-18の推奨に基づき、HTTPベースのMCPサーバーをOAuth 2.1で保護する具体的な実装方法をGo言語で解説する。リモート環境で機密性の高いリソースにアクセスするMCPサーバーにとって、適切な認証・認可が不可欠であると著者は強調する。

まず、シンプルなエコー機能を提供する認証なしのMCPサーバーをGo SDKで実装。次に、OAuth保護を追加するための要点を詳細に説明する。未認可時には401 Unauthorizedレスポンスとともに`WWW-Authenticate`ヘッダーで`resource_metadata`パラメータを提供し、MCPクライアントが認可サーバー情報を取得できるようにする。また、MCP仕様で必須とされるOAuth 2.0 Protected Resource Metadata (RFC 9728) エンドポイントの実装方法を示す。

アクセストークンの検証については、KeycloakがJWT形式のトークンを発行するため、レイテンシと認可サーバーの負荷を抑えるローカルでのJWT検証を採用。`keyfunc`ライブラリを用いてJWKSエンドポイントから公開鍵を自動取得し、署名を検証する。さらに、`iss` (発行者)、`exp` (有効期限)に加え、RFC 8707に基づく`aud` (Audience) クレームの検証が必須であると指摘。Keycloak 26.4がRFC 8707に未対応であるため、Audience Mapperを用いたワークアラウンドも紹介している。`mcp:tools`スコープの検証も実装し、これらの検証ロジックをGoのミドルウェアとして組み込むことで、MCPサーバーを保護する。

認可サーバーにはKeycloak 26.4を使用し、Docker Composeでの起動からCORS問題のワークアラウンド（Nginx利用）、テスト用レルム、クライアントスコープ、Audience Mapperの設定まで、詳細な手順が示される。OAuth 2.1で必須とされるPKCEについても、Keycloakのクライアントポリシーによる対応の必要性が言及されている。

記事の後半では、MCP Authorization仕様の今後の動向について深く掘り下げている。現在のDynamic Client Registration (DCR) に関連する運用上の課題（データベース増大、DoS攻撃脆弱性）やセキュリティリスク（クライアントなりすまし）を挙げ、SEP-991 (CIMD) やSEP-1032 (Software Statements) といった改善案を紹介。特にエンタープライズ環境向けには、DCRを使わないSEP-646 (Enterprise-Managed Authorization Profile) が、企業IdP連携や集中管理の観点から期待されると説明する。

さらに、MCPサーバーがGitHubやSlackなどの外部APIにアクセスする際のセキュリティ問題について言及。SEP-1036で提案されているURL modeがこの課題解決を目指すものの、初期案にはユーザー識別とトークン紐付けに関する深刻なセキュリティ上の懸念があると著者は指摘する。しかし、最新のドキュメント（PR #887）では、MCPサーバーが自身のURLを返すことで、よりセキュアなブラウザベースのOAuthフローを実現する推奨パターンが示されており、この進展についても触れている。

著者は、MCPの認証・認可の仕組みが現在も活発に議論され、今後大きく変化する可能性を強調し、実装時には最新の仕様と議論を確認することを推奨している。本記事は、MCPをセキュアに導入するための深い洞察と実用的な実装ガイドを提供する。