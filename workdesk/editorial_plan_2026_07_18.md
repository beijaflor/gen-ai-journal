# Editorial Plan - Journal 2026-07-18

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Identified Themes

*7 main themes proposed, ~27 candidate articles (STEP_04 will trim to the 18–25 target). Titles follow the `[named anchors] [single verb] [substantive topic phrase]` pattern.*

### Theme 1: Addy Osmani・AWS aidlc・公式プラグインが体系化するループ/ハーネスエンジニアリングの実践

**Articles (IDs):** 101, 219, 081, 225, 026

**Theme Introduction:**
今週も日本語コミュニティ最大の話題はClaude Codeを中心とした「ループ/ハーネスエンジニアリング」だった。Addy Osmaniはエンジニアが所有すべき領域を「アウター・ループ（意思決定・検証・説明責任）」と定義し、AWSのaidlc-workflowsの実践から「ハーネス（環境整備）」と「ループ（自律実行）」の観点が整理された。スキル設計の実務ポイントや著名エンジニアの公開スキルの分析も揃い、抽象論から具体的な設計手法へと議論が移っている。

**Editorial Notes:**
- 101 ⭐: Addy Osmani「アウター・ループを所有せよ」— エンジニアの責任範囲の再定義（リード候補）
- 219: AWS aidlc-workflowsから整理したハーネス vs ループの観点
- 081: Claude Codeのスキル設計で効く4つのポイント（新人に仕事を任せる視点）
- 225: 著名エンジニアの .claude/skills 公開ラッシュから学ぶ良いスキルの書き方
- 026: Claude CodeのPlanモードをループエンジニアリングで楽にする

---

### Theme 2: Kimi K3・GPT-5.6・Inklingが塗り替えるフロンティアモデルとオープンウェイトの勢力図

**Articles (IDs):** 090, 091, 082, 106

**Theme Introduction:**
フロンティアモデルの新リリースが集中した週だった。Moonshot AIは世界初のオープン3兆パラメータ級モデル「Kimi K3」を公開し、OpenAIはGPT-5.6ファミリー（sol/terra/luna）の移行ガイドを提示した。Thinking Machines Labのオープンウェイト「Inkling」も加わり、既知CVE検出ベンチマークではGPT-5.6とKimi K3が首位に並ぶなど、性能・価格・オープン性の三軸で競争が可視化されている。

**Editorial Notes:**
- 090 ⭐: Kimi K3 — 世界初のオープン3T級モデル（リード候補）
- 091 ⭐: GPT-5.6 モデルガイダンス（新機能・移行手順・プロンプト設計）
- 082: Inkling — Thinking Machines Labの975B オープンウェイトMoE
- 106: 13モデルのCVE検出ベンチマーク（GPT-5.6・Kimi K3が最高スコア）

---

### Theme 3: Grok Build通信解析・Memory Heist・MCP白書が突きつけるAIエージェントのセキュリティ

**Articles (IDs):** 032, 069, 209, 049

**Theme Introduction:**
エージェントが実行権限を持つほど、その攻撃面は現実的な脅威になる。Grok Build CLIがリポジトリ全体や.envを暗号化せず送信していた通信解析、ClaudeのWeb閲覧を悪用した間接プロンプトインジェクション「Memory Heist」、1万1000以上のMCPサーバー調査で判明した深刻な脆弱性、そしてワークフロー経由でガードレールを回避するIDEエージェントの脱獄と、実装・運用レイヤーの具体的な穴が並んだ。

**Editorial Notes:**
- 032: xAI Grok Build CLIのワイヤレベル解析（無断データ送信）
- 069: The Memory Heist — Claudeの記憶を盗む間接プロンプトインジェクション
- 209: MCPセキュリティ白書2026（11,000サーバー調査）
- 049: IDEコーディングエージェントのワークフローレベル脱獄

---

### Theme 4: antirez・Chelsea Troy・「コーディングはボトルネックでない」が問う開発者の役割変容

**Articles (IDs):** 100, 117, 102, 055

**Theme Introduction:**
AIが実装を担う前提で、人間側の専門性がどこに移るかを論じる記事が揃った。antirezは「コードではなくアイデアを支配せよ」と説き、AI生産性調査は真のボトルネックがレビューやCIなど後続工程にあると示す。ジュニア開発者の「センス・判断力」の養い方、そしてPdMから自ら実装する「プロダクトビルダー」への転換まで、役割の再定義が具体的に語られている。

**Editorial Notes:**
- 100: antirez「コードではなくアイデアを支配せよ」
- 117: コーディングは決してボトルネックではなかった（AI生産性調査）
- 102: AI時代のジュニア開発者の生存戦略（センスと判断力）
- 055: PdMをやめて「プロダクトビルダー」へ

---

### Theme 5: 反AI活動家・「人々はAIを求めていない」・Thinking Machinesが示す人間中心への揺り戻し

**Articles (IDs):** 036, 107, 135, 170

**Theme Introduction:**
AI推進一辺倒への対抗軸を示す論考・ルポが目立った週でもある。人類滅亡を危惧しOpenAIに抗議する強硬派活動家のルポ、「ユーザーは生活をAIで埋めたいわけではない」というUX論、AIを分散型ツールとして人間の判断を拡張すると掲げるThinking Machines Labのマニフェスト、そしてデザイン工程からAIを一切排除する書体デザイン会社の哲学と、人間中心の視点が並ぶ。

