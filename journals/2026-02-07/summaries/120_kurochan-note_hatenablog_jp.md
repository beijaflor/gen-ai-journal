## tmux上のClaude CodeやらCodexやらCopilotのCLIからShift + Enterを送信できるようにする

https://kurochan-note.hatenablog.jp/entry/2026/02/03/074837

tmux経由でAI CLIツールを利用する際に、Shift + Enterによる改行入力を可能にする設定方法を解説する。

**Content Type**: Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[tmux, Claude Code, GitHub Copilot CLI, Kitty keyboard protocol, CLI Workflow]]

普段から **tmux** を利用している開発者が、 **Claude Code** や **GitHub Copilot CLI** などのAIツールをターミナル上で使用する際に直面する「複数行入力ができない」という問題を解決するためのTipsを解説しています。これらのモダンなCLIツールは、 **Kitty keyboard protocol** を通じて **Shift + Enter** による改行を認識しますが、 **tmux** を経由するとこの入力が正しく中継されず、単なる改行（CR/LF）として認識されてしまう仕様上の課題があります。

記事では、ターミナルエミュレーターの **Ghostty** と **tmux** を組み合わせた環境において、 **.tmux.conf** に `bind -n S-Enter send-keys Escape "[13;2u"` という設定を1行追加することで、入力を本来期待されるエスケープシーケンスにリマップして送信する解決策を紹介しています。 **tmux** 側でプロトコルに完全対応するのは困難ですが、この設定だけでAIツールへのスムーズな複数行プロンプト入力が可能になります。 **CLI** ベースのAIコーディングツールを活用しつつ、ターミナルマルチプレクサの利便性も維持したいエンジニアにとって、即座に導入できる極めて実用的な知見です。