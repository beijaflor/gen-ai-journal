## GitHub Copilot CLI: まずはここから

https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-how-to-get-started/

**Original Title**: GitHub Copilot CLI: How to get started

GitHub Copilot CLIは、開発者がターミナル内でAIアシスタンスを直接利用できるようにし、文脈切り替えなしでリポジトリのクローンからプルリクエスト作成までを効率化します。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[GitHub Copilot CLI, ターミナル開発, 開発者ワークフロー, AIアシスタンス, 生産性向上]]

GitHubは、開発者がターミナル内で直接AIアシスタンスを活用できる「GitHub Copilot CLI」のパブリックプレビューを発表しました。これにより、リポジトリのクローンからプルリクエストの作成に至るまで、開発者はIDEやブラウザに切り替えることなく、一貫したワークフローの中でAIの恩恵を受けられます。著者は、このツールがコンテキストスイッチングを排除し、開発者の生産性を大幅に向上させると強調しています。

Copilot CLIは、npm経由で簡単にインストールでき、既存のGitHub Copilot Pro、Business、またはEnterpriseプランで認証するだけで利用可能です。例えば、初めてのコードベースに貢献する場合、通常はREADMEの読み込み、依存関係の確認、issueの検索に時間がかかりますが、Copilot CLIはこれらのタスクを自動化します。具体的には、以下のシナリオでその価値を発揮します。

1.  **プロジェクト構造の理解**: 「Explain the layout of this project.」と尋ねると、`find`や`tree`コマンド、READMEファイルを分析し、プロジェクトの概要をMarkdown形式で提示します。
2.  **開発環境の準備**: 「Make sure my environment is ready to build this project.」という指示で、必要な依存関係を確認・インストールし、ビルド環境を整えます。
3.  **適切なissueの検索**: 「Find good first issues in this repository and rank them by difficulty.」と入力すると、GitHub Issuesから貢献しやすいissueを難易度別に提示します。
4.  **実装の支援**: 「Start implementing issue #1234. Show me the diff before applying.」と指示すると、変更計画を立案し、修正をドラフトして差分を表示します。開発者は変更をレビューし、承認することで完全にコントロールを維持できます。
5.  **コミットとプルリクエスト作成の自動化**: 「Stage changes, write a commit referencing #1234, and open a draft PR.」で、ファイルのステージング、コミットメッセージの生成、ドラフトプルリクエストの作成を一連の流れで実行します。
6.  **一般的な開発の課題解決**: 特定のポートを占有しているプロセスを特定し、終了させるなどのコマンドもCopilot CLIを通じて実行できます。

Copilot CLIは、AIがコマンドを実行したりディレクトリにアクセスしたりする前に、必ずユーザーに許可を求めることで、開発者が完全にコントロールを維持できる安全な設計となっています。また、GitHub MCPサーバーが組み込まれており、issue検索やリポジトリ操作を強化しますが、ユーザーは`copilot /mcp`コマンドで他のMCPサーバーを追加し、機能を拡張することも可能です。

著者は、Copilot CLIが開発者がすでに作業しているターミナルにAIアシスタンスをもたらすことで、コンテキストスイッチングを避け、オンボーディングや新しいコードベースの探索の際に一貫したフローを維持できる点を最大の利点としています。これはIDEを代替するものではなく、「適切な場所に適切なツールがある」ことを目指していると述べられています。