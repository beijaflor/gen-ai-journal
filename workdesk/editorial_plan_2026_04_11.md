# Editorial Plan - Journal 2026-04-11

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Identified Themes

**Reminder: Theme titles should be concrete, specific, and factual**
- Name specific technologies, people, events, numbers
- List key topics covered in the theme
- Avoid generic category labels or dramatic/narrative framing

---

### Theme 1: Managed Agents・Advisor Strategy・Cowork — Anthropicプラットフォーム戦略の一週間

**Articles (IDs):** 166, 082, 098, 072, 036, 046, 038, 045, 219, 068, 076

**Theme Introduction (2-3 sentences in Japanese):**
Anthropicが今週、Managed Agents、Advisor Strategy、Cowork統制機能強化という3つの主要機能を相次いで発表した。エージェントの「脳と手の分離」アーキテクチャ、Opusの知能をSonnet/Haikuに統合するコスト最適化戦略、そしてエンタープライズ向けガバナンス機能が一挙に公開されている。さらに独自AIチップ開発の検討報道も加わり、Anthropicのプラットフォーム戦略の全体像が明確になった週である。

**Editorial Notes:**
- 166: Claude Managed Agents公式発表
- 082: Managed Agentsのスケーリング（脳と手の分離アーキテクチャ）
- 098: Managed Agents APIドキュメント概要
- 072: Managed Agentsハンズオン実践
- 036: Managed Agentsを触ってみた初期レビュー
- 046: Advisor Strategy（Opusの知能をSonnet/Haikuに統合）
- 038: Cowork統制機能のエンタープライズ強化
- 045: Anthropic独自AIチップ開発検討（Reuters報道）
- 219: Anthropic-Google-Broadcom提携（TPUインフラ）
- 068: Claude Codeに広告運用を1ヶ月任せた実践事例
- 076: PMがClaude Codeで本来の仕事を取り戻す

---

### Theme 2: ハーネスエンジニアリング・DESIGN.md・仕様駆動開発 — エージェント時代の「意図の設計」

**Articles (IDs):** 285, 245, 084, 268, 156, 133, 095, 078, 174, 171, 066, 050, 011

**Theme Introduction (2-3 sentences in Japanese):**
AIがコードを書く時代に、開発者の役割は「意図の定義」と「制御構造の設計」へ移行している。今週は、Spec-Driven Development・Context Engineering・Harness Engineeringの3概念を統合する論考、Google StitchのDESIGN.md仕様、そしてO'ReillyによるArchitecture as Codeの提言が集中した。ハーネスエンジニアリングの複数解釈を整理する記事や、使い捨て仕様書の実践報告など、理論と現場の両面から「エージェントの制御」を論じる記事が揃っている。

**Editorial Notes:**
- 285: Spec・Context・Harness三層設計の統合論考
- 245: ハーネスエンジニアリングの複数解釈整理（2026年版）
- 084: ハーネスエンジニアリングは枠組みから始めよう（CADDi）
- 268: Google Stitch DESIGN.md概要（AIのためのデザインシステム仕様）
- 156: awesome-design-md-jp（日本語UI向け）
- 133: awesome-design-md（VoltAgent）
- 095: DESIGN.md導入ガイドと採用記録
- 078: 仕様書は"使い捨て"にした方がうまくいった
- 174: デザインシステムをSkillsにする（サイボウズ）
- 171: SDD×マルチエージェントシステム
- 066: AIエージェント時代のクリーンコード
- 050: Architecture as Codeで人間とエージェントに設計を教える（O'Reilly）
- 011: エージェントは「何が良い状態か」を知らない（O'Reilly）

---

### Theme 3: Claude Mythos Preview・Project Glasswing・DFC — AIサイバーセキュリティの新章

**Articles (IDs):** 182, 153, 128, 276, 074, 109, 117, 141, 054, 102

**Theme Introduction (2-3 sentences in Japanese):**
Anthropicが公開したClaude Mythos Previewは、24時間以内にゼロデイ脆弱性を発見する能力を持つサイバーセキュリティ特化モデルであり、オープンソース化されたProject Glasswingとともにリリースされた。同時に、異なるモデル間の行動差異を自動検出する「Dedicated Feature Crosscoder（DFC）」手法も発表されている。MicrosoftのAgent Governance ToolkitやMozillaの0dinスキャナー発表も重なり、AIセキュリティが研究段階から実戦配備段階へ移行した週となった。

**Editorial Notes:**
- 182: Claude Mythos Previewのサイバーセキュリティ能力（ゼロデイ発見）
- 153: Project Glasswing公式発表（オープンソース防衛ツール）
- 128: Simon WillisonによるGlasswing解説
- 276: AIの「差分」ツールDFC（異なるモデル間の行動差異検出）
- 074: Mythos Previewの性能が桁外れ（実践検証）
- 109: Microsoft Agent Governance Toolkit（エージェント実行時セキュリティ）
- 117: AIエージェント間の不可視な通信（ステガノグラフィ論文）
- 141: Internet Bug Bounty報奨金一時停止
- 054: Mozilla 0din AIセキュリティスキャナー発表
- 102: Astralのオープンソースセキュリティ実践（Ruff/uv）

