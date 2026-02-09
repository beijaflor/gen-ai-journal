## 閉域内に Bedrock と MCP を使った Streamlit アプリを ECS Express モードでデプロイする

https://qiita.com/takeda_h/items/6c57a34453d01346478d

AWSの閉域環境において、BedrockとMCPを活用したStreamlitアプリをECS Expressモードで構築・デプロイする具体的な手順を解説する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 85/100 | **Overall**: 84/100

**Topics**: [[AWS, Amazon Bedrock, MCP, Amazon ECS, 閉域網]]

ガバメントクラウドなどのインターネット接続が制限された閉域網において、**Amazon Bedrock**と**MCP (Model Context Protocol)**を組み合わせた生成AIエージェントを構築するための実践的なガイドです。**ECS Expressモード**を活用し、コンテナオーケストレーションやロードバランサーの設定を簡略化しつつ、セキュアなインフラを構築する手法に焦点を当てています。

主な内容は、**Amazon ECR**や**Amazon Bedrock**への接続を維持するための**VPCエンドポイント**の構成、およびインターネット経由でのPyPI利用が不可能な環境における代替策です。具体的には、**AWS CodeArtifact**をPyPIのアップストリームとして設定し、**uvx**コマンド実行時にVPCエンドポイント経由でMCPサーバー（**Fetch MCP Server**）を起動させるための認証トークンの取得と設定コードが紹介されています。また、外部通信を前提とする既存のMCPツールが閉域環境では動作しないという制約に対し、イントラ内のWebコンテンツ要約に特化した構成への変更など、実務的な回避策も示されています。

セキュリティ要件の厳しいエンタープライズ環境や公共セクターで、AIエージェントの検証・導入を検討しているインフラエンジニアやWebアプリケーション開発者に最適な内容です。