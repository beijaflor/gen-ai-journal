## PleasanterをCursorのBrowser機能で分析する（MCPサーバはうまく使えず。。。）

https://qiita.com/t_narita/items/bdeb84347ffc5c789a16

著者は、Pleasanterのデータ分析において、当初計画したMCPサーバーの代わりにCursorのBrowser機能が極めて有効であることを示した。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 71/100 | **Annex Potential**: 70/100 | **Overall**: 72/100

**Topics**: [[Pleasanter, Cursor, IDE, AIアシスタント, データ分析]]

著者は、普段の開発に利用しているAI搭載IDEのCursorを使い、ノーコード・ローコード開発ツール「Pleasanter」のデータ分析を試みました。当初、PleasanterのMCP（Microservice Communication Protocol）機能を利用し、公開されている`pleasanter-mcp-server`をCursorに連携させることで、効率的なデータアクセスと分析が可能になると期待していました。

しかし、実際に`pleasanter-mcp-server`をセットアップし、Cursorからアクセスを試みたところ、MCPサーバー自体への接続は成功したものの、肝心のPleasanterからのデータ取得がうまくいかないという問題に直面しました。Cursorに直接リンクを貼って質問しても、意図した値は取得できませんでした。

この課題に対し、著者はCursor IDEに内蔵されているBrowser機能を代替手段として利用することを考案しました。Pleasanterのクラウド版環境で用意したテストデータに対し、Browser機能を通じてPleasanterのサイトURLを直接入力し、「サイトIDを調べて」と質問したところ、Cursorは記載された内容を正確に理解し、遅延しているタスクなどのデータを問題なく取得・分析できることが判明しました。この結果から、MCPサーバーを経由せずとも、CursorのBrowser機能だけでPleasanterのデータに対して効果的な分析が可能であることが実証されました。

この発見は、ウェブアプリケーションエンジニアにとって重要な示唆を与えます。専用のサーバー連携機能が期待通りに動作しない場合でも、AI搭載型IDEのBrowser機能が既存のウェブサービスとのシームレスな連携とデータ分析を可能にする強力な代替手段となりうることを示しています。ただし、Browser機能を使うにはCursorがPleasanterにログインできる必要があるため、初回アクセス時にログイン情報の入力が必要となる点には注意が必要です。著者は、手軽かつ高精度なデータ分析がIDE内で完結できるメリットは大きく、開発ワークフローの効率化に貢献すると強調しています。