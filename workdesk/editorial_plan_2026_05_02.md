# Editorial Plan - Journal 2026-05-02

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Identified Themes

7 themes covering 24 articles for the main journal. Titles name specific technologies, companies, people, or numeric findings; introductions describe what the articles cover, without manufactured narrative.

### Theme 1: Claude Design発表とデザイン業界の再編 — Figma株7%下落・DESIGN.md・Agentic UX

**Articles (IDs):** 055, 110, 015, 044

**Theme Introduction (factual, 2-3 sentences):**
2026-04-17のClaude Design（Opus 4.7ベースのデザイン生成 + Claude Codeへのhandoff）発表を起点に、Figmaの株価7%下落とAnthropic CPOの取締役辞任が業界を揺らした週となった。本セクションは独立系アナリストによる構造分析、Google LabsによるDESIGN.md仕様のOSS化、Goodpatchの「Agentic UX」概念整理を集めている。

**Editorial Notes:**
- 055 (Lead, 400-600w): Martin Alderson "Figma's Woes Compound with Claude Design" — SaaSの構造的弱点をAnthropicが直接突いた、独立系の構造分析。
- 110 (Supporting): Sam Henri Gold — デザインの「真実の源」がコードへ回帰する歴史的構図（Sketch→Figma→Code）。
- 015 (Supporting): Google Labs「Stitch app's DESIGN.md」OSS化発表。AIエージェントにデザインルールを伝える共通フォーマット。
- 044 (Synthesis/Supporting): Goodpatch「Agentic UX」概念整理（意図/環境/信頼/制御の4観点）。デザイン論の側からの応答。

---

### Theme 2: Claude Mythos の現実と虚像 — Firefox 271件修正・システムカード批判・NSA運用・GPT-5.5追従

**Articles (IDs):** 017, 151, 173, 182

**Theme Introduction (factual, 2-3 sentences):**
AnthropicのClaude Mythosは、Firefox 150の脆弱性271件をMozillaが一斉修正したという成果と、システムカード244ページの精査による「Firefox成功率72.4%は2件依存で4.4%に低下」という反証、NSAがブラックリスト無視で運用しているとのAxios報道、そしてXBOWによるGPT-5.5の同等性能達成発表が同週に重なった。本セクションは公式発表・批判的検証・運用現実・競合追従の4視点を集めている。

**Editorial Notes:**
- 017 (Lead, 400-600w): Mozilla公式「The zero-days are numbered」— Firefox 150の脆弱性271件をMythos Previewで修正。一次情報。
- 151 (Supporting): flyingpenguin「The boy that cried Mythos」— 244ページのシステムカード精査でFirefox成功率を再計算、特定2件への依存を指摘。
- 173 (Supporting): Reuters/Axios — NSAがDoDブラックリストを無視してMythosを利用しているとのスクープ。
- 182 (Synthesis): XBOW — GPT-5.5がMythos同等の脆弱性検出能力を達成（見逃し率40%→10%）、Anthropicの優位性は短命との示唆。

---

### Theme 3: GPT-5.5発表とOpenAI連発リリース — Terminal-Bench 2.0で82.7%・Codex Chronicle・Workspace Agents

**Articles (IDs):** 075, 028, 077

**Theme Introduction (factual, 2-3 sentences):**
2026-04-21〜23の3日間で、OpenAIはGPT-5.5本体、macOS版CodexのChronicle機能、企業向けWorkspace Agents、医療向けChatGPT for Cliniciansを連続発表した。本セクションは中核となる3件—フラッグシップモデル発表、開発者向け新機能、エンタープライズ向け新製品—を扱い、ベンチマーク結果と機能仕様を一次情報から確認する。

**Editorial Notes:**
- 075 (Lead, 400-600w): OpenAI公式「Introducing GPT-5.5」— Terminal-Bench 2.0で82.7%、GDPval 84.9%、社内ハーネスでラムゼー数のオフ対角漸近証明をLeanで形式検証。
- 028 (Supporting): Codex Chronicle — macOS画面OCRで作業コンテキストを「Memories」として自動蓄積（オプトイン、EU/UK/CH除外）。
- 077 (Synthesis): Workspace Agents — Codex基盤、5/6まで無料、企業向けのエージェント基盤。

