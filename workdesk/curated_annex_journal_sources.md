# Curated Annex Journal Sources - 2026-11-14

## Curation Status
- [x] AI candidate pool generated
- [x] Human review completed
- [x] APPROVED - Ready for STEP_06

---

<!-- STEP_04 §4 candidate pool (pre-gate). Independent-topic clusters only — not main-theme overflow. -->
<!-- Built from: 16 Supabase annex pre-flags (annex_flag) + Rev.1-demoted clusters + plan's named annex clusters. -->
<!-- Review in STEP_05: check [x] to keep, delete line to drop. Target after trim: ~25–35. -->
<!-- Signals: annex_flag = human pre-flag (Supabase) ／ ⭐ = standout ／ annexPotential = AI score. -->

## 1. 内製エージェント基盤・開発ハーネス

- [x] 137. https://zenn.dev/ubie_dev/articles/45501469c9c044
  <!-- Ubieの全社AI-Nativeクラウドエージェント基盤「Remoco」とエンジニアリングエージェント「Uvin」。Signals: ⭐ standout（Rev.1でmainから移動）  ax10 -->
- [x] 079. https://gibberishlab.com/blog/oss-ai-agent-harness-philosophy
  <!-- 有名OSSのAGENTS.md・フック・スキル構成を「AIへの信頼度」軸で比較した5事例。Signals: annexPotential 85（Rev.1でmainから移動） -->
- [ ] 146. https://speakerdeck.com/takateeen_knj/20261110-claude-deepdive
  <!-- Claude Codeを組織で安全運用するための多層ガバナンス・制御（ハーネス）Deep Dive。Signals: （Rev.1でmainから移動）  ax30 -->
- [ ] 064. https://zenn.dev/otar/articles/switchboard-own-dev-environment
  <!-- 自作ツールSwitchboardでGitHub制限等を解決し2か月で1,300超PRを自動生成した記録。Signals: （Rev.1でmainから移動）  ax20 -->
- [ ] 063. https://zenn.dev/minty1st/articles/51b1422d660d26
  <!-- AIエージェント「Pi」でClaude Opus＋DeepSeekを組み合わせた低コスト自動開発ハーネス事例。Signals: annex_flag  ax65 -->
- [x] 071. https://zenn.dev/pksha/articles/laplace-build-guide
  <!-- PKSHAのAIネイティブデータ分析基盤「Laplace」。人・プロダクト・権限・AIの4境界で安全性を設計。Signals: annex_flag  ax40 -->

## 2. AI市場・資金調達・バブル論（Rev.1でmainから移動）

- [ ] 121. https://www.techpowerup.com/354814/nvidia-allegedly-engineered-scarcity-by-funding-ai-startups-to-buy-its-gpus
  <!-- NVIDIAがAIスタートアップへ出資し自社GPUを買わせる「循環融資」で品不足を演出した疑い（WSJ報）。  ax5 -->
- [ ] 224. https://www.economist.com/leaders/2026/11/12/why-you-should-expect-an-ai-crash
  <!-- AIバブル崩壊に備えるべき理由（The Economist）。循環型資金調達・ドットコムとの類似・市場調整の必然。※要約はHN議論ベース、URLは正規（Economist）。Signals: annexPotential 45 -->
- [ ] 025. https://247wallst.com/investing/2026/11/07/openai-just-raised-11-billion-at-a-1-25-trillion-valuation-below-the-1-4-trillion-it-first-sought/
  <!-- OpenAIが1.25兆ドル評価で110億ドル調達、当初目標1.4兆ドルには届かず期待値調整を示唆。  ax30 -->
- [ ] 016. https://www.kadoa.com/companies/insights/ai-selloff-perspective
  <!-- AI株下落をS&P500全体では軽微な調整、半導体株ではコロナショック級と位置づける比較分析。Signals: annexPotential 40 -->

## 3. ローカル・オープンウェイト／オンデバイスAI

- [x] 092. https://www.ricursive.com/ripple
  <!-- Ripple-65B Preview。1/10コストでAgentic Coding米国オープンウェイトSOTAを主張。  ax10 -->
- [x] 140. https://zenn.dev/fixstars/articles/kimi-k31-pro-benchmark
  <!-- Kimi-K3.1-ProをB300でセルフホストし独自アセンブリ最適化ベンチで性能実証。  ax15 -->
