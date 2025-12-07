## A2A を基礎から学ぶ (4) Function Calling による複数 Agent の選択的呼び出しの実装

https://zenn.dev/sakura_internet/articles/72af3abdfe5c5b

本記事は、A2AアーキテクチャにおいてFunction Callingを利用し、Planner Agentが複数のWorker Agentから適切なものを選択的に呼び出す実装方法を解説します。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 79/100 | **Overall**: 80/100

**Topics**: [[AI Agent, Function Calling, A2A Protocol, LLM Orchestration, Agent-to-Agent Communication]]

本記事は、AI Agent間（A2A: Agent-to-Agent）の連携を深く掘り下げるシリーズの第4回として、LLMの「Function Calling」機能を活用して、Planner Agentが状況に応じて最適なWorker Agentを選択的に呼び出す実装方法を詳説します。

著者はまず、Function Callingの基本概念を解説します。これは、LLMに外部ツール（本記事ではWorker Agent）を登録し、ユーザーのプロンプトに基づいてLLMがどのツールを呼び出すべきかをクライアント（Planner Agent）に指示するメカニズムです。OpenAIが2023年6月に発表して以降、ClaudeやGeminiにも採用され広く普及しています。記事では、`tools`として関数名、説明、パラメーターをJSON形式で定義し、LLMがこれらの情報を用いて適切な関数（Agent）と引数を選択する具体的なプロセスをコード例で示しています。

さらに、著者はFunction CallingとAnthropicが発表したMCP（Monolithic Component Protocol）との比較を行い、Function Callingが当初モノリシックな構成であったのに対し、MCPはプロトコルがオープンで外部ツールを容易に組み込める利点があったと指摘します。しかし、A2AプロトコルとFunction Callingを組み合わせることで、A2Aが通信レイヤーを補完し、Function Callingのモノリシックな構成を克服し、外部Agentを動的にツールとして登録・呼び出しできるようになるという相性の良さを強調しています。

実践的な実装例として、著者はPlanner Agentが「質問応答Agent (AgentB)」と「時刻Agent (AgentC)」という2つのWorker AgentをFunction Callingのツールとして登録し、ユーザーの質問内容に応じて適切なAgentを選択してタスクを依頼するNode.jsコードを提示しています。ユーザーが「今何時ですか？」と問えば時刻Agentを、一般的な知識を問えば質問応答AgentをLLMが判断して呼び出すデモンストレーションを通じて、Function Callingがいかに賢くAgentを切り替えるかを示しています。これにより、開発者は複雑なタスクを専門のAgent群に効率的に分散させ、より柔軟で強力なAIアプリケーションを構築できると著者は結論付けています。Webアプリケーションエンジニアにとって、これはAIを活用したシステムの設計において、ユーザーの意図を汲み取り、適切なAI機能を動的に連携させるための実践的な知見となるでしょう。