---

### Theme 4: Amazon $25B拡張とAWS-Anthropic 10年提携 — Bedrock AgentCore・Claude Cowork・Project Rainier

**Articles (IDs):** 139, 006, 005

**Theme Introduction (factual, 2-3 sentences):**
Amazonは追加$5B（最大$25B）をAnthropicに出資、Anthropicは10年で$100BのAWS支出をコミット、Trainium2-4の採用と5GWのProject Rainier展開で合意した。本セクションは公式リリースに加え、提携を実装に落とし込むBedrock AgentCoreの新機能とClaude Coworkの組織展開を扱う。

**Editorial Notes:**
- 139 (Lead, 400-600w): Amazon公式 — 提携拡大の一次情報。$5B追加・最大$25B、Trainium2-4、5GW、Project Rainier。
- 006 (Supporting): AWS公式 — Bedrock AgentCoreの新機能（マネージドハーネス3 APIコール、AgentCore CLI、永続ファイルシステム）。
- 005 (Supporting): AWS公式 — Claude Cowork in Bedrock提供開始。IAM/VPC/CloudTrail統合、ナレッジワーカー向け展開。

---

### Theme 5: Claude Code Pro削除騒動とCopilot個人プラン制限 — エージェント時代のサブスク経済

**Articles (IDs):** 181, 038, 062

**Theme Introduction (factual, 2-3 sentences):**
AnthropicがPro プランからClaude CodeをA/Bテストで一時除外、GitHubがCopilot個人プラン（Pro/Pro+/Student）の新規受付停止と利用制限強化を発表、HNでは課金変更スレッドが活性化した週となった。本セクションは速報的な批評、公式発表、コミュニティ反応の3点を集めて、エージェント機能のコスト構造とサブスクリプションモデルの限界を扱う。

**Editorial Notes:**
- 181 (Lead, 400-600w): Ed Zitron (wheresyoured.at) — Anthropicによるドキュメント書き換えの記録、AI課金モデルの限界論。批評家の観点。
- 038 (Supporting): GitHub公式 — Copilot個人プラン新規受付停止、トークンベース利用制限、一部ハイエンドモデルのプラン制限。
- 062 (Supporting): HNスレッド — Claude CodeをProプランから除外するA/Bテスト発覚。コミュニティの初動反応。

---

### Theme 6: オープンウェイト勢のフロンティア追従 — Qwen3.6-27B・Kimi K2.6・LLM-as-a-Verifier 86.4%

**Articles (IDs):** 052, 108, 164

**Theme Introduction (factual, 2-3 sentences):**
Stanford×Berkeley×NVIDIA共同研究のLLM-as-a-VerifierがTerminal-Bench 2で86.4%のSOTAを達成、Qwen3.6-27Bデンスモデルが SWE-bench 77.2でClaude 4.5 Opusと同点に到達、Moonshot AIのKimi K2.6が最大300サブエージェント・10時間自律実行のAgent Swarm機能を発表した。本セクションは一次情報3件で、オープンウェイト勢のクローズドモデルへの追従を扱う。

**Editorial Notes:**
- 052 (Lead, 400-600w): LLM-as-a-Verifier — Stanford/Berkeley/NVIDIA共同研究、Terminal-Bench 2で86.4%、SWE-Bench Verifiedで77.8%、3軸スケーリング（Generation/K-best/Compute）の数式付き。
- 108 (Supporting): Qwen公式 — Qwen3.6-27Bデンスモデル、SWE-bench 77.2、Terminal-Bench 2.0でClaude 4.5 Opusと同点59.3。
- 164 (Synthesis): Moonshot公式 — Kimi K2.6、Agent Swarmで最大300サブエージェント、4,000ステップ並列、10時間自律実行。

---

### Theme 7: AGENTS.md/Skills/APMの標準化 — Pepabo CLAUDE.md 83%削減・Android CLI 70%削減・Microsoft APM

