## Claude Code on Amazon Bedrock の利用状況の可視化とコスト管理

https://zenn.dev/aws_japan/articles/2862581173159a

Amazon Bedrockで利用するClaude Codeのコストを個人レベルで可視化し、予算超過アラートを設定する方法を解説します。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 79/100 | **Overall**: 80/100

**Topics**: [[AWS Bedrock, Claude Code, コスト管理, 利用状況可視化, AWS Budgets]]

この記事では、Amazon Bedrock上でClaude Codeを使用する際のコスト管理と利用状況の可視化という、ウェブアプリケーションエンジニアにとって重要な課題への具体的な解決策を提示しています。従量課金制のBedrockは手軽に利用できる一方で、「誰がどれだけ使ったのかを把握したい」「一定額を超過したら通知が欲しい」といった運用上のニーズが生まれがちです。本稿は、これらの課題を解決するために「アプリケーション推論プロファイル」と「AWS Budgets」を組み合わせる方法を詳細に解説しています。

まず、利用者のコストを追跡するための「アプリケーション推論プロファイル」をAWS CLIを使用して作成します。このプロファイルはClaude SonnetやHaikuといったモデルごとに、利用者を識別するための任意のタグ（例: `EngineerName=yamary`）を付けて生成することが重要です。これにより、後からコストをユーザー単位でフィルタリングすることが可能になります。作成したプロファイルのARN（Amazonリソースネーム）は、Claude Codeの`settings.json`ファイル内の`ANTHROPIC_MODEL`および`ANTHROPIC_DEFAULT_HAIKU_MODEL`に設定を更新することで、Claude Codeがこのプロファイルを介してBedrockを利用するようになります。この設定により、個別の利用状況が追跡可能となる点が最大のポイントです。

次に、利用状況の可視化です。Billing Consoleで先ほど作成したコスト配分タグを有効化することで、最大24時間後にはAWS Cost Explorerでタグごとに利用料金を確認できるようになります。エンジニアはここで「EngineerName」タグを選択することで、自身の、またはチームメンバーごとのClaude Code利用コストを一目で把握できます。これは予期せぬ高額請求を防ぐ上で非常に役立ち、コスト意識の向上にも繋がります。

最後に、予算超過アラートの設定です。AWS Budgetsを利用して、Bedrockの利用コストに特化した予算を設定します。ここでは、タグでフィルタリングして個人単位の予算を設定したり、実際のコストが予算の80%などのしきい値に達した際にAmazon SNS経由でメール通知を受け取るように設定したりできます。これにより、予算を超過する前にプロアクティブにコストを管理し、安心してClaude Codeを開発に活用できる環境が構築されます。これらの仕組みは、開発チームがコストを意識しつつ、生成AIツールを最大限に活用するために不可欠なプロセスです。