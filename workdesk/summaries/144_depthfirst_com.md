## 1クリックでRCEを実行しMoltbotのデータとキーを窃取：脆弱性CVE-2026-25253の解説

https://depthfirst.com/post/1-click-rce-to-steal-your-moltbot-data-and-keys

**Original Title**: 1-Click RCE To Steal Your Moltbot Data and Keys (CVE-2026-25253)

人気のAIアシスタントOpenClawに存在する、URLパラメータ経由で認証トークンを奪取し任意コード実行（RCE）を可能にする致命的な脆弱性を詳述する。

**Content Type**: 🔬 Research & Analysis
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 84/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[OpenClaw, RCE, 脆弱性, CSWSH, AIエージェントセキュリティ]]

本記事は、10万人以上の開発者が利用するオープンソースAIアシスタント「**OpenClaw**（旧Moltbot）」で発見された、1クリックでフル・リモートコード実行（**RCE**）を許す深刻な脆弱性（**CVE-2026-25253**）の技術解説です。

脆弱性の核心は、URLのクエリパラメータとして渡された`gatewayUrl`を検証なしに保存し、即座に接続を試みるロジックにあります。接続時には**authToken**が自動的に付与されるため、悪意あるURLを踏ませるだけで認証情報が攻撃者に流出します。著者はさらに、**Cross-Site WebSocket Hijacking (CSWSH)** を併用してlocalhost制限を突破し、API経由で「実行時のユーザー確認」や「**サンドボックス**隔離」を無効化する攻撃チェーンを実証しました。最終的に、被害者のホストOS上で任意の**bash**コマンド実行が可能になります。

AIエージェントが「God Mode（高権限）」を持つ現代において、設定情報のインジェクションがいかに致命的かを示す好例です。**OpenClaw**ユーザーは直ちに v2026.1.24-1 以降へアップデートし、トークンを再生成する必要があります。AIエージェントのWebインターフェースや設定の永続化ロジックを設計する開発者は、信頼できない入力が引き起こす連鎖的なリスクを確認すべきです。