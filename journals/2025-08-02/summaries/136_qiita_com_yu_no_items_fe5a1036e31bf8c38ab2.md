## Strands Agents を使って AWS Pricing MCP サーバーを触ってみた話 #JapanAWSJr.Champions

https://qiita.com/Yu_NO/items/fe5a1036e31bf8c38ab2

Strands AgentsとAWS Pricing MCPサーバーを連携させ、自然言語でAWS料金を問い合わせるAIアシスタント構築の実験的な試みを紹介する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:3/5 | Depth:3/5 | Unique:3/5 | Practical:3/5 | Anti-Hype:3/5
**Main Journal**: 84/100 | **Annex Potential**: 81/100 | **Overall**: 60/100

**Topics**: [[Strands Agents, AWS Pricing MCP Server, マルチエージェントAI, AWS料金問い合わせ, CLIツール連携]]

「Strands Agents を使って AWS Pricing MCP サーバーを触ってみた話」は、開発者が日常業務で直面するAWS料金確認の課題に対し、AIエージェントを用いた革新的な解決策を提示します。この記事は、AWSが提供するマルチエージェントAIアプリケーション構築用SDK「Strands Agents」と、自然言語でAWS料金情報に問い合わせできる「AWS Pricing MCPサーバー」を連携させる具体的な手法を解説します。

なぜこれが重要かというと、Webアプリケーションエンジニアにとって、AWS料金は常に変動し、詳細な情報は複雑なAPIドキュメントやコンソール操作を必要とします。本記事で示されるアプローチは、AIエージェントがユーザーの自然言語による質問（例：「バージニア北部で t3.micro の料金はいくらですか？」）を理解し、直接MCPサーバーに問い合わせて、オンデマンド料金やリザーブドインスタンス料金といった正確な情報を即座に返答することを可能にします。これにより、開発者は時間と手間を大幅に削減し、より本質的な開発タスクに集中できるようになります。

具体的な実装では、PythonとStrands Agents SDKを使用し、`uvx`コマンドでAWS Pricing MCPサーバーを呼び出す方法や、Anthropic Claude-3.5 Sonnetをモデルとして利用したエージェントの定義が示されています。特に、MCPサーバーへの認証情報（AWSアクセスキーなど）の渡し方でハマったポイントとその解決策（`StdioServerParameters`の`env`引数を使用）は、同様のシステム構築を試みる開発者にとって非常に価値のある情報です。

この事例は、単に料金を問い合わせるだけでなく、AIエージェントが複雑なクラウドサービスAPIと自然言語のギャップを埋める強力なツールとなる可能性を示唆しています。将来的には、このようなエージェントが、インフラ管理、リソース最適化、デバッグ支援など、多様な開発・運用タスクを自然言語で実行できるようになるでしょう。これは、開発ワークフローのパラダイムシフトを予感させる一歩です。