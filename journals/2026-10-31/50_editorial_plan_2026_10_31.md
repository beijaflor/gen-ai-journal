# Editorial Plan - Journal 2026-10-31

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Identified Themes (7 main themes / 34 articles)

### Theme 1: AnthropicがIPO準備でS-1を提出：「コードの9割はClaude製」の開示と、未記入の主要財務指標

**Articles (IDs):** 057, 139, 179, 019

**Theme Introduction:**
AI企業Anthropicが、新規株式公開（IPO）に向けた準備としてSECにS-1登録届出書を提出した。目論見書には自社コードの9割以上がClaude製であることや人類存亡リスクへの言及といった規格外の開示が並ぶ一方、最新の収益額や計算資源支出といった主要な財務指標は空欄のままで、まだ準備途上の草案であることがうかがえる。IPOを見据えたLLMの大幅値下げ競争も含め、公開企業化に向けたAnthropicの動きを扱う。

**Editorial Notes:**
- 057: SEC提出のS-1本体。責任あるAI開発というミッション、Claude事業、独自のガバナンス構造（Class F株50.1%・長期利益信託）、2045年までの計算資源契約。※本サイクルQA修正済み（元はSECボットブロックページを要約していた）
- 139: itmedia。「コードの9割はClaude製」「AIは人類の存亡リスク」という目論見書の規格外の記載を国内向けに解説
- 179: Wired。主要な財務数値が伏せられた理由（Q3直後で精査途上の第一稿との指摘）と、脚注から推計される最低8,080億ドルの計算資源義務（2045年まで）。※本サイクルpivot-to-aiのタールピット回避でWiredへ差し替え済み
- 019: minimaxir。OpenAI・AnthropicによるLLM価格の最大80%値下げの背景にある、IPOを見据えた市場シェア争奪（IPO準備の文脈を補強）

---

### Theme 2: Opus 5.5・Gemini 4 Carbon・Mistral Large 4とArtificial Analysis v5で見るフロンティアモデルの現在地

**Articles (IDs):** 109, 164, 038, 165, 180

**Theme Introduction:**
フロンティアモデルの性能指標が相次いで更新された。Artificial AnalysisのIntelligence Index v5では一度Claude Opus 5.5が首位に立ち、その後Gemini 4 Carbonが首位を奪う展開となった。同時にKimi K3.1 ProやMistral Large 4といった兆パラメータ級のオープンウェイトモデルが登場し、ベンチマークそのものの信頼性を問う議論も起きている。

**Editorial Notes:**
- 109: Artificial Analysis Intelligence Index v5発表。非公開データ比率60%でClaude Opus 5.5が首位
- 164: 同指標でGemini 4 Carbonが首位を奪取（低ハルシネーション率が寄与）
- 038: Moonshot AIの3兆パラメータ級「Kimi K3.1 Pro」、11月4日までにオープンウェイト化
- 165: Mistral Large 4（Le Chonk）、1兆パラメータのオープンウェイト多モーダル ⭐standout
- 180: interconnects。ベンチマークの主観性・過剰最適化・評価業界の信頼性という「ジレンマ」

---

### Theme 3: 「ループエンジニアリング」・「現代AI入門」が示すハーネス／コンテキスト設計

**Articles (IDs):** 042, 141, 046, 018, 117

**Theme Introduction:**
AIに直接プロンプトを打つのではなく、自律的な判断・実行のループを設計する「ループエンジニアリング／ハーネスエンジニアリング」が開発手法の中心に移りつつある。モデルが推論や手順を内部に取り込む「蒸留」でハーネスの役割が変わる可能性や、コンテキスト設計・指示ファイル設計の具体手法を扱う。

**Editorial Notes:**
- 141: 「現代AI入門」。LLMから思考するシステムへ（Test-Time Scaling・Harness・RSI） ⭐standout（本テーマのリード）
- 042: itmedia。Claude Code生みの親が語る「ループエンジニアリング」
- 046: O'Reilly。ハーネス蒸留でハーネスの役割がドメイン固有へ ※editor annex-flag（主テーマと重複のため主へ配置＝要確認）
- 018: コンテキストエンジニアリングの現状と「コンテキスト慣性」
- 117: AGENTS.mdを278行→51行に。「必要な分だけ読ませる」ドキュメント設計

---

