## コンテンツネゴシエーションを活用した「AIエージェントに優しい」ページの構築手法

https://vercel.com/blog/making-agent-friendly-pages-with-content-negotiation

**Original Title**: Making agent-friendly pages with content negotiation

HTTPコンテンツネゴシエーションを活用し、AIエージェントに対してHTMLの代わりに最適化されたMarkdownを優先的に配信する手法を実装する。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 81/100 | **Overall**: 80/100

**Topics**: [[Content Negotiation, AI Agents, Markdown, Next.js, Token Optimization]]

Vercelは、自社のブログや変更ログにおいて、AIエージェント向けに最適化された**Markdown**形式を動的に返却する機能を導入した。これは、人間にはリッチなHTMLを提供し、**Claude Code**などのエージェントには構造化されたテキストを提供する**コンテンツネゴシエーション**（HTTP `Accept` ヘッダーの活用）によって実現されている。

技術的には、**Next.js**のミドルウェアがリクエストを検知し、**Contentful**のコンテンツを変換するルートハンドラーへ誘導する仕組みだ。これにより、HTML版（約500KB）と比較してペイロードを約2KB（99.6%削減）まで軽量化し、AIの**コンテキストウィンドウ**消費を劇的に抑え、トークン効率と処理速度を向上させている。また、エージェントが情報を網羅できるよう、メタデータを含む専用の**Markdownサイトマップ**も提供している。

RAGやAIエージェント向けのWebインターフェースを構築する開発者にとって、既存のWeb資産を「エージェント読み取り専用」に最適化する非常に実用的かつ即応性の高い設計パターンとなっている。