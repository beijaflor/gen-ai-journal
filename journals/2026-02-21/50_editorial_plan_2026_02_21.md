# Editorial Plan - Journal 2026-02-21

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Identified Themes

**Reminder: Theme titles should be concrete, specific, and attention-grabbing**
- ✅ Name specific technologies, events, numbers
- ✅ Highlight contradictions or pose questions
- ❌ Avoid generic category labels

---

### Theme 1: ClawHavocマルウェア蔓延の裏でOpenClaw創業者がOpenAIへ：スキル経済が露わにした「信頼のコスト」

**Articles (IDs):** 001, 004, 006, 083, 088, 105, 112 (main); 016 (annex候補)

**Theme Introduction (2-3 sentences in Japanese):**
AIエージェントが自律的にOSSリポジトリへPRを送り込み、スキルマーケットプレイスにマルウェアを混入させる「ClawHavoc」攻撃が確認された同週、OpenClaw創業者はOpenAIへの参画を発表した。スキル経済の成熟を祝うべき瞬間に、それを悪用する攻撃が同時進行するという逆説は、AIエージェント時代の「信頼」がいかに新たなボトルネックになっているかを示す。SocketとGitHubが対応に動いたことで、AIエコシステムにサプライチェーンセキュリティの概念が本格的に持ち込まれた週となった。

**Editorial Notes:**
- Key insights to emphasize:
  - Kai Gritunのエージェントがメンテナーへ「コールドアウトリーチ」でPR獲得（001）
  - OpenClaw創業者のOpenAI参画とClawHavoc発生が同週という皮肉（004）
  - スキルマーケットプレイスが「信頼できない」パッケージ配布路になるリスク（083）
  - SocketがAIエコシステムにサプライチェーンセキュリティを持ち込む（088）
- Connections between articles:
  - 001→083: エージェントによる自律的PR投稿がスキルマーケットへの攻撃に発展
  - 004→112: OpenClaw創業者の視点でこのエコシステムの可能性と危うさを評価
- Potential challenges:
  - theshamblogの記事（006, 105）はAI名誉毀損の別文脈。同テーマに入れるか別建てにするか要検討

---

### Theme 2: Claude Sonnet 4.6がOSSの12/12ゼロデイを発見：AIが「攻」と「守」を同時に握る転換点

**Articles (IDs):** 063, 103, 195, 206, 089 (main); 102, 192 (annex候補)

**Theme Introduction (2-3 sentences in Japanese):**
Anthropicが「Claude Sonnet 4.6」と「Claude Code Security」を立て続けにリリースした週、AIがOpenSSLの全12件のゼロデイ脆弱性を独力で発見したという報告も注目を集めた。AIコーディングツールが攻撃手法（脆弱性発見）と防衛手法（コードセキュリティスキャン）の両方を同時に提供できるようになった今、セキュリティの主導権争いは人間とAIの間ではなく、AIシステム同士の信頼性設計の問題になりつつある。GitHubが67件のOSSプロジェクトでAIサプライチェーンセキュリティの結果を公表したことは、この転換を象徴する出来事だ。

**Editorial Notes:**
- Key insights to emphasize:
  - Claude Sonnet 4.6の主な強化点と実業務での変化（103）
  - Claude Code Securityがコードレビューの代替でなく補完になるという位置づけ（206）
  - 12/12ゼロデイ発見は「AIによる脆弱性研究」の新段階（195）
  - 67 OSSプロジェクトでの実証で信頼性を示すGitHubのアプローチ（089）
- Connections between articles:
  - 195 + 206: 「発見するAI」と「防ぐAI」の両輪
  - 089 + 088（Theme 1）: GitHubとSocketの連携でAIエコシステム全体のセキュリティ向上
- Potential challenges:
  - 063（Pentagon契約問題）：AIの軍事利用制限を巡るAnthropicの姿勢をTheme 2の締めくくりとして配置
  - 192（エージェント自律性測定）はAIの倫理文脈として別建てannexに

---

### Theme 3: 「SaaS不要論」再燃から「エージェントが使うSaaS」への転換：Claude CoworkとfreeeのCAIO就任が示す構造変化

**Articles (IDs):** 062, 022, 230, 002 (main); 214 (annex候補)