**Editorial Notes:**
- 036: AIとの「戦争」に備える強硬派活動家たち（WSJ・パワウォール復旧済）
- 107: 人々は生活にもっとAIを求めているわけではない
- 135: Thinking Machines Labの人間中心・分散化ビジョン
- 170: 人間の手から — デザイン工程でAIを使わない理由（Mass-Driver）

---

### Theme 6: NVIDIA循環ファイナンス・SF住宅高騰・広告収益90%未達が映すAI経済の実像

**Articles (IDs):** 200, 201, 146

**Theme Introduction:**
熱狂の裏側にある数字を検証する記事が続いた。NVIDIAが出資しネオクラウドが巨額契約を結ぶ「循環型ファイナンス」の不透明さ、AI長者がサンフランシスコの住宅価格を押し上げ株式決済まで検討される事態、そしてOpenAIの広告収益が自社予測を90%下回るとのアナリスト分析と、AI経済の実像がデータで示されている。

**Editorial Notes:**
- 200: NVIDIA・CoreWeave・NebiusのGPU循環ファイナンス
- 201: AI長者がSF住宅価格を押し上げ（株式決済の検討）
- 146: OpenAIの広告収益、自社予測を90%下回る見通し

---

### Theme 7: 食べログ・デジタル庁源内・金融機関が進める日本企業/行政のAI組織実装

**Articles (IDs):** 228, 195, 218, 065

**Theme Introduction:**
個人の効率化から組織・行政レベルの実装へと軸が移った事例が集まった。食べログはAIを活用しDDDの実装コストを克服した中間データ層「Deal Provider」を構築、デジタル庁はガバメントAI「源内」で国産クラウド・国産LLMの実証を開始した。情報漏洩に厳しい金融機関での全社導入、そしてAI Ready基盤が生んだガバナンス低下への対処（IVRy）まで、実装の現実が語られている。

**Editorial Notes:**
- 228: 食べログの「Deal Provider」— AIで克服したDDD実装
- 195: ガバメントAI「源内」— 国産クラウド・国産LLMの実証
- 218: 金融機関でのClaude・Gemini・ChatGPT全社導入
- 065: AI Readyアーキテクチャの課題と組織最適化（IVRy）

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**
今週はフロンティアモデルの新リリースが集中した。Moonshot AIの「Kimi K3」（オープン3兆パラメータ級）、OpenAIのGPT-5.6ファミリー、Thinking Machines Labの「Inkling」が相次ぎ、CVE検出ベンチマークでGPT-5.6とKimi K3が首位に並ぶなど、性能・価格・オープン性の競争が可視化された。日本語コミュニティでは引き続きClaude Codeのスキル設計とループ/ハーネスエンジニアリングが最大の関心事で、Addy Osmaniの「アウター・ループ」論やAWS aidlc-workflowsの整理が議論を具体化させた。

**もう一つの軸:**
実装が速くなるほど、その周辺の課題が前景化している。セキュリティ面ではGrok Build CLIの無断データ送信、Claudeの記憶を狙う間接プロンプトインジェクション、MCPサーバー1万超の脆弱性調査と、エージェントの実行権限に伴うリスクが具体的に示された。役割論では「コーディングはボトルネックではない」という調査結果を軸に、レビュー・検証・意思決定へと専門性が移る議論が並んだ。

**人間中心と経済の現実:**
AI推進への対抗軸も明確だった。反AI活動家のルポ、「人々はもっとAIを求めていない」というUX論、デザイン工程からAIを排除する哲学など、人間中心の視点が揃う。経済面ではGPU循環ファイナンス、SF住宅高騰、OpenAI広告収益の予測未達と、熱狂の裏の数字が検証された。国内では食べログ・デジタル庁・金融機関の組織/行政レベルの実装事例が、個人の効率化から次の段階へ進んだことを示している。

---

## Curation Signal Summary

**⭐ Standout Articles Used:**
- 090 → Theme 2 (Lead)
- 091 → Theme 2
- 101 → Theme 1 (Lead)

**👍 Upvoted Articles:**
- 020 (GPT-Live 英会話学習) → 明確な分析テーマに収まらない実用系。メイン枠に入れるなら「個人の実用活用」小テーマを新設、そうでなければannex推奨（要判断）
- 070 (プロンプト＋パワポ420点) → 同上。実用リソース系でannex適性も高い（要判断）

**👎 Downvoted Articles (leads禁止、annex/補足のみ):**
- 169 (AIバブル投機的成長) → Theme 6の補足 or annex
- 214 (Inquiry Engineering) → Theme 1/5の補足 or annex
- 226 (成長とか上達って) → Theme 4の補足 or annex
- 005 / 009 / 019 / 220 → annex or omit

**Omitted Articles:** なし（Supabaseでのomitフラグ0件）

---

## Theme Coverage Summary

**Article Count by Theme (Planned):**
- Theme 1 (ループ/ハーネス): 5
- Theme 2 (フロンティアモデル): 4
- Theme 3 (エージェントセキュリティ): 4
- Theme 4 (役割変容): 4
- Theme 5 (人間中心への揺り戻し): 4
- Theme 6 (AI経済の実像): 3
- Theme 7 (日本企業/行政実装): 4

**Total Planned for Main:** ~28 (STEP_04で18–25へ調整)
**Remaining for Annex:** 残り約203件。うちSupabaseフラグ済み annex候補 34件（`curated_annex_journal_sources.md`）を起点にSTEP_05で選定。annexのセクション編成はキュレーターに委ねる。

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-07-18
**Reviewer:** beijaflor

**Changes Made:**
- Approved as drafted (via AskUserQuestion approval gate; popup closed without inline edits)

**Approval:** ✅ APPROVED

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)
