## Google、健康に関するAI要約の一部を削除——調査で「危険な欠陥」が判明

https://arstechnica.com/ai/2026/01/google-removes-some-ai-health-summaries-after-investigation-finds-dangerous-flaws/

**Original Title**: Google removes some AI health summaries after investigation finds “dangerous” flaws

Googleは、検索結果のAI Overviewsが肝臓検査値などの医療情報で誤った回答を生成し、患者に健康被害を及ぼすリスクがあるとして、一部の機能を停止した。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:3/5 | Practical:3/5 | Anti-Hype:5/5
**Main Journal**: 81/100 | **Annex Potential**: 78/100 | **Overall**: 76/100

**Topics**: [[Google, AI Overviews, RAG, 医療AI, ハルシネーション]]

Googleは、検索エンジンに統合されている生成AI機能「AI Overviews」が、健康に関する重大な誤情報を生成したとして、一部の回答表示を停止した。英Guardian紙の調査により、特定の医療クエリに対してAIが医学的根拠のない、あるいは既存の医療ガイドラインに反する「危険な回答」を出力していたことが明らかになった。

具体的に指摘されたのは、肝機能検査の血液検査結果（ALT、AST、アルカリホスファターゼなど）に関するクエリだ。AI Overviewsは、患者の年齢、性別、人種といった重要な臨床的背景を無視したまま、単なる数値テーブルを提示。専門家は、実際には重篤な肝疾患を抱えている患者が「正常値である」とAIに誤認させられ、必要な受診を見送る「誤った安心感」を与えるリスクがあると警告している。また、膵臓がん患者に対しては、標準的な医療アドバイスである「体重維持のための食事」とは真逆の「高脂肪食品の回避」を推奨し、患者の健康を直接的に損なう恐れがあった。

著者は、こうしたエラーが頻発する背景にAI Overviewsの構造的な設計ミスがあると指摘している。このシステムは、Googleの検索ランキング上位にあるウェブページを信頼できる情報源と仮定し、それらを要約するように設計されている。しかし、現在の検索アルゴリズムはSEO対策された低品質なコンテンツを排除しきれておらず、不正確な元データがAIモデルに供給される経路となっている。さらに、情報の統合プロセスにおいて、LLMが信頼性の高いソースから誤った結論を導き出したり、ハルシネーションを「断定的なトーン」で出力したりすることで、ユーザーを欺く結果を招いている。

Googleは、一部の特定のクエリについては機能を停止したが、類似の検索語（「lft reference range」など）では依然としてAI要約が表示される不完全な対応に留まっている。同社は「大半の情報は正確である」と弁明しているが、本記事は、RAG（検索拡張生成）ベースのシステムにおける出力制御の難しさと、SEOの汚染に対するレジリエンスの確保がいかに困難であるかを浮き彫りにしている。