## M4 の MacBook Air でローカルLLM（2種）： MLX版と公式の GGUF版の「Jan-v1-4B」をそれぞれ軽く試す（MLX LM と LM Studio を利用）

https://qiita.com/youtoy/items/dc8818981b7baff5dc08

本記事は、M4 MacBook Air上でローカルLLM「Jan-v1-4B」のMLX版とGGUF版を、LM StudioとMLX LMを用いて比較評価し、その実用的な性能を示します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 74/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[Local LLM, MLX, GGUF, MacBook Air M4, LM Studio]]

Webアプリケーションエンジニアにとって、開発環境のパフォーマンス向上やプライバシー保護は喫緊の課題です。本記事は、Apple Silicon搭載MacでのローカルLLM活用に焦点を当て、具体的に「Jan-v1-4B」モデルのMLX版とGGUF版を、それぞれMLX LMとLM StudioでM4 MacBook Air（メモリ16GB）上で動作させた実践的評価を共有しています。

特筆すべきは、2.5GB程度の小規模モデルが、持ち運び可能なM4 MacBook Airで十分に実用的な速度で動作するという結果です。LM Studio経由のGGUF版は推論時間約26秒、26.61トークン/秒を記録し、MLX LM経由のMLX版は生成速度34.880トークン/秒、ピークメモリ使用量2.434GBという詳細な性能指標が示されています。

この検証結果は、Webアプリケーション開発において、コード補完、ドキュメント生成、テストコード作成といったGenerative AI機能をローカル環境で手軽に統合できる可能性を示唆します。特に、インターネット接続に依存しないオフラインでの開発や、機密性の高いコードのプライバシーを確保しながらAIの恩恵を享受できる点は、今日の開発現場にとって極めて重要です。小規模ながらも実用的なLLMがコンシューマー向けデバイスで動作することは、個々の開発者の生産性を飛躍的に向上させ、新たな開発ワークフローを構築する基盤となり得ます。