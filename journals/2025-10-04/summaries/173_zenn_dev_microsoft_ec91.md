## LLM でインフラ管理をサポートしたい

https://zenn.dev/microsoft/articles/ec9190f4449413

Microsoft有志は、LLMを活用し、Azure Arc環境の構成管理、障害対応、ログ分析を効率化するAIチャットアプリケーション「Infra Support Copilot」を開発しました。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[LLM-powered agents, Infrastructure as Code, Azure Arc, Log Analytics, RAG]]

Microsoftの有志が開発したAIチャットアプリケーション「Infra Support Copilot」は、インフラエンジニアが直面する設定管理や障害対応の課題をLLMで解決します。特にAzure Arcで管理されるマルチクラウド環境での、陳腐化したインベントリ情報の検索や、複雑なログクエリ作成の難しさ、類似インシデントの参照不足といった問題に対応します。

このシステムは、ユーザーの入力に基づき、LLMがSQLクエリ実行、AI Searchによる検索、Log Analyticsクエリ実行の3つのツールを動的に呼び出します。例えば、SQLクエリツールでは、Azure SQL Databaseに集約されたAzure Arcのリソース情報をLLMが安全な読み取り専用SQLを生成して取得。AI Searchツールは管理組織や過去の障害情報をRAGで効率的に検索し、Log AnalyticsツールはAzureサービスのログやメトリクスをKQLで分析します。

ウェブアプリケーションエンジニアにとって、このアプローチは運用の自動化と効率化が如何に開発ワークフローを改善するかを示唆します。インフラの健全性を素早く把握し、障害の根本原因分析を加速できるため、開発者はより本来の業務に集中できます。また、LLMによるツール連携とプロンプトエンジニアリングは、アプリケーションレベルでの監視や自動化ツール開発にも応用できる実践的な知見を提供します。azd upを用いた容易な環境構築も、DevOps実践の参考になるでしょう。将来的にSREエージェントが担うような機能をCopilot形式で実装する本プロジェクトは、LLMがコード生成に留まらず、複雑な運用業務を高度に支援する可能性を明確に提示しています。