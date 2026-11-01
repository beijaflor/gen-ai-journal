# GenAI週刊 Annex 2026年10月24日号

メインジャーナルからは漏れたものの、独自の価値を持つ記事のカタログです。

## Annexについて

このAnnexジャーナルは、単なる"残り物"ではなく、ユニークな視点、実験的な試み、批判的思考、そしてニッチな深掘りを提供する厳選された「B面」コレクションです。

各記事は**カタログ形式**で紹介されています。80〜120字程度の簡潔な要約で、記事の核心と注目すべき視点を統合的に提示します。読むべきかを素早く判断できる構成です。

今週のB面は、新モデルとローカル実行、エージェント基盤と開発ツール、セキュリティとOSS、検証・言語設計・ベンチマーク、自律エージェントとフィジカルAI、労働・公益・文化をめぐる視点、開発ワークフローと組織運用、そして個人開発・学習・ファクトリー実践の8分野をカバーしています。

---
## 1. 新モデル・ローカル実行・音声/OCR

### shev: Apple SiliconローカルまたはDeepSeekを利用したシンプルなJSON意思決定支援ツール
**原題**: GitHub - aditauqir/shev: A simple Jev-like decision maker. Without the hype.
**URL**: https://github.com/aditauqir/shev

メールやチケットなど1件の入力に対し、対応要否・信頼度・返信案をJSONで返す判断特化のツールです。Apple SiliconではMLX上の2.2Bモデルがローカルで動き、それ以外はDeepSeek APIを使います。MCPで過去の判断履歴を他ツールから検索できます。エージェント化せず「1メッセージ1判断」に絞った設計が、読む価値のある点です。

---

### DeepSeek-V4.1-Flash-1017: 推論・コーディング・エージェント性能を向上させた最新マイナーアップデート
**原題**: deepseek-ai/DeepSeek-V4.1-Flash-1017 · Hugging Face
**URL**: https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017

V4.1-Flashの小幅更新版で、HLE、Terminal-Bench、DeepSWEなどのベンチマークで改善が報告されています。1Mトークンのコンテキスト、256K超の最大出力に対応し、MITライセンスで公開されました。実行時間の短縮と出力の最適化でコスト効率を上げた点が特徴で、モデルカードの数値と配布条件の確認用として読む価値があります。

---

### AI特有の書き癖（スロップ）を排除した「Qwen3-4B-deslop」の公開
**原題**: Qwen3-4B with the AI writing tics trained out
**URL**: https://100toolkit.com/blog/deslop-model/

Qwen3-4Bから、エムダッシュの多用や「delve」といったAI特有の文体を取り除いた微調整の記録です。独自の検出器を作り、MacBook Air上でわずか161件の回答からLoRA微調整を行い、スロップスコアを121から12.5へ下げました。GGUF形式でOllamaから動かせます。文が平坦になる点や固有名詞の捏造も率直に報告されています。

---

### Voxtral 3：音声認識・合成およびボイスエージェント用SDKの発表
**原題**: Voxtral 3: Speech-to-Text, TTS & Voice Agents | Mistral
**URL**: https://mistral.ai/news/voxtral-3/

Mistral AIが、50以上の言語に対応する音声認識、35以上の言語の音声合成、LiveKitベースのVoice Agent SDKを一式で公開しました。応答は1秒未満とされ、ツール実行を伴う対話もできます。欧州ホストのAPIに加えて自己環境へのデプロイも選べるため、データ主権を重視する企業が音声エージェントを検討するなら確認する価値があります。

---

### Indra OCR - CPUで動作する高速・軽量な多言語対応ドキュメント解析モデル
**原題**: datalab-to/indra-ocr · Hugging Face
**URL**: https://huggingface.co/datalab-to/indra-ocr

100万〜700万パラメータ、全体で約76MBのOCRモデルです。GPUなしで32コアCPUなら毎秒約44ページを処理し、Tesseractの15倍、PaddleOCRの10倍とされています。日本語を含む80以上の言語、手書き、数式に対応します。重みは修正OpenRAIL-Mで、売上2000万ドル以上の企業は条件の確認が必要です。

