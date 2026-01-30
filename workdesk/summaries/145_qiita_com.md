## Bedrock AgentCoreのデプロイツールがTypeScriptに対応！ 宇宙最速で試してみた

https://qiita.com/minorun365/items/57fb0da7257d9875409c

AWS Bedrock AgentCoreのデプロイツールキットがTypeScriptに対応したことを受け、プロジェクトの初期化からデプロイ、動作確認までの手順を速報として紹介する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[AWS Bedrock, AgentCore, TypeScript, AI Agents, Strands SDK]]

AWSのAIエージェント開発環境「**Bedrock AgentCore**」のデプロイツールキットが**TypeScript**プロジェクトをサポートしました。これまでPython主体だったエージェントの開発・デプロイフローが、**Express.js**と**Strands Agents SDK**を組み合わせることで、Webエンジニアに馴染みのあるTypeScriptスタックで完結可能になった点は大きな変更点です。

記事では、`npm init`による依存パッケージ（**@strands-agents/sdk**など）の導入から、**tsconfig.json**の設定、エージェントをAPIサーバー化する具体的なコード例、そして`agentcore deploy`コマンドによるAWSへの展開手順が、ソースコード付きで簡潔に解説されています。最後に`agentcore invoke`を用いて**Claude**からのレスポンスを確認するまでの一連のワークフローが網羅されており、開発者が即座に手元で試せる構成になっています。

AWS上で生成AIエージェントを迅速にプロトタイピング・デプロイしたいTypeScriptエンジニアにとって、実装のハードルを下げる有益な実戦ガイドです。