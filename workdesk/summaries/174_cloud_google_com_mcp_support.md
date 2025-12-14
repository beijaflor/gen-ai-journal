## GoogleサービスでModel Context Protocol (MCP)の公式サポートを発表

https://cloud.google.com/blog/products/ai-machine-learning/announcing-official-mcp-support-for-google-services?hl=en

**Original Title**: Announcing official MCP support for Google services

Googleは、AIエージェントがGoogleの各サービスや企業のAPIを容易に利用できるよう、Model Context Protocol (MCP)の公式サポートとマネージドサーバーの提供を開始しました。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[AIエージェント, Model Context Protocol, Google Cloud, API管理, 開発者ワークフロー]]

Googleは、AIモデルが実際のツールやデータと確実に連携し、複雑なマルチステップタスクを実行する「エージェント」としての能力を向上させるため、Model Context Protocol (MCP)の公式サポートを発表しました。これまで開発者は個別のMCPサーバーを管理する必要があり、実装が脆くなりがちでしたが、今回Googleの既存APIインフラストラクチャにMCPを組み込み、フルマネージドのリモートMCPサーバーとして提供することで、開発者の負担を軽減し、より堅牢なAIエージェントの実装を可能にします。

この新機能は、Google Maps、BigQuery、Google Compute Engine (GCE)、Google Kubernetes Engine (GKE)といった主要なGoogleサービスから段階的に展開されます。例えば、Google Maps PlatformのMaps Grounding Liteを通じて、AIエージェントは地理空間データにアクセスし、現実世界の場所や旅行に関するクエリに正確に回答できます。BigQuery MCPサーバーは、データ移動なしで企業データに対するクエリ実行を可能にし、セキュリティとレイテンシーのリスクを軽減します。GCEおよびGKEのMCPサーバーは、インフラストラクチャのプロビジョニング、サイズ変更、コンテナ操作を自律的に管理する能力をAIエージェントに与え、開発者が複雑なCLIコマンドを組み立てる手間を省きます。

さらに、Apigeeを通じて企業の既存APIスタックにもMCPを拡張することで、組織は自社の開発したAPIやサードパーティAPIを、エージェントが利用可能なツールとして公開・管理できるようになります。これにより、開発者は、BigQueryで売上データを予測しながらGoogle Mapsでビジネスロケーションを調査するといった、より高度なシナリオを容易に構築できます。

Googleは、Cloud API RegistryとApigee API Hubを通じたツールの発見性、Google Cloud IAMによるアクセス管理、監査ログによる可観測性、Google Cloud Model Armorによる脅威防御といったセキュリティとガバナンス機能も強化しています。著者は、MCPサポートの拡大により、開発者がエージェントとデータやアクションを容易に連携させ、AI革命を推進するエコシステムの構築に貢献し、開発者が次のイノベーションに集中できるようになると強調しています。