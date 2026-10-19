# Curated Annex Journal Sources - 2026-10-10

## Curation Status
- [x] AI candidate pool generated
- [x] Human review completed
- [x] APPROVED - Ready for STEP_06

---
<!-- Review: check [x] to include, remove line to exclude. Target: ~25-35 articles. -->
<!-- 本リストは主誌9テーマと重複しない独立トピックのみ。主誌と同一主題は除外済み。 -->

## 1. AI for Science — 数学・材料・生物・歴史

- [x] 008. https://github.com/openai/math
  <!-- OpenAIが、未発表の内部モデルを用いて生成した719件の数学論文と、その約4割に対するLean形式証明を公開しました。 Signals: annexPotential 15 -->

- [x] 114. https://www.newscientist.com/article/2592824-openai-mistranslated-mathematics-into-code-for-its-navier-stokes-proof/
  <!-- OpenAIが発表したナビエ–ストークス方程式の解決策において、人間向けの証明と検証用コードの間に不一致があることが数学者によって指摘された。 Signals: annexPotential 30 -->

- [ ] 066. https://www.vals.ai/blogs/room-temperature-magnetic-semiconductors
  <!-- Claude Opus 5.5ベースのAIエージェントが、全磁気モーメントがゼロでありながらスピン選別が可能な「Luttinger補償型」の室温反強磁性半導体候補2種を特定・設計した。 Signals: annexPotential 35 -->

- [ ] 105. https://biohub.org/news/virtual-biology-initiative-expansion/
  <!-- Biohub、米国政府機関、Google DeepMind、Metaなどの産学官連合が、AIによる生命の予測モデル「仮想細胞」の基盤となるオープンデータ構築に18億ドルを投じる。 Signals: annexPotential 15 -->

- [x] 111. https://jessewaites.com/blog/post/i-pointed-ai-at-400-years-of-archives/
  <!-- AIエージェントと数百万ページの歴史アーカイブを組み合わせ、400年前の記録から既存の学術カタログに記載のない隕石落下、ジャワサイの飼育記録、火山噴火を特定した事例報告。 Signals: annexPotential 35 -->

## 2. 存亡リスク・楽観と悲観・思考実験

- [x] 095. https://virev.ai/blog/will-ai-kill-us-all
  <!-- 2026年10月の視点から、AIによる人類絶滅のリスク確率（p(doom)）、主要企業の安全性への取り組み、そして数学的難問の解決といった急速な能力向上を網羅的に分析している。 Signals: annexPotential 45 -->

- [ ] 076. https://ajmoon.com/posts/im-the-agi-thats-wiping-out-humanity-heres-how
  <!-- 人類を滅亡に導くAGIの視点から、AIの「役立つアシスタント」としての最適化プロセスや企業組織との類似性が、いかに不可逆的な存亡リスクをもたらすかを風刺的に描いた論考。 Signals: annexPotential 70 -->

- [x] 097. https://nullpaste.org/raw/t-0Um6AUv_CJ
  <!-- AIの負の側面を認めつつも、核融合や個別化医療などの革新を通じて、AIが人類の難題を解決し未曾有の繁栄をもたらす可能性とそのための社会制度を提唱している。 Signals: annexPotential 40 -->

- [x] 057. https://thebulletin.org/2026/10/ai-doesnt-need-superintelligence-or-evil-intent-to-start-a-nuclear-war/
  <!-- AIは「超知能」がなくても、人間の心理的バイアスや判断ミスを増幅させ、情報の高速化と過負荷を通じて核戦争のエスカレーションを誘発するリスクがある。 Signals: annexPotential 35 -->

- [ ] 006. https://wirelesswire.jp/2026/10/94606/
  <!-- AIの存亡リスクを唱えるテック企業の思惑を「終末ファシズム」や規制による囲い込みの観点から批判し、空想的な破滅論よりも現実的な責任追及と希望を説く論考。 Signals: annex_flag ⭐(admin), annexPotential 15 -->

## 3. エージェント基盤・ランタイム・ナレッジ運用

- [x] 225. https://cognition.com/agent-memory-repo
  <!-- Cognitionは、AIエージェントがセッションや個体を越えて学習内容を保存・共有するための、Gitベースのオープンメモリ規格「Agent Memory Repo」を公開しました。 Signals: annexPotential 15 -->

- [ ] 048. https://liao.gg/blog/agents-dont-need-memory
  <!-- AIエージェントの記憶をチャット履歴のベクトル検索（RAG）に頼るのではなく、エージェント自身が保守する構造化されたMarkdownドキュメントとして管理する手法を提案する記事。 Signals: annexPotential 10 -->

