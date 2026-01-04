## Claude Code用TD Skills - Treasure Data向けAIネイティブCLI

https://tdx.treasuredata.com/guide/td-skills.html

Treasure Dataの操作をターミナル上のAIエージェントで完結させる専用プラグイン群を提供し、データエンジニアリングの効率を極限まで高める。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Treasure Data, Claude Code, AI Agent, Data Engineering, Digdag]]

Treasure Dataは、Anthropic社が提供するAIネイティブなCLIツール「Claude Code」を拡張する専用プラグイン群「TD Skills」を公開した。これにより、開発者はターミナル上で動作するAIエージェントを介して、Treasure Dataのクエリ作成、ワークフロー管理、CDP設定などの複雑なタスクを自然言語で実行・自動化できるようになる。

本ツール群は、データエンジニアリングの実務に即した3つの主要なカテゴリーで構成されている。
1. **SQL Skills (`sql-skills`)**: Treasure Data特有のTrino/Hive関数（`td_interval`や`td_time_range`など）をAIが正しく理解し、クエリの最適化や修正を行う。特に、メモリ不足エラー発生時にTrinoクエリを自動的にHiveへ変換する機能や、パーティションプルーニングを意識した時間フィルタリングの生成など、プラットフォームの特性を熟知したアシストを提供する。
2. **Workflow Skills (`workflow-skills`)**: Treasure Workflow（Digdag）の構文や`td>`オペレータを用いたワークフロー構築をサポートする。dbtとの連携設定やデバッグ、リトライ・バックフィルパターンの提案など、オーケストレーション作業の工数を大幅に削減する。
3. **tdx Skills (`tdx-skills`)**: CDPとしての中心機能であるセグメント作成やジャーニー定義のYAML構成、コネクタ設定などをCLIから直接制御する。また、`tdx agent`を用いて Treasure Data 独自のAIエージェントを構築するためのプロンプト作成支援機能も含まれている。

筆者（Treasure Data）によれば、これらのスキルは単なる補助ツールではなく、データ運用におけるコンテキストスイッチを最小化し、AIとの対話を通じて高品質なデータパイプラインを迅速にデプロイするための「AIネイティブなワークフロー」を実現するものである。`tdx claude`コマンド一つですべてのスキルが統合された状態で起動できるため、エンジニアは環境構築の手間なく即座に高度なAIアシスタンスの恩恵を受けることができる。GUI操作やドキュメント参照に費やしていた時間を、より本質的なデータ設計や分析に充てられるようになる点が、このツールの最大の意義であると主張されている。