# Editorial Plan - Journal 2026-03-21

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Identified Themes

### Theme 1: 「認知的負債」の正体：AIが生成したコードを人間が理解できなくなる日

**Articles (IDs):** 260, 023, 012, 022, 019, 037

- 260: Cognitive Debt (⭐ Standout)
- 023: Comprehension Debt - Addy Osmani
- 012: コード生成は生産性ではない
- 022: AIはソフトウェアエンジニアリングを簡素化していない
- 019: 認知的負債からの防御 — ドメインの死守
- 037: 新機能追加のために3,000行削除した話

**Theme Introduction (2-3 sentences in Japanese):**
AIコーディングツールの普及は「認知的負債（Cognitive Debt）」という深刻な問題を浮き彫りにしている。コードは動いている、テストも通っている、だが誰もその仕組みを理解していない——この見えない負債が、チームのメンタルモデルを内側から崩壊させている。今週は複数の論者が独立してこの問題に警鐘を鳴らし、「オニオンアーキテクチャ的な境界線」から「3,000行削除によるリファクタリング」まで、具体的な処方箋が提示された。

**Editorial Notes:**
- Key insights: ⭐ Standout記事260（Cognitive Debt）がテーマのアンカー。「技術的負債」との違いを明確に。
- Connections: Addy Osmani（023）がGoogleの視点から同じ現象を解説。037が「実際にどう返済するか」の具体例。
- Challenges: 抽象的な議論に終わらせず、実務者への処方箋として着地させる。

---

### Theme 2: 仕様が新しいコードである：SDD・IDD・ADRが描く「書かない開発」の未来

**Articles (IDs):** 054, 068, 050, 040, 067, 042

- 054: Beyond Code Review（O'Reilly）— 仕様駆動開発（SDD）
- 068: 意図駆動開発（IDD）— Why/Whatに集中
- 050: specre — 1ファイル1振る舞いのSpec Card
- 040: contextlint — ドキュメント整合性の静的解析
- 067: 生成AI時代のドキュメント基盤（7年運用の知見）
- 042: cc-sdd — ストーリーテストの自動組み込み

**Theme Introduction (2-3 sentences in Japanese):**
「コードレビューの先」にあるのは、仕様そのものの定義と検証に人間が集中する世界だ。O'Reillyが仕様駆動開発（SDD）への移行を提唱し、国内からは「意図駆動開発（IDD）」やspecre、contextlintといった具体的なツール群が続出。仕様を書き、仕様を検証し、コードはAIに任せる——このパラダイムシフトが今週、実装レベルで具体化した。

**Editorial Notes:**
- Key insights: SDDの理論（054）→IDDへの発展（068）→ツール化（050, 040）→実運用（067, 042）と成熟度の段階がある
- Connections: 仕様⇄コードの双方向トレーサビリティという共通テーマ
- Challenges: ツール間の違いと使い分けを明確にする

---

### Theme 3: ハーネスエンジニアリング実践録：AIエージェントを「仕組み」で制御する4つの現場

**Articles (IDs):** 048, 057, 059, 016, 055, 056

- 048: Harness Engineering ベストプラクティス2026（nyosegawa）
- 057: ハーネスで縛れ、AIに任せろ（GMO）
- 059: SREはAgentic Engineeringのハーネスになれるか？
- 016: AI生成コードのリリース安全基盤（ACES）
- 055: プッツンした人間がAIにダメ出しし続けたらflakyテストが全滅した（DeNA）
- 056: AIコードレビューを「単一責任の原則」で育てた話（グロービス）

**Theme Introduction (2-3 sentences in Japanese):**
AIエージェントの実力を引き出す鍵は、プロンプトの改善ではなく「仕組み（ハーネス）」にある。PostToolUse Hookによるミリ秒単位の品質強制、Feature Flagを使った段階的ロールアウト、SREの知見を機械可読にする取り組みまで——今週、日本のプロダクション現場から、AIを構造で制御する具体的な実践報告が相次いだ。

**Editorial Notes:**
- Key insights: 「プロンプトで指示→仕組みで強制」へのパラダイムシフトが核心
- Connections: DeNA（055）の「70の分身」運用とグロービス（056）の単一責任原則がSRE（059）の理論を裏付ける
- Challenges: 各企業の取り組みの違いと共通原則を整理する

---

### Theme 4: Stripeの週1,300PR、DeNAの95%効率化：AI駆動開発のスケーリング最前線

**Articles (IDs):** 136, 058, 063, 008, 017

- 136: Stripeの「Minions」が週1,300PRを自律生成する仕組み
- 058: DeNA南場会長「AIにオールイン」1年の進捗と誤算
- 063: Claude Code × GitHubでプロダクトマネジメントを再設計
- 008: CODEX/Antigravity/Claude Codeに同じアプリを作らせて比較
- 017: 私のMacには6人の社員がいる

