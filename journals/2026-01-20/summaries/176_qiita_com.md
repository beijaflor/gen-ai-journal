## Vercelが公開したAgent Skillsが便利な気がしたので早速Claude Codeに入れてみた

https://qiita.com/RioooJackpot/items/fee34d0e7dc119ed01a0

Vercelが公開したAIエージェント向け知識拡張ツール「Agent Skills」の導入方法と、実地検証に基づく著者の批判的な評価を提示する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:3/5 | Anti-Hype:5/5
**Main Journal**: 72/100 | **Annex Potential**: 76/100 | **Overall**: 76/100

**Topics**: [[Agent Skills, Vercel, Claude Code, React Best Practices, AI Coding Agents]]

2026年1月、VercelがReactおよびNext.jsの最適化ノウハウをAIエージェントに注入するための「Agent Skills」を公開した。本記事は、その導入手順と、実際に丸一日使用した上での極めて現実的な評価をまとめたものである。著者は当初、Vercel公式の知見をClaude CodeやCursorに統合できる点に高い期待を寄せていたが、最終的には「有用とは言えない」としてアンインストールに至っており、AIツール選定における冷静な視点を提供している。

技術的な側面として、Agent SkillsはMCP（Model Context Protocol）サーバーではなく、CLIコマンドを通じてAIエージェントに特定の知識やワークフローを追加する仕組みを採用している。`npx add-skill vercel-labs/agent-skills` という単一のコマンドで、マシンにインストールされているClaude Code、Cursor、VSCodeなどの主要エージェントを自動検出し、一括でスキルをセットアップできる。この導入の容易さは、従来のMCP設定と比較しても非常に洗練されていると著者は評価している。

提供されるスキルは主に2種類である。一つは「vercel-react-best-practices」で、Vercelが10年以上の本番運用で培った知見を45のルールに凝縮したものだ。特に「ウォーターフォールの排除」や「バンドルサイズの最適化」をクリティカルな優先事項として掲げており、useMemoなどの細かな最適化よりも、まずAPIコールの順序といった大きな影響力を持つ部分から改善を促す設計となっている。もう一つは「web-design-guidelines」で、アクセシビリティ（WAI-ARIA）やモバイルのヒットターゲット、アニメーションのパフォーマンスなど、Vercelのデザインチームによる数百の設計判断がまとめられている。

しかし、著者はこれらのスキルを実戦投入した結果、重大な懸念を表明している。スキルの知識を前提として生成されたコードをレビューした際、かえって手直しが発生する頻度が高まったというのだ。著者は、生成AIに完璧なコードを書かせるための補足ツールとして期待していたが、現状では「ここに記載されているコードがあれば要注意と考えるべき」というレベルの評価に落ち着いている。「Vercel公式」というブランドに起因する期待値と、実際の開発効率の向上が乖離していることを示唆しており、エンジニアに対しては盲目的な導入を避け、自身のワークフローにおける実利を厳しく見極めるよう促している。