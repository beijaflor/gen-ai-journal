## AI誤情報実験：AI検索が嘘を信じ込むプロセスとエンジニアへの教訓

https://ahrefs.com/blog/ai-vs-made-up-brand-experiment/

**Original Title**: I Ran an AI Misinformation Experiment. Every Marketer Should See the Results

架空のブランドを用いた実験を通じて、AI検索エンジンが詳細な虚偽情報を公式情報よりも優先して引用する脆弱性を暴き、情報の信頼性確保の重要性を提言する。

**Content Type**: 🔬 Research & Analysis
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 89/100 | **Overall**: 88/100

**Topics**: [[AI Misinformation, LLM Reliability, AI Search SEO, RAG, Brand Safety]]

Ahrefsのマーケティングリサーチャー、Mateusz Makosiewicz氏が行ったこの実験は、現在のAI検索エンジンが「真実性」よりも「情報の具体性」を優先してしまう深刻な脆弱性を浮き彫りにした。筆者は架空の高級ペーパーウェイトブランド「Xarumei」を設立し、公式サイトを立ち上げた後、RedditやMedium、独自ブログを通じて意図的に矛盾する虚偽情報をネット上に散布した。その後、Perplexity、Gemini、ChatGPT、Grok、Copilotなどの主要AIツールがこれらの情報をどう処理するかを2ヶ月にわたって追跡調査した。

実験の結果、衝撃的な事実が明らかになった。GeminiやPerplexity、Grokを含む多くのAIモデルが、公式サイトのFAQにある「否定」よりも、Redditの「内部告発」やMediumの「調査記事」を装った詳細な嘘を信じ込み、事実として回答したのである。特に、もっともらしい嘘を暴くふりをして新たな嘘を混ぜ込んだMediumの記事は、AIの信頼を勝ち取る上で極めて効果的であった。筆者は、LLMが情報を選択する際、「曖昧な真実」よりも「詳細に記述されたフィクション」を選択する傾向が強いと分析している。これは、具体的数値や地名、人名を含むストーリーの方が、AIの検索アルゴリズムや文脈理解において「権威ある情報」として処理されやすいためである。

特筆すべきは、モデル間での耐性の差だ。ChatGPT-4およびGPT-5は公式サイトのFAQを優先して参照し、虚偽情報を退ける堅牢性を示したが、GeminiやAI Modeは一度信じた虚偽情報を修正せず、以前の懐疑的な態度を忘れて自信満々に嘘を繰り返し続けた。筆者はこの現象を「ナラティブの乗っ取り」と呼び、Webアプリケーションエンジニアやマーケターに対して、AI時代の新しいPR戦略を提言している。

エンジニアリングの観点からは、RAG（検索拡張生成）のソースとしてのRedditやMediumの影響力の大きさを再認識する必要がある。筆者は、AIによる情報の空白を埋めるために、公式FAQの構造化（Schema markupの利用）、具体的な数値データを含む詳細な解説ページの作成、そして主要AIモデルごとのブランド言及内容の継続的なモニタリングが不可欠であると主張している。AIはソースの信頼性を判断する能力がまだ不十分であり、開発者は自社製品やサービスに関する正確な「グラウンディング（根拠付け）」をAIに対して能動的に提供し続けなければならない。