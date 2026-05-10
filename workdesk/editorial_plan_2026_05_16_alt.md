# Editorial Plan (Alternative) - Journal 2026-05-16

## Planning Status
- [x] Initial theme identification (AI-assisted, alternative angle)
- [ ] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [ ] APPROVED - Ready for STEP_04 curation

---

## Organizing Principle (How This Differs from the Original Plan)

The original plan groups articles by **topic cluster** — same technology, same company, same trend ("Agent Skills articles," "low-cost model articles," "platform announcements"). It is a defensible taxonomy but reads like a catalog: each theme is a bucket of "what's happening here."

This alternative organizes by **the working engineer's open decision points this week** — questions a reader is actively being asked to answer at their desk. Each theme is a question, and the articles inside it are the inputs for answering that question.

Concrete differences from the original:
- The Agent Skills cluster is **dissolved**: Addy Osmani / Perplexity / SKILL.mk go into "what shape does my SKILL.md take," while migrating-related material goes elsewhere.
- The "industry tension" theme is **absorbed**: Claude Is Dead, Atlantic, OpenClaw rough week are not their own theme — they're inputs to "should I stay on Claude Code or migrate."
- The **token economics** material is promoted to a top-level theme (it had been a sub-bucket).
- A new **"how do I prove the agent worked"** theme spans validation, accept-conditions, and dominator analysis — pieces the topic plan scattered across themes 5 and 6.

Total: 7 themes, 22 unique main articles after dedup.

---

## Identified Themes

### Theme 1: コード生成エージェントの乗り換え判断材料 — Claude Code / Codex / OpenCode Go / DeepClaude

**Articles (IDs):** 043, 067, 122, 037, 035, 144

**Theme Introduction (2-3 sentences in Japanese):**
Claude Codeの利用制限と推論品質に関する不満が公にされる一方、Codexアプリの実用性レビュー、OpenCode Go＋Kimi K2.6/DeepSeek V4 Proによる代替スタック、DeepClaudeによるバックエンド差し替えなど、移行先の具体的な選択肢が同時期に出揃いました。エージェント乗り換えを検討している開発者向けに、判断材料となる一次情報を集めました。

**Editorial Notes:**
- 043: Claude Is Dead — 移行を検討する起点となる批判記事。レート制限と推論劣化の主張
- 067: Claude Code → Codex入門 — permissionモードの違い、移行ガイド
- 122: OpenCode Go + pi-coding-agent — 月10ドルでDeepSeek V4 Pro/Kimi K2.6を使う具体セットアップ
- 037: DeepClaude — Claude Code CLIのUXのままバックエンド差し替え、17倍コスト削減（👎、補足扱い）
- 035: The Atlantic AI Bubble — Anthropic収益急成長、移行判断のビジネス継続性文脈
- 144: OpenClaw rough week — 競合フレームワークの安定性ポストモーテム

---

### Theme 2: SKILL.mdをどう書くか — Addy Osmani / Perplexity / SKILL.mk / sklock / 既存コード抽出

**Articles (IDs):** 003, 013, 020, 118, 064

**Theme Introduction (2-3 sentences in Japanese):**
Agent Skillsを「書く」段階に入った開発者が直面するのは、何を書き、どう構造化し、どう管理するかという三つの実務問題です。今週はAddy OsmaniとPerplexityがそれぞれ独立に設計原則を公開し、Makefile形式の代替仕様、依存管理CLI、既存コードからの抽出手法も登場しました。

**Editorial Notes:**
- 003: Addy Osmani Agent Skills — プロセス重視・反正当化テーブル等の5原則
- 013: Perplexity Designing Skills — 「Zen of Skills」と3階層構造、「Load when...」の重要性
- 020: SKILL.mk — Makefileで依存関係表現、トークン85%削減
- 118: sklock — スキル群のlockfile管理、影響範囲特定
- 064: 既存コードからAgent Skills抽出 — 暗黙知をSKILL.mdへ言語化

---

### Theme 3: トークンとコスト — DeepSeek V4 1786倍差 / GitHub 62%削減 / VSCode 1.118 93% / WebFetch Haiku

**Articles (IDs):** 099, 117, 130, 063, 068, 019

**Theme Introduction (2-3 sentences in Japanese):**
トークン消費の削減と価格構造の透明化が、今週の最も具体的な数値で語られています。DeepSeek V4のキャッシュヒット時の極端な低価格、GitHubが自社ワークフローで達成した62%削減、VSCode 1.118のキャッシュ利用率93%、そしてClaude CodeのWebFetchが裏でHaiku要約を挟んでいるという発見は、いずれも「実質トークンコスト」という共通指標で読み解けます。

**Editorial Notes:**
- 099: DeepSeek V4 1786倍 — キャッシュヒット時のClaude Opus比1786倍コスト差の試算
- 117: DeepSeek V4 公式pricing — 1Mトークンcontextと特別価格の一次情報
- 130: GitHub 62%削減 — Effective Tokensメトリクス導入（👍、リード候補）
- 063: VSCode 1.118 — キャッシュ93%、コンテキスト分離fork、Chronicle機能
- 068: WebFetch Haiku — メインモデルに渡る前にHaikuが要約している仕様暴露
- 019: Simon Willison DeepSeek V4 — フロンティア性能と低価格の分析

