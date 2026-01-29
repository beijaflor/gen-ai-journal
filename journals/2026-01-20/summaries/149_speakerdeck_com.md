## AI Agent の開発と運用を支える Durable Execution #AgentsInProd

https://speakerdeck.com/izumin5210/ai-agents-in-production-1

LLMの呼び出しやツール実行が繰り返されるAIエージェントの実行を、Durable Execution（再開可能な実行）によって安定化させる手法を解説する。

**Content Type**: Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[AI Agent, Durable Execution, Temporal, Backend Architecture, Human-in-the-Loop]]

本資料は、LayerXのizumin5210氏が、AIエージェントをデモレベルからプロダクトレベルへと引き上げるために不可欠な「バックエンドの耐久性（Durability）」について解説したものである。

著者は、AIエージェントの本質をLLMとツール実行のループ（Agentic Loop）にあると定義した上で、本番運用における最大の課題は、このループを「安定して・確実に動かしきる」ことにあると指摘している。LLM呼び出しの成功率がたとえ高くとも、ステップ数が増えれば全体の失敗確率は累乗で増加し、さらに人間が判断を挟むHITL（Human-in-the-Loop）が加わると、実行時間は数十分から数時間に及ぶこともある。これに対し、途中でエラーが起きたりデプロイのためにサーバーが再起動したりしても、最初からやり直すことなく途中から再開できる「Durable Execution（再開可能な実行）」の導入を提唱している。

具体的な解決策として、TemporalやInngest、Trigger.dev、Vercel Workflowなどのワークフロー基盤の活用が挙げられている。これらのミドルウェアは、副作用のある処理（Activity）とその実行順序を制御するロジック（Workflow）を分離し、各ステップの入出力を記録することで、障害発生時でも過去のステップをリプレイして正確に状態を復元できる。

特に実務的なメリットとして強調されているのが、HITL実装の簡略化である。従来、承認待ちなどの状態を管理するには複雑なDBスキーマ設計と状態遷移の管理が必要だったが、Durable Executionを用いれば、ワークフロー内のローカル変数として状態を保持し、外部からの「Signal（シグナル）」を待機するだけで実装が可能になる。

筆者は、Vercel AI SDKとTemporalを統合する`@temporalio/ai-sdk`の実装例を紹介しながら、今後のAIプロダクト開発においては、プロンプトエンジニアリングといった「AI Engineering」の側面だけでなく、信頼性を担保する「Software Engineering」の観点からバックエンド・アーキテクチャを設計することが、Webエンジニアにとって極めて重要になると結論付けている。