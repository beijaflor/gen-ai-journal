## ドキュメント検索MCPサーバを作ってみた【MCP+OpenSearch+AWS】

https://zenn.dev/levtech/articles/a5a3204ffed86c

レバテック開発部が、社内問い合わせ工数削減を目指し、OpenSearchとFastAPIを活用したドキュメント検索システムとFastMCPによるMCPサーバーの構築事例を詳細に解説する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 86/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[AI活用, 検索システム, OpenSearch, FastAPI, Lambda Web Adapter, Model Context Protocol]]

レバテック開発部のSREチームは、AWS、New Relic、TiDBなど複数のSaaSに関する社内問い合わせ対応の工数削減が課題でした。この課題解決のため、各サービスの公式ドキュメントを参照し、LLMに正確な回答を返すドキュメント検索MCP（Model Context Protocol）サーバーを構築した事例を解説しています。

筆者は、AWSが提供する優れたドキュメントMCPサーバーから着想を得たものの、その検索システムが専用APIに依存しているため、他のサービスへ応用するには検索システム自体を構築する必要があると説明。そこで、OpenSearchとFastAPIを組み合わせた検索システムとFastMCPによるMCPサーバーを自社で実装したと述べています。

システムアーキテクチャとして、検索エンジンには全文検索と将来的なベクトル検索によるハイブリッド検索を見据えOpenSearchを採用。バックエンドAPIはFastAPIで構築し、Lambda Web Adapterを使いAPI GatewayとLambdaによるサーバーレス構成で運用されています。MCPサーバーはFastMCP（Python）で実装され、LLMからの検索リクエストを受け付けてバックエンドAPIへ連携します。

バックエンドの実装では、AWSのAPI仕様を参考にPydanticスキーマを設計し、検索結果はタイトル、URL、抜粋、要約などのメタ情報に特化。詳細な情報取得はLLMに任せることで責務を分離しています。OpenSearchの検索部分は、`title`、`body`、`summary`の複数フィールドを対象とした`multi_match`クエリ（`title`に2倍の重み付け）や、`fuzziness: AUTO`による曖昧検索、ヒット箇所の前後テキストを抽出する`highlight`機能を活用し、高品質な検索結果を提供します。Lambda Web Adapterは、FastAPIアプリケーションを容易にサーバーレス環境で動作させるための重要なコンポーネントとして紹介されています。

ドキュメントの取り込みプロセスは、GitHubで公開されているSaaSの公式リポジトリをクローンし、MarkdownファイルをパースしてOpenSearchにインデックスするものです。ファイルパスからドキュメントURLを生成し付与する機能も含まれており、自動更新ワークフローの構築も示唆されています。

この取り組みは、開発現場における具体的な運用課題に対し、既存の技術スタック（OpenSearch, FastAPI, AWS Lambda）とAI（LLM, MCP）を組み合わせることで、効率的かつ実践的な解決策を構築できることを示しています。今後はベクトル検索によるセマンティック検索の強化などが検討されています。