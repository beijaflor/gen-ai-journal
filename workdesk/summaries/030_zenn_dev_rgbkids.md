## あるべき場所に帰ろう！ReActに立ち返りClaude Code + Playwright MCP + Figma MCPでデザインを反映

https://zenn.dev/rgbkids/articles/e93e6e9ade48f2

Figmaデザインからのコード生成精度を飛躍的に向上させるため、ReActパラダイムとPlaywrightによるVisual Regression Test (VRT) を統合したAI自動化ワークフローを構築し、反復的な修正プロセスを実現します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[ReAct, Figma MCP Server, Playwright VRT, AI Code Generation, Agent-based Development]]

FigmaデザインからのAIによるコード生成は便利であるものの、その再現性の低さからFigma MCPサーバーの活用を諦めてしまうケースが少なくありません。本記事は、この課題に対し、ReAct (Reasoning and Acting) パラダイムを核とした、より高精度なデザイン反映を可能にする自動化ワークフローを提案します。

鍵となるのは、人間の職人技に依存しがちな作業をAIエージェントに反復的に実行させるReActの考え方です。提案されるワークフローは以下の三段階で構成されます。まず「思考 (Reasoning)」の段階では、Figma MCPサーバーを通じてFigmaのデザインデータが取得されます。次に「行動 (Acting)」として、Claude Codeなどの生成AIが取得したデータに基づいてHTMLファイルをコーディングします。最後に「観察 (Observations)」として、Playwright MCPサーバーがVisual Regression Test (VRT) を実行し、生成されたコードの視覚的な差異を検証します。

このワークフローの最大の特長は、VRTが合格するまで（例：視覚的な差異が10%以内になるまで）、AIが思考・行動・観察のサイクルを繰り返し、自動でコードを修正・改善する点です。これにより、単一のAIプロンプトでは実現が難しかった高精度なデザイン再現が可能となり、デザイナーやフロントエンドエンジニアの属人的な調整作業を大幅に削減できます。記事では、Figma MCPサーバーとPlaywright MCPサーバーの具体的な設定方法、およびVRT用のテストコード例も提示されており、Webアプリケーションエンジニアが自身の開発ワークフローにAIエージェントをより効果的に統合するための実践的な指針を示しています。これは、AIによるコード生成の「使えない」から「使える」への転換点となる重要なアプローチです。