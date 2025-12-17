## Claudeを活用してピアノWebアプリを開発した方法

https://jcurcioconsulting.com/posts/how-i-used-claude-code-to-write-a-piano-web-app

**Original Title**: How I Used Claude Code to Write a Piano Web App

著者はClaude Maxをゼロから活用してRailsでピアノWebアプリを開発し、その具体的なプロセスとAIコーディングの効率性、そして改善点を通じて生成AIの実用性を検証した。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 100/100 | **Annex Potential**: 94/100 | **Overall**: 72/100

**Topics**: [[AIコーディング, Claude, Web開発, Ruby on Rails, プロンプトエンジニアリング]]

筆者は、OpenAIのツールを一年間使用した後、Claude Maxサブスクリプションを利用してワークフローを強化するため、ゼロからピアノWebアプリを開発するプロジェクトに着手した。これは、Claudeの実力を試すための実践的な実験である。

まず、空のRailsアプリケーションから開始し、ユーザーが楽曲を録音できる機能（「recordings」と「notes」テーブルを含む）と、録音を再生できる`/play/:id`エンドポイントの作成をClaudeに指示した。この最初のプロンプトだけで、シンプルなUI、ノート再生のためのJavaScript、適切なデータベースマイグレーション、ルート、コントローラー、モデルなど、最終製品の90%が生成されたことに著者は驚きを隠せなかった。

次に、いくつかの改善と機能追加を行った。録音に名前を付けられる機能、録音完了後に名前入力オプションを表示するUXの改善、GitHubリポジトリへのリンクとOctocatロゴのフッターへの追加（ロゴのSVGファイルも生成）、そして録音IDの推測を防ぐためのハッシュによるアクセス制御などだ。途中で発生した保存エラーもClaudeに修正させ、再生ページのURLを簡単に共有できるボタンも追加させた。最後に、ノートの押下時間を記録し、再生時にオリジナルの演奏を忠実に再現できるよう機能強化を行った。

開発中に、Claudeが生成したコードにいくつか理想的ではない点（フッターのコードが各ビューで繰り返される、アクセス制御の命名など）や、モバイルでの音声再生の問題（解決に至らず）があったものの、著者は今回のプロトタイプに非常に満足している。この経験を通じて、著者は生成AIが単なるコードアシスタンスツールを超え、日々のコーディング作業に大きく貢献できると確信した。特に、UIやJavaScriptの機能構築においてClaudeがその真価を発揮したと述べている。