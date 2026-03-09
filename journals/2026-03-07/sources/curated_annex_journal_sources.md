# Curated Annex Journal Sources — 2026-03-07

## Curation Status
- [x] AI candidate pool generated
- [x] Human review completed
- [x] APPROVED — Ready for STEP_06

**候補総数: 44記事 → 目標: 25-35記事に絞り込み**

---
<!-- Review: check [x] to include, remove line to exclude. Target: ~25-35 articles. -->
<!-- ⭐ = annex_flag（ブラウジング時に事前マーク） -->

---

## ブロック A: 思想・批評・マニフェスト

<!-- AIと社会・職業・哲学の境界に踏み込む論考 -->

- [x] 002. https://www.oreilly.com/radar/betting-against-the-bitter-lesson/
  <!-- ティム・オライリーが「ビター・レッスン」への対抗として人間の暗黙知をエージェントの「スキル」にパッケージ化する知識経済論を展開。戦略的視野が高い。 -->

- [x] 037. https://www.scottsmitelli.com/articles/you-dont-have-to/
  <!-- 「AIslop」の蔓延と「脳の賃貸」への警告。AIを使わない選択を肯定する、力強い反骨精神のエッセイ。 -->

- [ ] 111. https://nonstructured.com/zen-of-ai-coding/
  <!-- 「Zen of Python」へのオマージュ。AIエージェント時代のエンジニアリング哲学を10箇条で説く。コードを書くことからフィードバックループの設計へ。 -->

- [x] 076. https://www.agenticmanifesto.org/
  <!-- アジャイル・マニフェストのAI時代拡張版。人間とAIの共創・適応型知能・分散主体性を提唱。 -->

- [ ] 101. https://www.siliconsnark.com/do-ai-agents-actually-make-money-in-2026-or-is-it-just-mac-minis-and-vibes/
  <!-- 「AIエージェント自動収益化」ブームへの辛辣な批判。Mac Mini積み上げ系の幻想を解体し、真の価値は地味なB2B業務自動化にあると説く。 -->

- [x] 112. https://newsletter.danielpaleka.com/p/you-are-going-to-get-priced-out-of
  <!-- 最高のAIツールから一般ユーザーは締め出される——推論時計算量の増大がもたらす価格上昇と「AIの民主化」終焉論。 -->

- [x] 066. https://levtech.jp/media/article/interview/detail_814/
  <!-- 吉羽龍太郎氏の逆説「AIで爆速になる必要はない」。余剰時間を機能量産でなく価値探求に使えというアジャイルへの回帰。 -->

---

## ブロック B: セキュリティ深掘り・アーキテクチャ

<!-- メインジャーナルのTheme 3を補完する、より専門的・実践的なセキュリティ論 -->

- [x] 014. https://nanoclaw.dev/blog/nanoclaw-security-model
  <!-- 「エージェントを信頼するな」——コンテナ分離・エージェント間隔離・最小コードベースで構築するゼロトラストAIエージェント設計。メインTheme3の対策論を深掘り。 -->

- [x] 057. https://zenn.dev/aeyesec/articles/417578718dcced
  <!-- PRを送るだけでリポジトリを乗っ取る。GitHub ActionsのAIエージェント攻撃を実機検証した実証レポート。コマンドインジェクション3パターンを解説。 -->

- [ ] 083. https://qiita.com/takao-shimizu/items/7cb1d8b48cd442e07962
  <!-- Kubernetes環境でSysdig×OpenClaw×MCPを組み合わせ、24時間自律稼働するAI SOCを構築した実践記録。MITRE ATT&CK自動マッピング含む。 -->

- [ ] 026. https://www.mcherm.com/deterministic-programming-with-llms.html
  <!-- LLMの確率的ミスを防ぐには「ルールを守らせる」のでなく「決定論的なガードレールをLLMに作らせる」。Leanとの接続が鮮やか。 -->

- [ ] 091. https://blog.cloudflare.com/email-security-phishing-gap-llm/
  <!-- 受動的→能動的なフィッシング検知。LLMで「見えていなかった空白」を特定しMLモデルを訓練するCloudflareのハイブリッド防御。Q4で検知漏れ20.4%削減。 -->

---

## ブロック C: エンジニアリング・開発体験の転換

<!-- Claude Code / AIエージェントの実践的・思想的な応用事例 -->

- [ ] 047. https://product.hubspot.com/blog/automated-code-review-the-6-month-evolution
  <!-- HubSpotのAIコードレビュー6ヶ月進化記。Java自社フレームワーク移行＋「Judge Agent」導入でノイズ激減、サイクルタイム90%削減。 -->

