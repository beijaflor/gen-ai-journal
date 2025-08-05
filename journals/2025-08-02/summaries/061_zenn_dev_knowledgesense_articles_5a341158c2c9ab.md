## Googleによる Deep Research の新手法、OpenAI超え

https://zenn.dev/knowledgesense/articles/5a341158c2c9ab

Google Cloudの研究者らが開発した新しいDeep Research手法「Test-Time Diffusion Deep Researcher（TTD-DR）」は、初期の下書きを反復的にブラッシュアップし、必要に応じて調査計画を柔軟に変更することで、既存手法を上回る高精度な回答を生成します。

**Content Type**: Research & Analysis

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 83/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[Deep Research, AI Agent, LLM, RAG, Research Methodology]]

「Deep Research」機能はWeb情報を基に深く考察し、高精度な回答を生成するAIエージェントの重要な能力ですが、既存のオープンソース実装（GPT Researcherなど）は精度に課題があります。これは、従来のDeep Researchが「計画→Web検索→レポート作成」といった線形的なアルゴリズムに依存し、検索中に重要な発見があっても当初の計画を柔軟に変更できないため、調査が目的からずれてしまうことに起因します。

この課題に対し、Google Cloudの研究者らが2025年に提案した新手法が「Test-Time Diffusion Deep Researcher（TTD-DR）」です。TTD-DRは、人間がレポートを作成するプロセス、すなわち「まず初期仮説に基づき下書きを作成し、それを反復的にブラッシュアップしつつ、必要に応じて全体計画を大胆に変更する」というアプローチをAIエージェントに再現させます。具体的には、まずLLMの内部知識のみでレポートの骨子となる「初期下書き」と「リサーチ計画」を生成。その後、Web検索結果を基に初期下書き全体を繰り返し改善し、この過程で「計画」自体も自己進化させることで、LLMの回答に高い柔軟性を持たせます。

この手法の「なぜ重要か」は、その圧倒的な性能向上にあります。TTD-DRは、OpenAIのDeep Researchを含む既存のあらゆるサービスをベンチマークで上回り、特に長文レポート生成タスクではOpenAIに対して69.1%〜74.5%の勝率を達成。処理時間も同等以下でありながら、高精度を実現しています。

我々Webアプリケーションエンジニアにとって、この技術は、特に社内データを活用するエンタープライズ向けRAGシステムに大きな示唆を与えます。RAGにおいて単一の検索では不十分な複雑な社内データ課題に対し、TTD-DRのような「深く」「繰り返し」調査する手法を組み合わせることで、RAGの回答精度を飛躍的に向上させる可能性を秘めています。これは、より賢く、実用的なエンタープライズAIソリューションを構築する上で不可欠な進歩となるでしょう。