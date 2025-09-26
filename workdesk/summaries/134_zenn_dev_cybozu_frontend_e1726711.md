## Storybook公式MCPの解説とその先 - Design Systems with Agentsの提案について

https://zenn.dev/cybozu_frontend/articles/e17267112d7816

Storybook公式MCPアドオンがAIエージェントによるストーリーファイル生成を高度化し、デザインシステムとの連携を深めるAgentic WorkflowとDesign Systems with Agentsの提案を解説します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 84/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[Storybook MCP Addon, AIエージェント, デザインシステム, Agentic Workflow, UI開発]]

Storybookに公式の「MCP Addon」が導入され、AIエージェントがStorybookのコンポーネント情報に直接アクセスし、利用できるようになりました。このアドオンは、AIがStorybookのベストプラクティスに沿ったストーリーファイルを高精度で生成することを可能にします。実際にButtonコンポーネントのストーリーを生成する例では、MCPを活用することで、play関数やイベントのモックを利用したテストコード、多様な状態パターンを含む、より高品質で実践的なストーリーが自動生成されることが示されています。これにより、AI生成コードの品質とStorybook機能の活用が飛躍的に向上します。また、大規模なプロジェクトで必要なコンポーネントを素早く見つけるためのStory URL提示機能も提供します。

このアドオンの登場は、AIによるUI開発における「見えない壁」、すなわちAIが生成したUIの見た目や動作を事前に確認しにくいという課題への重要な一歩です。さらに、将来的な展望として「Agentic Workflow RFC」が提唱され、AIが自身の生成物を見直し、改善する仕組みが議論されています。

そして、最も注目すべきは「Storybook Design Systems with Agents RFC」の提案です。現状、AIはデザインシステムに準拠せず、既存のコンポーネントとは異なる独自のパーツやスタイルを生成しがちです。このRFCは、Storybookがコンポーネント情報をまとめた「コンポーネント・マニフェスト」を生成し、「Design System MCP Server」を通じてAIエージェントがこれを活用できるようにするものです。マニフェストには、利用可能なコンポーネントのリスト、Propsの詳細、使用例などが含まれ、AIはこれらを参照することでデザインシステムの一貫性を保ったUIを開発できるようになります。この取り組みは段階的な実装が計画されており、Storybookをデザインシステムの「Single Source of Truth」として運用する企業にとって、AIとデザインシステムの連携を深め、大規模なフロントエンド開発の効率と品質を劇的に高める、非常に夢のある提案です。