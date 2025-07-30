## AWS発のエージェント型IDE"Kiro"の速報レベルのメモ

https://zenn.dev/watany/articles/d6b948e05a4db1

AWSがエージェント型IDE「Kiro」を発表し、Spec-Driven Development（SDD）を通じて開発プロセスを効率化する新たなアプローチを提示しました。

[[エージェント型IDE, Spec-Driven Development, Vibeモード, Model Context Protocol, Claude 4.0 Sonnet]]

AWSから非公式ながらもエージェント型IDE「Kiro」が登場しました。これはCode OSSをベースとし、Spec-Driven Development（SDD）を提唱することで、プロトタイプから本番環境への開発を効率化することを目指しています。Kiroは、エージェントの自律性を調整する「Vibe」モードと「Spec」モードを備え、Model Context Protocol（MCP）を介して専門サーバーと連携します。現在、Claude 4.0 Sonnetなどのモデルを利用し、「Autopilot」機能や、MarkdownファイルでAIにプロジェクト固有のコンテキストを与える「Steering」機能を提供しています。ベータ版は無料で利用可能ですが、将来的には月間インタラクション数に応じた課金が予定されており、機密情報を扱うビジネス利用にはAmazon Q Developer Pro契約が必要です。

**編集者ノート**: エージェント型IDEの登場は、開発ワークフローに大きな変革をもたらす可能性を秘めています。特にKiroが提唱するSDDは、仕様記述からコード生成、テストまでを一貫してAIが支援することで、開発者の負担を大幅に軽減し、生産性を飛躍的に向上させるでしょう。VibeモードやSteering機能のように、AIの自律性と人間の制御のバランスを細かく調整できる点は、実際の開発現場での導入を促進する鍵となります。将来的には、このようなエージェント型IDEが、単なるコード生成ツールに留まらず、プロジェクト管理やデプロイメントまでを統合的に支援する「開発OS」のような存在になることを予測します。これにより、Webアプリケーション開発者は、より本質的な設計やアーキテクチャに集中できるようになるでしょう。