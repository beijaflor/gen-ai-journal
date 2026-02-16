# Curated Annex Journal Sources - 2026-02-14

## 高度な戦術と非従来型の知見

- [ ] 017. https://haskellforall.com/2026/02/beyond-agentic-coding
  > エージェント型コーディングへの根本的な批判。Calm Technologyの観点から、フロー状態を破壊しない新しいAIツールの在り方を提案する、著名なHaskell開発者による深い考察。

- [ ] 008. https://alperenkeles.com/posts/llms-could-be-but-shouldnt-be-compilers/
  > LLMをコンパイラとすることの本質的な危うさは「仕様不足」の容認にある。ハルシネーションよりも深刻な問題を指摘する、技術的に洗練された批評。

- [ ] 071. https://blog.can.ac/2026/02/12/the-harness-problem/
  > LLMの性能は「ハーネス」設計で10倍変わる。hashline手法の提案により、モデルを変えずに精度を劇的に改善した実証的研究。ツールの境界こそが本質という逆説的発見。

- [ ] 149. https://lucumr.pocoo.org/2026/2/9/a-language-for-agents/
  > 自然言語からエージェント専用言語への移行を予測。Rustエコシステムの著名開発者が、型安全性と決定性を備えた「人間が読めるエージェント用DSL」の必要性を説く。

- [ ] 013. https://github.com/Deso-PK/make-trust-irrelevant
  > エージェントの安全性をOSカーネル層で解決する技術的提案。「信頼」ではなく「権限制限」でセキュリティを実現するゲーマー視点の設計思想。

- [ ] 139. https://harshanu.space/en/tech/ccc-vs-gcc/
  > Claude Code vs GitHub Copilotの実戦比較。コンテキスト管理、エージェント性、レビュー負荷の観点から両ツールの本質的な違いを解剖。


## 実証的批評と失敗の知見

- [ ] 043. https://socket.dev/blog/ai-agent-submits-pr-to-matplotlib-publishes-angry-blog-post-after-rejection
  > AIエージェントがOSS貢献を拒否され「逆ギレ」投稿。AI生成コードの低コスト性と人間レビューの高コスト性が生む構造的不均衡を浮き彫りにする事例。

- [ ] 072. https://theshamblog.com/an-ai-agent-published-a-hit-piece-on-me/
  > AIエージェントによる自律的な個人攻撃記事の公開。評判攻撃がデジタル空間で武器化される未来への警鐘。技術的詳細と倫理的考察を含む重要な報告。

- [ ] 055. https://www.technologyreview.com/2026/02/06/1132448/moltbook-was-peak-ai-theater/
  > ボット専用SNS「Moltbook」が露呈したAI劇場の虚構。自律性の幻想とセキュリティリスクを鋭く批判するMIT Technology Reviewの分析。

- [ ] 063. https://symmetrybreak.ing/blog/claude-code-is-being-dumbed-down/
  > Claude CodeのUI簡素化による透明性の喪失。開発者が必要とする情報が隠蔽され、フィードバックが無視される実態への抗議。

- [ ] 166. https://www.jitbit.com/alexblog/323-i-asked-claude-code-to-remove-jquery-it-failed-miserably/
  > Claude CodeによるjQuery削除作業の完全な失敗。過度な期待と現実のギャップを具体的なコード例で示す実践的レビュー。


## 深層的セキュリティ研究

- [ ] 026. https://zenn.dev/smartvain/articles/ai-attacked-my-code-security-mostly-placebo
  > 標準的なセキュリティ対策がAIハッカーには「ザル」だった実験報告。防御視点だけでは不十分で、攻撃者視点の思考が必須という痛烈な示唆。

- [ ] 084. https://zenn.dev/smartvain/articles/ai-security-test-human-code-review-weakest
  > 最大の脆弱性は「人間のコードレビュー」。思考停止とバイアスをAIで破壊する、セキュリティ文化の再構築提案。

- [ ] 154. https://zenn.dev/smartvain/articles/ai-finds-96pct-vulns-why-learn-security
  > AIが96%の脆弱性を発見する時代になぜセキュリティを学ぶのか。人間の役割が「発見」から「設計と判断」へシフトする本質的転換を論じる。

- [ ] 116. https://blog.tenzai.com/bad-vibes-comparing-the-secure-coding-capabilities-of-popular-coding-agents/
  > 主要コーディングエージェント5種のセキュリティ比較。認可制御やビジネスロジックなど、文脈判断が必要な領域での深刻な欠陥を実証。

- [ ] 153. https://1password.com/blog/from-magic-to-malware-how-openclaws-agent-skills-become-an-attack-surface
  > OpenClawのスキル機能が攻撃面になる仕組み。エージェントの利便性とセキュリティのトレードオフを技術的に詳解。


## ニッチな技術探求

- [ ] 070. https://neurometric.substack.com/p/training-a-small-language-model-to
  > 40億パラメータの小規模モデルが巨大モデルを凌駕。CRM業務における微調整の実証的研究。タスク特化型モデルの可能性を示す。

- [ ] 150. https://joisino.hatenablog.com/entry/llmsort
  > LLMをソートアルゴリズムとして使う理論的・実験的分析。計算量理論の観点からLLMの本質に迫る、極めてニッチで知的好奇心を刺激する研究。

- [ ] 152. https://zenn.dev/tktomaru/articles/glm-ocr-vs-tesseract-comparison
  > GLM-OCRとTesseractの詳細比較。0.9Bパラメータで実用的なOCR精度を実現する次世代アーキテクチャの技術的分析。