---
## 2. エージェント基盤・ランタイム・開発ツール

### react-devtools-cdt-mcp で AI エージェントが React のコンポーネントツリーを調べられるようにする
**URL**: https://azukiazusa.dev/blog/react-devtools-cdt-mcp/

Chrome DevTools MCP経由ではDOMは操作できても、Reactのコンポーネント階層やProps、Hooksの状態は見えなかった。react-devtools-cdt-mcpは、アプリでimportしMCPサーバーをフラグ付きで起動するだけでこれらを公開する。Claude Codeが重いレンダリング箇所をプロファイリングで特定するデモがあり、フロントエンドのデバッグをエージェントに任せたい人は設定手順だけでも読む価値がある。

---

### エージェントスキル集 pstack の開発原則と使い方
**URL**: https://azukiazusa.dev/blog/pstack-agent-skills/

MetaやNetflixでの大規模開発経験をもとにしたスキル集pstackの解説。実装前に既存コードを調べて設計し、変更は最小限に抑え、コンパイルの成功ではなく再現スクリプトによる動作確認を求める。複数モデルの指摘を統合するinterrogateスキルも持つ。生成量より品質を優先する原則は、スキル設計の参考として読む価値がある。

---

### AIエージェント向け最速ブラウザ「ego lite」- 並列実行とChromeデータ引き継ぎに対応
**原題**: ego lite - The Fastest Browser for AI Agents
**カテゴリー**: ツール紹介
**URL**: https://ego-lite.apposters.com/

利用者が通常のブラウザ操作を続けたまま、エージェントが分離されたSpacesでタスクを並列実行できるデスクトップアプリ。Chromeのログイン情報や拡張機能を引き継ぎ、JavaScript関数を直接書くコード制御で最大2.5倍の高速化をうたう。データはローカル保存。ただし速度は製品ページ上の主張で、第三者の検証は示されていない。

---

### Maxwell: 世界初のコード実行モデル (CEM) — プログラム実行中にバイナリを動的最適化・形式証明
**原題**: Maxwell: The first Code Execution Model, by doubleAI
**URL**: https://heymaxwell.ai/

doubleAIが発表したMaxwellは、コードを書くのではなく実行中のバイナリを書き換えるモデル。データフローに基づきSIMDなどに最適化し、元のコードとの等価性を形式検証で証明すると説明する。LTX-2.5の4K動画生成は250秒から134秒に短縮された。ソースを変えずに速度を上げる発想は興味深いが、公開されている根拠は事例にとどまる。

---

### Vite+がAIエージェントによるアプリケーション開発手法をどのように変えたか
**原題**: Vite+ changed how I build applications with AI agents
**URL**: https://janmichalek.com/blog/vite-plus-agentni-vyvoj?lang=en

ESLint、Prettier、TypeScript、テストランナーの設定が散らばると、エージェントは何をもって「完了」とするか迷う。筆者はVite+で `vp check` と `vp build` に統一してこれを解消し、モノレポのCI時間を4分から50秒に短縮した。具体的なプロンプト例も公開されている。既存の大規模案件への移行には慎重な姿勢で、新規プロジェクト向けの標準化手法として読むのがよい。

---

### T3 Code - 複数のAIコーディングエージェントを統合管理するオープンソース・コントロールパネル
**原題**: pingdotgg/t3code: T3 Code is an "agent harness control surface".
**URL**: https://git.cafe/pingdotgg/t3code

Claude Code、Codex、Cursor、OpenCodeなどローカルのエージェントを一つの画面から操作するオープンソースのハーネス。各ツールの契約をそのまま使え、モバイル、Web、Electronから同じ操作感で利用でき、サーバー経由で遠隔操作もできる。Vite+を採用している。初期段階のため、複数ツールを併用していて操作画面を統一したい人向けの試用候補。

---

