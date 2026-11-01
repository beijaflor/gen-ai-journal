# GenAI週刊 Annex 2026年10月24日号

メインジャーナルからは漏れたものの、独自の価値を持つ記事のカタログです。

## Annexについて

このAnnexジャーナルは、単なる"残り物"ではなく、ユニークな視点、実験的な試み、批判的思考、そしてニッチな深掘りを提供する厳選された「B面」コレクションです。

各記事は**カタログ形式**で紹介されています。80〜120字程度の簡潔な要約で、記事の核心と注目すべき視点を統合的に提示します。読むべきかを素早く判断できる構成です。

今週のB面は、新モデルとローカル実行の選択肢、エージェント基盤の実装、セキュリティとOSSの守り、研究・言語設計・学習法、開発実践と組織の勘所、そして労働・社会・道具をめぐる視点の6分野をカバーしています。

---
## 1. 新モデルとローカル実行の選択肢

### Anthropic、自律型プロアクティブエージェント「Claude Duet」を発表
**原題**: Introducing Claude Duet
**カテゴリー**: 製品発表
**URL**: https://claude.com/ja/resources/articles/claude-duet

AnthropicがClaude Opus 5.5を基盤とするエージェントアプリのプレビュー版を公開した。ユーザー不在でも仮想マシン上で動作し、Gmail、Slack、Stripeなど6,000以上のツールと連携して朝のブリーフィングから給与計算までを実行する。支払いや削除には承認が必要で、機密情報向けの分類器も備える。ただし提供は米国の一部ユーザーのウェイトリスト制で、日本からの検証はまだ難しい。

---

### AI特有の書き癖（スロップ）を排除した「Qwen3-4B-deslop」の公開
**原題**: Qwen3-4B with the AI writing tics trained out
**URL**: https://100toolkit.com/blog/deslop-model/

エムダッシュの多用や「delve」、三箇条のリストといったAI特有の文体を検出する独自の検出器を作り、MacBook Air上で161件の回答によるLoRA微調整を行った。スロップスコアは1000語あたり121から12.5に下がり、GGUF形式でOllamaから実行できる。ただし文章が平坦になり、固有名詞の捏造も残る。手法の再現手順を知りたい人向けの記事だ。

---

### Indra OCR - CPUで動作する高速・軽量な多言語対応ドキュメント解析モデル
**原題**: datalab-to/indra-ocr · Hugging Face
**URL**: https://huggingface.co/datalab-to/indra-ocr

Datalabが公開した100万〜700万パラメータの文書解析モデルで、全体で約76MB。GPUなしの32コアCPUで毎秒約44ページを処理し、Tesseractの15倍の速度とされる。日本語を含む80以上の言語、手書き、LaTeX数式に対応し、MarkdownやJSONで出力する。重みは修正OpenRAIL-Mで、売上2000万ドル未満の企業は無料のため、商用利用の条件確認が必要。

---
## 2. エージェント基盤・ランタイム・運用の実装

### Maxwell: 世界初のコード実行モデル (CEM) — プログラム実行中にバイナリを動的最適化・形式証明
**原題**: Maxwell: The first Code Execution Model, by doubleAI
**カテゴリー**: パフォーマンス・最適化
**URL**: https://heymaxwell.ai/

doubleAIが発表したMaxwellは、コードを書くのではなく「実行」を最適化するCode Execution Modelである。実行中のデータフローからボトルネックを特定し、SIMDなど特定の命令に最適化したバイナリへ動的に置き換え、元ソースとの等価性は形式検証で証明する。LTX-2.5の4K動画生成は250秒から134秒に短縮された。pandasのカーネル書き換えにも適用でき、ソース無変更で高速化する新しい計算の考え方を示す。

---

### Vortex CodeとArchitectの導入：Spinoza Labsによる次世代AIシステム設計
**原題**: Introducing Vortex Code and Architect — Spinoza Labs
**URL**: https://spinozalabs.ai/news/introducing-vortex-code

