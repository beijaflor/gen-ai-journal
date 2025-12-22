## StrandsAgents + Nova 2 Sonic + Bedrock Knowledge Base で対話型アシスタントを作成する

https://acro-engineer.hatenablog.com/entry/2025/12/18/070000

Amazon Nova 2 SonicとStrandsAgents Bidirectional Agent、Bedrock Knowledge Baseを組み合わせ、音声による高速な双方向対話型AIアシスタントを構築し、その実用性、応答速度、課題を詳細に解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 100/100 | **Annex Potential**: 100/100 | **Overall**: 88/100

**Topics**: [[音声対話AI, StrandsAgents, Amazon Bedrock, RAG, リアルタイムエージェント]]

本記事は、Amazon Nova 2 Sonic、StrandsAgents Bidirectional Agent、およびBedrock Knowledge Baseを統合し、音声によるリアルタイムの対話型AIアシスタントを構築する具体的な手法と、その実用的な価値および課題を詳述する。ウェブアプリケーションエンジニアにとって、このアプローチは音声インターフェースを活用した新しいUXの可能性と、それに伴う技術的障壁への対処法を提示する点で重要だ。

著者は、Nova 2 SonicのSpeech-to-Speech機能とStrandsAgentsのBidirectional Agent（BidiAgent）の組み合わせにより、ユーザーの割り込み発話にも自然に対応する低ストレスな音声対話が実現したと強調している。特に、ユーザーが話し終えてから最初の音声応答まで約2秒という低レイテンシは、会話としてほとんどストレスを感じさせないレベルであり、実用化に向けた大きな進歩を示している。

なぜこれが重要かというと、Bedrock Knowledge BaseをRAG（Retrieval Augmented Generation）に利用することで、AgentCoreドキュメントのような社内ナレッジに対する音声での質問応答が、高い精度と高速性で可能になるためだ。記事中では「AgentCore Runtimeについて教えて」といった質問に対し、関連ドキュメントから要約された的確な回答が得られる様子が示されている。

実装面では、StrandsAgentsのサンプルをベースに、モデルを`BidiNovaSonicModel`に指定し、ツールとして`retrieve`を追加するだけで、この高度なシステムが構築できる手軽さが特徴だ。これは、リアルタイム音声AIエージェントの開発コストを大幅に削減できる可能性を意味する。

しかし、著者は複数の実用上の課題も明確に指摘している。
*   **日本語の発音と記号の読み上げ**: Nova 2 Sonicは日本語の発音に不自然な部分があり、数式や記号の読み上げが苦手なため、音声だけでなくテキスト表示（BidiTextIO）の併用やプロンプトによる指示の工夫が必要だと述べる。
*   **RAGコンテキスト内のコードの読み上げ**: Knowledge Baseにコードブロックや設定例が含まれる場合、それらがそのまま音声で読み上げられると理解が困難になる。この問題に対し、著者はナレッジ側のコンテンツ設計、StrandsAgentsのフックによるフィルタリング、またはプロンプトによる制御といった対策の必要性を提言している。

これらの課題は、音声AIを実際の業務フローに組み込む上で避けて通れない具体的な問題であり、先行事例としての著者の考察は、今後の開発における貴重な指針となるだろう。特に、コーディング中にエディタからフォーカスを外すことなく音声で質問できる「隣に座ってペアプロしてくれる先輩エンジニア」のような体験は、開発者の生産性向上に直結する可能性を秘めている。