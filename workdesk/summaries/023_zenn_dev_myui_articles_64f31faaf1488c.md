## なぜ今、Agentic Workflowなのか - Graflowの設計思想

https://zenn.dev/myui/articles/64f31faaf1488c

Graflowは、AIエージェントのプロダクション環境における「理想と現実のギャップ」を解消するため、ワークフローオーケストレーションに特化した、柔軟性と制御性を両立する新しいエンジンを提供します。

**Content Type**: Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 94/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[AI Agent Workflow, オーケストレーション, LangGraph, 分散システム, Human-in-the-Loop]]

本記事は、AIエージェントをプロダクション環境で運用する際の課題、特に「自律性と制御性の両立」に着目し、著者が開発する新しいオーケストレーションエンジン「Graflow」の設計思想を解説しています。現在のAIエージェントフレームワークが「SuperAgent型」に傾倒し、エージェント内部の推論ループまでグラフ化するLangGraphのようなアプローチが可読性や保守性の課題を抱える中、Graflowは異なる戦略を打ち出します。

Graflowは、AIワークフローを「Type B: Agentic Workflow（構造化フロー + エージェント自律性）」に特化することで、「制御された自律性」を実現することを目指しています。これは、ワークフロー全体は人間が設計しつつ、各タスク内部でエージェントが自律的に動作するというアプローチです。既存のSuperAgent型フレームワーク（Google ADK、PydanticAIなど）は「Fatノード」としてラップし、ワークフローオーケストレーションに集中することで、各領域のベストツールを活用できる「責務分離型」の利点を強調しています。

Graflowが解決する具体的な実務課題は多岐にわたります。LangGraphが抱える課題として、エージェント内部の推論ループまでグラフ化することによる可読性・保守性の低下に対し、GraflowはSuperAgentをFatノードとして扱い、ワークフローの「タスク間の連携」に注力します。また、LangGraphで事前定義が必要な条件分岐やループの柔軟性の低さに対しては、実行時の動的なタスク生成や条件分岐を可能にする`context.next_task()`や`context.next_iteration()`を提供。長時間ワークフローの途中落ち問題には、ユーザー制御の`checkpoint/resume`で再開を可能にし、承認待ちのHuman-in-the-Loop（HITL）も`checkpoint`と組み合わせることで効率化します。さらに、タスクの並列処理とワーカーの水平スケールを実現するため、Redisベースの分散実行アーキテクチャを採用し、シンプルなAPIで切り替えを可能にしています。

その他の重要機能として、軽量なLLM呼び出しを可能にする`inject_llm_client`、DAGとState Machineのハイブリッド設計をPythonic演算子DSLで記述できる柔軟性、Docker実行を標準装備したプラグ可能タスクハンドラー、タスク間のステート共有を担うChannel通信（型安全なTypedChannelを含む）、並列タスク実行時の細粒度エラーポリシー（Strict/Best-effort/At-least-N/Critical Tasks）、そしてLangFuse/OpenTelemetryを統合した実行時の可観測性強化（自動トレース収集とOpenTelemetryコンテキスト伝播）が挙げられます。

Graflowは2026年1月にOSS公開を予定しており、生産環境でAIエージェントワークフローを安心して動かすための、戦略的シンプルさ、実行時の柔軟性、開発体験、プロダクション対応、並列分散処理によるスケーリングをコア価値としています。