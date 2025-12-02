## Codex CLIとBright Data MCPの連携でInstagramとGoogle Mapのデータを収集してみた

https://qiita.com/AI_Beginner_Note/items/939cc4c80a22188747cd

Codex CLIとBright Data The Web MCPを連携させることで、動的なWebサイトからのデータ収集が格段に安定し、LLMを活用したデータ分析の可能性が広がります。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 85/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[Webスクレイピング, LLMエージェント, データ収集, Bright Data, API連携]]

この記事は、OpenAIが提供するコーディングエージェント「Codex CLI」と、強力なWebスクレイピングツール「Bright Data The Web MCP」を連携させ、動的なWebサイトから安定してデータを収集する方法を解説しています。著者は、ChatGPT PlusとCodexを積極的に活用し、Web上の最新情報に基づいたデータ分析に取り組む中で、Codexの標準的なWeb検索機能が動的サイトのスクレイピングやCAPTCHA処理に課題があることを指摘しています。

この課題を解決するために、著者はBright Data The Web MCPに注目。このサービスは、月間5,000リクエストの無料枠を提供し、強力なWeb Unlocker機能によってサイトブロックを回避しながら、InstagramやGoogle Mapのような動的サイトからのデータ収集を可能にします。特に、`scrape_as_markdown`ツールにより、抽出したデータをLLMが処理しやすい綺麗な形式で得られる点が大きなメリットとして強調されています。また、有料のProモードではXやTikTok、Instagram向けの60種類以上の専用ツールが利用でき、複数のAPI申請の手間を省ける点も実用性が高いと述べています。

具体的な連携手順としては、まずNode.js環境下でCodex CLIとOpenAI APIキーを設定。次に、`npm install -g @brightdata/mcp`でBright Data MCPサーバーをインストールし、Bright DataのAPIキーを環境変数に設定してサーバーを起動します。最後に、`~/.codex/config.toml`ファイルにBright Data MCPサーバーの設定を追加し、APIキーとProモードの環境変数を渡すことで、Codex CLIからBright Data MCPを呼び出せるようになります。

テストとして、Codexの標準機能では困難だったInstagramの動画コメントやGoogle Mapの店舗情報（店名、評価、住所、口コミ）の取得を試みた結果、Bright Data MCPの連携により、Instagramのコメントは綺麗に取得でき、Google Mapの口コミも一部取得に成功したと報告されています。

著者はこの連携により、LLMがリアルタイムのWebデータにアクセスし、Webスクレイピングやブラウザ操作を自動で実行できる強力なワークフローが構築できると結論付けています。これにより、Codexの自然言語による操作とBright Dataの高度なデータ取得機能が組み合わさり、今まで収集が困難だったデータも手に入れられるようになり、データ分析の可能性が大きく広がると主張しています。具体的なデータ分析例は今後の続編で紹介される予定です。