## TUIベースのAIコーディングエージェント「Crush」試用レビュー

https://grahamhelton.com/blog/crushing-it

**Original Title**: Testing out Crush, a TUI based coding agent (in neovim btw)

著者は、ターミナルベースのAIコーディングエージェント「Crush」を用いてOpen Graph画像の動的生成を試み、その効率性と優れたUXを評価する一方で、個人の趣味プロジェクトにおいてはコスト面で課題があると指摘する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 76/100 | **Annex Potential**: 76/100 | **Overall**: 76/100

**Topics**: [[AIコーディングエージェント, TUIツール, Neovim連携, 開発ツール評価, クラウドコスト管理]]

この記事では、著者がCharmのターミナルベースAIコーディングエージェント「Crush」をNeovim内で試用し、自身のサイトのOpen Graph画像の動的生成機能の実装に活用した経験を共有しています。VS Code中心のUIを持つCursorのようなツールとは異なるTUIベースのアプローチを評価しており、Charm製品に共通する洗練されたユーザーエクスペリエンス（UX）を特徴として挙げています。

CrushはClaude Codeに似た familiar な操作感を提供し、Open Graph画像生成機能の実装を通常数日かかる作業から約45分に短縮するなど、効率性の向上に貢献したと著者は述べています。特に、変更されたファイルリストやモデル・コスト表示機能、モデル切り替えやセッションサマリーなどのctrl-pオプションが便利だったと評価しています。

しかし、著者は、Crushのモデル非依存のアプローチは高く評価しつつも、個人的なプロジェクトにおけるコストが大きな課題であると指摘しています。Open Graph画像生成という比較的単純な機能の実装に、主にSonnet 4とGemini Flashを使用して23.04ドルかかったことを報告し、これは個人の趣味サイトにとって高額だと述べています。Cursorのような企業が、複雑なキャッシングやAnthropicとの提携による規模の経済によって、低価格でプレミアムモデルを提供できる点に言及し、Crushのようなツールを本格的に利用するには、将来的にデータセンターでのGPUセルフホスティングが必要だと結論付けています。

この経験から、著者はCrushを大規模で集中的なコーディング作業には使用しないものの、よりシンプルで安価なモデルで対応できる小規模なタスクや、ホームラボでの迅速な変更には活用していく意向を示しています。