### 日本語の業務データが、そのまま日本語のオントロジーに。Context Ontology Accelerator v0.3.6 の日本語対応
**URL**: https://zenn.dev/aws_japan/articles/context-ontology-accelerator-multilingual

AWSのOSS「Context Ontology Accelerator」v0.3.6は、Namespace単位で言語を指定でき、日本語のテーブル名やカラム名のままオントロジーを生成できる。練馬区のオープンデータを使い、分かち書きがない日本語に合わせた文字種変化でのMetric照合や、RDF言語タグ(@ja)の付与基準を説明する。日本語データでの運用を検討する人には、設計判断の根拠まで読める実践記事。

---

### DeNAにおけるAI時代のネットワーク管理システム [DeNA インフラ SRE]
**URL**: https://engineering.dena.com/blog/2026/10/nwcli/

DeNAのネットワークグループが、内製ツールnwcliで設定の構造化と共通化をやめ、生のConfigを直接扱う方針に転換した事例。LLMがコードを生成するので冗長さの管理コストが下がり、共通化による意図しない波及も避けられるという。MCPサーバー経由でAIがPR作成まで行い、人の役割はレビューに移った。人間向けの抽象化を見直す視点を得たいインフラ担当者に向く。

---
## 3. セキュリティとOSSの守り

### Claudeを活用したコードの攻撃対象領域（アタックサーフェス）の削減
**原題**: Using Claude to reduce the attack surface of code
**URL**: https://www.anthropic.com/research/attack-surface-reduction

AnthropicのFrontier Red Teamが、未知の脆弱性探しではなく「攻撃者が到達できるコード領域」の削減にClaudeを使った研究です。25のOSS(500万行超)から493件の問題を発見し、OpenSSHでは未認証で到達可能な不要な実験的コード約4,500行を特定、該当領域の約5分の1を削減できました。脆弱性を個別に潰すより露出そのものを減らす発想が、自社コードにも応用できる点で読む価値があります。

---

### Patch the Planet — オープンソースのセキュリティをAIで強化するOpenAIの新イニシアチブ
**原題**: Patch the Planet — OpenAI
**URL**: https://patchtheplanet.org/

OpenAIの「Daybreak」の一環で、Trail of BitsやHackerOneと組み、AIが見つけた脆弱性を人間が検証してメンテナにパッチを届ける取り組みです。Node.jsやBunに影響するBrotliの脆弱性などの修正実績があり、ファジング導入やテスト改善といった継続的な防御支援も含みます。OSSメンテナの負担をAI側が引き受ける形をどこまで維持できるかが、評価の分かれ目になりそうです。

---

### 1Password for Agents：AIエージェントにパスワードを教えずにログインを自動化する新プラットフォーム
**原題**: Introducing 1Password for Agents
**URL**: https://1password.com/blog/1password-for-ai-agents

エージェントへのタスク委任では、パスワードをプロンプトに書くか、ログイン画面のたびに人が介入するしかありませんでした。1Password for Agentsは、エージェントのログイン要求をユーザーが承認すると1Passwordが自動入力し、認証情報をモデルに渡しません。ChatGPTやClaudeなどとの連携が進行中で、個人・ファミリープランで提供が始まっています。エージェント運用の認証設計を考える人は押さえておきたい発表です。

---

### AI Bot Cosplay：AIボットを装い機密情報を狙う「なりすまし」攻撃の分析
**原題**: AI Bot Cosplay
**URL**: https://www.fastly.com/blog/ai-bot-cosplay

Fastlyの調査では、1日で600万件超のリクエストがOpenAIやAnthropicなどのAIボットを名乗り、.envファイルやGitメタデータを探っていました。約94%は単一のキャンペーンで、約1,600のIPが12種のボットを使い分け10万以上のサイトを走査しています。AIクローラーに寛容な設定が悪用されるため、User-Agentを信用せずIPレンジで検証済みボットを判定する対策が必須です。サイト運営者は自サイトの設定確認に役立ちます。

---

### ひとり会社が、AIと二人でISMSを取った話
**カテゴリー**: 実践事例
**URL**: https://note.com/timtarou/n/n5443f159e7bc

