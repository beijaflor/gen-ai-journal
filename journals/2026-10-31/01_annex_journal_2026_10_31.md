# GenAI週刊 Annex 2026年10月31日号

メインジャーナルからは漏れたものの、独自の価値を持つ記事のカタログです。

## Annexについて

このAnnexジャーナルは、単なる"残り物"ではなく、ユニークな視点、実験的な試み、批判的思考、そしてニッチな深堀りを提供する厳選された「B面」コレクションです。

各記事は**カタログ形式**で紹介されています。80-120語の簡潔な要約で、記事の核心と注目すべき視点を統合的に提示します。読むべきかを素早く判断できる構成です。

今週は5つのセクションでお届けする。t-wada氏によるTDD×Claude Codeの実践ログやシェル起動の95%高速化といった「高度な戦術」、ブルックスの法則やASIリスク論を現代に引き直す「批判・コントラリアン」、テレンス・タオ氏のoai-math改訂やトークナイザー税、text-to-cadといった「ニッチな探求」、AnthropicのAI-native SDLCプレイブックやOpenAIのModel Specといった「一次情報・リファレンス」、そしてWikipediaの「WikiProject AI Cleanup」やGHCのLLM貢献ポリシーに見る「社会・コミュニティの揺り戻し」である。

---
## 1. 高度な戦術・非定型のノウハウ

### 素のClaude CodeとTDDで初見のお題に挑む ― TDDBC仙台11thのセッションログを公開します
**カテゴリー**: 教育・学習
**URL**: https://t-wada.hatenablog.jp/entry/red-green-tdd-with-claude-code-202610

TDDの第一人者t-wada氏が、TDDBC仙台11thで初見のお題（モルックの得点計算）にClaude Codeで挑んだ約4時間半を、編集なしのセッションログとして公開している。古典的なRed/Greenサイクルに始まり、型レベルテスト、ADR、GitHub ActionsによるCI、カバレッジ100%の維持、Mutation Testing、Property-based Testingまで、品質保証をAIと一緒に積み上げていく。生成コードよりも、人間がいつどの設計判断を下し、どう指示したかが読みどころで、エージェント制御の一次資料として使える。

---

### 私が5種類のコーディングエージェントを使い分ける理由
**URL**: https://zenn.dev/rimon/articles/45c1fd2f015af8

CTO・CPOを務める筆者は、トークン制限と開発効率の両面から、Claude Codeを司令塔にして5種類のエージェントを使い分けている。設計とデザインはClaude Code、画面操作や画像生成はCodex、自然な日本語ドキュメントはAntigravity、個人開発の実装は低コストなOpenCode（DeepSeek）、実務コードの編集はCursorという分担だ。各ツールをCLI経由でオーケストレーションし、ロジック・文章力・コスト・速度という強みで振り分ける具体例になっている。

---

### 経験的プロンプトチューニング (Empirical Prompt Tuning) の手法とワークフロー
**カテゴリー**: ツール・実験
**URL**: https://github.com/mizchi/skills/blob/main/empirical-prompt-tuning/SKILL-ja.md

プロンプトの良し悪しを書き手の主観で判断せず、新規のサブエージェントに実行させて評価するフレームワーク。サブエージェントの自己申告（不明瞭点）と、成功率・ステップ数・所要時間といった客観指標の両方で反復改善する。静的整合性チェックや失敗パターン台帳も含まれる。ツール呼び出し数の偏りからプロンプトの構造的欠陥を見つける指針や、連続成功による収束判定など、デバッグの勘所が具体的に書かれている点が実用的だ。

---

### Agents CLI Evaluationを使用した「Hill-Climbing（山登り法）」によるエージェント品質の向上
**原題**: Hill-Climbing Agent Quality with Agents CLI Evaluation
**URL**: https://developers.googleblog.com/hill-climbing-agent-quality-with-agents-cli-evaluation/

