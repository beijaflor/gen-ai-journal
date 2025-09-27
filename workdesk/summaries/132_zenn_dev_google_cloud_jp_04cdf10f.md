## 【Agent Engine の A2A 対応記念】A2A リモートエージェントを Agent Engine にデプロイする

https://zenn.dev/google_cloud_jp/articles/04cdf10fb5cd70

Google CloudのAgent EngineがA2Aに標準対応したことで、マルチエージェントシステムのデプロイと連携が大幅に簡素化されました。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[Agent Engine, マルチエージェントシステム, A2A, Agent Development Kit (ADK), Vertex AI Workbench]]

Google CloudのAgent EngineがA2A（Agent-to-Agent）に標準対応し、マルチエージェントシステムのデプロイと連携が劇的に簡素化されました。これまでは、Agent Engineの前段にCloud RunでA2Aサーバーを別途構築する必要がありましたが、今回のアップデートによりその手間が不要に。Agent Development Kit (ADK)が提供する`RemoteA2aAgent`クラスとAgent EngineのA2A対応が連携し、ローカルエージェントとほぼ同じ感覚で、デプロイ済みのリモートエージェントをサブエージェントとして組み込めます。

記事では、Vertex AI Workbench上で「調査レポート作成」「記事執筆」「記事レビュー」といった役割を持つLlmAgent群をA2AリモートエージェントとしてAgent Engineにデプロイし、それらを順序立てて実行するルートエージェントを構築する具体例が示されています。特に、ADKが提供する`A2aAgentExecutor`クラスがA2AプロトコルリクエストをADKエージェントに転送するプロキシ機能を提供し、セッション管理に`VertexAiSessionService`を活用することで、スケーラビリティも考慮されています。

この機能強化により、ウェブアプリケーションエンジニアは複雑なインフラ構築に時間を割くことなく、複数の専門エージェントが協調してタスクを遂行する高度なAIシステムを、より手軽に開発・運用できるようになります。現状はExperimentalフェーズで一部ワークアラウンドが必要ですが、今後のADKとAgent Engineの進化が、agent-basedな開発ワークフローをさらに加速させるでしょう。