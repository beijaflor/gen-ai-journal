## ReAct 論文と共に読み解く strands-agents/sdk-python の実装

https://zenn.dev/aws_japan/articles/2025-11-17-react-strands-agents

AWS Japanのエンジニアが、AIエージェントの基盤技術であるReActパラダイムを解説し、その考え方がオープンソースの`strands-agents/sdk-python`でいかに実装されているかを詳細に分析する。

**Content Type**: Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:5/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[AIエージェント, ReActパラダイム, LLM, Python SDK, Tool Use]]

本記事は、AIエージェント開発において中心的な役割を果たす「ReAct (Reasoning and Acting)」パラダイムの理論と、AWSが提供するオープンソースSDK「strands-agents/sdk-python」におけるその具体的な実装について深く掘り下げています。著者は、2022年に発表されたReAct論文が、LLMが推論（Reasoning）と外部ツールを用いた行動（Acting）を組み合わせることで、複雑なタスクを効果的に解決するための汎用的な枠組みを提唱している点を強調します。このアプローチでは、思考（Thought）や推論の軌跡といった「言語空間での行動」をエージェントの行動空間に含めることで、LLMが自身の推論過程をコンテキストとして蓄積し、より賢明な次の行動を計画できるようにします。

なぜこれが重要かというと、LLMの登場以前は広大な言語空間を含む学習は非現実的でしたが、高性能な事前学習済みLLMが可能にしたからです。記事では、`strands-agents/sdk-python`がReActパラダイムをいかに具現化しているかを、実際のコード（`Agent`クラスの`__call__`メソッドから`event_loop_lifecycle`関数に至るまで）を辿って解説しています。このSDKでは、エージェントが「Agentic loop」を通じてLLMによる推論とツール実行を繰り返す構造が採用されており、特に`Messages`というデータ構造が、思考、行動、観測といった一連の情報を逐次保持し、LLMが次のステップを推論するための重要なコンテキストとして機能していることを示します。

具体的には、ユーザーからの問い合わせに対して、LLMがウェブ検索を計画し（思考）、ツールがウェブ検索を実行し（行動）、その結果を観測として受け取り、最終的にLLMが情報を整理して回答を生成するまでの一連のプロセスが、Messagesへの情報追加とイベントループのサイクルとして詳細に説明されています。この実装を理解することで、ウェブアプリケーションエンジニアは、自身のAIエージェントがどのようにして賢い振る舞いをするのか、その内部メカニズムを深く理解し、より高度で堅牢なエージェントシステムを構築する上で不可欠な知見を得ることができます。