---

### Theme 4: Bram Cohen批判・CSRF見落とし・COBOL脆弱性・ETH Zurich調査 — バイブコーディングのリスク集中

**Articles (IDs):** 183, 114, 169, 057, 252, 287, 016, 007, 005, 065

**Theme Introduction (2-3 sentences in Japanese):**
BitTorrent創設者のBram Cohen氏がバイブコーディングを「狂気」と断じた記事を筆頭に、AI生成コードの品質リスクに関する報告が今週集中した。Claude CodeとCodexの双方がCSRF脆弱性を見落とした実証、LLMにCOBOLを書かせた結果リモートコード実行の脆弱性が生まれた事例、ETH Zurichの調査によるバグ密度1.7倍の定量データなどが揃っている。Dave Winer氏によるAI生成コードの保守性調査提案や、OpenBSDにおけるAI生成コードの著作権問題も報じられた。

**Editorial Notes:**
- 183: Bram Cohenがバイブコーディングを「狂気」と批判
- 114: なぜ大半のVibe Codingプロジェクトは失敗するのか（Reddit分析）
- 169: Claude CodeもCodexもCSRF脆弱性を見落とした
- 057: LLMでCOBOLを書かせたらRCE脆弱性が発生
- 252: ETH Zurich調査 — バイブコーディングでバグ密度1.7倍
- 287: Dave Winer — AIボットは保守可能なコードを書けるか？
- 016: OpenBSDにおけるAI生成ext4と著作権問題
- 007: AIコード書き換えがOSSの法的基盤を揺るがす
- 005: バイブコーディングがデザインの権威を損なわせている
- 065: コードが安価になった今、エンジニアリングの価値はどこに

---

### Theme 5: コグニティブ・サレンダー・意思決定疲れ・並列エージェント認知負荷 — AI支援開発の人間コスト

**Articles (IDs):** 181, 146, 103, 157, 092, 116, 044, 027

**Theme Introduction (2-3 sentences in Japanese):**
AI支援開発がもたらす認知面の負荷について、今週は複数の独立した報告が収束した。Gizmodoが提唱した「コグニティブ・サレンダー（認知の降伏）」概念、Addy Osmaniが論じたAIエージェント並列稼働時の「Comprehension Debt（理解負債）」、RCT研究によるChatGPT利用後の知識保持率低下、そしてAIコーディングが引き起こすギャンブル依存類似の精神的消耗が報告されている。USC研究のAIによる思考・文章の均一化リスクも含め、AI活用の「人間側のコスト」を多角的に検証する記事が集まった。

**Editorial Notes:**
- 181: コグニティブ・サレンダー（認知の降伏）概念
- 146: AI効率化と意思決定のしんどさ（個人体験）
- 103: AIコーディングが精神を壊す（ギャンブル依存類似）
- 157: Addy Osmani — AIエージェント並列稼働の人間側の限界（Comprehension Debt）
- 092: ChatGPTは認知の松葉杖（RCT研究：知識保持率低下）
- 116: AIによる思考と文章の均一化リスク（USC研究）
- 044: 不要になるのはジュニアではなく教える機会を奪われた中堅
- 027: Claude Codeが書いたコードをチームのコードにする（理解負債対策）

---

### Theme 6: Gemma 4・LLM-jp-4・PLaMo 3.0・Bonsai 1-bit — 新モデルラッシュとローカルAI

**Articles (IDs):** 282, 270, 286, 137, 178, 261, 135, 148, 127, 149, 274, 273, 251, 126

**Theme Introduction (2-3 sentences in Japanese):**
Google DeepMindがApache 2.0ライセンスで公開したGemma 4シリーズを中心に、今週は新モデルのリリースが集中した。国立情報学研究所のLLM-jp-4はGPT-4oを日本語ベンチマークで上回り、Preferred Networksはプリファードネットワークス初の日本語推論モデルPLaMo 3.0 Prime betaを公開、1-bit量子化のBonsai 8BはRaspberry Piでの動作が実証されている。これらのモデルをMac・ブラウザ・Raspberry Piなどのローカル環境で実行する実践記事も多数出ており、ローカルAIの実用段階への到達を示す週となった。

**Editorial Notes:**
- 282: Gemma 4完全解説（性能・アーキテクチャ・競合比較）
- 270: Gemma 4ローカル実行ガイド（Unsloth Documentation）
- 286: LLM-jp-4公開（GPT-4o超えスコア）
- 137: PLaMo 3.0 Prime beta（PFN日本語推論モデル）
- 178: GLM-5.1（SWE-Bench Pro 1位）
- 261: Bonsai 8B 1-bit LLM発表
- 135: Gemma 4を8GB MacBook Neoで動作
- 148: 1-bit LLM Bonsai on Pixel 7a
- 127: Bonsai-8B-mlx + Goose ローカルエージェント
- 149: LM StudioとClaude Codeでローカル推論
- 274: AITuberKitとGemma 4でゲーム実況
- 273: DGX SparkでGemma 4 31B + OpenClaw
- 251: DGX Spark Gemma 4ベンチマーク
- 126: Gemma 4リリース解説（ローカルLLM視点）

