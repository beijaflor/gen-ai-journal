## Human-in-the-Loop な AI エージェントを支えるガードレール設計

https://www.wantedly.com/companies/wantedly/post_articles/1038437

確率的に動作するLLMの出力を制御し、信頼性の高いAIシステムを構築するためのガードレール設計手法を解説する。

**Content Type**: Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 82/100 | **Annex Potential**: 78/100 | **Overall**: 84/100

**Topics**: [[AI Guardrails, Self-consistency, Rate Limiting, Exponential Backoff, Software Architecture]]

Wantedlyの「AIエージェントモード」における、LLMの安全性を担保するためのガードレール設計に関する技術解説です。**Amazon Bedrock Guardrails**や正規表現などの手法では対応が困難な「採用文脈におけるドメイン知識」に基づいたセマンティックなバリデーションを実現するため、**ガードレール専用LLM**を層として組み込む設計を採用しています。

主な技術的ポイントは、LLM特有の課題に対する具体的な解決策です。まず、出力の揺らぎ（不確実性）に対しては、**Self-consistency**という手法を導入しています。これは同一プロンプトで複数回の推論を行い、その結果をスコアリングして平均値を閾値判定することで、単一推論よりも高い判定精度を確保するアプローチです。また、複数回の推論実行によって懸念されるAPIのレートリミット到達問題については、**Exponential backoff + Full Jitter**を用いたリトライ戦略を実装し、**Thundering Herd問題**を回避しながらシステムの可用性を高めています。

運用面では「誤検知は避けられない」という前提に立ち、判定ログのモニタリングを通じて**Few-shot**プロンプトを継続的に改善するサイクルについても言及されています。確率的な挙動を伴うAIを、信頼に足るシステムコンポーネントとして実装したいバックエンドエンジニアにとって、非常に実用的なリファレンスです。