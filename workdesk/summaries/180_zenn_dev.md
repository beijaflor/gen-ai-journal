## GitHub Copilotを使いこなすための概念整理

https://zenn.dev/cbmrham/articles/202601-github-copilot-concepts

GitHub Copilotの仕組みを「コンテキスト管理」という視点から再定義し、最新機能を含む各種モードやカスタマイズ手法を体系的に提示する。

**Content Type**: Technical Reference
**Language**: ja

**Scores**: Signal:4/5 | Depth:5/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[GitHub Copilot, コンテキスト管理, AIエージェント, MCP, Planモード]]

GitHub Copilotの本質を「適切なコンテキストをLLMに与える技術」と定義し、基本の**Ghost Text**（インライン補完）から、最新の**Planモード**、さらには**Model Context Protocol (MCP)**や**Agent Skills**といった高度な拡張機能までを体系的に解説している。単なる操作マニュアルではなく、各機能がどのようにプロジェクト内の情報を収集し、どの程度の自律性を持って動作するのかというアーキテクチャの視点から情報を整理している点が特徴だ。

主要な知見として、補完の進化形である**Next Edit Suggestions (NES)**が編集履歴に基づき「次に修正すべき場所」を予測する仕組みや、**Ask/Edit/Agent/Plan**という4つのモードをタスクの複雑度に応じて使い分ける実戦的な指針を提示している。特に大規模な変更においては、**Planモード**で事前に実装計画をレビューし、その後**Agentモード**へ引き継ぐワークフローが有効であると述べている。加えて、プロジェクト固有のルールを定義する**.github/copilot-instructions.md**や、ディレクトリごとに指示を切り替える**AGENTS.md**、さらに**SKILL.md**を用いたスキルの段階的読み込み（Progressive Disclosure）など、大規模リポジトリでモデルの精度を維持するためのコンテキスト管理手法が詳述されている。

Copilotを単なる「高度なコード補完ツール」としてではなく、自律的な開発パートナー（AIエージェント）として使いこなし、開発プロセスの自動化を一段階進めたいと考えている全Webアプリケーションエンジニアにとって必読のガイドである。