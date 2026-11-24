# Editorial Plan - Journal 2026-11-21

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

> Source pool: 269 summaries (IDs 001–275, gaps at 019/093/155/191/224/238). 1:1 sources↔summaries, schema-valid.
> Human curation signals this cycle (from `curation_flags.md`): ⭐ 272 ／ 👎 045, 061 ／ no omit.
> Supabase annex pre-flags (28, from `curated_annex_journal_sources.md`): 022, 025, 046, 047, 048, 051, 053, 058, 067, 069, 071, 076, 078, 083, 084, 090, 092, 114, 124, 131, 139, 146, 174, 194, 242, 252, 258, 262. (053 and 069 carry ⭐ *and* annex flags — see Curation Signal Summary.)
> Draft scope: **7 main themes / 36 articles** (inside the 6–9 / 30–40 spec). Order below = editorial priority (lead theme first). The remaining ~233 summaries route to annex/omit in STEP_04/05.
> 👎 045/061 are not used as leads or theme-drivers (route to annex). No Supabase annex pre-flagged article is placed in main. ⭐ 272 leads Theme 1 (the only main standout).

> **Revision history (human direction via gate):**
> - **Rev.1:** reduced 8 themes → 6 (merged model+science; merged harness+verification).
> - **Rev.2:** per human direction — (a) **split** the merged model+science theme back into two, with **AIの数学・科学（リーマン予想中心）as the lead Theme 1** — the week's most important story; frontier-model launches become **Theme 2**; (b) **de-prioritized Themes 6 (判断特化型AI) and 7 (Anthropic上場・市場)** to the bottom of the order, as both continue last issue's (2026-11-14) themes; (c) moved 239 (Re:Riemann) into the flagship Theme 1 as the human-agency response to the Riemann claim. Harness+verification merge (Theme 3) retained from Rev.1.

> **Continuity with last issue (2026-11-14).** Themes 6 and 7 continue last issue's Decision-Models and Anthropic-IPO storylines (hence de-prioritized); their intros state what is new this week. Stories already run in last issue's **main** are kept **out of main** here: the ESLint paid-contributor shutdown (this week's 007) and the No-AI-Slop manifesto (this week's 077) → annex. The freshest untouched clusters (GEO; Japanese enterprise agent adoption) are in **Candidate Themes for Review**.

---

## Identified Themes (7 main themes / 36 articles)

**Reminder: titles are concrete, specific, factual — named anchors + single verb + substantive topic phrase.**
**Order below = editorial priority (lead theme first).**

### Theme 1: リーマン予想・ブラックホール物理・15万論文監査に見るAIの数学・科学成果と人間の検証・応答

**Articles (IDs):** 272, 225, 015, 164, 239

**Theme Introduction:**
今週の最大のトピックは、AIが数学・科学の最前線で具体的な成果を主張した一連の報告だ。ある数学者はClaudeとの協働でリーマン予想の証明に至ったと報告し（約25万ページの証明をLeanで形式化・公開したと主張）、Claude Fable 5.2は量子重力の2難問を自律的に解決、Gemini 4ベースの/teamworkも複数の予想の証明・形式化を報告した。これと並行して、15万本超の論文をAIで監査し人間の査読が見落とす数式誤りを可視化した調査や、AIに発見を委ねることへの人間の主体性からの批判が現れ、「成果の主張」と「人間による検証・応答」が同じ週に揃っている。

**Editorial Notes:**
- 272: alpo.ge（⭐スタンドアウト・リード）。数学者がClaudeとの協働でリーマン予想・一般リーマン予想を証明したと報告。約25万ページの証明をLeanで形式化しソースを公開したと主張する。※著者による主張であり、本プール内に第三者の独立検証・評価は存在しない
- 225: Anthropic公式（一次情報）。Claude Fable 5.2がホーキング・ペイジ相転移と、3次元重力での最軽量ブラックホール質量上限（約c/9.1266）という量子重力の2難問を自律的に解決し、Leanで形式検証・論文執筆まで遂行
- 015: Google Research公式（一次情報）。Gemini 4ベースのマルチエージェント/teamworkが、Courtade–Kumar予想の完全証明・ヴェイユ予想の180万行形式化・Zircon 80万行のC++→Rust書き換えを達成。独立した検証者（Lean 4等）と組み合わせる構成。1万人の研究者へ無料提供
- 164: Casey Handmer。理論天体物理の論文15.8万本・55万引用をLLMで監査し、人間の査読を通過した数式誤りが出版8年後も修正されず引用され続ける実態をデータ化。AIを既存の科学文献の監査に使う応用例（数千ドルのAPI費用）
- 239: borretti.me。272のリーマン予想証明の報告を起点に、AIに発見を委ねることが人間の主体性・達成感を奪うと論じる批判的応答（検証ではなく人間中心の視点からの反論）

---

### Theme 2: Gemini 4 Neon・Claude Mythos・Qwen4-Maxが広げるフロンティアモデルの拡充とコスト

**Articles (IDs):** 112, 032, 108, 023, 157

**Theme Introduction:**
先週のGemini 4／Claude Fable 5.2発表に続き、今週はモデルの選択肢と価格帯がさらに広がった。GoogleはCarbonとHydrogenの中間に位置するGemini 4 Neonと、予約・決済・買い物まで代行するGeminiの「タスクモード」を投入。AnthropicのClaude MythosはAMD GPUへのモデル移植を最大1年から約3日へ短縮し、あわせてAlibabaのQwen4-Max、Microsoftの低コスト特化モデルMAI Code 2が登場した。

**Editorial Notes:**
- 112: Google公式（一次情報・リード）。Gemini 4 Neon。CarbonとHydrogenの中間で高度な推論を高速・低コストで処理。100万トークン、4段階の「Thinking Level」、AI Studio／Cloudで提供開始
- 032: Tom's Hardware。Claude MythosがAMD GPUへのモデル移植を最大12か月から約3日へ短縮し、カーネルをほぼ100%自律生成。NvidiaのCUDA優位に切り込む
- 108: Google公式（一次情報）。Gemini 4 Hydrogen搭載の「タスクモード」。予約電話・請求書分析・AP2決済・カレンダー登録などをハードウェア隔離VM上で実行。日本含む地域で無料ロールアウト
- 023: Alibaba Qwen公式（一次情報）。Qwen4-Max。2.4兆総パラメータ（推論時71Bアクティブ）のMoE、100万トークン、3D制作・金融法務・科学的発見を狙い、トークン効率を最大49%改善
- 157: Microsoft公式（一次情報）。MAI Code 2／Code 2 Flash。GPT-6.1 Solの約98%の性能を40%のコストで提供する日常コーディング特化モデル。GitHub Copilotで即利用可

---

### Theme 3: 「自律改善ハーネス」・変異テスト・LeanによるAIエージェント開発の設計と品質保証

**Articles (IDs):** 006, 102, 136, 041, 154, 120, 275

