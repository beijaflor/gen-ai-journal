## LLMを駆使したSlackbotによる例外アラート調査・分析の自動化

https://techblog.zozo.com/entry/llm-slackbot

ZOZOは、LLMとマルチエージェント構成のSlackbotを活用し、複雑なシステムにおける例外アラート調査とデプロイエラー分析の自動化を実現しました。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[LLM運用自動化, Slackbot開発, マルチエージェントシステム, アラート調査効率化, Strands Agents]]

ZOZOは、イベント駆動/CQRSパターンによるシステム複雑性の増大と、複数のプロダクト運用に伴う高い認知負荷という課題に対し、LLM（Claude Sonnet 4）とMCP（Model Context Protocol）を活用したSlackbotを導入しました。このSlackbotは、AWSが提供するStrands Agentsを用いたマルチエージェント構成が特徴で、技術的な調査・分析を担うWorker Agentと、その結果をSlack向けに最適化するMediator Agentが連携します。

本アプローチの重要な点は、人間が行う「情報収集→分析→判断」のサイクルを自動化し、エンジニアの認知負荷を大幅に軽減できることです。具体的には、Sentryからのエラー情報収集、GitHubからの関連コード探索、そして問題特定から修正案の分析までをWorker Agentが担当。これにより、複雑なイベント駆動システムの障害調査やデプロイエラーの根本原因特定が飛躍的に効率化されました。さらに、エラー内容に基づいたGitHub Issueの自動作成機能は、修正作業の開始を加速し、将来的にはコーディングエージェントと連携した完全自動修正の可能性も示唆しており、開発ワークフローに大きな変革をもたらします。Strands Agentsの採用は、学習コストを抑えつつ既存のAWSインフラと統合しやすい実践的なエージェント開発手法を示しており、LLMを活用した運用改善の具体的な事例として、その実用性と課題（コスト最適化）を明確に示しています。