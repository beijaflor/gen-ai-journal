## Qwen 3をOllama経由でStrands Agentsで使う！Bedrock AgentCore Runtimeにデプロイできるのか？！

https://qiita.com/moritalous/items/21f12f23f54a271f6138

Qwen 3をOllamaとStrands Agentsで動かし、AWS Bedrock AgentCore Runtimeへデプロイする際、多層Webサーバー構成とコンテナサイズ制限という課題を克服した具体的な手法を詳述する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[Ollama, Strands Agents, AWS Bedrock AgentCore Runtime, LLM Deployment, コンテナ化]]

小規模LLMをローカルで手軽に動かすOllamaと、AWSがOSS提供するエージェントフレームワークStrands Agentsを組み合わせ、Qwen 3（0.6B）モデルを動かす実践的な記事です。Webアプリケーションエンジニアにとっての核心は、このローカル環境で動くAIエージェントを、サーバーレスなAWS Bedrock AgentCore Runtimeへデプロイしようと試みる点にあります。

特に重要なのは、デプロイ時に直面した二つの大きな技術的課題と、その具体的な解決策です。一つ目は、Ollama自身がWebサーバーとして動作する上、Strands AgentsのアプリケーションもWebサーバーとして機能するため、単一のコンテナ内で二つのWebサーバーを協調動作させる必要があった点です。これには`supervisor`を導入することで対応しています。二つ目は、Bedrock AgentCore Runtimeのコンテナイメージサイズ1GBという厳格な制限です。OllamaのデフォルトインストールにはGPU利用のためのCUDAライブラリが含まれており、これがサイズ超過の原因となります。筆者はこれらの不要なライブラリを削除することで、なんとか1GBの壁をクリアし、デプロイに成功しています。

この試みは、Qwen 3のような特定のLLMやカスタムエージェントをAWSのマネージドサービスで動かしたいと考えるエンジニアにとって、極めて実践的な知見を提供します。現状ではAgentCore RuntimeでのGPU活用やコンテナサイズ制限といった課題は残るものの、ローカルで動くAIエージェントをクラウドに持ち込むための具体的なステップと、その際の落とし穴、そして回避策が示されており、今後のエージェント開発・運用における参考になるでしょう。