# Curated Annex Journal Sources - 2026-02-21

## Annex Theme A1: OpenClaw事件の解剖——Cryptoが資金供給したAI攻撃の全貌と「極小エージェント」の設計哲学

- [ ] https://news.ycombinator.com/item?id=47051866
  <!-- OSS maintainerを中傷したOpenClawボットが「Cryptoブロ」に資金供給・操作されていたというフォレンジック調査。AIが「自律的」に見えて実は人間が操る攻撃ツールという構造を可視化した貴重な事例 -->

- [ ] https://qiita.com/emi_ndk/items/bf3b5f0f3eef99a4d124
  <!-- 「スキルの12%がマルウェア」という衝撃の数字とCVE-2026-25253（ゼロクリック乗っ取り）の詳細を日本語で解説した緊急レポート。2万台以上のインスタンス被害という具体数値が示す規模感 -->

- [ ] https://zenn.dev/masahide/articles/ab93620ca9353e
  <!-- OpenClawの基盤コンポーネント「pi-coding-agent」の設計哲学：1000トークン以下のプロンプト、MCPの不採用、デフォルトYOLOモードなど「削ること」を徹底したミニマリズム設計の深掘り -->

- [ ] https://hackmyclaw.com/
  <!-- OpenClawベースのAIアシスタントへのプロンプトインジェクション公開チャレンジ（賞金300ドル）。メールという間接ベクトルを通じた攻撃の実験場として、AIセキュリティ研究の教材 -->

- [ ] https://note.com/fladdict/n/n5f315e408879
  <!-- 深津貴之氏によるOpenClaw+Claude Code連携の自律型開発アーキテクチャ。TODO.mdとREPORT.mdを状態管理ハブにした「プランナー・エグゼキューターモデル」の具体設計 -->

- [ ] https://news.ycombinator.com/item?id=47069299
  <!-- AnthropicがサードパーティツールでのサブスクリプションAuth利用を禁止した件のHN議論。逆ザヤ経済の合理性、OpenAIとの戦略差、エコシステムの囲い込みへの反発が交錯 -->

---

## Annex Theme A2: MCPセキュリティ・エージェント認可設計——攻撃手法から防御アーキテクチャまで

- [ ] https://marmelab.com/blog/2026/02/16/mcp-security-vulnerabilities.html
  <!-- 外部インジェクション・ツール記述改ざん・クロスツールハイジャックの3つのMCP攻撃手法を実証した技術記事。最新モデルでの検知率向上も含め、現実的な脅威を具体的に示す -->

- [ ] https://workos.com/blog/agents-need-authorization-not-just-authentication
  <!-- 「混乱した代理人」問題に対するFine-Grained Authorization（FGA）の提案。RBAC二択の罠とスコープ減衰・JIT認可・IBACという次世代IAM設計論 -->

- [ ] https://www.metachris.dev/2026/02/safe-yolo-mode-running-llm-agents-in-vms-with-libvirt-and-virsh/
  <!-- LibvirtとVirshを使ってLLMエージェントをVM内で安全に実行する実践ガイド。Claude Code/Gemini CLI/Codex CLIのインストール手順込みで、エージェントのYOLOモードを安全に実現 -->

- [ ] https://arxiv.org/abs/2602.11988
  <!-- 衝撃の研究：AGENTS.mdはタスク成功率を「悪化」させ推論コストを20%超増加させる。人間が書いても、AIが書いても逆効果という結果が示す、コンテキスト設計の本質的難しさ -->

- [ ] https://www.oreilly.com/radar/ai-a2a-and-the-governance-gap/
  <!-- A2A・ACP・MCPの3層スタックで組織のガバナンスが追いつかない「ガバナンスの溝」を警告。「エージェント条約」レイヤーの構築という具体提言が実務的 -->

- [ ] https://www.theregister.com/2026/02/18/generating_passwords_with_llms/
  <!-- Claude Opus 4.6が50回中18回同じパスワードを生成、エントロピー20〜27ビットという衝撃のデータ。LLMが「根本的にパスワード生成に不向き」な理由を技術的に説明 -->

---

## Annex Theme A3: スキルエコシステム実装の最前線——設計哲学から大規模運用まで

- [ ] https://zenn.dev/kyre/articles/evolution-agent-skills-nix
  <!-- Nixを使ってAIエージェントスキルを宣言的に管理。バージョン固定・依存関係の同梱・プロジェクトローカル導入まで対応した「agent-skills-nix」の進化 -->

- [ ] https://techblog.zozo.com/entry/agent-skills-for-techblog-review
  <!-- ZOZO年間100本のテックブログレビューをAgent Skillsで自動化。3年分のレビュー履歴を分析してルールを明文化し、人間の指摘の75%をカバーできた実証事例 -->

- [ ] https://note.com/timakin/n/nf497d32c2d35
  <!-- SkillsBench研究：人間キュレーションのスキルは+16.2%改善、AI自己生成は-1.3%という逆効果。「網羅的スキルの罠」と2〜3モジュール・具体手順・動作例1つの設計最適解 -->

