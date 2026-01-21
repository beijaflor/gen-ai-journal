## Claude Codeでreact-best-practicesスキルをadd-skillでインストールして使ってみた

https://zenn.dev/tonkotsuboy_com/scraps/01b829b7e7c157

Vercelが公開した「add-skill」ツールを用い、Claude Code等のAIエージェントへReactの専門知見を即座に装備させて開発ワークフローの質を向上させる。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[Claude Code, Vercel, React, Next.js, add-skill]]

Vercelがリリースした、10年分のReact/Next.jsの知見を凝縮した「react-best-practices」を、AIエージェントに統合する具体的な手順が示されている。特筆すべきは、同社が提供を開始したnpmパッケージ「add-skill」の存在である。著者は、`$ npx add-skill vercel-labs/agent-skills` というコマンド一つで、Claude CodeやCursorといった主要な開発環境へインタラクティブに専門スキルを導入できる簡便さを高く評価している。

実証実験では、Claude Codeに導入したスキルを用いてプルリクエストのレビューを実施。AIが「React.cache」の適用を提案するなど、Vercel公式のベストプラクティスに基づいた的確な指摘を行う様子が報告されている。筆者によれば、この手法は「男は黙って！」実行すべきほど強力であり、汎用的なLLMの知識だけでは到達しにくいフレームワーク固有の最適化を、AIエージェントを通じて自動的に開発ワークフローへ組み込める点が最大の利点である。エンジニアにとって、最新の公式知見をAIの「追加スキル」として即座に同期できるこの仕組みは、コード品質の担保とチームの教育コスト低減を同時に実現する、極めて実用性の高い手法と言える。