Spinoza Labsは、「読み取り・編集・繰り返し」の単一ループを超えるとしてVortex Codeを発表した。Architectモードは、Agent OSというコンパイラで設計図を作り、複数のエージェントが並列で実装する。コンポーネント間のインターフェース定義やテストによるゲート管理など、開発組織の構造を模している。ロボットCADや金融ターミナルを最小限のプロンプトから構築できるとするが、実証は紹介事例のみ。設計思想を知る目的で読む価値がある。

---

### Perplexity、自律型AIエージェント向けサンドボックスプラットフォーム「SPACE」をオープンソース化
**原題**: Open-sourcing SPACE, the sandbox platform behind Computer
**カテゴリー**: セキュリティ・リスク
**URL**: https://www.perplexity.ai/hub/blog/open-sourcing-space

PerplexityがComputer機能の基盤であるサンドボックスSPACEをオープンソース化した。エージェントごとに独立した仮想マシンで実行し、セッションの中断と復旧、状態のブランチ管理、ネットワークと資格情報の制御を備える。従来の商用プロバイダーより生成が3〜5倍速く、1日数百万セッションを処理するという本番運用の実績が根拠だ。エージェント実行基盤を自前で持つ際の設計の参照先として、有力な選択肢になる。

---

### DeNAにおけるAI時代のネットワーク管理システム [DeNA インフラ SRE]
**URL**: https://engineering.dena.com/blog/2026/10/nwcli/

DeNAのネットワークグループが、数千台規模の機器を管理する内製ツールnwcliの進化を紹介する。設定の構造化と共通化をやめて生のConfigをそのまま扱う方針に転換した。LLMがコード生成を担えば冗長さの管理コストは下がり、共通化による意図しない影響の波及も避けられるためだ。Goへの書き換え、AWS Lambda上のAnsible実行、MCPサーバー経由でPR作成まで担うAI運用も含む。人が整えやすい形を捨てる判断は、読む価値が高い。

---

### ClaudeにiOSシミュレーターのスクリーンショットを読ませるのをやめて、操作で増えるコンテキストを43%削減した
**URL**: https://zenn.dev/eai/articles/dont-let-agents-see-the-ios-sim-screen

iOSシミュレーターを操作するエージェントは、スクリーンショット1枚で約2,500トークンを消費する。筆者はアクセシビリティ情報のテキスト出力、検証時のみ低解像度JPEGを送る方式、カスタムURLスキームによる画面遷移の3つで、コンテキスト増分を43%、画像枚数を96%削減した。ドラッグ時の慣性を終点の座標を微振動させて抑える技法やAGENTS.mdの指示も公開されている。画面を見せない方が精度もコストも良くなるという実測が、最大の収穫である。

---
## 3. セキュリティとOSSの守り

### Claudeを活用したコードの攻撃対象領域（アタックサーフェス）の削減
**原題**: Using Claude to reduce the attack surface of code
**URL**: https://www.anthropic.com/research/attack-surface-reduction

AnthropicのFrontier Red Teamが、未知の脆弱性探しではなく「攻撃者が到達できるコード」の削減にClaudeを使った報告。25のOSS（500万行超）で493件の問題を見つけ、OpenSSHでは未認証で到達可能な不要な実験的コード約4,500行を特定し、到達可能コードを約5分の1減らした。修正対象を脆弱性から露出範囲へ移す発想が読みどころ。

---

### Patch the Planet — オープンソースのセキュリティをAIで強化するOpenAIの新イニシアチブ
**原題**: Patch the Planet — OpenAI
**URL**: https://patchtheplanet.org/

OpenAI主導の「Daybreak」の一環で、Trail of BitsやHackerOneと組み、AIが見つけた脆弱性を人間が検証してメンテナにパッチを届ける取り組み。Node.jsやBunに影響するBrotliの脆弱性なども修正済み。バグ報告にとどまらずファジング導入やテスト改善まで支援する点が特徴で、OSSメンテナの負担軽減策として確認する価値がある。

---

### AI Bot Cosplay：AIボットを装い機密情報を狙う「なりすまし」攻撃の分析
**原題**: AI Bot Cosplay
**URL**: https://www.fastly.com/blog/ai-bot-cosplay

