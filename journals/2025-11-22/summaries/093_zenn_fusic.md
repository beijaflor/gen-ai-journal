## Amazon Bedrock AgentCore Runtimeで zip ファイルを直接アップロードでデプロイしてみた

https://zenn.dev/fusic/articles/a8dcab7caf9904

Amazon Bedrock AgentCore Runtimeがzipファイルでの直接デプロイに対応し、AIエージェントの開発と検証サイクルを効率化します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 77/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[Amazon Bedrock AgentCore, AIエージェントデプロイ, Strands Agents, ZIPデプロイ, AWS Lambdaライク]]

Fusicのレオナ氏によるこの記事は、Amazon Bedrock AgentCore Runtimeに新たに追加された、AIエージェントをZIPファイルとして直接デプロイできる機能について解説しています。従来、AIエージェントのデプロイにはコンテナイメージをAmazon ECRにプッシュする必要がありましたが、今回のアップデートにより、Amazon S3バケットを介してZIPファイルをアップロードする形式が選択可能になりました。これにより、デプロイプロセスが大幅に簡素化され、開発者は検証サイクルを迅速に回せるようになります。

デプロイ方法には「Start with a template」「Upload to S3」「Choose from an existing S3 bucket」の3つの選択肢があり、筆者はこのうち「Upload to S3」に焦点を当て、具体的な手順をデモンストレーションしています。実装例では、2025年5月に公開されたAWSのオープンソースAIエージェント構築SDKであるStrands Agentsを使用し、シンプルな質問応答エージェントを構築します。

具体的な実装ステップとして、まず`uv`ツールを用いてARM64アーキテクチャ向けに`bedrock-agentcore`と`strands-agents`の依存関係を`deployment_pkg`ディレクトリにインストールします。次に、このディレクトリ内にエージェントのエントリーポイントとなる`main.py`ファイルを作成し、Strands Agentsを使ってペイロードからのプロンプトに応答するロジックを記述します。最後に`deployment_pkg`ディレクトリ全体をZIPファイルに圧縮します。

デプロイはAWSマネジメントコンソールから行い、生成されたZIPファイルを直接アップロードし、エントリーポイントとして`main.py`を指定、Python 3.13ランタイムを選択してホストエージェントを作成します。デプロイが完了すれば、サンドボックス環境でAIエージェントの動作確認が可能になります。

著者は、このZIPファイルによる直接デプロイ機能がAWS Lambdaと同様の手軽さをAIエージェント開発にもたらし、検証サイクルを効率化する点で非常に重要であると強調しています。特に、AIエージェント開発における反復作業の障壁を低減し、より迅速なプロトタイピングと改善を可能にする点が、ウェブアプリケーションエンジニアにとって大きなメリットとなるでしょう。