# Curated Annex Journal Sources - 2026-09-26

## Curation Status
- [x] AI candidate pool generated
- [ ] Human review completed
- [ ] APPROVED - Ready for STEP_06

---
<!-- Review: check [x] to include, delete a line to exclude. Target ~30-40 final. -->
<!-- Sections are the AI grouping suggestion; curator's final sections go in curated_annex_selected.md after approval. -->
<!-- Principle: pieces here are thematically distinct / niche / contrarian vs the 9 main themes. -->
<!-- Jev-APPLICATION overflow that repeats main Themes 1-2 (~30 articles) routes to OMIT, not annex; only distinctive Jev meta/skeptic analyses kept. -->

## 1. モデルとインフラの内側

- [ ] 072. https://www.oreilly.com/radar/the-post-training-process-openai-used-for-chatgpt/
  <!-- ChatGPTのSFT→報酬モデル→RLHFの3段階を技術的に解説。学習手法の教科書的整理。 Signals: criteria-only (scrutinize) -->
- [ ] 001. https://z.ai/blog/glm-built-its-inference-infrastructure
  <!-- GLM-5.3の Infra Agent が推論基盤を自律最適化、2週間で3倍。再帰的自己改善の初期実例。 Signals: criteria-only (scrutinize) -->
- [ ] 128. https://www.interconnects.ai/p/the-current-balance-of-power-in-open
  <!-- 中国オープンモデルがDL数・学術引用で米国を逆転。米中勢力均衡の分析。 Signals: criteria-only (scrutinize) -->
- [ ] 019. https://qwen.ai/blog?id=qwen-image-2.1
  <!-- Qwen-Image-2.1、7Bで透過(RGBA)生成と統合編集。軽量画像生成モデル。 Signals: criteria-only (scrutinize) -->
- [ ] 169. https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-text-to-speech/
  <!-- Gemini 3.8 TTS、自然言語でカスタムボイス生成と行単位の演出制御。 Signals: criteria-only (scrutinize) -->
- [ ] 252. https://huggingface.co/apple/LensVLM-9B
  <!-- Apple LensVLM-9B、圧縮画像から関連箇所のみ選択的に高解像展開。長文書処理の効率化。 Signals: criteria-only (scrutinize) -->

## 2. 開発の道具と手法

- [ ] 006. https://addyosmani.com/blog/audit-your-agent-files/
  <!-- Addy Osmani：CLAUDE.md等の設定ファイルの劣化を定期監査し削ぎ落とせ。 Signals: criteria-only (scrutinize) -->
- [ ] 050. https://zenn.dev/nogu66/articles/claude-code-function-hooks-claude-mods
  <!-- Claude Mods (Function Hooks) でClaude CodeをTypeScriptで深くカスタマイズ。 Signals: annex_flag ⭐ -->
- [ ] 209. https://www.tonyward.dev/articles/code-as-the-source-of-truth
  <!-- コードを唯一の真実のソースに——デザイン×開発の融合(デザインエンジニア)。 Signals: annex_flag ⭐ -->
- [ ] 200. https://portablecode.info/2026/09/23/herdr-annotate-ai-review/
  <!-- Herdr AnnotateでAIコーディングレビューのフィードバックループを効率化。 Signals: annex_flag ⭐ -->
- [ ] 155. https://github.blog/engineering/user-experience/rendering-huge-pull-requests-in-the-github-copilot-app/
  <!-- GitHub Copilotアプリで100万行超PRを高速描画する二重ジオメトリ仮想化。 Signals: annex_flag ⭐ -->
- [ ] 100. https://blog.cloudflare.com/worker-previews/
  <!-- Cloudflare Worker Previews：ブランチ毎に本番同様の隔離環境(ステート含む)。 Signals: annex_flag ⭐ -->
- [ ] 104. https://socket.dev/blog/oj-vite-rust
  <!-- LovableがViteをRust再実装(OJ)。AIがOSSフォークのコストを下げる時代。 Signals: annex_flag ⭐ -->
- [ ] 150. https://evilmartians.com/chronicles/ai-makes-design-system-guardrails-mandatory-this-framework-delivers-them
  <!-- Evil Martians：AI時代に必須のデザインシステム・ガードレール実装フレームワーク。 Signals: annex_flag ⭐ -->
- [ ] 206. https://github.blog/security/application-security/ai-powered-fuzzing-with-the-github-security-lab-taskflow-agent/
  <!-- GitHub Security LabのAI駆動ファジング Taskflow Agent。 Signals: annex_flag ⭐ -->

## 3. MCP・プロトコルの論争

