## Generative Agents を動かして遊ぶ

https://qiita.com/othelloman/items/7ed46bf59b7e1c7adf6e

スタンフォード大学らが提唱した「Generative Agents」をローカル環境で構築し、その内部ロジックを解析しながら日本語化や動作検証の手順を解説する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:3/5 | Anti-Hype:4/5
**Main Journal**: 90/100 | **Annex Potential**: 89/100 | **Overall**: 72/100

**Topics**: [[Generative Agents, LLM Simulation, Agent Architecture, Prompt Engineering, OpenAI API]]

本記事は、仮想空間内で自律的に行動するエージェントをシミュレートする研究プロジェクト「Generative Agents」を、現代のLLM環境に合わせて動作させ、その内部構造を深く考察した技術解説である。著者は、公式リポジトリが古いモデル（`text-davinci-003`など）に依存している点に注目し、`gpt-3.5-turbo-instruct`や`gpt-4`への移行、および日本語化のプロセスを具体的に示している。

著者が本記事を通じて提示している最大の意義は、単に「動かしてみた」という結果以上に、エージェントが「人間らしさ」を獲得するためのアーキテクチャの解明にある。シミュレーションは、知覚（Perceive）→計画（Plan）→行動（Act）→反応（React）→反省（Reflect）という緻密なサイクルで構成されている。著者の分析によれば、エージェントは一発のプロンプトで行動を決めているのではなく、個々の住人が持つ「空間記憶」や「対人関係の記憶」を都度LLMに参照させ、状態を微修正しながら連続性を保っている。

エンジニアにとっての実用的な知見として、LLMの出力をパースする際、プロンプトの日本語化が既存のパースロジック（`split()`など）を破壊してしまうという「LLM特有の不確実性」への対処法が語られている。また、`ChatCompletion` APIの`system`ロールを活用することで、英文の例文（few-shot）の強すぎる影響を緩和し、出力を制御するテクニックを提示している。

著者は、各エージェントが主体ごとに異なる関係性の要約を保持し、それを反省（Reflection）のプロセスで自己更新していく設計が、現在のエージェント型ワークフローを構築する上での重要なヒントになると主張している。高度な自律型エージェントを構築するには、LLMの推論能力だけに頼るのではなく、記憶と内省をどうシステムに統合すべきかという、具体的な実装パターンの重要性を再確認させる内容となっている。