**Theme Introduction (2-3 sentences in Japanese):**
AIコーディングエージェントは、もはや個人の生産性ツールではない。Stripeでは自律型エージェント「Minions」が毎週1,300件以上のPRを処理し、DeNAは特定業務で95%の効率化を達成した。しかしDeNAの南場会長が認めた「人材シフトの難航」が示すように、AI導入の本当のボトルネックは技術ではなく組織にある。

**Editorial Notes:**
- Key insights: 個人→チーム→組織スケールでのAI活用の段階的拡大
- Connections: Stripe（136）のBlueprints構造とDeNA（058）の組織課題が好対照
- Challenges: 成功事例だけでなく、組織的な課題にも正直に踏み込む

---

### Theme 5: MCPの光と影：66%が脆弱、プロンプトインジェクションからサンドボックス脱出まで

**Articles (IDs):** 006, 014, 007, 064, 046, 043

- 006: MCPサーバは安全か？ツールポイズニング・RCE・サンドボックス脱出の実例と対策
- 014: AIエージェントのセキュリティ：プロンプトインジェクションが実害をもたらす時代
- 007: CONTRIBUTING.mdへのプロンプトインジェクションでPRの50%がAIボットだと判明
- 064: AIコーディングエージェントに「rm -rf」を実行させるまでの手法と対策
- 046: Snowflake Cortex AIのサンドボックス回避脆弱性
- 043: AgentArmor — 8層防御セキュリティフレームワーク

**Theme Introduction (2-3 sentences in Japanese):**
AIエージェントが標準プロトコルMCPで連携する時代、そのセキュリティは壊滅的に脆弱だ。公開MCPサーバの66%に問題が確認され、CONTRIBUTING.mdへのプロンプトインジェクションでPRの半数以上がAIボットだと判明し、Snowflakeではサンドボックスを破られ機密データが窃取可能な脆弱性が発見された。攻撃と防御の両面から、エージェント時代のセキュリティ設計を緊急に再考する。

**Editorial Notes:**
- Key insights: 理論的リスクではなく、実際に起きた攻撃事例の集中
- Connections: 攻撃手法（006, 007, 046）→被害事例→防御フレームワーク（043, 064）の流れ
- Challenges: 恐怖を煽るだけでなく、実行可能な防御策を提示する

---

### Theme 6: OpenAIのAstral買収とAnthropic Institute設立：AI企業が「コーディングの未来」と「社会の未来」に賭ける理由

**Articles (IDs):** 110, 135, 130, 131, 132, 102_alt

- 110: The Anthropic Institute 設立（⭐ Standout）
- 135: 8万1千人の声から見るAIへの期待と懸念（⭐ Standout）
- 130: AstralがOpenAIに加入
- 131: OpenAIがAstralの買収を発表
- 132: OpenAIのIPOへの新たな焦点

**Theme Introduction (2-3 sentences in Japanese):**
今週、AI業界の地殻変動が2つ同時に起きた。OpenAIはPythonツールチェーンの雄Astralを買収し「Codex」を開発ワークフロー全体の覇者にする野心を示し、AnthropicはAIの社会的影響を研究する「The Anthropic Institute」を設立した。片や開発者エコシステムの囲い込み、片や社会的責任の引き受け——両社の戦略の違いが、AI産業の未来を占う分水嶺となっている。

**Editorial Notes:**
- Key insights: ⭐ 110（Anthropic Institute）と135（81k調査）がStandout。企業戦略×社会的責任の交差点
- Connections: OpenAIのIPO志向（132）vsAnthropicの研究志向が好対照
- Challenges: 企業PR的な内容にならず、批判的分析を加える

---

### Theme 7: 「判断」こそ人間の価値：AIが無料化する世界でエンジニアに残るもの

**Articles (IDs):** 004, 015, 013, 021, 032, 053

- 004: ソフトウェア開発者は決して滅びない（Marmelab CEO）
- 015: AIは専門知識を不要にしたのではなく、その価値を高めた
- 013: AI支援コーディングの現状：プロフェッショナルの実体験
- 021: AIツールの普及とCS基礎の重要性（HN議論）
- 032: AI時代のプログラマーの行方（Anil Dash）
- 053: プログラミングの「2つの世界」

**Theme Introduction (2-3 sentences in Japanese):**
AIがコード生成を「無料」にした時、エンジニアの価値はどこに残るのか。MarmelabのCEOは「仕様こそ新しいコード」と宣言し、Anil Dashは「手仕事の喜び」の喪失を嘆き、HNでは「CSの基礎を学ぶ意欲が失われている」という悲鳴が上がった。楽観と悲嘆が入り混じる今週の議論から浮かび上がるのは、「判断力」と「信頼」こそがAIには代替できない人間固有の資産であるという収束点だ。

