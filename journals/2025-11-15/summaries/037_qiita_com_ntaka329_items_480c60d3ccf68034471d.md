## Copilot Agentの出力を`copilot-instructions.md`で自分好みにカスタマイズし、レビュー負荷を軽減する実践ガイド

https://qiita.com/ntaka329/items/480c60d3ccf68034471d

GitHub Copilot Agentの出力を、プロジェクトの要求に合わせて`copilot-instructions.md`を使ってカスタマイズすることで、レビューの負担を大幅に軽減できることを実例を交えて解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[GitHub Copilot Agent, プロンプトエンジニアリング, 開発者ワークフロー, コードレビュー, ドキュメント生成]]

本記事は、GitHub Copilot Agent利用時に発生する、冗長な出力やチームの標準に合わない出力に対するレビューの疲弊を解消するため、`copilot-instructions.md`の活用を提案しています。著者は、このファイルをプロジェクトの`.github`ディレクトリに配置するだけで、Copilotがユーザーの指示を処理する前に真っ先に読み込む「指示書」として機能することを強調しています。これにより、同じコメントを繰り返し書く手間が省ける点が大きな利点です。

具体的な活用例として、著者は二つの「Before/After」ケースを示しています。

一つ目の例は、API設計書の作成です。
- **Before**: Copilot AgentはOpenAPI形式ではなく、詳細かつ冗長なMarkdownを出力し、リクエスト例なども不要に含んでいました。
- **After**: `copilot-instructions.md`に「API設計書はOpenAPI YAMLとパラメーター詳細説明用のMarkdownを作成する」「OpenAPIで自明なリクエスト呼び出し例は不要」といった指示を追記した結果、CopilotはOpenAPI形式のYAMLと、簡潔なMarkdownを出力するようになり、レビュー負荷が軽減されました。

二つ目の例は、詳細処理フロー設計書の作成です。
- **Before**: Copilot Agentは1400行近い大量のMarkdownを出力し、処理フローをASCIIアートで表現したり、サンプルソースコードを含めたりと、レビューに手間がかかる形式でした。
- **After**: `copilot-instructions.md`に「図はMermaid記法で作成」「要点のみを簡潔に記載」「実装例のソースコードは不要」「Request parameterのvalidationはTable形式でまとめる」といった具体的な指示を追加しました。これにより、出力は370行まで簡素化され、Mermaidによる処理フローやTable形式のバリデーション記載など、レビューしやすい形式に改善されました。

著者は、`copilot-instructions.md`の運用について、「Agentに対し、同じようなコメントが3回ぐらい出てきたら追記する、ぐらいの軽めの運用でも良い」「最初は1行からでも大丈夫」と、気軽な導入を推奨しています。このアプローチにより、Agentの出力結果を自分好みに調整し、レビューにかかる時間を大幅に削減できると結んでいます。これは、Webアプリケーションエンジニアが日々の開発業務で直面するAIツールとの連携における具体的な課題を解決し、生産性向上に直結する重要なプラクティカルな知見です。