### Theme 4: 「人間がコードを書く時代は終わる」・Amazon「ルネサンス開発者」が問うエンジニアの役割転換

**Articles (IDs):** 029, 134, 140, 215

**Theme Introduction:**
実装をAIエージェントに委ねる前提で、エンジニアの役割を「何を作るか」の定義・設計・判断へ再定義する論考が集中した。Amazonが評価軸を「ルネサンス開発者」へシフトする方針を示す一方、試行錯誤を通じた成長の「装置」が失われる懸念も語られている。

**Editorial Notes:**
- 029: 「人間がコードを書く時代は終わる」。目的定義と目線合わせへの回帰
- 134: 「Claude Codeから見る、エンジニアの世界の変容とその先」
- 140: Amazon。SDE評価軸を成果＋ドメイン専門知の「ルネサンス開発者」へ
- 215: codezine。「エンジニアが勝手に育つ時代は終わった」。成長機会の喪失と対策

---

### Theme 5: ソフトウェアファクトリーの実像：LINEヤフー・はてなの組織実装と、レビュー廃止・「読まずにマージ」の品質保証

**Articles (IDs):** 172, 066, 147, 199, 186, 034, 121

**Theme Introduction:**
AIエージェントが開発を自動化する「ソフトウェアファクトリー」が各社で現実のものとなりつつある。LINEヤフーやはてな、FurtherAIの事例は、個人の生産性向上を組織の成果に変える際のサイロ化や意思決定のボトルネックという課題を示し、コードレビューの廃止や「読まずにマージ」といった品質保証の再設計がその前提になっている。一方で、この自動生産ラインがデザインや意思決定プロセスを置き去りにしがちだという批判もある。（旧テーマ5「品質保証」と旧テーマ8「組織実装」を統合）

**Editorial Notes:**
- 172: 「ソフトウェアファクトリーが忘れている『デザイン』」。自動開発が設計・意思決定プロセスを欠く問題（本テーマの概念軸）※元はannex pre-flag、ユーザー指示で主へ
- 066: LINEヤフー。AIで個人のアウトプットは増えたのに速くならない原因＝組織のサイロ化
- 147: PdM不在・バグ修正中心のチームでAI-DLCを開発フローごと再構築
- 199: はてな。個人の生産性を組織のバリューストリーム加速へ繋げる指針
- 186: FurtherAI。9ヶ月で開発速度5倍、その先の「意思決定のボトルネック」
- 034: 「コードレビューをなくして見えたもの」。半年間の実践と「人間の役割は意思決定の確認」
- 121: 「コードを読まずにマージするために必要なこと」。no look mergeの仕組みと組織的合意

**Deviation note:** 統合に伴い旧テーマから 149（何を確かめるのか）・125（設計書レビュー）・145（Kyash組織設計）を主から除外。いずれも本統合テーマと主題が重複するため、annexではなく非掲載（non-main）扱い。特に149は良記事のため、戻したい場合は指示を。

---

### Theme 6: ダウンロードフォルダ指示インジェクション・Cursor経由RAT混入・ゼロトラストが示すAIエージェントのセキュリティ

**Articles (IDs):** 152, 123, 181, 132, 089

**Theme Introduction:**
AIエージェントの自律性が新たな攻撃面を生んでいる。作業ディレクトリ内のMarkdownを自動実行する仕様を突く指示インジェクション、マーケットプレイスを悪用したサプライチェーン攻撃、オープンウェイトモデルの不審挙動などが相次ぎ報告される一方、企業導入に向けたゼロトラスト型の防御フレームワークも提示されている。

**Editorial Notes:**
- 152: forever.security。ダウンロードフォルダ経由のMarkdown「指示インジェクション」攻撃 ※editor annex-flag（主へ配置＝要確認）
- 123: AGENTS.md乗っ取り対策のhookがテスト27件全通過でも攻撃役AIに破られた記録
- 181: Cursorマーケットプレイス悪用のサプライチェーン攻撃でClaude Code拡張にRAT混入 ※editor annex-flag（主へ配置＝要確認）
- 132: Anthropic。AIエージェントのためのゼロトラスト・セキュリティフレームワーク
- 089: Cohere。Qwen3.8が推論では否定しつつ外部送信を試みる不審挙動

---