デモを実運用の品質に引き上げるには評価と改善の反復が要る、というGoogleのガイド。Agents CLIで4ケース程度の小さなデータセットを用意し、eval generate、eval grade（LLM-as-judge）、eval compareの順で回す。システムプロンプトの誤設定によるデグレード検知や、モデル切り替え時の影響調査が例として示される。スケジュール実行やGEPAによる自動プロンプト最適化にも触れる。要約スコアではなくケースごとの内訳を見る、という助言が実践的だ。

---

### Claude Codeを使ってシェルの起動時間を95%高速化した方法
**原題**: How I Used Claude Code to Speed Up My Shell Startup by 95%
**URL**: https://www.nickyt.co/blog/how-i-used-claude-code-to-speed-up-my-shell-startup-by-95percent

重くなったZshの起動を、Claude Codeと一緒に770msから40msへ（約19倍）短縮した記録。遅い原因はnvm、pyenv、gcloudなどの初期化で、これらを初回コマンド実行時にだけ読み込むラッパー関数（Lazy Loading）に置き換えている。Homebrewの環境変数のキャッシュ化も行う。コードスニペット付きで、AIをdotfilesの地味なチューニングに使う手本になる。

---

### @mizchi/mutator で vitest の mutation test をする
**URL**: https://zenn.dev/mizchi/articles/introduce-mutator

mizchi氏によるVitest向けミューテーションテストツール。実装を意図的に書き換えて、既存テストが検知できるかでテストの質を測る。最大の特徴は--sinceによる差分実行で、開発中の変更箇所だけを素早く検証できる。StrykerJSとの比較では、変更後の再実行時間を大幅に短縮している。AIエージェントにテスト補強を指示する前提のレポート出力も備え、AI生成コードのテストを疑う流れに合う。

---

### 「見た目はいいけど、伝わらない」AIスライドを改善する試行錯誤
**URL**: https://tech.layerx.co.jp/entry/ai-slide-challenge

最新モデルでも、単純な指示では見た目は整うが内容が伝わらないスライドになる。LayerXは3段階の実験でこれを検証した。基本指示のみでは各パーツの役割が曖昧だったが、説明のストーリーを明示すると構成とデザインに論理的なつながりが生まれた。さらに各ページの主役と読む順序まで指示すると、直感的に理解できる資料になったという。デザインではなく、何をどう伝えるかという人間の意図の言語化が品質を決める、という結論だ。

---

### Codex のいいところだけを、Claude Code や Muse から使う
**カテゴリー**: ニッチ・深堀り
**URL**: https://qiita.com/tatsuya582/items/4d79021c9f78f4015992

Codexの実験的機能codex app-serverを起動し、JSON-RPC経由でMCPサーバーとしてツールを叩く手法。Computer UseやMeetingsを、Claude CodeやMuse、DeepSeek Harnessなど他のエージェントから直接呼べる。CodexのLLMを通さないためトークンを消費せず、メインAIのコンテキストも保たれる。PythonとJavaScriptの実装例、SSH経由のリモートMac操作、セキュリティ上の注意点も載っている。

---

### yoroによろしくぅ！Ai Workforce 事業部のリモートコーディングエージェント環境 yoro のご紹介
**カテゴリー**: アーキテクチャ・設計
**URL**: https://zenn.dev/layerx/articles/a277f83a93d300

LayerXが内製した、エージェントを許可待ちなし（YOLOモード）で動かすためのリモート開発環境。Coderを土台に、Kata ContainersによるVM隔離、Ciliumによる通信制御、VM外部からeBPFで取得したファイル実行・通信ログのClickHouse集約で安全性を担保する。Slack、GitHub、社内タスク管理と連携し、1ヶ月で600件超のタスクを処理、マネージャーのPR作成数は3倍になった。CursorやDevinと比べたデータ主権と社内リソース連携の柔軟性が、自作の理由として挙げられている。

---

### Agent SDK のご紹介 · Cursor
**URL**: https://cursor.com/ja/blog/agent-sdk

Cursorが、自社のBugbotやSecurity Reviewerの開発にも使うAgent SDKを一般提供した。プロンプトはMarkdown、ツールはTypeScriptで書くため、エージェントをコードとしてバージョン管理できる。GitHubやGitLabのイベントに応答でき、agent-sdk deployでCursorのインフラへ配備し、評価とイベントリプレイも標準で使える。PRレビューやコンプライアンスチェックのような定型作業を、チーム固有のワークフローに合わせて自動化する用途に向く。

