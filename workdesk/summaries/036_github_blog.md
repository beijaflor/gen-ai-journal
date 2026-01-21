## AIの出力を向上させる「コンテキスト・エンジニアリング」の活用法

https://github.blog/ai-and-ml/generative-ai/want-better-ai-outputs-try-context-engineering/

**Original Title**: Want better AI outputs? Try context engineering.

GitHub Copilotの精度を最大化するため、単なるプロンプト調整を超えた「コンテキスト・エンジニアリング」の3つの実践的手法を提示する。

**Content Type**: 📖 Tutorial & Guide
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 98/100 | **Annex Potential**: 94/100 | **Overall**: 80/100

**Topics**: [[GitHub Copilot, Context Engineering, Custom Instructions, AI Agents, SDLC]]

GitHub Copilotをより強力なツールへと進化させる鍵は、適切な情報を適切な形式でLLMに提供する「コンテキスト・エンジニアリング」にある。著者は、従来の「プロンプト・エンジニアリング（言葉の言い回し）」から脱却し、開発環境の構造そのものにコンテキストを組み込むことの重要性を強調している。

本記事では、GitHub Copilotにおいて開発者が今すぐ実践できる3つの具体的な手法が解説されている。

1. **カスタム指示（Custom Instructions）**: `.github/copilot-instructions.md` などの設定ファイルをリポジトリに配置することで、コーディング規約、命名規則、ドキュメントスタイル、エラーハンドリングの指針をCopilotに自動的に適用させる。これにより、チーム全体の標準に沿ったコード生成が可能になる。
2. **再利用可能なプロンプト（Reusable Prompts）**: 頻繁に行うコードレビュー、コンポーネントの雛形作成、テスト生成などを `.github/prompts/*.prompts.md` として定義し、スラッシュコマンドから即座に呼び出せるようにする。これにより、反復的なワークフローの効率化と一貫性の確保を実現する。
3. **カスタムエージェント（Custom Agents）**: API設計、セキュリティ解析、ドキュメント作成など、特定の役割に特化したAIペルソナを作成する。エージェントには独自のツールや制約、振る舞いを定義でき、複雑なワークフローではエージェント間でのタスクの引き継ぎも可能になる。

筆者によれば、これらの手法が重要な理由は、単に「より良い出力」を得るためだけではなく、AIに開発者の意図やプロジェクトのアーキテクチャを深く「理解」させるためである。適切なコンテキストを提供することで、推論の精度が向上し、AIとの無駄なやり取り（Back-and-forth）を減らすことができる。結果として、開発者は生成されたコードの修正に時間を取られることなく、本来の「フロー状態」を維持したまま開発に集中できるようになると主張している。Webエンジニアにとって、これらの仕組みをリポジトリ内に標準化して組み込むことは、チームの生産性を底上げするための必須のプラクティスとなるだろう。