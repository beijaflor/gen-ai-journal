## Claude Code のサンドボックス機能を試してみた

https://azukiazusa.dev/blog/claude-code-sandbox-feature/

**Original Title**: Claude Code のサンドボックス機能を試してみた

Claude Codeのサンドボックス機能は、AIエージェントのファイルシステムとネットワークアクセスを制限し、承認疲れを解消しつつ安全な自律動作を可能にする。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 78/100 | **Overall**: 84/100

**Topics**: [[AIコーディングエージェント, サンドボックス技術, セキュリティ, 開発ワークフロー, Claude Code]]

AIコーディングエージェントは強力なファイル操作やコマンド実行能力を持つ一方で、誤用や悪用のリスクがあり、通常はユーザーの承認を求める仕組みが備わっています。しかし、この「承認疲れ」が開発サイクルを低下させ、ユーザーが内容を確認せずに承認してしまうことで、かえってセキュリティリスクを高める可能性があると筆者は指摘します。従来の`permissions`設定による許可リストだけでは、`find . -exec rm {} \;`のような抜け道が発見されるリスクも残ります。

この課題に対し、Claude Codeが提供するサンドボックス機能は、OSレベルで軽量なサンドボックス環境を利用し、ファイルシステムとネットワークへのアクセスを制限することで、AIエージェントの自律性を維持しつつ安全性を高める解決策です。サンドボックス環境では、明示的に許可されたディレクトリやドメイン以外へのアクセスが防がれます。具体的には、macOSではApple Seatbelt（sandbox-execコマンド）、LinuxではBubblewrapが使用されており、その実装はオープンソースのnpmパッケージ`@anthropic-ai/sandbox-runtime`として公開されています。

サンドボックスは`/sandbox`コマンドで有効化でき、失敗した場合は通常のpermissions設定に基づいてユーザーの承認を求めます。しかし筆者は、`--dangerously-skip-permissions`オプション使用時にサンドボックスがAIエージェントの判断で無効化される可能性や、`dangerouslyOverrideSandbox`オプションの誤用リスクをセキュリティ上の懸念点として挙げています。`settings.json`ファイルの`sandbox`セクションでサンドボックスの詳細な設定（有効化、コマンド自動許可、ネットワーク設定など）が可能であり、ファイルシステムアクセスは`Read`/`Edit`権限、ネットワークアクセスは`WebFetch`権限で細かく制御できます。この機能は、開発者がAIエージェントの利便性とセキュリティを両立させる上で、重要な一歩となると筆者は示唆しています。