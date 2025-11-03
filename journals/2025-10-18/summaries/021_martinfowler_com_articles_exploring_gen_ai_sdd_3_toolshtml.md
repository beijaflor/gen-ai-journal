## スペック駆動開発の理解：Kiro、spec-kit、Tesslの検証

https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html

**Original Title**: Understanding Spec-Driven-Development: Kiro, spec-kit, and Tessl

著者は、Kiro、spec-kit、Tesslといった3つのスペック駆動開発（SDD）ツールを検証し、その多様な実装を探るとともに、AI支援型コーディングワークフローにおける実際の適用可能性と有効性について重要な疑問を提起する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 90/100 | **Annex Potential**: 93/100 | **Overall**: 92/100

**Topics**: [[スペック駆動開発, AIコーディングツール, 開発ワークフロー, コード生成, モデル駆動開発]]

ThoughtworksのDistinguished Engineerである著者は、「スペック駆動開発（SDD）」というAIコーディングにおける新しいバズワードを深掘りするため、Kiro、spec-kit、Tesslという3つの主要ツールを検証する。SDDの定義は依然として流動的だが、著者は「スペック（仕様書）をAIにコードを書かせる前に作成する（documentation first）」開発アプローチであると捉え、「spec-first」「spec-anchored」「spec-as-source」の3つの実装レベルを提示する。スペックとは、自然言語で書かれた、構造化された振る舞い指向の成果物であり、AIコーディングエージェントへのガイダンスとして機能すると定義している。

記事では、各ツールのワークフローと特徴が詳細に説明される。Kiroは軽量な「requirements > design > tasks」の3段階ワークフローを採用し、spec-firstに注力する。GitHubのspec-kitはCLIとして提供され、「constitution」と呼ばれる高レベルな原則を記憶バンクとして活用するが、多くのMarkdownファイルを生成し、実際の運用ではspec-firstに留まる可能性が指摘される。一方、Tessl Framework（ベータ版）はspec-anchoredやspec-as-sourceを明確に志向し、生成コードに「// GENERATED FROM SPEC - DO NOT EDIT」と記すことで、スペックを主要な成果物と見なすアプローチを試みる。

著者の考察と疑問点は、エンジニアにとって特に重要だ。まず、SDDが単一のアプローチではなく、ツールによって大きく異なることを指摘。Kiroやspec-kitのような規定されたワークフローが、多様な問題サイズ（特に小さなバグ修正や既存機能の拡張）に適用するには過剰であり、「大槌で木の実を割る」ような状況を生む可能性があると警鐘を鳴らす。大量のMarkdownファイルをレビューする手間は、コードを直接レビューするよりも煩雑で生産性が低いと感じさせるという。

さらに、AIエージェントが指示を完全に守らない、あるいは過剰に追従することによる「誤った制御感」についても言及。過去の経験から、少量の反復的なステップこそが開発の制御を維持する最善策であるとし、SDDの多大な事前スペック設計に懐疑的な見方を示す。機能仕様と技術仕様の分離の難しさ、そしてSDDのターゲットユーザーが不明確である点も課題として挙げられる。

特に「spec-as-source」に関しては、モデル駆動開発（MDD）との歴史的な類似性を引き合いに出し、LLMによる非決定性という新たな課題を抱えつつ、MDDの持つ柔軟性のなさやオーバーヘッドという欠点を再燃させる可能性を指摘している。

結論として、著者は「spec-first」の原則自体はAI支援型コーディングにおいて非常に価値があるものの、「スペック駆動開発」という用語はまだ曖昧で意味が拡散しており、現在のツールが既存の課題を増幅させる「Verschlimmbesserung」（改善しようとして悪化させる）になる可能性があると述べ、ツールの実用性について慎重な評価を促している。