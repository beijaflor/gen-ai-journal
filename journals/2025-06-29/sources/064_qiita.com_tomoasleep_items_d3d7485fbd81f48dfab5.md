## [GitHub Copilot Chat で Plan mode を再現する #VSCode](https://qiita.com/tomoasleep/items/d3d7485fbd81f48dfab5?utm_campaign=popular_items&utm_medium=feed&utm_source=popular_items)

**消えたCopilotの便利機能「Plan mode」を蘇らせる、VSCodeカスタム術**

GitHub Copilot Chatのプレビュー版に搭載されていた、実装の段取りを考えてくれる便利な「Plan mode」(`@workspace /plan`)。この機能は公式リリース版では削除されてしまいましたが、この記事ではその代替となるアイデアを紹介しています。

記事で提案されているのは、精巧なプロンプトを自作することでPlan modeの機能を再現する方法です。具体的には、「あなたはプロのエンジニアです。以下の依頼とコンテキストを元に、ステップバイステップで具体的な実装計画を立��てください」といった詳細な指示をCopilotに与えます。このプロンプトには、変更すべきファイルパスや実行すべきコマンドを明記させるなど、具体的なアウトプットを要求する工夫が凝らされています。

さらに、このカスタムプロンプトをVSCodeの`settings.json`に`"github.copilot.chat.participants"`として登録し、`@plan`のような自分専用のコマンドとして呼び出せるようにする方法も解説されています。これにより、かつてのPlan modeのように、手軽に実装計画を生成させることが可能になります。本記事は、失われた機能をただ嘆くのではなく、ツールのカスタマイズによって自分好みの開発環境を構築するための優れたヒントを与えてくれます。