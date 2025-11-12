## Apps SDKでシンプルなChatGPTアプリを作る

https://zenn.dev/himara2/articles/ae362b516e9e52

OpenAIのApps SDKとMCPサーバー、microCMSを活用し、リッチなUIを持つChatGPTアプリを開発する具体的な手順を解説する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 79/100 | **Overall**: 80/100

**Topics**: [[ChatGPT Apps SDK, Model Context Protocol (MCP), React, microCMS, AIアプリケーション開発]]

著者は、OpenAIのApps SDKを利用して、ChatGPT上でリッチなUIを持つアプリケーションを開発する具体的な手順を解説しています。これは、ユーザーとの会話内容に応じてChatGPTが最適なアプリを判断・推薦し、テキストベースの応答だけでなく、より視覚的でインタラクティブな情報提示を可能にする仕組みです。

記事では、「Z Coffee」というカフェの店舗情報を表示するサンプルアプリを例に、その実装方法を順を追って説明します。まず、店舗データの管理にはヘッドレスCMSであるmicroCMSを活用し、API経由でデータを取得できる形式で準備します。

次に、Model Context Protocol（MCP）サーバーをTypeScript SDKとHonoフレームワークを使って実装します。ここでは、microCMSから店舗情報を取得し、ユーザーの入力（例：住所）に応じて絞り込みを行う`store-list`というツールを登録します。このMCPサーバーがChatGPTとUIの間でデータのやり取りを仲介します。

UI部分は、ReactとTailwind CSSを用いて構築されます。`useOpenAiGlobal`フックを使ってChatGPT環境から渡されるツール出力（`toolOutput`）を取得し、これに基づいて店舗情報をカード形式で表示するコンポーネントを作成します。これにより、従来のChatGPTのテキスト応答では難しかった、画像や整形されたリストを含むリッチなユーザー体験を提供します。

最後に、MCPサーバーにビルドされたUI（HTML、CSS、JavaScript）をリソースとして登録し、ローカルサーバーをngrokで公開することで、開発中のアプリを実際にChatGPTから呼び出す方法を詳述します。ChatGPTの開発者モードを有効にし、ngrokで取得したURLを設定することで、「Z Coffee Store の店舗一覧を教えて」といったプロンプトに応じて、美しいUIで店舗情報が表示される様子を実演しています。

著者は、Apps SDKがまだプレビュー版でありながらも、既存のWeb開発スキル（React, TypeScriptなど）を活かしてインタラクティブなAIアプリケーションを構築できる点に大きな価値があると考えています。2025年後半には審査受付と収益化モデルのアナウンスが予定されており、今後の動向を注視していくべきであると結んでいます。この技術は、AIとの対話体験を根本から変え、開発者に新たな表現の場をもたらす可能性を秘めていると示唆されています。