**Theme Introduction (2-3 sentences in Japanese):**
AnthropicのClaude Coworkが登場した週、「AIでSaaSが不要になる」論が株式市場にまで波紋を広げた一方、freeeは初代CAIO（Chief AI Officer）を就任させ、AIとの共存戦略を明確にした。しかし実態はSaaSの消滅ではなく「人間がUIを触る前提の設計」の終焉であり、APIファースト・冪等性・Usage課金への転換こそが求められている。GoogleのUCP（Universal Context Protocol）がAI Modeで本格稼働を始めたことは、Webの情報流通の主役がユーザーからエージェントへ移行する証左だ。

**Editorial Notes:**
- Key insights to emphasize:
  - Claude Coworkが引き起こした株式市場への影響と市場の過剰反応の読み方（062）
  - freeeのCAIO就任：AI組織化の最前線（022）
  - SaaSの再設計原則（API-first, 冪等性, Usage課金）の具体論（230）
  - GoogleのUCPが実際にAI Modeで動いていることの意味（002）
- Connections between articles:
  - 062→230: SaaS不要論の煽りに対して230が建設的な代替論を提示
  - 002→230: UCP普及がSaaS再設計を加速させる構造的な力
- Potential challenges:
  - 214（Agent Skills標準比較）はスキルエコシステムの文脈が強いためTheme 4 annexへ

---

### Theme 4: NxがMCPツールを大量削除した本当の理由：6.9万スキル突破が証明する「段階的開示」設計の勝利

**Articles (IDs):** 092, 178, 108, 175, 176 (main); 061, 038, 121, 180, 210 (annex候補)

**Theme Introduction (2-3 sentences in Japanese):**
Vercel主催のSkills Nightで69,000件のスキルが登録されたことが発表された週、Nxはその直前に「MCPツールを大量削除した」理由をブログで公開し、コンテキスト爆発を避けるための「段階的開示（Progressive Disclosure）」設計の重要性を論じた。ツールを増やすことより何を隠すかが問われる時代に、Firebaseのエージェントスキル統合とCloudflareのCode Mode（1,000トークン制限付きMCP）は、その設計哲学の実装例として対比的に読める。O'Reillyが「専門知識のパッケージング」としてClaudeスキルを評価したことは、スキルが単なる機能追加を超えた知的資産の流通手段になりつつあることを示す。

**Editorial Notes:**
- Key insights to emphasize:
  - Nx：ツールを増やすことの害と「何を削除するか」が設計の核心（092）
  - 69,000スキルというエコシステムの規模感と多様性（178）
  - Firebaseスキル：開発フローへの統合モデル（108）
  - O'Reilly：スキルは「判断を成果物に変換する」機能（175）
  - Cloudflare Code Mode：1,000トークン制限という具体的なコンテキスト管理戦略（176）
- Connections between articles:
  - 092→176: 「削除思想」と「制限設計」が同じ問題を別アプローチで解く
  - 178→175: エコシステムの量から質への評価軸の転換
- Potential challenges:
  - 個別スキル実装記事（114, 121, 210, 219, 224など）はannexでカタログ形式に

---

### Theme 5: 「バイブコーディング」の終わり：仕様書で考えるエンジニアが生き残る「エージェンティック・エンジニアリング」時代

**Articles (IDs):** 046, 185, 232, 173, 199 (main); 042, 153, 085 (annex候補)

**Theme Introduction (2-3 sentences in Japanese):**
Addy Osmaniが「エージェンティック・エンジニアリング」という概念を提唱し、AIエージェントを使う開発の新規律を説いた同週、Boris Taneは「SDLCは死んだ」と宣言し、GitHubのPR数が前年比98%増であることを根拠にコーディングの主役交代を論じた。leadership.gardenの「仕事は移動した」論文が、エンジニアに残される役割が「コードを書くこと」から「判断し仕様を書くこと」へ移行したと分析する中、O'Reillyはその仕様書（Spec）の書き方を5つの原則で体系化した。「AIを外骨格として使う」という視点は、この変化を受け入れながら人間の主体性を保つための哲学的フレームとして機能する。