**Editorial Notes:**
- Key insights: 「判断（Judgment）」と「信頼（Trust）」が共通キーワード
- Connections: 004の「仕様=新コード」とTheme 2のSDDが呼応
- Challenges: 議論の多角性を活かしつつ、安易な「人間が勝つ」結論を避ける

---

## Highlight Draft ("今週のハイライト")

**Main Narrative Arc:**

今週のAI×コーディング界は、「加速」と「制御」の二律背反を軸に回っている。

一方では、Stripeの自律型エージェントが週1,300件のPRを出荷し、DeNAが95%の業務効率化を達成するなど、AIエージェントの組織レベルでのスケーリングが現実のものとなった。OpenAIのAstral買収は、AIが単なるコード生成を超え、開発ワークフロー全体を支配しようとする野心を示している。

しかしその加速の裏側で、「認知的負債」という新たな危機が浮上した。AIが書いたコードを誰も理解していない——Addy Osmaniの警鐘、Cognitive Debtの概念、そして「3,000行を削除して初めて前進できた」という実体験が、コード生成の「量」ではなく「理解」が真のボトルネックであることを突きつけている。

この矛盾への処方箋として、今週は2つの方向性が鮮明になった。第一は「仕様駆動開発（SDD）」への移行。O'Reillyが提唱し、specreやcontextlintといったツールが実装した「人間は仕様を書き、AIがコードを書く」というパラダイムだ。第二は「ハーネスエンジニアリング」。プロンプトの改善ではなく、Hooks、Feature Flag、SLOといった「仕組み」でAIの出力を構造的に制御するアプローチが、日本の複数の現場から報告された。

そしてセキュリティの面では、MCPサーバの66%に脆弱性が確認され、プロンプトインジェクションやサンドボックス脱出の実例が相次ぎ、「自律的に動くAI」を安全に運用するための制度設計が急務であることが明らかになった。

**Key Points to Cover:**
1. AIエージェントのスケーリングが組織レベルで実現した一方、認知的負債が新たなリスクとして浮上
2. 「仕様駆動」と「ハーネスエンジニアリング」という2つの処方箋の具体化
3. MCPセキュリティの壊滅的な現状と、エージェント時代のセキュリティ設計の緊急性
4. OpenAI vs Anthropicの戦略分岐：エコシステム囲い込み vs 社会的責任

**Cross-Cutting Insights:**
- 「コードの量」から「理解の深さ」へ——開発生産性の定義自体が転換点にある
- AIの「自律性」が高まるほど、「ハーネス（制約）」の設計が決定的に重要になる

---

## Curation Signal Summary

**⭐ Standout Articles Used:**
- 110 → Theme 6 (Lead) — Anthropic Institute設立
- 135 → Theme 6 (Supporting, upper weight) — 81k interviews
- 170 → Annex候補 — RakutenAI-3.0 LoRA検証
- 260 → Theme 1 (Lead) — Cognitive Debt

**👍 Upvoted Articles Used:**
- 189 → Theme 2 (Supporting) — Coding Agent時代のドキュメント管理

**👎 Downvoted Articles:**
- 009 → Annex/Omit — Google Antigravity入門
- 099 → Annex/Omit
- 102 → Annex/Omit — MCP vs REST
- 105 → Annex/Omit — Prompt Injection Attacks (WorkOS)
- 127 → Annex/Omit — Yann LeCun論文
- 166 → Annex/Omit — Codex Best Practice
- 213 → Annex/Omit — Fast, Good, and Cheap
- 269 → Annex/Omit — Anthropic社員のClaude Code活用術

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: 18-25 articles across 7 themes
- Annex Journal: Remaining articles across 5-6 themes

**Article Count by Theme (Planned):**
- Theme 1 (認知的負債): 6 articles
- Theme 2 (仕様駆動開発): 6 articles
- Theme 3 (ハーネスエンジニアリング): 6 articles
- Theme 4 (スケーリング最前線): 5 articles
- Theme 5 (MCPセキュリティ): 6 articles
- Theme 6 (企業戦略): 5 articles
- Theme 7 (人間の価値): 6 articles

**Total Planned for Main:** ~40 articles (to be narrowed to 22-25 during STEP_04)
**Remaining for Annex:** ~40-50 articles

*Note: Current article counts per theme exceed the 18-25 total target. STEP_04 will narrow each theme to 3-4 articles based on signal strength and editorial judgment.*

---

## Review Notes (Human Editor)

**Date Reviewed:**
**Reviewer:**

**Changes Made:**
-

**Approval:** ✅ APPROVED

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)
