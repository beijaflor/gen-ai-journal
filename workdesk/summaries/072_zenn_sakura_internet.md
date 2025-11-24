## A2A （Agent2Agent) プロトコルを基礎から学ぶ (1) LLM を使わない複数Agentのサンプル

https://zenn.dev/sakura_internet/articles/e29d64a9d211a4

Googleが提唱するA2A（Agent2Agent）プロトコルを、LLMなしの具体的なサンプルコードで基礎から解説します。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 77/100 | **Annex Potential**: 74/100 | **Overall**: 76/100

**Topics**: [[A2Aプロトコル, エージェント間通信, マルチエージェントシステム, LLMエージェント, JSON-RPC]]

2025年4月にGoogleが発表したA2A（Agent2Agent）プロトコルは、これまで個別に動作していたAIエージェント間の共通言語を提供し、企業内のサイロ化問題を解決することを目指しています。LLMと対話や外部ツール連携（RAG/MCP）が可能な「エージェント」が部門ごとに乱立する中、A2Aはこれらエージェント同士を連携させる標準規格として機能します。

著者は、MCP（Model Context Protocol）がLLMとツール・データを接続するのに対し、A2Aはエージェント同士を接続し、複数のエージェントが連携して複雑なタスク（例：新入社員の入社手続き）を一気通貫で実行可能にする、とその重要性を強調しています。Amazon Bedrock AgentCoreもA2Aのサポートを表明しており、このプロトコルが今後のマルチエージェントシステムの中心的な存在となることは間違いなさそうです。

記事では、A2Aの基本的な通信方式がJSON-RPCであること、そしてエージェントの機能やスキルを記述した「Agent Card」が`/.well-known/agent.json`で公開される仕組みを解説しています。さらに、エージェントの状態管理には`submitted`、`working`、`completed`など7種類のTask Stateが定義されており、デフォルトで非同期呼び出しが採用されていることも説明しています。

本記事の最も重要な点は、あえてLLMを使わないA2A連携のサンプルコード（Node.js, Express）を提供していることです。これは、本来エージェントがLLMを活用することが前提でありつつも、A2Aの「エージェントが他のエージェントをどう発見し、タスクを依頼するか」というプロトコル自体の仕組みを純粋に学ぶための工夫です。このサンプルを通じて、Agent AがAgent BのAgent Cardを取得し、タスクを生成・ポーリングして結果を受け取る一連のフローを具体的に理解できます。これにより、開発者はLLMの実装に入る前に、A2Aプロトコルによるエージェント間連携のコアロジックを習得できます。