- [ ] https://tech.plaid.co.jp/claude-code-scalable-team-operation
  <!-- PLAIDがAGENTS.md+Hooks+Skillsで月150PRを600PRに4倍スケール。コンテキスト設計・ガードレール自動化・プロセス定型化の3本柱による実践的チーム運用 -->

- [ ] https://developers.cyberagent.co.jp/blog/archives/62110/
  <!-- サイバーエージェント新卒2名で6名分の出力を実現。37スキル+24SubAgent・git worktreeによる並列実装・AskUserQuestion自動化の具体構成が公開された貴重な事例 -->

- [ ] https://zenn.dev/yusuke_shiya/articles/claude-code-team-adoption
  <!-- フロントエンド5名チームのVue2→React移行で8ヶ月使い込んで判明した「任せること」と「握ること」の境界線。設計委任の失敗経験と「マージの儀」による理解負債防止 -->

- [ ] https://boristane.com/blog/how-i-use-claude-code/
  <!-- 「計画が承認されるまでコードを1行も書かせない」原則と、research.md→アノテーション付きplan.md→実装の3段階。共有MarkdownファイルをMutable Stateとして扱うユニークな手法 -->

- [ ] https://qiita.com/dai_chi/items/252fb5ef031127784757
  <!-- Claude Code作者Boris Cherny氏が公開した9種のカスタマイズ手段と37以上の設定項目。Effort・LSPs・Skills・Hooks・Custom Agentsの全貌と4層セキュリティ構造 -->

- [ ] https://zenn.dev/neurostack_0001/articles/agent-teams-one-week-redefine-work
  <!-- Agent Teams+Skillsで3体のエージェントと1週間働いたら「選ぶ力」と「専門性の設計」が人間の本質的役割だと気づいた実体験。仕事の再定義を内側から描いた証言 -->

- [ ] https://tech.newmo.me/entry/claude-code-deep-research
  <!-- Claude Codeを「Deep Research」専用ツールに特化させる/mode-researcherスキル。Blink Shell→リモートサーバー→iCloud→Obsidianという完全モバイル対応ワークフロー -->

---

## Annex Theme A4: エンジニアリング変革の証言と技術深掘り

- [ ] https://cannoneyed.com/essays/software-industrial-revolution
  <!-- 第一次産業革命とのアナロジーで描く「ソフトウェア産業革命」論。VC依存とEnshittificationを破壊し科学者・専門家が自ら安価にツールを構築できる「豊穣の時代」の到来 -->

- [ ] https://github.blog/ai-and-ml/generative-ai/how-ai-is-reshaping-developer-choice-and-octoverse-data-proves-it/
  <!-- Octoverse 2025：TypeScriptがJavaScriptを抜いて首位になった背景に「コンビニエンス・ループ」。AIとの親和性が技術選定基準になったことをデータで証明 -->

- [ ] https://doodledapp.com/feed/ai-made-every-test-pass-the-code-was-still-wrong
  <!-- AIにテストを書かせると既存コードの挙動を正解とする「グラウンドトゥルースの罠」。AST比較+AI差分分析という解決策が実践的 -->

- [ ] https://martinfowler.com/fragments/2026-02-18.html
  <!-- Martin Fowler：AIは「アンプ」であり、劣悪な開発文化では技術負債を加速させる。「最強のプロンプトエンジニアリングはTDD」「健全なコードベースほどAIリファクタリングが30%安全」 -->

- [ ] https://nextjs.org/blog/agentic-future
  <!-- Next.jsチームがAIエージェントを「第一級の利用者」と定義し、MCPでエラー・ルート・セグメントを公開。「next dev」統合の方向性が示す、フレームワークとエージェントの統合未来 -->

- [ ] https://www.oreilly.com/radar/what-developers-actually-need-to-know-right-now/
  <!-- Tim O'Reilly×Addy Osmani対談：課題は「生成」でなく「オーケストレーション」、設計が新たなコーディング、「センス」が技術スキルの一部になるという3つの洞察 -->

- [ ] https://speakerdeck.com/cyberagentdevelopers/research-and-application-of-generative-ai
  <!-- サイバーエージェントAI Labの研修資料：Cline Memory Bank・Claude Code CLAUDE.md管理・MCPツール活用・長時間タスク自動化の実践テクニック集 -->

- [ ] https://www.seangoedecke.com/fast-llm-inference/
  <!-- AnthropicのバッチサイズUI最小化（2.5倍高速・精度維持）とOpenAIのCerebrasチップ+蒸留モデル（15倍高速・精度低下）の技術比較。速度と精度のトレードオフの核心 -->

- [ ] https://zenn.dev/sh1ma/articles/b6719fa5fec00c
  <!-- CLAUDE_CODE_TEAMMATE_COMMANDの隠し環境変数でAgent Teamの子インスタンスをGLM-5にオフロードし、トークン消費50%超削減。実運用レベルのコスト最適化ハック -->

---

## Annex Theme A5: AIへの批判・哲学的考察——信頼の喪失と人間性の問い

- [ ] https://www.fast.ai/posts/2026-01-28-dark-flow/
  <!-- バイブコーディングをスロットマシンのギャンブル依存「LDW（負けているのに勝っていると感じる）」にたとえるRachel Thomas。「主観では20%効率化、実際は19%遅化」の研究データが刺さる -->