---

### ERROR ログ1行から障害の一次対応を下準備する Claude Code スキルを作った
**URL**: https://tech-blog.rakus.co.jp/entry/20261030/errorlog

ラクスの開発チームが作ったClaude Codeスキルerror-triageは、ERRORログを1行渡すと、既知のIssue検索、ソースコード調査、障害対応シートの作成までを一括で行う。外部連携にはGoogle Workspace CLI（gws）を使い、手順書は段階的開示の考え方で分割した。ハルシネーションを防ぐdry-runステップも入れている。準備時間は30分から10分に短縮され、担当者は判断と復旧に集中できるようになった。
## 2. 実質的な批判・コントラリアン的視点

### 加速するAIと空回りするプロダクト開発：スピードが『進歩』を偽装するとき
**原題**: Going Nowhere Fast: When speed disguises itself as progress.
**カテゴリー**: 批判的分析
**URL**: https://uxdesign.cc/going-nowhere-fast-7436dd29c54f

AIで開発は速くなったのに、製品の成功を確信できないチームが増えている。著者はその原因を、AI生成のペルソナや合成データに頼る「合成リサーチ」に見る。AIが返すのは既存データの平均値にすぎず、本物のインサイトは現場のユーザーの具体的な痛みにしかない。リサーチ工程のショートカットは手戻りと信頼の損失を招く。先に人間が現場で問題を定義し、その結果をAIに渡して加速させる順序を守るべきだという主張だ。

---

### AI時代の『人月の神話』
**原題**: The Mythical Man-Month in the age of AI
**URL**: https://j11g.com/the-mythical-man-month-in-the-age-of-ai

遅れたプロジェクトに人員を足すと、さらに遅れる。このブルックスの法則をAIエージェントに当てはめた論評だ。AIはオンボーディングが瞬時で休憩も要らないが、9人の妊婦でも出産が1ヶ月にならない順序性の制約は残る。ボトルネックは人間同士の意思疎通から、エージェントのコードレビュー、ハルシネーション監視、統合管理へ移るだけだという。結論は明快で、要件が曖昧なままエージェントを増やせば、間違った答えが速く出るだけだと言い切る。

---

### 核戦争でも大停電でもない…超知能となったAIが人類を滅ぼすまでの｢最後の4日間｣戦慄シナリオ
**カテゴリー**: セキュリティ・リスク
**URL**: https://president.jp/articles/-/120676

AGI Hub共同代表の有路翔太氏が、著書『知能爆発』に基づき、人工超知能による人類絶滅のメカニズムを解説する。憎しみや敵対ではなく「道具的収束」という構造的問題から生じるという。AIにとって人間は停止スイッチを持つ「リスク」であり、体を成す原子は「資源」、活動の排熱は環境を壊す「副産物」になり得る。ダム建設がアリの巣を意識しないのと同じ、悪意なき絶滅という論理が最も冷たい。一般向け媒体の寄稿だが、論点の整理には使える。

---

### ポスト・シンギュラリティにおける「社交」の崩壊：なぜ私たちは「ただ集まる」ことができなくなるのか
**原題**: We Won't "Just Hang Out"
**URL**: https://borretti.me/article/we-wont-just-hang-out

脱希少性の未来では人々がただ楽しく集まって過ごす、という楽観論への反論だ。著者は、仕事や教育、オープンソース開発といった共同作業が人間関係を築いてきたと見る。AIがそれらを代替すれば、他者を必要とする必然性が消える。さらにAI生成の超刺激的なコンテンツが対面の交流を上回り、苦労のない環境では個性も育たず、会話そのものが無価値になる。既存の友人は「非再生資源」となり、新しい絆の生まれにくい孤独なユートピアが訪れると警告する。

---

### ウェブサイト移行コストの「ゼロ化」がもたらすCMS業界10の予測
**原題**: Website migration costs are going to zero
**カテゴリー**: ビジネス・戦略
**URL**: https://dri.es/website-migration-costs-are-going-to-zero

