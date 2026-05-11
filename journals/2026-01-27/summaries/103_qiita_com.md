## [RAG] Context-Aware Caching: 会話型 AI における「文脈を理解するキャッシュ設計」

https://qiita.com/tms-ducvu/items/f7eec536f790b73260aa

提唱する：会話型AIにおいて文脈を補完したクエリをキャッシュキーに用い、曖昧な入力に起因する誤回答を防ぐ設計手法。

**Content Type**: Technical Reference
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 79/100 | **Annex Potential**: 79/100 | **Overall**: 80/100

**Topics**: [[RAG, キャッシュ設計, AIエージェント, Semantic Cache Poisoning, Context-Aware Caching]]

従来のステートレスなキャッシュ設計が、文脈依存の強い会話型AI（**RAG**やエージェント）において「それはいくらですか？」のような曖昧なクエリで誤った回答を返すリスク（**Semantic Cache Poisoning**）を解説している。著者はこの問題の根本原因を、ユーザー入力をそのままキャッシュキーにすることにあると指摘する。

解決策として、LLMによる**文脈正規化（Context Normalization）**を経て生成された**Refined Query**（自己完結した質問）をキャッシュキーおよびベクトル検索に利用する「**Context-Aware Caching**」手法を提唱している。例えば「それはいくら？」という入力を履歴に基づいて「VinFast Presidentの価格はいくらですか？」に変換してから処理することで、誤情報の発生を防ぎ、回答精度を向上させる。

実用的なコード例を交え、キャッシュサイズ増加というトレードオフを許容してでも正確性を優先すべきだとする主張は、本番環境のAIアプリケーションを運用するエンジニアにとって重要な知見となる。**RAG**やチャットボットの実装において、キャッシュ起因のバグや精度の低下を回避したい開発者に最適な内容である。