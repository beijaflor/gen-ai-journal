## Shadcn Admin KitにMCPサポートを導入

https://marmelab.com/blog/2025/08/19/shadcn-admin-kit-mcp.html

MarmelabがShadcn Admin KitへのMCPサポートを統合し、Cursor IDEにおけるAIによる効率的な管理アプリ開発を実証しました。

**Content Type**: Tools
**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[MCP, Shadcn UI, AI-powered IDEs, Component Registries, Generative AI in Development]]

本記事は、Marmelabがオープンソースの管理UIライブラリ「Shadcn Admin Kit」に、AI駆動型IDE「Cursor」のMCP（Multi-Codebase Protocol）サポートを組み込んだ技術的なアプローチを詳細に解説しています。

従来のAIコーディングでは、LLMが一般的な知識に基づいてコードを生成するため、プロジェクト固有のコンポーネントライブラリや特殊な設定を正確に扱うことが困難でした。MCPは、AIが特定のレジストリやツールと連携し、より文脈に即した正確なコードを生成するためのプロトコルです。

Marmelabは、まだアルファ版のShadcn CLIにおける`registry:mcp`コマンドと`shadcn registry:build`コマンドを独自に解析し、Shadcn Admin KitをMCP対応にすることに成功しました。これにより、CursorのようなAI-IDEが、`npx shadcn@canary init`や`add`といったコマンドを直接実行できるようになります。

このアプローチの核心は、LLMに指示を与える`.cursor/rules/registry.mdc`ファイルにあります。このMarkdown形式のルールファイルは、AIに対し、レジストリのコンポーネントを優先的に使用すること、主要コンポーネント（例: `<Admin>`) の具体的な使用例、さらにはTypeScript設定の調整といった、プロジェクト固有のインストール後処理までを自然言語で伝えます。結果として、AIはわずか2、3回のプロンプトで管理アプリケーションの初期化、リソースの宣言、さらにはLucideアイコンの追加といった複雑なカスタマイズまでを自動で実行可能になります。

この実装は、AIが単なるコード生成を超え、プロジェクトのコンテキスト、ライブラリの規約、さらにはビルド時の制約までを考慮に入れた、高度な「論理的推論」と「タスク実行」を可能にするものです。ウェブアプリケーションエンジニアにとって、これは開発初期のセットアップや反復的なUI構築作業を劇的に削減し、カスタムUIライブラリのAIによる利用効率を飛躍的に向上させる画期的な進歩と言えます。この技術は、将来的に他のAI搭載IDEにも波及し、開発ワークフローにおけるAIの役割を一層深める可能性を秘めています。