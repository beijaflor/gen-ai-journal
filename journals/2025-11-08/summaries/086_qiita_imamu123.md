## 【GitHub Copilot】「コードが学習されるのが不安」を解消するオプトアウト設定

https://qiita.com/imamu123/items/e7105ab0e0a6292f0937

GitHub CopilotでプライベートコードがAIモデルの学習に利用される懸念を解消するオプトアウト設定方法を解説します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:3/5 | Depth:2/5 | Unique:2/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 65/100 | **Annex Potential**: 60/100 | **Overall**: 64/100

**Topics**: [[GitHub Copilot, プライバシー設定, AIモデル学習, データ利用, オプトアウト]]

この記事は、GitHub Copilot利用におけるプライベートコードのAI学習利用への懸念を持つ開発者向けに、その不安を解消するオプトアウト設定の手順を具体的に解説しています。著者は、情報流出やコードがAI学習に利用されることへの個人的な懸念から、その設定方法を調査し、備忘録として共有しています。

主な設定手順として、GitHubの「Settings」から「Copilot」セクションに進み、「Privacy」項目を確認することを案内しています。特に重要なのは「Allow GitHub to use my data for AI model training」という設定項目で、これを無効化（チェックを外す）することで、自身のコードがAIモデルの改善（学習）に利用されることを防げると著者は述べています。

また、関連設定として「Suggestions matching public code」（公開コードに一致する提案）についても触れていますが、これは学習オフ設定とは異なると説明しています。補足として、組織向けの有料版であるCopilot BusinessやEnterpriseでは、コードスニペットがAI学習に利用されないよう標準で設定されており、組織のデータが保護されるため、ガバナンスの観点からも推奨されると筆者は言及しています。この設定により、開発者は安心してGitHub Copilotを日々の開発に活用できるようになると結んでいます。