## Copilot Studio / Copilot からGoogle DriveのファイルをRAGする - Google Drive Microsoft 365 Copilot コネクタを使おう

https://qiita.com/tomoyasasaki1204/items/9278ffdbf6ad10777c54

**実現する**: Google Drive上のファイルをMicrosoft Graphへインデックス化し、Microsoft 365 CopilotやCopilot Studioでのセマンティック検索と引用付き回答を可能にする環境構築。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[Microsoft 365 Copilot, Google Drive, RAG, Copilot Studio, Microsoft Graph]]

本書は、**Google Drive**に蓄積された組織内データを、**Microsoft 365 Copilot**や**Copilot Studio**のRAGソースとして統合する手法を詳説している。主要な技術要素として、外部データを**Microsoft Graph**に複製・インデックス化する**Microsoft 365 Copilot コネクタ**（旧Graphコネクタ）の仕組みを採用しており、リアルタイムAPI呼び出しを行うPower Platformコネクタとの特性の違いや使い分けについても明確な基準を提示している。

具体的な構築プロセスとして、Google Cloud側での**サービスアカウント**作成や**ドメイン全体の委任**、M365管理センターでの**IDマッピング**（Entra ID UPNとの紐付け）といった、クロスプラットフォーム連携に不可欠なセキュリティ設定を体系的に網羅している。特に、Google Drive側の**ACL（アクセス制御）**を維持したまま、検索結果をユーザーごとに動的にフィルタリングする「セキュリティトリミング」の設定は、エンタープライズ利用において極めて重要な知見である。

Google WorkspaceとMicrosoft 365を併用しており、既存のナレッジベースを移行せずにAIエージェントの回答精度を向上させたいWebエンジニアやインフラ担当者に最適である。