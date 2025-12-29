## ONNXとRegexを組み合わせたAIワークフロー向けローカル完結・可逆的PIIスクラバー

https://medium.com/@tj.ruesch/a-local-first-reversible-pii-scrubber-for-ai-workflows-using-onnx-and-regex-e9850a7531fc

**Original Title**: A local-first, reversible PII scrubber for AI workflows using ONNX and Regex

外部AIサービスへのデータ送信時に、翻訳品質を損なわずに個人情報を保護する可逆的マスキングライブラリ「rehydra」を公開し、その技術的アプローチを解説する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 82/100 | **Overall**: 88/100

**Topics**: [[PII Masking, TypeScript, LLM Security, ONNX Runtime, Machine Translation]]

エンジニアがユーザーのサポートチケットやドキュメントをDeepLやGPT-5などの外部APIで処理する際、欧州のGDPRなどの規制により個人情報（PII）の送信は厳しく制限されている。著者は、単なるデータの「黒塗り」が翻訳品質を著しく低下させるという「プライバシー・翻訳パラドックス」を指摘している。例えば、「John」を単に「PERSON」というタグに置き換えると、ドイツ語やフランス語のような言語では、代名詞の性別一致や格変化のコンテキストが失われてしまうからだ。この課題を解決するため、著者はローカル環境（Node.js/Bun）で動作し、可逆的かつ文脈を維持したままPIIをマスキングできるTypeScriptライブラリ「rehydra」を開発・公開した。

筆者が提唱するソリューションの核心は、「検出→マスク→翻訳→再水和（Rehydrate）」というライフサイクルにある。検出フェーズでは、IBANやメールアドレスなどの構造化データには高速なRegex（正規表現）を用い、人名や組織名、場所などの非構造化データにはONNX Runtime上で動作する量子化されたNER（名前付きエンティティ認識）モデルを組み合わせるハイブリッド戦略を採用している。これにより、サブミリ秒のストリーム処理から高精度なドキュメント処理まで、開発者がトレードオフを選択できる柔軟性を提供している。

特に実用的な工夫として、筆者は「セマンティック・マスキング」と「ファジーな再水和」を挙げている。前者は、タグに性別や場所の属性（市、国など）をメタデータとして付与することで、翻訳エンジンが正しい文法で出力できるようにする試みだ。後者は、外部AIがタグ内のスペースや引用符を勝手に変更してしまう「ハルシネーション」に対処するための実装で、厳密な一致ではなく曖昧なパターンマッチングによって元のPIIを復元する。

セキュリティ面でも、PIIの対応表（PII Map）をAES-256-GCMで暗号化し、すべての個人情報をローカルのメモリ空間から出さない「ローカルファースト」の設計を徹底している。Webアプリケーションエンジニアにとって、本ツールはプライバシー保護とAI活用の利便性を両立させるための、具体的かつ強力な実装の選択肢となるだろう。