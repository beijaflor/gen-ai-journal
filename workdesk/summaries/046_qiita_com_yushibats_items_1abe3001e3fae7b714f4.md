## 【Select AI Agent】Oracle DBの中だけでReAct型AIエージェントを動かしてみた -NL2SQL×RAG-

https://qiita.com/yushibats/items/1abe3001e3fae7b714f4

Oracle AI Database 26aiの「Select AI Agent」機能が、外部フレームワークなしでOracle DB内部にReAct型AIエージェントを構築・実行可能にしたことを実演します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Oracle Database, AI Agent, ReActパターン, NL2SQL, RAG]]

本記事は、Oracle AI Database 26aiで発表された新機能「Select AI Agent」について、その詳細と実践的な利用方法を解説しています。Select AI Agentは、Autonomous AI Databaseの内部だけでReAct（Reasoning + Acting）型のエージェントを動作させられる画期的な仕組みであり、外部サーバーやフレームワークを必要とせず、データベース単体で自律エージェントを動かせる点が、Webアプリケーションエンジニアにとっての大きなメリットです。

著者は、このエージェントが「思考」と「行動」を交互に繰り返すReActパターンを採用していることを強調しています。Select AI Agentは、RAG（Retrieval-Augmented Generation）、自然言語からSQLを生成するNL2SQL、独自のPL/SQL処理、そしてWeb検索などを「ツール」として呼び出し、多岐にわたるタスクを実行可能です。エージェントのワークフローは、Agent Team、Agent、Task、Toolという4つのコンポーネントで定義され、特にAgent Teamは複数のエージェントを連携させ、共通の文脈を共有しながら複雑な処理を安定して完了させます。

具体的なユースケースとして、売上データ（構造化データ）と商品カタログPDF（非構造化データ）を組み合わせたデータ分析を実演。NL2SQLでデータベースの注文・商品データを検索するエージェントと、RAGで商品カタログPDFを検索するエージェントをAgent Teamとして連携させることで、自然言語による複合的な質問（例：「いつ・どの製品が・どんな特徴で売れているのか？」）に対し、両方のデータソースを参照しながら回答を生成できることを示しました。

特筆すべきは、エージェントの内部動作をログ（`USER_AI_AGENT_TOOL_HISTORY`ビュー）で確認できる点です。これにより、エージェントがどのような判断を下し、どのツールをどのように利用したかを追跡し、必要に応じてプロンプトを改善するためのヒントを得られると著者は指摘しています。

著者は、PL/SQLのみでAgent/Task/Tool/Teamが定義でき、外部アプリケーションなしでReActの多段推論が動くことの強力さを高く評価しており、その実装のシンプルさと体感的な使いやすさは想像以上だと結論づけています。今後、より複雑なユースケースでの活用や、エージェント連携・プロンプト設計の工夫への期待が述べられています。