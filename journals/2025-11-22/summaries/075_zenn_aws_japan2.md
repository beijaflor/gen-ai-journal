## エージェントの検索精度を向上させる Amazon Nova Multimodal Embeddings - embeddingPurpose

https://zenn.dev/aws_japan/articles/2f989837eb7fe1

Amazon Nova Multimodal Embeddingsは、9種類の`embeddingPurpose`を活用することで、マルチモーダルデータに対する検索精度を大幅に向上させ、特にRAGシステムやクロスモーダル検索において、より関連性の高い結果をもたらします。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 100/100 | **Overall**: 84/100

**Topics**: [[Multimodal Embeddings, RAG System Optimization, Vector Search, AI Agents, AWS Bedrock]]

本記事は、自律型AIエージェントの性能を左右する情報検索（Retrieval）の精度向上に焦点を当て、AWSの最新埋め込みモデル「Amazon Nova Multimodal Embeddings」とその「embeddingPurpose」機能の重要性を解説します。Webアプリケーションエンジニアにとって、RAGシステムやマルチモーダル検索を構築する上で、このモデルの適切な利用はエージェントの応答品質に直結するため、非常に実践的な内容です。

Amazon Nova Multimodal Embeddingsは、現在米国東部（US-EAST-1）リージョンで利用可能で、テキスト、画像、動画、音声、ドキュメントの5種類のモダリティデータを統一的なベクトル空間にマッピングできます。最大8kトークンの長いコンテキスト長に対応し、3,072次元から256次元まで柔軟な埋め込み次元を選択できる点が特徴です。

最も重要なのは、9種類の`embeddingPurpose`パラメータによる用途別の最適化です。これは、従来の埋め込みモデルが単一の埋め込みしか生成できなかったのに対し、Nova Multimodal Embeddingsが検索・RAG用途（`*_RETRIEVAL`など7種類）や分類・クラスタリング用途（`CLASSIFICATION`、`CLUSTERING`）など、タスクに応じて最適な埋め込みを生成できる点にあります。

著者によると、検索精度を最大化する鍵は、「インデックス作成時にはモダリティに関わらず`GENERIC_INDEX`を使用し、検索クエリ側ではタスクに応じた`DOCUMENT_RETRIEVAL`や`IMAGE_RETRIEVAL`などの`*_RETRIEVAL`モードを選択する」という非対称埋め込みの戦略です。これにより、検索時に真に関連性の高いドキュメントや画像とそうでないものを明確に区別し、Top-Kの精度向上や適切な閾値設定を可能にします。

実際の検証では、SageMakerの技術ドキュメント検索（文章検索）とCIFAR-10データセットを用いた画像検索の両方で、この`GENERIC_INDEX`と`*_RETRIEVAL`の組み合わせが、`GENERIC_INDEX`のみの場合と比較して、1位と2位のスコア差を大きく広げ、より効果的な検索を実現できることが示されました。

このモデルを適切に活用することで、開発者はより高精度な情報検索能力を持つAIエージェントを構築し、ユーザー体験を向上させることが期待されます。