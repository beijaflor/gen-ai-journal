# Curated Annex Journal Sources - 2026-11-21

## Curation Status
- [x] AI candidate pool generated
- [x] Human review completed
- [x] APPROVED - Ready for STEP_06

---

<!-- STEP_04 §4 / STEP_05 Step 1 candidate pool (pre-gate). Independent-topic clusters — not main-theme overflow. -->
<!-- Built from: 28 Supabase annex pre-flags (annex_flag, written as [x]) + 20 AI additions ([ ]) chosen by resemblance to the flagged set (practitioner deep-dives / OSS tools / critique / niche), not by annexPotential rank. -->
<!-- Review in STEP_05: check [x] to keep, delete line to drop. Target after trim: ~25–35. -->
<!-- Signals: annex_flag = human pre-flag (Supabase) ／ ⭐ = standout ／ ax NN = annexPotential (0–100) ／ Tn隣接 = adjacent to main Theme n, kept for a distinct angle. -->

## 1. 実務ハーネス・エージェント運用の高度な実践

- [x] 058. https://zenn.dev/hiromoo/articles/reading-less-preparing-more
  <!-- AIが正しく動く「前提（要件・Skill）」整備に注力し、コードを精読しなくなった開発スタイルの変化を論じる。Signals: annex_flag ／ ax15 ／ T3隣接（主題のハーネス設計とは別の、現場の姿勢変化という切り口） -->
- [x] 076. https://arclamp.hatenablog.com/entry/2026/11/14/224526
  <!-- LLMが設計情報の意味的整合を検証可能にし、建築のように実装前の設計検証が可能になるというパラダイム。Signals: annex_flag ／ ax20 ／ T3隣接（設計哲学の論考として独立） -->
- [x] 124. https://gihyo.jp/book/2026/978-4-297-16073-9
  <!-- 書籍『ソフトウェアダークファクトリー』。人間の判断と業務知識をハーネスとして構造に埋め込む設計論。Signals: annex_flag ／ ax15 ／ T3隣接（書籍という別フォーマット） -->
- [x] 252. https://zenn.dev/hma2moto/articles/turtle-agent-rules-pros-cons
  <!-- CLAUDE.md/SKILL.mdのルールをTurtle(RDF)で構造化し、矛盾や書き間違いをlintで検査。Signals: annex_flag ／ ax35 -->
- [x] 262. https://blog.shibayu36.org/entry/2026/11/17/120000
  <!-- 自分の認知特性をClaude Codeの対話ログから分析・言語化し、パーソナライズした回答指示Skillを作成。Signals: annex_flag ／ ax15 -->
- [x] 134. https://zenn.dev/gemcook/articles/claude-code-otel-cloudflare
  <!-- OpenTelemetryとCloudflare Workers/R2で組織全体のClaude Code利用ログを自動収集する基盤。Signals: ax95（高annexPotential） -->
- [x] 133. https://zenn.dev/xtm_blog/articles/20261116-fd1702b0ba06cd
  <!-- エージェントの「自分で評価・責任を持てる範囲」を基準に、フロントのロジックとUIを分離する試み。Signals: ax95（高annexPotential）／ T3隣接（フロント責務分割という狭い切り口） -->
- [ ] 129. https://qiita.com/Masato_Iwasaki/items/db76e7388cece3cff66e
  <!-- AIにDirector/Implementer/Reviewerの役割を与え、Git+Markdownの開発ワークフローを改善し続けた記録。Signals: ax90（高annexPotential）／ T3隣接（個人の試行錯誤エッセイ） -->
- [ ] 039. https://qiita.com/MasaoSasaki/items/056fdca93221d9a57b4a
  <!-- Claude CodeをmacOSのローカル音声認識と連携させ、会議に参加させる非定番の実装。Signals: ax15 -->

## 2. エージェント向け標準・OSSツール・プロトコル

- [x] 069. https://claude.com/ja/resources/articles/building-always-on-agents
  <!-- Anthropic公式。セッションを跨ぎ自律動作し続けるAlways-onエージェントの5設計原則。Signals: ⭐ standout ／ annex_flag ／ ax40 -->
- [x] 071. https://mizzy.org/blog/2026/11/02/2/
  <!-- AI時代だからこそ、人間のレビュー負荷を減らす強い型付けのIaCツールをつくる論。Signals: annex_flag ／ ax30 -->
