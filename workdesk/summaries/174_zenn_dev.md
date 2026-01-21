## AgentCore Gateway で MCP サーバー・ツールのアクセス制御を実現する 3 つの方法の徹底比較

https://zenn.dev/aws_japan/articles/003-bedrock-agentcore-policy-fgac

Amazon Bedrock AgentCore Gateway において、MCP ツールの実行権限をユーザー属性に基づき詳細に制御（FGAC）するための 3 つの実装アプローチを技術的・定量的側面から比較解説する。

**Content Type**: Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 94/100 | **Annex Potential**: 91/100 | **Overall**: 92/100

**Topics**: [[Amazon Bedrock, MCP, AWS CDK, アクセス制御, セキュリティ]]

Amazon Bedrock AgentCore Gateway を活用した AI エージェント運用において、Model Context Protocol（MCP）サーバー上の各ツールに対する詳細なアクセス制御（Fine-grained Access Control: FGAC）を実現するための 3 つの主要な手法を、AWS のスペシャリストが比較・検証している。

著者は、エンタープライズ環境でのエージェント導入において「誰がどのツールを実行できるか」というセキュリティ管理が不可欠になると説く。具体的には、JWT を用いた「Inbound authorization」、Cedar ポリシー言語を活用するマネージドな「AgentCore Policy」、そして Lambda で柔軟なロジックを実装できる「AgentCore Gateway interceptors」の 3 手法について、実装コード（CDK/Python）と共に解説している。

各手法の特性について、著者は以下のように結論付けている。
1. **Inbound authorization**: 設定が容易でレイテンシーも最小だが、制御単位が Gateway 単位に限定される。Gateway 自体へのアクセス制限には適しているが、ツール単位の細粒度な制御はできない。
2. **AgentCore Policy**: Cedar を用いることで、コードを書かずに宣言的なツール単位の制御（FGAC）が可能。`list/tools` の結果から権限のないツールを自動除外する機能もあり、基本的にはこの手法を第一候補とすべきである。
3. **AgentCore Gateway interceptors**: Lambda 実装が必要でコストは高いが、外部 DB との動的連携、PII（個人情報）の除去、Semantic Search 結果の加工など、標準機能では不可能な高度なカスタマイズに対応できる。

さらに、著者は各手法のオーバーヘッドを実測し、Policy で約 134ms、Interceptors で約 207ms の追加レイテンシーが発生することを明らかにしている。単一リクエストでの体感差は小さいが、累積を考慮した選択が必要だ。最終的な指針として、まずは実装の容易な AgentCore Policy を検討し、複雑な認可ロジックや入出力加工が求められる特殊なユースケースにおいてのみ Interceptors を選択するという、極めて実践的な選定基準を提示している。