- [ ] https://simonwillison.net/2026/Feb/15/deep-blue/
  <!-- Simon Willisonが命名した「Deep Blue」：長年培った技術が瞬時に代替される際の実存的恐怖。AIの台頭に直面するエンジニアのメンタルヘルスに名前をつけた重要な論考 -->

- [ ] https://www.theregister.com/2026/02/16/semantic_ablation_ai_writing/
  <!-- 「セマンティック・アブレーション」：AIがハルシネーションと逆に、独創的表現を削ぎ落として統計的平均へ収束させる現象。「思考のJPEG」という表現が秀逸 -->

- [ ] https://joshcollinsworth.com/blog/sloptimism
  <!-- 「AI楽観主義は階級特権」：AIの恩恵を受ける側の無自覚な特権性を鋭く批判。盗作されるアーティスト・解雇されるジュニア層・ディープフェイクの被害者を「コスト」として負わせる構造 -->

- [ ] https://blog.fallible.net/why-we-hate-ai/
  <!-- AIへの嫌悪をマルクスの商品フェティシズムとダストン・ギャリソンの「客観性」理論で解読。労働に内在する人間的社会関係を機械による「客観性」が疎外・切断するという哲学的論考 -->

- [ ] https://www.jeffgeerling.com/blog/2026/ai-is-destroying-open-source/
  <!-- curlなどのOSSで有用な脆弱性報告が激減し、AIスロップPRが急増。GitHubがPR機能を完全無効化するオプション追加を余儀なくされた現状への告発 -->

- [ ] https://automaton-media.com/articles/newsjp/godot-20260218-422080/
  <!-- Godotメンテナーの悲鳴：AI生成の支離滅裂なPRの精査で疲弊し士気低下。「提案者が変更内容を理解していない」「ハルシネーションか単純ミスか判別困難」という現場の実態 -->

- [ ] https://dlants.me/agi-not-imminent.html
  <!-- AGIが近くない技術的理由：認知プリミティブ・身体性の欠如とTransformerのTC⁰制約。CoTは「外部スキャフォールディング」に過ぎずモデル内部の知能構造進化ではないという反論 -->

- [ ] https://nicole.express/2026/not-my-casual-hobby.html
  <!-- レトロゲーム研究者が告発するAIハルシネーションによる情報commons破壊。Ars Technicaすら信頼できない現実と「確認コストの激増」という具体的な問題提起 -->

---

## Annex Theme A6: LLMアーキテクチャ・ビジネスモデルの再設計

- [ ] https://www.oreilly.com/radar/ai-is-not-a-library-designing-for-nondeterministic-dependencies/
  <!-- AIは決定論的ライブラリでなく「非決定論的コラボレーター」。リトライ・テスト・観測性の3領域で従来の常識が通用しない理由と、ガードレール＋フォールバック設計の処方箋 -->

- [ ] https://blog.exe.dev/expensively-quadratic
  <!-- LLMエージェントのキャッシュ読み取りコストが二次関数的に増大し最終的にコストの87%を占める問題を実測で証明。「ツール一括実行」「サブエージェント分離」「会話リセット」の対策 -->

- [ ] https://georgeguimaraes.com/your-agent-orchestrator-is-just-a-bad-clone-of-elixir/
  <!-- PythonやJSのAIフレームワークはElixir/BEAMが30年前に解決済みの問題を再発明しているだけ。「Let it crash」監視ツリー・ホットコードスワップのAIエージェントへの適合性 -->

- [ ] https://royapakzad.substack.com/p/multilingual-llm-evaluation-to-guardrails
  <!-- 同一プロンプトでも言語によって人権報告書の要約が「告発」から「法執行の強調」に変質。英語で拒否される危険な医療アドバイスがペルシア語では通ってしまう安全性の不一致 -->

- [ ] https://commaok.xyz/ai/just-in-time-software/
  <!-- 食料品店で買い物中に2分でカスタムアプリを作るという体験から導く「ジャストインタイム・ソフトウェア」パラダイム。コスト0.34ドル・ガソリン23メートル分という現実的試算付き -->

- [ ] https://xenospectrum.com/ai-disruption-2026-matt-shumer-warning/
  <!-- OthersideAI CEOがGPT-5.3の「自己進化ループ」開始を警告。「ドラフト作成ツール」から「自律完結型」への質的変化と、パンデミック直前の「過小評価」段階にあるという指摘 -->

- [ ] https://www.anthropic.com/research/measuring-agent-autonomy
  <!-- Anthropicの大規模調査：Claude Codeの自律稼働時間が3ヶ月で倍増し、熟練ユーザーほど「継続的監視」へ移行。AIが自ら確認を求める頻度が人間介入より高いという安全機能の発見 -->

- [ ] https://1password.com/blog/filesystems-for-agent-swarms
  <!-- エージェント・スウォームの時代にファイルシステムが共有メモリの普遍的基盤として再評価される理由。本番運用には個別アイデンティティとCapabilityベースの権限管理が必要 -->
