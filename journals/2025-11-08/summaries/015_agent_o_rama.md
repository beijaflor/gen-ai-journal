## Agent-o-rama発表：JavaまたはClojureでステートフルLLMエージェントを構築、追跡、評価、監視

https://blog.redplanetlabs.com/2025/11/03/introducing-agent-o-rama-build-trace-evaluate-and-monitor-stateful-llm-agents-in-java-or-clojure/

**Original Title**: Introducing Agent-o-rama: build, trace, evaluate, and monitor stateful LLM agents in Java or Clojure

Red Planet Labsは、Java/Clojure開発者向けに、スケーラブルでステートフルなLLMエージェントの構築、追跡、評価、監視を一貫して行うオープンソースライブラリ「Agent-o-rama」を発表しました。

**Content Type**: Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[LLMエージェント, JVM開発, エージェントトレーシング, エージェント評価, 状態管理]]

Red Planet Labsは、JVM上でスケーラブルかつステートフルなLLMエージェントを構築するためのオープンソースライブラリ「Agent-o-rama」を発表しました。現在のAIツールエコシステムはPythonが中心であり、LangChain4jのようなライブラリがJVMに提供されてきたものの、LLMベースのシステムを厳密に評価、監視、展開するための統合ツールが不足していました。Agent-o-ramaは、LangGraphやLangSmithのコンセプト（構造化エージェントグラフ、トレーシング、データセット、実験、評価）をJavaとClojureにネイティブに導入することで、このギャップを埋めます。

著者は、LLMが強力であると同時に予測不可能な性質を持つため、実用的で高性能なLLMアプリケーションを構築するには、厳密なテストと監視が不可欠であると強調しています。Agent-o-ramaでは、エージェントはJavaまたはClojure関数のシンプルなグラフとして定義され、並列実行されます。本ライブラリは詳細なトレースを自動的にキャプチャし、オフライン実験、オンライン評価、モデル遅延やトークン使用量などの時系列テレメトリーのためのWeb UIを内蔵しています。また、モデル呼び出しやノードからのリアルタイム出力をストリーミングするためのシンプルなクライアントAPIもサポートしています。

Agent-o-ramaは、LangGraphやLangSmithのアイデアをさらに拡張し、はるかに優れたスケーラビリティ、完全な並列実行、そして高性能なデータストレージとデプロイメントを組み込んでいます。これは、依存関係としてRamaクラスターにデプロイされ、すべてのデータとトレースはユーザーのインフラストラクチャ内に保持されます。Ramaの強力な分散プログラミングモデルを、その学習曲線なしにLLMエージェントの構築に活用できる点が、本ツールの大きな利点です。これにより、JVM開発者は使い慣れた環境で、堅牢かつ観測可能なLLMエージェントの開発から運用までを一貫して行えるようになります。