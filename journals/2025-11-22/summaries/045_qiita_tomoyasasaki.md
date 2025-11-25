## Agent 365 MCPツールを触ってみる

https://qiita.com/tomoyasasaki1204/items/cb64a4eda6b4f738ea9d

マイクロソフトの佐々木氏は、2025年のIgniteで発表されたAgent 365 MCPツールをCopilot Studioに組み込むことで、Microsoft 365のサービスをAIエージェントが安全かつ柔軟に操作できる具体的な方法を解説します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[Microsoft Copilot Studio, Agent 365 MCP, Microsoft 365 Copilot, LLMエージェント, 開発ツール連携]]

マイクロソフトの佐々木氏が、2025年のIgniteで発表された「Agent 365 MCPツール」の概要とMicrosoft Copilot Studioへの具体的な統合方法を紹介しています。Agent 365 MCPは、Microsoft 365の各サービスをAIエージェントが安全に操作するための「ツールサーバー」群であり、監査可能でポリシー適用済みのAPIを提供することで、エージェントがメール送信、予定調整、ファイル操作などを実行できる基盤を構築します。このツールはMicrosoft 365管理センターの[エージェント]タブからアクセス可能で、Frontierプログラムへの申し込みが必要です。

記事では、主要なAgent 365 MCPをCopilot Studioのエージェントに追加するデモを通じて、その実用性を解説しています。

*   **Copilot Search MCP**: 社内のあらゆるMicrosoft 365リソースを横断的に検索し、根拠に基づいた回答を提供します。Copilot StudioエージェントからMicrosoft 365 Copilotをシームレスに呼び出し、例えば過去の会議の要約と根拠リンク提示といったシナリオで利用可能です。特化型MCPがない場合のフォールバックとしても機能します。
*   **Microsoft 365 User Profile MCP**: ユーザープロファイルや組織情報を取得し、特定のユーザーの直属の部下などを検索できます。「上司にメールを送信して」といったプロンプトに対して、EntraID上の上司のプロファイルを取得し、後続アクションに活用する用途が想定されます。
*   **Microsoft Outlook Mail MCP**: Outlookメールに関する操作全般に対応し、メールの作成・送信、自然言語やODataによる検索・フィルタリングが可能です。メールの下書き作成や送信、メールボックス内の検索などに利用できます。
*   **Microsoft Word MCP**: Wordファイルに対する操作全般（ファイルの生成、ドキュメントの取得、閲覧、コメント管理）に対応します。ユーザーのOneDriveルートに新しいWord文書を作成したり、メールの下書きにWordファイルを添付するなどの用途が考えられます。

著者は、Agent 365 MCPを利用することでユーザーの意図をかなり解釈してくれるようになったと感じており、従来のコネクタを介したMCPとの使い分けが今後の課題としつつも、その先進性を高く評価しています。特に、M365 Copilot MCPがオールラウンダーである一方、Outlook MCPやWord MCPが特定のタスクに特化している点が重要であり、開発者がこれらのツールを組み合わせることで、より高度なAIエージェントを構築できる可能性を示唆しています。