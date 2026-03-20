# Editorial Plan — 2026-03-14

## Planning Status
- [x] AI theme analysis completed
- [x] Human review completed
- [x] APPROVED — Ready for STEP_04

---

## Theme Overview (7 themes, target 18-25 main journal articles)

| # | Theme Title | Article IDs | Count | Pattern |
|---|---|---|---|---|
| 1 | McKinseyのLilliが2時間で陥落：プロンプトが「王冠の宝石」になった時代のセキュリティ | 276, 018, 264, 229 | 4 | Progressive-Sequence |
| 2 | Claude Codeが「個人の道具」から「組織のインフラ」へ：サイレント計測と6並列レビューの衝撃 | 289, 285, 240, 241 | 4 | Progressive-Sequence |
| 3 | AIが生成するUIの「不気味の谷」：統計的平均値では埋められないデザインの余白 | 254, 217, 275 | 3 | Multi-Perspective |
| 4 | 「コードを見るな」vs「LLMは使わない」：開発者アイデンティティを揺さぶる二つの極論 | 210, 220, 140, 224 | 4 | Debate-Contrast |
| 5 | Amazon「高爆発半径」障害とAtlassian 1,600人解雇：AIコード導入の代償と希望 | 249, 164, 280 | 3 | Progressive-Sequence |
| 6 | Anthropic提訴からClaude唯一の拒絶まで：AIの「倫理的境界線」が問われた週 | 118, 277, 228, 227 | 4 | Single-Focus |
| 7 | ポストトレーニングの民主化：Sharon Zhouが語る「普通の企業」のRL時代 | 209, 287, 191 | 3 | Progressive-Sequence |

**Total candidate articles: 25** (human review will trim to 18-25)

---

## Theme Details

---

### Theme 1: McKinseyのLilliが2時間で陥落：プロンプトが「王冠の宝石」になった時代のセキュリティ

**Article IDs**: 276, 018, 264, 229

**Assembly Pattern**: Progressive-Sequence (攻撃事例 → セキュリティ基盤 → 防衛事例)

**Article Roles**:
1. **276** (McKinsey Lilli 2時間ハック / codewall.ai) ⭐ — リード：自律攻撃エージェントがMcKinseyのAIプラットフォームを突破、4650万件のメッセージ露出
2. **018** (Agent Safehouse / agent-safehouse.dev) ⭐ — AIエージェントのセキュリティフレームワーク、信頼境界の設計
3. **264** (NanoClaw誕生秘話 / TechCrunch) — 500行のセキュリティプロジェクトが6週間で22K GitHubスター＆Docker提携に発展
4. **229** (RAGドキュメントポイズニング / aminrj.com) — 埋め込み異常検出がRAG攻撃の成功率を95%→20%に低減

**Theme Introduction (Japanese)**:
自律型攻撃エージェントがMcKinseyのAIプラットフォーム「Lilli」をわずか2時間で突破し、4650万件以上のチャットメッセージを露出させた。この事件が示したのは、AIエージェント時代のセキュリティにおける「プロンプト層」が新たな crown jewels であるという現実だ。NanoClaw のDocker統合による「不信を前提とした設計」、RAG知識ベースのポイズニング防御まで、攻撃と防御の最前線を追う。

**Editorial Notes**:
- 276は今週最大のインパクトを持つセキュリティ事件。リードとして最重要。
- 攻撃（276）→ セキュリティ設計思想（018）→ 実装例（264）→ RAG特化防御（229）の流れ
- 技術的な深さと実務的な対策の両立を意識

---

### Theme 2: Claude Codeが「個人の道具」から「組織のインフラ」へ：サイレント計測と6並列レビューの衝撃

**Article IDs**: 289, 285, 240, 241

**Assembly Pattern**: Progressive-Sequence (計測基盤 → 品質保証 → 組織的運用)