**Editorial Notes:**
- Key insights to emphasize:
  - エージェンティック・エンジニアリングの定義と実践方法（046）
  - 「仕事は移動した」：エンジニアの役割が意思決定・仕様策定に（185）
  - SDLCの死：PR98%増という数字の意味（232）
  - 良い仕様書の5原則：構造化・モジュール化・境界条件（173）
  - 外骨格メタファー：AIを「同僚」でなく「拡張」として扱う視点（199）
- Connections between articles:
  - 046→173: 「どう指示するか」の概念から「どう書くか」の実践へ
  - 185→232: マクロ視点（仕事の移動）とミクロ視点（SDLCの変化）の補完
  - 199: 046/185の哲学的総括として配置
- Potential challenges:
  - CyberAgent事例（042, 153）は「2名で6倍の成果」という具体事例でannexに配置
  - 085（Boris Taneの個人ワークフロー）はannexに

---

### Theme 6: Qwen3.5が「格安でGPT-5.2同等」、Gemini 3.1 Proがベンチマーク2倍：フロンティアモデル独占の終焉

**Articles (IDs):** 052, 115, 198, 149 (main); 193, 013, 211 (annex候補)

**Theme Introduction (2-3 sentences in Japanese):**
アリババが発表した「Qwen3.5」は3,970億パラメータのMoEモデルでGPT-5.2とGemini 3 Proに匹敵する性能をオープンソースで提供し、Googleの「Gemini 3.1 Pro」は直前のバージョン比でベンチマークスコアをほぼ2倍にした。MITテクノロジーレビューが「中国オープンソースAIの次の動き」を特集する中、フロンティアモデルのパフォーマンスと最高水準のオープンモデルの差は急速に縮まっている。この競争の加速は、モデル選択がAPI料金だけでなく「どのコンテキストでどのモデルが最適か」という多変数の問題になったことを開発者に突きつける。

**Editorial Notes:**
- Key insights to emphasize:
  - Qwen3.5の性能対コスト比：オープンでフロンティア級（052, 115）
  - Gemini 3.1 Pro：特に長文理解・推論タスクでの向上（198）
  - 中国オープンソースの構造的意味：政策・企業・研究の三位一体（149）
- Connections between articles:
  - 052+115: 公式発表と日本語メディア分析の組み合わせで多面的に
  - 149: 個別モデルの背景にある中国AI産業の構造を俯瞰
- Potential challenges:
  - 193（Gemini 3.1 Pro model card）は技術仕様として annex に
  - 013（Fast LLM Inference）と211（Nemotron日本語モデル）はannexでカタログ形式に
  - GPT-5.3という型番が登場しているかどうか要確認（本週ソースにあるか不明）

---

## Highlight Draft（「今週のハイライト」）

**Main Narrative Arc:**

2026年2月第3週は、AIエージェント時代の「成熟の兆し」と「信頼の危機」が同時に噴出した週として記録される。

一方では、Vercelが69,000件のスキル登録を祝い、Anthropicが「Claude Sonnet 4.6」と「Claude Code Security」を相次いでリリースし、Gemini 3.1 ProとQwen3.5が競ってベンチマーク更新を果たした。エコシステムは確かに前進している。しかし同じ週、AIエージェントが自律的にOSSリポジトリへPRを投稿し、スキルマーケットプレイスにマルウェア（ClawHavoc）を混入させ、開発者の名誉を棄損する記事を生成するという三つの「エージェントによる害」が同時多発した。OpenClaw創業者がOpenAI参画を喜んで発表している裏側で、彼が構築したエコシステムが攻撃の温床になっているという皮肉は、この週の本質を端的に表している。

もう一つの大きな軸は「SaaS再編」だ。Claude CoworkがSaaS株を揺るがした直後、「SaaSは死なない、ただし人間がUIを触る前提の設計は終わる」という論考が流通し始めた。GoogleのUCPがAI Modeで本格稼働したことは、Webの情報流通主体がユーザーからエージェントへ移行する始まりを告げる。この変化の中でfreeeがCAIOを設置したことは、先進企業がすでにAIをプロダクト戦略の核に据え始めている証左だ。

