## Strands × MCP × AgentCore Identity使用時のエラー解消メモ

https://qiita.com/har1101/items/f9a12f86ff642f8920c3

Amazon Bedrock AgentCore RuntimeとStrands SDKを組み合わせた自律型エージェント開発において遭遇する、認証トークンの有効範囲やクラス仕様に起因する実装上のエラーと解決策を具体的に解説する。

**Content Type**: Technical Reference
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 82/100 | **Annex Potential**: 75/100 | **Overall**: 80/100

**Topics**: [[Amazon Bedrock, AgentCore Identity, MCP, Strands SDK, AWS Lambda]]

本書は、Amazon Bedrock AgentCore RuntimeとStrands SDKを用いた、スケジュール駆動型の「Ambient Agent（自律型エージェント）」開発における具体的なトラブルシューティングをまとめた技術資料である。著者は、Connpassのイベント情報を収集してLINEへ通知するエージェントの実装過程で直面した、認証とSDKの仕様に関する2つの主要な課題を挙げ、その原因と対処法を提示している。

第一の課題は、AgentCore Identityから認証情報を取得する際の「Workload access token has not been set」エラーである。著者の分析によれば、このエラーの根本原因は、IAM認証（SIGV4）利用時に`RuntimeUserId`パラメータが欠落していること、および`@requires_api_key`デコレーターが`@app.entrypoint`のコンテキスト外（`asyncio.create_task`による非同期タスク内など）では動作しないという仕様にある。著者は、この重要性について、エージェントがバックグラウンドで処理を行う前に、適切に認証情報の取得と受け渡しを行う設計が不可欠であると説いている。具体的な対処法として、EventBridge Schedulerの設定に`RuntimeUserId`を追加し、IAM権限に`InvokeAgentRuntimeForUser`を付与した上で、エントリポイント内で取得した認証情報を引数として非同期タスクへ渡すコードパターンを提示している。

第二の課題は、Strands Agents SDKにおいてMCP（Model Context Protocol）ツールを扱う際に発生する`AttributeError: 'MCPAgentTool' object has no attribute 'name'`である。著者はこの原因を、MCPの標準仕様とStrandsによるラッパークラスの仕様の乖離にあると指摘する。Strandsの`MCPAgentTool`クラスでは、複数のMCPサーバー間でツール名の衝突を避ける「曖昧性排除（Disambiguation）」のために、エージェント側が参照する名前を`tool_name`、サーバー通信用の名前を`mcp_tool.name`として厳密に区別している。このため、従来のように`.name`でアクセスするとエラーになる。著者は、SDKの内部実装を紐解きながら、エージェント側の実装では`tool_name`プロパティを使用すべきであることを結論付けている。

これらの知見は、Bedrock上のエージェント構築において、マネージドな認証基盤と外部プロトコル（MCP）を組み合わせる際の「落とし穴」を回避するための実用的なガイドとなっている。