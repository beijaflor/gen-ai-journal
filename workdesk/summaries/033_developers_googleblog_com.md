## Universal Commerce Protocol (UCP) の技術詳解：次世代「エージェンティック・コマース」の標準規格

https://developers.googleblog.com/under-the-hood-universal-commerce-protocol-ucp/

**Original Title**: Under the Hood: Universal Commerce Protocol (UCP)

AIエージェントによる自律的な購買体験を実現するため、GoogleがShopifyやWalmart等の業界リーダーと共同開発したオープンソースの標準プロトコル「UCP」を導入する。

**Content Type**: 🛠️ Technical Reference
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 75/100 | **Overall**: 88/100

**Topics**: [[Agentic Commerce, UCP, Model Context Protocol, AI Agents, Interoperability]]

Googleは、AIエージェントがユーザーに代わって商品を探索・意思決定・購入まで完結させる「エージェンティック・コマース」を加速させるためのオープンソース標準、Universal Commerce Protocol（UCP）を発表した。このプロトコルは、Shopify、Etsy、Target、Walmartといった主要な小売業者や、Visa、Mastercard、Stripeなどの決済プロバイダーを含む20社以上のグローバルパートナーと共同で策定されたものである。

著者は、現在のEコマースにおける最大の課題として「N対Nの統合ボトルネック」を挙げている。現在、ビジネス側が新しいAIインターフェースに対応しようとするたびに、個別の統合コードを記述する必要があり、これがエコシステムの進化を妨げているという。UCPはこの複雑さを解消するため、発見（Discovery）から決済、注文管理に至るまでの全工程を単一の抽象化レイヤーで標準化する。

技術的な構成要素として、UCPは以下の3つの柱で成り立っている：
1. **共通言語とプリミティブ**: 商品検索、カート操作、チェックアウト、割引適用といったコマースの基本機能を「Capability」として定義し、JSONスキーマで標準化している。
2. **動的ディスカバリ**: ビジネス側は `/.well-known/ucp` パスにマニフェストファイルを配置することで、エージェントに対して動的に自社の機能や支払いオプションを公開できる。
3. **拡張可能なアーキテクチャ**: Model Context Protocol (MCP) や Agent Payments Protocol (AP2) と互換性を持ち、REST APIだけでなく、エージェント間（A2A）の直接通信もサポートする。

特に注目すべきは決済アーキテクチャだ。UCPは支払い手段（カード情報等）と決済ハンドラー（プロバイダー）を分離して定義しており、トークン化された決済と検証可能な資格情報を組み合わせることで、すべての認可に対してユーザーの同意を暗号化証明として付与する。これにより、エージェントによる代理決済の安全性を担保している。

GoogleはすでにSearchのAIモードやGeminiにおいて、Google Payを活用したUCPの参照実装を開始している。Webアプリケーションエンジニアにとって、UCPの採用は「特定のAIプラットフォームへの依存を避けつつ、あらゆるAIエージェント経由のトラフィックを受け入れる」ための戦略的な一歩となる。著者は、このオープンな標準化こそが、摩擦のない次世代のショッピング体験を実現する鍵であると主張している。開発者向けにはPython SDKとサンプル実装が公開されており、すぐにプロトコルの動作を検証することが可能だ。