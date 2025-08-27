## Copilot Studio で Azure のログ調査を Agent 化 #AIOps

https://qiita.com/Isato-Hiyama/items/c463f383b1c0e4f5f2c9

Copilot StudioとAzure Monitor Logsコネクタを活用し、自然言語でAzureログを自動調査・解析するAgentの構築方法と可能性を実証する。

**Content Type**: Tutorial & Guide

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 79/100 | **Overall**: 80/100

**Topics**: [[Copilot Studio, Azure Monitor Logs, AIOps, KQL, Agent-based development]]

この記事は、Microsoft Copilot StudioとAzure Monitor Logsコネクタを用いて、Azure環境における複雑なネットワークログ調査を自動化するAgentの構築手法を具体的に解説しています。ウェブアプリケーションエンジニアが直面する、Azure FirewallやApplication Gatewayなど複数のリソースログを横断して通信問題をトラブルシューティングする課題に対し、自然言語での問い合わせからKusto Query Language (KQL) を自動生成し、ログ解析結果を返すAgentを開発する実践的なアプローチを提示しています。

このアプローチが重要なのは、従来の煩雑で時間のかかる手動ログ分析を大幅に効率化し、AIOpsの実現に向けた具体的な一歩となる点です。記事では、Copilot StudioのInstructionにKQLクエリの生成ルールや特定のログテーブル（AZFWNetworkRule, AGWAccessLogsなど）の検索パターンを詳細に記述する方法が示されており、これによってユーザーは特定のIPからの通信経路やエラー原因などを迅速に特定できるようになります。例えば、「192.168.0.4からの通信がFirewallで正常に処理されたか確認したい」といった自然言語の指示が、Agentによって適切なKQLクエリに変換され、解析結果がテーブル形式で返される様子が示されています。

本稿は、Log Analytics WorkspaceのリソースIDの取得からAgentの作成、Instructionの設定、Azure Monitorコネクタの接続、そしてTeamsでの動作確認まで、詳細な手順を追って解説しており、非常に実践的です。また、Agent化のメリットだけでなく、「ログの中身を理解していないとクエリ指示が難しい」「Instructionの柔軟性にはまだ改善の余地がある」といった実運用上の課題や改善点にも言及しており、現実的な視点を提供しています。複雑なAzure環境での運用効率を向上させたいエンジニアにとって、すぐにでも試せる価値の高い情報です。