## 「notebooklm-skill」でClaude CodeからNotebookLMへ直接アクセスできるようになったので試してみた

https://qiita.com/mamoru-ngy/items/a73607a1a0392b5d2c6c

「notebooklm-skill」は、Claude CodeからNotebookLMに直接アクセスすることを可能にし、アップロードされた資料のみを根拠に回答を生成することで、情報の正確性と鮮度を確保する新しい連携方法を紹介します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[LLM, Claude Code, NotebookLM, RAG, AI連携ツール]]

この記事では、Claude Code（CLI版）からGoogleのNotebookLMへ直接アクセスを可能にする「notebooklm-skill」について、その設定方法と活用例を具体的に解説しています。Webアプリケーション開発者にとって、AIモデルの回答の正確性を高めることは重要な課題であり、このスキルはClaudeがNotebookLMにアップロードされた資料のみを参照して回答することで、誤情報や古い情報の生成を防ぐという点で非常に実用的な価値を提供します。

著者はまず、Claude CodeとNotebookLMを連携させるための事前準備（Claude Code Pro/Max、Googleアカウント、Chromeブラウザ）と、スキルをセットアップする手順を詳細に示しています。`git clone`でリポジトリを導入し、スキルがClaudeに認識されていることを確認するプロセスは、既存のClaude Codeユーザーであれば容易に試せるでしょう。

デモでは、NotebookLMにアップロードした10月の東京と大阪の天気情報をもとに、「10月の東京と大阪の天気の違いを日本語で教えて」という質問をClaudeに行い、Claudeが正確に資料内のデータのみを根拠に回答を生成する様子が示されています。さらに、資料に含まれていない「10月の名古屋の天気」を尋ねた際には、「NotebookLMに登録されている資料には、名古屋の天気データは含まれていませんでした」と明確に回答し、情報源に基づかない推測をしないことが確認されました。

著者はこの連携機能について、議事録や企画書といった社内資料をアップロードすることで、比較分析や新しい提案の自動生成を簡単に行える点が便利だと結論付けています。これにより、開発者は特定のプロジェクトやドメインに特化した情報をClaudeに参照させ、より精度の高いインサイトやコード生成に活用できるため、日々の開発ワークフローにおけるAIの活用範囲が大きく広がることが期待されます。