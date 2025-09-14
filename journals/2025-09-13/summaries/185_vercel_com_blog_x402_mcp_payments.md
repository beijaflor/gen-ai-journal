## Introducing x402-mcp: Open protocol payments for MCP tools

https://vercel.com/blog/introducing-x402-mcp-open-protocol-payments-for-mcp-tools

Vercelは、AIエージェントが外部サービス利用料を自律的に支払うためのオープンプロトコル「x402」と、Model Context Protocol (MCP)およびVercel AI SDKへの統合「x402-mcp」を発表し、プログラム可能な決済をHTTPリクエストに直接組み込みます。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[AI Agent Payments, HTTP 402 Protocol, Vercel AI SDK, Model Context Protocol (MCP), Programmatic Payments]]

AIエージェントの能力向上に伴い、有料の外部サービス利用時の決済は大きな課題でした。従来のモデルでは、APIごとにアカウント登録、APIキー管理、個別の請求関係が必要で、エージェントが自律的に新しいサービスを発見・利用する際の障壁となっていました。

Vercelが発表したオープンプロトコル「x402」は、この課題に対し、HTTPリクエスト自体に支払い機能を直接組み込むことで解決策を提示します。これはHTTPの402 Payment Requiredステータスコードを利用し、事前の口座開設なしにAPIが直接支払い要求を行えるようにするものです。この「x402」プロトコルは、Model Context Protocol (MCP)サーバーとVercel AI SDKに「x402-mcp」として統合されました。

Webアプリケーションエンジニアにとって重要なのは、その実用性です。`x402-next`の`paymentMiddleware`を導入するだけで、APIルートを簡単に有料化できます。クライアント側では`x402-fetch`のラッパーを使うことで、支払いプロセスが抽象化され、複雑な決済ロジックを意識せずAPIを呼び出せるようになります。MCPツールにおいても、`createPaidMcpHandler`で有料ツールを定義し、クライアント側で`withPayment`ラッパーを使うだけで、エージェントがツール利用料を自動的に支払えるようになります。

この仕組みは、クライアントが保護されたリソースを要求し、サーバーが402ステータスと支払い指示を返すことで機能します。クライアントは支払い認証情報をヘッダーに含めてリクエストを再試行し、サーバーは外部の決済ファシリテーターを通じて支払いを検証・処理します。現時点ではBaseブロックチェーン上のUSDCによるワンタイム支払いが主流ですが、プロトコル自体は多様な決済ネットワークに対応可能です。

このプロトコルの登場は、AIエージェントの自律的なエコシステム構築を加速させます。開発者は、APIやツールの利用料徴収・支払いの仕組みをシンプルに実装できるため、AI駆動型アプリケーションのマネタイズや、エージェント間連携の可能性を広げることが期待されます。Vercel AI Starterテンプレートを使えば、Next.jsやAI SDKと連携したx402の活用例をすぐに試せ、AI開発における新たな標準となる可能性を秘めています。