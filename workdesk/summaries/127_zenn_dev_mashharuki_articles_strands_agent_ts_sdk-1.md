## Strands AgentsのTypeScript SDKが登場！AWSでのAIエージェント開発に新たな選択肢を提供

https://zenn.dev/mashharuki/articles/strands_agent_ts_sdk-1

Strands AgentsのTypeScript SDKが発表され、TypeScript開発者がAWS上でAIエージェントを容易に構築・連携できるようになった具体的な方法をデモンストレーションする。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[AI Agent, TypeScript, AWS, SDK, AI開発ツール]]

AWS re:Inventにて、AWSが提供するAIエージェント開発フレームワーク「Strands Agents」のTypeScript SDKが発表されました。これまでPython SDKのみが提供されていたため、TypeScript開発者がAIエージェントを構築する際にはMastraやLangGraph、LangChainといったサードパーティ製フレームワークを利用するのが一般的でした。しかし、このTypeScript SDKの登場により、AWSネイティブのAIエージェント開発に新たな強力な選択肢が加わります。

著者は、この待望のSDKをいち早く試用し、その特徴と具体的な実装方法を解説しています。Strands Agentsは、数行のコードでAIエージェントを実装できる手軽さが特徴で、デフォルトモデルとしてClaude Sonnet 4.5が設定されています。また、外部ツールやModel Context Protocol (MCP) の統合も可能です。実装の流れはMastraに酷似しているため、Mastraに慣れている開発者にとってはスムーズに移行できると著者は指摘しています。現在のところ、対応プロバイダーはClaudeとOpenAIに限定されているものの、今後の拡充に期待が寄せられます。

記事では、以下の具体的なコード例を用いてSDKの基本的な使い方をデモンストレーションしています。
1.  **シンプルな呼び出し**: エージェントを初期化し、質問を`agent.invoke()`で実行する最小限のコード例。
2.  **システムプロンプトの設定**: エージェントの振る舞いを制御する`systemPrompt`を引数に渡して設定する方法。
3.  **レスポンスストリーミング**: `agent.stream()`メソッドを使って、エージェントからの応答を逐次受け取る方法。
4.  **外部ツールの呼び出し**: 天気予報を取得する`get_weather`ツールを定義し、エージェントに登録することで、ユーザーの問い合わせに応じてエージェントが自動的にツールを呼び出す仕組み。
5.  **MCP（Model Context Protocol）の呼び出し**: AWS Document MCPサーバーを利用するための`McpClient`を設定し、エージェントに登録することで、AWSドキュメント検索ツールを呼び出す例。

これらの実践的なデモンストレーションを通じて、Strands Agents TypeScript SDKがいかに簡単にAIエージェントを構築し、外部機能と連携できるかを示しています。著者は、Mastraを使った経験がある開発者ならすぐに慣れるだろうと述べ、AIエージェントをAWS上で稼働させる場合、AgentCoreや他のAWSサービスとの連携を考慮すると、このSDKが非常に強力な選択肢となると結論付けています。