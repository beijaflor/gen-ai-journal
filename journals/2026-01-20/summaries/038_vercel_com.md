## Streamdown v2: バンドルサイズの軽量化とMarkdown修復のカスタマイズ性を向上

https://vercel.com/changelog/streamdown-v2

**Original Title**: Streamdown v2: Smaller bundle size and new Remend options

AIストリーミングに特化したMarkdownレンダラーをプラグイン方式に刷新し、パフォーマンス向上と詳細な修復設定を実現する。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 92/100 | **Annex Potential**: 88/100 | **Overall**: 84/100

**Topics**: [[Vercel, Markdown, Streaming UI, React, Performance]]

Vercelは、AIによるテキスト生成（ストリーミング）に最適化されたMarkdownレンダリングライブラリ「Streamdown」のメジャーアップデートとなるv2をリリースした。

今回のアップデートの最大の眼目は、ユーザーからの要望が最も多かったバンドルサイズの削減だ。v2ではプラグインベースのアーキテクチャが導入され、開発者は`code`、`mermaid`、`math`（KaTeX）、`cjk`（日中韓文字対応）といった機能を必要に応じて個別にインポートできるようになった。これにより、不要なコードを排除し、フロントエンドのパフォーマンスを大幅に向上させることが可能になった。

また、UX面での改善として、コンテンツの生成中であることを示す「キャレット（カーソル）」インジケーターが標準搭載された。これにより、テキストエディタのような視覚的フィードバックを容易に実装できる。

技術的に重要な点は、ストリーミング中の不完全なMarkdownをリアルタイムで補完・修復するバックエンドライブラリ「Remend」が詳細に設定可能になったことだ。著者は、リンク、画像、太字、インラインコード、KaTeXといった要素ごとに、どの程度「修復（healing）」を適用するかを制御できるオプションを提供している。これにより、生成AI特有の「レンダリング途中の表示崩れ」を防止しつつ、アプリケーションの要件に合わせた挙動を選択できるようになった。`react-markdown`のドロップイン置換として設計されており、AIチャットインターフェースを構築するエンジニアにとって、実用性の高いツールへと進化している。