- [x] 098. https://martinfowler.com/articles/reduce-friction-ai/design-first-collaboration.html
  <!-- Martin Fowler作。コード生成前に5階層でAIと設計合意する「デザイン・ファースト」手法。「実装の罠」を防ぐホワイトボード対話の再現。 -->

- [ ] 058. https://zenn.dev/ramenumaiwhy/articles/178406388fced6
  <!-- 非エンジニアのvibe-codingに「理解」を強制するplan-viewerプラグイン。PreToolUse hookで設計確認をブロックする独創的な設計。 -->

- [ ] 073. https://dev.henry.jp/entry/2026/03/02/120532
  <!-- Claude Codeのマルチエージェントで電子カルテの外部連携仕様書を自動生成。探索・生成・レビューの3エージェント構成が秀逸。 -->

- [ ] 075. https://techblog.enechain.com/entry/pdm-claude-code-impact
  <!-- PdMがClaude Codeで仕様書作成→AI同士でレビュー→Notion自動投稿パイプラインを構築。非エンジニアのAI活用拡張。 -->

- [ ] 044. https://developers.cyberagent.co.jp/blog/archives/62375/
  <!-- ABEMAのA/Bテスト膨大な過去知見を、Google ADKマルチエージェントで検索・要約・示唆出し自動化。Human-in-the-loopで精度担保。 -->

- [ ] 079. https://speakerdeck.com/karia/devintoclaude-code-srenoxian-chang-deshi-idao-sitemitajian
  <!-- FilmarksのSRE現場でDevinとClaude Codeを使い分けた実践事例。Terraform化・CI/CD・負荷試験など具体的な用途別ノウハウ。 -->

- [ ] 060. https://zenn.dev/heybombon/articles/be7b28840cd580
  <!-- AIが提案する「冪等性の確保」という対症療法が真のバグを隠蔽する技術的負債になる。AIのバイアスをドメイン知識で乗り越えた実例。 -->

- [ ] 051. https://qiita.com/delphinus/items/9325c8dd750c85bac944
  <!-- Claude Codeの会話をObsidianに全自動保存するツールを作った記録。AI時代の「車輪の再発明」の意義についての考察が光る。 -->

---

## ブロック D: アーキテクチャ・設計論

- [x] 063. https://zenn.dev/neko3cs/articles/software-architecture-for-the-ai-era
  <!-- AIがコードを書くことを前提とした「AIネイティブ・アーキテクチャ」論。クリーンアーキテクチャより「純粋MVC（Fat Model）」がAIの推論効率を最大化するという提言。 -->

- [x] 069. https://ejholmes.github.io/2026/02/28/mcp-is-dead-long-live-the-cli.html
  <!-- 「MCPは死んだ、CLIこそが本命」。専用プロトコルの複雑さを批判し、UNIX哲学的なCLI整備を説く反骨論。 -->

- [ ] 095. https://tonyalicea.dev/blog/trace-declarative-modeling-ai-age/
  <!-- AI時代の宣言的モデリング規格「Trace」。フォルダ構造でシステム仕様を定義しLLMへのインプット品質を担保する新アプローチ。 -->

- [x] 096. https://hvpandya.com/llm-design-systems
  <!-- デザインシステムをMarkdown仕様書・トークン層・監査スクリプトの3層でLLMに公開し、デザインドリフトを機械的に防ぐ手法。400箇所のハードコード排除。 -->

- [ ] 001. https://www.oreilly.com/radar/why-capacity-planning-is-back/
  <!-- クラウドの「無限の弾力性」神話が崩壊。GPUとAIワークロードの物理的制約によりキャパシティプランニングが第一級の設計変数として復活。 -->

---

## ブロック E: 倫理・社会・法

- [x] 080. https://www.jasonwillems.com/technology/2026/01/23/AI-Copyright/ ⭐
  <!-- AIは著作権法を壊したのでなく、人間規模前提の構造的欠陥を露呈させた。3層（学習・生成・流通）での限界分析が鋭い。 -->

- [x] 100. https://futurism.com/artificial-intelligence/ars-technica-fires-reporter-ai-quotes
  <!-- Ars TechnicaのシニアAI記者がハルシネーション引用で解雇。「AI専門家でも罠に陥る」という皮肉な事例。メディア倫理への問い。 -->

- [ ] 015. https://www.wired.com/story/openai-fires-employee-insider-trading-polymarket-kalshi/
  <!-- OpenAI従業員が予測市場でインサイダー取引し解雇。テック業界における新しい形の不正とコンプライアンスの空白。 -->

