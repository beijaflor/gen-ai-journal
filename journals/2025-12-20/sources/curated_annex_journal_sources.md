# Curated Annex Journal Sources - 2025-12-20

## Advanced Tactics & Unconventional Wisdom (高度な戦術と非自明な知見)

- [ ] https://syu-m-5151.hatenablog.com/entry/2025/12/19/173309
<!-- Claude CodeのAgent Skillsは設定したほうがいい
LLMの根本的な制約(ステートレス性)を克服し、「AIエージェントのためのBDD」という新しい概念を提示。Progressive Disclosureによるコンテキスト効率化は、実装レベルで差がつく高度なテクニック。Anthropic公式の設計思想をここまで深掘りした解説は希少。 -->

- [ ] https://engineering.dena.com/blog/2025/12/legacy-code-migration-using-devin/
<!-- Devin AI で挑む AI エンジニアによるレガシー API 移行
DevinとClaude Codeの「80-15-5」ワークフロー、CI/CDによるガードレール設計、AIの学習能力を引き出す実践手法。レガシーコード移行という具体的ユースケースで、AIとの協業モデルを体系化した実戦報告。人間の役割が「アーキテクト+PM」へシフトする未来を具体的に示す。 -->

- [ ] https://friendlybit.com/python/writing-justhtml-with-coding-agents/
<!-- コーディングエージェントでJustHTMLを開発した方法
html5libテストスイート100%達成というベンチマークで証明された、エージェント駆動開発の実力。「広範なテストスイートがAIの自己修正を可能にする」という知見、性能最適化とファジングテストまで含む実践的アプローチ。人間は「考えること」に集中する分業モデルの成功例。 -->

- [ ] https://zenn.dev/livetoon/articles/ba4536e4722187
<!-- 医療業界で突然LLMを使ってくれと言われたら
日本の医療業界という最も規制が厳しい領域で、3省2ガイドライン準拠とデータ主権の両立を技術的に解決。AWS Bedrock CRISの従量課金+国内完結という現実解は、他の規制産業にも応用可能な戦略的選択。「患者データを守りながら実用価値を出す」という本質を見失わない判断基準が秀逸。 -->

- [ ] https://speakerdeck.com/icoxfog417/generative-ai-agent-should-work-in-night
<!-- 夜を制する者が "AI Agent 大民主化時代" を制する
営業時間の1.6倍もある夜間という「ブルーオーシャン」に着目した発想の転換。AWS FRONTIER AGENTSを活用した具体的なタスク分類と、人間が休む間にAIが働く新ワークフローは、生産性の次元を変える戦略。マルチタスクによる集中阻害を回避する知恵。 -->

- [ ] https://zenn.dev/genda_jp/articles/2025-12-12-drawio-tips-claude-code
<!-- Claude Code に draw.io の図を描かせるコツ
XMLレベルの罠(フォント設定、矢印配置、テキストサイズ)を体系的に整理し、pre-commit hookによる自動PNG生成まで含む実践的ワークフロー。「draw.ioアプリとPNG出力の差異」という見落としがちな落とし穴への警告も貴重。AIに図を描かせる際の再現可能な知見。 -->

- [ ] https://zenn.dev/ubie_dev/articles/llm-as-a-judge-rubric-evaluation
<!-- LLM-as-a-Judge とルーブリック評価
主観評価の限界(5点満点で差がつかない)を、ルーブリック評価で完全再現性(50回全一致)へ。true/falseの客観判定による改善点の可視化は、LLMOpsにおける品質保証の実効性を飛躍的に高める。OpenAI HealthBench採用の手法を実例で検証した価値。 -->

- [ ] https://qiita.com/Yodeee/items/1882750551e3c932937c
<!-- AgentフレームワークStrands Agentsの設計思想をコードを追って理解する
AWSのモデル駆動アプローチの内部実装を、Pythonコードレベルで徹底解剖。`event_loop_cycle`におけるLLM推論ループ、`ConcurrentToolExecutor`による並列実行、非同期ジェネレータのストリーミング処理。表層的な使い方ではなく、設計思想を理解することでデバッグと拡張が可能になる深い知見。 -->

## Substantive Critique & Contrarian Views (実質的批評と対抗視点)

- [ ] https://www.technologyreview.jp/s/374024/the-great-ai-hype-correction-of-2025/
<!-- GPT-5ローンチ失敗、企業95%が成果出せず … 転換期を迎えたAIブーム
MIT Technology Reviewによる冷静な現実分析。GPT-5の期待外れ、企業AI導入の95%が価値創出に失敗という厳しいデータ。「期待を再調整する好機」という建設的な結論が、誇大宣伝への反動を超えて、実践的AI活用への道筋を示す。スマホの進化に例えた「普通のテクノロジー化」の洞察。 -->

