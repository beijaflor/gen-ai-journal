## プロンプトで祈るのはもうやめる。Outlines/Guidance で LLM の出力を 100% 制御する技術

https://qiita.com/harusato2806/items/1f73ed7d1d3e6af932a8

確率的な挙動に頼るプロンプトエンジニアリングを脱却し、**Constrained Decoding**を用いてLLMの出力を構造的に100%制御する手法を解説する。

**Content Type**: Standard articles
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 95/100 | **Annex Potential**: 92/100 | **Overall**: 80/100

**Topics**: [[Outlines, Constrained Decoding, JSON Schema, Pydantic, vLLM]]

LLMをシステムに組み込む際の「JSONフォーマットの崩れ」や「不要な応答文の混入」といった不確実性を、プロンプト（自然言語）ではなくデコーディングプロセスへの論理的制約で解決する手法を解説している。具体的には、**Outlines**や**Guidance**といったライブラリを活用し、正規表現や**JSON Schema**、**Pydantic**モデルを**有限オートマトン (FSM)**に変換。生成の各ステップで次に続くべきトークン以外をマスク（**Logit Masking**）する**Constrained Decoding**の仕組みを紹介し、構造的に正しい出力のみを物理的に保証する「お祈り不要」の開発パターンを提示している。

技術検証として、**vLLM**バックエンドと**Outlines**を組み合わせた実装例を掲載。正規表現による厳密なIPアドレス生成や、**Pydantic**を用いた型安全なオブジェクト生成、**Enum**による値の制限などを具体的に示している。この手法は出力の信頼性を100%に近づけるだけでなく、思考過程や謝罪文などの不要なトークン生成をスキップできるため、結果として生成速度の向上とリトライコストの削減に直結するという洞察が示されている。

RAGや自律型エージェントの実装において、LLMの出力をプログラムで確実に扱いたい開発者や、不安定な出力に伴う例外処理に苦慮しているエンジニアにとって、本番環境の安定性を高めるための極めて実践的なガイドである。