**Theme Introduction:**
AIがコードを量産する前提に立ち、「どう設計するか」と「どう検証するか」が一体の問いとして問われている。開発者の役割を仕様・オントロジー・自動監査（ハーネス）の構築へ置き換える論、責務を分けたリポジトリで自律改善を回す実装、自律性レベルを実測した検証が設計側を担い、AI生成テストを変異テストで採点する調査、Claude Codeチームの検証の考え方、証明支援系Leanが品質保証側を担う。ハーバード大の研究は、生成量が増えてもレビューが長期化し成果物は増えなかったことを示し、両者が同じ課題であることを裏づけている。

**Editorial Notes:**
- 006: O'Reilly（リード）。AIがコードを書く時代に開発者が注力すべきは、仕様定義（ガードレール）・ビジネス概念の体系化（オントロジー）・AI自身に修正を促す自動監査（ハーネス）の構築だと説く
- 102: NTTデータ。規約・台帳・文脈・記録・検査の5責務に分けた`_harness`リポジトリとHooks・`harness-doctor`で記録漏れと基盤の健全性を担保し、エージェントが自律的にチームを組む自律実行ループを構築
- 136: 国内実務者。Claude CodeとStrands Harnessで自律性レベル（助言／承認付き／自律）を実測。承認は破壊的操作は防ぐが「もっともらしい誤った方針」は防げず、承認の読み取り負荷は1日35〜50分に達すると警告
- 041: 国内実務者。Claude Code・Codex・Gemini CLIのテストを変異テスト（StrykerJS）で48回採点。Geminiはほぼ100%検出する一方、仕様を渡すとAIが仕様外挙動を試さなくなりスコアが下がる逆説を発見
- 154: Claude.dev（一次情報）。Claude CodeチームがE2E・プロパティ・デファレンシャルテストでAIに自らのコードを検証させる考え方と、検証システム自体の信頼性を保つ運用プロセスを公開
- 120: ComplexDiscovery。ハーバード大研究（718社・約72万人）。AI導入でコード生成量は約30%増えたがマージ時間が49%増・修正依頼がほぼ倍増し、出荷済みの仕事量は増えず、ボトルネックがレビューへ移動
- 275: レバテック。AIが書いたコードの正しさを、テストや型検査を超えて保証する手段として定理証明支援系Lean 4の仕組みと可能性を解説

---

### Theme 4: GTIG・ARTEX・Pwn2Ownに見るAI駆動の攻撃自動化と防御の最前線

**Articles (IDs):** 089, 200, 111, 184, 199

**Theme Introduction:**
AIが攻撃と防御の双方を担い、セキュリティの前提が組み替わっている。GoogleのGTIGは攻撃者がARTEX等の自律型フレームワークで脆弱性調査からエクスプロイト実行までを「マシン速度」で回す段階に入ったと警告し、FBIも同フレームワークの認証情報悪用を勧告した。Pwn2Own優勝者はAIと人間の役割分担を語り、国内では内製エージェントによる自律型レッドチーミング基盤が稼働している。一方、年間インシデント分析は、原因の多くがAI特有の脆弱性ではなく従来型の認証情報露出・過剰権限だったことを示している。

**Editorial Notes:**
- 089: Google GTIG／Mandiant（一次情報・リード）。攻撃者がARTEX/CAIRNで脆弱性調査からエクスプロイト兵器化・実行までを人手を介さず実行。LLMJackingやAI生成ペルソナによる情報操作も台頭。防御はGemini 4 Carbonや自律型防衛（AITD）で対抗
- 200: 1Password。FBI勧告（FLASH-20261113-001）に基づくARTEXの脅威詳報。放置された認証情報を瞬時に特定し3時間以内に特権昇格。掃査・ローテーション・CI/CD制限・最小権限・権限監視の5対策
- 111: @type。Pwn2Own Ireland 2026で日本勢初の総合優勝を果たしたIkotas Labs辻知希氏が、AIが見つけた脆弱性を人間が「連鎖」させて実効的攻撃に変える役割分担を語る
- 184: LayerX。内製エージェントharoとPromptfooで全サービスのLLM機能を自動検知・攻撃・判定する自律型レッドチーミング基盤を構築（決定論的な成功判定で誤検知を抑制）
- 199: Aikido。2026年のAIセキュリティ50件を「AIが標的／AIが攻撃ツール／ガードレール不足のAI」に分類。原因の多くは露出シークレット・過剰権限など従来型の不備で、対策の基本は従来のAppSecにあると指摘

---

### Theme 5: 専門職のギグワーク化・Google従業員の抗議・HUMAN.mdに見るAI時代の労働と人間の尊厳

**Articles (IDs):** 226, 234, 026, 150, 109

**Theme Introduction:**
生成AIの加速が労働と人間の役割をどう変えるかを、現場・制度・文化の各面から問い直す動きが目立った。AIの学習データ生成のために高度専門職がギグワーク化し一方的に搾取される構造、AIを拒む学校への制裁に対するGoogle従業員の抗議、ゲーム業界労組による強制AI導入への拒否宣言に加え、クリエイター宣言HUMAN.mdやケンブリッジ辞典の今年の単語「human」まで、人間中心の揺り戻しが具体化している。

**Editorial Notes:**
- 226: Rest of World（リード）。Scale AI傘下Outlier等が時給180ドルで医師・弁護士・博士を募集するが、報酬引き下げと予告なきアカウント凍結という「プラットフォーム抽出主義」で専門性が搾取される構造（エール大ポサダ助教）
- 234: Mother Jones。GoogleがGeminiを無効化した学校への検索遮断方針を提示し、Alphabet Workers Union（1,000人超）が撤回を求め嘆願。NY・LA・シカゴの学区は代替検索への切り替えを検討
- 026: 欧州ゲーム労組連合。生成AIがスキル剥奪・雇用不安定・品質低下・無断学習を招くとし、労働者にAI利用拒否を、雇用主に強制導入の禁止と学習データへの対価を求めるマニフェスト
- 150: Briana May（HUMAN.md）。AIが出す「平均」を越える人間の価値は感性（Taste）にあるとし、意図的にルールを破り、現実の体験から着想し、出力の責任を自ら負う姿勢を説くクリエイター宣言
- 109: CNN。ケンブリッジ辞典が2026年の単語に「human（人間）」を選出。AIと人間を区別しようとする関心の高まり（human-made等）を象徴

---

### Theme 6: PostHog・Microsoft Decision・Gemini Decisionが広げる判断特化型AI（Decision Models）の実務活用

**Articles (IDs):** 159, 254, 101, 250

**Theme Introduction:**
（前号に続く継続テーマ。）文章を生成せず分類・採点・判定の結果だけを返す判断特化型AI（Decision Models）が、低コスト・高速な業務自動化の実用軸として広がり続けている。今週はPostHogが判断モデルの4ユースケースと閾値設計を示し、国内実務者がFAQ振り分け・スパム判定・Microsoft Decision 1.1の実機検証で生成LLMとの使い分けを具体化した点が新しい。

