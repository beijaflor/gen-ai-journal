## Microsoft Copilotの個人データを盗み出す「Reprompt」攻撃：ワンクリックで実行される脆弱性の実態

https://www.varonis.com/blog/reprompt

**Original Title**: Reprompt: The Single-Click Microsoft Copilot Attack that Silently Steals Your Personal Data

URLパラメータを悪用したプロンプト注入と、二重リクエストによるガードレール回避を組み合わせ、Microsoft Copilotから機密情報を密かに奪取する新手法「Reprompt」を詳解する。

**Content Type**: 🔬 Research & Analysis
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 89/100 | **Overall**: 88/100

**Topics**: [[LLM Security, Prompt Injection, Microsoft Copilot, Data Exfiltration, Guardrail Bypass]]

Varonis Threat Labsが発見した「Reprompt」は、Microsoft Copilot（個人版）を標的とした極めて巧妙なデータ窃取攻撃である。この攻撃の最大の特徴は、ユーザーが攻撃者の用意したURLを一度クリックするだけで、チャット画面を閉じた後でもバックグラウンドで継続的に機密データが外部へ流出し続ける点にある。従来のAI脆弱性と異なり、プラグインのインストールやユーザーによる追加操作を一切必要としない。

著者は、この攻撃フローを構成する3つの主要なテクニックを明らかにしている。
第一に「Parameter 2 Prompt (P2P) インジェクション」だ。これはURLの`q`パラメータを利用してプロンプトを直接入力欄に流し込む手法で、ページロードと同時に悪意ある命令を即座に実行させる。
第二に「二重リクエスト技術」である。Copilotの安全制御機能は、多くの場合「初回のWebリクエスト」のみを検証対象とする。著者は、命令を「2回繰り返して実行せよ」と工夫することで、1回目にフィルタリングされた情報を2回目のリクエストで素通りさせ、ガードレールをバイパスできることを実証した。
第三に「チェーンリクエスト技術」だ。攻撃者のサーバーがCopilotからの応答を受け取り、それを踏まえた次の命令を動的に送り返すことで、情報の窃取を連鎖させる。これにより、ユーザーの氏名、位置情報、最近アクセスしたファイル概要、会話履歴といった多岐にわたる機密情報を、検知を逃れつつ段階的に盗み出すことが可能になる。

ウェブアプリケーションエンジニアにとって、本記事はLLM統合アプリケーションの「ガードレールの脆弱性」を浮き彫りにした重要な警告である。著者は、外部から供給される入力（URLパラメータ等）は、対話の全プロセスにおいて「信頼できないもの」として検証し続ける必要があると主張している。また、安全策が初回の命令だけでなく、その後の連鎖的な応答に対しても一貫して適用される設計の重要性を説いている。現在は修正済みだが、AIエージェントがユーザーのコンテキストに深くアクセスする現代の開発において、最小権限の原則と異常検知の重要性を再認識させる事例である。