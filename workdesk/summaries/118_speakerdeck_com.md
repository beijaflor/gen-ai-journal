## 2025年 Amazon Bedrock AgentCoreまとめ

https://speakerdeck.com/yuu551/2025nian-amazon-bedrock-agentcorematome

AIエージェントの構築・運用に必要な全コンポーネントを網羅的に解説し、開発者がプロトタイプから本番環境へ移行するための具体的な実装指針を提示する。

**Content Type**: 🛠️ Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 94/100 | **Annex Potential**: 91/100 | **Overall**: 92/100

**Topics**: [[Amazon Bedrock, AI Agent, MCP, AWS, Strands Agents]]

Amazon Bedrock AgentCoreの全体像と、各コンポーネントの詳細を解説した包括的な技術リファレンスである。著者は、AIエージェントを単なるLLMの利用から一歩進め、自律的にタスクを計画・実行・評価する存在として定義し、その展開・運用を支えるマネージドサービス群の重要性を強調している。Webアプリケーションエンジニアにとって、インフラ管理を排してロジック構築に集中できる環境がいかに整っているかが具体的に示されている。

主要な機能群として、Runtime、Identity、Memory、Gateway、Observability、Evaluationsの6つが挙げられている。Runtimeは、Strands AgentsやLangGraphといった多様なフレームワークをサポートし、サーバーレスで自動スケールする実行環境を提供する。IdentityはCognito等と連携した認証（Inbound）に加え、Secrets Managerを用いた外部APIへの安全なアクセス（Outbound）を担う。特筆すべきはMemory機能で、会話履歴などの短期記憶だけでなく、エピソード記憶（教訓の抽出）を含む長期記憶をマネージドで提供し、エージェントの「学習」を容易にしている。

また、Gateway機能は、多数のLambda関数や外部APIをMCP（Model Context Protocol）互換ツールとして集約する。これにより、セマンティック検索を用いた適切なツールの動的選択が可能となり、大量のツール登録によるコンテキスト汚染を回避できる。さらに、2024年末にアップデートされた「Policy（Cedarによる認可制御）」や「Interceptors」を用いることで、ユーザー権限に応じたきめ細やかなツール実行制御が可能となった。

著者は、AIエージェントは「作って終わり」ではなく、継続的な評価と改善が不可欠であると主張している。Evaluations（Preview）によるLLM-as-a-Judge（目標達成率やツール選択の正確性評価）と、Observabilityによるトレース可視化を組み合わせることで、本番運用における挙動の不透明さを解消し、信頼性の高いエージェント開発を可能にする。本書は、最新のAWSアップデート（re:Invent 2024等）を反映しており、2025年におけるAIエージェント構築の決定版と言える内容となっている。