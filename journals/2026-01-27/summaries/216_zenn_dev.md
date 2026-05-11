## 【個人開発】Claude Codeに83%のコードを書かせる「ドキュメント駆動開発」の全貌【Flutter向けCLAUDE.md公開】

https://zenn.dev/furunag/articles/claude-code-document-driven-development

**Claude Code**の生成精度を極限まで高めるため、AIの文脈理解を制御する「ドキュメント駆動開発」の具体的なディレクトリ構造と**CLAUDE.md**のテンプレートを提示する。

**Content Type**: 🛠️ Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 84/100 | **Overall**: 88/100

**Topics**: [[Claude Code, Flutter, ドキュメント駆動開発, CLAUDE.md, AI開発フロー]]

Flutterアプリ開発において、全コミットの83%を**Claude Code**に生成させた実践的な「ドキュメント駆動開発」の手法を詳説している。AIにコードを書かせる前段階として、最初の3日間で24種類のドキュメントを徹底的に整備することで、AIの「推測」を排除し「確信」に基づく実装を引き出すアプローチが核となる。

技術的なポイントとして、プロジェクトの指針を定義する**CLAUDE.md**を詳細情報のポインタとして運用し、AIに思考の順序を強制する番号付きディレクトリ構造（`10_product`、`30_technical`等）の採用、および情報の矛盾を防ぐための**SSOT（信頼できる唯一の情報源）**のルール化が挙げられる。また、「曖昧な点は必ず質問せよ」という一文をプロンプトに含めることでAIの思考解像度を向上させるテクニックや、**Conventional Commits**に基づいた細粒度なGit運用など、AIとの協調開発における具体的なベストプラクティスが網羅されている。

AIコーディングツールの出力精度に悩む開発者や、**Flutter**での実用的なAI開発フローを構築したいエンジニアにとって、即座に適用可能な「地図」となる内容だ。