---

### Theme 4: エージェントの動作を「証拠」で検証する — GitHub Dominator / Plan Mode / SPECA / Mozilla Firefox 271件 / OWASP Juice Shop

**Articles (IDs):** 105, 145, 093, 136, 121

**Theme Introduction (2-3 sentences in Japanese):**
非決定的なエージェントが「成功した」と報告したとき、それを何で確かめるか。ドミネータ分析による必須通過点の特定、Plan Modeを安易に承認しないための受け入れ条件分離、仕様書からチェックリストを生成する監査フレームワーク、そしてMozillaがFirefoxで271件の脆弱性を実証的に検出した事例は、いずれも「エージェント出力を証拠で裏付ける」という共通の問題意識を持っています。

**Editorial Notes:**
- 105: GitHub Dominator分析 — グラフ理論で必須通過点を抽出、自己評価82.2%→ドミネータ100%
- 145: AIのPlan Mode盲信しない — 既存情報から条件候補を抽出、4観点レビュー
- 093: SPECA — 仕様書からの証明試行型監査、Sherlockコンテストで4件の新規バグ発見
- 136: Mozilla Firefox 271件脆弱性 — Claude Mythos Previewで実証検出
- 121: Claude-security-scan / OWASP Juice Shop — 60-70%検出率の実測（👍、リード候補）

---

### Theme 5: プラットフォームの自動化拡張 — Claude Managed Agents / Linear / Stripe MPP / Supabase ChatGPT App / Anthropic 金融

**Articles (IDs):** 153, 002, 062, 158, 053

**Theme Introduction (2-3 sentences in Japanese):**
AIエージェントを「使える場所」がアプリ単体から業務基盤全体へと広がった一週間でした。AnthropicのDreaming/Outcomes/Multiagent Orchestration、Linearの「Issue tracking is dead」宣言、StripeのMPP/Tempo/Link Agent Wallets、SupabaseのChatGPT公式アプリ、Anthropicの金融向けエージェントが相次ぎ、それぞれ既存ワークフローへの統合点を提示しています。

**Editorial Notes:**
- 153: Claude Managed Agents — Dreaming/Outcomes/Multiagent Orchestration
- 002: Linear Issue tracking is dead — Linear AgentとSkills、コンテキスト実行モデル
- 062: Stripe Sessions 2026 — MPP、Tempo、Link Agent Wallets
- 158: Supabase ChatGPT App — 29種類のツール、自然言語DB管理
- 053: Anthropic 金融 — 10種テンプレート、Microsoft 365統合、Opus 4.7で64.37%

---

### Theme 6: ローカル/オープンウェイトモデルの選択肢 — DeepSeek V4 / Gemma 4 / Kimi K2.6 / antirez ds4

**Articles (IDs):** 084, 029, 141, 097, 007

**Theme Introduction (2-3 sentences in Japanese):**
クラウドAPIへの依存を見直す材料が今週は揃いました。Gemma 4の日本語能力とMTPによる3倍高速化、Kimi K2.6がプログラミング競技でフロンティアモデルを上回った報告、antirez氏のApple Silicon特化推論エンジン、O'Reillyのローカルモデル現状整理という形で、「クラウドの代わりにこれが手元にある」という具体性が増しています。

**Editorial Notes:**
- 084: Gemma 4 — 31B/26B/E4B/E2B、日本語能力の飛躍、MCP対応
- 029: Kimi K2.6 — プログラミング競技でGPT-5.5/Claude/Geminiを上回る
- 141: antirez ds4 — Apple Silicon Metal特化のDeepSeek V4 Flash推論エンジン
- 097: Gemma 4 MTP — Multi-Token Predictionで3倍高速化
- 007: O'Reilly Local AI — ローカルAIの現状、フロンティアとの性能差縮小

---

### Theme 7: 「AIに任せる」の境界線 — Uncle Bob / Cognitive Surrender / Vibe coding境界 / Agentic Trap / 認知負債 / DBを消したのは

**Articles (IDs):** 032, 057, 115, 039, 149, 051

**Theme Introduction (2-3 sentences in Japanese):**
AIエージェントへの委譲をどこで止めるかという議論が、この一週間で複数の論者から独立に提示されました。Uncle Bobの「終わった」宣言、Addy Osmaniの「認知の放棄」、Simon Willisonの境界曖昧化への懸念、larsfaye氏の「監視のパラドックス」、川島氏の「認知負債」、idiallo氏の「DBを消したのはAIではない」は、それぞれ立場が異なるものの、「人間の理解と責任の所在」という共通の論点を扱っています。

