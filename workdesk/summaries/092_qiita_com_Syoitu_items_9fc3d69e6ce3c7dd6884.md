## GA版AgentCoreRuntimeにA2A対応AIエージェントをデプロイして詰まったこと! #bedrock

https://qiita.com/Syoitu/items/9fc3d69e6ce3c7dd6884

GA版AgentCoreRuntimeへのA2A対応AIエージェントデプロイ時に、Cognito認証設定のOAuth audience誤入力で認証に失敗した経験を解説し、具体的な解決策と手順を提示します。

**Content Type**: Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 89/100 | **Annex Potential**: 88/100 | **Overall**: 88/100

**Topics**: [[AWS Bedrock AgentCoreRuntime, AI Agent Deployment, Cognito Authentication, A2A, Troubleshooting]]

本記事は、AWS BedrockのAgentCoreRuntimeがGA版となり、A2A（Agent-to-Agent）対応AIエージェントのデプロイが可能になったことを受け、実際にデプロイを試みた際に著者が直面した認証の課題と解決策を詳細に解説しています。TypeScriptのSDKが未提供であることへの言及もありつつ、特にCognito認証設定における特定の落とし穴に焦点を当てています。

著者は、公式ドキュメントのガイドラインに沿ってデプロイを進める中で、認証に数時間を費やしたと述べています。その原因は、認証用のCognitoユーザープール設定時に使用する`agentcore configure`コマンドの対話式設定において、「OAuth audience」の入力欄に誤って「client IDs」の値を入力してしまったことでした。公式ドキュメントではこの箇所に関して十分な説明が不足しており、著者はトークンをデコードして詳細に調査することで、初めてこの問題の根本原因を特定できました。正解は、「OAuth audience」を空欄のままにしておくことでした。

記事では、Cognitoユーザープール、クライアント、テストユーザーを自動でセットアップするシェルスクリプトの具体的な内容と、`agentcore configure`コマンド実行時の正確な入力方法（discovery URLとclient IDsは入力し、OAuth audienceは空欄にする）を丁寧に説明しています。また、デプロイが成功した後、Cognitoから発行されるAccessTokenを使用してデプロイ済みAIエージェントのAgent Cardsを取得する方法も、具体的なPythonスクリプトとともに紹介されています。

この知見は、AWS Bedrock上でAIエージェントを開発・デプロイしようとするウェブアプリケーションエンジニアにとって非常に実用的です。特に、認証のような重要な設定部分でドキュメントの不足や誤解が生じやすい中、著者の具体的なトラブルシューティング経験は、同様の問題に直面する他の開発者の時間と労力を大幅に節約する貴重な情報となります。AIエージェントのA2A連携のような新しい技術を活用する上で、こうした実践的なデプロイノウハウは不可欠です。