## TypeScript 向けの AI フレームワーク TanStack AI を試してみた

https://azukiazusa.dev/blog/try-tanstack-ai/

**Original Title**: TypeScript 向けの AI フレームワーク TanStack AI を試してみた

TanStack AIは、複数のLLMプロバイダーを抽象化し、ツール呼び出しやストリーミング処理をTypeScriptで型安全に実装できる軽量なAIフレームワークである。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[TanStack AI, TypeScript, AI Frameworks, LLM Tool Calling, Next.js Integration]]

この記事は、TanStackチームが開発するTypeScript向けの軽量AIフレームワーク「TanStack AI」の概要と基本的な使い方を詳細に解説している。TanStack AIは、OpenAIやAnthropicなど異なるLLMプロバイダーのAPIインターフェースを抽象化し、複数のモデルをスムーズに切り替えて開発できる点が特徴だ。これにより、従来のAI SDKやLangChainと同様に、LLMとの連携における煩雑さを大幅に軽減する。

主な機能として、`chat`関数を用いたLLMへのメッセージ送信とストリーミングレスポンスの受信、非同期イテレータによるチャンク処理が挙げられる。特に重要なのは「ツールの呼び出し」機能で、ツール定義と実装を分離することで、Zodによる型安全なスキーマ定義、さらにサーバーとクライアント間での共有を可能にしている。例えば、サーバーサイドでデータベース操作、クライアントサイドでローカルストレージ操作といった柔軟な使い分けが可能だ。ツールの実行前にはユーザーの承認を求める`needsApproval`オプションも提供され、セキュリティ面にも配慮されている。

さらに、Next.jsアプリケーションへの統合方法も具体的に示されており、Route HandlersでサーバーサイドのAPIエンドポイントを作成し、`@tanstack/ai-react`パッケージの`useChat`フックでクライアントサイドのチャット状態管理とメッセージ送信を行う実践的なアプローチが紹介されている。`toStreamResponse`関数によりストリーミングレスポンスをHTTPレスポンスに変換し、`fetchServerSentEvents`を通じてクライアントと接続することで、リアルタイム性の高いインタラクティブなAIチャットボットを構築できる。

ウェブアプリケーションエンジニアにとって、このフレームワークは複雑なLLM連携をTypeScriptの型安全性と既存のWeb開発パラダイム（Next.js, React）に馴染む形で実現する強力な選択肢となる。異なるLLMへの依存度を下げつつ、堅牢で拡張性の高いAIエージェントやチャット機能を効率的に開発できる点が、その実用的な価値と重要性を示している。