- [x] 018. https://nousresearch.com/arete
  <!-- Qwen3.8-27Bをベースに西欧的価値観でポストトレーニングし政治バイアス低減を狙うArete-27B。Signals: annexPotential 35 -->
- [x] 174. https://huggingface.co/blog/ggml-org/llama-cpp-v1
  <!-- llama.cpp v1.0.0。semverでAPI安定化、ローカルAIエコシステムの基盤化。  ax15 -->
- [x] 102. https://translate.preferredai.jp/news/20261105-2-plamo3-translate-open-weight/
  <!-- PFNの翻訳特化LLM「PLaMo 3 Translate」。53言語・オフライン動作をオープンウェイト公開。  ax5 -->
- [ ] 120. https://unsloth.ai/docs/models/qwen3.8
  <!-- Qwen3.8をGGUF/NVFP4でローカル高速・低メモリ実行するUnslothの設定ガイド。  ax15 -->
- [x] 157. https://content.claris.com/local-ai-server-get-started
  <!-- Apple子会社ClarisのMac向けプライベートAIサーバー「Claris Harbor」。Thunderbolt 5でメモリをプール。Signals: annexPotential 65 -->
- [ ] 093. https://wirelesswire.jp/2026/11/94903/
  <!-- 小さなローカルAIが「プログラムを売る」商売を終わらせるというソフトウェア産業消滅論。Signals: annexPotential 40 -->
- [x] 087. https://shizuku.ai/en/blog/1/
  <!-- 相槌・割り込み対応の80ms低遅延 日本語フルデュプレックス音声対話モデル Shizuku-Duplex。Signals: annex_flag  ax35 -->

## 4. AI導入の現実・生産性のギャップ

- [x] 212. https://cabird.com/talks/shipping-faster/
  <!-- コード生成の高速化が出荷速度に直結しない「活動と成果の乖離」を研究から分析した講演。  ax8 -->
- [x] 169. https://www.activtrak.com/news/productivity-lab-ai-users-longer-workdays/
  <!-- AI利用者は非利用者より勤務時間が最大90分長く集中が途切れるという9,140人調査。  ax12 -->
- [x] 188. https://www.oreilly.com/radar/measuring-ais-unintended-consequences/
  <!-- AI導入による保守性低下・バーンアウト等の副作用を定量評価する手法の提案。  ax15 -->
- [x] 236. https://blog.jetbrains.com/blog/2026/11/13/scaling-ai-agents-what-we-learned-from-9-real-world-cases/
  <!-- AIエージェントで成果を出す鍵はワークフロー整備・コードベース最適化・移譲スキルという9実例。Signals: annexPotential 90 -->
- [x] 145. https://www.itmedia.co.jp/news/article/2611/10/2000003040/
  <!-- PwCの「AI店長」実験。指摘を学習できず信頼が損なわれ、推論コスト優先で機会損失も。  ax10 -->
- [x] 189. https://blog.sentry.io/slopware-factory/
  <!-- SentryのCEOが語る、AIは完全自動化でなく退屈を減らす「不完全な工場」という現実観。  ax15 -->

## 5. Gemini 4 周辺の学習基盤・ツール（Google、main Theme 2 非収録分）

<!-- main Theme 2（045/159/219/220/167）へ昇格済み。下記は昇格しなかったGemini 4 周辺の候補。166はmain Theme 2（159/219）と同一主題のため omit 候補。 -->

- [x] 166. https://note.com/npaka/n/nf3aa0a193147
  <!-- Gemini 4 Hydrogenの概要（npaka解説）。※main Theme 2と同一主題＝omit候補。  ax5 -->
- [x] 241. https://developers.googleblog.com/what-is-pathways-single-controller-training-for-large-models/
  <!-- Gemini学習の分散システム「Pathways」がGoogle CloudでGA、SPMDの限界を超える。  ax15 -->
- [ ] 242. https://developers.googleblog.com/announcing-long-context-training-on-tpus-with-maxtext-context-parallelism/
  <!-- MaxText＋TPUで最大1,400万トークン学習を可能にするコンテキスト並列化戦略。  ax10 -->
- [ ] 243. https://developers.googleblog.com/from-prompt-to-app-build-with-google-maps-in-ai-studio/
  <!-- AI StudioとMaps統合で自然言語から地図アプリを即生成。Signals: annexPotential 70 -->

## 6. MCPエコシステム