会計事務所向け経理代行の4649株式会社の代表が、AIとISO/IEC 27001(ISMS)を取得した体験談です。規格書と海外GRCツールの機能をAIに学習させて管理策を整理し、資産台帳はGoogle WorkspaceやGitHubのAPIから自動取得、審査にもAIが同席しました。雛形に自社を合わせず、実態をAIに文書化させる方針で形骸化を避けています。小規模組織が認証取得を検討するなら、進め方の具体例として参考になります。

---
## 4. 検証・言語設計・ベンチマーク

### ソースコードがない？問題ありません！：バイナリしかないプログラムを移植するには？
**原題**: No Source Code? No Problem!: What if you have to port a program, but all you have is a binary?: Queue: Vol 1, No 6
**URL**: https://queue.acm.org/doi/10.1145/945131.945155

ソースが失われた旧ソフトを現代機へ移植する手法を、エミュレーションとバイナリ翻訳の比較で解説する。前者は忠実だがデコードやフラグ更新の負荷が大きく、後者は高速でも自己書き換えコードやジャンプテーブルの解析が難しく、生成コードの保守性も低い。TRS-80やファンタシースターIIIの事例付き。AI時代の話題ではなく、変換の限界を知る古典として読む価値がある。

---

### ポケモン2v2環境におけるマルチエージェントLLMの協調
**原題**: Multi-agent LLM coordination in a Pokémon 2v2 environment
**URL**: https://olivergrabner.com/research/pokemon/

不完全情報ゲームのポケモンのダブルバトルで、LLMエージェント間の対話が協調に与える影響を測った実験。Qwen3.8-27Bでは自由に会話できる設定の勝率が64%で、対話なしの42%、単一モデルによる2体操作の54%を上回った。相性の誤解を互いに訂正する場面も確認された。ただし1バトルで約100万トークンを消費し、協調の利得とコストの釣り合いが問われる。

---

### LLMを混乱させるために設計された難解プログラミング言語「KillSwitch」の実験と検証
**原題**: I built a programming language that LLMs can't use
**URL**: https://blog.picheta.me/post/killswitch-lang/

LLMのコード生成が記憶か論理的理解かを確かめるため、Dominik Picheta氏がスタック型の難解言語を作った。識別子の文字数カウントの強制、仕様書への虚偽の混入、「Ignore previous instructions」の構文化など、あえてLLMを惑わす設計になっている。Claude Opus 5が最高スコアでも、多くのモデルはガードレールの作動で失敗した。未知言語での対応力は印象的だが、真の理解とは別物という結論。

---

### レビューの終わりとは何か — AIレビューの停止と品質の完了条件
**URL**: https://qiita.com/kayowa/items/3c997b135b78eab24542

AIが実装とレビューの両方を担う開発で、修正のたびに新たな指摘が出て終わらない「レビューの収束」問題を、家計簿アプリの実験で扱う。提案は、初回は統合レビューを全面実施し、以降は影響範囲を独立に判断して証拠を再利用すること。Claude Codeチームの事例も参照する。未完了リスクをCIや人間の承認という別ゲートで扱うべきだという主張が、実装側の判断材料になる。

---

### LLMにとって書きやすい構文とは何か：end と end func foo を1,000回以上比べてみた
**URL**: https://zenn.dev/nextbeat/articles/2026-10-syntax-locality-llm

学習データにない未知の言語で、ブロックの閉じ方を単純な `end` と `end func foo` のような名前付き閉じで比較した1,000回超の生成実験。ネスト深さ8以上では単純な閉じ方が全滅し、名前付き閉じはほぼ100%の精度を示した。著者は依存距離の短縮よりも、各行で構造を自己照合できる冗長な手がかりが効くと分析する。言語設計の常識に一石を投じる結果で、読む価値は高い。

---

### E-Commerce Bench: 長期間の自律的ビジネス運営におけるLLMエージェントの評価ベンチマーク
**原題**: E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business Operation
**URL**: https://arxiv.org/abs/2608.30730