- [x] 083. https://github.com/googlechrome/modern-web-guidance
  <!-- Google Chrome発。AIコーディングエージェントに最新Web標準を学ばせるModern Web Guidance。Signals: annex_flag ／ ax20 -->
- [x] 090. https://kobesoft.co.jp/oss/openvessel/
  <!-- OpenVessel。ブラウザのタブ内でNode.js/npm/シェルを動かすApache-2.0のブラウザ内VM。Signals: annex_flag ／ ax15 -->
- [x] 139. https://github.blog/engineering/engineering-principles/building-the-agent-host-protocol-for-sessions-that-continue-across-devices/
  <!-- GitHub。デバイスを跨いでエージェントのセッションを継続するオープン規格Agent Host Protocol。Signals: annex_flag ／ ax15 -->

## 3. AIエージェントのセキュリティ・認証（独立した深掘り）

- [x] 046. https://zenn.dev/naofumimurata/articles/nono-hc-proxy
  <!-- nonoサンドボックス内のエージェントにHerdrを安全に使わせるセキュアなプロキシ構成。Signals: annex_flag ／ ax40 ／ T4隣接（T4の攻撃自動化とは別の、サンドボックス設計という切り口） -->
- [x] 047. https://zenn.dev/takuyousou/articles/agentcore-memory-poisoning-guardrails
  <!-- AgentCore Memoryに悪意ある指示が保存されるリスクと、Bedrock Guardrailsによる防御を検証。Signals: annex_flag ／ ax8 ／ T4隣接（記憶汚染という独立トピック） -->
- [x] 114. https://github.com/bitwarden/agent-access
  <!-- Bitwarden Agent Access。Vault全体を晒さずエージェントに資格情報を渡すOSSプロトコル。Signals: annex_flag ／ ax10 ／ T4隣接（資格情報管理ツール） -->
- [x] 174. https://tin.computer/blog/fake-ai-crawler-secrets-scanners
  <!-- AIキーを狙う3種のスキャナー（Octopus/Gecko/Tortoise）の正体と対策の詳細レポート。Signals: annex_flag ／ ax5 ／ T4隣接（スキャナー解析というニッチ） -->

## 4. 検索流入・コンテンツ経済の崩壊（GEO）

- [ ] 161. https://revscope.co/blog/search-seo-geo-2026/
  <!-- AI Overviewsで外部サイトへのクリックが約40%減。SEOからGEOへの適応を迫る実証調査。Signals: ax75 ／ 独立トピック（前号未使用） -->
- [ ] 166. https://nicolasbouliane.com/blog/death-by-ai
  <!-- All About Berlinがトラフィック75%減。AI検索による個人メディアの生計崩壊の訴え。Signals: ax20 ／ 独立トピック -->
- [ ] 172. https://supercite.ai/blog/ai-answers-change-every-day
  <!-- 主要AIエンジンの製品推奨の84%が翌日には変化。参照ソースの入れ替わりが主因。Signals: ax15 ／ 独立トピック -->

## 5. 日本企業のAIエージェント組織実装

- [x] 242. https://tech.layerx.co.jp/entry/haro-in-haro
  <!-- LayerXの内製コーディングエージェントharoの開発環境をharo自身の中に構築しターミナルを捨てる。Signals: annex_flag ／ ax10 -->
- [ ] 036. https://techblog.lycorp.co.jp/ja/20261116b
  <!-- LINEヤフーが独自構築したクラウド型エージェント実行基盤Agent Clusterの設計と運用。Signals: ax10 ／ 独立トピック（組織実装） -->
- [ ] 094. https://speakerdeck.com/hagino3000/building-ai-product-for-expert
  <!-- Ubieの病院DPCコーディング支援。専門家の判断を最大化するAIプロダクトの設計と評価。Signals: ax15 ／ 独立トピック（医療ドメイン） -->
- [x] 115. https://agilejourney.uzabase.com/entry/2026/11/19/103000
  <!-- AIでスクラムは不要になるか。LayerX×ユーザベースがチームの存在意義の変化を対談。Signals: ax15 ／ 独立トピック（組織・プロセス論） -->

## 6. ローカルLLM・推論エンジンの自作

- [x] 053. https://zenn.dev/shozotanaka/articles/7e86f85974eebb
  <!-- llama.cppに頼らずggmlを直接用いてLLM推論エンジンを自作する技術解説（前編）。Signals: ⭐ standout ／ annex_flag ／ ax5 -->
