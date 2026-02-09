## OpenClaw：AIエージェントに全システム権限を与えるべきか？革命かセキュリティの悪夢か

https://innfactory.ai/en/blog/openclaw-ai-agent-security/

**Original Title**: OpenClaw: When AI Agents Get Full System Access – Revolution or Security Nightmare?

詳述する：フルシステムアクセスを持つAIエージェント「OpenClaw」の利便性と、プロンプトインジェクションによる壊滅的なセキュリティリスク、および必須のサンドボックス対策を解説する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 82/100 | **Annex Potential**: 76/100 | **Overall**: 84/100

**Topics**: [[OpenClaw, AIエージェント, セキュリティ, MCP (Model Context Protocol), サンドボックス]]

**OpenClaw**（旧Moltbot）は、個人のPCに対してフル制御権限を持つオープンソースのAIエージェントです。WhatsAppやSlackなどのチャットUIを通じて、ファイルシステム、ブラウザ、ターミナルを操作でき、**Model Context Protocol (MCP)** を介した100種類以上のツール連携や、エージェント自身が新しいスキルを学習する自己拡張機能を備えています。しかし、筆者はこの利便性の裏にある「全システムアクセス」が、現在のAI技術では極めて危険な「セキュリティの悪夢」になり得ると警告しています。

最大のリスクとして挙げられているのが、根本的な解決策のない**プロンプトインジェクション**です。悪意ある指示が埋め込まれたメールをエージェントが読み取ると、ユーザーに気づかれずにパスワードファイルを窃取したり、外部へデータを送信したりする攻撃が成立します。これを防ぐため、筆者は**UTM**や**VirtualBox**による**完全な仮想マシン (VM)**、あるいはネットワークとボリュームを厳格に分離した**Docker**コンテナでの**サンドボックス化**を強く推奨しています。特権の最小化（**Least Privilege**）や、書き込み・実行アクションに対する人間による承認プロセスの導入が不可欠です。

AIエージェントをローカル環境や業務ワークフローに統合しようと考えているエンジニアや、エージェント開発におけるセキュリティ設計を学びたい開発者に最適です。