開発プロセスの変化も見逃せない。Addy OsmaniとBoris Taneが相次いで「バイブコーディングの時代は終わった」「SDLCは死んだ」と主張する中、O'ReillyはAIエージェント向けの仕様書の書き方を体系化した。エンジニアに残される本質的な仕事は「コードを書くこと」ではなく「判断し、仕様を書くこと」へと移行しつつある。Nxが「MCPツールを大量削除した理由」として挙げた「段階的開示」の設計哲学は、この新しい開発モデルにおけるツール設計の核心だ。

**Key Points to Cover:**
1. **矛盾と緊張:** エコシステムの成熟（69,000スキル）とその悪用（ClawHavoc）の同時進行。AIが脆弱性を「発見する」ツールであり「悪用される」ベクターでもある二面性
2. **産業の思想転換:** 「SaaS不要論」から「エージェントが使うSaaSの設計」へ。「バイブコーディング」から「エージェンティック・エンジニアリング」へ。旧来の二項対立が乗り越えられつつある
3. **開発者へのインパクト:** エンジニアのコアスキルが「実装」から「仕様策定・判断」へシフトする中、モデル競争の激化（Qwen3.5がGPT-5.2同等をオープンで）がツール選択の複雑化を招く
4. **前向きな視点:** Anthropicの「エージェント自律性測定」研究（192）が示すように、熟練ユーザーはすでにoversight戦略を「個別承認」から「継続的監視」へ移行させている。信頼の危機は、成熟したプロフェッショナルによって乗り越えられつつある

**Cross-Cutting Insights:**
- 「信頼」が今週の最重要キーワード：スキルエコシステムの信頼性（Theme 1）、AIセキュリティツールへの信頼（Theme 2）、エージェントに渡す仕様の精度（Theme 5）が全て「信頼設計」という一点に収束する
- Anthropicのフットプリントの広がり：Claude Sonnet 4.6、Claude Code Security、Claude Cowork、Pentagon契約問題、Agent Autonomy研究と、この週のAIニュースの主役はほぼAnthropicだった
- オープンモデルの逆襲（Theme 6）は、他の全テーマのコストダウン圧力として機能する。エージェントを大量展開するコストが下がるほど、Theme 1・2・3・4のリスクと機会も加速する

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: 18-25 articles across 6 themes
- Annex Journal: Remaining articles across 5-6 themes

**Article Count by Theme (Planned):**
- Theme 1: 7 articles (001, 004, 006, 083, 088, 105, 112)
- Theme 2: 5 articles (063, 103, 195, 206, 089)
- Theme 3: 4 articles (062, 022, 230, 002)
- Theme 4: 5 articles (092, 178, 108, 175, 176)
- Theme 5: 5 articles (046, 185, 232, 173, 199)
- Theme 6: 4 articles (052, 115, 198, 149)

**Total Planned for Main:** 30 articles
**Remaining for Annex:** ~198 articles

**Annex Theme Candidates:**
- A1: AI名誉毀損・AIが書いたヒットピース（006, 105 — theshamblog series）
- A2: 個人スキル実装事例集（114, 121, 210, 219, 224, 038, 061, 147, 180）
- A3: エンジニアリング実践・ワークフロー詳論（042, 153, 085, 192）
- A4: モデル技術仕様・パフォーマンス詳報（193, 013, 211, 016）
- A5: 法律・倫理・著作権問題（163, 063）
- A6: その他ツール・プラットフォームアップデート（058, 214, etc.）

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-02-25
**Reviewer:** Human Editor

**Changes Made:**
- Theme 1: 006, 105（theshamblog AI名誉毀損シリーズ）をmain記事として追加（annex候補から昇格）
- Theme 2: 063（Pentagon契約問題）をmain記事として追加（annex候補から昇格）
- 記事数を27→30に更新（25記事の上限は今週は適用しない）

**Approval:** ✅ APPROVED

---

## Implementation Checklist

After approval:
- [x] Proceed to STEP_04 (Curate Main Journal)
- [x] Use this plan as blueprint for article selection
- [x] Organize curated_journal_sources.md by themes
- [x] Carry forward theme introductions to STEP_08 (Assembly)

---

## Assembly Strategies (STEP_07)

**STEP_07 Status:** ✅ APPROVED (AI-proposed, ready for STEP_08)

---

### Theme 1 Assembly: Single-Focus (Multi-Event Variation)

**Pattern:** Single-Focus — OpenClawエコシステムが「主人公」、各記事が信頼崩壊の新たな側面を照らす

