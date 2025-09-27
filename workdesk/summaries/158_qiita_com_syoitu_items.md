## CDKでもAgentCoreをデプロイしたい - Mastra & StrandsAgents #AWS

https://qiita.com/Syoitu/items/65fda40c75dd467b5cd7

AWS CDKを用いてStrands AgentsとMastraフレームワークで構築したAIエージェントをAWS Bedrock AgentCoreにデプロイする具体的な手順を解説する。

**Content Type**: 📖 Tutorial & Guide

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 79/100 | **Overall**: 80/100

**Topics**: [[AWS CDK, AWS Bedrock AgentCore, AI Agent Deployment, Mastra Framework, Strands Agents]]

AWS Bedrock AgentCoreがCloudFormationに対応したことで、Infrastructure as Code (IaC)によるデプロイがAWS CDKで可能になったことは、AIエージェント開発において非常に大きな進展です。これは、エージェントのデプロイプロセスをコードで管理し、自動化・再現性を高める上で極めて重要であり、特にPython以外の言語で構築されたAIエージェントにとって、CDKによるデプロイパスが確立されたことは、運用効率の向上に直結します。

この記事では、この新機能を活用し、PythonベースのStrands AgentsとTypeScriptベースのMastraという異なるAIエージェントフレームワークをAgentCoreにデプロイする具体的な手順を、豊富なコード例と共に解説しています。Strands Agentsの例では、CDKスタックでのIAMロール定義やDockerイメージ（ECR Asset）の利用方法をL1 Constructで示し、Mastraの例では、AI SDK for Bedrockを用いたエージェントの実装に加え、AgentCoreからの呼び出しに対応するExpress APIサーバーの構築、Dockerfile作成、環境変数設定といった実践的なステップが詳細に紹介されています。

この具体的な実装例は、Webアプリケーションエンジニアにとって実用価値が高く、これまで手動で行っていたエージェントのデプロイ作業をCDKに移行することで、CI/CDパイプラインへの組み込みや、複数環境への一貫した展開が容易になります。特にMastraのようにTypeScript/JavaScriptエコシステムで開発されているAIエージェントをBedrock AgentCoreにデプロイしたい開発者にとっては、そのまま利用できる貴重なリファレンスとなるでしょう。Python以外の言語でAIエージェントを運用しようと考えているチームにとって、このCDKによるデプロイ手法は、将来的な開発・運用効率を大きく左右する重要な選択肢となります。ただし、著者はPython製フレームワークに関してはBedrock AgentCore Starter Toolkitの方が使いやすいと述べており、状況に応じたツールの選定が求められます。