- [ ] https://zenn.dev/aun_phonogram/articles/a8757102bc8ca8
<!-- AI時代にWebエンジニアに必要なのは「検証力」
Karpathyの「検証可能性」概念を軸に、AIと人間の役割分担を再定義。「What/How」はAIに、「Why」は人間にという明確な指針。「このコードは何を検証しようとしているか?」という問いは、AI時代のエンジニアの思考法を根本から変える。検証できない戦略判断こそが人間の価値。 -->

- [ ] https://tech.speee.jp/entry/ai-agent-rd-milestone-driven
<!-- AIエージェント開発で半年間成果が出なかった私が、前に進めるようになるまで
停滞の原因(曖昧なマイルストーン、手段の検証への執着)と打開策(事業成果からの逆算、1日1実験)を赤裸々に告白。4ヶ月138回の実験で画像認識への転換を実現した軌跡は、R&Dの不確実性と向き合う全エンジニアへの教訓。小さく試して学ぶ愚直さこそが最速の道。 -->

- [ ] https://forest.watch.impress.co.jp/docs/serial/aidev/2071380.html
<!-- コーディング変革！「仕様駆動開発(SDD)」の手引き
「実装先行、仕様後付け」という負のサイクルへの根本的解決策。AIとの協業を前提とした「仕様ファースト」は、コードとドキュメントの乖離、品質保証の後手、という長年の課題を一掃する。開発者の役割が「コーダー」から「仕様アーキテクト」へ進化する未来の設計図。 -->

- [ ] https://blog.pokutuna.com/entry/ai-rediscovered-tech-and-tools
<!-- AI で再注目された技術やツールたち
SSE、Pandoc、Markdown、アクセシビリティツリー、音声入力という既存技術が、AI時代に新しい価値を獲得した実例集。「目新しさ」より「実績ある技術の再文脈化」という視点は、技術選定において本質を見抜く力を養う。GraphRAGやサンドボックス技術まで含む広範な観察眼。 -->

## Niche Explorations & Deep Dives (ニッチな探求と深掘り)

- [ ] https://qiita.com/k_kitamura/items/7c9bff3e42133f4ebaf7
<!-- 初めてのバグ分析でGemini先生に壁打ちを頼んだ話
QAエンジニアがバグ分析の壁打ち相手としてGeminiを活用。「テスト量≠品質」という洞察をAIが客観的に指摘し、著者の誤った参照データを修正した事例は、AIが単なるツールを超えて「思考のパートナー」となる可能性を示す。適切な文脈と意図を伝える「舵取り」の重要性。 -->

- [ ] https://qiita.com/TokomaBaou/items/cff5444e7135c98a45ae
<!-- 雑談会から始まった社内勉強会を、Next.js + NestJS + AI で学習プラットフォームに進化させた話
3年間の雑談会を、AIアーカイブ+ゲーミフィケーション+QR出席で「居場所」へ昇華。月150回以上のアーカイブ閲覧という数字が、「参加できない理由は仕組み側にある」という設計思想の正しさを証明。Claude Codeによる「Why & What」と「How」の分業モデルも実践的。 -->

- [ ] https://dev.classmethod.jp/articles/claude-code-custom-slash-commands-routine-tasks/
<!-- Claude Codeのカスタムスラッシュコマンドで定型作業を効率化する
コーディング外での活用(会議アジェンダ、Marpスライド)という発想の転換。「毎回ちょっと面倒だけど同じこと」をコマンド化し、60-70%の雛形で手動作業を削減。チーム共有によるプロンプト標準化という組織的価値も示唆。定型業務のAI化における具体的成功パターン。 -->

- [ ] https://note.com/kohya_ss/n/n613b44bb15a5
<!-- 生成AIに知識を垂れ流すラジオ番組を作ってもらう
Gemini CLI、T5Gemma-TTS、Sunoを連携させた「変な知識ラジオ」という創造的実験。Gemini CLIのプロンプト忠実性、参照音声による声質固定など、複数AIツールの強みを組み合わせた実践例。「垂れ流す」というユニークコンセプトがAIで実現可能であることを証明。 -->

- [ ] https://note.com/mmiya/n/n5f3a4644469f
<!-- AI時代の超読書術の試行錯誤の話
「知識を得る読書」から「知識を作る読書」への変革。Kindleハイライト→AI書評→対話的深掘り→Notebook LM結晶化という5ステップは、紙の時代には不可能だった体験。プレリーディングのバイアスやハルシネーションという限界も正直に指摘する誠実さが、実用性を高める。 -->