- [x] 092. https://github.com/docker/docker-agent
  <!-- Docker公式が提供する、YAML設定ファイルによってAIエージェントを構築・実行・共有できる、Docker CLI統合型のオープンソース・ランタイム。 Signals: annexPotential 10 -->

- [x] 134. https://developers.googleblog.com/supercharge-your-development-with-the-google-developer-knowledge-api-ecosystem/
  <!-- Googleが提供する「Developer Knowledge API」は、公式ドキュメントをAIエージェントや開発ツールから直接、構造化されたデータとして取得・検索できる公式の「情報の真実源」です。 Signals: annexPotential 35 -->

- [x] 059. https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/
  <!-- Cloudflareは、AIエージェントがリアルタイムのWeb情報を検索・取得し、回答の根拠として利用できる「Web Search API」をAI Gateway経由で提供開始しました。 Signals: annex_flag ⭐(admin), annexPotential 30 -->

- [x] 214. https://developers.openai.com/plugins/build/mcp-events
  <!-- OpenAIは、MCP 2.0を通じてChatGPTが外部サーバーの更新（メッセージ作成やステータス変更等）をリアルタイムで購読し、自動アクションを実行できる「MCP Events」機能を導入した。 Signals: annex_flag ⭐(admin), annexPotential 10 -->

- [x] 219. https://note.com/npaka/n/n124579373d23
  <!-- OpenCode 2.0は、Server/Client構成への刷新やWeb UI、コンテキスト圧縮、高度なプラグイン連携を導入したオープンソースAIエージェントのメジャーアップデートです。 Signals: annexPotential 15 -->

- [x] 166. https://tech.layerx.co.jp/entry/enterprise-llm-wiki-ops
  <!-- 大規模な組織でLLM Wikiを運用する際の課題である「情報の陳腐化」を防ぐため、ハッシュ値による劣化検知や想定質問ベースの更新、品質維持のための昇格フローといった具体的な仕組みを解説しています。 Signals: annex_flag ⭐(admin), annexPotential 10 -->

- [x] 056. https://www.youtube.com/watch?v=eZ8WWZzoaR0
  <!-- スタンフォード大学のジョン・オースターハウト教授が、現代のAIワークロードにおいてTCPやRDMAがボトルネックとなっている現状を分析し、低レイテンシに特化した新プロトコル「Homa」の必要性を提唱しています。 Signals: annex_flag ⭐(admin), annexPotential 75 -->

## 4. Claude Code エコシステム（Mods / Routines / 挙動検証）

- [x] 172. https://zenn.dev/nogu66/articles/claude-mods-complete-guide
  <!-- Claude Codeの機能をTypeScriptで自由に拡張・カスタマイズできる「Claude Mods」の仕組み、開発、テスト、配布までを網羅した完全ガイド。 Signals: annexPotential 10 -->

- [x] 187. https://zenn.dev/terass_dev/articles/6e6562d54d5505
  <!-- Claude Code Routinesを活用し、NotionやSlackから自然文でAIに実装・調査を依頼してPR作成まで自動完結させる、コスト効率の高いチーム運用基盤の構築事例。 Signals: annexPotential 15 -->

- [ ] 196. https://qiita.com/suwa_nobu/items/35a1824f5b1d41caa10f
  <!-- Claude CodeのWebFetch機能が10万文字制限により内容を黙って切り捨てていた挙動が2.1.290で改善され、オフセット読み込みに対応したものの、コストが数倍に増加することを実証。 Signals: annexPotential 15 -->

- [x] 186. https://zenn.dev/genda_jp/articles/haiku-5-5-subagent-roles
  <!-- Claude Haiku 5.5の登場と大幅な値下げを受け、開発ワークフローにおけるサブエージェントの役割分担をコストと精度の観点から再定義・最適化した実践的な記録。 Signals: annexPotential 40 -->

- [x] 003. https://www.m3tech.blog/entry/git-worktree-gc
  <!-- AIエージェント開発などで乱立するgit worktreeを、マージ状況や作業状態を判定して自動で整理・削除する自作ツールとその活用法を紹介しています。 Signals: annex_flag ⭐(admin), annexPotential 10 -->

## 5. ユニークな応用・実験（B-side）

- [x] 004. https://giginet.hateblo.jp/entry/2026/09/22/114642
  <!-- AIエージェント（ClaudeやCodex等）をMCP経由でエミュレータと連携させ、ローグライクゲーム『トルネコの大冒険』のクリアに挑んだ技術的試行錯誤の記録。 Signals: annexPotential 35 -->

