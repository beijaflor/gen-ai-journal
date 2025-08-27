## A proposal for inline LLM instructions in HTML based on llms.txt

https://vercel.com/blog/a-proposal-for-inline-llm-instructions-in-html

VercelがAIエージェント向けに、HTML内に直接命令を埋め込むことで保護されたWebコンテンツへのアクセスを容易にする`<script type="text/llms.txt">`形式を提案します。

**Content Type**: Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 91/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[AIエージェント, LLM連携, HTML拡張, Vercel, 認証メカニズム]]

Vercelは、CursorやDevin、Claude CodeといったAIエージェントが認証保護されたVercelプレビューデプロイメントに直接アクセスできないという課題に対し、HTML内に直接LLMへの指示を埋め込む新たな慣習を提案しました。具体的には、HTTP 401レスポンスなどのHTML内に`<script type="text/llms.txt">`タグを使用し、エージェントが保護されたコンテンツにアクセスするためのメソッド（例：Vercel MCPサーバーのget_access_to_vercel_url関数やバイパストークン利用方法）を記述します。

このアプローチの利点は、ブラウザが未知のスクリプトタイプを無視するため、通常のユーザー体験には影響がない点です。一方で、LLMはこれらのスクリプト要素を認識し、適切な指示として解釈します。既存の`llms.txt`標準に準拠することで、ウェブ上のLLM向けコンテンツ発見メカニズムと整合性を保ちます。Vercelは既にこの仕組みを本番環境の401ページに導入しており、AIエージェントがVercelのデプロイメントに容易にアクセスできるようになっています。

これは、AIエージェントがサイトやアプリケーションをナビゲートする際に、利用可能なサービス（例えば、MCPサーバー）を直接発見したり、エラーページから問題解決のためのサービスへ誘導したりする汎用的な方法として注目されます。LLMの柔軟性を活かし、特定の訓練やプロバイダーとの連携なしに、この慣習をすぐに導入できる点が大きなメリットです。ウェブ開発者にとって、AIエージェントのユーザーエクスペリエンス（DX）を向上させ、プラットフォームの機能をより効果的にエージェントに伝えるための強力な手段となるでしょう。