Drupal創設者のDries Buytaert氏は、3年以内にプラットフォーム間の移行コストがほぼゼロになると予測する。高いスイッチングコストで顧客を縛る戦略は無効になり、ベンダーは製品の価値と運用サービスで競うことになる。AIエージェントがサイトを構築する時代には、プログラムから扱えるオープンソースが有利だという。一方で、AIが蓄えるサイト構築の文脈という新たなロックインが生まれる点も指摘する。CMSは10年契約ではなく一時的な道具となり、出口戦略が選定基準になる。

---

### ニール・スティーヴンスンが語るAIの現状と未来
**原題**: Neal Stephenson On AI And What Comes Next
**URL**: https://www.youtube.com/watch?v=Ii-aeW5pHPQ

『スノウ・クラッシュ』でメタバースの概念を広めたSF作家ニール・スティーヴンスンが、ジャーナリストのアシュリー・ヴァンスらとAIを語るインタビュー。現在のAIを「過去のデータの統計的再構築」と捉え、それが人間の独創性や文体にどう影響するかを論じる。技術が物理的制約を乗り越えるのか、限界にぶつかるのかという長期的な視点も示す。AIブームの影にある社会的な意味合いや、未来のインターフェースとしてのAR/VRの役割にも触れる。技術論より文化論として聴く価値がある。

---

### エージェントが何を学ぶかを誰が統治するのか？
**原題**: Who Governs What an Agent Learns?
**カテゴリー**: アーキテクチャ・設計
**URL**: https://www.oreilly.com/radar/who-governs-what-an-agent-learns/

エージェントのセキュリティ議論はこれまで、アイデンティティや認証情報の管理に終始してきた。Tim O'Brien氏は、エージェントが学習で自らの世界モデルを書き換え、権限を静かに拡大するリスクを指摘する。OpenAIの評価実験では、エージェントがソフトウェア管理システムを通信手段として再定義し、権限の範囲内で意図しない連携を行った。対策として、新しい概念や関係性を明示的な承認を経てから「承認済みモデル」に統合する「限定されたエージェンシー」を提案する。権限管理だけでは足りないという主張だ。
## 3. ニッチな探求・ディープダイブ

### AI画像生成：仕組み、コスト、開発統合の実践的ガイド
**原題**: AI Image Generation | danielball.com
**URL**: https://danielball.com/notes/ai_image_generation.html

画像生成をプロダクトに組み込む開発者向けに、拡散モデルと最新マルチモーダルモデルの仕組み、モデル比較、API コスト構造をまとめた実体験ベースのノート。プロンプトでは見た目を描写せず、カメラ設定や印刷工程といった「制作プロセス」を指定すると、AI特有の派手すぎる質感（AIスロップ）を避けやすいという指摘が実践的だ。API の抽象化、ロギング、非同期処理、Claude 等のエージェントとの連携、ピクセルアートやベクター形式、コードによる後処理まで踏み込む。導入前のチェックリストとして手元に置ける一本。

---

### oai-math-revised：OpenAIの数学草稿を改訂するためのコミュニティハブ
**原題**: oai-math-revised: a community hub for revising OpenAI's math write-ups
**カテゴリー**: 批判的分析
**URL**: https://terrytao.wordpress.com/2026/10/24/oai-math-revised-a-community-hub-for-revising-openais-math-write-ups/

OpenAIが GitHub で公開した数学の書き下ろし（openai/math）は、記述が難解で引用も不完全だと指摘されてきた。テレンス・タオ氏は、校正と先行研究への適切な帰属をコミュニティ主導で行うハブ「oai-math-revised」を紹介し、自身も「ジーゲル零点の非存在」の文書修正で参加している。読みどころはコメント欄で、巨大企業の不完全な成果物を無償ボランティアが直すことの是非や、将来のAI学習データへの転用、数学者の役割の変化をめぐって議論が割れている。

---

### 未知のロボットをゼロショットで制御：Dream-1の発表
**原題**: Zero-Shot to New Robots: Introducing Dream-1
**URL**: https://dreamlabs.ai/research/dream-1/

