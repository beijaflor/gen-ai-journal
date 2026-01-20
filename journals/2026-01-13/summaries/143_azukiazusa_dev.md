## Figma MCP でデザインシステムを提供して AI コーディングエージェントに一貫したフロントエンドコードを書かせる

https://azukiazusa.dev/blog/using-figma-mcp-to-provide-design-system-for-ai-coding-agents/

Figma MCPとStorybook MCPを活用して、AIコーディングエージェントにデザインシステムの文脈を直接提供し、一貫性のあるフロントエンドコードを生成させる手法を解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 83/100 | **Overall**: 88/100

**Topics**: [[Figma MCP, Claude Code, Storybook MCP, デザインシステム, デザイントークン]]

AIコーディングエージェント（Claude Codeなど）にフロントエンドの実装を任せる際、特定の配色やフォントに偏る「AI Purple Problem」と呼ばれる画一的なデザインが生成されやすい課題がある。著者はこの問題を解決するため、Figma MCP（Model Context Protocol）サーバーを通じてデザインシステムの詳細なコンテキストをエージェントに提供し、プロジェクト固有のデザインガイドラインを遵守させる具体的なワークフローを提示している。

主な手法として、まずFigma MCPを使用してFigma上のデザインデータ（レイアウト、タイポグラフィ、カラー等）にアクセス可能な環境を構築する。特筆すべきは、Figma公式が提供する「Skills」をClaude Codeに導入することで、エージェントがFigma MCPツールを効果的に使用するためのガイドライン（実装知識）を学習させている点だ。これにより、`get_variable_defs`ツールを用いてデザイントークンを抽出し、自動的にTailwind CSS v4のCSS-first configuration形式へ変換するといった高度なタスクを精度高く実行させている。

また、Storybook MCP Addonを併用することで、AIが既存コンポーネントを再利用したり、Storybookのベストプラクティスに従ったStory実装を行ったりするフローを解説している。ページ全体の実装においては、コンテキスト制限（最大トークン数）を回避するために、Figma側でレイヤーを適切に分割し、セクション単位でエージェントに指示を出す「分割実装」の重要性を説いている。

筆者は、AI時代においてはコード実装そのものが自動化されるため、エンジニアの役割は「Figmaでの正確なデザイン設計」や「デザインシステムの整備」といった、AIに正しいコンテキストを与えるための設計能力にシフトしていくと主張している。FigmaのAuto LayoutやVariants、Variablesを適切に使いこなすことが、高品質なコードを素早く生成するための鍵となるという視点は、これからのフロントエンドエンジニアにとって極めて実践的な示唆を含んでいる。