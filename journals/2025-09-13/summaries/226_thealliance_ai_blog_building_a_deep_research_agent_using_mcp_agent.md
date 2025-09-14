## Building a Deep Research Agent Using MCP-Agent

https://thealliance.ai/blog/building-a-deep-research-agent-using-mcp-agent

MCP-Agentの作成者が、複雑なタスクに対応するディープリサーチエージェント「Deep Orchestrator」の開発過程と、シンプルさ、確定的検証、プロンプトエンジニアリングの重要性を詳述する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 90/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[AI Agent Architecture, Deep Research Agents, Prompt Engineering, Agent Orchestration, MCP-Agent]]

MCP-Agentの作成者であるSarmad Qadri氏は、深層調査を含む複雑なタスクに対応する汎用エージェント「Deep Orchestrator」の開発ジャーニーを共有しています。当初、計画・実行・合成レイヤーを持つ「Orchestrator」パターンを試みましたが、LLMのハルシネーション、トークン効率の悪さ、事前計画の限界に直面しました。

次に、動的なサブエージェント、FIFOキュー、外部メモリ、予算管理などを導入した「Adaptive Workflow」を試みましたが、実世界ではナビゲーションの問題や性能低下、複雑性によるオーバーヘッドが発生し、期待通りの成果は得られませんでした。

最終的に「Deep Orchestrator」として、最初のOrchestratorのシンプルさを基盤としつつ、失敗したAdaptive Workflowから得られた教訓を統合しました。特に、フルプランの事前生成とタスク間の依存関係に基づくメモリ伝播、LLMのハルシネーションを補完する「確定的（コードベース）な計画検証」、XMLタグを活用した体系的なプロンプトエンジニアリング、そしてシンプルなポリシーエンジンによる意思決定の導入が成功の鍵となりました。

この開発を通じて、シンプルで洗練されたアーキテクチャが最終的に優れた結果をもたらすこと、MCPサーバーの汎用性がいかに強力であるか、そして細部の設計がエージェントの性能を大きく左右するという重要な教訓が導き出されています。ウェブアプリケーションエンジニアにとって、複雑なAIエージェントシステムを構築する際の具体的なアーキテクチャ上の課題と、それらを克服するための実践的なアプローチが示されており、特に確実性とスケーラビリティを求める上で重要な洞察を提供します。