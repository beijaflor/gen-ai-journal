## Zapier × Gemini × Slackで新着記事要約botをつくってみた #個人開発

https://qiita.com/AS_atsushi/items/a369a9720951d66636e3

開発者向けの最新記事情報追跡の負担を軽減するため、Zapier、Gemini、Slackを連携させて新着記事を自動要約し通知するボットの構築手順を解説します。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 82/100 | **Annex Potential**: 78/100 | **Overall**: 80/100

**Topics**: [[Zapier, Gemini API, Slack連携, RSS自動化, LLM活用]]

本記事は、ChatGPTやGeminiといったLLM関連のニュースを追うことの疲弊や、最新情報を迅速にキャッチアップしたいというニーズに応えるため、Zapier、Gemini、Slackを連携させた新着記事要約通知ボットの構築方法をステップバイステップで説明しています。

筆者は、Twitterだけでは情報収集が遅れる可能性があり、常に最新情報へのアクセスが求められる現状を指摘。この課題を解決するため、RSSフィードを利用して記事を即座に取得し、その内容を要約してSlackに通知する仕組みを提案します。

構築手順は以下の通りです。まずZapierでZapを作成し、RSSをトリガーに設定します。「New Item in Feed」を選択し、監視したい記事のRSSフィードURLを入力。これにより、新着記事の情報を自動で取得する基盤ができます。次に、アクションとしてSlackを設定し、「Send Channel Message」で取得したRSS要素（記事タイトル、URLなど）をSlackチャンネルに送信するメッセージを作成します。

さらに、記事の要約機能を追加するため、Zapierのステップの間にGoogle AI Studio（Gemini）を組み込みます。Gemini APIキーを取得し、適切なモデルを選択した上で、「以下の内容を要約して」というプロンプトを指示。Slackへの送信内容を、Geminiによって要約されたテキストに変更することで、新着記事の概要を効率的に把握できる仕組みが完成します。

注意点として、Zapierの無料プランではステップ数が2つまでに制限されること、またGemini APIキーの取得には請求先登録が必要であることが述べられています。著者は、このボットが社内での情報管理やキャッチアップにおいて非常に有用であると強調しています。