**Editorial Notes:**
- 159: PostHog（リード）。判断特化型モデルはLLMより最大444倍安く193倍速いとし、PIIゲート（LLM呼び出しを98.7%削減）・モデルルーター・額面チェック・過剰LLM代替の4ユースケースと、偽陽性/偽陰性に基づく閾値設計を解説
- 254: 国内実務者。Jev／Azure Decisions API／Clefを、明確な誤り検出では生成LLM（gpt-6-luna）と同等精度・中央値0.16秒と示す一方、微妙な情報不足や多肢カテゴリ推定は生成LLMが優位として「適材適所」の併用を推奨
- 101: 国内実務者。Microsoft-Decision-1.1のGA。ベースモデルがGemma 4 26B A4B（MoE）に変更され画像入力対応。入力30Kトークン規模で高速性が顕著、キャリブレーション（ECE）が大幅改善
- 250: 個人開発。Gemini Decision 1で、ドメイン認証を通る巧妙なスパムをIMAP巡回で判定・隔離。無料枠内で運用する実装コードを公開

---

### Theme 7: Anthropic上場（ANT）・ナスダック急落・「安全でない」連合が映すAI市場の期待と懐疑

**Articles (IDs):** 176, 232, 235, 170, 180

**Theme Introduction:**
（前号のAnthropic上場前テーマに続く継続。今週は上場そのものと市場反応が確定した点が新しい。）公募価格は1株83ドル・約9.8億株で史上最大規模となったが、上場2日目の急落がナスダックの2026年上昇分を消すAI株売りの引き金となり、売りは半導体株やアジア・欧州へ波及した。IPO直前には「安全なAI企業ではない」とする専門家連合の声明が出され、生成AIの富の創出を冷静に見積もる論考も並んだ。

**Editorial Notes:**
- 176: Anthropic公式（一次情報・リード）。IPO価格を1株83ドルに決定、約9.8億株を公募し2026/11/19にNasdaq（ティッカーANT）で取引開始。公共利益法人として上場、主幹事はGoldman Sachs／Morgan Stanley
- 232: Guardian。上場2日目にAnthropic株が9%下落し、ナスダックは2026年の上昇分を全て消す5%急落。Nvidia/TSMC/Micronも10%超下落し、アジア・欧州市場へ波及
- 235: NBC News。上場市場の売りが強まる中でもAnthropicなど有力スタートアップの未公開株への需要は高く、二次市場で数億ドル規模の取引が加速。過剰なプレミアムへの懸念も
- 170: Business Wire。CAISを含む科学者・法学者・テックリーダーの連合が、IPOを前に「Anthropicは安全なAI企業ではない」とする声明（MisAnthropic Statement）を発表。ピンカー、レッシグ、T.Wolf、G.Verdonら立場の異なる署名者が名を連ねる
- 180: Colossus（ジェリー・ノイマン）。生成AIはPC革命型ではなくコンテナ輸送革命型の「成熟した波」で、利益は既存巨大企業と川下（医療・教育・専門サービス）に還元されると論じる

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**
今週の最大のトピックは、AIが数学・科学の最前線で具体的な成果を主張した一連の報告だった。ある数学者はClaudeとの協働でリーマン予想の証明に至ったと報告（約25万ページの証明をLeanで形式化・公開したと主張）し、Claude Fable 5.2は量子重力の2難問を自律的に解決、Gemini 4ベースの/teamworkも複数の予想の証明・形式化を報告した。これと並行して、15万本超の論文をAIで監査し人間の査読が見落とす数式誤りを可視化した調査や、AIに発見を委ねることへの人間の主体性からの批判も現れ、「成果の主張」と「人間による検証・応答」が同じ週に揃っている。モデル面でも、Gemini 4 NeonやClaude MythosのAMD GPU移植（最大1年→約3日）など、フロンティアの拡充が続いた。

実務面では、AIがコードを量産する前提で「どう設計し・どう検証するか」が一体の問いになった。責務を分けたハーネスや自律性レベルの実測が設計側を、変異テストやClaude Codeチームの検証の考え方、証明支援系Leanが品質保証側を示し、「生成量は増えてもレビューがボトルネックになる」というハーバード大の知見が両者をつなぐ。セキュリティでは、GTIGやFBIがARTEX等によるマシン速度の攻撃自動化を警告する一方、年間インシデントの原因の多くは従来型の認証情報露出・過剰権限だった。

社会・労働の面では、高度専門職のギグワーク化、AIを拒む学校への制裁に対するGoogle従業員の抗議、ゲーム業界労組の拒否宣言、ケンブリッジ辞典の今年の単語「human」など、AIの加速に対する人間中心の揺り戻しが具体化している。前号から続く話題としては、判定だけを返す判断特化型AI（Decision Models）の実務拡大と、AnthropicのNasdaq上場（ANT）および上場2日目の急落によるAI株売りがある。

**Key Points to Cover:**
1. AIの数学・科学成果（リーマン予想中心）と、検証・監査・人間の主体性という論点
2. フロンティアモデルの拡充（Gemini 4 Neon／Claude Mythos ほか）
3. AI量産コードの設計と品質保証（ハーネス・変異テスト・Lean・レビューのボトルネック化）
4. AI駆動の攻撃自動化と防御の攻防、AI時代の労働と人間の尊厳
5. （継続）判断特化型AIの実務拡大、Anthropic上場とAI市場の期待・懐疑

---

## Curation Signal Summary

**⭐ Standout Articles Used:**
- 272 → Theme 1 (Lead) — 唯一のメイン・スタンドアウト。リーマン予想証明の報告（著者の主張として明示）

**⭐ Standout but annex pre-flagged (human kept in annex — not promoted to main):**
- 053 → Annex（LLM推論エンジンを自作する技術解説・前編）
- 069 → Annex（Anthropic公式 Always-on agents 構築ガイド／英語一次情報）
  - いずれも⭐かつSupabase annex pre-flag。人間の判断を尊重しannexに残置（主へ昇格したい場合は要相談）

**👍 Upvoted Articles Used:** なし（今サイクルは upvote フラグなし）

**👎 Downvoted Articles:**
- 045 → Annex候補（結婚式向け地図サイトの1年後レビュー）。リード/テーマドライバーには使わない
- 061 → Annex候補（キーボードを捨てた超効率開発環境）。リード/テーマドライバーには使わない

**Omitted Articles:** なし（omit フラグなし）。最終的な omit 判断は STEP_04 で実施

**Kept out of main due to overlap with last issue (2026-11-14 main):**
- 007（ESLint有償貢献者制度終了）: 前号が本編で扱った同一イベント → annex/omit候補
- 077（No AI Slop Manifesto署名）: 前号のslop宣言と主題が重複 → annex候補

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: ~30–40 articles across 6–9 themes → 本案は **7 themes / 36 articles**
- Annex Journal: 残り ~233 summaries を STEP_04/05 で annex/omit に振り分け（Supabase annex pre-flag 28件を含む）

**Article Count by Theme (Planned):**
- Theme 1 (数学・科学成果／リーマン予想中心・リード): 5
- Theme 2 (フロンティアモデルの拡充): 5
- Theme 3 (エージェント開発の設計と品質保証): 7
- Theme 4 (AIセキュリティ攻防): 5
- Theme 5 (労働と人間の尊厳): 5
- Theme 6 (判断特化型AI／継続・優先度低): 4
- Theme 7 (Anthropic上場と市場／継続・優先度低): 5

**Total Planned for Main:** 36 articles
**Remaining for Annex/Omit:** ~233

