## Temporal Knowledge Graphで作る！時間変化するナレッジを扱うAI Agentの世界

https://tech.layerx.co.jp/entry/tkg-agent

LayerXが、時間と共に変化するナレッジを動的に扱うAI Agent開発のため、Temporal Knowledge GraphとGraphitiを活用したPoCと実践的ノウハウを具体的に解説します。

**Content Type**: Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 91/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[AI Agent, Temporal Knowledge Graph, Graphiti, Knowledge Graph構築, RAG]]

LayerXのエンジニアが、時間と共に変化するナレッジを扱うAI Agentの構築に不可欠なTemporal Knowledge Graph (TKG) の概念とその具体的な活用法を解説します。静的な知識グラフでは対応しきれない、企業ルールやユーザーの嗜好など動的に進化する情報をAI Agentが長期記憶として扱えるようにする点が重要です。特にOSSフレームワークであるGraphiti（Zep）を核に、その3層構造（エピソード、セマンティックエンティティ、コミュニティサブグラフ）がどのようにして生データの損失なく、時間的文脈を保持しつつ知識を動的に表現するかを詳述します。

同社が「バクラク」のAI申請レビュー機能向けに行ったPoCでは、TKGを導入することで、以下のような動的なナレッジ運用が実現されました。
1.  **自然言語でのルール変更取り込み**: ユーザーが自然言語で入力した申請ルールの変更をリアルタイムに反映し、即座にAI Agentの判断に適用します。
2.  **差し戻しコメントからの学習**: 人間による差し戻しコメントから自動的にルールを拡張し、同様の申請に対するレビュー精度を向上させます。
3.  **曖昧なルールの発見と補完**: 社内規定文書の曖昧な箇所をAI Agentが自律的に発見し、ユーザーの回答に基づいてルールを明確化します。

これらの機能は、LLMを活用したエンティティ/リレーション抽出パイプラインと、LangGraph、Azure OpenAI、Graphitiを組み合わせることで実現されています。実装プラクティスとしては、日本語特有の主語省略への対応を含むプロンプトエンジニアリング、効率的なグラフ構築のためのバルクインサート、マルチテナント対応のための`group_id`の活用、Context Recallを重視した検索クエリ生成などが紹介されています。TKGはAI Agentがユーザーの世界を深く学び、サービスにとって強力な資産となり、競合に対する差別化要因となる基盤であることを強調します。