- [ ] 108. https://news.ycombinator.com/item?id=47230438
  <!-- EU AI Act第12条準拠のためのOSSロギング基盤。SHA-256ハッシュチェーン＋S3 Object Lockで改ざん防止する実装。 -->

- [x] 042. https://arxiv.org/abs/2602.07164
  <!-- LLMは性格サブネットワークを内部に持つ——プロンプト不要でペルソナを抽出できる新手法。パーソナライゼーションの根本を変える可能性。 -->

---

## ブロック F: 事前フラグ済み (annex_flag ⭐)

- [ ] 065. https://zenn.dev/jundayo/articles/1e7acf4409e7b1 ⭐
  <!-- Agent Skills × Notionでコルブの経験学習モデルに基づく振り返りを自動化。AIを思考深化パートナーとして使う独創的な事例。 -->

- [x] 102. https://danlevy.net/llm-connection-strings/ ⭐
  <!-- LLMをDB接続文字列のように扱う「llm://」URIスキームの提案。IETFのRFCドラフトに発展。DX改善の実用的発明。 -->

- [x] 107. https://leodemoura.github.io/blog/2026/02/28/when-ai-writes-the-worlds-software.html ⭐
  <!-- AI生成コードの検証ギャップにLean形式検証で応える。「テストは確信、証明は保証」——仕様記述がエンジニアの核心となる未来像。Theme 2（Knuth）と知的シナジーあり。 -->

- [x] 127. https://www.jonkolko.com/writing/a-design-turn ⭐
  <!-- デザインの本質が「制作」から「リベラルアーツ（批評リテラシー）」へ転換するというコルコの論考。AIによる制作自動化がデザイナーの存在意義を問い直す。 -->

- [x] 134. https://chrisclapham.com/blog/nuclear-war-an-llm-scenario ⭐
  <!-- LLMが核指揮系統に入ったら6分間で何が起きるか。ハルシネーションと機械的確信が人間の躊躇という最後の安全弁を破壊するシナリオ。Theme 1（倫理）の極点。 -->

- [x] 175. https://406.fail/ ⭐
  <!-- RFC 406i「AI生成スロップ拒絶プロトコル」の風刺的文書。「delve」の不自然な使用等の診断基準を列挙。投稿者と人間メンテナーの努力の非対称性を告発。 -->

- [x] 180. https://zenn.dev/astra_et_luna/articles/d8d0e89313d00f ⭐
  <!-- 4年間挫折したヒッタイト語学習アプリをClaude Codeで2週間で完成。58万インプレッション。「ディレクター兼ドメイン知識監修」として実装9割をAIに委ねた実践記録。 -->

- [x] 193. https://note.com/shi3zblog/n/n834b60210766 ⭐
  <!-- 自己書き換え型AIの試作を起点に、GitHubの「博物館」化・AIの身体性獲得・停滞するゲーム産業の再定義を説く文明論。80-90年代PC文化への郷愁と融合した独自視点。 -->

- [x] 225. https://note.com/tanakaps/n/n410dbceb8c8d ⭐
  <!-- プログラミング未経験者がClaude×PS3（Cell/SPU）開発に挑戦。15年未解決のcellGcmシェーダ制御を突破。「田中憲法」と「スキルファイル」によるAI協働の体系化が光る。 -->

- [x] 229. https://aba.hatenablog.com/entry/2026/03/01/140039 ⭐
  <!-- GodotエンジンがAIエージェント開発に最適な理由。ヘッドレスCLI・プレーンテキストシーンファイル・MCPなしの開発ループ。WSL2×Claude Codeによる実証付き。 -->

---

## レビュー用メモ

**ブロック別推奨採用数（目標25-35記事）:**
- A（思想・批評）: 7本 → 4-5本に
- B（セキュリティ）: 5本 → 3-4本に（Themeと重複しないよう注意）
- C（実践事例）: 9本 → 5-6本に
- D（設計論）: 5本 → 3-4本に
- E（倫理・法）: 5本 → 3-4本に
- F（事前フラグ）: 10本 → 全採用推奨（内容未確認の⭐マーク記事を確認してほしい）

**特に推奨する記事（AIとして強く推したいもの）:**
- 098（Martin Fowler設計論）— 権威ある著者、実践的、完成度が高い
- 069（MCP is dead）— 反骨論として際立つ
- 047（HubSpot Judge Agent）— 具体的な数値と進化プロセスが説得力抜群
- 111（Zen of AI Coding）— 哲学的でシェアされやすい
- 101（Mac Mini and Vibes）— ユーモアと洞察の両立
- 107（Lean形式検証 ⭐）— Knuth論文（Theme 2）との知的シナジー
