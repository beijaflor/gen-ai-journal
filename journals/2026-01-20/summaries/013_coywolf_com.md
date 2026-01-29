## エージェンティックAIの危険性：Signal経営陣がセキュリティと信頼性の欠如を警告

https://coywolf.com/news/productivity/signal-president-and-vp-warn-agentic-ai-is-insecure-unreliable-and-a-surveillance-nightmare/

**Original Title**: ‘Signal’ President and VP warn agentic AI is insecure, unreliable, and a surveillance nightmare

警告する：エージェンティックAIの無謀なOS統合がもたらすセキュリティ上の欠陥と、多段階タスクにおける壊滅的な信頼性の低さを論理的に解き明かす。

**Content Type**: 🎭 AI Hype
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:3/5 | Anti-Hype:5/5
**Main Journal**: 88/100 | **Annex Potential**: 89/100 | **Overall**: 84/100

**Topics**: [[AI Agents, Cybersecurity, Privacy, Windows Recall, LLM Reliability]]

Signalの経営陣であるMeredith Whittaker氏とUdbhav Tiwari氏は、第39回Chaos Communication Congress（39C3）において「AI Agent, AI Spy」と題した講演を行い、現在のAIエージェントの実装が「監視の悪夢」であり、技術的に極めて信頼できないものであると断じた。彼らが最も危険視しているのは、AIエージェントがユーザーの代わりに行動するために、個人の機密データへ広範囲にアクセスし、その行動履歴を非暗号化状態で保存する構造だ。

特にMicrosoftの「Windows Recall」を例に挙げ、数秒ごとのスクリーンショット撮影とOCR処理、そしてセマンティック解析によって作成される「デジタルライフの完全な履歴データベース」の危うさを指摘した。このデータベースはローカルに保存されるとはいえ、オンライン攻撃によるマルウェアや、巧妙に隠されたプロンプトインジェクション攻撃によって容易にアクセスされる可能性がある。Tiwari氏によれば、これは通信の「エンドツーエンド暗号化（E2EE）」を根本から無効化するものであり、Signal側で画面キャプチャを防止するフラグを導入しても、それは一時的な対症療法に過ぎないと述べている。

さらにWhittaker氏は、AIエージェントの「自律性」に対する期待が、数学的な現実と乖離している点を厳しく批判した。AIモデルは本質的に確率的（Probabilistic）であり、確定的な動作を保証できない。彼女が提示したシミュレーションによれば、各ステップの精度が95%という現状では到達困難な高水準であっても、10ステップのタスクを完遂できる確率は約59.9%に留まり、30ステップでは約21.4%まで低下する。現実的な90%の精度であれば、30ステップ後の成功率はわずか4.2%となり、複雑な業務を自律的にこなすには程遠い。著者は、現在の最高水準のモデルですらエージェントとしてのタスク遂行に70%の確率で失敗している現状を挙げ、利便性ばかりを強調する業界のハイプ（過剰な宣伝）を強く牽制している。

結論として、Signal経営陣は「無謀な展開の停止」「デフォルトでのオプトアウト設定」「徹底した透明性と監査可能性」を業界に要求した。エンジニアにとって、本記事はAIエージェントをシステムに組み込む際のセキュリティ設計や、多段階LLMワークフローにおけるエラー率の累積という実務的な制約を再考するための重要な視点を提供している。