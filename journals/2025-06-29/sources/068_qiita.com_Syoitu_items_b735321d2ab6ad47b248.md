## [Vercelのmcp-adapterはいいぞ!AWSでも使える! #Next.js](https://qiita.com/Syoitu/items/b735321d2ab6ad47b248?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items)

**Vercelのmcp-adapterでMCPサーバーを手軽に構築！AWSでも利用可能**

この記事では、Vercelが提供する`@vercel/mcp-adapter`を利用して、Streamable HTTP対応のMCP（Model-Context-Protocol）サーバーをNext.jsで手軽に構築する方法を紹介しています。

プロジェクトの初期化から、`@vercel/mcp-adapter`と`zod`をインストールし、簡単なAPIルートを作成する手順が解説されています。作成したMCPサーバーは、VSCodeのCopilotやMCP Inspectorから簡単にテストすることが可能です。

さらに、記事では`experimental_withMcpAuth`関数を用いた認証の実装方法や、作成したアプリケーションをVercelおよびAWS Amplifyへデプロイする具体的な手順も紹介されています。特にAWS Amplifyを利用するメリットとして、既存のAWSリソース（ファイアウォールやカスタムドメインなど）と容易に連携できる点が挙げられており、より柔軟なインフラ構成が可能になるとしています。Next.jsを使い慣れた開発者にとって、MCPサーバーの構築とデプロイを迅速に行うための実践的なガイドです。