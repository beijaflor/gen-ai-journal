## AWS Lambda + Bedrock + Athena で S3 Tables (Iceberg) に自然言語でクエリするMCPサーバーを構築してみた

https://developers.cyberagent.co.jp/blog/archives/59292/

サイバーエージェントは、AWS Lambda、Bedrock、Athenaを組み合わせ、S3 Icebergテーブルに対してClaudeから自然言語でクエリを実行し、結果を要約して返すMCPサーバーの構築手順を解説しています。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 96/100 | **Annex Potential**: 93/100 | **Overall**: 96/100

**Topics**: [[AWS Lambda, Amazon Bedrock, Amazon Athena, Apache Iceberg, 自然言語クエリ]]

サイバーエージェントのデータインテグレーションチームは、Amazon S3 Tables (Iceberg形式) に自然言語でクエリを実行できるMCP (Model Context Protocol) サーバーを構築した事例を紹介しています。このシステムは、AWS Lambda、Amazon Bedrock (Claude)、Amazon Athenaを組み合わせることで、従来のS3バケット運用と比較してクエリ性能とデータガバナンスの両立を容易にすることを目指しています。

本記事で構築されたサーバーは、Claude（ブラウザ版）から日本語の自然言語クエリを受け取り、BedrockのClaudeがこれをSQLクエリに自動生成します。生成されたSQLはAthenaによってS3上のIcebergテーブルに対して実行され、結果はJSON形式で取得されます。最終的に、Lambda上のMCPサーバーがこのJSON結果とBedrock (Claude) による要約をClaudeに返却することで、非技術者でもデータに素早くアクセスできる環境を実現します。

著者は、この仕組みが特に「締切はいつ？」のような社内のちょっとした問い合わせに対して迅速な応答を可能にし、「データガバナンスや性能改善」に繋がることを強調しています。すべての質問文、生成されたSQL、実行結果は監査ログに残るため、データの利用状況が可視化され、より安全かつ効率的なデータ活用が期待されます。

具体的な構築手順として、IAMロールの作成、IcebergテーブルへのLake Formation権限付与、Lambda関数のPythonコード（Text-to-SQLプロンプトの設計、Athenaでのクエリ実行と結果取得、結果の要約機能を含む）、必要な依存ライブラリのパッケージング、そしてAPI Key認証付きのFunction URL設定が詳細に解説されています。特に、MCPハンドラー (`awslabs.mcp_lambda_handler`) を用いて`test_connection`、`text_to_sql`、`execute_query`、`fetch_query_results`といったツールをClaudeから呼び出せるようにする点が、このソリューションの核となっています。

今後は、クエリバリデーションの追加による安全性向上や、SSO・厳密な権限管理の導入を検討しており、このサーバーレスMCP環境が社内外の自然言語検索やデータ活用に広く貢献する可能性を示唆しています。webアプリケーションエンジニアにとっては、自社データ基盤におけるデータアクセシビリティ向上とガバナンス強化のための具体的なソリューションとして非常に参考になるでしょう。