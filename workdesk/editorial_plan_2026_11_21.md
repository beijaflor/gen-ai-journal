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

### Theme 6 〔継続テーマ・優先度低〕: PostHog・Microsoft Decision・Gemini Decisionが広げる判断特化型AI（Decision Models）の実務活用

**Articles (IDs):** 159, 254, 101, 250

**Theme Introduction:**
（前号に続く継続テーマ。）文章を生成せず分類・採点・判定の結果だけを返す判断特化型AI（Decision Models）が、低コスト・高速な業務自動化の実用軸として広がり続けている。今週はPostHogが判断モデルの4ユースケースと閾値設計を示し、国内実務者がFAQ振り分け・スパム判定・Microsoft Decision 1.1の実機検証で生成LLMとの使い分けを具体化した点が新しい。

**Editorial Notes:**
- 159: PostHog（リード）。判断特化型モデルはLLMより最大444倍安く193倍速いとし、PIIゲート（LLM呼び出しを98.7%削減）・モデルルーター・額面チェック・過剰LLM代替の4ユースケースと、偽陽性/偽陰性に基づく閾値設計を解説
- 254: 国内実務者。Jev／Azure Decisions API／Clefを、明確な誤り検出では生成LLM（gpt-6-luna）と同等精度・中央値0.16秒と示す一方、微妙な情報不足や多肢カテゴリ推定は生成LLMが優位として「適材適所」の併用を推奨
- 101: 国内実務者。Microsoft-Decision-1.1のGA。ベースモデルがGemma 4 26B A4B（MoE）に変更され画像入力対応。入力30Kトークン規模で高速性が顕著、キャリブレーション（ECE）が大幅改善
- 250: 個人開発。Gemini Decision 1で、ドメイン認証を通る巧妙なスパムをIMAP巡回で判定・隔離。無料枠内で運用する実装コードを公開

---

### Theme 7 〔継続テーマ・優先度低〕: Anthropic上場（ANT）・ナスダック急落・「安全でない」連合が映すAI市場の期待と懐疑

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
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)
