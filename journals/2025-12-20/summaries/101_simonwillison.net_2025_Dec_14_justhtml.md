## 「JustHTML」に見るVibe Engineeringの真髄

https://simonwillison.net/2025/Dec/14/justhtml/

**Original Title**: JustHTML is a fascinating example of vibe engineering in action

「JustHTML」の開発事例を通して、専門知識を持つプログラマーがAIを高度に活用し、設計や品質管理を主導する「Vibe Engineering」の重要性を論じます。

**Content Type**: 💭 Opinion & Commentary
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 93/100 | **Annex Potential**: 94/100 | **Overall**: 92/100

**Topics**: [[Vibe Engineering, AI-Assisted Programming, Coding Agents, HTML Parsing, ソフトウェアエンジニアリングプラクティス]]

Simon Willison氏は、Emil Stenström氏が開発したPythonの新しいHTML解析ライブラリ「JustHTML」を紹介し、その機能性（純粋なPython実装、html5lib-testsの9,200以上のテスト合格、100%のテストカバレッジ、CSSセレクターサポート、わずか3,000行のコード）に当初は感銘を受けました。Willison氏は後に、このライブラリがGitHub CopilotのAgentモード、Claude Sonnet 3.7、Gemini 3 Pro、Claude Opusといった複数のLLMを活用した「コーディングエージェント」によってほぼ構築されたことを知ります。

Willison氏は、この開発プロセスを、彼が提唱する「Vibe Engineering」の優れた事例として高く評価しています。「Vibe Engineering」とは、コードレビューなしでLLMにコードを生成させる「Vibe Coding」とは異なり、専門的なプログラマーがAIコーディングエージェントをプロフェッショナルかつ責任ある方法で活用し、高品質で信頼性の高い結果を生み出すアプローチです。

Emil氏の詳細な開発手法は、「Vibe Engineering」の具体的な実践を示しています。彼は開発初期からブラウザベンダーも利用するhtml5lib-tests適合性スイートを導入し、厳格な品質保証を確立しました。また、API設計は自身で行い、モデルに実装を指示。既存ライブラリとの比較ベンチマークを組み込み、初期の数値に基づいてRustによる最適化を試みました。さらには、元のコードを一度破棄し、Servoのhtml5everライブラリを基に再構築し、カスタムプロファイラと新たなベンチマークを構築してGemini 3 Proに微細な最適化を行わせることで、既存の純粋なPythonライブラリを上回るパフォーマンスを達成しました。さらに、カバレッジツールで不要なコードを特定・削除し、カスタムファザーを構築して大量の不正なHTMLドキュメントを生成させ、パーサーの堅牢性を強化しました。

Willison氏は、こうしたEmil氏のアプローチを「リードアーキテクトの役割に近い」と表現し、「エージェントはタイピングを、私は思考を行った」というEmil氏の結論に強く同意しています。これは、AIコーディングエージェントがコードのタイピングという作業を代替し、プログラマーがより価値の高い設計、意思決定、エージェントの指示といった知的活動に時間を集中できる、という現代のソフトウェア開発における理想的な役割分担を示唆しています。