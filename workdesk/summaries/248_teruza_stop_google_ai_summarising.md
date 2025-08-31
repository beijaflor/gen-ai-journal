## How to Stop Google from AI-Summarising Your Website (and Reclaim Your Organic Traffic)

https://www.teruza.com/info-hub/how-to-stop-google-from-ai-summarising-your-website

GoogleのAI検索結果要約がウェブサイトのトラフィックを減少させる問題に対し、サイト運営者が`max-snippet:0`などのメタタグを用いて対抗する方法と、進行中の規制動向を詳述します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 84/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[AI Overviews, Google SEO, Traffic Reduction, Meta Tags, Regulatory Investigations]]

Googleが検索結果に導入したAIによる要約機能「AI Overviews」が、ウェブサイト運営者にとって深刻なトラフィック減少問題を引き起こしています。ユーザーがサイトにアクセスせずとも検索結果ページで情報が得られるため、オーガニックトラフィックが奪われ、これはコンテンツ提供者の収益モデルを脅かしかねない「ダークパターン」であると指摘されています。

この問題に対し、サイト運営者が講じうる具体的な技術的対策として、主に3つのメタタグが紹介されています。
1.  **`<meta name="robots" content="max-snippet:0">`**: このタグは、AIによる要約だけでなく、通常の検索結果スニペットも含む全ての要約表示を停止させます。これにより、AI Overviewsからのトラフィック流出は防げますが、検索結果の魅力が低下し、クリック率（CTR）が大幅に減少する可能性があります。現状では最も効果的ですが、諸刃の剣となる解決策とされています。
2.  **`<meta name="robots" content="nosnippet">`**: `max-snippet:0`とほぼ同じ効果を持ち、検索結果の記述を完全に削除します。
3.  **`<span data-nosnippet>`**: 特定のテキストセクションのみを要約から除外できるものの、Googleが他の部分から要約を生成する可能性があり、完璧な解決策ではありません。

なぜこれが重要かというと、ウェブサイト運営者は「AIにコンテンツを要約されてトラフィックを奪われる」か「要約をブロックして検索結果での視認性を失う」かの二者択一を迫られているからです。これは、Googleが自身のプラットフォーム上での支配力を利用し、ウェブエコシステムを歪める可能性を示唆しています。

しかし、希望も見えてきました。EUと英国の規制当局が、GoogleのAI Overviewsが独占禁止法に抵触し、パブリッシャーに損害を与えているとして調査を開始しています。強制的な帰属表示やトラフィック共有の義務付け、Googleの自己優遇の制限などが検討されており、これは長期的な解決に向けた重要な一歩となるでしょう。当面の間は、不完全ながらも`max-snippet:0`が最も現実的な対策とされています。