- [x] 084. https://hiraoku.dev/blog/mcp-cli-cloud/
  <!-- 2026年7月の仕様変更で状態管理・コンテキスト圧迫が解消しCLIに対し復権したMCPの背景。  ax15 -->
- [x] 186. https://blog.modelcontextprotocol.io/posts/exploring-file-uploads-and-downloads-in-mcp/
  <!-- モデルのコンテキストを介さず大容量ファイルを転送するMCP拡張案。Signals: annex_flag  ax30 -->
- [x] 187. https://blog.modelcontextprotocol.io/posts/mcp-release-cycle/
  <!-- MCP仕様を年2回の固定スケジュール化し、リリースマネージャー制度を導入。Signals: annexPotential 40 -->
- [ ] 190. https://blog.sentry.io/mcp-or-cli/
  <!-- CLIとMCPを統合し、エージェントがCLIの機能と認証をシームレスに使える開発者体験。  ax15 -->
- [ ] 177. https://evilmartians.com/chronicles/building-uscreens-remote-multi-tenant-mcp-server-inside-a-rails-app
  <!-- 既存RailsアプリにマルチテナントのリモートMCPサーバーを統合する設計手法（Uscreen事例）。  ax5 -->
- [ ] 249. https://engineering.nature.global/entry/2026/11/mcp-architecture-patterns
  <!-- MCP組込みアプリを手元で複数動かす際のポート競合等を解消する5つの構成パターン。Signals: annexPotential 95 -->
- [ ] 085. https://github.com/DIYgod/pinky
  <!-- PCのAIエージェントからスマホを承認付きで操作できるOSSのMCPサーバー「Pinky」。  ax10 -->

## 7. Muse・パーソナルAIエージェント・新機能

- [ ] 070. https://zenn.dev/watany/articles/342b9815dd0553
  <!-- MetaのエージェントMuseを司令塔に外部LLM/コーディングエージェントを束ねる実践ガイド。Signals: annexPotential 60 -->
- [ ] 091. https://www.watch.impress.co.jp/docs/series/nishida/2154614.html
  <!-- AIが「最安」を選び続ける世界の是非。Museが購買を代行する未来の経済秩序を考察。  ax25 -->
- [ ] 151. https://pc.watch.impress.co.jp/docs/topic/feature/2155692.html
  <!-- 24時間クラウドで動く「相棒」としてのMuseを2週間試用したレビュー。  ax30 -->
- [ ] 245. https://www.watch.impress.co.jp/docs/news/2155063.html
  <!-- MuseがApple Watch/Wear OSに対応、アバターが動く。  ax15 -->
- [ ] 115. https://claude.com/ja/resources/articles/claude-meetings
  <!-- AIがビデオ会議に参加し議事録・ドキュメント化・質問回答を支援する「Claude Meetings」ベータ。  ax15 -->
- [ ] 149. https://claude.com/ja/resources/articles/sheets-whiteboards-data
  <!-- Claude内でブレスト・表計算・データ分析を行うWhiteboards/Sheets/Dataの発表。  ax10 -->
- [ ] 122. https://claude.com/ja/resources/articles/projects-redesigned
  <!-- タスク分解・委任・並行実行を自律管理する刷新版「Claude Projects」。  ax10 -->
- [ ] 099. https://zyphra.com/maia
  <!-- Slack等と連携しチームの文脈を学習して自動化する「AI同僚」MAIAベータ。Signals: annexPotential 75 -->
- [ ] 168. https://www.techno-edge.net/article/2026/11/13/5713.html
  <!-- 元Anker CMOが作る11gのAIウェアラブル「Memoket Gem」。長期記憶で現実の会話を補完。  ax10 -->

## 8. エージェント対応Web・UI（agent-ready）

<!-- 要判断: 本クラスタはmainテーマ6「AIとともにデザインする」と主題が近接。特に160はmain 124（Vercel UI SDK）と同一主題。STEP_05のレビューでannex維持かmain昇格か除外かを判断してください。 -->

- [x] 238. https://www.tak-dcxi.com/article/make-website-agent-ready/
  <!-- サイトをAgent Readyにする実装記録（Markdownネゴシエーション・llms.txt・Content-Signal）。Signals: annex_flag（テーマ6隣接）  ax10 -->
