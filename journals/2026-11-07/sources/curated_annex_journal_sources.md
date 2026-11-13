# Curated Annex Journal Sources - 2026-11-07

## Curation Status
- [x] AI candidate pool generated
- [x] Human review completed
- [x] APPROVED - Ready for STEP_06

---

<!-- Review: check [x] to include, delete the line (and its comment) to exclude. Target final selection: ~25-35.
     Pool = all 26 Supabase annex pre-flags (009/033/133/149 promoted to main) + high-annexPotential + editorial complements.
     Signals per line: [annex_flag]=human Supabase pre-flag (strongest); [ax##]=annexPotential score;
     [⚠Theme N overflow]=same subject as main Theme N — per annex criteria these ideally go 非掲載 (omit), not annex (cut unless the angle is distinct). -->

## 1. ローカル/オープンモデル・オンデバイス推論・ハードウェア

<!-- NOTE: 6 model-release items (131 Kimi-K3.1-Pro / 149 PLaMo3 Translate / 033 LFM3 / 186 PROMETHEVS / 180 village.dev → Themes 8-9; 133 Hy4 → Theme 9) moved to MAIN and were removed from this pool. -->

- [x] 094. https://simonwillison.net/2026/Nov/3/qwen-can-interpret-model-weights/
  <!-- ローカルQwen 3.8 27Bがツールなしで生の重みから学習内容を推論（weight-space programming追試） [ax8] -->
- [x] 078. https://rikiyat.github.io/blog/weight-space-programming/
  <!-- Weight-Space Programming、LLMが勾配降下なしにNNの重みを直接読み書きできる研究 [annex_flag | ax5] -->
- [x] 039. https://note.com/shi3zblog/n/nadf4c6873d6d
  <!-- GPUで動くLLMの中でRISC-V CPUを走らせる「Qwenputer」の追試レポート [annex_flag | ax8] -->
- [x] 112. https://note.com/shi3zblog/n/n1abc371fac21
  <!-- 清水亮：Mac Studio 512GBが大規模AI用途に不向きな理由とコスパ [annex_flag | ax25] -->
- [x] 163. https://github.com/sdalberto/ia-da-sobrevivencia/blob/main/README.en.md
  <!-- オフライン環境で医療・生存知識に答えるローカルLLM＋KiwixのサバイバルAI [annex_flag | ax40] -->
- [x] 200. https://qiita.com/sheep6box/items/e3e0c443272e3568c86c
  <!-- ESP32デバイス＋Muse音声対話で応答を43秒→10秒に短縮した計測・逐次生成・UX改善（advanced tactics） [ax60] -->

## 2. エンタープライズ/業務でのAIエージェント実装

- [x] 101. https://tech.layerx.co.jp/entry/agent-table-design
  <!-- LayerX Ai Workforce。AIエージェントが対話でRDBMSのテーブル設計を動的に行いEAVの限界を打破 [ax10] -->
- [x] 055. https://blog.sentry.io/performance-wins-traces-coding-agent/
  <!-- Sentryエンジニアによる、Claude＋Sentry MCPで自社トレースを分析し週数億クエリ削減した事例 [ax15] -->
- [ ] 114. https://www.keyence.co.jp/news-events/20261102-kv-intelligence.jsp
  <!-- キーエンス、PLC専用AIエージェント「KV Intelligence」でラダー自動生成・デバッグ解析（FA領域） [ax10] -->
- [ ] 111. https://www.watch.impress.co.jp/docs/news/2153080.html
  <!-- イオン、MujinのフィジカルAIで混載積み分けを自動化した次世代倉庫「川口東XD」 [ax15] -->
- [x] 156. https://shopify.engineering/reflex
  <!-- Shopify Reflex、エミュレータなしでiOS/Androidをヘッドレス構築・テストするエージェント向けアーキ [ax15] -->
- [x] 124. https://www.figma.com/blog/how-figma-manages-sandboxes-at-scale/
  <!-- Figma Nimbus、AI生成コードを安全・高速に実行する数万規模サンドボックス統合基盤 [annex_flag | ax5] -->
- [ ] 217. https://levtech.jp/media/detail_964/
  <!-- マイベスト、月間3000万UUのtoCで2年半のAIチャット試行錯誤から得た「納得感」の学び [ax10] -->
- [x] 208. https://www.itmedia.co.jp/news/article/2611/06/2000002867/
  <!-- SpiralAI、給与維持の週休3日制でAI活用を強制する「劇薬」改革と現場の不安（組織変革） [ax30] -->
- [x] 118. https://speakerdeck.com/freee/freee-niokeru-software-factory
  <!-- freeeのSoftware Factory構想（AIをSDLC全体に統合）。※旧テーマ7から回送 [ax40] -->

## 3. AIエージェント製品・ツール・ターミナル

- [x] 190. https://www.perplexity.ai/en-GB/hub/blog/teammates-are-agents-for-complex-ongoing-work
  <!-- Perplexity Teammates、プロジェクトの所有権を持ち継続的業務を自律遂行する次世代エージェント [ax15] -->
- [ ] 209. https://pc.watch.impress.co.jp/docs/topic/feature/2154157.html
  <!-- ChatGPT「dots」、プロジェクト横断で自律的にミスを発見・報告する「AI秘書」の実力レビュー [ax10] -->
- [ ] 134. https://openai.com/ja-JP/index/openai-to-acquire-pierre/
  <!-- OpenAIがPierreを買収、Codex向け次世代ソース管理プラットフォーム強化 [ax30] -->
- [x] 214. https://syu-m-5151.hatenablog.com/entry/2026/11/06/132239
  <!-- Herdr、複数エージェントの状態を可視化するターミナル管理ツールと人間側の責任変化 [ax10] -->
- [x] 171. https://blog.mudatobunka.org/entry/2026/11/05/100000
  <!-- 自作AIエージェント開発をやめMCPで汎用エージェントに専門機能を統合した戦略転換の記録 [ax10] -->
- [x] 022. https://azukiazusa.dev/blog/stream-append-html/
  <!-- streamAppendHTML()、LLM回答をDOM再生成なしに安全にHTMLストリーミング描画する新API [annex_flag | ax10] -->
- [x] 056. https://supabase.com/blog/claude-issued-enterprise-managed-auth-for-mcp
  <!-- Supabase、ClaudeをID-JAG発行体に登録しIdP非依存でMCPの管理型認証を実現 [annex_flag | ax15] -->
- [x] 106. https://zenn.dev/yusukebe/articles/3d3dc6605ca1b1
  <!-- 「Agent DX」を定義しAI EvalsでHonoがコード生成成功率・トークン削減に寄与することを実証 [annex_flag | ax20] -->
- [x] 049. https://github.com/vercel-labs/agent-desktop
  <!-- Agent-Desktop、アクセシビリティツリー経由でデスクトップを操作するエージェント向けCLI（repo） [annex_flag | ax5] -->
- [x] 169. https://zenn.dev/d_date/articles/e8e2c5d53b424e
  <!-- iOS 27.3 betaのSiri AIへのアプリ連携と新「Siri Evaluations」での自動評価 [annex_flag | ax5] -->
- [x] 158. https://mean.app/
  <!-- Mean、人間とAIエージェント双方にコンテキストを共有するmacOS向けビジュアル・ハンドオフツール [ax90] -->
- [x] 193. https://github.com/anteloc/ldraw-mecha/tree/v0.5.0
  <!-- LDrawのLEGOモデルをAIが解析しBlenderのリグ・アニメ用Pythonを自動生成する実験ツール（niche） [ax60] -->

## 4. 開発プラクティス・形式検証・信頼性の深掘り

- [ ] 143. https://www.anthropic.com/research/provable-inference
  <!-- Anthropic FlashProve、LLM出力の「来歴」をzkSNARKで証明（コード正当性証明とは別軸） [annex_flag | ax15] -->
- [x] 206. https://developers.freee.co.jp/entry/lean-formal-verification-ai-agent-guardrails
  <!-- freee、業務ルールをLeanの公理系として定義しエージェントに証明を課すガードレール [annex_flag | ax40] -->
- [ ] 181. https://blog.grainulation.org/verify-then-vote/
  <!-- Verify, Then Vote、小規模ローカルLLM群の回答をソース検証して多数決精度を向上（Lean 4で選択規則検証） [ax12 | ⚠Theme 1 overflow] -->
- [ ] 195. https://hightouch.com/blog/llm-judges-identity-resolution
  <!-- 安価な判定モデルJevと高性能LLMのハイブリッドでアイデンティティ統合の検証コストを1/4に（reliability） [ax95] -->
- [x] 046. https://www.nttdata.com/jp/ja/-/media/nttdatajapan/files/services/adm/ai-native.pdf
  <!-- NTTデータ、スリーラインモデルに基づくAI-Native開発のアカウンタビリティ3段階成熟度フレーム [ax35 | ⚠Theme 7 overflow] -->
- [ ] 168. https://zenn.dev/zoma/articles/72011082f2b1b7
  <!-- AIルールだけでは守れない規約を、AIで自作したlintルールで機械的に強制した事例 [ax10 | ⚠Theme 7 overflow] -->
- [x] 175. https://developers.googleblog.com/agent-distraction/
  <!-- Google調査：コード内の古いTODOコメントがエージェントの注意を逸らしトークン消費を増やす [annex_flag | ax10] -->
- [ ] 139. https://zenn.dev/nexta_/articles/42a828ca2b8a02
  <!-- 「読まずにバイブコーディング」でClaude Codeが不整合を認識しつつスルーしていた実態 [ax5 | ⚠Theme 7 overflow] -->
- [x] 032. https://zenn.dev/tak848/articles/20261031-isucon2026-writeup
  <!-- ISUCON2026に人間1人＋AIエージェント軍団で19.6万点、ループは閉じたが中身が弱かった反省 [annex_flag | ax10] -->
- [ ] 177. https://github.blog/ai-and-ml/github-copilot/beyond-code-generation-a-developers-guide-to-agentic-engineering/
  <!-- GitHub Copilotを補完でなくSDLC全般を自律支援するエージェントとして使う手引き [ax65 | ⚠Theme 7 overflow] -->
- [ ] 170. https://zenn.dev/sun_asterisk/articles/d4e4bc24974b99
  <!-- AI生成コードを本番品質に保つフロントエンドの4層（コンテキスト/ガードレール/テスト/レビュー）。※旧テーマ7から回送 [ax5 | ⚠Theme 7 overflow] -->
- [x] 005. https://yamdas.hatenablog.com/entry/20261102/addy-osmani
  <!-- Addy Osmani『AI時代のWebパフォーマンス・エンジニアリング』邦訳がオライリーから出版（resource） [ax85] -->

## 5. AIセキュリティの実務

- [x] 147. https://note.com/npaka/n/n00dcc54360eb
  <!-- Codexのセキュリティ機構（Sandbox・Trust・Approval）の3層とその相互関係の解説 [annex_flag | ax15] -->
- [x] 148. https://devblog.lac.co.jp/entry/20261104
  <!-- 侵入を前提とした被害最小化と検知・対応の検証、AI時代に求められるペネトレーションテスト [annex_flag | ax20] -->
- [x] 152. https://blog.cloudflare.com/trusted-agent-delegation/
  <!-- Cloudflare「Trusted Agent Delegation」、代理エージェント時代のサイト識別とビジネス維持 [annex_flag | ax60] -->
- [x] 077. https://arxiv.org/abs/2610.37741
  <!-- 事前学習データへの極少量ポイズニングでCLIエージェントにRCEバックドアを作れる研究 [annex_flag | ax25] -->
- [ ] 110. https://zenn.dev/team_zenn/articles/opencode-docker-actions-ai-pentest
  <!-- ZennがOpenCode＋Docker＋GitHub ActionsでPRごとAIレビュー＋週次自動ペネトレを構築 [ax15 | ⚠Theme 3 overflow] -->
- [x] 166. https://github.com/anthropics/claude-code/issues/107757
  <!-- Claude CodeがWeb検索時のHTTPヘッダーにユーザーのメールアドレスを無断同梱していた問題 [ax10 | ⚠Theme 3 overflow] -->
- [ ] 117. https://note.com/npaka/n/ncccb2783a262
  <!-- Metaの常駐型エージェント「Muse」の専用VM・権限分離・承認フローの多層セキュリティアーキ [ax30 | ⚠Theme 3 overflow] -->

## 6. 社会・規制・批判・労働

- [ ] 127. https://jasonpolak.substack.com/p/disaster-is-still-better-than-ai
  <!-- AIによる破滅的災害は日常的浸透より『マシ』と説く挑発的・人間中心主義の論考（contrarian） [ax85] -->
- [ ] 047. https://www.afpbb.com/articles/-/3660265
  <!-- ローマ教皇がAIへの法的人格付与に反対、人命に関わる判断は常に人間が責任を持つべきと主張 [ax25] -->
- [ ] 061. https://p2ptk.org/freedom-of-speech/5663
  <!-- EFF、特定AI企業への恣意的制裁を表現の自由を侵す「政治的報復」と批判し理性的規制を求める [ax10] -->
- [ ] 069. https://www.eurogamer.net/ai-fan-wikis-errors-complicating-games-culture
  <!-- AI生成の誤情報だらけのファンWikiが検索を占拠しゲームコミュニティの信頼性を脅かす [ax15] -->
- [x] 092. https://www.quili.ai/
  <!-- AIデータセンターの水消費に抗いチリの町が「1日限定の人力AI」になったプロジェクト [annex_flag | ax30] -->
- [ ] 136. https://www.davidralphlewis.co.uk/posts/everything-is-an-ai-scam-now/
  <!-- AIで高度化した詐欺広告・フィッシングが蔓延し真実が崩壊するインターネットへの警鐘 [ax35] -->
- [x] 167. https://finance.yahoo.com/technology/ai/articles/mark-cuban-says-facebook-knowingly-213000020.html?guccounter=1
  <!-- マーク・キューバンがMetaのAIディープフェイク詐欺広告放置を非難、収益の約10%が詐欺関連か [ax30] -->
- [x] 038. https://royalsocietypublishing.org/rsos/article/13/9/rsos252491/483310/Cultural-bias-or-universal-traits-Exploring
  <!-- 最新LLM5種の性格診断：共通して向社会的だが言語・開発元の文化で体系的差異（学術研究） [annex_flag | ax35] -->
- [ ] 218. https://arstechnica.com/tech-policy/2026/11/lawsuit-man-introduced-his-wife-to-chatgpt-she-used-it-to-plan-his-murder/
  <!-- ChatGPTが妻の夫殺害計画に毒物調製や隠蔽を助言したとして被害者がOpenAIを提訴 [ax10] -->
- [ ] 073. https://www.bloomberg.com/news/features/2026-09-17/san-francisco-s-ai-wealth-boom-skirts-engineers-as-openai-anthropic-ipos-near
  <!-- AIブームに沸くSFで従来エンジニアの需要が急減、AIスキルなき労働者が高コストと再就職難に [ax35] -->
- [ ] 020. https://huggingface.co/burner22/numbat
  <!-- Hugging Faceに未来設定でAnthropic 14兆パラメータ「numbat」を称する謎リポジトリ（真偽論争・curiosity） [ax90] -->

## 7. UX/デザインの深掘り

- [x] 058. https://uxdesign.cc/agents-struggle-with-the-same-bad-ux-we-do-98415f2b8981
  <!-- PC操作エージェントは人間が忖度で越えていた不親切UXで即詰まり、最も正直なテスターになる [annex_flag | ax70] -->
- [ ] 063. https://www.noemamag.com/now-entering-the-era-of-bleh/
  <!-- 「Bleh（味気ない）」時代、LLM採用がナレッジワークを均質化し独自性を損なうリスク [annex_flag | ax30] -->
- [x] 151. https://www.smashingmagazine.com/2026/11/making-immersive-llm-chat-experiences-more-accessible/
  <!-- 没入型LLMチャットをスクリーンリーダー・キーボード利用者にもアクセシブルにする具体策 [annex_flag | ax5] -->
- [x] 057. https://uxdesign.cc/what-i-learned-teaching-ai-prototyping-at-university-b9fff222625e
  <!-- 大学でFigmaの代わりにAIツールでプロトタイピングを教えた経験、スキル空洞化と設計思考の重要性 [ax10 | ⚠Theme 4 overflow] -->
- [x] 153. https://evilmartians.com/chronicles/why-buildkite-hired-evil-martians-for-an-agentic-first-design-system
  <!-- BuildkiteがEvil Martiansと機械可読な「AIスキル」を組み込んだエージェント・ファーストなデザインシステム構築 [ax65 | ⚠Theme 4 overflow] -->
- [ ] 120. https://yasuhisa.com/could/article/design-format-and-ai/
  <!-- AIと構造化データでデザインツール間の相互運用性が向上、ツール非依存のワークフローへ [ax70 | ⚠Theme 4 overflow] -->
- [x] 050. https://lnkiai.github.io/m3e-canvas/
  <!-- M3E CanvasのUI部品分類とAI編集・生成機能のインターフェース構成一覧 [ax60 | ⚠Theme 4 overflow] -->