- [ ] 154. https://www.oreilly.com/radar/mcp-is-not-just-another-api-standard/
  <!-- MCPは単なるAPI標準ではない——記述がインターフェースになる新パラダイム。 Signals: criteria-only (scrutinize) -->
- [ ] 022. https://maharship.com/blog/why-mcp-was-always-a-bad-idea/
  <!-- MCPは最初から悪いアイデアだった、とHTTP/CLI回帰を説く対の論(contrarian)。 Signals: criteria-only (scrutinize) -->
- [ ] 086. https://azukiazusa.dev/blog/mcp-skills-extension/
  <!-- MCPサーバーからAgent Skillsを配布するSkills Extension (SEP-2640)。 Signals: criteria-only (scrutinize) -->
- [ ] 031. https://qiita.com/suwa_nobu/items/c795cf89d0fd4091c9cb
  <!-- Claude CodeのAGENTS.mdは初回セッションで読まれない——検証記事。 Signals: annex_flag ⭐ -->

## 4. Jevの深掘り・懐疑(main外)

- [ ] 192. https://blog.monochromegane.com/blog/2026/09/21/jev/
  <!-- Jevの実現方式をDirect Logit型/Decision Head型に分類・再現。 Signals: annex_flag ⭐ -->
- [ ] 059. https://note.com/kantahayashiai/n/n4c54eed30787
  <!-- Jevはサイコロを振らない——較正の自信過剰を実験で指摘(懐疑)。 Signals: annex_flag ⭐ -->
- [ ] 092. https://zenn.dev/cybernetics/articles/71ea975d935414
  <!-- Jevを分類器でなく確率モデルの部品(条件付き確率)として捉え直す試論。 Signals: annex_flag ⭐ -->
- [ ] 042. https://zenn.dev/hakotech/articles/5c2fe2eb8a6051
  <!-- Gemma 3でJev風判断モデルを3方式比較(ローカル再現)。 Signals: annex_flag ⭐ -->
- [ ] 061. https://anond.hatelabo.jp/20260920135749
  <!-- Jevの強みは技術革新でなく即座に使えることだとする批判的論評(contrarian)。 Signals: criteria-only (scrutinize) -->
- [ ] 129. https://qiita.com/yukihirop/items/e0d8ffb121c1a753075a
  <!-- 自然言語からCLIコマンドを組み立てる jany(Jev活用のハイブリッド解析)。 Signals: annex_flag ⭐ -->

## 5. 安全・セキュリティ(main外)

- [ ] 117. https://arstechnica.com/security/2026/09/muse-metas-extraordinarily-privileged-ai-assistant-has-a-serious-0-day/
  <!-- Meta Muse に重大0-day、macOS特権とWhatsApp/カメラが奪取される恐れ。 Signals: criteria-only (scrutinize) -->
- [ ] 222. https://blog.trailofbits.com/2026/09/18/auditing-in-the-age-of-good-enough-ai/
  <!-- Trail of Bits：AIで監査ツールを自作しMiden zkVMの高深刻度脆弱性を特定。 Signals: criteria-only (scrutinize) -->
- [ ] 156. https://yamdas.hatenablog.com/entry/20260924/tada-tadashi
  <!-- AIで防御側が勝てる時代が来たのか——Defense Factory論の紹介。 Signals: criteria-only (scrutinize) -->
- [ ] 032. https://qiita.com/kf_webdev/items/cbd1d7bb724676a3b686
  <!-- 生成AIセキュリティ：間接プロンプトインジェクションとRAG権限・多層防御。 Signals: criteria-only (scrutinize) -->
- [ ] 171. https://normanponte.io/19df691f
  <!-- クラウドエージェントは必然的な AIの監獄 へ収束する(隔離アーキ論)。 Signals: criteria-only (scrutinize) -->

## 6. 規制・労働・社会

- [ ] 107. https://www.anthropic.com/institute/econ-scenarios
  <!-- Anthropic：2030年の経済影響を3シナリオで試算するモデルとシミュレータ。 Signals: annex_flag ⭐ -->
- [ ] 210. https://www.kenklippenstein.com/p/feds-think-ai-critics-are-foreign
  <!-- 米政府がAI批判派を 外国の代理人 として刑事訴追の標的に。 Signals: criteria-only (scrutinize) -->
- [ ] 075. https://www.bbc.com/news/articles/cm5y7qj54klpo
  <!-- AI開発者の多くは 人類滅亡 説に冷笑的——BBC取材。 Signals: criteria-only (scrutinize) -->
