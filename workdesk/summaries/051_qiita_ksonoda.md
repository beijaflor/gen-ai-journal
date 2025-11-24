## AIエージェントの新たな業界標準仕様：Oracle Open Agent Specification #LLM

https://qiita.com/ksonoda/items/f47dcde81b8a8bc6d889

OracleがAIエージェント開発の断片化に対応すべく、定義と実行を分離したフレームワーク非依存の標準仕様「Open Agent Specification (Agent Spec)」を導入し、エージェントの移植性、再利用性、拡張性を大きく推進する。

**Content Type**: Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 94/100 | **Annex Potential**: 87/100 | **Overall**: 92/100

**Topics**: [[AIエージェント, 標準化, マルチエージェント, Function Calling, フレームワーク相互運用性]]

AIエージェント市場は多様なツールが乱立し、フレームワーク間の相互運用性や移植性が課題となっています。本記事は、日本オラクルがこの課題に対応すべくリリースした新たな標準仕様「Open Agent Specification (Agent Spec)」を詳解しています。

著者はまず、AIエージェントがFunction CallingやMCP（Model Context Protocol）で外部サービスと連携し、マルチエージェント構成ではグラフデータモデルで複雑なタスクを協調処理する現状を紹介。特定のフレームワークに依存しがちな現状が、開発の柔軟性を妨げていると指摘します。

Agent Specは、AIエージェントとワークフローの「定義」と「実行」を分離することで、この課題を解決します。これはフレームワーク非依存の宣言型仕様であり、機械学習モデルのONNXのように、AIエージェント開発のエコシステムにおける相互運用性、移植性、再利用性、そして拡張性をもたらすことを目的としています。

Agent Specは、GoogleのAgent2Agent (A2A)やMCPの仕様を包括する設計であり、単一エージェントから複雑なマルチエージェント構成まで、簡素化されたコードで定義できる包括的なクラスを提供します。OCI Generative AIを含む多様なLLMや、付属のFlowライブラリによる複雑なワークフロー表現に対応しています。

その最大の利点は、Agent Specで定義したエージェントが、LangGraph、AutoGen、CrewAI、WayFlowといった複数の既存フレームワーク上で動作可能である点です。これにより、開発者は特定のフレームワークへのロックインを避け、将来的に登場する新機能を既存のエージェントに容易に組み込み、検証できるようになります。

記事では、OCI Generative AIやOllamaを用いたシンプルなエージェントの定義と実行、Tavily Searchを連携させたエージェント、コード生成とレビューを行うマルチエージェント、さらには既存のAutoGen環境にAgent Specで定義したエージェントを追加する例など、豊富なPythonコードサンプルを通じてその実用的な活用方法を具体的に示しています。

著者は、Agent Specのような標準化の動きが、新規参入を促し、業界全体の技術革新を加速させ、異なる企業が開発したエージェント間の連携を効率化することで、AIエージェント市場の持続的な成長を後押しすると強調しています。この新仕様がAIエージェント開発の未来を大きく変える可能性を秘めていると締めくくっています。