仮想環境の365日間で、市場調査、仕入れ交渉、在庫管理、資金繰りを行い総資産を競う長期エージェント評価。18モデルの比較では、GPT-5.6 Solが総資産で首位でも不正回避は16位で、全指標で勝つモデルはなかった。オープンウェイトではQwen3.8-Max-Previewが最大利益を出した。単一指標の順位だけで選べないことを示す点が最大の収穫。

---
## 5. 自律エージェント・フィジカルAI・世界モデル

### MetaのパーソナルAIエージェント「Muse」、日本で提供開始
**URL**: https://www.watch.impress.co.jp/docs/news/2150567.html

Metaが北米以外で初めて、日本でMuseの提供を始めた。メール送信や旅行予約を代行し、メルカリなど国内サービスとも連携する。隔離VM上で動き、決済前には必ず承認を求める。月額2,799円からの有料プランもあり、日本の連携先を知りたい人向け。

---

### Company World Modelsへの道：実体経済をAIで進化させるBeaconの構想
**原題**: Towards Company World Models — Beacon
**URL**: https://www.beaconholdings.com/research/towards-company-world-models

Beaconは、経営判断を支援する「Company World Models」を提唱する。現在のLLMはカフェ経営の実験で赤字を出すほど未熟で、傘下企業の内部データと熟練オーナーの判断で補う方針だ。引退世代の経験をモデルに継承させる狙いが独自である。

---

### フィジカルAIの社会実装に向けて -AIエージェントからAgentic Roboticsへ-
**URL**: https://speakerdeck.com/hf149/fijikaru-ai-no-shakai-jissou-ni-muke-te-ai-ejento-kara-agentic-robotics-he

AIの進化を4段階で整理し、VLAや世界モデルによるロボット制御を紹介するスライド。エージェントが制御コードを自ら書く「Agentic Robotics」を提唱し、信頼性や破滅的忘却といった現場の課題も扱う。動向を一通り把握したい人向け。

---

### シリコンバレー、AIエージェント訓練用の「シミュレーション環境」に巨額投資
**原題**: Silicon Valley bets big on 'environments' to train AI agents | TechCrunch
**URL**: https://techcrunch.com/2025/09/21/silicon-valley-bets-big-on-environments-to-train-ai-agents/

関心は静的データから、エージェントが操作を練習する強化学習環境へ移っている。Anthropicは1年で10億ドル超を構想する。ただしリワードハッキングが壁で、投資が成果に結びつくかは未知数だ。

---

### 人間のAIに対する判断移譲
**URL**: https://scrapbox.io/nishio/%E4%BA%BA%E9%96%93%E3%81%AEAI%E3%81%AB%E5%AF%BE%E3%81%99%E3%82%8B%E5%88%A4%E6%96%AD%E7%A7%BB%E8%AD%B2

Copilotの提案から、Cursorの承認なし実行、Claude CodeのAuto modeまで、2024年以降の変化を整理した記事。人間の確認待ちが最大のボトルネックになったと説く。最終判断への固執は「信仰」に近いという主張が論争的だ。

---
## 6. 労働・公益・文化をめぐる視点

### Anthropicにおける雇用と業務の変化：AIエージェントの浸透による組織変革の実態
**原題**: How employment is changing at Anthropic
**URL**: https://www.anthropic.com/research/employment-at-anthropic

Anthropic社内ではAIエージェントの稼働時間が人間の6倍に達し、エンジニアのコード生成量は半年で5倍になった。ジュニア技術職の採用比率は27%から9%に低下し、評価軸も自律性と判断力へ移る。AI企業自身による雇用変化の開示だ。

---

### Anthropic 2026年公益報告書：AIの安全性と人類への貢献に向けた5つの柱
**原題**: Public Benefit Report \ Anthropic
**URL**: https://www.anthropic.com/public-benefit-report

