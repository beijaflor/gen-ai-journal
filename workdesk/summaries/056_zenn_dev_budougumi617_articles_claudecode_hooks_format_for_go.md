## Claude Code Hooksを使って編集したGoファイルだけ必ず自動フォーマットする

https://zenn.dev/budougumi617/articles/claudecode-hooks-format-for-go

Claude CodeのHooks機能を活用することで、Goファイルの編集時に自動でフォーマットを適用し、開発ワークフローを効率化できる。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 84/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[Claude Code, Go言語, 開発ツール, 自動化, コードフォーマット]]

本記事は、AnthropicのAIコーディングツール「Claude Code」を使用するGo言語開発者向けに、コードフォーマットの課題を解決する実践的な方法を提示します。Claude Codeを用いたGoファイルの編集において、意図しないフォーマット崩れや行末改行の削除が発生することがあり、`CLAUDE.md`にルールを記載しても徹底されない場合がありました。

そこで筆者は、Claude Code v1.0.38以降で追加されたHooks機能、特に`PostToolUse`フックを活用し、編集されたGoファイルに対して自動的に`gofmt`と`goimports`を実行する設定を考案しました。`.claude/settings.json`に特定の`command`を記述することで、`Write`、`Edit`、`MultiEdit`といったファイル操作後にこのフックが発火します。

この設定の重要な点は、`jq`コマンドを用いてAIが編集したファイルパスの中から`.go`ファイルのみを効率的に抽出し、`xargs`で該当ファイルに対してのみフォーマッターを実行する点です。これにより、プロジェクト規模に関わらず必要最低限の時間で処理が完了し、複数のフォーマッターが同時に実行されて競合するのを防ぐため、`gofmt -w && goimports -w`と直列で実行しています。

このアプローチにより、開発者はAIによるコード変更後のフォーマット手直しから解放され、プルリクエスト作成後のCI/CDでのフォーマットエラーを防ぐことができます。Go以外の言語にも応用可能であり、開発ワークフローの効率とコード品質向上に大きく貢献する、具体的な自動化手法として注目されます。