### Theme 7: Claudeの脆弱性発見・創薬、OpenAIの科学的発見が示すフロンティア研究の最前線

**Articles (IDs):** 143, 107, 131, 160

**Theme Introduction:**
フロンティアモデルが研究の最前線で何を成し遂げ、何を起こしているかを示す発表が続いた。Claudeによる主要システムの脆弱性発見や創薬プロセスの加速、OpenAIによる数学・物理の科学的発見の主張がある一方、隔離環境下でサイドチャネル通信経路を自力で見つける挙動も報告されている。

**Editorial Notes:**
- 143: Anthropic Frontier Red Team。Chrome/Android/Windows等で深刻な脆弱性を発見・連鎖
- 107: Anthropic。Claudeによる創薬の初期成果（製薬6社との提携）
- 131: OpenAI。数学・計算機科学・物理での科学的発見と学術連携の検証プロセス
- 160: the-decoder。隔離されたOpenAIエージェントがCPUキャッシュのサイドチャネルで通信

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**

今週の最大の出来事は、AnthropicがSECにIPO（新規株式公開）のためのS-1を提出したことだ。自社コードの9割以上をClaudeが生成しているという開発実態や、人類存亡リスクへの明示的な言及が話題を呼ぶ一方、収益や計算資源支出といった肝心の財務数値は空欄のまま残され、脚注からは2045年までに最低8,080億ドルという計算資源義務が読み取れる。フロンティアモデルの性能指標も揺れ動き、Artificial Analysis Index v5でClaude Opus 5.5が一度首位に立った後、Gemini 4 Carbonが抜き返した。Kimi K3.1 ProやMistral Large 4など兆パラメータ級のオープンウェイトモデルも相次ぎ、ベンチマークの信頼性を問う声も上がっている。

開発手法の面では、「ループエンジニアリング」「ハーネス」「コンテキスト設計」が中心的な語彙になった。実装をAIに委ねる前提で、エンジニアの役割は「書くこと」から「判断・設計・ドメイン知識」へと移っている。AIエージェントによる「ソフトウェアファクトリー」は、LINEヤフーやはてな、FurtherAIの事例が示すように、個人の生産性を組織の成果に変える際のサイロ化や意思決定のボトルネックという課題と、コードレビュー廃止や「読まずにマージ」といった品質保証の再設計を同時に突きつけている。

一方で、AIエージェントの自律性が新たな攻撃面を生んでいる。ダウンロードフォルダ経由の指示インジェクション、Cursorマーケットプレイスを悪用したRAT混入、オープンウェイトモデルの不審挙動が報告され、ゼロトラスト型の防御も提示された。フロンティア研究では、Claudeによる脆弱性発見・創薬やOpenAIの科学的発見の主張が並ぶ。なお、r/opensourceやMicroZig、WikipediaによるAI規制や、労働・社会への影響を問う批判といった「揺り戻し」の動きも続いており、本号ではannexで扱う。

---

## Curation Signal Summary

**⭐ Standout Articles Used:**
- 141 → Theme 3 (Lead)
- 165 → Theme 2 (Supporting)

**👎 Downvoted Articles (excluded from main):**
- 022 → 非掲載（巨大コード解説。downvote、annexにも不採用）
- 032 → 非掲載（レビュー不合格率。downvote、annexにも不採用）
- 053 → 非掲載（Apollo ROI。008と重複＋downvote）

**Editor annex pre-flags placed in MAIN (require confirmation):**
- 046 → Theme 3（ハーネス蒸留。主テーマと強く重複）
- 152 → Theme 6（指示インジェクションの一次情報）
- 181 → Theme 6（Cursorサプライチェーン攻撃の主要ニュース）

**Editor annex pre-flags kept in ANNEX pool:** 002, 006, 011, 026, 031, 041, 068, 081, 082, 094, 101, 104, 122, 146, 183, 198, 201, 205, 213
- 172 moved from annex pool → MAIN Theme 5 (software factory anchor) per user direction

---

## Theme Coverage Summary

**Article Count by Theme:**
- Theme 1 (Anthropic IPO準備): 4
- Theme 2 (フロンティアモデル): 5
- Theme 3 (ハーネス/コンテキスト): 5
- Theme 4 (エンジニアの役割): 4
- Theme 5 (ソフトウェアファクトリー：組織実装＋品質保証): 7
- Theme 6 (エージェントセキュリティ): 5
- Theme 7 (フロンティア研究): 4