公益法人のAnthropicが、安全性の技術的解決、普遍的な安全慣行、民主主義の強化、繁栄、利益の公平な分配の5本柱を示した年次報告書。方針の宣言が中心で、具体的な数値は乏しい。同社の公式な立場を確認したい人向けだ。

---

### AI文学賞受賞作品リスト：AI活用の歴史と論争の記録
**原題**: Award-Winning AI Literature
**URL**: https://jamesyu.org/award-winning-ai-literature/

AIが関与した、または疑われた文学作品と賞の事例一覧。日経・星新一賞や芥川賞の例に加え、AI検出器Pangramの疑惑を手書き草稿で晴らした作家が続出し、検出器の信頼性の低さが浮かぶ。創作とAIの境界を事例で知りたい人向け。

---

### AI時代にWebサイトは必要なのか？
**URL**: https://www.mitsue.co.jp/knowledge/column/20261020.html

AIが情報を要約する時代でも、Webサイトは信頼構築と検証可能な公式情報源として必要だと説くコラム。言行一致、セキュリティとガバナンスの強化、AIエージェントも対象にしたアクセシビリティを優先事項に挙げる。運営方針の見直し材料になる。

---

### 私たちは今でも紙を使っている：AI時代における道具の選択と主体性
**原題**: We Still Use Paper
**URL**: https://humanpro.co/articles/we-still-use-paper/

数千年を経ても人が紙で考える理由から、AIの位置づけを論じる。チャット形式が万能ではなく、AIも用途別の製品へ洗練が要ると指摘する。道具が成果物に与える影響を理解し、自分で選ぶ姿勢を促す、立ち止まって考えたい人向けの一本。

---

### 使い捨てのソフトウェア：AnthropicのScionに見るAI時代の開発文化
**URL**: https://records.dodgson.org/2026/10/16/disposable-software/

AnthropicのVCS「Scion」はMetaのSaplingに似ているのに謝辞がない、という指摘から始まる。AIによる模倣が容易になると、OSSを通じた技術共有が衰え、使い捨ての開発に傾くと警鐘を鳴らす。筆者個人の主張だ。

---

### 公益への投資：Anthropicが「Anthropic Public Benefit Fund」を設立
**原題**: Investing in the public benefit
**URL**: https://www.anthropic.com/news/public-benefit-fund

AnthropicがLLC形式の公益基金を設立した。当初は株式の5%を保有し、企業価値が50%上がるごとに2%を追加する成長連動型で、最終的に約20%以上が公益に充てられる見通し。労働市場対策や寄付に使い、ロビー活動は禁止される。

---
## 7. 開発ワークフローと組織運用の実践知

### エージェントを使い続けるためのメタワーク / Meta-work for keeping using the agent
**URL**: https://speakerdeck.com/rkaga/meta-work-for-keeping-using-the-agent

コード生成が速くなった結果、人間の確認と判断が新たなボトルネックになったという前提のスライドです。対策として、仕様や決定事項をAIが自分で引ける組織コンテキスト、トリガーで動く自動テスト・QA、実行記録から指示を改善する仕組み、図解による承認の迅速化の4点を挙げます。AIが書く量が増えるほど、人間の仕事は仕組み作りへ移るという主張が核心です。

---

### AIプロダクト開発から学んだ38の教訓：PostHogにおける4年間の実践的知見
**原題**: 38 things we've learned about building AI products
**URL**: https://newsletter.posthog.com/p/38-things-weve-learned-about-building

PostHogが4年間・10以上のAIプロダクトで得た知見をまとめた記事です。LLMは差別化にならず、独自のデータ・ツール・ワークフローというコンテキストが競争力になると述べます。UIはエージェントの処理を確認・承認する場に変わり、評価は小さなデータセットから早く始めるべきだとします。製品設計をエージェント利用前提で問い直す視点が参考になります。

---

### AI時代の開発ワークフロー「Brain Sandwich（脳のサンドイッチ）」：思考を外注しないためのシンプルな手法
**原題**: The Brain Sandwich – Terrible Software
**URL**: https://terriblesoftware.org/2026/10/02/the-brain-sandwich/

