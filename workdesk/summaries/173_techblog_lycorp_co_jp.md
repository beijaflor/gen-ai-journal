## Claude Code × MCPで実現するPRレビュー準備の自動化 ——週6時間のレビュー工数を削減した実践例——

https://techblog.lycorp.co.jp/ja/20260122a

**Claude Code**と**MCP**を連携させ、PRの背景情報を外部ドキュメントから自動集約することでレビュー準備工数を劇的に削減する手法を提示する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Claude Code, MCP, コードレビュー, NotebookLM, ワークフロー自動化]]

大規模なレガシーコードや複雑なSQLを抱えるプロジェクトにおいて、**Claude Code**と**MCP (Model Context Protocol)**を中核に据えた「AIレビュー準備」の自動化事例を紹介しています。育休復帰後のエンジニアが直面した仕様理解のボトルネックを解消するため、PRのURLから関連情報を自動収集する仕組みを構築した経緯を詳述しています。

技術構成として、**GitHub MCP**や**GitHub CLI**でPR情報を取得し、さらに**Jira**や**Confluence**のリンクを辿って設計情報を自動で集約します。AIはこれらを元に、**ERD**やシーケンス図、**Must/Should Fix**といった観点を含む「解説ドキュメント」をMarkdown形式で生成します。このワークフローにより、レビュー前の準備時間を1件あたり30分、週換算で約6時間削減することに成功しました。また、**NotebookLM**にドキュメントを読み込ませ、チャット形式でドメイン知識を補完する補助的な手法も併用しています。

大規模プロジェクトのキャッチアップに苦慮しているエンジニアや、限られた時間の中でレビューの「深さ」と「幅」を向上させたいチームリーダーにとって、非常に再現性の高い実践例となっています。