- [x] 202. https://www.vlt.io/blog/act-accordingly
  <!-- Next.jsから自動でMarkdownを生成しエージェント理解度を高めるOSSプラグイン@affordances/md。Signals: annex_flag（テーマ6隣接）  ax15 -->
- [x] 160. https://github.com/vercel-labs/ui
  <!-- Vercel Labsのフレームワーク非依存な振る舞いベースUIライブラリ。Signals: annex_flag（⚠ main 124と同一主題の可能性）  ax15 -->

## 9. 論考・研究・その他（独立トピック）

- [x] 047. https://stoppels.ch/2026/10/03/wake-me-up-when-ai-can.html
  <!-- 2016–2026のHNコメントから800超の「AIへの期待」を抽出し約1万人が達成状況を投票検証。Signals: annex_flag（テーマ8隣接）  ax20 -->
- [x] 050. https://opensource.googleblog.com/2026/11/sandboxing-untrusted-ai-agents-at-scale.html
  <!-- GoogleがエージェントのオーケストレーターAgent SubstrateとgVisorをCNCFに寄贈。Signals: annex_flag  ax10 -->
- [x] 113. https://osssaysno.com/
  <!-- AI生成物の投稿を禁止するOSSプロジェクトを一覧化したカタログ「Open Source Says No」。Signals: annex_flag（テーマ8隣接）  ax65 -->
- [x] 148. https://arxiv.org/abs/2611.05306
  <!-- 長文生成コスト最大7倍を指摘し、頻繁な圧縮（コンパクション）とSSSMで短文脈でも精度維持。Signals: annex_flag  ax45 -->
- [x] 171. https://nowokay.hatenablog.com/entry/2026/11/13/101644
  <!-- Fable 5.2で物理モデリング音源のコード生成と高度な作曲を検証した実験。Signals: annex_flag（テーマ1隣接）  ax30 -->
- [x] 172. https://joisino.hatenablog.com/entry/searchrecbook
  <!-- LLM時代の検索（RAG vs 全文プロンプト）と推薦のパラダイムシフトを専門家が解説。Signals: annex_flag  ax8 -->
- [ ] 208. https://babuschk.in/posts/2026-01-25-life-on-claude-nine.html
  <!-- エージェント自動化が社会の自律統治・再帰的自己改善の恐怖へ至るSF短編。Signals: annex_flag annexPotential 95（テーマ8隣接） -->
- [x] 217. https://blog.cip.org/p/ai-models-know-what-women-peace-and
  <!-- AIが「女性・平和・安全保障(WPS)」視点を自発的に適用できない課題を測る初の公開ベンチ。Signals: annex_flag  ax15 -->
- [x] 191. https://shopify.engineering/cyber-chaos-monkey
  <!-- 本番環境へ安全に攻撃し攻撃者より先に脆弱性を特定する自律型「Cyber Chaos Monkey」。Signals: annex_flag（テーマ5隣接）  ax25 -->


## 10. 全非掲載スイープで追加した独立候補（annexPotential ≥60、STEP_04で未収録だったもの）

<!-- 全非掲載153件をannexPotentialでスイープし、8テーマと独立かつ高スコアの候補を追加。👎除外済み。 -->

- [x] 218. https://github.com/hyperionaidev/smolmaxxing/
  <!-- 超小型・低スペック機（TV Box・旧スマホ）で16B〜80BのLLMを動かす最適化フレームワークSmolmaxxing。Signals: ax92 -->
- [x] 020. https://antonau.tech/posts/2026/11/agents-microvm-firecracker/
  <!-- GoogleのAIエージェント用サンドボックスをFirecrackerで再現し25ms起動・3MB/インスタンスを実証した技術検証。Signals: ax90 -->
- [ ] 026. https://respawnfirst.com/linux-script-emails-sam-altman-unused-ram-ram-altman/
  <!-- 空きRAM量を毎日Sam Altmanにメール報告する皮肉Bashスクリプト「Ram Altman」。（奇抜/批評）Signals: ax90 -->
- [x] 086. https://claude.ai/artifact/5rGviSNATjR6aF6A54XALj
  <!-- 映画好きの「うるさいおじさん」から返信が来るClaude Artifacts製の遊び心アプリ。（※STEP_02でuser KEEP・判断保留＝奇抜/周縁、annexかomitか要判断）Signals: ax90 -->
