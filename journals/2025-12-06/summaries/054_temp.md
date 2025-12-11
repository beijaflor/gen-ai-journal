## AI時代の「Embedded Documentation」のススメ

https://nealle-dev.hatenablog.com/entry/2025/12/01/090000

ニーリーの古庄氏が、AI時代における開発ドキュメント管理の課題に対し、コード内にMermaid図を直接埋め込む「Embedded Documentation」の概念と、その実践を支援する自作VS Code拡張機能「mermaid-comment-viewer」を提案します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Embedded Documentation, VS Code Extension, Mermaid, AI in Documentation, Literate Programming]]

本記事は、AI時代における開発現場のドキュメント管理の課題に対し、「Embedded Documentation」という新しいアプローチを提案しています。著者は「Code is the executable design document（コードこそが動く設計書である）」という原則に基づき、コードと重複する自然言語でのドキュメント作成が、メンテナンスコスト増大や情報の不整合を招くと指摘します。

このアプローチでは、情報の管理場所を「Why & What」（なぜ作るのか、ビジネスルールは何か）と「How」（具体的な処理フロー、クラス構造）に明確に分離します。「Why & What」はNotionやConfluenceといったコラボレーションツールでPMやデザイナーとの合意形成の共通言語として管理し、「How」はコードそのものの中に集約すべきだと主張します。具体的には、関数のDocstring内にMermaid記法でフロー図を直接埋め込むことで、コード（詳細）と図（全体像）を物理的に最も近い場所に共存させ、コードをSSOT（Single Source of Truth）とします。これはかつての「文芸的プログラミング」の現代的な再評価と位置づけられています。

しかし、このスタイルを実践する上で、VS Code上でコード内のMermaid図を快適に閲覧する手段が少ないという課題がありました。そこで著者は、この課題を解決するために自作のVS Code拡張機能「mermaid-comment-viewer」を開発しました。この拡張機能は以下の特徴を持ちます。

*   **分離されたWebview Panel**: コードエディタを汚さず、サイドパネルにMermaid図を独立して表示。カーソル位置やアクティブなファイルに基づいて、該当するMermaidブロックをリアルタイムで抽出し、コードを読み進めながら全体像を確認できるUXを実現します。
*   **オフライン対応**: 拡張機能内に`mermaid.min.js`をバンドルしているため、インターネット環境がない場所でも図の表示が可能です。
*   **柔軟なパースロジック**: TypeScriptの`/** ... */`やPythonの`""" ... """`など、多様なコメント構文からMermaid記法を正確に特定します。

さらに、著者はこのアプローチの未来として、AIとMCP（Model Context Protocol）の活用を展望しています。AIがMCP経由でConfluenceのPRD（Why）を読み込み、その背景を理解した上でコードとDocstring内のMermaid図（How）を自律的に更新するワークフローを提案。これにより、エンジニアはHowの可視化作業そのものをAIに委譲し、「設計の正しさの検証」というより本質的な業務に集中できるようになると述べています。

この「Embedded Documentation」と「mermaid-comment-viewer」は、ドキュメント管理の負担を軽減し、エンジニアがより価値の高い業務に注力するための実践的な解決策として、Webアプリケーションエンジニアにとって非常に価値のある提案です。