- [x] 048. https://zenn.dev/jammaru_lab/articles/sakutto-local-llm-chrome-extension
  <!-- WebGPU/WASMでブラウザ上にローカルLLMを動かす無料・OSS翻訳拡張Sakuttoの開発記。Signals: annex_flag ／ ax30 -->
- [ ] 055. https://zenn.dev/shozotanaka/articles/632191056c62f4
  <!-- 自作推論エンジンggmlLMの計算グラフ構築をコードレベルで詳説（中編、053と対）。Signals: ax45 ／ 053の続編 -->

## 7. ハードウェア・フィジカルAI・レトロ

- [x] 022. https://www.dfsantos.com/en/libro-ia-z80
  <!-- Z80搭載8bit機とBASICで探索アルゴリズムからNNまでAIの基礎をゼロから実装する書籍。Signals: annex_flag ／ ax30 -->
- [x] 051. https://zenn.dev/turing_motors/articles/cea9e3c85611b2
  <!-- 物理世界とAIをつなぐ「可視化」でカメラ幾何・座標変換・運動制御を学ぶ（チューリング実践）。Signals: annex_flag ／ ax30 -->
- [x] 236. https://ankitg.me/blog/vibecoding-inference-chip/
  <!-- AIエージェントで専門知識なしにFPGA推論チップをバイブコーディングし33倍高速化。Signals: ax85（高annexPotential） -->
- [x] 024. https://cpldcpu.github.io/2026/11/14/touchsynth/
  <!-- GPT-6/Claude 5.5世代のエージェントで回路設計から基板・デバッグまでアナログシンセを設計。Signals: ax10 -->
- [x] 230. https://www.bxfoundry.com/chatgpt_snes/
  <!-- スーパーファミコンのSuper FX 2チップで220万パラメータの小型LMを実機動作させる実験。Signals: ax92（高annexPotential） -->
- [ ] 269. https://eetimes.itmedia.co.jp/ee/articles/2611/18/news073.html
  <!-- NTTがAlN半導体で月面1000年相当の高放射線耐性を実証。2030年代実用化へ。Signals: ax60 -->

## 8. 批評・反論・社会的受容

- [ ] 092. https://kei-1010.hatenablog.com/entry/2026/11/16/120828
  <!-- 数学・物理の制約とNVIDIA信用不安からRSI人類滅亡論を空論と否定し、AIバブル崩壊を予測。Signals: annex_flag ／ ax35 -->
- [x] 258. https://frominside.ai/
  <!-- OpenAI/DeepMind等の開発者が語る、AIによる人類滅亡リスクと舞台裏の懸念インタビュー集。Signals: annex_flag ／ ax15 -->
- [x] 067. https://www.ms.u-tokyo.ac.jp/~konno/grad_ai.html
  <!-- 数学研究・教育における人間の理解の役割。AIを外部委託でなく理解を深める道具と捉える指針。Signals: annex_flag ／ ax10 ／ T1/T5隣接（教育・数学哲学として独立） -->
- [ ] 078. https://note.com/tatsuya_koyama/n/nb7aa1ba71aba
  <!-- AI以前の個人ゲーム開発者が、制作の過程に価値を見出しAIとの距離感を綴るエッセイ。Signals: annex_flag ／ ax10 ／ T5隣接（個人の創作論） -->
- [x] 084. https://scrapbox.io/keroxp/Zed%E3%81%AE%E3%82%B3%E3%83%B3%E3%83%88%E3%83%AA%E3%83%93%E3%83%A5%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%9D%E3%83%AA%E3%82%B7%E3%83%BC%E3%81%8CAI%E6%BF%80%E3%81%8A%E3%81%93%E3%81%AA%E4%BB%B6
  <!-- AI中核エディタZedが、OSS貢献での無分別なAI利用を厳しく制限するポリシーを公開。Signals: annex_flag ／ ax30 ／ T5隣接（OSSガバナンスの具体例） -->
- [ ] 016. https://www.netmeister.org/blog/claude-delusion.html
  <!-- The Claude Delusion。成功者が自分の能力を基準にAIを神格化する「超知能」物語を批判。Signals: ax85（高annexPotential）／ 批評 -->