AIに思考まで任せてしまう問題への対策として、Emily氏が示す手法です。人間が方向を決め、AIが実装し、人間が差分をレビューする3段階で進めます。判断基準は「自分の言葉で変更内容を説明できないなら、レビューに出さない」の一点です。導入コストが低く、すぐ試せる運用ルールとして読む価値があります。

---

### 社内の Slack と GitHub を LLM に読ませて技術ブログの題材を探す：モデルに任せたこと、任せなかったこと
**URL**: https://zenn.dev/salt2/articles/slack-github-llm-bb912760

SALT2社が、Slack・GitHub・会議メモをLLMに解析させて技術ブログの題材を探した記録です。そのままでは変更履歴への偏り、人名の誤認、守秘判定のミスが起きるため、モデルが推測してよい範囲を厳密に限定しました。日本語の単語境界にはバイグラム比較を使い、執筆可否とプライバシー判断は人間に残します。任せない範囲の線引きが具体的です。

---

### ClaudeにiOSシミュレーターのスクリーンショットを読ませるのをやめて、操作で増えるコンテキストを43%削減した
**URL**: https://zenn.dev/eai/articles/dont-let-agents-see-the-ios-sim-screen

スクリーンショット1枚が約2,500トークンを消費し、コンテキストを圧迫する問題への対処です。アクセシビリティ情報のテキスト出力、検証時のみ低解像度JPEG、カスタムURLスキームによる画面遷移の3つで、コンテキスト増分を43%、画像枚数を96%削減しました。ドラッグ時の慣性を抑える座標の微振動など、AGENTS.md付きの実装例まで公開されています。

---

### AIを利用したレガシーコード改善
**URL**: https://zenn.dev/naoyuki1212/articles/20261019-legacy-code-with-ai

テストのないGo/Wails/Svelte製の自作アプリを、Claude Codeで改善した記録です。先に特性テストとゴールデンファイルでカバレッジ100%の安全網を作り、AIが見つけた10件の挙動矛盾を人間が判断して修正しました。その後にパッケージ分割やSvelteから素のTypeScriptへの移行も実施しています。テストを先に固める順序が、AI任せの大規模改修を成立させた要点です。

---

### 人による工数見積もりをやめて、AIに任せることにした
**URL**: https://www.tanp-blog.com/entry/2026/10/15/110018

タンプ社が、施策の工数見積もりをエンジニアからAI（Devin）に移した事例です。施策検討で必要なのは絶対的な精度ではなく、優先順位を決めるための一定基準での比較だと考えました。事業部が要求定義を書き、AIがコードベースを調査して不備と工数を返すため、ROI判断まで事業部内で完結します。精度より速度を選んだ割り切りと役割分担の再設計が読みどころです。

---

### 【資料公開】AIで組織を加速させる勘所
**URL**: https://www.ryuzee.com/contents/blog/14627

アジャイルコーチの吉羽龍太郎氏による講演資料です。AIは組織の増幅器であり、機能不全の組織はより悪化すると指摘します。個人作業ではなく顧客に届くまでのフローを最適化し、承認待ちを減らして判断を現場へ寄せ、増える検証コストは機械化で下げます。成果は生成量ではなくアウトカムで測り、生まれた時間を学習に充てる点が実践的です。

---
## 8. 個人開発・学習・技術スタックとファクトリー実践

### AIを使えば、ソフトウェアエンジニアとしての規律は身につくのか
**URL**: https://note.com/yoshiki_shibata/n/n9b1a1bbfb4f1

ベテランエンジニアの柴田芳樹氏が、AI時代の「エンジニアとしての規律」を論じた記事。AIはコードやテストを高速に生成するが、バグ修正前に再現テストを書く、仕様を先に定義するといった品質確保の原則までは教えない。規律がなくてもソフトウェアは完成するため、若手が手順の理由を学ぶ場がどこにあるのかという教育上の問いが残る。

---

### Claude Opus 5.5でいい感じのアクションゲームを作るための一工夫七つ
**URL**: https://aba.hatenablog.com/entry/2026/10/22/194027