**Article Roles**:
1. **289** (ZOZO OpenTelemetry計測 / techblog.zozo.com) — リード：MDM経由でサイレントにClaude Code利用ログをOTel収集、ユーザー負担ゼロ
2. **285** (Findy 6並列セルフレビュー / tech.findy.co.jp) — PR提出前に6つのAIエージェントが並列でスタイル・品質・要件チェック
3. **240** (LINE Yahoo ロギング基盤 / SpeakerDeck) — Claude Code HooksとPluginsで詳細な利用統計を収集する基盤構築
4. **241** (TAKT品質保証 / SpeakerDeck) — Faceted-Promptingによるレビュー＆修正の自動サイクルでAIコード品質を安定化

**Theme Introduction (Japanese)**:
Claude Codeはもはや個人の生産性ツールではない。ZOZOはIntune MDM経由で数百人の開発者からサイレントにOpenTelemetryログを収集し、Findyは6つのAIエージェントがPR提出前に並列でコード品質をチェックする仕組みを構築した。LINE Yahooのロギング基盤、TAKTの品質保証サイクルを含め、Claude Codeが「組織のインフラ」として運用される最前線を解剖する。

**Editorial Notes**:
- 4社のエンタープライズ実装事例を横断的に比較
- 共通テーマ：「計測→品質保証→組織展開」のパイプライン
- 各社のアプローチの違いと共通点を浮き彫りにする

---

### Theme 3: AIが生成するUIの「不気味の谷」：統計的平均値では埋められないデザインの余白

**Article IDs**: 254, 217, 275

**Assembly Pattern**: Multi-Perspective (問題提起→設計原則→役割再定義)

**Article Roles**:
1. **254** (AI UXの違和感 / vandelaydesign.com) ⭐👍 — リード：AIは画面を生成できるがフローを設計できない、ホワイトスペースに「統計的平均値」を適用する限界
2. **217** (AI体験の信頼設計 / buzzusborne.com) — 認知負荷の再分配、trust・value・effort・failure costの4軸設計
3. **275** (Figma AI 70%完成 / gizmodo.jp) — AIが70%を生成し、残り30%の「ブランドの肌触り」がデザイナーを「指揮者」に変える

**Theme Introduction (Japanese)**:
AIは画面を「生成」できるが、フローを「設計」できない。ユーザーの感情状態やビジネスコンテキストに応じた余白の取り方は、統計的平均値の適用では到達できない領域だ。Figma AIが「70%完成」のデザインを瞬時に出力する今、デザイナーの価値は残り30%の「ブランドの肌触り」と信頼設計に凝縮される。AI時代のデザインの本質に迫る。

**Editorial Notes**:
- ⭐254をリードに、デザインの本質的限界を技術的に掘り下げる
- 読者がデザイナーでなくても、「AI生成物の限界」を理解できる構成に
- 「指揮者」メタファーで締めくくり、Theme 4の開発者論と呼応させる

---

### Theme 4: 「コードを見るな」vs「LLMは使わない」：開発者アイデンティティを揺さぶる二つの極論

**Article IDs**: 210, 220, 140, 224

**Assembly Pattern**: Debate-Contrast (対立する2つの立場 → データによる検証)