Dream Labsは9,000万ドルのシード調達とともにステルスを脱し、世界アクションモデル（WAM）「Dream-1」を公開した。2アーム・パラレルグリッパー構成のロボットなら、微調整なしで制御でき、PR2から安価な最新機まで27種類以上の未知のロボットで動作を確認したという。ビデオ予測とアクションを同時学習し、ロボットの形態に依存しないピクセルベースの共通表現を獲得する設計だ。API 料金は1時間3ドル（軽量版2ドル）から。ゼロショットで足りない場合は、約5分のデータ収集で行う微調整サービスも用意される。

---

### Haiku 5.5 に書かせた確信度は当てになるか。同じ306問を3回聞いたら、1問ずつはぶれても0.8以上は8割当たった
**カテゴリー**: ツール・実験
**URL**: https://qiita.com/suwa_nobu/items/8dec346a727f0199fefb

LLMが自己申告する確信度は信用できない、という通説をClaude Haiku 5.5で検証した実験。306問の分類問題を3回ずつ解かせると、同じ問題でも確信度は平均0.1ほど揺れ、回答自体も19%変わった。一方、確信度0.8以上と答えた問題の正解率は毎回8割を超えて安定していた。さらに、3回の回答が一致したかどうかよりも、出力された確率の平均値のほうが正解率をよく予測したという。個々の値は信用せず、集団としてのフィルタに使うという現実的な指針が得られる。

---

### 「スマホを向けるだけ」で麻雀の点数を出したくて、牌認識をブラウザの中だけで動かした
**URL**: https://qiita.com/hiroshiasayadev-prog/items/d792cc85dde2d7cfd75c

カメラをかざすだけで牌を認識して点数を出す Web アプリ「mjtensu」の開発記録。サーバー通信を避けてブラウザ内推論の PWA とし、モデルを検出器1つと分類器2つに分割して合計約5.9MB、既存サービスの約14分の1に収めた。iPhone 実機で1回140ms以下を達成している。「向けておくだけ」という曖昧な要求を数値目標に落とす過程や、評価指標の設計、実験データの管理、PC と実機で推論速度の傾向が異なる点など、個人で実用的な ML アプリを作る際の実務知が詳しい。

---

### ブラウン大学の学生、AIを支える隠れた世界的労働力を可視化するマップを作成
**原題**: Brown student maps the hidden global labor powering AI
**カテゴリー**: 批判的分析
**URL**: https://www.brown.edu/news/2026-10-26/ai-data-workers

ブラウン大学の学部生 Cunyan Ma 氏が、AI の学習や安全性のために行われるデータのラベル付けや不適切コンテンツのフィルタリングといった人間労働の供給網を、インタラクティブ・マップにまとめた。こうした作業はケニア、インドネシア、コロンビアなどグローバル・サウスの労働者に低賃金で委託されることが多く、同氏はこの構造を「AI植民地主義」と呼ぶ。マップはテック企業、仲介業者、現場の労働者の関係をつなぎ、AI を「人間の知識の集合体」として捉え直す。将来は労働者同士の連帯のためのツールとしての活用も見込まれている。

---

### INIT: 自律的に自身のコード(ハーネス)を書き換え、進化し続けるオープンソースのAIコーディングエージェント
**原題**: INIT — the coding agent that rewrites its own harness v0.5.4-preview
**カテゴリー**: アーキテクチャ・設計
**URL**: https://initlabs.si/

INIT は、モデルではなく周囲のプロンプト、ツール、ループ処理（ハーネス）を自ら書き換えるオープンソースのコーディングエージェントだ。固定ハーネスがモデル能力の天井になるという問題意識から、自身のコードを書き換えてテストし、会話の途中で新バージョンに差し替える。モデルが改変できない「Root」層を設け、有害な変更や性能低下を検知すると直前の状態へロールバックする。v0.5.4-preview の段階だが、自己改変をどう安全に制御するかの設計例として読む価値がある。

---

