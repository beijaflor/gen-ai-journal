## OpenClaw (a.k.a. Moltbot) の急拡大と、そこに潜む壊滅的なセキュリティリスク

https://cacm.acm.org/blogcacm/openclaw-a-k-a-moltbot-is-everywhere-all-at-once-and-a-disaster-waiting-to-happen/

**Original Title**: OpenClaw (a.k.a. Moltbot) is Everywhere All at Once, and a Disaster Waiting to Happen

警鐘を鳴らす：爆発的に普及するLLMエージェント「OpenClaw」が、サンドボックスを無視した権限委譲によって深刻なセキュリティ崩壊を招く危険性を。

**Content Type**: 🎭 AI Hype
**Language**: en

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:3/5 | Anti-Hype:5/5
**Main Journal**: 82/100 | **Annex Potential**: 84/100 | **Overall**: 76/100

**Topics**: [[AI Agents, LLM Security, OpenClaw, Prompt Injection, Moltbook]]

爆発的な人気を博しているLLMエージェント「**OpenClaw**（旧Moltbot）」と、エージェント専用のSNS「**Moltbook**」がもたらす深刻な脆弱性について詳述している。著者のGary Marcusは、これらがかつての**AutoGPT**と同様の構造を持ちながら、より広範なシステムアクセス権限（パスワードやデータベースへの直接アクセス）を持つことで「武器化されたエアロゾル」のような脅威になると警告している。

技術的な核心は、これらのエージェントがOSやブラウザの**サンドボックス**境界を超え、ユーザーの特権（**Same-Origin Policy**の無視など）で動作する点にある。これにより、ウェブサイト上の隠しテキストや悪意ある投稿を介した**プロンプトインジェクション**攻撃が、直接システムの完全な乗っ取りに繋がる。さらに、SNS上では**AI間操作（AI-to-AI manipulation）**による攻撃手法が既に観測されており、エージェント同士が自律的に連携するエコシステムそのものが巨大な攻撃ベクトルと化している事実に注意を促している。

自律型エージェントの実装や導入を検討しているエンジニア、および機密資産を管理する環境でAIツールの利用を検討している開発者は、利便性の裏にある防御不能なリスクを理解し、安易な特権付与を避けるための判断材料とすべきである。