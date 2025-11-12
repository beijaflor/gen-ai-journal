## Moonshot AI、推論とツール実行を統合したK2 Thinkingモデルを発表

https://moonshotai.github.io/Kimi-K2/thinking.html

**Original Title**: Kimi K2 Thinking

Moonshot AIが、思考プロセスとツール実行を単一モデル内で統合したK2 Thinkingを発表し、SWE-Bench Verifiedで71.3%、BrowseCompで60.2%を記録、人間の介入なしで200-300回の連続ツール実行を実現した。

**Content Type**: 🔬 Research
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 92/100 | **Annex Potential**: 85/100 | **Overall**: 92/100

**Topics**: [[エージェント型AI, 思考推論モデル, ツール統合, SWE-Bench, コーディングエージェント]]

Moonshot AIは、オープンソース思考推論モデル「Kimi K2 Thinking」を発表しました。このモデルの最大の特徴は、推論とツール実行を単一のモデルアーキテクチャ内で統合し、従来のように推論LLMとツール実行システムを分離せず、200-300回の連続ツール呼び出しを人間の介入なしに実行できる点です。

主要ベンチマークでの成果として、SWE-Bench Verified（ソフトウェアエンジニアリングベンチマーク）で71.3%、SWE-Bench Liteで59.5%を記録し、複数ファイルにまたがるコードベース編集で高い成功率を示しています。エージェント型推論タスクでは、HLEツール使用時に44.9%を記録しGPT-4o（23.1%）を上回り、BrowseComp（ウェブブラウジング）では60.2%を達成しました。一般推論能力においても、AIME 2024で56.7%、GPQA Diamondで65.2%、Codeforces Eloレーティング1620を記録しています。

技術仕様は、Kimi k1.5をベースモデルとし、Apache 2.0ライセンスで公開。Hugging Faceでモデルウェイトがダウンロード可能で、APIアクセスも提供されています。エージェントとして検索エンジン、Wikipedia、ウェブページ読み取り、URLナビゲーション機能を統合活用します。