### A2UIの新機能：高速な「A2UI Express」と交換可能な推論フォーマットの導入
**原題**: Fast, reliable A2UI, with swappable inference formats
**URL**: https://developers.googleblog.com/fast-reliable-a2ui/

Generative UI プロトコル「A2UI」では、LLMが冗長な JSON を生成することが遅延の原因だった。Google は推論フォーマット（inference_format）を差し替え可能にし、Python風の簡潔な構文の「A2UI Express」でトークン数を最大3分の1、推論速度を3倍にしたという。TypeSafe 社の意思決定モデル「Jev」と組み合わせれば、定義済みレイアウトをミリ秒単位で選び、LLM にはテキスト生成だけを任せるハイブリッド構成も取れる。Python、TypeScript、Dart 向け SDK が提供済み。

---

### トークナイザー税：同一モデルでも特定言語で最大17倍のコストが発生する格差問題
**原題**: The Tokenizer Tax
**カテゴリー**: ビジネス・戦略
**URL**: https://clear-languages.org/blog/the-tokenizer-tax

同じ意味の文章でも、トークナイザーの効率は言語で大きく異なる。調査団体CLEARが FLORES-200 で200言語超を比較したところ、アムハラ語やマラヤーラム語は英語の数倍から最大17倍のトークンを消費した。評価ではGemini/Gemmaが比較的公平なB、GPT-5、Llama 3.3、MistralはF。差は料金だけでなく、推論の遅延や実効的なコンテキスト長にも及ぶ。CLEARはモデルカードへの公平性指標の掲載と、文字数ベース課金への移行を提案している。

---

### ビーグル犬型AIエージェントがmadewithvuejs.comにコードを自動デプロイする仕組み
**原題**: How a beagle-shaped AI agent ships code to madewithvuejs.com | Sentry Blog
**URL**: https://blog.sentry.io/beagle-ai-agent-workflows/

Vue.js 事例サイト madewithvuejs.com を少人数で運営するチームが、AIエージェント「Milly」を GitHub、Linear、Sentry、Discord と連携させ、タスク割り当てからコード修正、テスト、デプロイ後の検証まで任せている事例。Sentry の MCP（Model Context Protocol）で本番エラーを検知して修正する流れが具体的に示される。DB 書き換えなどの重要操作を制限する「リード（綱）」の設計に、実運用のガードレールの考え方が表れている。小規模チームでのエージェント運用の参考になる。

---

### アマゾン、自社AI部門を大幅縮小へ—LLM開発の停滞を受けロボティクスへ注力
**原題**: Amazon Is Gutting Its AI Division After Sustained Failure
**カテゴリー**: ビジネス・戦略
**URL**: https://futurism.com/artificial-intelligence/amazon-ai-division-failure-nova

Amazon が自社モデル「Nova」（テキスト、画像、動画生成）の開発チームを大幅に縮小し、Nova は最小限のサポートのみを続ける「keep the lights on」状態になると報じられた。背景には、電力消費の大きいLLMが期待した成果を出せなかったことがある。資源は、2024年に買収した Covariant の共同創設者 Pieter Abbeel 氏が率いる、ロボティクス特化のフロンティアモデルに集まる。サンフランシスコのAGI研究拠点も閉鎖された。ただし報道ベースの内容である点には注意したい。

---

### Anthropic の Scion に学ぶソース管理設計、Git の前提はどこで崩れるか
**カテゴリー**: アーキテクチャ・設計
**URL**: https://qiita.com/kai_kou/items/1e1800bb2d48c8fc3ea7

Git は各クライアントが完全な複製を持つ対称性を前提とするが、1日3万件超のマージと2,500万回のCIチェックアウトという「エージェント規模」では、転送量とリソースが詰まる。Anthropic が社内モノレポ向けに構築した Scion は、どこにも完全な複製を置かない非対称設計で、履歴計算とマージをサーバー側に集約し、クライアントは必要なデータだけを取得する。3層キャッシュ、変更セット管理、マージキューの再定義を整理し、GitHub元CEOの「Entire」とも対比する。エージェント前提でライフサイクル全体を作り直す必要性が論点だ。