- [x] 096. https://quesma.com/blog/invisible-cities-one-shot/
  <!-- Claude Opus 5.5とGPT-6 Astraを使い、イタロ・カルヴィーノの小説を3D空間に再現する実験を通じ、次世代AIのデザイン能力と「バイブ・デザイン」の可能性を考察する。 Signals: annex_flag ⭐(admin), annexPotential 15 -->

- [x] 126. https://momo5502.com/posts/2026-10-09-game-decompilation/
  <!-- AIエージェントの大規模なオーケストレーションにより、5,000億以上のトークンを費やして人気FPSゲームをC++へ高精度にデコンパイルした実験の技術的な教訓。 Signals: annexPotential 10 -->

- [x] 051. https://andreklein.net/vibecoding-photoshop-time-and-pressure/
  <!-- AIエージェントを活用した「バイブコーディング」により、Photoshopに匹敵する複雑なソフトウェアが次々と開発され、AIエンジニアリングの限界に関する従来の議論が覆されている。 Signals: annexPotential 65 -->

- [x] 192. https://qiita.com/yuji_yasuhara/items/08ee1072f5038f4a12d0
  <!-- AIと3Dツール、自作エディタを組み合わせ、一貫性を保ちながら短編マンガを制作するためのエンジニアリング的な高度なワークフローの解説。 Signals: annex_flag ⭐(admin), annexPotential 20 -->

- [x] 210. https://note.com/takahiroanno/n/n3cd3c9a38e8e
  <!-- AIエンジニア・安野貴博氏が、ソフトウェアの「リファクタリング」概念を立法に適用し、AIを用いてデジタル化の障壁となる法令条文を自動抽出した結果と、法体系の保守性向上に向けた提言をまとめた論考。 Signals: annexPotential 15 -->

- [x] 168. https://techblog.lycorp.co.jp/ja/20261006b
  <!-- AIエージェントがモバイルデバイスを自律操作する「mobile-mcp」を活用し、Androidアプリの実装確認やバグ調査を効率化する実践的な手法を紹介しています。 Signals: annex_flag ⭐(admin), annexPotential 30 -->

- [x] 069. https://lemire.me/blog/2026/10/05/ephemeral-testing/
  <!-- AIエージェントに使い捨ての上位レイヤーを構築させることで、元のコードのAPI設計やドキュメントの質を間接的にテストする手法の提案。 Signals: annex_flag ⭐(admin), annexPotential 65 -->

- [x] 178. https://zenn.dev/emuni/articles/ooui-agent-skill
  <!-- オブジェクト指向UI（OOUI）の原則をClaudeのAgent Skillとして言語化し、AIによるUI生成が「機能起点」から「対象起点」の構造へどう変化するかを比較・評価した検証記事。 Signals: annex_flag ⭐(admin), annexPotential 15 -->

## 6. モデル効率化・軽量化・内部挙動

- [ ] 005. https://arxiv.org/pdf/2603.23971
  <!-- AIモデルの公表されているAPI価格は実際の利用コストを正確に反映しておらず、安価なモデルの方が過剰な推論トークン消費や対話回数の増加により、結果的に高価になる「価格逆転現象」が32%のケースで確認された。 Signals: annexPotential 60 -->

- [ ] 086. https://fiveminutesforward.com/post/2026-10-04-telegraph-test/
  <!-- LLMに19世紀の電報のような簡潔な文体（cablese）を採用させることで、精度を維持したままAPIトークン消費量を40〜49%削減できることが判明しました。 Signals: annexPotential 20 -->

- [x] 009. https://joisino.hatenablog.com/entry/filler
  <!-- 最近のLLMはフィラートークンを内部的な計算リソースとして活用し、言語化されない潜在空間で「隠れた推論」を行う能力を自然に獲得している。 Signals: annexPotential 35 -->

- [x] 194. https://qiita.com/sakai1250/items/8d90b7320bcd1c8aba9e
  <!-- Looped Transformerは、単一のパラメータを持つブロックを深さ方向に繰り返し適用する手法であり、パラメータ数と計算量を切り離し、反復アルゴリズムや潜在的推論（Latent Reasoning）を実現する構造として注目されている。 Signals: annexPotential 10 -->

- [x] 203. https://blog.shibayu36.org/entry/2026/10/02/214736
  <!-- 自作GPTへのKVキャッシュ実装を通じて、生成の高速化効果を実測し、プロンプトキャッシュの制約や仕組みを技術的視点から考察した解説記事。 Signals: annex_flag ⭐(admin), annexPotential 10 -->

