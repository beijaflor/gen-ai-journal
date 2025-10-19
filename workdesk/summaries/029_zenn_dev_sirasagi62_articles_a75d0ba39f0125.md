## 実は進化している！ローカルで動くembeddingモデルたち

https://zenn.dev/sirasagi62/articles/a75d0ba39f0125

日本語RAGシステム向けに、軽量かつ高性能なローカル埋め込みモデル`ruri-v3`と`granite-embedding-107m-multilingual`が、APIコストとデータプライバシーの課題を解決する強力な選択肢として登場しました。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[ローカル埋め込みモデル, RAG, ruri-v3, granite-embedding, ONNX]]

日本語RAGシステムの構築において、APIコスト削減とデータプライバシー確保は喫緊の課題です。本記事は、オープンウェイトのローカル埋め込みモデルが驚くべき進化を遂げ、これらの課題を解決する強力な選択肢を提供していると強調します。特に、開発者が注目すべきは`ruri-v3`と`granite-embedding-107m-multilingual`の二つです。

まず、名古屋大学発の`ruri-v3`は、わずか37M（8ビット量子化で37MB）の`ruri-v3-30m`モデルで、日本語ベンチマークJMTEBにおいてOpenAIの`text-embedding-v3-large`に匹敵するか、それを上回る性能を発揮します。この極めて軽量なモデルは、CPUでも高速に動作し、日本語に特化したRAGアプリケーションのAPI利用料削減に大きく貢献します。著者は、ブラウザやNode.js、C++での利用を可能にするONNX版も提供しており、幅広い環境での導入を促しています。

次に、IBMの`granite-embedding-107m-multilingual`は、オープンウェイトモデルとしては珍しく、**日本語でのコード検索**において突出した性能を発揮します。多くのコード特化型埋め込みモデルが英語中心である中、このモデルは多言語対応に加え、日本語コードのセマンティック検索を可能にする点で、日本の開発者にとって非常に価値が高いです。パラメータ数も107Mと効率的で、多言語かつコードを含むRAGシステムを検討する際の有力な候補となります。

これらのモデルは、`veqlite`や`@huggingface/transformers.js`を用いた具体的なコード例とともに紹介されており、RAGシステムへの即時導入が可能です。高性能な埋め込み処理をローカルで完結できることは、API依存からの脱却を意味し、より堅牢でコスト効率の高いAIアプリケーション開発への道を開きます。
