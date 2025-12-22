## 【Claude】Pluginsで簡単横展開 - 開発手法の標準化 -

https://tech.findy.co.jp/entry/2025/12/17/070000

Claude Codeの新機能「Plugins」がリリースされ、開発組織やチーム間で開発手法やワークフローを簡単に標準化できるようになった。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 77/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[Claude Code, Plugins, 開発標準化, 開発ワークフロー, GenAI]]

ファインディ株式会社の戸田氏が、Claude Codeの新機能「Plugins」について解説しています。生成AIがソフトウェア開発に大きな変革をもたらす中で、開発支援ツールが日常的なワークフローに不可欠となりつつあります。本記事は、このPluginsの概要、作成方法、利用方法を具体的に紹介し、開発組織におけるその重要性を強調しています。

Pluginsとは、Custom slash commands、Subagents、Hooks、Agent Skills、MCPサーバーといったClaude Codeの各種設定や機能を事前にパッケージ化し、組織やチーム間で簡単に横展開・標準化するための仕組みです。これにより、開発手法やワークフローの統一が飛躍的に容易になります。

その作成手順はシンプルで、まずGitHubリポジトリに`.claude-plugin/marketplace.json`を作成し、マーケットプレイスを定義します。次に、その中に含まれる個々のPluginsのディレクトリに`.claude-plugin/plugin.json`を配置します。その後、展開したいClaude Codeの設定ファイル（例えばCustom slash commandの定義ファイル）をPluginsのディレクトリ内に配置し、GitHubにプッシュするだけで構築が完了します。

利用する際は、Claudeコンソールで`/plugin marketplace add [GitHubリポジトリ名]`コマンドを用いてマーケットプレイスを登録し、続いて`/plugin install [プラグイン名]@[マーケットプレイス名]`でPluginsをインストールします。インストール後、Claude Codeを再起動すれば、`/development-plugin:hello`のようにPluginsが提供するコマンドが利用可能になります。

著者は、Pluginsを活用することで開発組織全体での開発手法やワークフローの標準化が容易になり、開発効率の大幅な向上が期待できると主張しています。実際にファインディ社では、共通のCustom slash commandsやPull request作成用のAgent SkillsなどをPlugins化し、既に開発効率向上に役立てていると具体例を挙げています。この機能は、AIを活用した開発環境のガバナンスと効率性を向上させる上で非常に重要な役割を果たすでしょう。