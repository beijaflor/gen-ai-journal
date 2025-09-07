## Gemini 2.5 Flash Image（nano-banana）で画像生成MCPサーバーを作った

https://zenn.dev/shinpr_p/articles/2afc87be0eaed7

開発者は、GoogleのGemini 2.5 Flash Image (nano-banana) を活用し、キャラクターの一貫性や画像ブレンドを可能にする画像生成MCPサーバーを実装し、開発ワークフローを効率化した。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 76/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[Generative AI, MCP, Gemini API, Agentic Coding, 開発ワークフロー効率化]]

この記事は、個人開発における画像生成ワークフローの課題を解決するため、Googleがリリースした「Gemini 2.5 Flash Image (コードネーム：nano-banana)」を活用した画像生成MCP（Model Context Protocol）サーバーの実装について解説しています。従来の画像生成AIでは難しかったキャラクターの一貫性維持や、複数の画像素材を自然にブレンドする機能にnano-bananaが優れており、品質とコストパフォーマンスの高さから開発効率向上の鍵となると筆者は指摘します。

Webアプリケーションエンジニアにとって重要なのは、このMCPサーバーがClaude CodeやCursorのようなLLM対応IDEに直接統合され、AIによる意図解釈に基づいて画像生成APIの高度な機能を活用できる点です。具体的には、`maintainCharacterConsistency`、`blendImages`、`useWorldKnowledge`といったGemini APIの独自パラメータをMCPツールの引数として定義し、LLMがユーザーの指示を解析してこれらのフラグを自動的に設定することで、より文脈に沿った正確な画像生成が可能になります。これにより、開発者は画像生成とコード組み込みの往復作業から解放され、よりスムーズなクリエイティブ作業に集中できます。

しかし、実装過程ではAgentic Coding環境特有の課題も浮き彫りになりました。特に、サブエージェントが生成する結合テストの不安定性（flakyなテスト）や、LLMが最新のSDK情報を認識しない問題は、AIを活用した開発における現実的な壁を示唆しています。これらの課題は、開発者がAIをワークフローに組み込む際に直面しうる実践的な教訓となり、「理想的なAI」と「現実的なAIの限界」のバランスを考慮することの重要性を強調しています。このMCPサーバーは、画像生成を伴うプロジェクトを進めるWebエンジニアにとって、実装の詳細と現実的な課題解決のヒントを提供する実践的なソリューションと言えるでしょう。