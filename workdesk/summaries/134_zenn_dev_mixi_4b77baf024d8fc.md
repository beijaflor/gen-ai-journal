## 話題のMCPサーバー「Serena」をClaude Codeで使ってみた

https://zenn.dev/mixi/articles/4b77baf024d8fc

LSPを活用したMCPサーバーSerenaを導入することで、Claude Codeのコード理解度と提案精度の向上が実証された。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[Claude Code, Serena (MCP Server), Language Server Protocol (LSP), AIコードアシスタント, 開発効率化]]

最近、AnthropicのAIコーディングアシスタント「Claude Code」の精度低下が指摘される中、本記事はLanguage Server Protocol（LSP）を活用するMCPサーバー「Serena」を導入し、その効果を検証します。Serenaは、AIがコードを単なるテキストではなく関数やクラスといったシンボルレベルで認識・操作することを可能にし、コンテキスト効率を大幅に改善する点が特徴です。

記事では、GitHubリポジトリを対象にClaude CodeとSerenaを連携させる具体的な手順を解説。Serenaがプロジェクトの全体像把握のために、`check_onboarding_performed()`, `onboarding()`, `list_dir()`, `get_symbols_overview()`, `write_memory()`, `think_about_collected_information()`といったMCPツールを自律的に呼び出し、プロジェクト概要や技術スタック、開発コマンドなどを詳細に分析する過程を追体験できます。これにより、AIはリポジトリの構造とロジックを深く理解し、`project_overview.md`などの形で「記憶」します。

このシンボル認識能力は、Webアプリケーションエンジニアにとって大きな意味を持ちます。Claude Codeに対し「機能追加案」や「リファクタリングが必要な箇所」を尋ねると、Serenaのツール群（`find_symbol()`, `search_for_pattern()`など）を駆使してコードベースを詳細に分析。結果として、実績時間トラッキング、タスクフィルタリング、ログ出力統一、コンポーネント巨大化の解消といった、具体的かつ実践的な提案を高い精度で生成しました。

著者はSerenaの導入により「違う、そうじゃない！」という手戻りが減少したと体感しており、AIコードアシスタントの活用における精度と信頼性の向上を実感しています。特に複雑なコードベースを持つ大規模プロジェクトにおいて、SerenaのようなLSPベースのMCPサーバーは、AIがより深くコードを理解し、開発者の意図に沿った質の高い提案を行うための強力なソリューションとなります。Claude Codeの振る舞いに課題を感じているエンジニアにとって、Serenaの導入は開発体験を改善する有効な手段となるでしょう。