**Editorial Notes:**
- 032: Uncle Bob "It's over" — プログラミング終焉宣言、Vibe Codingの是非
- 057: Cognitive Surrender (Addy Osmani) — オフロードとサレンダーの違い、理解負債
- 115: Simon Willison Vibe coding境界 — Vibe codingとAgentic engineeringの境界曖昧化
- 039: Agentic Coding is a Trap — 監視のパラドックス、スキル萎縮
- 149: 認知負債 (川島) — 技術負債・認知負債・意図負債の3層整理
- 051: idiallo / DBを消したのは — ツール責任転嫁批判、ガードレール設計責任

---

## Highlight Draft ("今週のハイライト")

今週のソースは、AIコーディングエージェントを「導入するか」ではなく「すでに導入したものをどう運用するか」という段階の問いで占められています。DeepSeek V4のAPIがキャッシュヒット時にClaude Opusの1786分の1という極端な低価格を提示し、Kimi K2.6がプログラミング競技で商用フロンティアモデルを上回り、Gemma 4が日本語能力を飛躍させてMTPで3倍高速化を実現する一方、Claude Codeの利用制限と推論品質への不満が「Claude Is Dead」として公に書かれ、Codex、OpenCode Go、DeepClaudeなど移行先の具体的な選択肢が同時期に揃いました。乗り換えを検討する材料が、今週これだけまとまった量で出揃ったのは初めてに近い状況です。

二つ目の軸は、Agent Skillsの「設計と運用」です。Addy OsmaniとPerplexityがそれぞれ独立に設計原則を公開し、SKILL.mkがMakefile形式でトークン85%削減を実証し、sklockが依存管理を、既存コード抽出手法が暗黙知の言語化を、と Skill単位のエコシステムが具体化しました。同時にトークン経済の数値も鮮明になり、GitHubが自社運用で62%削減、VSCode 1.118がキャッシュ93%、WebFetchが裏でHaiku要約を挟んでいるという仕様暴露が並びました。Skillをどう書くかと、それを動かすコストをどう下げるかが、運用フェーズの中心テーマになっています。

三つ目はエージェント出力を「証拠で検証する」手法群です。GitHubのドミネータ分析は自己評価82.2%に対しドミネータ100%という具体数で精度を示し、Plan Modeを盲信しないためのワークフロー、SPECAの仕様書駆動監査、MozillaがFirefoxで271件の脆弱性を実証検出した事例、Juice Shopでの60-70%検出率という実測が並びます。これらは「AIに任せた結果を、何で確かめるか」という実務問題への独立した回答です。

最後に、プラットフォーム側の動きとして、Anthropic Managed AgentsのDreaming/Outcomes、LinearのIssue tracking廃止宣言、StripeのMPP/Tempo、Supabase ChatGPT App、Anthropic金融エージェントが揃い、AIエージェントが「使える場所」が業務基盤全体へ拡張しました。これらと並行して、Uncle Bob・Addy Osmani・Simon Willison・larsfaye・川島・idialloが独立に「AIに任せる境界線」を論じており、利用範囲の拡大と委譲の限界がほぼ同時に語られているのが今週の風景です。

---

## Curation Signal Summary

**👍 Upvoted Articles Used:**
- 121 → Theme 4 (Lead候補) — OWASP Juice Shopでの60-70%検出率
- 130 → Theme 3 (Lead候補) — 62%削減
- 059 (Playwright CLI) → Annex候補（決定レベルのテーマに合致せず）

**👎 Downvoted Articles:**
- 037 deepclaude → Theme 1 補足（17倍コスト削減の事実情報のみ）
- 018 Governor → Annex候補
- 071 OpenCode + Gemma 4 → Annex（122・094で代替）
- 074 SKILL.md整理ノート → Annex候補
- 131 AIエージェントPRレビュー → Annex候補

**Omitted Articles:** Supabaseで明示的omit指定なし

---

## Theme Coverage Summary

| Theme | Articles | Count |
|-------|----------|-------|
| 1. 乗り換え判断材料 | 043, 067, 122, 037, 035, 144 | 6 |
| 2. SKILL.mdの設計 | 003, 013, 020, 118, 064 | 5 |
| 3. トークンとコスト | 099, 117, 130, 063, 068, 019 | 6 |
| 4. 動作を証拠で検証 | 105, 145, 093, 136, 121 | 5 |
| 5. プラットフォーム自動化 | 153, 002, 062, 158, 053 | 5 |
| 6. ローカル/オープンモデル | 084, 029, 141, 097, 007 | 5 |
| 7. AI委譲の境界線 | 032, 057, 115, 039, 149, 051 | 6 |

**Total Planned for Main:** 38 article slots → 22 unique articles after dedup
**Remaining for Annex:** Supabaseフラグ済み32件 + 残り

---

## Review Notes (Human Editor)

**Date Reviewed:** TBD
**Reviewer:** TBD

**Changes Made:** TBD

**Approval:** ⏳ PENDING REVIEW

---

## Implementation Checklist

After approval:
- [ ] Choose between this alt plan and the original `editorial_plan_2026_05_16.md`
- [ ] Rename approved version to `editorial_plan_2026_05_16.md` (replacing the other)
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use approved plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)