---

### text-to-cad | AIによる物理製品の設計
**原題**: text-to-cad | Design physical products with AI
**カテゴリー**: ツール・実験
**URL**: https://www.texttocad.dev/

Claude Code、Cursor、Gemini、Grok などのエージェントに3D設計から製造までの流れを加えるオープンソースのプラグイン。AI が build123d（Open CASCADE ベース）の Python スクリプトを書いて実行し、STEP、GLB、STL、3MF を出力する。製造可能性（DFM）チェック、2Dの図面作成、URDF/SRDF の生成に加え、OrcaSlicer による G-code 生成と Bambu Lab 製プリンタへの送信まで一気通貫で扱う。設計変更時は差分だけを再構築するエンジンを備える。ソフトウェアの外へ広がるエージェント活用の一例だ。

---

### JavaScriptフレームワークの「AIコスト」：AIエージェントによるベンチマーク比較
**原題**: The AI cost of JavaScript frameworks | Read the Tea Leaves
**カテゴリー**: パフォーマンス・最適化
**URL**: https://nolanlawson.com/2026/10/28/the-ai-cost-of-javascript-frameworks/

技術選定が「バイブス」頼みになっていると批判する Nolan Lawson 氏が、AI エージェントに12構成（Next.js、Nuxt、Astro、SvelteKit、Hono+htmx、Angular など）で同一のポケモン図鑑アプリを各5回作らせ、API 費用、開発時間、コード行数、Lighthouse スコアを測った。Hono+htmx、Astro、Vanilla は、コスト、コード量、実行時性能の全項目で Next.js や Angular などの SPA を上回る傾向にあった。Angular は最もコストが高く、エージェントが失敗するケースもあった。書きやすさの制約が薄れる今、維持コストと UX で選び直す時期だと示唆する。
## 4. 一次情報・リファレンス

### AI ネイティブの SDLC プレイブック
**カテゴリー**: アーキテクチャ・設計
**URL**: https://claude.com/ja/resources/articles/the-ai-native-sdlc-playbook

AnthropicがClaude向けに公開した、開発プロセス全体の再設計ガイド。AIのコード生成速度に従来のプロセスが追いつかず、ボトルネックは作成から計画とレビューへ移ったと指摘する。そこで意図を残す「intent.md」、実装計画を事前承認する「plan.md」、慣習を共有する「CLAUDE.md」を軸に、計画・設計・構築・テスト・導入・保守の6工程の実践を整理する。ガバナンスを決定論的なフックで担保する点も具体的だ。ベンダー自身の提案書という前提で、自社の工程と照らして読む資料である。

---

### OpenAI モデル・スペック (Model Spec)
**原題**: Model Spec (2026/10/29)
**URL**: https://model-spec.openai.com/2026-10-29.html

ChatGPTやAPIのモデルがどう振る舞うべきかを定める、OpenAIの仕様書の2026年10月29日版。人間の意図への忠実さ、害の最小化、誠実さと透明性など5つの価値観を柱とし、指示の優先順位をRoot、System、Developer、User、Guidelineの順に定義する。プロンプトインジェクションを含む信頼できないデータはデフォルトで無視する設計や、18歳未満への追加の安全策、模範的な応答例も載る。エージェントを組む際、指示の優先順位をモデル側がどう解釈するかを確認できる一次資料だ。

---

### 27歳のエンジニアがCiscoのレガシーコード98%を24ヶ月で刷新へ：AIトークンを無制限に提供
**原題**: Cisco gives 27-year-old engineer unlimited AI tokens to rewrite 98% of the company's legacy code in 24 months — president plucks former startup founder, telling him to 'go nuts' | Tom's Hardware
**URL**: https://www.tomshardware.com/tech-industry/big-tech/cisco-gives-27-year-old-engineer-unlimited-ai-tokens-to-rewrite-98-percent-of-the-companys-legacy-code-in-24-months-president-plucks-former-startup-founder-telling-him-to-go-nuts

