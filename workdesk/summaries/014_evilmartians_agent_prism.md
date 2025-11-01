## AIエージェントのデバッグを高速化するオープンソースライブラリ「AgentPrism」

https://evilmartians.com/chronicles/debug-ai-fast-agent-prism-open-source-library-visualize-agent-traces

**Original Title**: Debug AI fast with this open source library to visualize agent traces

Evil MartiansとQuotient AIが協力し、AIエージェントのデバッグ時間とコストを大幅に削減する視覚化ライブラリAgentPrismをオープンソースとして公開しました。

**Content Type**: Tools
**Language**: en

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[AI Agent Debugging, Observability Tools, OpenTelemetry, React Components, Developer Workflow]]

Evil Martiansは、AIエージェントがサイレントに失敗したり、無限ループに陥ったり、誤ったツールを呼び出したりする際に、JSONログの手動解析によるデバッグが非効率的で多大な時間とコストを要するという課題に直面していました。この問題は、企業顧客が求める堅牢なデバッグ・モニタリング機能がLLM駆動型エージェントのオブザーバビリティで追いついていない現状から生じていました。

この課題を解決するため、Evil MartiansはQuotient AIと協力し、AIエージェントのトレースを視覚化するオープンソースのReactコンポーネントライブラリ「AgentPrism」を開発しました。人間が視覚パターン認識に優れているという洞察に基づき、AgentPrismはOpenTelemetryによる体系的なトレース追跡を通じて、JSONでは見えづらかったループや問題のあるパターンを視覚的に明確に提示します。これにより、デバッグ時間を数時間から数秒に大幅に短縮し、モデル呼び出しの冗長性やAPIの誤順序によるコストを削減できると著者は強調しています。

AgentPrismは以下の4つの主要なコンポーネントを提供し、デバッグワークフローの中核的なニーズに対応します。
1.  **ツリービュー (Tree View)**: エージェントのステップ間の階層構造と親子関係を表示し、問題のあるパターンを赤くハイライトします。
2.  **タイムラインビュー (Timeline View)**: ガントチャート形式で実行フローを示し、時間の浪費、ボトルネック、並行処理の問題を明らかにするとともに、リアルタイムのコスト積算も行います。
3.  **詳細パネル (Details Panel)**: 各ステップの入出力データ、コスト内訳、パフォーマンスメトリクスなど、必要なコンテキストを簡潔に表示します。
4.  **シーケンスダイアグラム (Sequence Diagram)**: プロンプトと応答の視覚的なフローをステップバイステップで再生し、複雑な意思決定チェーンや循環ロジックの理解・特定を容易にします。

技術的には、AgentPrismはpnpm、TypeScript、React、Viteを用いたモノレポとして構築されており、アクセシビリティに優れた（Radix/ARIA準拠）テーマ設定可能なUIコンポーネントと、OTLPデータをコンパクトなUIスキーマに変換するデータサービスを含みます。既存のスタックに簡単に統合できるよう、shadcnスタイルでコンポーネントのソースコードを配布しており、外部ダッシュボードへのコンテキスト切り替えなしにIDE内でネイティブなデバッグ体験を提供します。

このライブラリは、即座のパターン認識、デバッグ時間の80%削減、リアルタイムコスト監視、業界標準のOpenTelemetry基盤により、AI開発者が信頼性の高い製品を5倍速く出荷できる価値を提供します。