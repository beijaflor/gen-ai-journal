## Claude Codeの対話記録を詳細なHTMLに変換・共有する新ツール「claude-code-transcripts」が登場

https://simonwillison.net/2025/Dec/25/claude-code-transcripts/

**Original Title**: A new way to extract detailed transcripts from Claude Code

Claude Codeでの対話記録を抽出し、推論プロセスまで含めた詳細なHTML形式で保存・共有可能にするPython CLIツールを紹介する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 94/100 | **Annex Potential**: 93/100 | **Overall**: 92/100

**Topics**: [[Claude Code, LLM Transcripts, Python, CLI Tools, AI-Assisted Programming]]

Anthropicが提供するエンジニア向けAIエージェント「Claude Code」の対話ログを、読みやすく共有しやすいHTMLドキュメントに変換するツール「claude-code-transcripts」がSimon Willison氏によって公開された。このツールは、ローカルのセッションだけでなく、iPhoneアプリなどのモバイル環境から利用した「Claude Code for web」のセッションも取得し、GitHub Gist経由で即座に公開する機能を備えている。

著者がこのツールを開発した背景には、開発ワークフローの劇的な変化がある。著者は現在、エディタで直接コードを書くよりもClaude Code経由で実装する時間が長くなっており、特に外出先からiPhoneのClaudeアプリを使って複雑な機能を実装する「サイエンス・フィクションのような働き方」を日常的に行っている。しかし、ここで問題となるのが、開発における重要な意思決定や設計の根拠（Context）がAIとの対話の中に閉じ込められてしまうことだ。かつてGitHubのIssueやコメントに記録されていた「なぜこの実装にしたのか」という背景が、今やLLMとの対話記録へと移行しているのである。

このツールの特筆すべき点は、単なるログの書き出しに留まらず、Claude Codeが内部で生成している「思考トレース（thinking traces）」をも可視化できる点だ。通常のターミナル画面のコピーでは見落とされがちな、AIが問題をどのように分析し、どのような試行錯誤を経て結論に至ったかという詳細なプロセスを記録できる。これにより、後からのコードレビューや、将来的なメンテナンス時の文脈理解が格段に容易になる。

技術的な実装面も興味深い。このツール自体がClaude Codeを駆使して開発されており、テストには`pytest`やスナップショットテスト用の`syrupy`が活用されている。また、Web版Claude Codeからセッションを取得するために、プライベートAPIを逆コンパイルして解析。macOSのキーチェーンから認証トークンを安全に取り出す仕組みを実装するなど、実用的なエンジニアリング手法が凝縮されている。

AIエージェントによる自動コーディングが普及するにつれ、ソースコードそのものと同じくらい、そこに至るまでの「対話プロセス」の資産価値が高まっている。本ツールは、そのプロセスを透明化し、チームやコミュニティで共有可能な知見へと変換するための、現代的な開発者にとって不可欠なユーティリティと言える。