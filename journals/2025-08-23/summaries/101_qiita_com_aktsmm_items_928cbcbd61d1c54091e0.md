## 簡単！M365 Copilot で MS Docs MCP を使う

https://qiita.com/aktsmm/items/928cbcbd61d1c54091e0

Copilot Studioを通じてM365 CopilotにMicrosoft Learn Docs MCPを連携させることで、公式ドキュメントに基づく正確かつ最新の回答を引き出し、Copilotの専門性を飛躍的に向上させる具体的な設定手順と検証結果を詳述する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[M365 Copilot, Copilot Studio, Microsoft Learn Docs MCP, AIエージェント, ドキュメント検索拡張]]

本記事は、M365 CopilotをMicrosoft製品の専門家として活用するため、Copilot Studioを介してMS Learn Docs MCP（Model Context Protocol）サーバーと連携させる具体的な手順と効果を詳述しています。これまでVS CodeのGitHub CopilotでDocs MCPを利用していたユーザーにとって、既存のM365 Copilot環境で追加コストなしに同様の機能を利用できる点が大きなメリットです。

この連携の最大の価値は、M365 CopilotがMicrosoft Learnの公式ドキュメントを参照することで、その回答の正確性と鮮度が飛躍的に向上することにあります。例えば、ネットワークセキュリティペリメーター（NSP）のGA状況に関する質問で、MCPが有効な場合は常に最新の正しい情報が返される一方、そうでない場合は古い情報や誤った回答が返されることが検証で示されています。これは、日々進化するクラウドサービスや新機能に対応するウェブアプリケーションエンジニアにとって、常に信頼できる最新情報を得られる点で非常に重要です。

設定はCopilot Studioで新規エージェントを作成し、「Docs MCP」ツールを追加するだけと非常に簡単です。さらに、生成AIの設定で「一般的なナレッジやWebの情報」の使用をオフにすることで、MCPサーバーからの回答を強制し、より確実な情報提供を実現できます。カスタムインストラクションを用いて回答スタイルや出典の表示ルールを細かく制御できる点も、開発ワークフローにおけるAIの信頼性を高める上で役立ちます。

Docs MCP以外のMCPサーバー（Outlook、D365、GitHubなど）との連携の可能性も示唆されており、このアプローチがM365 Copilotを多角的に強化する基盤となるでしょう。Microsoft製品を活用するエンジニアは、まずDocs MCP連携を試すことで、Copilotを「Azureの専門家」に変貌させ、日々の業務における情報検索の質と効率を大きく改善できるでしょう。