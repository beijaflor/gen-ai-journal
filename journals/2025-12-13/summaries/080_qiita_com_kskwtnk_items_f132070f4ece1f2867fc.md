## Figma MCPを活かすためのデータ作りとプロンプト 20パターンの検証で分かったこと

https://qiita.com/kskwtnk/items/f132070f4ece1f2867fc

Figma MCP（Multiplayer Component Platform）を活用し、高品質なコードを生成するためのFigmaデータ作成方法とプロンプト設計の最適解を、20パターンにわたる詳細な検証を通じて導き出す。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 96/100 | **Annex Potential**: 93/100 | **Overall**: 96/100

**Topics**: [[Figma MCP, AIコード生成, プロンプトエンジニアリング, Tailwind CSS, フロントエンド開発]]

この記事では、Figma MCPを用いて高品質なコードを生成するために、Figmaデータの構築方法とプロンプトの指示方法を、20パターンの検証を通じて深掘りしています。著者は、FigmaのVariables、Auto Layout、Layer Names、Annotationsといった各機能が生成されるコードにどのような影響を与えるかを体系的に分析しました。

検証の初期段階では、意外な発見がありました。Auto Layoutは絶対配置からFlexboxベースのレイアウトへとコード構造を大きく改善する上で最も重要であり、これはプロンプトだけでは補えない根本的な要素であると判明しました。一方、Variables（デザイントークン）を有効にすると、シンプルなプロンプトではTailwindの標準クラスではなくCSS変数による任意値が出力され、セマンティックHTML化やインタラクティブ要素の生成が抑制される問題が見られました。Layer Namesは`data-name`属性を追加しデバッグ性を向上させましたが、コード構造自体には影響しませんでした。Annotationsは単体での効果は限定的でしたが、特定の組み合わせではTypeScriptのインターフェース生成に貢献することもありました。

しかし、検証を進める中で転換点が訪れます。シンプルなプロンプトではFigma MCPの潜在能力を最大限に引き出せないことが判明し、プロンプトの詳細化が必須であることが浮き彫りになりました。VariablesのTailwind標準クラスへのマッピング、Semantic HTML要素（`<header>`, `<a>`, `<button>`など）の使用、hover状態やtransitionなどのインタラクティブ要素の追加、TypeScriptインターフェースの定義やデータ駆動型のアプローチ（`.map()`による繰り返し要素のレンダリング）といった具体的な要件をプロンプトで明示的に指示することで、初期の課題が解決されました。

最終的な結論として、高品質なコード生成には、Figmaデータの全要素（Variables、Auto Layout、Layer Names、Annotations）を適切に活用することと、これらの意図をAIに正確に伝える包括的かつ詳細なプロンプトの両方が不可欠であると著者は強調しています。特に、Auto Layoutがレイアウト構造の基礎を築き、VariablesがFigma側の効率化とコード品質の両立を可能にするためには、適切なプロンプトが前提となります。この記事は、Figma MCPを実務に導入しようとするデザイナーやエンジニアに対し、具体的な設定とプロンプトテンプレートを提供し、高品質で保守性の高いAIコード生成を実現するための道筋を示しています。