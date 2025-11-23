## 「Gemini in Looker」で実現するダッシュボード要約機能

https://techblog.zozo.com/entry/gemini-in-looker

ZOZOは、マルチテナント環境のLookerダッシュボードに、生成AIを活用した要約機能をセキュアに組み込むためのカスタマイズ実装とその技術的課題解決を詳細に解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Looker Extension, Generative AI, Multi-tenant Architecture, Data Security, Prompt Engineering]]

ZOZOは、マルチテナント環境で運用するLookerダッシュボードに、生成AIによる要約機能を安全に実装した事例を紹介している。外部テナントユーザー向けの厳格なアクセス制御が求められる中、同社はGemini in LookerのDashboard Summarization Extensionをカスタマイズして導入した。

標準機能ではなくLooker Extensionを活用した理由として、マルチテナント環境でのセキュリティ要件やビジネス要件への柔軟な対応を挙げている。実装の中心は、Lookerインスタンスからのアクセスのみを許可するCloud Load BalancingとCloud Armorによる二重防御、そしてLookerのUser AttributeとAccess Filterを組み合わせた厳密なデータアクセス制御である。Looker Extension（フロントエンド）がユーザー権限でLooker Query APIを呼び出すことで、Looker内部でクエリと権限制御が完結し、パラメータ改ざんなどのセキュリティリスクを回避している点が重要である。

さらに、ZOZOTOWNのビジネス特性に合わせた現実的な提案を生成するため、プロンプトの一部を`guideline.txt`として外部ファイル化し、コード変更なしにビジネス情報を更新可能にした。要約機能自体も、デフォルトの個別タイル要約ではなく、複数のクエリ結果を統合してダッシュボード全体を俯瞰する形に改善。社外ユーザー利用におけるセキュリティ懸念から、ユーザーが自由に質問を入力するUIは廃止し、固定プロンプトのみを使用するよう変更した。

本番適用時の重要な技術的課題として、ユーザーがフィルタを変更した際に要約が古いフィルタ状態に依存してしまう「要約の不整合」があった。これは要約生成時に`tileHostData.dashboardFilters`から現在のフィルタ状態を動的に取得し、Lookerのダッシュボードメタデータと共に渡すことで解決され、常に画面表示と要約内容の整合性が保たれるようになった。

この実装は、複雑なマルチテナント環境において、厳格なデータセキュリティを確保しつつ最先端の生成AI機能を実用的に導入できることを示しており、同様の課題を持つWebアプリケーションエンジニアにとって重要な知見を提供する。