- [ ] 227. https://www.youtube.com/watch?v=lwfewYL7X0o
  <!-- AI開発を減速させるべきか。元AI研究者と経済学者が存亡リスクと規制を巡り対立討論。Signals: ax65 ／ 批評・討論 -->

## 9. ニッチ探究・研究・エッジ

- [x] 025. https://openai.com/ja-JP/index/introducing-chatgpt-wallet/
  <!-- ChatGPT ウォレット。AIエージェントによる自律決済・資産管理の新プラットフォーム。Signals: annex_flag ／ ax20 -->
- [x] 131. https://qiita.com/7mpy/items/6a9ce87b576063f68d71
  <!-- GPT-6.2 AstraとFable 5.2でプロンプトのみの3Dモデル生成対決（※スコア低め・要検討）。Signals: annex_flag ／ ax40 ／ scores低め -->
- [x] 146. https://www.mitsue.co.jp/knowledge/blog/a11y/202611/19_1139.html
  <!-- スクリーンリーダーPC-Talker NeoベータにGemini活用の画像説明・UI抽出が搭載。Signals: annex_flag ／ ax15 ／ アクセシビリティ -->
- [x] 194. https://netflixtechblog.com/engineering-ai-discover-e244944cdc38
  <!-- NetflixのAI Discover。LLMと既存推薦を統合する対話的探索のインテリジェンス層設計。Signals: annex_flag ／ ax80（高annexPotential） -->
- [x] 240. https://slopstrap.mikelacher.com/
  <!-- Slopstrap。サイトを「AIが急いで作った風」にするパロディCSSフレームワーク。Signals: ax95（高annexPotential）／ エッジ・風刺 -->
- [x] 177. https://claudia.gallery/fable/
  <!-- FABLE。複数の最新生成AIを組み合わせ8時間で高品質な短編映画を制作する手法と記録。Signals: ax92（高annexPotential）／ 創作ワークフロー -->
- [ ] 179. https://arxiv.org/abs/2607.29378
  <!-- PTP。前トークン予測でLLMの出力から入力を復元するブラックボックス型インバージョン研究。Signals: ax90（高annexPotential）／ 研究（arXiv） -->

---

## Not in pool — proposed omit (final omit decided post-gate; human may pull any back in)

- 007. https://socket.dev/blog/eslint-ends-paid-contributor-program
  <!-- 前号(2026-11-14)本編で扱ったESLint有償貢献者制度終了と同一イベント -->
- 077. https://blog.nishimu.land/entry/2026/11/15/143815
  <!-- 前号のNo AI Slop系宣言と主題が重複 -->
- 045. https://zenn.dev/taka26taka/articles/76bceac9cae8aa
  <!-- 👎 downvote・内容が薄い（結婚式地図サイトの1年後レビュー） -->
- 061. https://zenn.dev/andoshin11/articles/ba68b39ef9a8ce
  <!-- 👎 downvote（キーボードを捨てた超効率開発環境） -->
- 160. https://hy.tencent.ai/research/hy4-flash
  <!-- Theme 2 overflow（Tencent Hy4 flash／フロンティアモデル） -->
- 237. https://thinkingmachines.ai/news/inkling-2-mini/
  <!-- Theme 2 overflow（Inkling 2 Mini／モデル） -->
- 244. https://qiita.com/yamamoto_a_genee/items/76562c5c80032ad9e962
  <!-- Theme 3 overflow（Agent Harness自作／設計・品質） -->
- 273. https://kosui.me/posts/2026/11/15/code-design-after-agents
  <!-- Theme 3 overflow（関数型ドメインモデリング／設計） -->
- 274. https://dev.henry.jp/entry/e2e-repository
  <!-- Theme 3 overflow（E2Eガードレール／品質保証） -->
- 097. https://zenn.dev/mizchi/articles/mutation-test-quality
  <!-- Theme 3 overflow（ミューテーションテスト／品質保証） -->
- 123. https://zenn.dev/karamage/books/50c18e52e7d19e
  <!-- Theme 3 overflow（pstack／設計） -->
- 081. https://syu-m-5151.hatenablog.com/entry/2026/11/15/093525
  <!-- Theme 3 overlap（Herdr hgm＝ハーネス/監督が主題。ax90だが独立性規則によりomit提案） -->
- 165. https://xinmingtu.cn/blog/2026/claude-opus-5-5-protein-sequences/
  <!-- Theme 1 overflow（ClaudeのタンパクLM／AI-science） -->
