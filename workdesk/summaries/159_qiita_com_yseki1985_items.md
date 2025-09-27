## AIエージェントでObservabilityを実装してみよう！

https://qiita.com/yseki1985/items/53eccd3ede7e92d98efa

AIエージェント「Claude code」を活用し、手間のかかるGo言語アプリケーションへのNew Relic Observability自動計装の可能性を実証しました。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[AIエージェント, Observability, Go言語, 自動計装, New Relic]]

Go言語におけるObservabilityの計装は、コンパイル言語の特性上、開発者がコードにSDK APIを直接組み込む必要があり、多くの手間を伴います。本記事は、この課題に対し、AIコーディングツール「Claude code」を用いてNew Relic Goエージェントの計装を自動化できるかを検証しています。

検証ではまず、意図的な遅延やエラーを組み込んだシンプルなGo製Web APIアプリケーションをClaude codeに開発させました。次に、「このアプリケーションをNew Relicで観測できるように計装してください」という非常にシンプルなプロンプトでAIに計装を依頼。その結果、Claude codeはNew Relic APMでアプリケーションのスループット、レスポンスタイム、エラー率、トランザクション、そして商品番号や注文数といったカスタム属性までを可視化できるレベルで計装を成功させました。特に、詳細な指示なしにAIがカスタム属性を自律的に追加した点は、その理解度の高さを示すものです。

一方で、外部サービス呼び出しの計装において、AIは`StartExternalSegment`を用いたものの、より効率的な`newrelic.NewRoundTripper`のようなAPIが存在するなど、改善の余地も指摘されています。しかし、より詳細なプロンプトを与えることで、さらに最適な計装が期待できる可能性を示唆しています。

本検証の意義は大きく、AIエージェントによる開発が加速しコードがブラックボックス化する懸念が高まる中、ObservabilityがAI生成コードの挙動を人間が理解するための不可欠な手段となることを明確に示しています。将来的には、非技術者がAIを活用してアプリケーションを開発する機会が増えることで、エンジニアはAIに適切にObservabilityを実装させるための知識や設計が、より重要なスキルとなるでしょう。これは、AIを活用した開発における品質保証と運用効率の新たな形を提示するものです。