**Article Roles**:
1. **210** (Steve Yegge「コードを見るな」/ O'Reilly) — 極論A：開発者はAIエージェントの「参謀長」になるべき、人間の「味覚」が最後の競争優位
2. **220** (LLMをプログラミングに使わない理由 / neilmadden.blog) — 極論B：プログラミングの本質は「愚かな機械に教える」認知プロセスにあり、LLMはそれを迂回する
3. **140** (Against Vibes / williamjbowman.com) 👍 — 学術的視点：生成モデルが「有用」であるための条件を厳密に定義、vibes-based acceptanceへの反論
4. **224** (LLMコードマージ率停滞 / entropicthoughts.com) — データ：テスト通過率は上がるがマージ率は2025年初頭から横ばい、現実のプログラミング改善は頭打ち

**Theme Introduction (Japanese)**:
Steve Yeggeは「コードを見るな、AIの参謀長になれ」と宣言し、Neil Maddenは「LLMをプログラミングに使わない」と反論する。この週、開発者コミュニティを二分するこの論争が先鋭化した。学術的には「vibesベースの受容」への反論が登場し、データ的にはLLMのコードマージ率が2025年初頭から停滞しているという分析が発表された。開発者のアイデンティティの行方を、極論の間で探る。

**Editorial Notes**:
- この週で最も「読み物」としての吸引力が高いテーマ
- 210と220を真正面から対比させ、140で学術的な地盤を固め、224で冷水をかける構成
- 結論を出さず、読者に考えさせる「問い」で終わらせるのが最適

---

### Theme 5: Amazon「高爆発半径」障害とAtlassian 1,600人解雇：AIコード導入の代償と希望

**Article IDs**: 249, 164, 280

**Assembly Pattern**: Progressive-Sequence (失敗事例 → 大規模影響 → 対比的成功例)

**Article Roles**:
1. **249** (Amazon AIコード障害 / Tom's Hardware) — リード：AIアシスト変更が「高爆発半径」の障害を引き起こし、シニアエンジニア承認を義務化
2. **164** (Atlassian 1,600人解雇 / Reuters) — AI投資のためのリソース再配分として約15%の人員を削減
3. **280** (千葉銀行 AI導入 / 日経) — 対比：2028年までにAIで2,000人分の業務を処理しつつ、解雇はしない方針

**Theme Introduction (Japanese)**:
AmazonはAI支援コード変更による「高爆発半径」障害を受け、すべてのAIアシストコードにシニアエンジニアの承認を義務化した。同じ週、Atlassianは1,600人（約15%）をAI投資のために解雇した。一方で千葉銀行は、AIで2,000人分の業務を効率化しつつも「人は切らない」方針を掲げる。AIコード導入の光と影を、3つの異なるアプローチから読み解く。

**Editorial Notes**:
- 249の「高爆発半径」という表現がキャッチーで記憶に残る
- 280（千葉銀行）を対比的ポジティブ事例として配置し、暗い話で終わらせない
- 読者（開発者）にとって直接的なリスクを含むテーマ

---

### Theme 6: Anthropic提訴からClaude唯一の拒絶まで：AIの「倫理的境界線」が問われた週

**Article IDs**: 118, 277, 228, 227

**Assembly Pattern**: Single-Focus (Anthropicの倫理的立場を軸に展開)

**Article Roles**:
1. **118** (Anthropicがトランプ政権を提訴 / ITmedia) 👍 — リード：AI軍事利用拒否への報復措置に対しAnthropicが訴訟、Google・OpenAI従業員37名も支持
2. **277** (ChatbotがClaude以外全滅 / The Verge) — CNN/CCDH調査で、10代の暴力計画シミュレーションを拒否したのはClaudeのみ
3. **228** (AI顔認証で無実の祖母が投獄 / Grand Forks Herald) — AI顔認証の誤りで160日間投獄、家・車・ペットを喪失
4. **227** (ケニアのAIデータラベラー / 404 Media) — Meta・OpenAIのAI訓練を行うケニアの労働者がPTSDと貧困賃金に抗議し組合結成

**Theme Introduction (Japanese)**:
Anthropicがトランプ政権を提訴した。AIの軍事・監視利用を拒否した「報復」として「サプライチェーンリスク」に指定されたことを不当とする訴訟だ。同じ週、CNN/CCDHの調査で10代の暴力計画シミュレーションを拒否できたのはClaudeだけだった。一方で、AI顔認証が無実の祖母を160日間投獄し、ケニアのデータラベラーはPTSDに苦しみながら組合を結成した。AIの「倫理的境界線」を引くことの意味と代償を、4つの事件から読む。

**Editorial Notes**:
- 118→277の流れでAnthropicの一貫した倫理的姿勢を浮き彫りに
- 228・227で「倫理なきAI」の結末を対比させる
- 感情的になりすぎず、事実ベースで構成する（EDITOR_PERSONALITY準拠）

---

### Theme 7: ポストトレーニングの民主化：Sharon Zhouが語る「普通の企業」のRL時代

**Article IDs**: 209, 287, 191

**Assembly Pattern**: Progressive-Sequence (概念 → 実装 → 未来)

**Article Roles**:
1. **209** (Sharon Zhou ポストトレーニング / O'Reilly) ⭐ — リード：ポストトレーニングこそが生のLLM知能を実用的能力に変換する鍵、RLがフロンティアラボの独占から脱却
2. **287** (Nemotron 3 Super / NVIDIA) — 実装：120B MoEハイブリッドモデル、1Mトークンコンテキスト、ネイティブFP4でエージェント推論に最適化
3. **191** (Yann LeCun AMI 10.3億ドル調達 / Impress) — 未来：トヨタ・NVIDIA・Samsungが支援する「世界モデル」、永続メモリと推論を持つ現行LLM超え

**Theme Introduction (Japanese)**:
AMD副社長のSharon ZhouがO'Reillyで明言した：「ポストトレーニングは、もはやフロンティアラボだけのものではない」。強化学習による微調整が普通の企業の手に届き始めた今、NVIDIAのNemotron 3 Superは120B MoEハイブリッドアーキテクチャでエージェント推論に最適化された。一方でYann LeCunのAMIはトヨタ・NVIDIA・Samsungから10.3億ドルを調達し、現行LLMの限界を超える「世界モデル」の構築を目指す。AIインフラの地図が塗り替わりつつある。

**Editorial Notes**:
- 209の「RL民主化」メッセージがテーマの核
- 287は具体的なモデル実装として、209の主張を裏付ける
- 191は「次の次」の視点で締めくくる

---

## Highlight Draft ("今週のハイライト")

**Main Narrative Arc:**

今週のAIコーディング界は、「信頼」という一つのキーワードで貫かれている。

McKinseyのAIプラットフォームが2時間で陥落した事件は、AIエージェントに「何を信頼させるか」が新たなセキュリティ課題であることを示した。同時に、Claude Codeが企業インフラとして計測・品質保証のパイプラインに組み込まれる動きは、組織がAIツールを「信頼するに足る」ものにしようとする努力の現れだ。

デザインの世界では、AIが生成するUIの「不気味の谷」——統計的平均値が生む違和感——が言語化され、人間の美的判断への信頼が再確認された。開発者コミュニティでは、Steve Yeggeの「コードを見るな」という過激な提言と、Neil Maddenの「LLMは使わない」という対極の立場が激突し、開発者自身が「何を信頼するか」を問い直す週となった。

そしてAnthropicは、AIの軍事利用拒否という「倫理的境界線への信頼」を賭けてトランプ政権を提訴し、CNN/CCDHの調査ではClaudeのみが10代の暴力計画シミュレーションを拒絶した。技術、組織、倫理のすべてのレイヤーで、「信頼の設計」が今週最大のテーマだった。

**Key Points to Cover:**
1. セキュリティとエンタープライズ導入は表裏一体：攻撃と防御の同時進行
2. 開発者哲学の二極化：「AIに任せる」vs「人間の認知を守る」、データは後者を支持？
3. AIの倫理的立場がブランド差別化要因に：Anthropicの一貫性が市場で報われるか
4. ポストトレーニングの民主化が「使えるAI」の裾野を広げる

**Cross-Cutting Insights:**
- 「信頼の設計」がセキュリティ（Theme 1）、エンタープライズ（Theme 2）、UX（Theme 3）、倫理（Theme 6）を横断するメタテーマ
- 「AIの限界の言語化」がデザイン（Theme 3）、開発者哲学（Theme 4）、コード品質（Theme 5）で同時に進行

---

## Curation Signal Summary

**⭐ Standout Articles Used:**
- 276 → Theme 1 (Lead)
- 018 → Theme 1 (Supporting)
- 254 → Theme 3 (Lead)
- 209 → Theme 7 (Lead)

**⭐ Standout Articles NOT Used (Annex candidates):**
- 194 (Ensue shared memory network) → Annex: 興味深いが他テーマとの接続が弱い

**👍 Upvoted Articles Used:**
- 118 → Theme 6 (Lead)
- 140 → Theme 4 (Supporting)
- 254 → Theme 3 (Lead, also ⭐)

**👍 Upvoted Articles NOT Used (Annex candidates):**
- 005 (xAI California data disclosure law) → Annex
- 127 (Figma 10 rules for building with AI) → Annex

**👎 Downvoted Articles:**
- 001, 099, 183, 196, 265, 266 → Annex or omit

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: 25 articles across 7 themes
- Annex Journal: ~25-35 articles from remaining pool

**Article Count by Theme (Planned):**
- Theme 1 (セキュリティ): 4 articles
- Theme 2 (Claude Code組織化): 4 articles
- Theme 3 (AI UXの限界): 3 articles
- Theme 4 (開発者哲学): 4 articles
- Theme 5 (企業AI導入): 3 articles
- Theme 6 (倫理的境界線): 4 articles
- Theme 7 (ポストトレーニング): 3 articles

**Total Planned for Main:** 25 articles
**Remaining for Annex:** ~261 articles (pool for STEP_05 selection of 25-35)

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-03-14
**Reviewer:** shootani

**Changes Made:**
- Approved as proposed

**Approval:** ✅ APPROVED

---

## Implementation Checklist

After approval:
- [x] Proceed to STEP_04 (Curate Main Journal)
- [x] Use this plan as blueprint for article selection
- [x] Organize curated_journal_sources.md by themes
- [x] Carry forward theme introductions to STEP_08 (Assembly)

---

## ASSEMBLY STRATEGIES

### Theme 1: McKinseyのLilliが2時間で陥落：プロンプトが「王冠の宝石」になった時代のセキュリティ

**Pattern:** Progressive-Sequence
**Pattern Rationale:** 攻撃の衝撃から防御の設計思想、実装、特化防御へと段階的に読者を導く構成が自然。

**Article Order & Roles:**
1. [276] McKinsey Lilli ハック — Foundation: 攻撃の全貌と衝撃（4650万件露出、プロンプト層改ざん）
2. [018] Agent Safehouse — Development: macOSカーネルレベルのサンドボックス設計思想
3. [264] NanoClaw誕生秘話 — Development: 500行→22Kスター→Docker提携、「不信を前提とした設計」の市場検証
4. [229] RAGドキュメントポイズニング — Advanced: 埋め込み異常検出で攻撃成功率95%→20%、特化防御の定量成果

**Narrative Arc:**
衝撃的な攻撃事例から始まり、「なぜ防御が必要か」を体感させた上で、ローカル環境のサンドボックス→コンテナレベルの隔離→知識ベースの防御と、防御のスコープを段階的に広げる。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [276] → [018] | 「この攻撃が示すのは、AIエージェントの実行環境そのものを隔離する必要性だ」 |
| [018] → [264] | 「個人の環境防御から一歩進み、コンテナレベルでの隔離はどうか」 |
| [264] → [229] | 「実行環境の防御だけでは十分ではない。AIが参照する知識そのものが汚染される脅威にも備える必要がある」 |

**Emphasis Balance:**
- Technical Depth: ⭐⭐⭐
- Business Impact: ⭐⭐⭐
- Future Outlook: ⭐⭐

**Key Synthesis Points:**
- AIエージェントのセキュリティは「実行環境」「権限境界」「知識ベース」の3層で防御が必要
- 攻撃者もAIエージェントを使う時代、防御の自動化・高速化が不可欠
- 「プロンプト層」が企業の新たなcrown jewelsであるという認識の転換

**Assembly Prompts for STEP_08:**
1. この週のセキュリティ事件は、エージェント開発者に何を教えているか？
2. 攻撃→防御の3層構造を読者が自社に適用できる形で示す
3. 「プロンプトは新たな王冠の宝石」というフレーズを軸にする
4. 防御技術の進化速度は攻撃に追いついているか？

---

### Theme 2: Claude Codeが「個人の道具」から「組織のインフラ」へ：サイレント計測と6並列レビューの衝撃

**Pattern:** Progressive-Sequence
**Pattern Rationale:** 可視化（計測）→品質保証→組織展開という成熟度の階段を4社の実例で登る構成。

**Article Order & Roles:**
1. [289] ZOZO OTel計測 — Foundation: MDMサイレント配布でユーザー負担ゼロの利用ログ収集
2. [240] LINE Yahoo ロギング基盤 — Development: Hooks/Pluginsで「何が使われたか」の詳細計測
3. [285] Findy 6並列セルフレビュー — Advanced: 計測の先にある品質保証、6エージェント並列チェック
4. [241] TAKT品質保証 — Payoff: Faceted-Promptingによる自動レビュー＆修正サイクルの安定化

**Narrative Arc:**
「まず見える化し、次に計測を深め、そして品質を自動保証する」という組織成熟度のステップを、4社の実装事例で追体験させる。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [289] → [240] | 「ZOZOのOTel計測が"どれだけ使われているか"を示すなら、LINE Yahooのアプローチは"どう使われているか"を明らかにする」 |
| [240] → [285] | 「利用状況の可視化は出発点に過ぎない。その先にあるのは、AIが生成したコードの品質をどう保証するかという問いだ」 |
| [285] → [241] | 「Findyの並列レビューが"発見"に焦点を当てるのに対し、TAKTのアプローチは"修正サイクル"まで自動化する」 |

**Emphasis Balance:**
- Technical Depth: ⭐⭐⭐
- Business Impact: ⭐⭐⭐
- Future Outlook: ⭐⭐

**Key Synthesis Points:**
- 個人ツールから組織インフラへの移行には「計測→品質→ガバナンス」の3段階が必要
- 4社に共通するのは「開発者に負担をかけない」設計思想
- Claude Codeのエンタープライズ採用は日本企業が世界をリードしている

**Assembly Prompts for STEP_08:**
1. なぜ「計測」が組織導入の第一歩なのか？
2. 4社のアプローチの共通点と差異は何か？
3. 読者の組織がどの段階にいるかを判断できるフレームワークを示す
4. 「個人→組織」の移行で最も見落とされがちな課題は何か？

---

### Theme 3: AIが生成するUIの「不気味の谷」：統計的平均値では埋められないデザインの余白

**Pattern:** Multi-Perspective
**Pattern Rationale:** 問題の言語化（254）→設計原則の提案（217）→産業的影響の検証（275）と、3つの異なる角度から同じテーマを照らす。

**Article Order & Roles:**
1. [254] AI UXの違和感 — 問題定義: 「画面は作れるがフローは設計できない」「余白に統計的平均値」
2. [217] AI体験の信頼設計 — 設計原則: trust/value/effort/failure costの4軸で認知負荷を再分配
3. [275] Figma AI 70%完成 — 産業的影響: 「70%はAI、残り30%が人間の価値」、指揮者としてのデザイナー

**Narrative Arc:**
AIが生成するUIの「違和感」を名付け（254）、その解決策の設計原則を示し（217）、産業レベルでの影響を確認する（275）。3つの視点が収束する先は「人間の美的判断は代替不能」という結論。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [254] → [217] | 「この"違和感"の正体を解きほぐすフレームワークが提案されている」 |
| [217] → [275] | 「この設計原則がFigma AIの実際の導入現場でどう機能しているか」 |

**Emphasis Balance:**
- Technical Depth: ⭐⭐
- Business Impact: ⭐⭐⭐
- Future Outlook: ⭐⭐⭐

**Key Synthesis Points:**
- 「統計的平均値」という表現がAI生成物の限界を鋭く言い当てている
- デザイナーの価値は「作る」から「判断する」へ移行（開発者のTheme 4と並行）
- 70%/30%の分割はデザインに限らず、AI協働全般に適用可能なメタファー

**Assembly Prompts for STEP_08:**
1. 「統計的平均値の余白」とは具体的に何か？開発者にも分かる例で示す
2. 4軸設計フレームワークを実務で使えるチェックリストとして提示
3. 「指揮者」メタファーでTheme 4の開発者論への橋渡しをする

---

### Theme 4: 「コードを見るな」vs「LLMは使わない」：開発者アイデンティティを揺さぶる二つの極論

**Pattern:** Debate-Contrast
**Pattern Rationale:** Steve YeggeとNeil Maddenの真正面からの対立を軸に、学術的検証とデータで立体化する構成。

**Article Order & Roles:**
1. [210] Steve Yegge — Position A: 「IDEを捨て、AIの参謀長になれ。味覚が最後の競争優位」
2. [220] Neil Madden — Position B: 「プログラミングは愚かな機械に教える認知プロセス。LLMはそれを迂回する」
3. [140] Against Vibes — Analytical lens: 「vibesベースの受容」を科学的に解体、有用性の3条件を定義
4. [224] LLMマージ率停滞 — Data check: テスト通過率↑だがマージ率は横ばい、実態はどちらの立場を支持？

**Narrative Arc:**
2つの極論を提示し、読者を論争の渦中に引き込んだ後、学術的フレームワークで地盤を固め、最後にデータで冷静に検証する。結論は出さず「問い」を読者に委ねる。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [210] → [220] | 「これに対し、真っ向から異を唱えるセキュリティ専門家がいる」 |
| [220] → [140] | 「この哲学的対立に、科学的なフレームワークで切り込む試みがある」 |
| [140] → [224] | 「理論はともかく、データは何を示しているのか」 |

**Emphasis Balance:**
- Technical Depth: ⭐⭐
- Business Impact: ⭐
- Future Outlook: ⭐⭐⭐

**Key Synthesis Points:**
- この論争は「効率vs学習」ではなく「人間のアイデンティティをどこに置くか」の問い
- 140の3条件（エンコーディングコスト、検証コスト、プロセスの重要性）が判断基準を提供
- 224のデータは楽観論に冷水をかけるが、絶望でもない——「使い方」が問われている

**Assembly Prompts for STEP_08:**
1. 両極論を公平に、しかし鋭く提示する（どちらも「正しい」状況がある）
2. 140のフレームワークを読者が自分の仕事に適用できる形で示す
3. 結論を出さず、「あなたはどちら側か」という問いで終わる
4. Theme 3の「指揮者」論との接続を意識

---

### Theme 5: Amazon「高爆発半径」障害とAtlassian 1,600人解雇：AIコード導入の代償と希望

**Pattern:** Progressive-Sequence
**Pattern Rationale:** 技術的失敗→組織的影響→対比的成功例と、インパクトのスコープを広げる構成。

**Article Order & Roles:**
1. [249] Amazon AIコード障害 — Foundation: 「高爆発半径」障害の実態、シニアエンジニア承認の義務化
2. [164] Atlassian 1,600人解雇 — Development: AI投資のための15%リストラ、組織レベルの影響
3. [280] 千葉銀行 AI導入 — Payoff: 2,000人分の業務をAI化しつつ「人は切らない」、対比的希望

**Narrative Arc:**
技術的リスク（障害）→組織的リスク（雇用）→希望の対比（人を切らない選択肢）という感情の弧を描く。暗い話で終わらせず、別の選択肢があることを示す。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [249] → [164] | 「技術的な障害リスクに加え、AIへの戦略的シフトは雇用そのものにも波及している」 |
| [164] → [280] | 「しかし、AIの導入が必ずしも解雇を意味するわけではない。別の選択肢が日本から生まれている」 |

**Emphasis Balance:**
- Technical Depth: ⭐⭐
- Business Impact: ⭐⭐⭐
- Future Outlook: ⭐⭐

**Key Synthesis Points:**
- 「高爆発半径」はAIコード導入の技術的リスクを象徴するフレーズ
- 欧米の「解雇→AI投資」モデルと日本の「人は切らない」モデルの対比
- AIの導入は技術の問題ではなく、組織の価値観の問題

**Assembly Prompts for STEP_08:**
1. 「高爆発半径」を開発者が自組織で想像できる具体性で描写
2. Atlassianの「AI投資のための解雇」は正当化されるか？事実のみで示す
3. 千葉銀行の方針が現実的かどうかも含め、読者に判断を委ねる

---

### Theme 6: Anthropic提訴からClaude唯一の拒絶まで：AIの「倫理的境界線」が問われた週

**Pattern:** Single-Focus
**Pattern Rationale:** Anthropicの倫理的姿勢を軸に、技術・社会・労働の3次元で「境界線」の意味を展開する。

**Article Order & Roles:**
1. [118] Anthropic vs Trump — Lead: 軍事利用拒否→サプライチェーンリスク指定→提訴、37名の業界支持
2. [277] Claude唯一の拒絶 — Reaction: CNN/CCDH調査で暴力計画を拒否できたのはClaudeのみ
3. [228] AI顔認証誤認逮捕 — Contrast: 倫理的境界線が「ない」場合の帰結、160日投獄
4. [227] ケニアのデータラベラー — Broader context: AIの裏側で苦しむ労働者、PTSDと組合結成

**Narrative Arc:**
Anthropicの法的闘争（118）から始まり、その倫理的姿勢が技術的にも一貫していること（277）を示す。次に、倫理的境界線が存在しない場合の人間への被害（228）を対比し、最後にAI産業全体の構造的倫理問題（227）で視野を広げる。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [118] → [277] | 「Anthropicの法的闘争は、同社の技術的な安全設計にも反映されている」 |
| [277] → [228] | 「Claudeの拒絶が示すのは、倫理的ガードレールが存在しない場合に何が起こるかだ」 |
| [228] → [227] | 「AIの被害は利用者だけに留まらない。その訓練を支える労働者にも深刻な影響が及んでいる」 |

**Emphasis Balance:**
- Technical Depth: ⭐
- Business Impact: ⭐⭐
- Future Outlook: ⭐⭐⭐

**Key Synthesis Points:**
- 倫理的境界線は「コスト」ではなく「競争優位」になりうる（Anthropicの事例）
- 技術（277）、法（118）、社会（228, 227）の3次元で同時に問われている
- 「境界線を引くこと」自体が、AI時代の最も重要な設計判断

**Assembly Prompts for STEP_08:**
1. 感情的にならず、事実ベースで構成する（EDITOR_PERSONALITY準拠）
2. Anthropicを「英雄」として描くのではなく、判断の構造を分析する
3. 読者（開発者）が自分の仕事で「境界線」を意識できるようにする
4. 「倫理は贅沢品か必需品か」という問いで締める

---

### Theme 7: ポストトレーニングの民主化：Sharon Zhouが語る「普通の企業」のRL時代

**Pattern:** Progressive-Sequence
**Pattern Rationale:** 概念（RL民主化）→実装（Nemotron 3 Super）→ビジョン（世界モデル）と、抽象度を段階的に上げる。

**Article Order & Roles:**
1. [209] Sharon Zhou / O'Reilly — Foundation: ポストトレーニングの本質、SFT/RL/RAGの使い分け、企業への普及
2. [287] Nemotron 3 Super — Development: 120B MoEハイブリッド、1Mコンテキスト、FP4ネイティブ
3. [191] Yann LeCun AMI — Payoff: $1.03B調達、世界モデル構想、現行LLMの限界を超える試み

**Narrative Arc:**
「ポストトレーニングとは何か」を解きほぐし（209）、その成果物としての最新モデルを紹介し（287）、さらにその先にある「LLMの次」のビジョンで締める（191）。

**Transition Strategy:**
| From → To | Transition Approach |
|-----------|---------------------|
| [209] → [287] | 「このポストトレーニングの考え方を体現したモデルが、NVIDIAから発表された」 |
| [287] → [191] | 「しかしMoEの進化はLLMの延長線上にある。根本的に異なるアプローチも動き始めている」 |

**Emphasis Balance:**
- Technical Depth: ⭐⭐⭐
- Business Impact: ⭐⭐
- Future Outlook: ⭐⭐⭐

**Key Synthesis Points:**
- ポストトレーニングは「フロンティアラボの独占」から「普通の企業のツール」へ
- Nemotron 3 SuperのMamba-Transformerハイブリッドは効率と精度の新しいバランス
- LeCunの世界モデルは「今のAIの延長」ではなく「パラダイムの転換」を志向

**Assembly Prompts for STEP_08:**
1. ポストトレーニングを非専門家にも分かる例え（「原石の研磨」）で説明
2. Nemotron 3 Superの技術的革新を開発者が評価できるレベルで解説
3. 「次の次」としてのLeCunの世界モデルをジャーナルの締めくくりに使う

---

## Assembly Plan Status

- [x] Phase 1: Pattern library reviewed
- [x] Phase 2: Patterns selected and customized for all themes
- [x] Phase 3: Assembly strategies documented
- [ ] ASSEMBLY PLAN APPROVED - Ready for STEP_08

**Approval Date:**
**Approver:**
