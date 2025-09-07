## Claude Codeをネイティブインストールしたらめっちゃ面倒くさかったのでnpmに戻す方法

https://zenn.dev/minato86/articles/8493ffc8d3975c

Claude CodeのNative Installが引き起こすダウングレードやアンインストールの困難を、設定ファイルと環境変数の適切な管理によって解決し、npmインストール版に戻す具体的な手順を詳述する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:3/5
**Main Journal**: 84/100 | **Annex Potential**: 81/100 | **Overall**: 80/100

**Topics**: [[Claude Code, インストール管理, トラブルシューティング, 環境変数, バージョン管理]]

最近、「Claude Codeがアホになった」という声が聞かれる中、特定のバージョンへのダウングレードやアンインストールが非常に困難になるケースが報告されており、特にデフォルトのnpmインストールではなく「Native Install」を導入している開発者がこの問題に直面しやすい。

筆者の経験から、Native InstallされたClaude Codeは、自動アップデートの失敗を回避するために導入されることがある。しかし、一度Native Installされると、その削除方法が公式には提供されておらず、手動で`.local/bin/claude`や関連ディレクトリを削除しても、`~/.claude.json`内の`"installMethod": "native"`という設定が原因で、Claude Codeを起動するたびに自動的にNative Install環境が再構築されてしまうという、非常に厄介な挙動を示す。これにより、npm版を導入しようとしても常にNative Install版との競合が発生し、意図しないバージョンが実行されるなど、バージョンの制御が不可能になる。

この循環的な問題を解決するには、まず`claude config set -g installMethod unknown`を実行し、Claude Codeの設定自体をNative Installから切り離すことが不可欠である。次に、`.bashrc`などに自動で追加された`export PATH="/home/minato86/.local/bin:$PATH"`のような環境変数を削除し、`~/.local/bin/claude`のシンボリックリンク、さらに`.local/share/claude/`、`.local/state/claude/`といったNative Installに関連する全てのファイルを完全に削除する。これらのクリーンアップ後、環境変数を再読み込みし、npmで希望するバージョンのClaude Codeを再インストールすれば、安定した管理可能な開発環境を取り戻せる。

この複雑な復元手順は、開発ツール選択における透明性と管理の重要性を示す。公式ドキュメントにないインストール方法の採用は、予期せぬ問題発生時に深刻なワークフローの阻害に繋がりかねない。筆者は、このような潜在的なトラブルを避けるため、Claude Codeのインストールにはnpm版を使用し、Native Installへの移行を避けることを強く推奨している。これにより、ツールのバージョン管理や問題発生時の対応が格段に容易になり、開発効率の維持に貢献するだろう。