## Gemini CLIの全社利用を支える技術

https://techblog.zozo.com/entry/technologies-supporting-company-wide-use-of-gemini-cli

ZOZOは、データプライバシー、コスト、セキュリティの課題を解決し、全社的なGemini CLIの安全かつ効率的な利用を実現する堅牢な管理基盤を構築した。

**Content Type**: 🛠️ Technical

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 96/100 | **Annex Potential**: 94/100 | **Overall**: 96/100

**Topics**: [[Gemini CLI, Google Cloud 管理, IaC, AIツールのコスト管理, GitHub Actions 連携]]

ZOZOが全社的なGemini CLI利用を安全かつ効率的に推進するために構築した管理基盤の詳細を解説しています。本記事は、個々の開発者によるAIツールの活用法ではなく、システム管理者やプラットフォームエンジニアがAIツールの企業導入に伴うデータプライバシー、コスト管理、セキュリティといった運用上の課題をいかに解決したかに焦点を当てています。

認証方式の選定では、入力データが学習に利用されないVertex AI Gen APIを採用し、情報漏洩リスクを排除。全社統一のGoogle Cloudプロジェクトを設定することで、権限管理と費用集計を一元化しています。利用者への権限付与は、GitHubとTerraformを用いたIaC（Infrastructure as Code）で自動化され、申請プロセスを簡素化しています。

特に注目すべきは、AIツールの利用費管理です。Cloud Billingデータと監査ログをBigQueryに集約し、個人や部署ごとの費用を詳細に可視化する仕組みを構築。APIコール数に基づいた費用按分ロジック（SQLクエリ例付き）は、実用的な知見を提供します。また、Cloud Monitoringを用いてリアルタイムでトークン利用量を追跡し、過度な利用があった場合にはSlack通知やDeny Policyによる一時的な権限削除で自動的に制限をかける仕組みを導入し、使いすぎを防止しています。

さらに、GitHub ActionsでのGemini CLIの安全な実行にはWorkload Identity Federationを利用し、認証情報をセキュアに管理。これにより、CI/CDパイプラインでのAI活用を促進します。脆弱性発生時には監査ログから影響範囲を即座に特定できる体制も整備。
この包括的な管理システムは、単にAIツールを導入するだけでなく、企業が直面する現実的な運用課題に対する具体的なソリューションを提示しており、WebアプリケーションエンジニアがAIツールを安心して利用できる環境を裏から支える重要な取り組みと言えます。