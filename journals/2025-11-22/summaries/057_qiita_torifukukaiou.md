## 私のKiro CLI(旧Amazon Q Developer CLI)の起動方法を大公開

https://qiita.com/torifukukaiou/items/b23538894e706a000410

Kiro CLI（旧Amazon Q Developer CLI）の起動方法と、AWS MCP Serversを最新情報に対応させる設定、およびサービス統合と料金体系の変遷を解説します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 88/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Kiro CLI, Amazon Q Developer CLI, AWS MCP Servers, CLI Tools, 生成AI料金体系]]

この記事は、かつてAmazon Q Developer CLIとして知られていたKiro CLIの起動方法と、その効果的な利用のための設定を詳細に解説しています。Webアプリケーションエンジニアにとって、生成AIの知識が古くなるという共通の課題に対し、筆者は`~/.kiro/settings/mcp.json`にAWS MCP Serversを設定することで、AWSの最新ドキュメントを参照できるようになり、この問題を解消できると強調しています。これにより、Kiro CLIが常に最新の情報に基づいて応答するようになり、開発者は信頼性の高いAIアシスタントを活用できます。

具体的な起動コマンドとして、`kiro-cli chat --resume --trust-tools`を使用し、AWS関連の様々なツールを信頼して利用する方法が示されています。これは、AIアシスタントの機能を最大限に引き出し、開発ワークフローに深く組み込むための実用的なステップです。

また、記事はKiro CLIの歴史と料金体系についても言及しています。Amazon Q Developer CLIがKiro CLIへと名称変更され、AWSサービス内で統合が進んでいる背景が説明されています。特に重要な点として、かつて「体感使い放題」とされていた旧Amazon Q Developer CLIの利用が、現在は月額19ドルのProプランで「おおよそ1,000回」という上限に制限されていることが明確に指摘されており、料金ページが流動的であることにも注意を促しています。この情報は、コスト意識の高い開発者にとって、AIツールの選定と利用計画において極めて重要です。

筆者は、Kiro CLIがIDE統合版とCLI版の両方を提供する中で、自身はCLI版を愛用していることを述べ、その実用性を強調しています。このツールがAWS開発における情報収集とコーディング支援においてどのように役立つか、具体的な設定と過去の変遷を通じて理解を深めることができます。