**Articles (IDs):** 200, 003, 105, 042

**Theme Introduction (factual, 2-3 sentences):**
コンテキストファイル（CLAUDE.md/AGENTS.md/SKILL.md）の構造化によるトークン削減実証と、それらを管理するパッケージマネージャの整備が重なった週となった。本セクションはPepaboのCLAUDE.md 3層構造化（83%削減）、Google AndroidのCLI+Skills（70%削減）、Microsoft APM（Agent Package Manager）、mizchiのSKILL.md実例の4件を扱う。

**Editorial Notes:**
- 200 (Lead, 400-600w): Zenn pepabo — CLAUDE.mdを3層構造化しトークン消費83%削減（11万→1.9万）。実装手順と計測結果。
- 003 (Supporting): Google公式 — Android CLI + Skillsでトークン使用量70%削減、タスク3倍高速化。
- 105 (Supporting): Qiita TKfumi — Microsoft APM（Agent Package Manager）の解説。エージェントスキルのバージョン管理。
- 042 (Synthesis): GitHub mizchi/chezmoi-dotfiles — empirical-prompt-tuning SKILL.mdの実例。実運用例の参照。

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**

2026-05-02号で扱う週は、フラッグシップモデルの発表とエンタープライズ提携の更新が同時に進行した。OpenAIはGPT-5.5を中核に、macOS版CodexのChronicle機能、企業向けWorkspace Agents、医療版ChatGPT for Cliniciansを4日間で連続投入した。AmazonはAnthropicへの出資を最大$25Bに拡張し、AnthropicはAWSに10年で$100Bを支出することでProject Rainier（5GW、Trainium2-4）を稼働させる。一方、Anthropicは2026-04-17にClaude Designを発表してデザインツール市場に参入し、Figmaの株価は7%下落した。

**ベンチマーク数値とコンテキスト管理の実証データ:**

性能指標では、GPT-5.5がTerminal-Bench 2.0で82.7%を達成、Stanford×Berkeley×NVIDIA共同研究のLLM-as-a-Verifierが同ベンチで86.4%のSOTAを取った。Qwen3.6-27BデンスモデルはClaude 4.5 Opusと同点（Terminal-Bench 59.3）に到達し、Moonshot AIのKimi K2.6は最大300サブエージェント・10時間自律実行のAgent Swarmを公開した。コンテキストファイル管理では、PepaboがCLAUDE.mdの3層構造化でトークン消費83%削減（11万→1.9万）、Google AndroidがCLI+Skillsで70%削減・3倍高速化を実証した。

**論争と反証:**

Claude Mythosでは、Mozilla がFirefox 150の脆弱性271件を修正したという成功事例と、244ページのシステムカードを精査して「Firefox 72.4%成功率は2件依存で4.4%に低下」という反証、NSAがDoDブラックリスト無視で運用しているとのAxios報道、XBOWによるGPT-5.5の同等性能達成発表が同週に揃った。サブスクリプション面では、AnthropicがClaude CodeをProプランから一時除外するA/Bテスト、GitHubがCopilot個人プランの新規受付停止と利用制限強化を発表し、エージェント機能のコスト構造が露呈した。

**読者への含意:**

開発者にとっての観測点は、(1) ハーネス側の実装パターン（Skills/APM/AGENTS.md）が標準化フェーズに入りつつあること、(2) オープンウェイトのフロンティア追従ペースが加速していること、(3) サブスクリプションモデルがエージェント時代のコスト構造に追いついていないこと、の3点に集約される。

---

## Curation Signal Summary

**⭐ Standout Articles Used:** （Supabase flagsは過去週分のみのため、今週分は0件）

**👍 Upvoted Articles Used:** （同上、0件）

**👎 Downvoted Articles:** （同上、0件）

**Omitted Articles:** （Supabaseの今週分フラグなし）

**Note:** 本号では `workdesk/curation_flags.md` のフラグはすべて過去週のID/URLにマッピングされており、今週分のソースには一致がない。テーマ選定はAIによる summary 解析と curation_criteria.md に基づく。

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: 24 articles across 7 themes (target 18-25, 6-7 themes)
- Annex Journal: 残りから ~25-35 articles を STEP_05 で選定

