## GitHub Copilotに新機能、指示を適用するかエージェントごとに選択

https://codezine.jp/news/detail/22561

GitHub Copilotのカスタム指示ファイルに新機能「excludeAgent」プロパティが追加され、各エージェントへの指示適用をより細かく制御できるようになったことを発表しました。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 75/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[GitHub Copilot, AIエージェント, コーディング支援, 開発ツール, カスタム設定]]

GitHubは、GitHub Copilot向けにカスタム指示ファイルの新機能「excludeAgent」プロパティを追加したと発表しました。これにより、開発者は従来のディレクトリ単位でカスタム指示ファイル「instructions.md」を適用する機能に加え、GitHub CopilotコードレビューやGitHub Copilotコーディングエージェントといった個別のエージェントに対し、特定の指示を適用しないよう細かく制御できるようになります。

たとえば、`excludeAgent`プロパティに「code-review」と指定することで、コードレビューエージェントではその指示が無効となり、他のエージェントには適用されるといった使い分けが可能です。この機能は、AIアシスタントの振る舞いを特定のユースケース（例：コード生成、レビュー、デバッグ）に合わせて最適化し、より的確な支援を受けたいと考えるウェブアプリケーションエンジニアにとって重要です。エージェントごとの指示制御は、開発ワークフローにおけるAIアシスタントの統合度を高め、不必要な提案や誤ったガイダンスを減らす上で実用的な価値を提供します。