## Claude Code の `/hooks` コマンドによる通知機能の活用

https://zenn.dev/keit0728/articles/bfb68f669755a7

Claude Code の `/hooks` コマンドを活用し、タスク完了や承認依頼時にスマートフォンへプッシュ通知を送信する方法を解説する。

[[Claude Code, AIエージェント, 通知機能, 開発ワークフロー, スマートフォン連携]]

Claude Code におけるタスクの進捗や承認依頼のタイミングで、迅速かつ確実に情報を把握することは、開発ワークフローの効率化において重要である。本記事では、Claude Code に新たに搭載された `/hooks` コマンドに着目し、これを活用して外部サービス `ntfy.sh` を介してスマートフォンにプッシュ通知を送信する具体的な手順を解説している。`ntfy.sh` は、シンプルなHTTPリクエストで通知を送信できるサービスであり、モバイルアプリも提供されている。記事では、`PreToolUse`、`PostToolUse`、`Notification`���`Stop` の4つのフックタイミングの中から、タスク完了や承認依頼の通知に適したタイミングを選択し、カスタムコマンドとして設定する方法を示している。これにより、開発者はAIエージェントの作業状況をリアルタイムで把握し、必要なアクションを迅速に取ることが可能になる。

---

**編集者ノート**: この `/hooks` 機能は、AIエージェントとのインタラクションを非同期かつリアルタイムに管理するための強力な一歩と言える。特に、開発ワークフローにおいてAIエージェントの作業完了や承認待ちの状態を即座に知りたいというニーズは高い。`ntfy.sh` のような外部サービスとの連携は、開発者が日常的に使用するデバイスでAIの進捗を把握できるため、コンテキストスイッチのコストを削減し、生産性を向上させる可能性がある。今後は、より多様な通知チャネル（Slack, Discordなど）との連携や、通知内容のカスタマイズ性が向上することで、AIエージェントが開発チーム��コミュニケーション基盤にさらに深く統合されていくと予測する。