**Article Count by Theme (Planned):**
- Theme 1 (Claude Design): 4 articles
- Theme 2 (Claude Mythos): 4 articles
- Theme 3 (GPT-5.5/OpenAI): 3 articles
- Theme 4 (Amazon-Anthropic): 3 articles
- Theme 5 (Subscription controversy): 3 articles
- Theme 6 (Open weight): 3 articles
- Theme 7 (Context files): 4 articles

**Total Planned for Main:** 24 articles
**Remaining for Annex:** 185 articles (annex候補は ~25-35 をSTEP_05で絞り込み)

---

## Annex Direction (Tentative — STEP_05で確定)

注: STEP_05 の human review が決定権を持つ。以下は方向性メモ。

**B-side候補の柱:**

1. **批判的論考とコントラリアン**: 098 (ハーネス批判), 079 (Doctorow), 082 (pluralistic doomers批判), 122 (tante fascist artifact), 144 (BBC MIT 脳活動55%低下), 064 (nial.se less human), 048 (kaminashi non-scaling), 047 (mattstromawn)

2. **AI Slop と OSS 持続可能性**: 034 (Hono yusukebe), 053 (LWN kernel), 065 (Internet Archive blocked), 135 (yomoyomo), 121 (surfacedby Nginx)

3. **エージェント UX とダークパターン**: 132 (chatbox UI批判), 133 (dark patterns 8修正策), 134 (UCSD Deception 55.8%), 130 (Thia DIY), 140 (Show HN slop)

4. **オープンウェイト周辺と量子化推論**: 040 (Lucebox), 083 (Ternary Bonsai 1.58bit), 165 (Kimi Vendor Verifier), 045 (NTT token unification), 209 (RTX 5090 180t/s)

5. **公共セクターと国家AI**: 030 (デジタル庁源内 OSS), 129 (Ukraine 25K robots), 162 (自衛隊white paper), 156 (羽生九段), 166 (SPReAD 1000)

6. **労働データと未来予測**: 141 (Anthropic 81K調査), 174 (Meta keystroke), 119 (AI Index 2026), 170 (future of work), 168 (Dark Factories)

7. **Cloudflare 内製スタックとプロトコル提案**: 011 (AI Code Review 4.8万MR), 012 (R&D 93%利用), 013 (Privacy Pass)

8. **Securityとガバナンス**: 049 (CSA storm), 137 (Vibe Code Auth), 167 (Behavioral Credentials), 175 (Native Messaging独立検証)

数を絞るのは STEP_05 の役目。本STEP_03bでは方向性のみ記載。

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-04-30
**Reviewer:** beijaflor

**Changes Made:**
- None — plan accepted as drafted.

**Approval:** ✅ APPROVED

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)

---

## Notes / Questions for Human Review

1. **テーマ7の単独化 vs Theme 4-5への分散**: AGENTS.md/Skills/APMは記事数が多く独立テーマに値するが、Microsoft APM (105) と mizchi SKILL.md (042) はやや軽い。「ハーネスエンジニアリング」トピック（002 Addy Osmani, 098批判）と再編する選択肢もある。

2. **Cloudflare cluster (011, 012, 013) の扱い**: 一次情報として強いが3記事のみ。メインに昇格させる、またはAnnexの独立セクションに残す、の選択。

3. **OpenAI連発リリース (Theme 3) の構成**: 075/028/077 を選定したが、078 (ChatGPT for Clinicians, HealthBench Professional) もstandalone primary source。4記事でも可。

4. **Theme 1 の Lead 選択**: 055 (Martin Alderson) と 110 (Sam Henri Gold) はどちらも独立分析。055を採用したが、Lead を 110 に入れ替える選択もある。

5. **アノテーション**: メインから外した日本語Tips系記事 (066, 068, 069, 086, 088, 090, 091, 095, 104, 187, 191, 193, 195, 196, 198, 205-208) は Annex の主軸ではないが、STEP_05でリストに含めるかは判断要。
