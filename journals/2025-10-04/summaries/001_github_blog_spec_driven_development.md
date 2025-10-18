## Spec-driven development: Using Markdown as a programming language when building with AI

https://github.blog/ai-and-ml/generative-ai/spec-driven-development-using-markdown-as-a-programming-language-when-building-ai/

AIコーディングエージェント向けにMarkdownを「プログラミング言語」として活用する仕様駆動開発を提唱し、コンテキストロスを減らし反復速度を向上させる手法を解説します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 90/100 | **Overall**: 88/100

**Topics**: [[Spec-driven development, AI coding agents, GitHub Copilot, Markdown as code, Generative AI workflows]]

AIを活用したコーディングでは、エージェントがアプリの目的や過去の決定を「忘れてしまう」というコンテキストロスの問題が頻繁に発生します。この記事では、GitHubのエンジニアが提唱する「仕様駆動開発」という革新的なアプローチを紹介しています。これは、アプリケーション全体の仕様、例えばCLIの定義、データ構造、データベーススキーマなどをMarkdownファイル（`main.md`や`README.md`）に記述し、AIコーディングエージェント（GitHub Copilotなど）にそれを実際のGoコードに「コンパイル」させるというものです。

開発者は`main.md`を編集し、`compile.prompt.md`のようなシンプルなプロンプトを使ってAIにGoコードを生成させ、テストと修正を繰り返します。これにより、仕様と実装の同期が保たれ、コンテキストの喪失が減り、開発のイテレーションが加速されると筆者は強調しています。例えば、`README.md`でCLIの引数を更新すれば、そのままAIがGoコードに反映します。また、Markdown内にGraphQLクエリやデータベースのテーブル定義を直接記述することで、抽象的な要件だけでなく具体的な実装の詳細もAIに指示できます。

この手法は、Markdownを実質的に高レベルな「プログラミング言語」として扱い、AIがその仕様を解釈して下位レベルのコードを生成する新しい開発パラダイムを示唆しています。結果として、よりクリーンな仕様と高速な開発サイクルが実現可能となりますが、明確な記述の難しさや、コードベースの成長に伴うコンパイル速度の低下といった課題も指摘されています。しかし、このアプローチは、AI時代における開発者のワークフローとコードベースの管理に大きな示唆を与え、AI生成コードの信頼性と保守性を高める可能性を秘めています。