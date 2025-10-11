## GitHub Copilot gets smarter at finding your code: Inside our new embedding model

https://github.blog/news-insights/product-news/copilot-new-embedding-model-vs-code/

GitHub Copilotは、新たな埋め込みモデル導入により、コード検索の精度、速度、メモリ効率を劇的に向上させ、開発者の生産性を高めます。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[GitHub Copilot, 埋め込みモデル, コード生成AI, Retrieval-Augmented Generation, 開発者ワークフロー]]

GitHub Copilotが新たな埋め込みモデルを導入し、VS Codeでのコード検索を大幅に強化したと発表されました。このモデルは、Retrieval-Augmented Generation（RAG）の「検索」ステップの基盤となる埋め込みを改善し、関連性の高いコードや自然言語コンテンツを意味的に識別する能力を高めます。

具体的な改善点として、Retrieval品質が37.6%向上し、スループットは約2倍に、インデックスサイズは8分の1に縮小されました。これにより、Copilotチャットやエージェント機能の応答精度が向上し、結果表示が高速化され、VS Codeのメモリ使用量も削減されます。特にC#とJava開発者においては、コード受容率がそれぞれ110.7%と113.1%も向上したと報告されており、これは日々のコーディング体験に直接的な影響を及ぼします。

このモデルは、コードとドキュメントに特化して訓練され、特に重要なのは「対照学習（contrastive learning）」と「ハードネガティブ（hard negatives）」の活用です。ハードネガティブとは、一見正しそうに見えて実際は間違っているコード例のことで、これらをモデルに学習させることで、「ほぼ正しい」と「実際に正しい」を厳密に区別する能力が飛躍的に向上しました。これにより、意図に完璧に合致するスニペットの検索が可能となり、大規模なモノレポでのテスト関数検索、ヘルパーメソッドの発見、エラー文字列のデバッグなど、開発者の多様なシナリオで高い実用性を提供します。

ウェブアプリケーションエンジニアにとって、これはCopilotが単なるコード補完ツールではなく、より賢く、文脈を深く理解し、正確な解決策を提示する「インテリジェントなアシスタント」へと進化していることを意味します。開発者は、複雑なコードベースの中から目的のコードを素早く、高い精度で見つけ出すことができ、結果として開発効率とコード品質の向上に直結します。