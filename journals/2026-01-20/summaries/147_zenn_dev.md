## AI が AWS ダッシュボードを"描く"。A2UI プロトコルで作る動的 AWS Advisor

https://zenn.dev/aws_japan/articles/3753f8eb32cca7

A2AおよびA2UIプロトコルとAWS Strands Agentsを組み合わせ、自然言語クエリから動的にダッシュボードUIを生成する実装手法を提示する。

**Content Type**: 🛠️ Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:5/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 93/100 | **Annex Potential**: 93/100 | **Overall**: 92/100

**Topics**: [[A2UI, A2A, AWS Strands Agents, MCP, 動的ダッシュボード]]

本記事は、Googleが提唱し標準化が進むA2A (Agent-to-Agent) およびA2UI (Agent-to-User Interface) プロトコルを、AWSのAIエージェントフレームワーク「Strands Agents」と組み合わせて活用する実践的なガイドである。著者は、従来のチャット形式のインターフェースでは限界があった「複雑なデータの可視化」や「構造的な操作」を、エージェントが動的にUIを生成・送信することで解決する手法を提案している。マルチエージェントの世界では、エージェントがクライアントのDOMを直接操作できないため、UIを「メッセージ」として安全に伝える標準プロトコルの必要性を説いている。

特筆すべきは、A2UIの設計思想である「Security First」「LLM-Friendly」「Framework-Agnostic」の解説だ。A2UIは実行可能コードではなく、宣言的なJSONデータ（隣接リストモデル）としてUIを定義するため、LLMによる生成が容易であり、かつセキュリティリスクを最小限に抑えつつ、Webやモバイルなどのネイティブコンポーネントにマッピングできる。これにより、エージェントは「今月のコストを円グラフで見せる」といった、データに最適化された表現を能動的に選択可能になる。筆者によれば、これはエージェントが「UIを話す（speak UI）」状態を実現するものだという。

実装面では、Python製のStrands Agentsを用い、ストリーミングレスポンス中にA2UIの定義をキャプチャする「Callback Handler」パターンや、MCP (Model Context Protocol) を介したAWS公式ドキュメントとの連携など、具体的なテクニックが網羅されている。また、GoogleのADK (Agent Development Kit) との比較を通じて、Strandsにおけるツール定義の簡潔さやプロンプト注入の柔軟性といったトレードオフも分析されている。

開発者にとっての重要性は、LLMを単なるテキスト生成器から、動的なダッシュボードや複雑な管理画面を構築する「UIの設計者」へと昇華させる具体的なアーキテクチャが示された点にある。これは、将来的なAIエージェントによるUXの自動生成において、フロントエンドとバックエンド（エージェント）の新しい協調モデルとして極めて示唆に富んでいる。