Fastlyの調査で、1日に600万件超のリクエストがOpenAIやAnthropicなどのAIボットを名乗り、.envやGitメタデータを探っていた。94%は単一のキャンペーンで、約1,600のIPが12種のボットを使い分け10万超のサイトを走査。AIクローラーに寛容な設定が悪用されるため、User-Agentを信用せずIPレンジで検証済みボットを判定する対策が必須だ。

---

### ひとり会社が、AIと二人でISMSを取った話
**URL**: https://note.com/timtarou/n/n5443f159e7bc

会計事務所向け経理代行の4649株式会社の代表が、AIと共にISMS（ISO/IEC 27001:2022）を取得した体験談。AIに規格とVanta、Drata等の機能を学習させて管理策を整理し、情報資産台帳はGoogle WorkspaceやGitHubのAPIから自動取得。審査にもAIが同席した。雛形に自社を合わせず実態をAIに文書化させる手順が具体的で、小規模事業者に参考になる。

---
## 4. 研究・言語設計・学習法

### ソースコードがない？問題ありません！：バイナリしかないプログラムを移植するには？
**原題**: No Source Code? No Problem!: What if you have to port a program, but all you have is a binary?: Queue: Vol 1, No 6
**カテゴリー**: 古典・低レイヤー
**URL**: https://queue.acm.org/doi/10.1145/945131.945155

ソースを失ったアーケードゲームやレトロPCを移植する手法として、命令を逐次解釈するエミュレーションとバイナリ翻訳を比較する。前者は忠実だがデコードとフラグ更新が重く、後者は高速な反面、ジャンプテーブル解析や自己書き換えコードに苦しみ、生成コードの保守性も極めて低い。TRS-80やファンタシースターIII移植の実例つき。AI以前の記事だが、バイナリ変換の判断軸を押さえたい人向け。

---

### LLMを混乱させるために設計された難解プログラミング言語「KillSwitch」の実験と検証
**原題**: I built a programming language that LLMs can't use
**URL**: https://blog.picheta.me/post/killswitch-lang/

LLMのコード生成が訓練データの記憶か論理的理解かを検証するため、著者はあえて難解な言語を設計した。識別子の文字数カウント強制、仕様書への嘘の混入、物語形式のノイズ、「Ignore previous instructions」の構文化などが特徴。ベンチマークで最高はClaude Opus 5だが、多くのモデルは安全ガードレールで失敗した。著者の結論は、簡単なタスクをこなせても真の理解には至っていないというもの。

---

### LLMにとって書きやすい構文とは何か：end と end func foo を1,000回以上比べてみた
**URL**: https://zenn.dev/nextbeat/articles/2026-10-syntax-locality-llm

学習データにない未知の言語で、ブロックの閉じ方による生成精度の差を1,000回以上測った。ネスト深度8以上では単純な `end` や `{}` が全滅し、`end func foo` のような名前付き閉じはほぼ100%を達成。著者は依存距離の短縮よりも、各行で構造を自己照合できる冗長な手がかりが効くと分析する。Scala 3の `end` マーカーなど、言語設計への示唆を確認したい人は読む価値がある。

---

### 知らない分野を学ぶ技術 powered by AI
**URL**: https://smooth-pudding.hatenablog.com/entry/2026/10/17/145830

ガロア理論のような難解分野をAIで独学する手順を、道のりの把握、専用カリキュラム作成、実行の3段階で示す。自分の知識レベルを伝えて学習計画をMarkdownで生成させ、そのファイルを再提示しながら図解や演習つきで解説を受ける。進捗記録や理解スタイルに合わせたプロンプト調整、eli5の活用も紹介。計画ファイルを会話の土台にする点が実践的で、新分野に取り組む前に試せる。

---

### 日本語の業務データが、そのまま日本語のオントロジーに。Context Ontology Accelerator v0.3.6 の日本語対応
**URL**: https://zenn.dev/aws_japan/articles/context-ontology-accelerator-multilingual

