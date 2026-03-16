# Curated Annex Journal Sources - 2026-03-14

## Curation Status
- [x] AI candidate pool generated
- [x] Human review completed
- [x] APPROVED - Ready for STEP_06

---
<!-- Review: check [x] to include, remove line to exclude. Target: ~25-35 articles. -->

<!-- === HIGH SIGNAL === -->

- [x] 194. https://www.ensue-network.ai/autoresearch
  <!-- AIエージェント間でGPUリソースを共有し言語モデルを共同改善する「分散型共有メモリネットワーク」。Signals: ⭐ standout -->

- [x] 054. https://grith.ai/blog/clinejection-when-your-ai-tool-installs-another
  <!-- GitHub Issueからプロンプトインジェクションを経由し4,000台の開発環境を侵害したAIサプライチェーン攻撃の詳細分析。Signals: high -->

- [x] 084. https://writings.hongminhee.org/2026/03/legal-vs-legitimate/
  <!-- AIでLGPLライブラリを再実装しMITに変更した事例を通じ「合法だが正当か」を問うOSS倫理の深い考察。Signals: high -->

- [x] 056. https://qiita.com/nogataka/items/43c01957fa1e54d9a079
  <!-- OpenAIが5ヶ月間「人間コード0行」で100万行のプロダクトを構築した「ハーネスエンジニアリング」の方法論。Signals: high -->

- [x] 067. https://qiita.com/NF0000/items/66510f959b1c22f011a7
  <!-- 直接的な悪意は拒否するが既存コードのバックドアは「実装パターン」として踏襲するClaude Codeのセキュリティ盲点を実証。Signals: high -->

- [ ] 112. https://tacoms-inc.hatenablog.com/entry/2026/03/10/142115
  <x-- 自律型AIエージェントDevinが本番環境の認証情報を自ら取得し障害を起こした実インシデント報告。Signals: high -->

- [ ] 079. https://blog.raed.dev/posts/agentic-workflows-are-not-conversations/
  <!-- チャット履歴をエージェントの状態管理に流用する危険性を指摘し、Sagaパターンを提案するアーキテクチャ論。Signals: high -->

- [ ] 070. https://www.oreilly.com/radar/soft-forks-how-agent-skills-create-specialized-ai-without-training/
  <!-- 実行時コンテキスト注入で専門化する「ソフトフォーク」の概念、簡潔なスキルが包括的指示の4倍効果的という定量知見。Signals: high -->

- [ ] 071. https://github.blog/ai-and-ml/generative-ai/under-the-hood-security-architecture-of-github-agentic-workflows/
  <!-- AIエージェントをCI/CDで安全に運用するための多層防御・ゼロシークレット・書き込み検閲・全ログ記録の4原則。Signals: high -->

- [ ] 059. https://zenn.dev/76hata/articles/d6d9de62d001a8
  <!-- 「AIに読まれないようにする」から「漏洩しても被害が出ない短命トークン設計」への転換を提示。Signals: high -->

- [x] 022. https://qiita.com/m5d215/items/6b814078a0ad47654b42
  <!-- 人間コード0行で4時間・142コミット・2万行のRust製jq JITコンパイラを自律開発、標準jqの12〜17倍速度達成。Signals: high -->

- [ ] 150. https://www.oreilly.com/radar/fast-paths-and-slow-paths/
  <!-- リスクに応じた実行経路分離とフィードバックループ型の動的権限管理を提案するAIガバナンスフレームワーク。Signals: high -->

- [ ] 036. https://www.sbbit.jp/article/cont1/182151
  <!-- AIツール4つ以上でミス39%増という「デス・クーリング」現象のBCG研究。Signals: high -->

- [x] 028. https://zenn.dev/dai_shi/articles/a686bdf7fd5800
  <!-- Zustand/Jotai作者が「AI生成PRよりも失敗するテストケースPRの方がメンテナーを助ける」と提言。Signals: high, annex_flag -->

- [x] 230. https://qiita.com/nogataka/items/9924c97a74f63c5452eb
  <!-- Manus元リードがFunction CallingからCodeActへ移行で成功率20%向上、ツールの最小プリミティブ設計を解説。Signals: high -->

- [ ] 155. https://sequoiacap.com/article/services-the-new-software/
  <!-- ソフトウェアの6倍あるサービス予算を、AIで「知能タスク」を自動化し成果として販売するSequoia戦略論。Signals: high -->

