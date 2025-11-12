## Claude Code on the Webの仕様を徹底解剖

https://zenn.dev/oikon/articles/claude-code-web-sandbox

本記事は、Anthropicが提供するブラウザベースの開発環境「Claude Code on the Web」のサンドボックス環境を徹底的に解剖し、その内部構造、機能、およびローカル環境との相違点を詳述しています。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:5/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 92/100 | **Annex Potential**: 93/100 | **Overall**: 92/100

**Topics**: [[Claude Code on the Web, サンドボックス環境, gVisor, Claude Code, 開発者ツール]]

本記事は、Anthropicが提供するブラウザベースの開発環境「Claude Code on the Web」のサンドボックス環境を徹底的に解剖し、その内部構造、機能、およびローカル環境との相違点を詳述しています。筆者は、この環境がGoogleが開発したセキュリティ強化技術であるgVisorベースのコンテナで稼働し、Ubuntu 24.04.3 LTS、4コアCPU、8GBメモリといった基本スペックを持つことを明らかにしています。

特に重要なのは、Claude Code on the WebがGitHubリポジトリを `/home/user/` にクローンし、その中でClaude Codeを起動するという仕組みです。この前提を理解することで、サンドボックス内での操作範囲が見えてきます。筆者の調査によると、グローバルなClaude Code設定（`~/.claude/`）は持ち込めないものの、プロジェクト固有の設定（`./.claude/`）は適用可能です。

また、筆者はグローバル設定に含まれる `stop-hook-git-check.sh` スクリプトの存在を詳細に分析しています。このスクリプトは、未コミットの変更、未プッシュのコミット、および未追跡ファイルがないかを自動的にチェックし、差分がある場合にClaudeにコミットとプッシュを促す役割を担っています。これにより、Claude Code on the Webが変更後すぐにコミットとプッシュを行う理由が明確になります。

さらに、記事ではサンドボックス内でのClaude Code起動時オプションも掘り下げています。これにより、モデルが「Sonnet 4.5」に固定されていることや、GitHub CLI (`gh` コマンド) が明示的に使用禁止ツールに含まれていることが判明しました。詳細なシステムプロンプトの解析からは、特定のフィーチャーブランチでの開発、明確なコミットメッセージ、厳格なgitプッシュ/プル手順が求められていることが示されています。

機能面では、`CLAUDE.md`、Hooks、Subagents、そして（一部非推奨ながら）`output-style`が利用可能である一方、Slash CommandとSkillsは `canUseTool` の無効化により直接は使えないものの、ClaudeがMarkdownの内容を解釈して間接的に機能させることが多いと説明されています。

本記事の知見は、Webアプリケーションエンジニアにとって極めて実用的な価値があります。Claude Code on the Webの内部挙動や制限を深く理解することで、プラットフォームをより効果的に活用し、gitワークフローを最適化し、ツールや機能のサポートに関する現実的な期待値を設定できるようになります。筆者の詳細な調査は、ブラウザベースのAIコーディング環境における開発ワークフローを改善するための具体的な技術的洞察を提供しています。