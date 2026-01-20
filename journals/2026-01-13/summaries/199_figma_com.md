## 制約を料理する：デザイナーのためのAIプロンプト・フレームワーク

https://www.figma.com/blog/designer-framework-for-better-ai-prompts/

**Original Title**: Cooking with Constraints: A Designer’s Framework for Better AI Prompts

料理の「下ごしらえ」の概念をプロンプトに応用した「TC-EBC」フレームワークを提唱し、曖昧なAI出力を確実な設計・実装へと導く手法を提示する。

**Content Type**: 📖 Tutorial & Guide
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 91/100 | **Annex Potential**: 82/100 | **Overall**: 88/100

**Topics**: [[AIプロンプト, TC-EBCフレームワーク, Figma Make, モデル選択, MCP]]

Figmaのデザイナー・アドヴォケートであるGreg Huntoon氏による、AIプロンプトを「運任せ」から「信頼できるエンジニアリング」へと昇華させるための実践的ガイドである。筆者は、優れた料理が「ミザンプラス（下ごしらえ）」に依存するように、AIの出力もまた構造化された準備によって決まると主張している。

本記事の核心は、筆者が考案した**TC-EBC（Task, Context, Elements, Behavior, Constraints）**というフレームワークだ。
- **Task（タスク）**: 何を構築するかを定義する。
- **Context（コンテキスト）**: なぜ、誰のために作るのかという背景。
- **Elements（要素）**: UIコンポーネントやフォーム、カードなどの構成要素。
- **Behavior（振る舞い）**: ユーザーのアクションに対するアプリの応答。
- **Constraints（制約）**: ターゲット、アクセシビリティ、使用禁止事項などのガードレール。

筆者は、AIに対して「お願いします」といった礼儀正しい言葉（Pleasantries）を使うことは、モデルに不必要なトークンを消費させ、曖昧さを導入するだけで逆効果であると指摘する。むしろ、設計図のように「引き算」の美学で、エッセンスだけを抽出した直接的な指示こそが、確率論的なLLM（Stochastic）を確定的（Deterministic）な設計ツールへと変える鍵となる。

さらに、エンジニアにとって実用的な知見として、モデルの使い分けとコンテキストの統合方法が挙げられている。構造と論理を重んじる「Claude 3.5 Sonnet」、特定の狭いタスクで高速かつ正確な「Gemini 1.5 Pro」、推論と例示に強い「GPT-4」といった特性を理解し、タスクに応じて「ナイフ」を使い分けるべきだとしている。また、単なるスクリーンショットではなく、Figmaのフレームのような「構造化されたデザインデータ」を直接AIに渡すことや、MCP（Model Context Protocol）サーバーを介してNotionやGitHubのコンテキストを統合することで、AIの理解度は飛躍的に向上すると解説している。

最終的に、プロンプトは単なる指示ではなく、将来の自動化を支える「再現可能なシステム」の設計であると結論付けている。これは、生成AIを単なるチャットツールとしてではなく、開発ワークフローの一部として統合しようとするウェブエンジニアにとって、非常に解像度の高い指針となるだろう。