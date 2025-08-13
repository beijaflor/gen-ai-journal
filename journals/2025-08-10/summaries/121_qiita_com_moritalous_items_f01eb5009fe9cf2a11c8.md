## Serenaやってみた！StreamlitとStrands Agentsを組み合わせてオレオレコーディングエージェントを作る

https://qiita.com/moritalous/items/f01eb5009fe9cf2a11c8

「Serena」「Strands Agents」「Streamlit」を活用し、対話型コーディングエージェントを構築する実践的な手法を解説します。

**Content Type**: Tools

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 100/100 | **Overall**: 80/100

**Topics**: [[コーディングエージェント, Strands Agents, Serena, Streamlit, LLMツール連携]]

本記事は、Webアプリケーションエンジニアが自身の開発ワークフローに最適化されたAIコーディングエージェントを構築するための具体的な道筋を示します。著者は、近年注目されるAIエージェントフレームワーク「Strands Agents」と、IDE統合のための多機能な言語モデルツール「Serena」、そして手軽にWebUIを構築できる「Streamlit」を組み合わせることで、対話形式でコードを操作・生成する「オレオレコーディングエージェント」の作成手法を詳説しています。

特に重要なのは、「Serena」をMCP（Multi-Component Protocol）サーバーとして活用し、その豊富なツール群を「Strands Agents」のAgentから利用する連携モデルです。これにより、単なるコード生成に留まらず、既存のプロジェクト内でのファイル検索や特定パターンの修正といった複雑なタスクを、AIエージェントに実行させることが可能になります。記事では、`uv`によるプロジェクト初期化から、`StdioServerParameters`や`MCPClient`を用いたSerenaとの接続、`Strands.agent.Agent`でのBedrockモデル（Claude Sonnet 4など）の利用法、さらにはStreamlitで対話履歴を管理し、ツール呼び出しを可視化するUI構築まで、具体的なPythonコードを提示しながらステップバイステップで解説されており、再現性が非常に高いです。

このアプローチは、既成のAIコーディングツールでは手の届かない、きめ細やかな開発支援を実現する可能性を秘めています。プロジェクト固有のコードベースを理解し、その文脈に沿った正確な作業をAIに委ねられるようになるため、開発者はより創造的で戦略的な業務に集中できるでしょう。自身の開発環境にAIエージェントを深く組み込みたいと考えるWebエンジニアにとって、実践的な第一歩となる貴重なガイドと言えます。