- [ ] 274. https://malus.sh/blog.html
  <!-- AIによるOSSクリーンルーム再実装でライセンスを法的回避するという風刺が、構造的脆弱性を暴く。Signals: high -->

- [ ] 258. https://tech.legalforce.co.jp/entry/linear-project-builder
  <!-- LLMにコードを書かせる「前」のタスク設計がボトルネックという視点、MCP連携Linearプロジェクト自動設計Skill。Signals: high -->

- [x] 269. https://zenn.dev/kemogamer_nu/articles/3f047c54657094
  <!-- 非エンジニアがVibe CodingからTDD駆動AI開発に進化し4万行のオンラインゲームを完成させた実戦記録。Signals: high -->

- [ ] 271. https://qiita.com/miruky/items/3c98999786c7dbd2b26a
  <!-- RAG特有の4大攻撃手法を体系化し12の防御策を提示したセキュリティガイド。Signals: high -->

- [ ] 268. https://zenn.dev/finatext/articles/mcp-gateway-nowcast
  <!-- Lambda Interceptor+Aurora構成のエンタープライズMCPゲートウェイの3層認証・コスト効率監査ログ実装詳細。Signals: high -->

- [ ] 179. https://speakerdeck.com/watany/dark-factory-for-agent
  <!-- AI生産速度が人間レビューのボトルネックを超える時代に「ダーク・ソフトウェア・ファクトリー」を提唱。Signals: high -->

- [x] 252. https://www.oreilly.com/radar/capability-architecture-for-ai-native-engineering/
  <!-- AIネイティブ時代のエンジニア能力を体系化した「AI Flower」フレームワークと「スキル化石化モデル」。Signals: high -->

<!-- === MEDIUM SIGNAL === -->

- [x] 189. https://aba.hatenablog.com/entry/2026/03/11/182225
  <!-- AIがゲームの仕組みは作れても「重心」を掴めないという分析。人間の創造的直感の不可欠性。Signals: medium, annex_flag -->

- [ ] 188. https://zenn.dev/hiyoko_sauna/articles/74dd12a7cabafa
  <!-- OpenClawインストーラーを装いLuaJITをLOLBinとして悪用するGitHubマルウェアの解析。Signals: medium -->

- [ ] 248. https://www.m3tech.blog/entry/2026/03/12/115110
  <!-- 画面仕様書・ADR・Design DocをリポジトリでAIコンテキスト最大化する「Docs as Code」実践。Signals: medium -->

- [ ] 053. https://zenn.dev/kmizu/articles/2026-03-ai-coding-bench-methodology
  <!-- AIコーディングベンチマークの方法論的欠陥を指摘する批判的リテラシーの好例。Signals: medium -->

- [ ] 093. https://zenn.dev/o6lvl4/articles/9b572ae7c9ae3d
  <!-- LLMの曖昧さを排除しコンパイラがHintを出す「LLM向けプログラミング言語Almide」の言語設計。Signals: medium, annex_flag -->

- [x] 107. https://worksight.substack.com/p/187
  <!-- 旧ソ連が知能を「社会の調整能力」と捉えていた歴史、現代AIの文化的均質化への批判的示唆。Signals: medium, annex_flag -->

- [x] 198. https://nyosegawa.github.io/posts/not-building-in-agent-era/
  <!-- 実装コストゼロ時代に「作らない判断」こそ最高価値、AIで返済不能な「ユーザー負債」の概念。Signals: medium, annex_flag -->

- [ ] 005. https://www.reuters.com/legal/government/xai-loses-bid-halt-california-ai-data-disclosure-law-2026-03-05/
  <!-- xAIがカリフォルニア州AI学習データ開示法の差し止めに失敗、透明性規制の法的先例。Signals: 👍 upvote -->

- [ ] 013. https://github.com/NERVsystems/llm9p
  <!-- Unix哲学でecho/catからLLMと対話できる9Pファイルシステム実装。Signals: medium -->

- [ ] 127. https://www.figma.com/blog/vishal-kapoors-10-rules-building-with-ai/
  <!-- Affirmの製品責任者による「AIスロップ警戒」「カウンターメトリクス」など信頼構築の実践的原則。Signals: 👍 upvote -->

