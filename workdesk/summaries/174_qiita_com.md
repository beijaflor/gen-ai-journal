## AIエージェント歴1か月 - AgentCore/Strands Agents/Streamlitでインフルエンサー検索エージェントを作成する

https://qiita.com/Yoshi1001/items/d1079e4a5cfad0073c12

**AgentCore**と**Strands Agents**を活用し、外部ツール連携と記憶保持機能を備えた実用的なインフルエンサー検索エージェントの構築手法を解説する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 94/100 | **Annex Potential**: 91/100 | **Overall**: 72/100

**Topics**: [[AIエージェント, AgentCore, Strands Agents, Streamlit, Auth0]]

本記事は、学習開始から1ヶ月で**AgentCore**および**Strands Agents**を用いたインフルエンサー検索エージェントを構築した開発記です。マーケティング業務におけるインフルエンサー調査の自動化を目的としており、単なる検索に留まらず、PR戦略の提案まで行うエージェントの実装過程が共有されています。

技術構成として、UIには**Streamlit**、認証基盤に**Auth0**を採用。バックエンドでは**AWS Bedrock**を基盤とした**AgentCore**を活用し、**AgentCore Memory**による長期記憶の保持を実現しています。これにより、過去の検索結果に対するフィードバックを次回の提案に反映させる高度な対話が可能です。また、**Streamlit Community Cloud**へのデプロイ時における**secrets.toml**の管理や、**Auth0**との統合に関する具体的なTipsは、同様の構成を検討するエンジニアにとって即戦力となる情報です。

今後は**AgentCore Identity**による機密情報管理や、各ツールの**AWS Lambda**移行による疎結合化を目指すと述べており、スケーラブルなエージェント設計の道筋も示されています。**AgentCore**を用いた実用的なエージェント開発の全体像を把握したいエンジニアに最適な内容です。