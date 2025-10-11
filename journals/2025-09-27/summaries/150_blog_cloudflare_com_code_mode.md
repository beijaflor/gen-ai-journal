## Code Mode: the better way to use MCP

https://blog.cloudflare.com/code-mode/

Cloudflareは、AIエージェントがModel Context Protocol (MCP) ツールを直接呼び出す代わりにTypeScriptコードを生成して実行する「Code Mode」を導入し、エージェントのツール利用能力とセキュリティを大幅に向上させます。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:5/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 98/100 | **Annex Potential**: 97/100 | **Overall**: 96/100

**Topics**: [[AIエージェント, ツール呼び出し, Model Context Protocol (MCP), Cloudflare Workers, TypeScriptコード実行]]

Cloudflareは、AIエージェントが外部ツールと連携する際の新たなアプローチ「Code Mode」を発表しました。これまでのAIエージェントは、MCP（Model Context Protocol）のようなツールを「関数呼び出し」の特殊トークンを通じて直接利用していましたが、この方式には限界がありました。LLMはツール呼び出しのために作成された合成データでしか学習しておらず、大量の複雑なツールを扱うことや、複数のツール呼び出しを効率的に連結することが困難で、トークン消費も無駄が多いという課題があったのです。

Code Modeは、この課題を解決するため、LLMがMCPツールを直接呼び出すのではなく、そのツールをTypeScript APIに変換し、LLM自身にこのAPIを呼び出すTypeScriptコードを生成・実行させるという画期的な手法を提案しています。LLMは大量の現実世界のコードで学習しているため、人工的に作られたツール呼び出しよりも、自然なコード生成の方がはるかに得意です。これにより、エージェントはより多くの、より複雑なツールを正確に使いこなし、複数の操作を効率的に連結できるようになります。

この生成されたコードは、Cloudflare WorkersのV8 isolates上でセキュアなサンドボックス環境で実行されます。V8 isolatesはコンテナよりもはるかに軽量で高速に起動するため、エージェントが生成するコードごとに新しい隔離を瞬時に作成・破棄でき、パフォーマンスとコスト効率に優れています。サンドボックスはインターネットから完全に隔離され、MCPサーバーへのアクセスは「binding」を通じてのみ許可されるため、APIキーの漏洩リスクを排除し、厳格なセキュリティを確保します。これは、AIアプリケーションを開発する上で、エージェントの能力を最大限に引き出しつつ、信頼性と安全性を高める上で非常に重要な進歩と言えます。