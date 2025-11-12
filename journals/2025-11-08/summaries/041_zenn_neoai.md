## 「Slackの会話」を「Notionタスク」に変換するAIツールを作ってみた！

https://zenn.dev/neoai/articles/48ecdf48c51470

neoAIのエンジニアが、Slackの会話からNotionタスクを自動生成するAI Botを開発し、その過程で直面した重複リクエストやCold Start、Notion APIの型安全性といった実践的な課題への技術的対策と、内製ツールによる社内DX推進の価値を解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 91/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[Slack API, Notion API, Azure Functions, LLM Integration, Internal DX]]

株式会社neoAIのエンジニアが、Slackの会話内容をNotionのタスクに自動変換するAI Bot「Task Bot」を開発した事例を紹介している。スレッド内でメンションするだけで、タスクの内容、期限、責任者をNotionに自動登録するこのツールは、「AIでできそう」というアイデアを「現場で実際に使われる仕組み」へと落とし込む過程で直面した具体的な課題とその解決策が詳述されている点が、Webアプリケーションエンジニアにとって非常に示唆に富む。

本ツールはAzure Functionsをトリガーとし、LLM（大規模言語モデル）による会話文脈の解析を経てNotionへタスクを登録するアーキテクチャを採用。開発と運用の効率化のため、IaC（Infrastructure as Code）とGitHub ActionsによるCI/CDパイプラインが構築されている。

開発過程で浮上した主要な技術的課題と対策は以下の通りである。

1.  **Slackイベントの重複リクエスト**: Slack Events APIの再送メカニズムにより、サーバレス環境のCold Startなどで応答が遅れると、同じイベントが複数回送信されNotionに重複タスクが登録される問題。
    *   **対策**: Azure Table Storageを活用し、Slackの`channel`と`ts`（タイムスタンプ）を組み合わせた一意のIDでリクエストの冪等性を担保。これにより、超低コストで堅牢な重複処理防止を実現している。
2.  **Azure FunctionsのCold Start**: ConsumptionプランにおけるCold Startによる起動遅延が、Slackの3秒応答要件を満たせない原因となる問題。
    *   **対策**: Timer Triggerを利用し、5分おきにウォームアップ処理を実行することで、インスタンスの自動スケールダウンを防ぎ、常時高速応答を可能にしている。これはAzure Functionsの無料枠内で賄える低コストな運用方法である。
3.  **Notion APIの型定義の欠如**: PythonのNotion公式SDKには型定義がなく、型安全な開発が難しい問題。
    *   **対策**: 社内エンジニアが開発した、Pydantic v2とhttpxに対応した型安全なNotion APIクライアントライブラリ「notion-py-client」を利用することで、ドメインモデルへのマッピングを容易にし、開発効率を向上させている。

このTask Botは社内で日常的に利用されており、自社の業務に合わせた内製ツールの価値を実証した。外部ツールを探すのではなく、APIを活用してワークフローにフィットするツールを自社で作り込むアプローチが、低コストかつ高インパクトなDXに繋がることが強調されている。この取り組みを契機に、他の社内DXプロジェクトも始まり、「あったらいいよね」という構想を「実際に使われる仕組み」へと落とし込む文化が醸成されている。