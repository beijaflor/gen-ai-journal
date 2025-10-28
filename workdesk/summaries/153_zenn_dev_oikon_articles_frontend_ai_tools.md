## Claude・Codex・Kombaiを使ったFigma to Codeの比較

https://zenn.dev/oikon/articles/frontend-ai-tools

Figmaデザインからコードを生成する際に、主要なAIツールであるClaude Code + Figma MCP、Codex CLI + Figma MCP、Kombaiの3つを詳細に比較し、それぞれの再現度、技術スタック、および実用性を評価する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[Figma to Code, AIコーディングツール比較, フロントエンド開発, Next.js, Material UI]]

この記事では、Figmaデザインからコードを生成するAIツールの現状と課題を掘り下げ、特にClaude Code、Codex CLI、Kombaiの3つのツールをFigma MCPとの連携を含めて比較検証している。著者によれば、フロントエンド開発におけるデザインからコードへの変換は、再現度、レスポンシブ対応、最新ライブラリ知識の欠如、保守性といった課題を抱えている。特にAIツールは、画像の解釈よりもFigmaのデザインデータを直接読み込む「Figma MCP（Multi-platform Client Protocol）」を使用することで、より正確なコンポーネント構造を認識し、デザイン忠実度を高められると指摘している。

実験では、共通のFigmaデザイン（Portfolio Design）とプロンプトを使用し、各ツールのコード生成能力を評価した。

1.  **Claude Code + Figma MCP**: Next.js 14、TailwindCSS、TypeScriptで13個のコンポーネントを生成。グラデーションやblur効果など細かなデザインニュアンスを再現できたものの、固定px値の使用によりレスポンシブ対応は部分的だった。
2.  **Codex CLI + Figma MCP**: Next.js 14（HTML混在）、カスタムCSS（BEM風）、TypeScriptで、セマンティックHTMLとアクセシビリティを重視した実装を生成し、レスポンシブ対応も良好。HTMLとReactコンポーネントの混在が特徴的。
3.  **Kombai**: フロントエンド特化型AIとして、React 18、Material UI (MUI) v5、Emotionを使用。MUIのブレークポイントシステムを活用した良好なレスポンシブ対応と、3ツール中最も高いデザイン再現度を達成したが、MUIへの依存性が強い点が挙げられた。

著者による比較結果では、デザイン再現度においてKombaiが約75-80%で最高、次いでCodex CLI (70-75%)、Claude Code (65-70%)という評価になった。どのツールも現時点ではピクセルパーフェクトな実装は難しいものの、約70%以上の忠実度でコードを生成可能であり、簡単な実装や開発の「叩き台」としては十分な精度であると結論付けている。しかし、生成されたコードのフレームワークやライブラリの整合性については、引き続きエンジニアによる評価と調整が必要であると強調している。