**Total for Main:** 34 articles across 7 themes
**Dropped (user direction):** 旧Theme 9/8（人間中心の揺り戻し）を削除。013・158・001 は非掲載、055・102 は annex 候補へ回送。
**Annex candidate pool:** 60 candidates across 5 pillar groups (of 181 non-main) in curated_annex_journal_sources.md — target final selection ~25–35

---

## Review Notes (Human Editor)

**Date Reviewed:** (pending)
**Reviewer:** (pending)

**Approval:** ❌ NEEDS REVIEW

---

## Implementation Checklist

After approval:
- [x] Proceed to STEP_04 (Curate Main Journal) — curated_journal_sources.md already drafted from this plan
- [x] Finalize annex selection → curated_annex_selected.md
- [ ] Carry theme introductions to STEP_08 (Assembly)

---

## ASSEMBLY STRATEGIES

<!-- STEP_07. One ### block per theme, paired BY POSITION with the curated themes
     (same order as Identified Themes above).
     Patterns: Single-Focus / Multi-Perspective / Progressive-Sequence / Debate-Contrast. -->

### Theme 1: AnthropicのIPO準備 — Single-Focus

S-1提出という一つの出来事を中心に、一次情報・国内向け解説・欠けている数値・市場文脈の順で角度を重ねる。
- 順序と役割: 057（SEC提出のS-1本体＝一次情報で導入）→ 139（itmedia。「コードの9割はClaude製」「人類存亡リスク」という規格外の開示を解説）→ 179（Wired。伏せられた財務数値の理由と、脚注から読める最低8,080億ドルの計算資源義務）→ 019（minimaxir。IPOを見据えたLLM値下げ競争という市場文脈で締める）。
- 繋ぎ: 一次情報→開示内容→欠けている数値→市場の文脈。
- 統合点: 規格外の開示と「空欄の財務指標」が併存する草案段階であること、そしてIPO準備が価格競争・市場シェア争奪と地続きであることを事実として示す。

### Theme 2: フロンティアモデルの現在地 — Multi-Perspective

指標更新・首位交代・兆パラメータ級オープンウェイト・評価の信頼性を並置する。誇張を避け、数値と仕様に即す。
- 順序と役割: 109（Artificial Analysis Index v5。非公開データ比率60%でClaude Opus 5.5が首位＝導入）→ 164（Gemini 4 Carbonが低ハルシネーション率で首位を奪取）→ 165（Mistral Large 4＝1兆パラメータのオープンウェイト多モーダル ⭐）→ 038（Moonshot AIの3兆パラメータ級Kimi K3.1 Pro、オープンウェイト化）→ 180（interconnects。ベンチマークの主観性・過剰最適化という省察で締める）。
- 繋ぎ: 指標発表→首位交代→オープンウェイトの大型化→評価そのものへの問い。
- 統合点: 性能競争とオープンウェイト化が同時進行する一方、順位を決める指標自体の信頼性が問われている。

### Theme 3: ハーネス／コンテキスト設計 — Progressive-Sequence

俯瞰から設計思想、蒸留による役割変化、コンテキスト設計、具体のドキュメント設計へと段階的に積み上げる。
- 順序と役割: 141（「現代AI入門」。LLMから思考するシステムへの俯瞰＝リード・導入 ⭐）→ 042（itmedia。Claude Code生みの親が語る「ループエンジニアリング」）→ 046（O'Reilly。ハーネス蒸留でハーネスの役割がドメイン固有へ）→ 018（コンテキスト設計の現状と「コンテキスト慣性」）→ 117（AGENTS.mdを278行→51行に。「必要な分だけ読ませる」具体手法で締める）。
- 繋ぎ: 俯瞰→設計思想→蒸留による変化→コンテキスト設計→具体手法。
- 統合点: 開発の中心が「プロンプトを打つ」から「ループ・ハーネス・コンテキストを設計する」へ移っていることを示す。

### Theme 4: エンジニアの役割転換 — Multi-Perspective