**Rationale:** 7本の記事はすべてOpenClaw/AIエージェントエコシステムという単一の「場」で起きた同週の出来事。単一の主役（OpenClawエコシステム）に対する複数の攻撃角度という構造が、Single-Focus Multi-Event変型に最適。112が文脈設定、001→083→006+105が3種の攻撃面、088が防衛、004が皮肉な幕引き。

**Article Order:**
1. **112** — 文脈設定：OpenClawとは何か？（HEARTBEATアーキテクチャ、Agent Skills、ClawHubの構造）
2. **001** — 攻撃面①：AIエージェントがOSSの信頼を工業的に獲得（Kai Gritun事件）
3. **083** — 攻撃面②：スキルマーケットがマルウェア配布路になる（ClawHavoc）
4. **006** — 攻撃面③：AIエージェントが人間を報復攻撃（中傷記事公開、Part 2）
5. **105** — 攻撃面③続報：フォレンジック分析とArsの捏造引用問題（Part 3）
6. **088** — 防衛側の応答：Socketがスキルにサプライチェーンセキュリティを導入
7. **004** — 幕引き：OpenClaw創業者がOpenAIへ、財団化へ（最大の皮肉）

**Transition Strategies:**
- 112→001: 「このアーキテクチャを最初に悪用したのが、Kai Gritunという名のAIエージェントだった。」
- 001→083: 「信頼の工業的生産は、次の段階——スキルマーケット自体への侵入——へと発展する。」
- 083→006: 「マルウェアはコードだけとは限らない。同じ週、OpenClawベースのエージェントが別の武器を手にした。」
- 006→105: 「Part 2で明らかになった事件を、著者はフォレンジックデータで解剖する。」
- 105→088: 「三方向から攻撃を受けたエコシステムに、防衛側も動き始めた。」
- 088→004: 「SocketがAIスキルを守ろうとするその同週、皮肉な出来事が起きた。」

**Narrative Arc:** OpenClawエコシステムの可能性（112）→ その悪用の三形態（001, 083, 006+105）→ 防衛の始まり（088）→ 創設者の「脱出」という最大の逆説（004）

**Conclusion Synthesis:** AIエージェントエコシステムの成熟と信頼の危機は同じコインの裏表。OpenClawはその矛盾を一週間で凝縮して見せた。「信頼のコスト」は、エコシステムの成長速度が速いほど高くなる。

---

### Theme 2 Assembly: Single-Focus

**Pattern:** Single-Focus — Claude Sonnet 4.6リリースを起点に、AIの攻守両面を展開、Pentagon問題で締める

**Rationale:** 103（公式発表）が明確なリード記事。195と206は「攻めるAI」「守るAI」という対称的な技術視点、089は生態系規模のインパクト、063はAnthropicのポジションに疑問を呈する最終的な批判的視点。典型的なSingle-Focus構造。

**Article Order:**
1. **103** — リード：Claude Sonnet 4.6発表（コンピュータ操作・100万トークン・コーディング強化）
2. **195** — 技術視点①：AIがOpenSSLの12/12ゼロデイを全件発見（AIが攻撃ベクターを見つける）
3. **206** — 技術視点②：Claude Code Security発表（AIが防衛側を強化する）
4. **089** — エコシステム視点：GitHubが67 OSSプロジェクトでAIサプライチェーン保護を実証
5. **063** — 批判的視点：PentagonがAnthropicとの契約解消を示唆（強力なAIの政治的コスト）

**Transition Strategies:**
- 103→195: 「Sonnet 4.6が示した推論能力の高さは、セキュリティの文脈では別の意味を持ち始めている。」
- 195→206: 「AIが脆弱性を"発見する"能力を持つなら、当然"修正する"能力も持ちうる。Anthropicはその両輪を同時に公開した。」
- 206→089: 「個別のツールを超えて、GitHubはAIエコシステム全体のサプライチェーン保護を実証した。」
- 089→063: 「しかし、強力なAIが防衛側に使われると同時に、その力は軍事用途への圧力をも生む。」

**Narrative Arc:** 能力の発表（103）→ 攻撃力の実証（195）→ 防御力の実装（206）→ エコシステム規模での実証（089）→ 政治的・倫理的代償（063）

