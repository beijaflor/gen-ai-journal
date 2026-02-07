## 読み取り専用のBacklog MCPを作成しました

https://qiita.com/s_moriyama/items/1ed558a637138cd1a2da

プロジェクト管理ツール**Backlog**の情報をAIエージェントが安全に取得できるよう、書き込み操作を物理的に遮断した読み取り専用の**MCP**サーバを公開し、その設計思想と設定方法を解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 82/100 | **Annex Potential**: 78/100 | **Overall**: 80/100

**Topics**: [[Backlog, MCP (Model Context Protocol), AI Agent, Security, kiro]]

本記事は、プロジェクト管理ツール**Backlog**のデータをAIエージェントから安全に参照するために開発された、読み取り専用の**MCP (Model Context Protocol)**サーバを紹介しています。公式のMCPサーバは高機能ですが、AIによる意図しない書き込みや誤操作を防ぐ「読み取り専用」の制約が不十分な場合があります。筆者はこの課題を解決するため、APIコール時に**GETメソッド**以外を物理的に遮断し、さらに「create」や「edit」といった名称を含むツールの登録自体を禁止する厳格な設計を採用しました。

機能面では、頻繁に参照する特定のプロジェクトを固定できる**デフォルトプロジェクト機能**や、ワークスペースごとに設定を切り替えられる**環境変数**および`.backlog-mcp.env`のサポートが実装されています。これにより、**Cursor**や**Cline**、**kiro**などのツールから機密性の高いタスク情報を取得する際の利便性と安全性が向上しています。また、開発にはAIエージェントツールの**kiro**や**GitHub Copilot**のレビュー機能を活用しており、モダンなAI駆動開発の実践例としても参考になります。**Backlog**を社内基盤として利用しつつ、安全かつ迅速にAIエージェントをワークフローに組み込みたい開発者に最適な内容です。