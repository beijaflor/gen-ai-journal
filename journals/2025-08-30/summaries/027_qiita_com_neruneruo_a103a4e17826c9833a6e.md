## Auth0＋Amazon Bedrock AgentCore Identityの認証をTerraformで構築する

https://qiita.com/neruneruo/items/a103a4e17826c9833a6e

Amazon Bedrock AgentCoreのGatewayを使わずにAuth0とTerraformでWorkload Identityを直接操作し、AIエージェントの認証を構築する具体的な方法と技術的課題の解決策を詳述します。

**Content Type**: Tutorial & Guide

**Scores**: Signal:4/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 94/100 | **Annex Potential**: 92/100 | **Overall**: 92/100

**Topics**: [[Amazon Bedrock AgentCore Identity, Workload Identity, Auth0認証, Terraform, AIエージェントセキュリティ]]

この記事は、Amazon Bedrock AgentCoreの認証システムにおいて、通常推奨されるGatewayを利用せず、Auth0とTerraformを組み合わせてWorkload Identityを直接操作する高度な認証構築手法を深掘りしています。ウェブアプリケーションエンジニアにとって、AIエージェントのセキュリティは極めて重要であり、この記事はより柔軟な認証フローを実装するための具体的な指針を提供します。

著者は、Auth0でUser Federation認証（JWT発行）とMachine to Machine (M2M) 認証を設定し、これらをBedrock AgentCoreのWorkload Identityと連携させるプロセスを詳細に解説。特に重要な発見として、Workload Identityのトークン発行APIをユーザーコンテキストで利用する際に、Bedrock AgentCoreのコントロールプレーンではなくデータプレーンの`endpoint_url`を直接指定するというSDK内部でも用いられる「裏技」を明かしています。これにより、コントロールプレーンで作成されたリソースがユーザー主導のトランザクションでアクセスできないという課題を克服しています。

また、Terraformを用いたIaC（Infrastructure as Code）でAuth0のクライアントやリソースサーバー、AWS IAMポリシーを定義し、Bedrock AgentCoreのOAuth2 Credential ProviderとWorkload Identityを構築する具体的なコードが示されています。`terraform destroy`時にWorkload Identityが自動削除されない問題への対処法として、`terraform_data`リソースと`local-exec`プロビジョナーを利用した明示的な削除スクリプトを導入する堅実なアプローチも提示されています。

この手法の「なぜ重要か」は、Gatewayに依存しないことで、より高度なセキュリティ要件や既存のIDプロバイダーとの統合が求められる複雑なエンタープライズ環境において、AIエージェントの認証をきめ細かく制御できるようになる点です。さらに、M2M認証で`customParameters`を設定できないSDKの制約や、Auth0 JWTトークンが有効期限内でも都度認証が発生するというBedrock AgentCoreの現在の仕様上の課題（APIコール数による課金に影響）にも言及しており、実運用における注意点を明確に示唆することで、開発者は将来的なコストやシステム設計における潜在的な問題を事前に考慮できます。