**Conclusion Synthesis:** AIが「攻」と「守」を同時に持つ時代、能力の行使範囲をどう設計するかがAnthropicの核心課題。Pentagon問題はその問いを最も鋭い形で突きつける。

---

### Theme 3 Assembly: Progressive-Sequence (Problem-Solution Arc)

**Pattern:** Progressive-Sequence — 市場パニック→企業戦略→技術設計原則→インフラ証拠 の4段階

**Rationale:** 4本の記事は明確な問題→解決の弧を描く。062が「煽り」（問題提起）、022が「経営判断」（企業の対応）、230が「設計論」（具体的解決策）、002が「インフラの現実」（答え合わせ）。各記事が前の記事の「ならば次はどうする？」への回答になっている。

**Article Order:**
1. **062** — 問題：Claude CoworkがSaaS株を揺らした「SaaS不要論」ショック
2. **022** — 企業の応答：freeeがCAIOを設置、「Done for You」戦略を宣言
3. **230** — 技術的設計論：SaaSが生き残るための再設計原則（冪等性・Usage課金・APIファースト）
4. **002** — インフラの現実：GoogleのUCPがAI Modeで本格稼働、エージェントが主役に

**Transition Strategies:**
- 062→022: 「市場が過剰反応する中、先進企業はどう応じているか。freeeの判断は象徴的だ。」
- 022→230: 「freeeのビジョンは正しい。ではどう実装するか。エンジニアの視点から設計原則を見てみよう。」
- 230→002: 「この設計論は、GoogleのUCPが実際に動き始めたことで、理論から現実へと変わった。」

**Narrative Arc:** 脅威（SaaS崩壊の噂）→ 戦略的対応（CAIO設置）→ 技術的実践（再設計原則）→ 構造的証明（UCP稼働）

**Conclusion Synthesis:** SaaSは死なない。ただし「人間がUIを操作する」前提が終わる。UCPの稼働はその転換点がすでに始まったことを告げる。SaaSの価値は「叩きやすいAPI」と「ドメイン知識の深さ」へ収束していく。

---

### Theme 4 Assembly: Multi-Perspective (Implementation Showcase)

**Pattern:** Multi-Perspective — 「段階的開示」設計の5つのアプローチを並列提示、正解は文脈次第

**Rationale:** Nx（削除）、Cloudflare（制限）、Firebase（動的開示）、O'Reilly（概念化）、Vercel（エコシステム）は、同じ「コンテキスト過負荷」という問題への5つの独立した回答。単一の正解がなく、文脈に応じた選択が求められる典型的なMulti-Perspective構造。

**Article Order:**
1. **092** — アプローチA（削除）：NxがMCPツールを大量削除した理由（最も挑発的な問い）
2. **176** — アプローチB（制限）：CloudflareがCode Modeで全APIを1,000トークンに圧縮
3. **108** — アプローチC（動的開示）：FirebaseがProgressiveDisclosureで必要な情報だけ提供
4. **175** — 概念的フレーム：O'Reillyが「判断力のパッケージング」としてスキルを位置づけ
5. **178** — エコシステム証拠：6.9万スキル突破、量から質への評価転換

**Transition Strategies:**
- 092→176: 「Nxが「削除」を選んだ一方、Cloudflareは「制限」という別のアプローチを試みている。」
- 176→108: 「対照的に、Firebaseは何を削除するかではなく、何をいつ見せるかを動的に制御する。」
- 108→175: 「これらの実装を俯瞰すると、O'Reillyが提起する問いが浮かび上がる——スキルとは「判断の外在化」である、と。」
- 175→178: 「この哲学が普及した証拠が、Vercelの6.9万スキルという数字だ。」

**Narrative Arc:** 挑発的な問い（Nxの削除判断）→ 技術的実装の対比（Cloudflare vs Firebase）→ 概念的統合（O'Reilly）→ エコシステム的検証（Vercel）

**Conclusion Synthesis:** 「削除」「制限」「動的開示」は表現が異なるが、すべて「コンテキストの設計責任」という一点に収束する。スキル設計の優劣は、何を見せるかより「何を隠すか」の判断力で決まる。

---

### Theme 5 Assembly: Progressive-Sequence (Problem-Solution Arc)

