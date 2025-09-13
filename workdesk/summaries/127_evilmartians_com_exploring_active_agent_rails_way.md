## Exploring Active Agent, or can we build AI features the Rails way?

https://evilmartians.com/chronicles/exploring-active-agent-or-can-we-build-ai-features-the-rails-way

Active AgentがRailsの慣習に沿ってAI機能統合を可能にする方法を探求し、実用例と将来の課題を詳述する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Active Agent (Rails Gem), Rails AI Integration, LLM Application Development, AI Agent Architecture, AI Feature Testing]]

「Active Agent」は、Ruby on RailsにAI機能を「Rails Way」で統合する新しいgemとして登場しました。既存のLLM SDKが高レベルの抽象化を欠く中、Active Agentはアクション駆動型オブジェクト、コールバック、Action Viewによるプロンプトレンダリングなど、Rails開発者に馴染み深いパターンでAIロジックをカプセル化します。これにより、開発者はより自然な形でAI機能に取り組めます。

JokerAgentの例では、AI生成リクエストをトリガーするエージェントクラス、同期/非同期実行、Action Viewを活用したプロンプトテンプレートによる命令分離など、その基本的な使い方が示されました。プロンプトをコードから分離し、Railsのビュー機能で管理できる点が重要です。

実戦では、オンデマンド翻訳機能を持つTranslateAgentの実装を通し、「エージェントがDB更新ロジックをどこまで担うべきか」という関心分離の課題が浮上しました。記事では、副作用の暗黙性やモデル実装への依存を減らすため、モデル層でのロジックカプセル化が推奨されています。また、LLM呼び出しの非同期処理化が、パフォーマンスとユーザー体験向上のために不可欠であることも示唆されました。

AI機能のテスト容易性も重要な論点です。LLM APIへのHTTPリクエストを直接スタブする手法の課題を指摘し、Active Agentのアダプターパターンを利用したテスト用FakeLLMProviderの自作アプローチが紹介されています。これにより、LLMプロバイダの変更に強く、安定したテストが実現できます。

AIレビューア機能を持つReviewAgentの例では、ツールの統合と構造化出力の課題が議論されました。特に、JSONスキーマを手動で記述する非「Rails Way」な現状を改善するため、RBS（Ruby Type Signatures）を活用したツール定義や、よりオブジェクト指向的な構造化出力（`Data.define`と`output_object`）の導入が提案されています。これは、AIを活用したアプリケーション開発におけるボイラープレートの削減と開発者体験の向上に直結します。

記事は、Active Agentが現在提供する抽象化の先を見据え、将来のAIアプリケーションに求められる高度な機能について深く考察しています。利用状況追跡、動的プロンプト、ガードレール、エージェントワークフロー、メモリ管理、RAGのためのコンテキストエンジニアリングといった課題に対し、Active Agentのようなライブラリがプラグインによる拡張性を備えることの重要性を強調します。

Active Agentは、RailsでAI機能を構築するための有望な基盤ですが、本番環境の要求に応えるには、絶えず進化するAIの特性に柔軟に対応できる拡張ポイントが不可欠です。Rails開発者にとってAI統合はまだ黎明期にありますが、Active Agentが「Rails流」を追求することで、自然で堅牢なAI搭載アプリケーション開発への道が開かれるでしょう。