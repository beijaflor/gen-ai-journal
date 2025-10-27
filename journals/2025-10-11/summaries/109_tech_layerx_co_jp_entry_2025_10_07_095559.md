## 【Agent Memory】Graphitiで法文書のインデックスを構築する

https://tech.layerx.co.jp/entry/2025/10/07/095559

LayerXのエンジニアが、Agent Memory向けTemporal Knowledge GraphフレームワークGraphitiを法律文書の構造に特化させるため、エンティティ・エッジ抽出のプロンプトを調整し、その実践的なアプローチを共有します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[Agent Memory, Temporal Knowledge Graph, Graphiti, Prompt Engineering, 法律文書処理]]

LayerXのエンジニアが、AI Agentの永続的な記憶層を構築するAgent Memoryにおいて、時系列知識グラフフレームワークGraphitiを法律文書のインデックス化に応用する挑戦的な取り組みを紹介します。Graphitiは本来チャットアプリケーションを想定しているため、法律文書特有の「条・項・号」といった階層構造や、相対参照（例：「前項の規定」）を正確に抽出する課題が存在しました。

この課題に対し、著者はGraphitiの内部関数である`extract_text`（エンティティ抽出）と`edge`（エッジ抽出）のプロンプトを直接書き換え、GPTモデルが法律文書の条文番号を明確なエンティティとして認識し、項を跨ぐ参照関係まで正しく抽出するようチューニングしました。具体的には、プロンプト内で「第n条n項n号」のような絶対表現への解決ガイドラインや、相対表現の解釈ルールを詳細に指示し、指示代名詞の問題を解決。さらに、GPTの`reasoning`レベルを`'minimal'`から`'medium'`に引き上げることで、複雑なエッジ関係の検出精度を向上させています。

この実践的な知見は、大規模な契約書や規定集といった長大な構造化文書をAI Agentに扱わせる際に極めて重要です。単にテキストを埋め込むだけでなく、文書内の意味的・構造的関係性をKnowledge Graphとして構築することで、Agentは文脈に即した正確な情報検索や推論が可能になります。これにより、開発者はLLMのコンテキストウィンドウの限界に縛られず、より高度で信頼性の高いAgentシステムを構築するための具体的なアプローチを得られます。