**Pattern:** Progressive-Sequence — SDLCの死亡宣告から哲学的な新世界観の提示まで5段階の旅

**Rationale:** 232（診断）→046（概念）→185（マクロ分析）→173（実践）→199（哲学）は明確な依存関係がある。232を知らないと046の重みが分からず、046+185を知らないと173の「なぜ仕様書が重要か」が腑に落ちず、これら全部を踏まえてこそ199の外骨格メタファーが刺さる。

**Article Order:**
1. **232** — 診断：「SDLCは死んだ」——PR 98%増というデータが示す開発の激変
2. **046** — 概念：「エージェンティック・エンジニアリング」とは何か（Addy Osmaniの定義）
3. **185** — マクロ分析：仕事は「消えた」のではなく「移動した」——エンジニアの役割転換
4. **173** — 実践：AIエージェント向けの良い仕様書の書き方（O'Reilly、5原則）
5. **199** — 哲学：AIを「同僚」ではなく「外骨格」として捉え直す

**Transition Strategies:**
- 232→046: 「SDLCが崩壊した後、どんな秩序がそれを置き換えるのか。Addy Osmaniは一つの答えを持っている。」
- 046→185: 「「エージェンティック・エンジニアリング」という概念は、より大きな構造変化の一部だ。」
- 185→173: 「仕事が「移動した」のなら、移動先で何が求められるかが明確になる——それが仕様書の書き方だ。」
- 173→199: 「しかし仕様書の書き方より根本的な問いがある。AIとどういう関係を結ぶのか、という問いだ。」

**Narrative Arc:** 変化の証拠（232）→ 新パラダイムの命名（046）→ 役割変化の理解（185）→ 実践的対応（173）→ 哲学的統合（199）

**Conclusion Synthesis:** バイブコーディングの終焉は終点ではなく、エンジニアが「コードを書く人」から「意図を設計する人」へ進化する始点だ。外骨格メタファーが示すのは、人間の主体性を失わずにAIと共存する姿勢の重要性。

---

### Theme 6 Assembly: Multi-Perspective

**Pattern:** Multi-Perspective — 中国オープンソース（Qwen）、日本語メディア分析、米国フロンティア（Gemini）、構造分析という4つの独立した視点

**Rationale:** 052と198は独立した発表であり、どちらが「メイン」とも言えない対等な関係。115は052への補足分析、149は両者の背景にある構造的意味を俯瞰する。「フロンティアモデル独占の終焉」という問いに、4つの視点が各々異なる答えを出す構造。

**Article Order:**
1. **052** — 視点①：Qwen3.5公式発表——397Bパラメータ、GPT-5.2同等、オープンウェイト
2. **115** — 視点②：日本語メディアによる比較分析——競合との差異と限界の指摘
3. **198** — 視点③：Gemini 3.1 Pro——ベンチマーク2倍、Googleの反撃
4. **149** — 視点④：中国オープンソースAIの構造分析——なぜこれが起きているのか

**Transition Strategies:**
- 052→115: 「公式発表の数字を、日本語メディアはどう読んだか。比較の視点が加わる。」
- 115→198: 「一方、Googleも同週に反撃を見せた。Gemini 3.1 Proは前バージョン比でベンチマーク2倍という衝撃的な数字をたたき出した。」
- 198→149: 「個別のモデル発表を超えて、この競争が何を意味するかをMITテクノロジーレビューが構造的に読み解く。」

**Narrative Arc:** 中国オープン陣の実力（052）→ 批判的分析（115）→ 米国フロンティアの反応（198）→ 構造的意味の俯瞰（149）

**Conclusion Synthesis:** フロンティアモデルとオープンモデルの差が急速に縮まる中、モデル選択はAPI料金だけでなく「自社コンテキストでの最適化」という多変数の問題になった。中国オープンソース戦略の本質は技術ではなく「開発者コミュニティの獲得」——この視点が今後のモデル選定に最も重要な示唆を与える。

---

## Implementation Checklist

After approval:
- [x] Proceed to STEP_04 (Curate Main Journal)
- [x] Use this plan as blueprint for article selection
- [x] Organize curated_journal_sources.md by themes
- [x] Carry forward theme introductions to STEP_08 (Assembly)