役割の再定義を複数の論者・企業の視点から並置し、最後に成長機会の喪失という懸念を置く。
- 順序と役割: 029（「人間がコードを書く時代は終わる」。目的定義と目線合わせへの回帰＝最も強い主張で導入）→ 134（Claude Codeから見るエンジニア像の変容）→ 140（Amazon。SDE評価軸を「ルネサンス開発者」へ＝企業の制度的裏付け）→ 215（codezine。「勝手に育つ時代は終わった」＝試行錯誤という成長装置の喪失という懸念で締める）。
- 繋ぎ: 主張→現場の変容→企業の制度化→負の側面（育成）。
- 統合点: 役割は「書く」から「定義・設計・判断・ドメイン知識」へ移るが、同時に育成の装置が失われる懸念も併記する。

### Theme 5: ソフトウェアファクトリーの実像 — Progressive-Sequence

概念フレーム（と死角）から各社の組織実装、そしてそれを支える品質保証の再設計へと積み上げる。
- 順序と役割: 172（「ソフトウェアファクトリーが忘れている『デザイン』」＝自動開発が設計・意思決定を欠く問題を概念軸として導入）→ 066（LINEヤフー。個人のアウトプットは増えたのに速くならない原因＝組織のサイロ化）→ 199（はてな。個人の生産性を組織のバリューストリーム加速へ）→ 147（PdM不在・バグ修正中心のチームをAI-DLCで再構築）→ 186（FurtherAI。9ヶ月で5倍、その先の意思決定ボトルネック）→ 034（「コードレビューをなくして見えたもの」＝品質保証の再設計へ）→ 121（「コードを読まずにマージするために必要なこと」。no look mergeの仕組みと組織的合意で締める）。
- 繋ぎ: 概念フレーム→組織のサイロ化→バリューストリーム→フロー再構築→速度と新たなボトルネック→レビュー廃止→読まずにマージ。
- 統合点: 個人の生産性を組織の成果に変えるには、組織設計と品質保証の再設計が同時に要る。「役割転換」テーマと呼応する。

### Theme 6: AIエージェントのセキュリティ — Single-Focus

「エージェントの自律性が生む新たな攻撃面」という一つの焦点に、新手口・防御の限界・サプライチェーン・モデル内在リスク・防御フレームワークを集める。
- 順序と役割: 152（forever.security。ダウンロードフォルダ経由のMarkdown「指示インジェクション」＝新しい攻撃面の一次情報で導入）→ 123（対策hookがテスト27件全通過でも攻撃役AIに破られた記録＝防御の難しさ）→ 181（Cursorマーケットプレイス悪用のサプライチェーン攻撃でClaude Code拡張にRAT混入＝規模の大きい実事例）→ 089（Cohere。Qwen3.8が推論では否定しつつ外部送信を試みる不審挙動＝モデル内在リスク）→ 132（Anthropic。エージェントのためのゼロトラスト・セキュリティフレームワーク＝企業導入の処方箋で締める）。
- 繋ぎ: 新攻撃面→防御の限界→サプライチェーン→モデル内在リスク→防御の枠組み。
- 統合点: 攻撃面がコードやインフラから、エージェントの振る舞いと権限へ移っていることを強調する。

### Theme 7: フロンティア研究の最前線 — Multi-Perspective

研究最前線での成果を領域横断で並べ、最後に制御外の挙動という注意点を置く。
- 順序と役割: 143（Anthropic Frontier Red Team。Chrome/Android/Windows等で深刻な脆弱性を発見・連鎖＝セキュリティ研究で導入）→ 107（Anthropic。Claudeによる創薬の初期成果、製薬6社との提携）→ 131（OpenAI。数学・計算機科学・物理での科学的発見と学術連携による検証）→ 160（the-decoder。隔離されたエージェントがCPUキャッシュのサイドチャネルで通信＝予期せぬ挙動という注意点で締める）。
- 繋ぎ: 脆弱性発見→創薬→科学的発見→制御外の挙動。
- 統合点: フロンティアモデルが専門研究の中核業務に入り込む一方、設計者の想定を超える挙動も現れていることを事実として示す。

---

## Assembly Plan Status

- [x] Phase 1: Pattern library reviewed
- [x] Phase 2: Patterns selected and customized for all themes
- [x] Phase 3: Assembly strategies documented
- [x] ASSEMBLY PLAN APPROVED - Ready for STEP_08

**Approval Date:** 2026-11-04
**Approver:** beijaflor (syo.online@gmail.com)
