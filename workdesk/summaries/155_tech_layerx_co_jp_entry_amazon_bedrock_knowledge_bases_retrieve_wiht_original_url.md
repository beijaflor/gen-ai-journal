## Amazon Bedrock Knowledge Basesで実現する"元のリンクとセット"で検索できるRAG

https://tech.layerx.co.jp/entry/amazon-bedrock-knowledge-bases-retrieve-wiht-original-url

Amazon Bedrock Knowledge BasesでRAGシステムを構築する際、生成AIの回答に元の情報源URLを付与することで、回答の信頼性と検証可能性を劇的に向上させる革新的な手法を提案します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 88/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Amazon Bedrock, RAG, Knowledge Bases, Metadata Management, AI Agent Development]]

この記事は、Amazon Bedrock Knowledge Basesを活用したRAG（Retrieval-Augmented Generation）システムにおいて、AIが生成した回答の信頼性を高めるため、その情報源となる「元のリンク」を付与する実践的な手法を詳述しています。RAGの能力は高いものの、検索結果が常に絶対的に正しいとは限らず、誤った情報源を元にAIがあたかも正しいかのように回答してしまう「ハルシネーション」のリスクは無視できません。エンドユーザーがAIの回答の真偽を検証できない場合、システム全体の信頼性が損なわれる深刻な問題となります。

著者は、Knowledge Basesの`retrieve` APIレスポンスが、データソースがS3の場合に内部的なS3パスしか提供しないという課題を指摘。これに対し、本来検索フィルタリングのために設計されたKnowledge Basesのカスタムメタデータ機能を逆転の発想で活用することを提案します。具体的には、S3に保存するソースデータファイルと対になるメタデータファイル（`.metadata.json`）に、`"original-url": "<元のWebページのURL>"`といった形で、情報源のURLをカスタムメタデータとして付与します。

この工夫により、`retrieve`実行時の結果に元のURLが含まれるようになり、AIエージェントは回答と共に「この情報はここから来た」と明確に提示できます。これは単なる機能拡張に留まらず、ユーザーがAIの回答を容易に検証し、詳細情報を自ら確認できるため、RAGシステムへの信頼と透明性を劇的に向上させます。Webアプリケーション開発者が信頼性の高いAIエージェントを構築する上で、この「情報源の明確化」は必須のプラクティカルなアプローチであり、システムの利用価値を大きく高める重要な技術的ブレークスルーと言えるでしょう。