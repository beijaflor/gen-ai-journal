## Claude Codeを駆使した初めてのiOSアプリ開発 ~ゼロから3週間でグローバルハッカソンで入賞するまで~

https://speakerdeck.com/oikon48/claude-codewoqu-shi-sitachu-metenoiosapurikai-fa-zerokara3zhou-jian-degurobaruhatukasonderu-shang-surumade

Claude Codeを活用し、モバイルアプリ開発未経験の著者が3週間でiOSアプリを開発し、グローバルハッカソンで入賞した事例を詳述します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[Claude Code, iOSアプリ開発, グローバルハッカソン, AIコーディングワークフロー, Subagent活用]]

このプレゼンテーションでは、モバイルアプリ開発未経験の著者がClaude Codeを駆使し、わずか3週間でiOSアプリを開発し、グローバルハッカソン「Shipaton」で入賞した体験が詳細に語られています。著者は、この短期間での成果はClaude Codeの強力な能力の賜物だと強調し、「Claude is Horse, Claude Code is Harness」という考え方を提唱しています。

特に、以下のClaude Code活用術が開発の加速に貢献したと説明しています。
1.  **開発環境とIDE連携**: 慣れないXcodeではなくVS Codeを主要な開発環境とし、`xcrun`や`xcodebuild`といったCLIツールをClaude Code経由で実行。Claude CodeのIDE連携機能（`mcp__ide__getDiagnostics`など）を活用し、コードの静的解析や診断情報を取得することで、学習コストを抑えつつ効率的な開発を実現しました。
2.  **学習モードの活用**: `/output-style`コマンドの学習モードを使用し、タスクごとのインサイトを得たり、`TODO(human)`で演習題材を提示させたりすることで、コード理解と実践的な学習を深めました。著者は、AIに適切な指示を出すためには、人間側もコードを理解する努力が不可欠であると指摘しています。
3.  **効率的なコンテキスト管理**: `CLAUDE.md`の見直し、不要なコンテキストの削除（`/clear > /compact`）、そして何よりも「Subagent」の積極的な活用を推奨しています。コンテキスト占有率を`/context`で確認し、メインのコンテキストを汚染しないよう配慮しました。
4.  **実装ドキュメントの作成**: AWS KiroのSDDの作法を取り入れ、実装計画をドキュメント化することで、タスク粒度の調整、他のAIエージェントへの引き継ぎ、レビュー時のコンテキスト理解の促進など、多くのメリットを享受しました。
5.  **Subagentの役割分担**: Implementor（実装）、Validator（検証）、Architect（全体設計）など、明確な役割を持つSubagentを作成し、それぞれに参照ドキュメントやツールを限定することで、複雑なタスクを効率的に進めました。特にValidatorがリードオンリーで競合を起こさずに検証できる点が強調されています。
6.  **AI完結型のフィードバックループ**: ビルド、テスト、シミュレータ実行、実機インストールといった一連の作業をClaude Code上のスクリプトで完結させ、そのログもコンテキスト内に保持。人間は全体の理解とワークフローの整備に注力することで、開発を高速化しました。
7.  **複数AIモデルによるコードレビュー**: 異なるAIモデルによるレビュー結果を統合し、妥当な変更のみを抽出するワークフローにより、多角的な視点からコード品質を向上させました。
8.  **スマホ単体での開発**: GitHubとTestFlightを活用し、軽微な修正作業であればスマートフォンから完結できる工夫も凝らされました。

著者は、Claude Codeがゼロからの開発や新しい技術習得において強力なツールであり、「自分の能力の拡張」を可能にすると結論付けています。