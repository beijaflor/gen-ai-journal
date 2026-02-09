## AI-DLC(Kiroとawslabs/aidlc-workflows)でAI駆動開発をやってみる #AWS

https://qiita.com/tjotjo/items/83931ded621f0a52235a

AWSが提唱するAIネイティブな開発手法「**AI-DLC**」を検証し、人間が主導権を握る開発プロセスの標準化とチーム開発における実効性を評価する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 98/100 | **Annex Potential**: 99/100 | **Overall**: 76/100

**Topics**: [[AI-DLC, Kiro, aidlc-workflows, AWS, AI駆動開発]]

AWSが提唱するAIネイティブなソフトウェア開発方法論**AI-DLC（AI-Driven Development Life Cycle）**を、実装リポジトリである**aidlc-workflows**とAWSのIDE**Kiro**を用いて実践した記録です。AI-DLCはAIをプロセスの中心に据えつつも、重要な意思決定は人間が行う「**Human in the Loop**」を原則としており、Inception（計画）、Construction（構築）、Operation（運用）の3フェーズで構成されます。

記事では、新規プロジェクトの立ち上げからコード生成、テストまでの具体的なステップを解説しています。AIが勝手な推測をせず、Markdown形式のファイルを通じて人間に質問を投げ、選択肢を提示しながら要件を固めていくプロセスが詳述されています。また、進捗を管理する**aidlc-state.md**や全やり取りを記録する**audit.md**の自動生成により、開発の透明性が確保される仕組みも紹介されています。

著者は、チーム開発においてワークフローと成果物（ドキュメント）を標準化できる点を高く評価しており、特に既存コードから仕様を抽出する**リバースエンジニアリング**機能の有用性に言及しています。一方で、人間の判断がボトルネックになる点や、エンジニアの役割変化といった組織的な課題にも触れています。個人のAI利用から組織的な「AI駆動開発」への移行を検討しているエンジニアや、最新のAWS開発エコシステムに関心がある読者に適した内容です。