- [ ] 206. https://www.johnnunemaker.com/dont-make-a-human-do-what-ai-is-amazing-at/
  <!-- Nunebotで依存更新・バグ修正等の退屈作業を自動化し短期で250 PRを処理した実践記録。Signals: ax85 -->
- [x] 176. https://1password.com/blog/1password-for-agents-security-privacy
  <!-- 生パスワードを渡さずエージェントに操作委任する「1Password for Agents」のセキュリティ設計。（テーマ5隣接（T5 244 Proverは別製品））Signals: ax75 -->
- [ ] 161. https://scrapbox.io/funwarioisii/%E7%90%86%E8%A7%A3%E3%81%8C%E3%83%9C%E3%83%88%E3%83%AB%E3%83%8D%E3%83%83%E3%82%AF%E3%81%AA%E3%82%89%E7%90%86%E8%A7%A3%E3%82%92%E9%AB%98%E9%80%9F%E5%8C%96%E3%81%99%E3%82%8C%E3%81%B0%E3%81%84%E3%81%84%E3%81%98%E3%82%83%E3%81%AA%E3%81%84
  <!-- 真のボトルネック「人間の理解」をMCPと動画生成で高速化するProfessoreの提案。Signals: ax70 -->
- [x] 098. https://zenn.dev/hoshinotsuyoshi/articles/c994c29833f36c
  <!-- Herdr.app/hcでClaude Codeを司令塔に複数エージェントを認知負荷低く統括する運用解説。Signals: ax70 -->
- [x] 090. https://note.com/ochyai/n/n7a1dbd68c8fa
  <!-- 落合陽一が超知能による人類滅亡シナリオと「道具の自然化」を自己批判的に再考する論考。Signals: ax70 -->
- [ ] 237. https://www.figma.com/blog/ai-role-in-the-creative-process/
  <!-- AI統合時に自動化すべき「労働」と守るべき「思考の摩擦」を区別し創造性の本質を定義。（テーマ6/8隣接）Signals: ax65 -->
- [x] 230. https://www.mitsue.co.jp/knowledge/blog/x-tech/202611/12_1352.html
  <!-- OpenAI Agents SDK＋Playwrightで実行ツールを厳格制限した安全な自作ブラウザエージェント構築。Signals: ax65 -->
- [ ] 227. https://techblog.lycorp.co.jp/ja/20261111b
  <!-- PR単位のログ集計と定型作業のモデル最適化でAIエージェント導入のROIを正確に評価する戦略。Signals: ax65 -->
- [x] 207. https://openai.com/ja-JP/index/ai-effect-on-freelance-work/
  <!-- OpenAI×Upwork研究。AIがフリーランス市場で単純代替でなく高単価案件とスキル再編を促す実態。Signals: ax65 -->
- [ ] 205. https://haydenbleasel.com/taking-away
  <!-- 開発コスト激減後、プロダクト開発は「足し算」から生成物の何を削るかの「引き算」へ。Signals: ax65 -->
- [ ] 185. https://www.oreilly.com/radar/podcast/generative-ai-in-the-real-world-memory-for-personal-ai-with-duncan-davidson/
  <!-- AIツール間で断片化した「記憶」を統合する、ユーザー制御可能なポータブルメモリの重要性。（テーマ7（Muse/パーソナル）隣接）Signals: ax65 -->
- [ ] 061. https://zenn.dev/koheidisney/articles/729394f8be42c5
  <!-- 旧世代GPU（GTX 1080）で4〜9BのローカルLLMを動かし知識量・思考力を検証した実験。Signals: ax65 -->
- [ ] 029. https://matteoraso.github.io/im-not-convinced-the-ai-bubble-exists.html
  <!-- 投資規模・参入障壁欠如のバブル懸念に、収益成長・健全財務を根拠に反論する「崩壊しない」論。（グループ2（市場）への反対論＝ディベート材料）Signals: ax65 -->
- [ ] 221. https://roll.bybacon.com/2026/10/14/vibes-dont-maintain.html
  <!-- AIで動くプロトタイプは一瞬だが、設計意図を欠く「雰囲気コード」は運用・保守に耐えないという批評。Signals: ax60 -->
- [x] 075. https://openai.com/ja-JP/index/setting-new-standard-responsible-ai-infrastructure/
  <!-- OpenAIが地域対話・エネルギー費自己負担・環境対策を柱とするAIインフラ指針「地域社会との協約」を発表。Signals: ax60 -->