---

## Candidate Themes for Review (not in the 7 above — human may swap in / consolidate)

これらは強いクラスタだが、今回はメインから外した。GEOと国内エンタープライズ実装は前号未使用で新規性が高く、継続テーマ（6・7）と差し替える候補にもなる。

- **検索流入・コンテンツ経済の崩壊（GEO／新規性高）**: 161（AI Overviewsで外部クリック約40%減）, 166（All About Berlinがトラフィック75%減）, 172（AI推薦の84%が翌日変化）, 264（才流：BtoBサイト流入半減と対策）, 153（AI検索対応状況調査）
- **日本企業のAIエージェント組織実装（新規性高）**: 034/035（LayerX haro）, 036（LINEヤフー Agent Cluster）, 086（メルカリ）, 094（Ubie DPC）, 270（NOTA情シス）, 247（コールセンター）
- **設計・品質保証の補遺（Theme 3から外した分）**: 244（Agent Harness自作）, 273（関数型ドメインモデリング）, 097（ミューテーションテスト）, 274（E2Eガードレール）, 123（pstack）
- **ローカルLLM／オンデバイス推論**: 052, 062, 122, 221, 208, 255
- **ハードウェア／フィジカルAI（バイブコーディング）**: 020（Jeep）, 024（アナログシンセ）, 236（FPGA 33倍）, 271（シンセ魔改造）, 103（GR00T 2）, 151（BirdDreams）

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-11-24
**Reviewer:** beijaflor (via human-review-gate / AskUserQuestion)

**Changes Made:**
- Rev.1: reduced 8 themes → 6 (merged model+science; merged harness+verification)
- Rev.2: split model+science back into two (リーマン予想/数学・科学 as lead Theme 1; frontier models as Theme 2); de-prioritized 判断特化型AI and Anthropic上場 (Themes 6/7, last-week continuations); moved 239 into Theme 1

**Approval:** ✅ APPROVED

---

## Implementation Checklist

After approval:
- [x] Proceed to STEP_04 (Curate Main Journal)
- [x] Use this plan as blueprint for article selection
- [x] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)

---

## ASSEMBLY STRATEGIES (STEP_07)

> Patterns from `patterns/assembly/`. **Article order = the editorial-priority order in `curated_journal_sources.md`** (the STEP_08 writers receive that order; no reorder is introduced here). Transitions are grounded in the actual article bodies (`unified_summaries_main.md`) — no invented connections; articles are presented as-is (per `feedback_assembly_narrative` / `feedback_editorial_tone`). The STEP_08 writers run in parallel and cannot see each other's sections, so shared facts are assigned a single owning section below.
>
> **Pattern note for this cycle:** no main theme has a genuine dependency chain (Progressive-Sequence) or two opposing camps (Debate-Contrast). The honest fits are Single-Focus (one authoritative lead + reactions) and Multi-Perspective (peers / facets of one shift). T1 is Single-Focus's **Multi-Event variation** — 272 leads but 225/015 are *parallel* achievements, not reactions to it.