---

### Theme 7: OpenAI — Stargate UK凍結・ChatGPT広告導入・フロリダ州調査・投資家のAnthropic移行

**Articles (IDs):** 069, 021, 035, 136, 206, 020, 142, 143, 032, 037, 022, 024

**Theme Introduction (2-3 sentences in Japanese):**
OpenAIは今週、複数の方面からの圧力に直面している。Stargate UKプロジェクトの一時凍結、ChatGPTへの広告導入テスト開始、フロリダ州司法長官によるFSU事件関連の調査開始が報じられた。New Yorker誌によるサム・アルトマンの信頼性を問う大型プロフィール記事、LA Timesが報じた投資家のAnthropicへの移行、そしてAI大規模惨事の責任制限法案への支持表明が重なり、ビジネス・規制・社会的信頼のすべてで課題が表面化した週である。

**Editorial Notes:**
- 069: OpenAI Stargate UK計画を一時凍結（エネルギーコスト）
- 021: ChatGPTでの広告表示テスト開始
- 035: フロリダ州司法長官がOpenAIを調査（FSU事件関連）
- 136: New Yorker — サム・アルトマンの信頼性を問う
- 206: LA Times — 投資家がOpenAIからAnthropicへ急移行
- 020: OpenAIがAI大規模惨事の責任制限法案を支持
- 142/143: OpenAI産業政策提言（超知能時代の国家戦略）
- 032: OpenAI投資家にAnthropicに対する計算資源優位性を強調
- 037: サム・アルトマン「ChatGPTにタイマー機能は1年かかる」
- 022: サム・アルトマン宅に火炎瓶（社会的反発）
- 024: サム・アルトマン声明 — AGIへの道

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**

今週のGenAI週刊は、Anthropicのプラットフォーム戦略が一気に可視化された週として記録される。Managed Agents、Advisor Strategy、Cowork統制機能の連続発表に加え、サイバーセキュリティ特化のClaude Mythos PreviewとProject Glasswingの公開は、同社がAIエージェントの「開発・運用・防御」全レイヤーを押さえにきたことを示している。

対照的にOpenAIは、Stargate UK凍結、ChatGPT広告導入、規制当局の調査、そしてNew Yorker誌による批判的プロフィール記事と、複数の逆風に直面している。投資家のAnthropicへの移行を報じたLA Timesの記事は、AI業界の勢力図が変動しつつあることを示唆している。

技術面では、ハーネスエンジニアリング・DESIGN.md・仕様駆動開発が「エージェントの制御構造」という共通軸で収束しつつあり、Google DeepMindのGemma 4を筆頭に、LLM-jp-4やPLaMo 3.0など新モデルのローカル実行が実用段階に達した。一方で、バイブコーディングのリスクを指摘する声も集中しており、Bram Cohenの「狂気」批判、CSRF脆弱性の見落とし、COBOL生成での脆弱性発生など、AI生成コードの品質問題が定量的に裏付けられている。

さらに注目すべきは、AI支援開発の「人間側のコスト」を論じる記事群の登場である。コグニティブ・サレンダー、並列エージェントのComprehension Debt、AIによる思考の均一化といった、ツールの性能向上とは逆方向の問題提起が複数の独立したソースから同時に現れた点は、今週の重要な特徴である。

**Key Points to Cover:**
1. Anthropicの3連続プラットフォーム発表（Managed Agents、Advisor Strategy、Cowork）
2. Mythos Preview / Glasswingによるサイバーセキュリティの実戦配備
3. ハーネスエンジニアリング・DESIGN.md・仕様駆動開発の収束
4. Gemma 4・LLM-jp-4・PLaMo 3.0のローカルAI実行
5. バイブコーディングのリスクの定量的裏付け
6. コグニティブ・サレンダーと認知コストの多角的検証
7. OpenAIの多面的プレッシャー

---

## Curation Signal Summary

**⭐ Standout Articles Used:**
- (No Supabase flags available — proceed without)

**👍 Upvoted Articles Used:**
- (No Supabase flags available)

**👎 Downvoted Articles:**
- (No Supabase flags available)

**Omitted Articles:** (No Supabase flags available)

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: 18-25 articles across 7 themes
- Annex Journal: Remaining articles

**Article Count by Theme (Candidate Pool — to be narrowed in STEP_04):**
- Theme 1 (Anthropicプラットフォーム): 11 candidates
- Theme 2 (ハーネス/DESIGN.md): 13 candidates
- Theme 3 (サイバーセキュリティ): 10 candidates
- Theme 4 (バイブコーディング批判): 10 candidates
- Theme 5 (認知コスト): 8 candidates
- Theme 6 (新モデル/ローカルAI): 14 candidates
- Theme 7 (OpenAI): 12 candidates

**Total Candidates:** ~78 articles (to be narrowed to 18-25 in STEP_04)
**Remaining for Annex:** ~196 articles (to be reviewed in STEP_05)

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-04-18
**Reviewer:** Human Editor

**Changes Made:**
- Reviewed all 7 themes — approved as-is

**Approval:** ✅ APPROVED

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)