- [ ] 161. https://www.technologyreview.com/2026/09/22/1144910/the-download-dont-believe-ai-hype/
  <!-- AIの最新ブレイクスルーと懸念はハイプの可能性(MIT TR/Gebru・Bender)。 Signals: criteria-only (scrutinize) -->
- [ ] 220. https://openclassactions.com/lawsuits/privacy/openai-chatgpt-human-review-project-lily-class-action-lawsuit.php
  <!-- ChatGPT Project Lily 人間査読を巡る集団訴訟。 Signals: criteria-only (scrutinize) -->
- [ ] 218. https://www.tomshardware.com/tech-industry/artificial-intelligence/japanese-used-bookstores-see-5x-sales-surge-as-books-are-being-bought-by-the-ton-one-50-ton-order-sent-to-the-us-for-ai-scanning-and-destruction-multitude-of-suspicious-bulk-buys-thought-to-end-up-in-foreign-ai-scan-and-shred-facilities
  <!-- 日本の古書店が トン単位 でAI学習用に爆買い・裁断廃棄。 Signals: criteria-only (scrutinize) -->
- [ ] 176. https://blog.arxiv.org/2026/09/23/arxiv-receives-multiyear-investment/
  <!-- arXivが独立非営利へ移行、計1,720万ドルを調達。 Signals: criteria-only (scrutinize) -->

## 7. 知性・意識・人間をめぐる問い

- [ ] 145. https://que.dailyshincho.jp/node/20880/
  <!-- テッド・チャン AIは意識を持ち得ない——身体性・代謝・時間の欠如。 Signals: annex_flag ⭐ -->
- [ ] 254. https://news.jp/i/1468434149571740088
  <!-- 脳科学者・渡辺正峰 デジタル不老不死 とAIに意志は宿るか。 Signals: criteria-only (scrutinize) -->
- [ ] 245. https://huyukiitoichi.hatenadiary.jp/entry/2026/09/24/080000
  <!-- THE LINE──AIが〈ひと〉になるとき、人格の境界を法学から。 Signals: criteria-only (scrutinize) -->
- [ ] 108. https://naturalgeneralintelligence.ai/
  <!-- Natural General Intelligence：地球システムを学ぶネイチャーモデルの提唱。 Signals: annex_flag ⭐ -->
- [ ] 080. https://pluralistic.net/2026/09/21/sunsetting/
  <!-- ドクトロウ クロードの錯覚——AIに意図を見出す人間側の幻覚(AI無神論)。 Signals: criteria-only (scrutinize) -->
- [ ] 174. https://madradavid.com/claudes-load-bearing-seams/
  <!-- Claudeの耐力継ぎ目——推論の構造的制約を巡るメタ考察。 Signals: criteria-only (scrutinize) -->

## 8. 創作・文化・産業・その他

- [ ] 011. https://john.hartnup.uk/2026/06/07/ai-event-posters.html
  <!-- AI生成ポスターを 安っぽさ から脱却させるスタイル指定術。 Signals: annex_flag ⭐ -->
- [ ] 253. https://anond.hatelabo.jp/20260829104434
  <!-- 一次創作同人作家の生成AI活用術と 道具 としての捉え方。 Signals: criteria-only (scrutinize) -->
- [ ] 225. https://resobscura.substack.com/p/ai-labs-need-to-start-funding-historical
  <!-- AIラボは歴史研究に資金提供すべき——暗号解読・文献特定の成果。 Signals: annex_flag ⭐ -->
- [ ] 266. https://www.itmedia.co.jp/news/article/2609/25/2000001728/
  <!-- Google Project Suncatcher 宇宙AIデータセンターの試作衛星打ち上げへ。 Signals: criteria-only (scrutinize) -->
- [ ] 170. https://www.anthropic.com/news/claude-discovers-novel-enzyme-system
  <!-- ClaudeがCRISPR様の反復配列を持つ新規酵素システムを自律発見。 Signals: criteria-only (scrutinize) -->
- [ ] 195. https://geta.team/
  <!-- Geta.Team：既存ツール連携で自律的に働く AI従業員 プラットフォーム。 Signals: annex_flag ⭐ -->
- [ ] 226. https://launchvideo.io/
  <!-- LaunchVideo：URLからOpus 5.5が動画をコード生成しMP4出力。 Signals: annex_flag ⭐ -->
- [ ] 236. https://zenn.dev/pnd/articles/claude-castles
  <!-- Opus 5.5の3Dモデリング能力で歴史考証つきの城を構築(モデル能力デモ)。 Signals: annex_flag ⭐ -->