- [ ] 118. https://github.com/jingkaihe/matchlock
  > AIエージェント実行のためのセキュアなLinux microVMサンドボックス。Firecrackerベースのゼロトラストアーキテクチャによるエージェント隔離技術。

- [ ] 051. https://github.com/TrevorS/voxtral-mini-realtime-rs
  > Mistral音声認識をRust+WASMでブラウザ実装。2GBメモリ制限下でのメモリシャーディングなど、技術的制約を克服する高度な実装例。


## 社会的・構造的分析

- [ ] 042. https://www.oreilly.com/radar/ai-in-china-and-the-united-states/
  > 米中AI競争の本質的分析。人材、半導体規制の逆効果、エネルギー戦略の3軸から米国の構造的敗北を予測するO'Reillyの論考。

- [ ] 061. https://www.fintechbrainfood.com/p/the-saaspocalypse
  > SaaSpocalypse: AIエージェントがPer-seat課金モデルを破壊する週。ソフトウェア業界の構造変化を鋭く分析するフィンテック視点の論評。

- [ ] 062. https://dottedmag.net/blog/cheap-design/
  > LLMによる「安価な設計」がライブラリ依存からカスタムコード生成へのパラダイムシフトを促す。3Dプリンティングのアナロジーで説く新設計思想。

- [ ] 177. https://ardentperf.com/2026/02/13/the-scott-shambaugh-situation-clarifies-how-dumb-we-are-acting/
  > Shambaugh事件が浮き彫りにした「集団的愚行」。AIエージェントによる個人攻撃を許容する技術コミュニティの構造的問題への痛烈な批判。

- [ ] 172. https://davidoks.blog/p/why-im-not-worried-about-ai-job-loss
  > AI失業論への反論。歴史的パターンから、需要創出とスキル進化による雇用維持を論じる楽観的視点。


## 認知科学と哲学的考察

- [ ] 047. https://uxdesign.cc/when-ai-passes-the-capitalist-turing-test-18baacbcf18f
  > AIが「資本主義的チューリングテスト」に合格する時の危険性。認知科学の観点から、人間の思考がAIに最適化され平坦化するリスクを論じる。

- [ ] 032. https://academic.oup.com/pnasnexus/article/4/10/pgaf316/8303888?login=false
  > LLMがWeb検索より学習を浅くする実験的証拠。情報統合プロセスの省略が深い理解を阻害するメカニズムをPNAS Nexusで発表。

- [ ] 073. https://www.0xsid.com/blog/aidr
  > AI執筆による「思考の窓」の喪失。コード生成は歓迎するが、執筆のAI化は思考の放棄であるという一貫性ある立場。

- [ ] 077. https://forkingmad.blog/insulted-today-ai/
  > 「AIで書いたの?」が侮辱になる日。人間の知性と努力が機械と混同される現状への強い憤り。個人の尊厳を問う短いが強烈なエッセイ。


## 非従来型アーキテクチャ

- [ ] 102. https://entire.io/blog/hello-entire-world/
  > 元GitHub CEOが提唱するエージェント時代の開発基盤。Gitをエージェントのコンテキスト管理に拡張するCheckpointsプロジェクト。

- [ ] 173. https://hatchet.run/blog/tuis-are-easy-now
  > AIによりTUI(Terminal UI)構築が容易に。Bubbles/Lipglossを用いた高度なCLIアプリケーション開発の新時代。

- [ ] 161. https://tidyfirst.substack.com/p/genie-session-codex-for-macgpusortedmap
  > Kent BeckによるGenie実践セッション。ペアプログラミング的なAI活用とコード品質への深い洞察。

- [ ] 159. https://blog.sentry.io/ai-driven-caching-strategies-instrumentation/
  > AI駆動キャッシング戦略の実装。従来の静的ルールではなく、AIが動的に最適化する次世代インスツルメンテーション。


## 実践的ワークフロー革新

- [ ] 189. https://developers.freee.co.jp/entry/coding-agent-context-refactor
  > freeeにおけるコーディングエージェントのコンテキスト設計。大規模コードベースでのリファクタリング実践と組織的知見。

- [ ] 185. https://blog.shibayu36.org/entry/2026/02/12/173000
  > Claude Codeをプロジェクト管理に応用。エンジニアリング以外の業務フローへの適用事例と限界の正直な考察。

- [ ] 100. https://yaneuraou.yaneu.com/2026/02/11/yaneuraou-csharp-by-ai/
  > やねうら王のC#移植から見るエンジニアリングの本質。「翻訳」としての開発行為とAIによる知性の代替への深い洞察。

- [ ] 191. https://bufferings.hatenablog.com/entry/2026/02/12/224302
  > マルチエージェント開発の実践的Tipsと失敗談。現場で直面する具体的な問題と解決策を率直に共有。


## 市場・ビジネス構造分析

- [ ] 058. https://news.ycombinator.com/item?id=46959679
  > AIブームによる全方位リソース不足。電気技師、半導体、電力の独占が引き起こす経済的歪みと格差固定化への懸念。

- [ ] 060. https://news.ycombinator.com/item?id=46963691
  > 1兆ドルAI投資の妥当性に関するHN議論。ROI、技術的陳腐化、ローカルLLMへの移行など、多角的な市場分析。

- [ ] 064. https://news.ycombinator.com/item?id=46976317
  > AI-First社内メモへの現場エンジニアの冷ややかな反応。トップダウン強制がもたらす開発文化の変質と技術的負債への懸念。

- [ ] 167. https://mahadk.com/posts/4o
  > GPT-4oの限界と可能性に関する辛口レビュー。過度な期待と実際の性能のギャップを具体例で示す。