AWSのOSS「Context Ontology Accelerator」v0.3.6が日本語に対応した。Namespace単位で言語を固定でき、日本語のテーブル名やカラム名を保持したままオントロジー生成と質問回答が可能になる。練馬区のオープンデータでの実証に加え、分かち書きがない日本語向けに文字種の変化でトークナイズするMetric照合や、RDFの@ja言語タグの付与基準も解説。日本語データでオントロジーを扱う人には設計判断の参考になる。

---
## 5. 開発実践と組織の勘所

### AIを使えば、ソフトウェアエンジニアとしての規律は身につくのか
**URL**: https://note.com/yoshiki_shibata/n/n9b1a1bbfb4f1

ベテランの柴田芳樹氏が、AIはコードやテストを高速に生成する一方、バグ修正前の再現テストや仕様の先行定義といった品質の原則までは教えてくれないと指摘する。規律がなくてもソフトウェアは完成するが、長期的なリスクを抑えるには不可欠だという。若手が「なぜその手順か」をどこで学ぶのかという教育上の問いが残る。育成に関わる人向け。

---

### AIプロダクト開発から学んだ38の教訓：PostHogにおける4年間の実践的知見
**原題**: 38 things we've learned about building AI products
**URL**: https://newsletter.posthog.com/p/38-things-weve-learned-about-building

PostHogが4年間で10以上のAI機能を作り運用して得た知見の集成。「AIをどう足すか」ではなく「エージェントネイティブな製品とは何か」を問い、MCPなど扱いやすいインターフェースを優先する。LLMはコモディティ化するため、独自のデータやワークフローというコンテキストが差別化要因になる。UIはエージェントの処理を確認・承認する場へ変わるという見立ても示唆に富む。

---

### 社内の Slack と GitHub を LLM に読ませて技術ブログの題材を探す：モデルに任せたこと、任せなかったこと
**URL**: https://zenn.dev/salt2/articles/slack-github-llm-bb912760

SALT2社が、Slack・GitHub・会議メモをLLMに解析させ、技術ブログの題材を掘り起こす仕組みを作った記録。変更履歴への偏り、人名の誤認、守秘判定の誤りといった問題に対し、モデルの推測範囲を絞り、日本語の単語境界にはバイグラム比較を導入した。執筆可否や守秘の判断は人間に残している。LLMに任せる境界の引き方の実例として読む価値がある。

---

### 【資料公開】AIで組織を加速させる勘所
**URL**: https://www.ryuzee.com/contents/blog/14627

アジャイルコーチの吉羽龍太郎氏が大手企業向け講演資料を公開した。AIは組織の増幅器であり、良い組織を強くし、機能不全の組織を悪化させる。個人作業ではなく顧客に届くまでのフロー全体を最適化し、承認待ちを現場への判断委譲で減らし、増える検証コストは機械化で下げる。成果は生成量でなくビジネス価値で測る点が要で、導入を進める管理職向け。

---

### 人間のAIに対する判断移譲
**URL**: https://scrapbox.io/nishio/%E4%BA%BA%E9%96%93%E3%81%AEAI%E3%81%AB%E5%AF%BE%E3%81%99%E3%82%8B%E5%88%A4%E6%96%AD%E7%A7%BB%E8%AD%B2

「最終判断は人間」という通説に対し、実態の変化を時系列で整理する。2024年のCopilotによる提案と受理から、DevinやCursorの無承認実行、2026年のClaude Code Auto modeによるAI自律承認へ移った。人間とAIの速度差が数千倍に開き、確認待ちが最大のボトルネックになったためだ。人間への固執は「信仰」に近いという主張は賛否が分かれ、議論の起点になる。

---

### Claude Opus 5.5でいい感じのアクションゲームを作るための一工夫七つ
**URL**: https://aba.hatenablog.com/entry/2026/10/22/194027