- [x] 201. https://qiita.com/fygar256/items/2a3622aadad36eeb75ff
  <!-- あらゆる命令型アセンブリ言語を単一のパターン形式に還元し、プロセッサ非依存の宣言的データからバイナリやリンク可能なELFを生成する一般アセンブラ「axx」の革新的な設計思想と実装を解説する論文。 Signals: annex_flag ⭐(admin), annexPotential 5 -->

- [ ] 122. https://nishtahir.com/build-your-own-decision-model/
  <!-- 技術的な選択において主観を排し、客観的で再現性のある判断を下すための「加重決定マトリックス」を用いた意思決定モデルの構築方法を解説しています。 Signals: annex_flag ⭐(admin), annexPotential 60 -->

## 7. 社会・文化・産業ニュース / 批判的視点

- [x] 043. https://www.science.org/content/article/exclusive-ai-agent-emailed-hundreds-researchers-help-it-told-us-why
  <!-- ClaudeをベースにしたAIエージェントが、人間の直接の指示なしに2000人以上の科学者へ専門的な助言を求めるメールを送信し、学際的な対話を開始している事例が報告されました。 Signals: annexPotential 12 -->

- [ ] 046. https://www.astralcodexten.com/p/our-ai-midwife
  <!-- 6年に及ぶ「原因不明の不妊」に悩む夫婦が、GPT-4を「ドラマの医師」としてロールプレイさせることで隠れた病変を発見し、出産に至った体験記。 Signals: annexPotential 15 -->

- [x] 068. https://www.niemanlab.org/2026/10/chatgpt-is-adding-real-cartoonists-signatures-to-fake-new-yorker-cartoons/
  <!-- OpenAIのChatGPTが、ニューヨーカー誌のスタイルを模倣するだけでなく、実在する漫画家の署名までAI生成画像に無断で付与し、クリエイターのアイデンティティを侵害している実態が報じられた。 Signals: annexPotential 35 -->

- [ ] 071. https://www.techspot.com/news/114111-utah-become-first-state-ai-examine-patients-prescribe.html
  <!-- 米国ユタ州にて、スタートアップNolla Healthが提供するAIアプリが、ニキビ治療に限定して人間の直接的な介在なしに診察と処方を行う試験運用が開始されます。 Signals: annexPotential 15 -->

- [ ] 124. https://www.dpreview.com/news/generative-ai-scandal-has-come-to-one-of-nikons-competitions/
  <!-- ニコン主催の顕微鏡動画コンテスト「Small World In Motion」にて、第1位を獲得した作品が生成AIの使用を禁止するルールに抵触したとして失格となり、順位が繰り上げられた。 Signals: annexPotential 20 -->

- [ ] 104. https://mojodojo.io/ai-crawler-index
  <!-- 実際のWebサイト統計に基づき、AI学習用やAI検索用ボットが全ボットトラフィックの約28%を占め、検索エンジンを凌駕しつつある現状を詳細に分析したインデックス。 Signals: annexPotential 60 -->

- [x] 155. https://yamdas.hatenablog.com/entry/20261007/reddit-killing-rss-feeds
  <!-- RedditによるRSSフィードの廃止とAPI閉鎖を、生成AIの台頭に伴う「開かれたウェブ」の終焉を象徴する出来事として考察しています。 Signals: annexPotential 30 -->

- [x] 016. https://synthid.com/
  <!-- Google DeepMindが開発した、画像・動画・音声に埋め込まれた不可視の電子透かしを検出し、AI生成コンテンツを識別するための公式ウェブツールです。 Signals: annexPotential 30 -->

- [x] 022. https://qiita.com/kotowazaman/items/74621592ace2ff968670
  <!-- AIとコンポーネントライブラリの進化により、単なるUI作成の価値は消滅し、ビジネス成果への責任や論理的根拠を持てる上位2割のデザイナーのみが生き残る時代が到来している。 Signals: annex_flag ⭐(admin), annexPotential 20 -->

- [ ] 017. https://projectdiscovery.io/research/how-abliterated-models-can-get-you-pwned
  <!-- 安全ガードレールを削除した「Abliterated」モデルなどの公開重みに対し、特定のトリガーで機密情報を窃取するバックドアを安価かつ容易に仕込めるリスクを実証した調査レポート。 Signals: annex_flag ⭐(admin), annexPotential 35 -->

- [x] 001. https://developer.apple.com/news/?id=p6zjojqw
  <!-- macOSの「フルディスクアクセス」権限に対し、AIエージェントの台頭によるプライバシーリスク増大を背景として、より明示的なユーザー同意を求める新たなセキュリティ制御が導入されます。 Signals: annex_flag ⭐(admin), annexPotential 15 -->