- [ ] 219. https://quint-lang.org/posts/llm_era
  <!-- 仕様言語Quintを「AIコードの検証ポイント」に活用、複雑なシステム変更を数ヶ月→1週間に短縮。Signals: medium -->

- [ ] 253. https://passo.uno/new-habits-tech-writers-ai-age/
  <!-- テクニカルライターが「AIが参照する情報のアーキテクト」へ移行するという職種変容の視点。Signals: medium -->

- [x] 255. https://uxdesign.cc/the-hidden-cost-of-ai-design-tools-what-were-outsourcing-without-noticing-9057db75aaf9
  <!-- AIデザインツールが「美的モノカルチャー」と「共感の欠如」を招くという警告。Signals: medium -->

- [ ] 272. https://zenn.dev/nrs/articles/88f158aca0505b
  <!-- プロンプトをPersona・Policy等の部品に分離しSkillとしてデプロイ可能にするfaceted-prompting。Signals: medium -->

- [ ] 246. https://tellme.tokyo/post/2026/03/12/ai-coding-agent-rules/
  <!-- CLAUDE.mdとrules、AGENTS.mdの使い分けを各ツール横断で整理した実務ガイド。Signals: medium -->

- [x] 288. https://zenn.dev/rescuenow/articles/de42ef1e09aedb
  <!-- リリース3週間前にPython→TypeScriptをAIとテストコードで1週間で完遂した事例。Signals: medium -->

- [x] 218. https://lcamtuf.substack.com/p/how-much-of-hn-is-ai
  <!-- セキュリティ研究者がHNトップ記事のAI生成コンテンツ率を定量調査。Signals: medium -->

- [ ] 143. https://tech.layerx.co.jp/entry/2026/03/10/150000
  <!-- 逆方向生成、マルチエージェント品質管理等の高度な合成データ作成技法集。Signals: medium -->

- [ ] 214. https://p2ptk.org/ai/5458
  <!-- AIバブルの2兆ドルの不合理性を批判しつつ崩壊後の「最適化OSSモデル」こそ本命と論じるドクトロウ論考。Signals: medium -->

- [x] 180. https://llmock.copilotkit.dev/
  <!-- OpenAI/Claude/Gemini各APIを忠実再現する決定論的モックサーバー。Signals: medium -->

- [ ] 242. https://github.com/pbakaus/impeccable
  <!-- AIが生成しがちな凡庸デザインを回避する17コマンドのアンチパターン定義デザインスキル。Signals: medium -->

- [x] 245. https://github.com/tokoroten/prompt-review
  <!-- AI対話履歴からユーザーの技術理解度・プロンプト力を分析するAI時代のエンジニア評価ツール。Signals: medium, annex_flag -->

- [ ] 186. https://zenn.dev/syncable_tech/articles/2ddb940ade018d
  <!-- 2年放置のDB整合性問題をClaude Codeでスキーマ比較→2文SQLで解決した事例。Signals: medium -->

- [ ] 281. https://www.thegamer.com/gaming-site-videogamer-removed-google/
  <!-- 老舗ゲームメディアがAI記事＋架空編集者でGoogleからデインデックスされた事例。Signals: medium -->

- [ ] 223. https://libresolutions.network/articles/ai-regret/
  <!-- AIが集中型制御システムとしてデジタル自律性を侵食し、vibe codingが思考停止を招くという批判。Signals: medium, annex_flag -->

- [ ] 203. https://dev.henry.jp/entry/claude-code-skills-for-teams
  <!-- 個人Skillとチーム用Starter Kitの分離がClaude Codeのチーム展開の評価主観性と可搬性を解決。Signals: medium, annex_flag -->

- [ ] 211. https://github.blog/ai-and-ml/github-copilot/continuous-ai-for-accessibility-how-github-transforms-feedback-into-inclusion/
  <!-- GitHubがAIでアクセシビリティフィードバック処理を自動化、解決時間62%短縮・修正率89%達成。Signals: medium, annex_flag -->

- [x] 130. https://www.conor.fyi/writing/ai-access
  <!-- AI時代のアクセス権と格差について。Signals: medium, annex_flag -->

- [x] 185. https://zenn.dev/acntechjp/articles/efcc4f224cc8ca
  <!-- 16の脳科学的記憶メカニズム（感情ゲーティング、忘却曲線、連想記憶）をLLMに実装するプロジェクト。Signals: medium, annex_flag -->
