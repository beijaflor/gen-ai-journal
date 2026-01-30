## AIエージェント「Taskflow Agent」による脆弱性選別の自動化：GitHub Security Labの実践

https://github.blog/security/ai-supported-vulnerability-triage-with-the-github-security-lab-taskflow-agent/

**Original Title**: AI-supported vulnerability triage with the GitHub Security Lab Taskflow Agent

**Taskflow Agent**と**MCP**を連携させ、LLMの文脈理解能力によってセキュリティアラートの選別作業（トリアージ）を高度に自動化します。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[GitHub Security Lab, Taskflow Agent, MCP, Vulnerability Triage, CodeQL]]

**GitHub Security Lab**が、セキュリティアラートのトリアージを自動化するAIエージェントフレームワーク「**Taskflow Agent**」の実践手法を公開しました。従来、**CodeQL**などの静的解析ツールが生成する大量のアラートから「偽陽性（False Positive）」を排除する作業は、人間の専門家による反復的な判断が必要でした。本手法は、LLMが持つコードのセマンティクス（意味論）理解能力を活用し、このプロセスを構造化されたタスクフローとして自動化します。

技術的な核心は、YAML形式で定義された**Taskflow**による多段階処理です。処理を**情報収集**、**監査（Audit）**、**レポート生成**、**バリデーション**というステップに分解し、各段階でLLMに具体的な指示を与えます。特に、GitHub API操作やファイル検索などの確定的な処理は**MCP (Model Context Protocol)**サーバーに委譲し、LLMには権限チェックの論理検証などの複雑な判断に集中させることで、ハルシネーションを抑制しつつ高い一貫性を実現しています。

実際に**GitHub Actions**やJavaScriptの脆弱性調査に投入され、約30件の現実の脆弱性を発見する成果を上げています。中間状態を**データベース**に保存し失敗時の再試行を容易にする設計や、既存のレポートを基にしたGitHub Issueの自動作成機能など、実務に即した知見が凝縮されています。大規模なコードベースのセキュリティ管理を担当するエンジニアや、AIエージェントによる自動化ワークフロー構築に興味がある開発者に強く推奨されます。