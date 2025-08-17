## Vibe codingによって生成されたコードの品質を担保するためにUltraciteを使ってみた

https://zenn.dev/bita/articles/df3e289155005d

UltraciteをVibeコーディングに導入することで、AI生成コードの品質と可読性が劇的に向上することを実証します。

**Content Type**: Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[AIコード生成, コード品質, リンター, 開発ツール, Biome]]

本記事は、CursorとClaude Codeを用いた「Vibeコーディング」で生成されるコードが、長大なファイル、複雑なロジック、アンチパターンを含みがちであるという品質課題に焦点を当て、その解決策としてUltraciteの導入と効果を詳述しています。高速で設定不要、かつ継続的に更新されるリンティングツールを探していた著者は、AI ReadyなBiomeベースのリンター「Ultracite」を発見し、その有効性を検証しました。

記事では、Next.jsプロジェクトへのUltraciteの具体的な導入手順をステップバイステップで解説しており、ESLintの無効化、Biome拡張機能のインストール、Ultraciteの初期化、MCP（Multi-Client Protocol）設定、そして`package.json`へのスクリプト追加など、実践的な導入方法が示されています。特に、`shadcn/ui`のコンポーネントをリンティング対象外にする設定など、実務で役立つ具体的な設定例も紹介されています。

最も重要な点は、VibeコーディングにおいてAI（Claude Code）に「use Ultracite rule from mcp server」と指示することで、AIがUltraciteのルールセットを自動的に取得し、そのベストプラクティスに従ったコードを生成するようになるという検証結果です。これにより、「動けばOK」で終わってしまうAI生成コードの可読性と保守性の問題が飛躍的に解決されることが実証されました。このアプローチは、ウェブアプリケーション開発者がAIの迅速な開発速度を享受しつつ、コードベースの品質基準を維持するための非常に実践的かつ効果的な手段を提供します。Ultraciteは単独のリンティングツールとしても有用であり、AI時代の開発ワークフローにおける品質管理の新たな基準を示すものです。