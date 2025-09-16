## Amazon S3 Vectors をベクトルストアにした Amazon Bedrock Knowledge Bases のノーコード RAG 構築をゼロから解説

https://dev.classmethod.jp/articles/bedrock-knowledge-bases-s3-vectors-rag-no-code/

開発者は、Amazon S3 VectorsをベクトルストアとしたAmazon Bedrock Knowledge Basesを活用し、RAGシステムをノーコードで構築する手順を詳細に学ぶことができます。

**Content Type**: 📖 Tutorial & Guide

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 79/100 | **Overall**: 80/100

**Topics**: [[Amazon Bedrock Knowledge Bases, Amazon S3 Vectors, RAG, ノーコード開発, ベクトル検索]]

本記事は、ウェブアプリケーション開発者やインフラエンジニア向けに、Amazon Bedrock Knowledge Bases と、パブリックプレビューが開始された安価なベクトルストアである Amazon S3 Vectors を連携させ、RAG（検索拡張生成）システムをノーコードで構築する詳細な手順を解説します。これにより、開発に不慣れなエンジニアでも、Amazon S3がベースとなるベクトルストアの利点を活かし、コスト効率良くLLMを活用した高精度な情報検索・生成システムを容易に導入できるようになります。

記事では、まずRAGシステム全体のイメージ図を提示し、S3バケットの準備（元の生データを格納する汎用バケットと、ベクトルストアとして機能するベクトルバケットの二つ）から始めます。特に、ベクトルバケット作成時には、埋め込みモデル（Amazon Titan Text Embeddings V2のデフォルトである1024次元）の出力次元数と距離メトリック（テキスト検索に適したコサイン距離）を一致させる重要性を強調しています。その後、Bedrock Knowledge Bases上でチャンキング戦略や埋め込みモデルを設定し、データ同期によって、チャンキングとベクトル化が自動で行われ、S3 Vectorsにベクトルデータが格納される一連のプロセスを、具体的なIAMロールの設定例とともに丁寧に追体験できます。

また、システム構築後のテスト方法だけでなく、クロスリージョン推論を行うテキストモデル（Claude Sonnet 4）を選択した際に、AWSアカウントのリージョン制限により発生したエラーとその解決策（非クロスリージョン推論モデルの選択）を具体的に示しており、実際の運用で遭遇しがちな課題に対する深い洞察を提供します。この実践的なガイドは、先進的なLLMアプリケーション開発を、コーディングの負担とコストを抑えつつ迅速に試したい開発者にとって、非常に価値のある情報源となるでしょう。