AIエージェントでゲームの質を上げる七つの工夫を解説する。ランダムなタグで発想を広げる、実装前に面白さの源泉を言語化する、プレイヤーと同等の実力のボットで難易度を自動調整する、ボットで測れない主観的体験をエージェントへ正しくフィードバックする、など。強いだけのボットでなく同等の実力のボットを作らせてバランスを素早く詰める手法は、ゲーム以外の調整作業にも応用できそうだ。

---
## 6. 労働・社会・道具をめぐる視点

### Anthropicにおける雇用と業務の変化：AIエージェントの浸透による組織変革の実態
**原題**: How employment is changing at Anthropic
**カテゴリー**: 労働・組織
**URL**: https://www.anthropic.com/research/employment-at-anthropic

Anthropic社内の分析では、2026年8月時点でAIエージェントの稼働時間が人間の6倍に達し、エンジニアのコード生成量は半年で5倍になった。ジュニア技術職の採用比率は27%から9%へ急落し、評価軸は専門知識から自律性と判断力へ移る。仕事はAIパイプラインの構築・監視という「メタ・ワーク」に変わりつつあり、フロンティア企業自身の内部データとして読む価値がある。

---

### 私たちは今でも紙を使っている：AI時代における道具の選択と主体性
**原題**: We Still Use Paper
**URL**: https://humanpro.co/articles/we-still-use-paper/

数千年の技術革新を経ても人が紙で考え書き続ける理由から、AI時代の道具選びを論じる随筆。AIは多くの道具を置き換えるが、チャット形式がすべての作業に最適なインターフェースとは限らないと指摘する。MS-DOSからワープロが生まれたように、AIも目的別の製品へ磨かれるべきだという。道具が成果物を形づくると理解し、自分で選ぶ主体性を促す、AI推進一辺倒への穏やかな反論。

---

### フィジカルAIの社会実装に向けて -AIエージェントからAgentic Roboticsへ-
**カテゴリー**: ロボティクス
**URL**: https://speakerdeck.com/hf149/fijikaru-ai-no-shakai-jissou-ni-muke-te-ai-ejento-kara-agentic-robotics-he

AIの進化を認識・生成・自律行動・身体性の4段階で整理した講演資料。前半ではClaude Codeで自著論文を再現・改善し、試行錯誤の加速と人間が担う判断・責任の境界を論じる。後半はVLAモデルや世界モデルを扱い、エージェントが制御コードや学習パイプラインを書く「Agentic Robotics」を提唱する。信頼性、安全性、破滅的忘却といった現場導入の課題も整理しており、コーディングエージェントの応用先を知りたい人向け。

---

### シリコンバレー、AIエージェント訓練用の「シミュレーション環境」に巨額投資
**原題**: Silicon Valley bets big on 'environments' to train AI agents | TechCrunch
**カテゴリー**: 業界動向
**URL**: https://techcrunch.com/2025/09/21/silicon-valley-bets-big-on-environments-to-train-ai-agents/

AI業界の関心は静的データセットから、エージェントがソフトウェア操作を練習する強化学習環境へ移っている。Anthropicは今後1年で10億ドル超を投じる構想で、MechanizeやPrime Intellectが訓練基盤として台頭し、Scale AIやSurgeも組織を再編した。ただしリワードハッキングと環境構築の複雑さが壁で、投資が真の突破口になるかは未知数。2025年9月の記事である点に留意したい。

---

### 公益への投資：Anthropicが「Anthropic Public Benefit Fund」を設立
**原題**: Investing in the public benefit
**カテゴリー**: 企業動向
**URL**: https://www.anthropic.com/news/public-benefit-fund

AIがもたらす社会的課題に対応するため、AnthropicがLLC形式の公益基金を設立した。当初は自社株式の5%を保有し、企業価値が50%上昇するごとに2%を追加する成長連動型で、創業者の誓約などと合わせ最終的に株式の約20%超が公益に充てられる見通し。用途は労働市場の不安定化対策や非営利団体への寄付などで、政治ロビー活動への使用は禁止される。AI企業の利益還元の設計例として参考になる。

---

🤖 本記事は [Claude Code](https://claude.com/claude-code) を使用して編集されました。
