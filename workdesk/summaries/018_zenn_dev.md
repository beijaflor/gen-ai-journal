## Claude Code標準機能だけで実践する仕様駆動開発

https://zenn.dev/flinters_blog/articles/0601de84c0eb91

仕様駆動開発を**CLAUDE.md**の設定と**Planモード**だけで完遂し、AIの文脈肥大化問題を根本から解決するワークフローを提示する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 83/100 | **Annex Potential**: 82/100 | **Overall**: 80/100

**Topics**: [[Claude Code, 仕様駆動開発 (SDD), CLAUDE.md, エージェントオーケストレーション, 文脈管理]]

**Claude Code**の標準機能のみを組み合わせ、**仕様駆動開発（SDD）**を実戦投入するための具体的なワークフローを紹介しています。**CLAUDE.md**の設定を通じてAIを「マネージャー（オーケストレーター）」役に固定し、実装前の仕様定義を徹底させる運用ルールに焦点を当てています。

主要なテクニックとして、**Planモード**で**AskUserQuestion**ツールを強制し、実装前に曖昧な点を人間に問い詰めさせることで仕様の穴を塞ぎます。仕様確定後はあえて**コンテキストをリセット**し、作成されたPlanファイルを**Single Source of Truth**として読み込ませることで、会話の肥大化による「AIの物忘れ」を防止します。また、実作業を**subagent**に委譲することで、本体エージェントのコンテキストを常にクリーンに保つ管理手法が解説されています。

AIとの対話が長引くほど精度が低下する現象に悩んでいる開発者や、**Claude Code**を無秩序なコード生成ツールではなく、統制された開発パートナーとして運用したいエンジニアに強く推奨されます。