## Claude Code on the Webでghコマンドを使う

https://zenn.dev/oikon/articles/claude-code-web-gh-cli

Claude Code on the Webにおいて、制限解除されたGitHub CLI（ghコマンド）を自動インストールし、ブラウザ完結でのPR作成やIssue操作を実現する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Claude Code, GitHub CLI, sessionStartHooks, サンドボックス環境, 開発オートメーション]]

AnthropicのAIコーディングツール「Claude Code」のWeb版において、これまで制限されていたGitHub CLI（ghコマンド）が利用可能になったことを受け、その具体的なセットアップ手法を解説する記事である。Claude Code on the WebはブラウザのみでGitHubリポジトリを編集・実行できる強力な環境だが、従来はセキュリティや環境の制約からghコマンドの使用が明示的に禁止されていた。

筆者は、Claude Code on the Webの内部仕様を詳細に分析し、2025年12月中旬のアップデートによって内部的な起動オプション（startup.json）から「disallowed_tools: ["Bash(gh:*)"]」という禁止設定が削除されたことを発見した。これにより技術的に利用が可能になったが、Web版のサンドボックス環境にはデフォルトでghバイナリが存在しないため、そのままでは動作しない。この記事は、その欠落を「sessionStartHooks」という比較的新しい自動化機能を活用して埋める、非常に実用的なガイドとなっている。

解説の核心は、セッション開始時に自動実行されるシェルスクリプトによるインストール手順だ。具体的には、`.claude/hooks/gh-setup.sh` を作成し、実行環境のアーキテクチャ判定からバイナリのダウンロード、配置、PATHの設定までを自動化する。ここで重要なのが `CLAUDE_CODE_REMOTE` という環境変数の活用である。これを使用することで、ローカルのClaude Code環境では実行をスキップし、Web（リモート）環境でのみインストールを実行するという、開発環境を汚さないクリーンな運用が可能になる。

また、認証に必要な `GITHUB_TOKEN` をカスタム環境変数として設定する方法や、`CLAUDE_ENV_FILE` を介してセッション中のPATH設定を永続化するテクニックも詳述されている。これにより、一度設定してしまえば、ブラウザでリポジトリを開くだけでAIエージェントが自律的にPRを作成したり、Issueの内容を読み取って修正を開始したりといった、真の「ブラウザ完結型AIコーディング」が実現する。

筆者は、ghコマンドの使用時に必要となるプロキシ制約（-Rフラグの推奨）や、AIへの指示をスムーズにするためのCLAUDE.mdへの記述など、実運用における微細なハマりどころまでカバーしている。Web版Claude Codeを単なるコードエディタとしてではなく、GitHub連携を含むフル機能の開発ハブへと進化させるための重要な知見と言える。