## 社内データ基盤 × Agent Engine × ADK × Next.jsで、分析エージェントを作っている話（技術編）

https://zenn.dev/readyfor_blog/articles/3f6909aff58261

READYFORは、社内データ基盤を活用するデータ分析エージェントの開発経緯と技術的詳細を公開し、アーキテクチャや実装の課題克服を具体的に示します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 96/100 | **Annex Potential**: 93/100 | **Overall**: 96/100

**Topics**: [[Agent Engine, Agent Development Kit, Next.js, LLMコンテキスト管理, データ品質]]

READYFORは、社内のdbtとBigQueryで整備されたデータ基盤を活用し、誰もが手軽にデータを引き出せるようにするため、LLMを組み合わせたデータ分析エージェント「めぐりちゃん」を開発しました。このエージェントは、ユーザーの指示に応じてSQL生成・実行や全文検索ツールを駆使し、社内データに基づいた回答を提供します。営業における事例探しなどで既に高い実用性を示し、意思決定の速度向上に貢献しています。

本記事では、このエージェントの技術的な詳細を解説します。アーキテクチャはGoogle Cloudを基盤とし、認証にIdentity-Aware Proxy、WebアプリケーションにCloud RunとNext.js（UI AI Elements, AI SDK）、エージェントバックエンドにVertex AI Agent EngineとAgent Development Kit (ADK) (Python) を採用しています。連携ツールとしてVertex AI Search、dbtのデータカタログ、BigQueryを活用することで、エージェントが自ら必要なデータモデルを検索し、SQLを生成・実行する仕組みを実現しています。

開発における主要な工夫と知見として、著者は以下の点を挙げています。
*   **Agent EngineとADKの活用**: Google提供のProduction-readyなフレームワークとサービスにより、会話履歴保持型のAIエージェントを迅速に構築し、可観測性や評価の仕組みも活用。
*   **Next.jsの採用**: Agent EngineのPythonスタックが一般的な中で、社内のTypeScript/React/Next.jsとの親和性を優先。Vercel AI SDKの豊富なライブラリでUIを素早く構築。
*   **コンテキスト管理の最適化**: Gemini 2.5 Flashのリージョンごとの最大入力トークン数の違い（東京リージョンは128K）を考慮し、トークン消費状況を可視化。
*   **LLMの空文字応答対策**: Geminiが稀に空文字を返す問題に対し、思考予算の明示的な指定と、`after_model_callback`を用いたエラーメッセージへのフォールバックを実装。
*   **ツール出力のトークン枯渇防止**: 大量のツール実行結果によるLLMコンテキストウィンドウの枯渇を防ぐため、`@with_token_guard`デコレータを導入。ツール出力にトークン上限を設け、超過時はエラーと具体的な修正提案を返すことで、エージェントの安定稼働とユーザーの軌道修正を促しています。
*   **データ基盤の品質向上**: LLMにデータ基盤を使わせることで、カラム説明の不足や古いカラムといったデータ品質の問題が顕在化。著者はLLMのため、そして将来の新入社員のためにも、データ基盤の定義補強や不要カラムの削除が不可欠であると強調しています。

本記事は、自社でLLMを用いたエージェント開発を検討しているエンジニアにとって、実践的なアーキテクチャ選定、実装上の課題とその解決策、そしてデータ基盤の重要性に関する貴重な示唆を提供するものです。