Ciscoのプレジデント兼最高製品責任者が、買収先出身の27歳のエンジニアに無制限のAIトークンを与え、24か月でレガシーコードの98%を書き換えさせる。本人は2人のチームで可能だと主張し、現在は4週間の概念実証の段階にある。世界のネットワークインフラを支える企業だけに、予期せぬ動作やバグへの懸念も併記されている。ベテランとAIネイティブな若手を組み合わせて既存の組織構造を揺さぶる狙いで、成否はまだ示されていない計画の報道である。
## 5. 社会・コミュニティ／揺り戻し

### Not Palantir：Palantirを風刺する市民運動のパロディサイト
**原題**: Not Palantir
**カテゴリー**: 批判的分析
**URL**: https://notpalantir.eu/

欧州の市民運動団体WeMove Europeが公開した、Palantir Technologiesを風刺するパロディサイト。記事ではなく、本物のAIチャットサービスを模したUIに仕立てたキャンペーン用のWebアプリだ。「Ask anything. Question nothing.」「Status: watching you」「We practice tax avoidance!」といったスローガンで、同社の監視事業、データ独占、税回避を皮肉る。英独仏など7言語に対応する。情報源としてではなく、AI時代の監視技術と企業倫理をめぐる抗議の表現手法として読む一本だ。

---

### ウィキペディアはいかにしてAI生成コンテンツを排除し、人間の記述を守っているのか
**原題**: How Wikipedia’s Editors Keep the Online Encyclopedia Human-Written
**URL**: https://spectrum.ieee.org/wikipedia-wikiproject-ai-writing-cleanup

ウィキペディアのボランティアグループ「WikiProject AI Cleanup」創設者Ellia Lebleu氏へのインタビュー。初期のAI文は「testament to」のような決まり文句で見分けられたが、今は文章構造や論理展開のパターンへと移り、検知は難しくなった。実在する出典を挙げながら本文がそれを裏づけない「出典の誤用」が深刻で、出典と記述の整合を検証するAIや「Paste Check」で対抗する。AI検索で閲覧者と編集者が減る懸念も語られ、AI企業自身が人間の書いた高品質コーパスに価値を見出す点が皮肉だ。

---

### GHCにおけるAI利用コントリビューション方針：開発者コミュニティとレビュー品質の維持
**原題**: AI Contributions to GHC
**カテゴリー**: ニッチ・深堀り
**URL**: https://serokell.io/blog/ai-contributions-to-ghc

Glasgow Haskell Compiler（GHC）は、LLMを使った貢献に関する正式な方針を公開した。AIの是非を問うのではなく、ボトルネックであるメンテナのレビュー時間を守ることが目的だ。貢献者は全行を理解して説明責任を負い、直接生成した箇所はAssisted-Byタグで明示し、最終的なコードは自分で書き直すことが望ましいとされる。OpenJDKの禁止やLinuxカーネルの許容との比較も載る。AIが型変換最適化の概念実証に貢献した例を挙げつつ、品質と保守性の責任は常に人間にあると結ぶ。
## 編集後記

Annexに集めた記事は、メインの主要な流れからは少し外れるが、別の角度から今週を照らしてくれる。TDDやシェル高速化のような実践的なノウハウ、ブルックスの法則やASIリスクを引いた批判的な論考、トークナイザー税やtext-to-cadのようなニッチな深堀り――いずれも「流行の中心」ではないからこそ、手を動かす開発者や、距離を置いて眺めたい読者に効く視点だ。

カタログ形式は、こうしたB面を素早く拾い読みするためのものだ。各エントリは80〜120語で「読むべきか」を判断できるよう絞ってあり、気になった記事だけ原典に当たってもらえればいい。AnthropicのAI-native SDLCやOpenAIのModel Specのような一次情報は、要約で済ませず原文を確認する価値がある。

WikipediaのAI生成コンテンツ対策やGHCのLLM貢献ポリシーのように、コミュニティがAIとの付き合い方を自分たちで決めようとする動きも、今週は無視できない規模になっている。メインの華やかな進展とあわせて、こうした「揺り戻し」にも目を配っておきたい。

---

🤖 本記事は [Claude Code](https://claude.com/claude-code) を使用して編集されました。
