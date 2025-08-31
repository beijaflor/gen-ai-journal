## Securing the AI Revolution: Introducing Cloudflare MCP Server Portals

https://blog.cloudflare.com/zero-trust-mcp-server-portals/

Cloudflareは、LLMと企業アプリケーションをセキュアに連携させるModel Context Protocol (MCP) の接続を中央管理・監視する「Cloudflare MCP Server Portals」の提供を開始します。

**Content Type**: News & Announcements

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 91/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[AIセキュリティ, LLM連携, ゼロトラスト, Model Context Protocol, SASE]]

Cloudflareは、大規模言語モデル（LLM）がSlackやJiraなどの企業アプリケーションとセキュアに連携するためのオープンソース標準であるModel Context Protocol（MCP）の接続を一元化、保護、監視する「Cloudflare MCP Server Portals」をオープンベータで提供開始しました。

この機能は、LLMが単なる情報検索ツールから、社内データやツールにアクセスして具体的なアクションを実行できる「インテリジェントなエージェント」へと進化する上で不可欠なMCPのセキュリティ課題に対処します。MCPの普及に伴い、プロンプトインジェクション、サプライチェーン攻撃、意図しない権限昇格（confused deputy）、データ漏洩といった新たな攻撃経路が生まれ、未保護の「シャドーAI」インフラがリスクとなる可能性が高まっています。

Cloudflare MCP Server Portalsは、全てのMCPサーバーへの「単一の入り口」を提供することで、これらのリスクを軽減します。具体的には、Cloudflare Oneに統合されることで、ユーザーアクセスに対する多要素認証やデバイスポスチャチェックなどのゼロトラストポリシーを適用できます。これにより、どのLLMクライアントがどのMCPサーバー上のツールにアクセスできるかを詳細に制御可能になります。さらに、全てのMCPリクエストのログを一元的に集約し、監査や異常検知に必要な可視性を提供します。管理者は承認されたサーバーとツールのみをユーザーに公開でき、最小権限の原則に基づいた安全なAI利用環境を構築できます。

ウェブアプリケーションエンジニアにとって、この発表は、開発中のAI連携アプリケーションのセキュリティと運用管理を大幅に簡素化するものです。個々のMCPサーバーごとにセキュリティ対策を講じる必要がなくなり、既存のCloudflare Zero TrustフレームワークでAI関連のアクセスも包括的に管理できるため、安全なAIエージェントの構築とデプロイを加速できるでしょう。

将来的にCloudflareは、MCPサーバーのロックダウン機能、WAFによるプロンプトインジェクション防御、機械学習を用いた異常検知、そしてMCP標準自体の強化に取り組む予定です。これは、企業がAIの可能性を安全に活用し、イノベーションを推進するための重要な一歩となります。