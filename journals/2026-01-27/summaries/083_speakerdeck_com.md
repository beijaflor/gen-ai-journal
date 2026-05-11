## AI Agent / Agentic Workflow の可観測性 / Observability of AI Agent Agentic Workflow

https://speakerdeck.com/yuzujoe/observability-of-ai-agent-agentic-workflow

AIエージェント特有の非決定的な挙動に対し、**OpenTelemetry**の**Span Links**等を活用して「説明可能性」を担保する可観測性の実装指針を提示する。

**Content Type**: Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 82/100 | **Overall**: 88/100

**Topics**: [[Agentic Workflow, OpenTelemetry, Span Links, Explainability, LLM Observability]]

LayerXの**Ai Workforce**事業部が実践する、AIエージェントおよび**Agentic Workflow**（半決定論的ワークフロー）の可観測性への技術的アプローチを解説しています。従来の可観測性の3要素（Metrics, Logs, Traces）では、LLMの判断根拠や非同期処理の繋がりを追いきれないという課題に対し、単なる状態の観測を超えた「説明可能性（Explainability）」の実現を目指しています。

具体的な技術手法として、**OpenTelemetry**の**Span Links**を活用してジョブ投入側とワーカー側のトレースを親子関係に縛られずに関連付ける手法や、**W3C traceparent**を用いた非同期境界の伝播、`decision_path`（判断経路）や`tenant_id`を属性に組み込むカスタム計装を詳述。これにより、LLMの判断理由がブラックボックス化するのを防ぎ、エラー発生時の原因がLLM、DB、外部APIのどこにあるかを特定可能にします。また、計装を本番だけでなく開発環境から導入することの重要性も説いています。

**Agentic Workflow**の実装において、デバッグや信頼性向上のためのトレーシング設計に悩むバックエンドエンジニアやAIエンジニアにとって、実務に即した具体的なリファレンスとなる内容です。