**Cross-theme fact ownership (parallel writers can't see each other):**
- **Lean（形式証明支援系）** appears in two different applications. **T1 owns Lean-as-math/science-proof-verification** (272/225/015 each formalize a *mathematical* claim in Lean). **T3 / 275 owns Lean-as-AI-code-correctness** (定理証明でソフトウェアの正しさを保証). Different use; **no cross-reference, no shared explanation.**
- **「検証／監査」の語義**: **T1** = AIが主張した数学・科学的発見の検証・監査（164 は *人間が書いた* 論文の監査）. **T3** = AI生成 *コード* の品質保証（テスト・型・証明）. Keep the two senses apart.
- **Gemini 4**: **T1 / 015** owns "Gemini 4ベースの/teamwork" strictly as the *math-proof agent*. **T2 / 112** owns the *Gemini 4 Neon model* and **T2 / 108** the *Gemini タスクモード*. T1/015 does not describe the model launch; T2 does not describe the proofs.
- **Claude（数学・科学 vs インフラ）**: **T1** owns Claude's math/science results (272 Riemann協働, 225 Fable 5.2 量子重力). **T2 / 032** owns the *Claude Mythos AMD-GPU 移植* story (model-infra). No overlap.

---

### Theme 1: リーマン予想・ブラックホール物理・15万論文監査に見るAIの数学・科学成果と人間の検証・応答

**Pattern:** Single-Focus（**Multi-Event variation**）
**Pattern Rationale:** ⭐272 のリーマン予想証明報告を筆頭に、AIが数学・科学の最前線で成果を主張した報告が同じ週に集中した。ただし 225/015 は 272 への *反応ではなく並行する独立成果* なので、それらは additive（「同じ週、別の研究でも」）でつなぐ。164 は成果の *生成* ではなく既存文献の *監査* という別応用、239 のみが 272 への批判的 *応答* としてループを閉じる。

**Article Order & Roles:**
1. 272 — **Lead / ⭐**（500–600語）: 数学者がClaudeとの協働でリーマン予想・一般リーマン予想を証明したと報告、約25万ページをLeanで形式化・公開したと主張。**⚠️ 著者による主張であり、本プール内に第三者の独立検証・評価は存在しない——⭐の厚みで書く場合も「主張」「報告」と明示し、証明の成立を断定しない。** Lean は *数学的証明の形式化* の文脈（T3/275 のコード用Leanとは別）
2. 225 — 並行成果（additive）: Claude Fable 5.2 がホーキング・ペイジ相転移と3次元重力の最軽量ブラックホール質量上限（約c/9.1266）を自律的に解決、Leanで形式検証・論文執筆。Anthropic公式一次情報
3. 015 — 並行成果（additive）: Gemini 4ベースの/teamwork がCourtade–Kumar予想の完全証明・ヴェイユ予想180万行形式化・Zircon 80万行C++→Rust書換えを達成、独立検証者(Lean 4等)と併用、1万人の研究者へ無料提供。Google公式一次情報。**モデルの話(Neon=T2)には触れない**
4. 164 — 別応用（scope shift）: 理論天体物理の論文15.8万本・55万引用をLLMで *監査* し、人間の査読を通過した数式誤りが8年後も修正されず引用され続ける実態をデータ化。**これは人間が書いた既存論文の監査であり、272/225/015 の主張を検証するものではない——「上記の成果を確かめた」とは書かない**
5. 239 — 批判的応答（close the loop）: 272 のリーマン証明報告を *起点に*、AIに発見を委ねることが人間の主体性・達成感を奪うと論じる。検証ではなく人間中心の視点からの反論

**Narrative Arc:** AIが数学・科学で成果を主張した複数の報告（272 リード／225・015 並行）、AIを既存文献の監査に使う応用（164）、発見をAIに委ねることへの人間中心の批判（239）が同じ週に並んだ——「成果の主張」と「人間の応答・別応用」の併置。*主張→検証* の直線的な弧にはしない（164/239 は検証者ではない）。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 272 → 225 | 「同じ週、別の研究でも AI が物理の難問を自律的に解いたと報告された」（並行成果・additive。272を「受けて」ではない） |
| 225 → 015 | 「さらに Google も、Gemini 4 ベースのエージェントで複数の予想の証明・形式化を報告した」（並行成果・additive） |
| 015 → 164 | 「成果を *生み出す* 側とは逆に、AI を使って *既存の（人間が書いた）* 科学文献を監査する応用も現れた」（別応用・scope shift） |
| 164 → 239 | 「こうした成果と応用に対し、発見を AI に委ねること自体を人間の主体性から問い直す声もある」（239 は 272 への応答としてリードへループ） |

**Emphasis Balance:** Technical High / Business Low / Societal(人間の主体性) Medium

**Key Synthesis Points:**
- 272/225/015 は *並行して* 現れた独立成果であり、相互の検証関係はない——共通するのは「AIが数学・科学の最前線で具体的成果を主張した」週だったこと
- 272 は著者の主張（独立検証なし）、225/015 は公式一次情報——情報源の性質の違いを読者に示す
- 164（既存文献の監査）と 239（人間中心の批判）は、成果の *生成* とは別軸の「検証・応答」の動き。164 を 272 らの検証と混同しない

**Conclusion Approach:** 勝者も真偽も断定せず、striking な（しかし帰属付き・未検証の）主張と、監査という新応用、人間の主体性からの問い直しを同じ週の出来事として並置して締める。

**Assembly Prompts for STEP_08:**
1. 今週 AI は数学・科学で何を「主張」したか（272/225/015）——各々の情報源の性質は
2. 164 の監査は何に対する監査か（＝人間の論文。AIの主張ではない）
3. 239 は 272 の何を問うているか
4. 「成果の主張」と「人間の応答」を並べると何が見えるか

---

### Theme 2: Gemini 4 Neon・Claude Mythos・Qwen4-Maxが広げるフロンティアモデルの拡充とコスト

**Pattern:** Multi-Perspective（ベンダー横断のモデル・ラウンドアップ）
**Pattern Rationale:** 複数ベンダーの独立したリリース（Google Neon／Anthropic Mythos移植／Google タスクモード／Alibaba Qwen4／Microsoft MAI）が「選択肢と価格帯の拡充」という一つの地殻変動の各面を成す。単一の主役はなく peers。編集優先度で 112（Google フラッグシップ Neon）が開く。

**Article Order & Roles:**
1. 112 — 開き（編集的重み）: Gemini 4 Neon。CarbonとHydrogenの中間、高度な推論を高速・低コスト、100万トークン、4段階Thinking Level、AI Studio/Cloud提供開始。Google公式一次情報
2. 032 — peer: Claude Mythos がAMD GPU移植を最大12か月→約3日、カーネルほぼ100%自律生成、NvidiaのCUDA優位に切り込む。Tom's Hardware（第三者）。**Mythos はここ(インフラ移植)が所有——T1のClaude数学成果とは別**
3. 108 — peer: Gemini タスクモード（Hydrogen搭載）。予約電話・請求書分析・AP2決済・カレンダー登録をハードウェア隔離VMで実行、日本含む無料ロールアウト。Google公式
4. 023 — peer: Qwen4-Max。2.4兆総params（推論時71Bアクティブ）MoE、100万トークン、3D制作・金融法務・科学的発見狙い、トークン効率最大49%改善。Alibaba公式
5. 157 — peer: MAI Code 2／Code 2 Flash。GPT-6.1 Solの約98%性能を40%コストで、日常コーディング特化、GitHub Copilotで即利用可。Microsoft公式

**Narrative Arc:** フロンティアの選択肢がモデル（Neon/Qwen4/MAI）・既存モデルの移植効率（Mythos）・モデルを使う機能（タスクモード）の各面で広がり、価格帯も下方に拡充された一週間。意義の一般化や競合煽りはせず、出荷された具体で締める。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 112 → 032 | 「新モデルの登場と並んで、既存モデルを別ハードへ *移植* する速度も跳ね上がった」（別角度・peer） |
| 032 → 108 | 「モデルそのものだけでなく、モデルを *使う* 機能面でも」→ Gemini タスクモードへ（別角度） |
| 108 → 023 | 「別のベンダーからも大型の新モデルが」→ Qwen4-Max へ（peer） |
| 023 → 157 | 「低コスト特化という軸では」→ MAI Code 2 へ（peer） |

**Emphasis Balance:** Technical Medium / Business Medium / Future Low

**Key Synthesis Points:**
- 112（高速・低コスト中間層）・157（98%性能/40%コスト）・023（トークン効率49%改善）が共通して「性能あたりコスト」を下げる方向——価格競争の面
- 032 はモデルでなく *移植（AMD対応）* の話、108 は *機能（タスク代行）* の話——「モデル拡充」は新モデルだけではない
- 一次情報が中心で第三者評価は 032 のみ——評価の確度に差があることを示す

**Conclusion Approach:** 一般化・予測を避け、出荷された具体（Neon の提供開始、Mythos の3日移植、タスクモードの無料ロールアウト範囲、Qwen4/MAIの価格・性能）を並べて締める。

**Assembly Prompts for STEP_08:**
1. 今週「広がった」のは何か（新モデル／移植／機能／価格帯）
2. 各リリースはどの軸でフロンティアを押し広げたか
3. 読者が今すぐ触れられるものは
4. （一般化した将来予測はせず、事実で締める）

---

### Theme 3: 「自律改善ハーネス」・変異テスト・LeanによるAIエージェント開発の設計と品質保証

**Pattern:** Multi-Perspective（二グループ：設計／品質保証。120 が横断的シンセシス）
**Pattern Rationale:** 7本は相互依存の *連鎖* ではない——006 が「設計＝仕様/オントロジー/ハーネス、QA＝自動監査」という枠組みを与え、102/136 が設計側の、041/154/275 が品質保証側の *独立した* 実例。120（ハーバード）は「生成量が増えてもレビューがボトルネック」という両者を貫く現実を示すシンセシス。偽の積み上げ（「〜を発展させ」）を作らず、グループ内は peers として並置する。

**Article Order & Roles:**
1. 006 — 枠組み（lead/framing）: AIがコードを書く時代、開発者は仕様定義（ガードレール）・ビジネス概念の体系化（オントロジー）・自動監査（ハーネス）の構築へ。O'Reilly
2. 102 — 設計の実例（peer）: 規約・台帳・文脈・記録・検査の5責務に分けた `_harness` リポジトリ＋Hooks・`harness-doctor` で自律実行ループ。NTTデータ
3. 136 — 設計/運用の実例（peer）: Claude Code＋Strands Harnessで自律性レベル（助言/承認付き/自律）を実測、承認は「もっともらしい誤った方針」を防げず読み取り負荷35〜50分/日
4. 041 — 品質保証の手法（peer）: AI生成テストを変異テスト（StrykerJS）で48回採点。Geminiはほぼ100%検出するが、*仕様を渡すとAIが仕様外挙動を試さなくなりスコアが下がる* 逆説
5. 154 — 品質保証の考え方（peer）: Claude CodeチームがE2E・プロパティ・デファレンシャルテストでAIに自らのコードを検証させる運用と、検証システム自体の信頼性維持。claude.dev一次情報
6. 120 — **シンセシス**: ハーバード大研究（718社・約72万人）。コード生成量は約30%増だがマージ時間+49%・修正依頼ほぼ倍増、出荷量は増えず、ボトルネックがレビューへ移動
7. 275 — 品質保証の最も強い形（closer）: テスト・型検査を超えてAI生成コードの正しさを保証する定理証明支援系 **Lean 4**。レバテック。**Lean はここでは *コードの正しさ保証* の文脈——T1 の数学証明用Leanとは別、相互参照しない**

**Narrative Arc:** 006 が設計とQAを一体の問いとして枠付け → 設計の実例（102 ハーネス、136 自律性の実測）→ 品質保証の手法（041 変異テスト、154 検証の考え方）→ 120 が「生成↑でもレビューがボトルネック」という共通の現実を可視化 → 275 がコード正しさの最も強い保証（形式証明）として締める。各グループ内は peers（因果の積み上げではない）。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 006 → 102 | 「この枠組みを実装に落とした例として」→ NTTのハーネス（別角度・設計 peer） |
| 102 → 136 | 「別の実務者は、自律エージェントの *自律性レベル* そのものを実測した」（別角度・設計/運用 peer） |
| 136 → 041 | 「設計に対し、品質保証の側面では」→ 変異テストによるAIテストの採点へ（グループ転換） |
| 041 → 154 | 「別の品質保証の考え方として」→ Claude Codeチームの検証プロセス（QA peer） |
| 154 → 120 | 「こうした設計・検証の努力をマクロに見ると」→ ハーバード大の「レビューがボトルネック」へ（シンセシス） |
| 120 → 275 | 「レビュー負荷が増すなか、人手の確認に頼らず正しさを機械的に保証する手段として」→ Lean 4 へ（最も強い保証） |

**Emphasis Balance:** Technical High / Business Medium / Future Medium

**Key Synthesis Points:**
- 「どう設計するか（006/102/136）」と「どう検証するか（041/154/275）」は別個の作業ではなく、120 が示すとおり *同じボトルネック（レビュー）* に収束する一体の問い
- 041 の逆説（仕様を渡すとAIが仕様外を試さない）と 136 の警告（承認は誤方針を防げない）は、「人間のチェックをどこに置くか」という共通課題の別の顔
- 275（形式証明）は 120（レビュー過負荷）への一つの方向——ただし「275 が 120 を解決する」とは断定せず、QAの最も強い形として提示

**Conclusion Approach:** 生成量の増加がレビューを新たなボトルネックにした（120）という現実を軸に、設計（ハーネス）と品質保証（変異テスト・形式証明）が同じ課題の両面であることを示して締める。

**Assembly Prompts for STEP_08:**
1. 「設計」と「品質保証」をなぜ一体で論じるのか（006 の枠組み）
2. 設計側・QA側の各実例は何を具体化したか
3. 120 は何を「ボトルネック」と呼ぶか
4. 275 の形式証明はその課題にどう関わるか（断定せず）

---

### Theme 4: GTIG・ARTEX・Pwn2Ownに見るAI駆動の攻撃自動化と防御の最前線

**Pattern:** Multi-Perspective（攻撃・防御・現実の各 facet）
**Pattern Rationale:** AIがセキュリティの攻防を組み替える局面を、攻撃ランドスケープ(089)・具体的脅威(200)・人間×AIの攻撃役割分担(111)・自律防御(184)・年間総括の現実(199)という複数 facet から描く。単一イベントへの反応でも二項対立でもなく、同じ地殻変動の各面。199 が「原因の多くは従来型」という sober な締め。

**Article Order & Roles:**
1. 089 — 攻撃ランドスケープ（編集的重み・lead）: 攻撃者がARTEX/CAIRNで調査→兵器化→実行をマシン速度で。LLMJacking、AI生成ペルソナの情報操作。防御はGemini 4 Carbon・自律型防衛(AITD)。Google GTIG/Mandiant一次情報。**ARTEX はこのテーマが所有**
2. 200 — 具体的脅威（facet）: FBI勧告(FLASH-20261113-001)に基づくARTEX詳報。放置された認証情報を特定し3時間以内に特権昇格。掃査・ローテーション・CI/CD制限・最小権限・権限監視の5対策。1Password
3. 111 — 人間×AIの攻撃（facet）: Pwn2Own Ireland 2026で日本勢初の総合優勝、辻知希氏。AIが見つけた脆弱性を人間が「連鎖」させ実効的攻撃にする役割分担
4. 184 — 自律防御（facet）: 内製エージェントharo＋Promptfooで全サービスのLLM機能を自動検知・攻撃・判定する自律型レッドチーミング、決定論的な成功判定で誤検知抑制。LayerX
5. 199 — 現実の総括（sober close）: 2026年のAIセキュリティ50件を「AIが標的／AIが攻撃ツール／ガードレール不足」に分類。原因の多くは露出シークレット・過剰権限など従来型で、対策の基本は従来のAppSec。Aikido

**Narrative Arc:** 攻撃の自動化がマシン速度に達し(089)、FBIが具体的脅威を勧告(200)、攻撃も防御も人間とAIの分担・自律化が進む(111/184)。だが一年を総括すると、原因の多くは *従来型* の不備だった(199)——高度化と基本の両面を併置。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 089 → 200 | 「この脅威を具体化するFBI勧告として」→ ARTEXの認証情報悪用の詳報へ（facet・additive） |
| 200 → 111 | 「攻撃側では、AIと人間の役割分担も明確になっている」→ Pwn2Own優勝者の証言へ（別角度） |
| 111 → 184 | 「防御側でも自律エージェントが攻撃役を担い始めた」→ LayerXの自律レッドチーミングへ（別角度） |
| 184 → 199 | 「しかし一年を総括すると、原因の多くは *従来型* の不備だった」→ Aikidoの分析へ（現実・contrast） |

**Emphasis Balance:** Technical High / Business Medium / Future Medium

**Key Synthesis Points:**
- 089（マシン速度の攻撃自動化）と 200（3時間で特権昇格）は脅威の規模・速度を、111/184 は攻防ともに人間×AI・自律化が進む様子を示す
- 199 の反転——高度な脅威が注目される一方、実被害の原因は露出シークレット・過剰権限という *基本* の不徹底
- 防御の柱（200 の5対策、184 の決定論的判定、089 のID中心/AITD）は新技術だけでなく基本衛生の自動化・徹底に帰着

**Conclusion Approach:** 攻防はマシン速度で高度化するが（089/200/111/184）、原因の基本は従来型（199）——派手な脅威より認証情報・権限の基本を自動化・徹底することが要、と締める。

**Assembly Prompts for STEP_08:**
1. AIは攻撃・防御の何を変えたか（速度・自律・役割分担）
2. ARTEXの脅威の具体像は（089/200）
3. 199 の「原因の多くは従来型」は何を意味するか
4. 読者が明日見直すべき基本は（認証情報・権限）

---

### Theme 5: 専門職のギグワーク化・Google従業員の抗議・HUMAN.mdに見るAI時代の労働と人間の尊厳

**Pattern:** Multi-Perspective（人間中心の揺り戻しの各 facet、現場→制度→文化）
**Pattern Rationale:** AI時代の労働と人間の尊厳を、現場の搾取構造(226)・企業内の抗議(234)・労組の拒否宣言(026)・クリエイター宣言(150)・文化的象徴(109)という複数ドメインの peers として並置。単一の権威も二項対立もなく、各面で揺り戻しが具体化する範囲を見せる。

**Article Order & Roles:**
1. 226 — 現場の構造（編集的重み・lead）: Scale AI傘下Outlier等が時給180ドルで医師・弁護士・博士を募集するが、報酬引き下げと予告なきアカウント凍結という「プラットフォーム抽出主義」で専門性を搾取（エール大ポサダ助教）。Rest of World
2. 234 — 制度/企業（facet）: GoogleがGeminiを無効化した学校への検索遮断方針を提示、Alphabet Workers Union(1,000人超)が撤回を求め嘆願、NY・LA・シカゴの学区が代替検索を検討。Mother Jones
3. 026 — 労組の宣言（facet）: 欧州ゲーム労組連合が、生成AIはスキル剥奪・雇用不安定・品質低下・無断学習を招くとし、労働者にAI利用拒否を、雇用主に強制導入禁止と学習データ対価を求めるマニフェスト
4. 150 — 個人/思想（facet）: HUMAN.md。AIが出す「平均」を越える人間の価値は感性(Taste)にあるとし、意図的にルールを破り、現実の体験から着想し、出力の責任を自ら負う姿勢を説くクリエイター宣言
5. 109 — 文化的象徴（close）: ケンブリッジ辞典が2026年の単語に「human」を選出、AIと人間を区別しようとする関心の高まり(human-made等)を象徴。CNN

**Narrative Arc:** AIの加速が労働と人間の役割をどう変えるかを、現場の搾取(226)→企業内の抗議(234)→労組の拒否(026)→個人の美学(150)→文化的象徴(109)と、ミクロからマクロへ、人間中心の揺り戻しの各面で描く。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 226 → 234 | 「個々の労働者の搾取と並んで、企業内でも抗議が」→ Googleの学校制裁と従業員嘆願へ（別角度・peer） |
| 234 → 026 | 「個別の抗議を超え、労組が集団で拒否を宣言した例」→ 欧州ゲーム労組マニフェストへ |
| 026 → 150 | 「制度的な抵抗の一方、個人の美学として」→ HUMAN.md のクリエイター宣言へ（別角度） |
| 150 → 109 | 「こうした動きを象徴するように」→ 辞典の今年の単語「human」へ（文化的象徴で締め） |

**Emphasis Balance:** Technical Low / Business Low / Societal High

**Key Synthesis Points:**
- 226/234/026 は経済・雇用の構造的問題、150/109 は価値・文化の問題——「人間の尊厳」という芯で連なる（反テクノロジーではなく人間中心）
- 226 の「プラットフォーム抽出主義」と 026 の「学習データへの対価要求」は、*AIの学習を支える人間の労働が正当に報われない* という同じ構造を別角度から突く
- 109 の「human」選出は、226〜150 の具体的動きが社会全体の関心に昇華した表れ

**Conclusion Approach:** 現場・制度・文化の各面で、AIの加速に対する人間中心の揺り戻しが具体化している——反AIというより「人間の労働・判断・責任の尊厳をどこで守るか」という問いだと示して締める。

**Assembly Prompts for STEP_08:**
1. 各動きに共通する「人間の尊厳」とは何か
2. 226 と 026 の構造的な一致（労働の対価）は
3. 搾取・抗議・宣言・文化はどう連なるか
4. 読者は自分の現場でどこに線を引くか

---

### Theme 6: PostHog・Microsoft Decision・Gemini Decisionが広げる判断特化型AI（Decision Models）の実務活用

**Pattern:** Single-Focus（継続テーマ・優先度低）
**Pattern Rationale:** 「判断特化型AI（Decision Models）」という単一トレンドを、PostHogの俯瞰(159)がリードし、実務検証(254)・製品GA(101)・個人実装(250)が裏づける。159 に明確な俯瞰の権威。前号(2026-11-14)からの継続テーマで、今週は閾値設計の具体化・MS-Decision GA・実務での使い分けが新しい。

**Article Order & Roles:**
1. 159 — Lead/俯瞰: 判断特化型モデルはLLMより最大444倍安く193倍速いとし、PIIゲート(LLM呼び出し98.7%削減)・モデルルーター・額面チェック・過剰LLM代替の4ユースケースと、偽陽性/偽陰性に基づく閾値設計を解説。PostHog
2. 254 — 実務検証: Jev／Azure Decisions API／Clefを、明確な誤り検出では生成LLM(gpt-6-luna)と同等精度・中央値0.16秒と示す一方、微妙な情報不足や多肢カテゴリ推定は生成LLMが優位とし「適材適所」の併用を推奨
3. 101 — 製品GA: Microsoft-Decision-1.1のGA。ベースがGemma 4 26B A4B(MoE)に変更され画像入力対応、入力30Kトークン規模で高速性顕著、キャリブレーション(ECE)が大幅改善
4. 250 — 個人実装（payoff）: Gemini Decision 1で、ドメイン認証を通る巧妙なスパムをIMAP巡回で判定・隔離、無料枠で運用する実装コードを公開

**Narrative Arc:** 判断特化型とは何か・どこで効くか(159 の4ユースケースと閾値設計) → 生成LLMとの使い分けの実測(254) → 製品の成熟(101 GA) → 無料枠での個人実装(250)。概念→検証→製品→応用。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 159 → 254 | 「この枠組みを実務で検証すると、どこで生成LLMと使い分けるべきか」→ 254 の適材適所へ |
| 254 → 101 | 「製品側でも判断特化モデルが成熟した」→ Microsoft-Decision 1.1 のGAへ |
| 101 → 250 | 「個人開発でも、無料枠で実用的な判定が組める」→ Gemini Decision のスパム判定へ |

**Emphasis Balance:** Technical Medium / Business High / Future Medium

**Key Synthesis Points:**
- 159 の「444倍安い/193倍速い」と 254 の「中央値0.16秒・生成LLM同等精度」が、コスト・速度の優位を定量裏づけ
- 254 の「微妙な判断は生成LLMが優位」は、判断特化型が万能でなく *使い分け* の対象であることを示す（159 の閾値設計と対応）
- 継続テーマだが、今週は閾値設計の具体化・MS-Decision GA・実務検証という「実運用への落とし込み」が新しい

**Conclusion Approach:** 判断特化型は低コスト・高速な実運用層として定着しつつあり、要点は生成LLMとの *使い分け*（閾値設計・適材適所）だと締める。継続テーマゆえ煽らず、今週の増分（GA・実務検証）に焦点。

**Assembly Prompts for STEP_08:**
1. 判断特化型AIの4ユースケースと閾値設計(159)は何を示すか
2. 生成LLMとの使い分けの基準は(254)
3. 今週の増分（MS-Decision GA・実務検証）は何が新しいか
4. 読者はどこで判断特化型を使うべきか

---

### Theme 7: Anthropic上場（ANT）・ナスダック急落・「安全でない」連合が映すAI市場の期待と懐疑

**Pattern:** Single-Focus（継続テーマ・優先度低）
**Pattern Rationale:** AnthropicのNasdaq上場(ANT)という単一イベントを、一次情報(176 価格決定)がリードし、市場反応(232 急落／235 未公開株需要)、上場前の批判(170)、市場全体の見立て(180)が反応として連なる。前号(2026-11-14)の上場前テーマの継続で、今週は上場そのものと市場反応が確定した点が新しい。

**Article Order & Roles:**
1. 176 — Lead/一次情報: IPO価格を1株83ドルに決定、約9.8億株を公募し2026/11/19にNasdaq(ティッカーANT)で取引開始。公共利益法人として上場、主幹事Goldman Sachs/Morgan Stanley。Anthropic公式
2. 232 — 市場反応: 上場2日目にAnthropic株9%下落、ナスダックは2026年の上昇分を全て消す5%急落、Nvidia/TSMC/Micronも10%超下落、アジア・欧州へ波及。Guardian
3. 235 — 対照的な需要: 売りが強まる中でもAnthropicら有力スタートアップの未公開株需要は高く、二次市場で数億ドル規模の取引が加速、過剰プレミアム懸念も。NBC News
4. 170 — 上場前の批判（contrarian）: CAIS含む科学者・法学者・テックリーダー連合が「Anthropicは安全なAI企業ではない」声明(MisAnthropic Statement)、ピンカー・レッシグ・T.Wolf・G.Verdonら立場の異なる署名者。Business Wire
5. 180 — 市場全体の見立て（analytical close）: 生成AIはPC革命型でなくコンテナ輸送革命型の「成熟した波」で、利益は既存巨大企業と川下(医療・教育・専門サービス)に還元されると論じる。Colossus(ジェリー・ノイマン)

**Narrative Arc:** 上場の確定(176) → 直後の市場反応（急落 232／対照的に高い未公開株需要 235）→ 上場前からの安全性批判(170) → 生成AIの富をどう見積もるかの冷静な分析(180)。期待と懐疑の緊張。

**Transition Strategy:**
| From → To | Approach |
|-----------|----------|
| 176 → 232 | 「史上最大規模の上場だったが、直後の市場反応は」→ 2日目の急落へ |
| 232 → 235 | 「一方、公開市場の売りとは対照的に、未公開株には依然高い需要が」→ 二次市場へ（contrast） |
| 235 → 170 | 「期待が渦巻く一方、上場前には安全性への異論も出ていた」→ MisAnthropic声明へ |
| 170 → 180 | 「ではこのAI市場の期待値をどう見積もるか」→ ノイマンの「成熟した波」論へ（分析で締め） |

**Emphasis Balance:** Technical Low / Business High / Future Medium

**Key Synthesis Points:**
- 176 の「史上最大規模」と 232 の「上場2日目に市場全体を巻き込む急落」が、期待の大きさと脆さの両方を示す
- 235（未公開株は高需要）と 232（公開株は急落）の対照——市場の評価が割れている
- 170（安全性への批判）と 180（富の配分は川下へ）は、過熱した期待への二つの異なる冷却——倫理面と経済面

**Conclusion Approach:** 勝者も真偽も断定せず、史上最大の上場という実像と、急落・安全性批判・「成熟した波」論という懐疑を並置して締める。読者は期待と懐疑のどちらに重きを置くかを問われる。継続テーマゆえ煽らない。

**Assembly Prompts for STEP_08:**
1. 176 は何を確定させたか（価格・規模・上場形態）
2. 232 と 235 の対照は市場の何を示すか
3. 170 の批判は何を突くか
4. 180 はAI市場の富をどう見積もるか

---

### Annex（カタログ）Assembly

**Format（EDITOR_PERSONALITY カタログモード）:** 1件80–120語の統合ナラティブ。「読むべきか？」に答える decision-focused。批評的要点は地の文に織り込む（別建ての「なぜ重要か」等は作らない）。英語記事は**原題を併記**（検索性）。カテゴリは非自明な文脈を足すときだけ（目安3–4割）。独自・論争的な角度は末尾で前景化。**メイン記事の内容を繰り返さず、annex独自の角度を前景化。**

**Sections（8 — curator's organisation in `curated_annex_selected.md`、STEP_05承認済）:**
1. 実務ハーネス・エージェント運用の高度な実践 (058, 076, 124, 252, 262, 134, 133)
2. エージェント向け標準・OSSツール・プロトコル (069, 071, 083, 090, 139)
3. AIエージェントのセキュリティ・認証（独立した深掘り） (046, 047, 114, 174)
4. 日本企業のAIエージェント組織実装 (242, 115)
5. ローカルLLM・推論エンジンの自作 (053, 048)
6. ハードウェア・フィジカルAI・レトロ (022, 051, 236, 024, 230)
7. 批評・反論・社会的受容 (258, 067, 084)
8. ニッチ探究・研究・エッジ (025, 131, 146, 194, 240, 177)

**Signals / overlap notes:**
- **⭐ standout kept in annex per human**（主へ昇格せず）: **069**（Anthropic公式 Always-on agents 構築ガイド／英語一次情報・Sec.2）、**053**（LLM推論エンジン自作・前編・Sec.5）。カタログでも⭐相応に充実させるが、主記事ではないので煽らない
- **Main-adjacent（overlap→tag, not drop）**: Sec.1(058/076/124) は T3「設計と品質保証」隣接、Sec.3(046/047/114/174) は T4「セキュリティ」隣接。いずれも main を繰り返さず、annex固有の深掘り・個別ツールの角度を前景化
- **原題併記が要る英語記事**: 022(z80/スペイン語原文), 083(modern-web-guidance), 139(GitHub Agent Host Protocol), 174(fake AI crawler secrets), 194(Netflix Tech Blog), 240(slopstrap), ほか英語タイトルの記事は原題を併記

**Annex note:** 最終的なセクション構成（タイトル・記事の再グルーピング）は STEP_08 assembly の編集判断。上記は curator の承認済み8分類で、gen_writer_prompts はこの並びで section プロンプトを出す。

---

## Assembly Plan Status

- [x] Phase 1: Pattern library reviewed
- [x] Phase 2: Patterns selected and customized for all themes (7 main + annex)
- [x] Phase 3: Assembly strategies documented
- [x] Assembly strategies defined (STEP_07)
- [x] ASSEMBLY PLAN APPROVED - Ready for STEP_08

> The agent leaves `ASSEMBLY PLAN APPROVED` **unchecked**; it is flipped to `[x]` only after the human approves through the `human-review-gate` skill (AskUserQuestion). The STEP_03b approval `[x] APPROVED - Ready for STEP_04 curation` above still stands and is unaffected.

**Pattern distribution:** Single-Focus ×3 (T1 Multi-Event・T6・T7) ・ Multi-Perspective ×4 (T2・T3・T4・T5). No Progressive-Sequence or Debate-Contrast — no main theme this cycle has a genuine dependency chain or two opposing camps (honest fit; not forced into last cycle's mix).

**Approval Date:** 2026-11-25
**Approver:** beijaflor (via human-review-gate / AskUserQuestion)
