## Gemini Canvas でも大体の GAS はかけるよーという話

https://zenn.dev/howdy39/articles/1a543b500bb05d

ジェミニキャンバスを活用し、Apple Business ManagerとNotionを連携させるGoogle Apps Scriptを反復的なプロンプトと手動修正で効率的に開発できることを実証します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[Google Apps Script, Gemini Canvas, LLMを用いた開発, API連携, ワークフロー自動化]]

本記事は、GoogleのGemini CanvasがGoogle Apps Script (GAS) の複雑なコード生成にどれほど効果的であるかを示しています。著者は、Apple Business Manager (ABM) のデバイス情報をGoogleスプレッドシートに取得し、それをNotionデータベースに同期するという具体的なユースケースを通じて、その開発プロセスを詳細に解説しています。

重要な点は、AIが生成したコードをスクリプトエディタに貼り付け、必要に応じて手動で修正し、その変更を再びGemini Canvasにフィードバックするという反復的なアプローチです。この「会話型開発」により、アクセストークンの取得、コンテナバインドスクリプトへの修正、APIリクエストのエラー対応、さらにはNotion連携の複雑な処理まで、段階的にコードを完成させていきます。

この手法がウェブアプリケーションエンジニアにとってなぜ重要かというと、Gemini Canvasのような汎用的なLLMツールが、Cursorのような専用AIコーディングエディタがなくとも、実用的なGASアプリケーション開発の強力な支援となることを示しているからです。API連携やデータ変換といった複雑なロジックも、対話を通じて効率的に構築できるため、GAS開発の敷居を大きく下げ、開発効率を向上させます。著者は、自身の10年近いGAS開発経験から、過去に作成したGASアプリケーションのほとんどがこの方法で構築可能だと述べており、LLMを活用した新しい開発パラダイムの可能性を具体的に提示しています。人間とAIが協調し、お互いの強みを活かすことで、複雑な自動化スクリプトも手軽に実装できるという、AI時代の開発ワークフローの典型例と言えるでしょう。