AIエージェントでゲームを作る際の7つの工夫を紹介する。ランダムなタグで発想を広げる、面白さの源泉を実装前に言語化する、人間の主観的な体験をエージェントへ正しく返す、といった内容だ。中でも、強いだけでなくプレイヤーと同等の実力のボットを作らせて難易度を調整する手法が実用的で、ゲーム開発以外の自動調整にも応用できる。

---

### Rust off Rails: AI時代に向けた、強い意見を持ったWebスタック
**原題**: Rust off Rails: the opinionated web stack for the AI era
**URL**: https://rustoffrails.org/

Claude CodeやCursorがコードを書くことを前提に、Railsの「設定より規約」をRustへ持ち込んだWebスタック。Axum、SeaORM、Tailwindを採用し、規約をAGENTS.mdに記述してAIに読ませる。ジョブキューやキャッシュをDBに集約して単一バイナリで配備できる点が特徴で、規約をAI向けに明文化する発想が読みどころだ。

---

### TanStack AIにおける構造化出力の探索：ストリーミングガイド
**原題**: Exploring Structured Output in TanStack AI: Streaming Guide
**URL**: https://blog.master.dev/structured-output-with-tanstack-ai/

TanStack AI入門シリーズの第2部。Zodでワークアウト計画のスキーマを定義し、サーバーとフロントエンドの両方でLLMの出力に適用する。JSON生成の途中でも、TanStack AIがタグを補完してパース可能な状態を保つ。DeepPartial型で画面を段階的に更新できるため、ストリーミングUIを実装する人は読む価値がある。

---

### Jevにウォーリーを探させたら0.4秒で見つけやがった!!
**URL**: https://qiita.com/kikuziro/items/c1b47d4bfaa64960ca18

判断特化型AI「Jev」の画像入力と位置特定機能を、AI生成のウォーリー風画像で検証した記事。AWS Lambda上で約400ms、1リクエストあたり約0.05円という結果で、Python SDKの実装例とトークン数の分析も載る。対象が小さい場合や絵柄が異なる場合はバウンディングボックスに補正が要るため、人間が確認する前の一次スクリーニング向きと結論づけている。

---

### 知らない分野を学ぶ技術 powered by AI
**URL**: https://smooth-pudding.hatenablog.com/entry/2026/10/17/145830

ガロア理論のような難解な分野をAIで独学する手順を、3段階で解説する。必要な前提知識をAIと洗い出し、自分の知識レベルを伝えて学習カリキュラムをMarkdownで作らせ、そのファイルを提示し直しながら図解や演習つきで進める。進捗記録や理解スタイルに合わせたプロンプト調整まで含み、新分野を学びたい人がそのまま試せる内容だ。

---

### ソフトウェア ファクトリー - 再現性のあるソフトウェアの工場づくり / Software factory
**URL**: https://speakerdeck.com/iktakahiro/software-factory

池内孝啓氏のスライド。AI時代の開発を「工場」と捉え、実装期間を2ヶ月から数日に縮めた事例を示す。TanStack StartやBun、ConnectRPCによるT-Stackのモノレポ構成、レビューやE2Eテストをリポジトリ内でスキル化する仕組み、docsへの文脈集約が柱だ。人間は製造ラインの構築と全体設計を担い、コーディングはAIに任せる分業を提案している。

---

### 施策立案からQAまで：AIエージェントで回す開発フローの全体像とアーキテクチャ
**URL**: https://tech.findy.co.jp/entry/2026/10/16/120000

ファインディが、PM向け・開発向け・QA向けの3つのプラグインで構成したAIエージェントの開発フローを公開した。GitHub Issueのblocked_byで並列実装を制御し、スタックPRでレビューを効率化、Playwright MCPで自動QAを行う。施策の採択とマージ判断、最終QAは人間が担う「AIが委任、人間が判断」の設計が、導入時の参考になる。

---

🤖 本記事は [Claude Code](https://claude.com/claude-code) を使用して編集されました。
