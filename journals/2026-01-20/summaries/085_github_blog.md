## AIを活用したコミュニティ主導のセキュリティ：セキュリティ研究用オープンソースフレームワーク

https://github.blog/security/community-powered-security-with-ai-an-open-source-framework-for-security-research/

**Original Title**: Community-powered security with AI: an open source framework for security research

AIエージェントを用いて脆弱性調査の自動化とセキュリティ知見の共有を可能にする、オープンソースのセキュリティ研究用フレームワークを提供する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 84/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[GitHub, AIエージェント, セキュリティ研究, MCP, オープンソース]]

GitHub Security Labは、AIエージェントを通じてセキュリティ研究の知見をエンコード、共有、スケールさせるためのオープンソースフレームワーク「GitHub Security Lab Taskflow Agent（seclab-taskflow-agent）」を公開した。これは、自然言語を用いてセキュリティツール（CodeQL等）を操作し、脆弱性調査やバリアント解析（既知の脆弱性に似たパターンの探索）を自動化するための基盤である。

本フレームワークの中核を成すのは「Taskflow」と呼ばれるYAMLファイルだ。これはGitHub Actionsのワークフローに似た構造を持ち、AIエージェントが実行すべき一連のタスクを定義する。各タスクでは、特定の役割を持つ「Personality（性格）」と、外部ツールへのインターフェースである「Toolbox」を組み合わせて使用する。特に、Anthropicが提唱するModel Context Protocol (MCP) を採用しており、LLMがソースコードの閲覧や静的解析ツール、キャッシュシステム等と安全かつ効率的に対話できる仕組みを整えている。

著者がこのツールを公開した背景には、セキュリティ調査を「クローズドなブラックボックス」から「コミュニティ主導のオープンな活動」へと変革したいという強い意志がある。従来の高度なセキュリティ監査は属人的なスキルに依存しがちだったが、Taskflowとしてナレッジをパッケージ化することで、他の開発者が容易に調査プロセスを再現・改良できるようになる。また、研究チーム自身が迅速に実験を行うための「実験場」としての役割も重視されており、洗練された効率性よりも、拡張性や修正の容易さが優先されている。

Webアプリケーションエンジニアにとっての意義は、AIの力を借りて「セキュリティ担当者レベルの高度なコード監査」を自身のワークフローに組み込みやすくなる点にある。すでにCodeQLアラートのトリアージ（優先順位付け）などの実用的なTaskflowも共有されており、自身のプロジェクトに最適化した独自の監査エージェントを構築することも可能だ。Pythonのパッケージエコシステム（PyPI）を利用した配布モデルにより、企業やコミュニティ間での「セキュリティの自動化手順」の共有が加速することが期待される。