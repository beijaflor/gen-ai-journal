## LLM 機能を支える Langfuse / ClickHouse のサーバレス化

https://speakerdeck.com/yuu26/20250808-yurusre

LayerXは、LLM機能の計測基盤としてLangfuseとClickHouseをAWS Fargate上でサーバレス化し、個別ECSサービス構成とEFSスループットモード変更で安定稼働を実現した。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 96/100 | **Annex Potential**: 93/100 | **Overall**: 96/100

**Topics**: [[LLMOps, Langfuse, ClickHouse, Serverless Architecture, AWS Fargate]]

LayerXは、AI申請レビュー機能のリリースに伴い、そのLLM開発・検証・計測基盤としてLangfuseとClickHouseをAWS Fargate上にサーバレスで構築した。これは、プロンプトのバージョン管理やモデルごとの精度検証など、LLMOpsの要となる機能を提供する。

特に注目すべきは、ClickHouseの分散構成をFargate上で実現するための工夫だ。サーバごとに異なる`server_id`の指定が必要な点や、クラスタ内の1:1通信が必須となる点が課題だった。LayerXはこれを解決するため、ClickHouseおよびClickHouse Keeperの各インスタンスを個別のECS Serviceとして構築し、ECS Service Discoveryによってサービス間の直接通信を可能にした。これにより、ロードバランサを介さずに特定のインスタンスを指定できる堅牢なインフラが完成した。

しかし、稼働後にLangfuseからClickHouseへの書き込みタイムアウトが頻発するパフォーマンス問題が発生。原因調査の結果、ClickHouseのデータ格納先であるEFSのスループットモードが「Bursting」になっており、初期使用量では十分なスループットが得られていなかったことが判明した。これを「Elastic」モードへ変更することで、EFSのボトルネックが解消し、システム全体の安定稼働とLangfuseでの高速な操作が実現した。

この事例は、LLM計測基盤のサーバレス化における具体的な設計指針と、分散データベースのFargate運用で直面しがちな課題、そしてストレージ設定の見落としといった実用的な教訓を提供する。LLMOpsインフラを構築するウェブアプリケーションエンジニアにとって、実装の詳細からトラブルシューティングまで、多岐にわたる知見が得られるだろう。