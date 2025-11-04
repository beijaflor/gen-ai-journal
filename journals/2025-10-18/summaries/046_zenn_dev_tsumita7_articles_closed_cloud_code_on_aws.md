## AWS Bedrockを利用して、AWSの日本国内に閉じてClaude Codeを利用しよう！！

https://zenn.dev/tsumita7/articles/closed-cloud-code-on-aws

強固なセキュリティ要件を持つ開発者向けに、AWS Bedrock上でClaude Codeを日本国内の閉域環境で利用するための詳細な構築手順をTerraformを用いて解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[AWS, Bedrock, Claude Code, 閉域網, Terraform, EC2, VPC]]

この記事は、何らかの事情でClaude CodeをAWSの日本国内に閉じた形で利用したい開発者向けに、その環境構築方法を詳細に解説しています。著者によれば、2025年10月17日現在、日本国内で利用可能なモデルはClaude Sonnet/Haiku 4.5に限定されているという制約を冒頭で明確に示しつつ、この制約下でどのようにセキュアな閉域環境を構築するかを説明しています。

構築手順は主に以下の3つのフェーズに分かれています。まず、Node.js、npm、そしてClaude Codeが導入されたAmazon Linux 2023のAMIを作成します。これにより、必要な開発ツールが事前に準備された基盤が確立されます。次に、AWSのVPC、サブネット、ルートテーブル、セキュリティグループ、IAMロール、そしてAWS Bedrockランタイム用のVPCエンドポイントを含む閉域環境をTerraformで構築します。このTerraformコードは、EC2インスタンスがVPC内部からのみBedrockサービスにアクセスできるように設計されており、高いネットワークセキュリティとデータレジデンシー要件に対応します。最後に、構築したEC2インスタンスにAWS Systems Manager (SSM) で接続し、Claude Codeを起動するための環境変数（`CLAUDE_CODE_USE_BEDROCK=1`、`ANTHROPIC_MODEL=jp.anthropic.claude-haiku-4-5-20251001-v1:0`など）を設定することで、閉域環境下でのClaude Codeの利用が可能になります。

この構築ガイドは、企業がデータガバナンスやセキュリティポリシーを厳格に遵守しながら、AIコーディング支援ツールを導入する際の具体的な解決策を提供します。特に、AWSの日本国内リージョンに閉じ込めることで、データ所在地の要件を満たし、安心して生成AIツールを利用できる点が重要です。