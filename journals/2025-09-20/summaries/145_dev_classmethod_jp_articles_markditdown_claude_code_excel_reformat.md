## MarkItDownとClaude Codeを使ってExcel方眼紙をリフォーマットしてみた

https://dev.classmethod.jp/articles/markditdown-claude-code-excel-reformat/

MarkItDownとClaude Codeのカスタムスラッシュコマンドを連携させ、AI活用が困難な「Excel方眼紙」を効率的かつ正確に読みやすいMarkdown形式へリフォーマットする手順を紹介します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:5/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 90/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Excel方眼紙, MarkItDown, Claude Code, LLMプロンプトエンジニアリング, データ整形・変換]]

日本企業や官公庁で広く使われる「Excel方眼紙」は、複雑な設計書や仕様書の作成に便利ですが、AIツールでの構造化データとしての活用には大きな課題がありました。MarkItDownで一度Markdownに変換しても、結合セルや空セルの多さから`NaN`や`Unnamed`の大量発生により、人間にもAIにも読みづらく、コンテキストサイズも無駄に増大するという問題が生じます。

この記事では、この課題を解決するため、MarkItDownと独自開発したClaude Codeのカスタムスラッシュコマンドを組み合わせた画期的なリフォーマット手法を提案しています。ワークフローは3つのステップで構成されます。まず、MarkItDownでExcelを荒いMarkdownに変換します。次に`/excel-md:prepare`コマンドがそのMarkdownを詳細に分析し、シート構造、不要な`NaN`や`Unnamed`の分布を特定。この分析に基づき、Claude Codeが各シートを独立したタスクとして並列処理するための厳密なプロンプトを自動生成します。このプロンプトは、元データの厳格な保持とコンテキストウィンドウ制限への対応を重視しています。最後に`/excel-md:transform`コマンドが、このプロンプトに従い、各シートから`NaN`や`Unnamed`を効率的に除去し、可読性の高いクリーンなMarkdownファイルとして個別に整形。最終的に`/excel-md:merge`コマンドでこれらを統合し、AIが処理しやすい統一されたドキュメントを生成します。

この手法は、従来のAIでは扱いにくかったExcel方眼紙の情報を、効率的かつ正確に構造化されたテキストデータへと変換することを可能にします。これにより、開発者は設計書や仕様書といったレガシー文書から、AIによる要約、コード生成、ドキュメント化などの高度なAI活用ワークフローを容易に構築できるようになり、開発効率の大幅な向上が期待されます。提供されているスラッシュコマンドはGitHubで公開されており、実際の開発現場での活用を促進します。