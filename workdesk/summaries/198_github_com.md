## ウェブドキュメントをAIエージェント用「スキル」へ変換する：agent-skills-generator

https://github.com/rodydavis/agent-skills-generator

**Original Title**: agent-skills-generator: Generate agent skills from website documentation

ウェブサイトのドキュメントを巡回し、AIエージェントやLLMに最適化されたMarkdown形式の「スキル」を自動生成する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 54/100 | **Annex Potential**: 50/100 | **Overall**: 76/100

**Topics**: [[AI Agents, RAG, Web Scraping, LLM Context, VS Code Extension]]

ウェブサイトの公開ドキュメントを、AIエージェントやLLMが即座に利用可能なMarkdown形式の「スキル」として変換・出力するオープンソースツール **agent-skills-generator** が公開されました。本プロジェクトは、GUIで直感的にクローリングルールを管理できる **VS Code Extension** と、高速な再帰的クローリングを実行する **Go CLI** の2つのツールで構成されています。

技術的な特徴として、トークン消費効率を最適化するためのクリーンな **HTML to Markdown** 変換機能を備えており、元のURLやタイトルを含む **Frontmatter** の自動抽出にも対応しています。また、**RAG（検索拡張生成）** との親和性を高めるために、ディレクトリ構造を排したフラットなストレージ出力を選択可能です。開発者は特定の技術ドキュメントのURLを指定し、サブパスの包含・除外ルールを設定するだけで、最新のライブラリ仕様などをエージェントの推論コンテキストとして容易に統合できるようになります。

外部ライブラリの最新仕様や独自フレームワークのドキュメントを、AIエージェントやカスタマイズされたLLMワークフローに効率よく組み込みたいエンジニアにとって、データ準備のパイプラインを簡素化する非常に実用的なツールです。