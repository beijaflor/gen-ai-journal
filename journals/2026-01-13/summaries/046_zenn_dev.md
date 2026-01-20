## "AIツールのスイス" TanStack AI の設計哲学

https://zenn.dev/tsuboi/articles/fbce183f930fc0

特定のプロバイダーやフレームワークに依存しない「中立性」と、モデルごとに動的に切り替わる厳密な型安全性を備えた新世代AI SDK「TanStack AI」の核心を解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[TanStack AI, AI SDK, TypeScript, Type Safety, Local-first AI]]

TanStackの作者Tanner Linsley氏が発表した「TanStack AI」は、特定のクラウドプロバイダーやフレームワーク、ランタイムに依存しない「AIツールのスイス（中立性）」を標榜する新世代のSDKだ。Vercel AI SDKが「規約による自動化（Magic & Convention）」を重視するのに対し、TanStack AIは「明示的な設定（Explicit & Config）」という設計哲学を掲げ、挙動の予測可能性と開発者の制御を優先している。著者は、この設計の違いが開発体験や保守性に決定的な差を生むと指摘している。

最大の特徴は、モデルごとに型定義が動的に切り替わる「Per-Model Type Safety（高忠実度）」だ。Vercel AI SDKではモデル固有のオプションは汎用的なプロパティに格納されるため、モデル変更時の修正漏れが型エラーになりにくい。一方、TanStack AIではAdapterパターンにより、OpenAIからGeminiへ変更した際などに、モデルに存在しないオプション（例：OpenAI特有のlogitBiasなど）をコンパイル時に即座に検出できる。これにより、ドキュメントを往復することなくIDE上でAIの仕様を把握できる「Type-Driven AI Development」を実現している。

また、ツールの「定義」と「実装」を分離する「Isomorphic Tools」という概念も画期的だ。サーバー側で実行するDB操作（.server()）と、ブラウザ側で実行するDOM操作やクリップボード操作（.client()）を一つのツール定義内で分離して実装できる。これにより、従来はサーバーからのレスポンスをフロントエンドでパースして条件分岐させていたような複雑なUI操作を、AIに直接委ねることが可能になる。

さらに、TanStackエコシステムとの統合は「ローカルファーストAI」という強力なビジョンを提示している。特にTanStack DBとの連携は、AIの短期記憶（コンテキスト）だけでなく、リアルタイムに同期・永続化される「活きた長期記憶」としての役割を果たす。これにより、オフライン対応やマルチユーザー間でのエージェント状態の同期など、従来のチャットUIの枠を超えたアプリケーション構築の道が開かれると著者は主張している。

筆者によれば、Vercel AI SDKがNext.jsやVercelプラットフォームに最適化されているのに対し、TanStack AIはマルチフレームワーク環境や、Deno・Bun・Cloudflare Workersといった多様なランタイム、そして長期的なベンダー非依存を重視するプロジェクトにとって有力な選択肢になる。現時点ではアルファ版だが、その明確な設計原則はAI開発における新しい標準を示唆している。