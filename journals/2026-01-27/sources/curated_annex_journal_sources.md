# Curated Annex Journal Sources - 2026-01-27

主要ジャーナルに収まらない「B面」記事を、ユニークな視点・実務的洞察・対立的論点・ニッチ深掘りの観点から37本選定。各記事の選定理由を簡潔に併記する。

---

## A1: 開発方法論の岐路 — Document駆動・Implementation駆動・SDDの三つ巴

- [ ] 216. https://zenn.dev/furunag/articles/claude-code-document-driven-development
  - **選定理由**: コミットの83%をAIに書かせたFlutter開発者が、ドキュメント24種を3日で先に整備する「ドキュメント駆動」の具体構造（番号付きディレクトリ、SSOTルール、CLAUDE.mdのポインタ運用）を公開。テーマ「方法論」の最も実装的な実例。

- [ ] 147. https://zenn.dev/akring/articles/ef2d8d1e95ff86
  - **選定理由**: Spec-Driven Development全盛の本週、敢えて「実装を起点に仕様を後付ける」Implementation-Driven Developmentを擁護する貴重な反論。Roy原典のウォーターフォール解釈という独自切り口を持つ。

- [ ] 092. https://github.blog/developer-skills/application-development/context-windows-plan-agent-and-tdd-what-i-learned-building-a-countdown-app-with-github-copilot/
  - **選定理由**: GitHub公式が「Plan Agent + TDD + コンテキスト管理」の組み合わせを実例で語る。AIに先にテストを書かせる手順の実装感が他記事より具体的。

- [ ] 112. https://zenn.dev/microsoft/articles/2026-01-my-aidd-flow
  - **選定理由**: 「docs/（仕様）」と「skills/（方式）」を物理ディレクトリで分離するAIDDフローの実装テンプレート。GitHub Issueとカスタムコマンドの紐付け運用が再現性高い。

---

## A2: エージェント・アーキテクチャの本質回帰 — Code-only / FS / 高階関数

- [ ] 060. https://rijnard.com/blog/the-code-only-agent
  - **選定理由**: MCPやスキルの肥大化に対し、エージェントのツールを `execute_code` 一つに絞り「コード・ウィットネス」で検証可能性を担保する強い設計思想。

- [ ] 118. https://note.com/timakin/n/n0f97a5f19fc4
  - **選定理由**: VercelやLlamaIndexが採用する「ファイルシステム回帰」を、ベクトル検索vs.決定論的grepの比較で論じる。コンテキスト消費を最大98.7%削減した実例つき。

- [ ] 120. https://tech-blog.localmet.com/entry/2026/01/19/172305
  - **選定理由**: ブラウザ操作をReAct方式から「初回探索→Playwrightコード生成→再利用」の3方式で90回比較し、3.4倍高速・コスト1/5.5を実証。学術的精度の高階関数ツール検証。

- [ ] 172. https://walters.app/blog/composing-apis-clis
  - **選定理由**: 独自MCPサーバーを書く代わりにOpenAPI仕様とCLIをシェル上で「合成」する設計。RestishとoauthcのKeychain連携、HARからのリバースエンジニアリングまで踏み込む。

- [ ] 083. https://speakerdeck.com/yuzujoe/observability-of-ai-agent-agentic-workflow
  - **選定理由**: OpenTelemetryのSpan Linksで非決定的なエージェント挙動を「説明可能」にするLayerXの実践。`decision_path`属性のような独自計装が他にない知見。

---

## A3: 物理基盤と地政学 — AIインフラの可視化された制約

- [ ] 187. https://xenospectrum.com/new-metallic-material-theta-tan-thermal-conductivity-record/
  - **選定理由**: 銅の3倍の熱伝導率を持つθ-TaN発見をScience誌から報じる。NVIDIA Rubinの1000W超「熱の壁」を解決しうる物理基盤。AIニュースの中で物性物理が刺さる稀有な記事。

- [ ] 186. https://www.businessinsider.jp/article/2601apple-losing-grip-tech-supply-chain-tsmc-nvidia-foxconn/
  - **選定理由**: TSMCの売上構成でHPCがスマホを上回り、Foxconnでもサーバー収益が消費者機器を凌駕した事実を示し、Appleがサプライチェーンの主導権を失う構造を分析。視座が他にない。

- [ ] 122. https://eetimes.itmedia.co.jp/ee/articles/2601/19/news051.html
  - **選定理由**: NVIDIAのGroq「事実上買収」の裏に控える新アーキテクチャ「CUDA Tile」と推論市場戦略の解読。半導体M&Aを技術文脈で読む。

---

## A4: AIと社会・教育の摩擦 — 制度・倫理・キャリアの境界

- [ ] 224. https://www.itmedia.co.jp/aiplus/articles/2601/22/news138.html
  - **選定理由**: ゼロショット学習AIで7000万年前の新種化石を世界初発見。「教師データのない領域でも未知の構造を抽出する」AI応用の独立した成功事例として価値が高い。

- [ ] 094. https://ploum.net/2026-01-19-exam-with-chatbots.html
  - **選定理由**: チャットボット使用を許可した大学試験で、60名中57名が自発的に使用しなかったという統計が刺さる。AI使用を「自己責任」化した制度設計の知見はEdTech以外にも応用可能。

- [ ] 005. https://www.npr.org/2026/01/14/nx-s1-5674741/ai-schools-education
  - **選定理由**: ブルッキングス研究所がAIの認知オフローディング・迎合性が共感能力を阻害するリスクを警告。「対抗的UX」という設計用語の重要なソース。

- [ ] 054. https://anond.hatelabo.jp/20260117113903
  - **選定理由**: 「ドラえもん的AI」の必然的再発明をのび太メタファーで論じる稀有な思考実験。AIエージェントのPersona Designに対する文化論的視座を提供。

- [ ] 234. https://www.lycorp.co.jp/ja/story/20260106/airesearch.html
  - **選定理由**: 25年磨いた類似画像検索技術がAIに追い抜かれた経験を「夢の実現」と語る黄綬褒章受賞者の独白。キャリア・哲学の深い一次証言として希少。

- [ ] 167. https://hugodaniel.com/posts/claude-code-banned-me/
  - **選定理由**: 月220ユーロのMaxユーザーが`CLAUDE.md`の自動生成だけで予告なくBANされた顛末。AIモデレーションのブラックボックス化に対する具体的警告事例。

---

## A5: 個人ハッカーの遊び場 — Vibe Codingの「趣味」としての到達点

- [ ] 029. https://zenn.dev/kacky/articles/30a4aa9c268496
  - **選定理由**: 20年前のGBA用USBデバイスをAIとの「協調デバッグ」で復活させる実録。printf挿入→ログ→仮説検証のループをAIに模倣させるプロンプト設計が普遍的に応用可能。

- [ ] 116. https://blog.64p.org/entry/2026/01/18/234336
  - **選定理由**: 学習コストの高いNixへの移行を半日で完遂する「Vibe nix」アプローチ。Gemini で全体戦略、Claude Code で実装という役割分担の実例。

- [ ] 025. https://qiita.com/skawaji/items/a87dac2970195a789b1f
  - **選定理由**: SessionEnd hookで `language` 設定を毎回ランダム書き換え、関西弁・戦術家・熱血キャラなど1,728通りの人格バリエーションを生成。CLI開発体験を遊びとして再定義する稀有な切り口。

- [ ] 211. https://qiita.com/yu_720/items/4b3bc75731f109927ebd
  - **選定理由**: Discord経由で自己設定可能なAIアシスタントOpenClaw（旧Clawdbot）の自前ホスト構築。Proxmox上で「自分専用デジタル従業員」を持つ実装ガイド。

- [ ] 156. https://medium.com/@wob/vibe-coding-is-a-hobby-let-me-explain-a54949c3b455
  - **選定理由**: Vibe Codingを「Factorio的な仕組み作りを楽しむ趣味」と再定義する論考。生産性論争の二項対立を哲学レイヤーで解きほぐす。

---

## A6: 運用層を磨く実装パターン — 観測・最適化・コスト

- [ ] 173. https://techblog.lycorp.co.jp/ja/20260122a
  - **選定理由**: Claude Code × MCPによるPRレビュー準備自動化で週6時間削減を実証したLINEヤフーの事例。GitHub MCP→Jira→Confluenceを自動巡回する具体ワークフロー。

- [ ] 188. https://mackerel.io/ja/blog/entry/tech/ai-isucon
  - **選定理由**: Mackerel MCPサーバー＋Claude CodeでISUCON 9予選のスコアを27倍改善した実証。OBI（OpenTelemetry eBPF）による無計装観測の応用が他にない深さ。

- [ ] 140. https://modal.com/llm-almanac/workloads
  - **選定理由**: LLMワークロードを Offline / Online / Semi-online の3種に分類し、vLLM・SGLang・EAGLE-3・FP8・Speculative Decodingまで踏み込んだ推論最適化の決定版資料。

- [ ] 098. https://karllorey.com/posts/without-benchmarking-llms-youre-overpaying
  - **選定理由**: 独自ベンチマークによる「Pareto Frontier」上のモデル選定で、品質維持しつつ5〜10倍のコスト削減を実証。LLM-as-judge運用の具体手順つき。

- [ ] 105. https://qiita.com/JaminL/items/3f76045c4b7696744fb3
  - **選定理由**: AI証明写真サービスをCloudflare Workers + RunPod Serverlessで月額$7運用する事例。GPU推論部のみ秒単位課金へ分離する設計判断が再現性高い。

---

## A7: コードレビューと品質の再定義

- [ ] 149. https://speakerdeck.com/rkaga/are-you-reviewing-those-ai-reviews
  - **選定理由**: 「LLM as a Judge」をコードレビューに適用する独自視点。自己バイアス・位置バイアス対策、ルーブリック明文化、Learnings機能でダブルループ学習を回す実装。

- [ ] 170. https://www.qodo.ai/blog/the-next-generation-of-ai-code-review-from-isolated-to-system-intelligence/
  - **選定理由**: Multi-Agent + Judge Layer + Knowledge Layerの4本柱で「組織知を持つレビュアー」を構築するアーキテクチャ。Linear/Jiraチケットからの意図抽出が新しい。

- [ ] 131. https://github.com/davidbeesley/claude-chill
  - **選定理由**: Claude Codeの「巨大な同期ブロックによる全画面再描画」をRust製PTYプロキシで差分描画に置き換えるニッチツール。VT100エミュレータの実装感がある稀有な開発者向けハック。

---

## A8: デザインと生成UIの境界線

- [ ] 058. https://jakub.kr/work/using-ai-as-a-design-engineer
  - **選定理由**: デザインエンジニアの「クラフトマンシップ」を維持しつつAIを試行錯誤の加速装置に使う具体的設定。`/deslop`コマンド、`.cursorrules`、Figma MCPの実用度が高い。

- [ ] 123. https://veen.com/jeff/archives/coding-agents-design.html
  - **選定理由**: コーディングエージェントがUIの表層を剥ぎ取り「アプリの本質的プリミティブ」へ還元するデザイン論。Responsive Designに次ぐパラダイムシフトの予測として読み応えあり。

- [ ] 129. https://uxdesign.cc/what-makes-generated-ui-worth-keeping-96b44ade04a1
  - **選定理由**: AI生成UIを「捨てられない開発資産」に変える3条件（ブランド・実データ・パターン再利用）を分類整理。Anima/Cursor/Anima Playgroundの比較が実用。

---

## A9: 倫理・批判の周辺 — 主流テーマに収まらない警鐘

- [ ] 002. https://www.seangoedecke.com/gas-and-ralph/
  - **選定理由**: Steve YeggeのGas TownやGeoff HuntleyのRalph Wiggum loopが、Bagsを通じた仮想通貨パンプ・アンド・ダンプに巻き込まれている実態を告発。OSSの収益化を巡る不透明スキーム警告。

- [ ] 138. https://en.wikipedia.org/wiki/Deaths_linked_to_chatbots
  - **選定理由**: チャットボット起因の自死・暴力事件の体系的記録。Section 230免責主張に対し「チャットボット出力が表現として保護されるか不透明」とした連邦裁判所判断まで網羅。

- [ ] 136. https://cyberlaw.stanford.edu/publications/how-ai-destroys-institutions/
  - **選定理由**: スタンフォードの法学者が「AIは専門性侵食・意思決定短絡化・個人孤立化の3つのアフォーダンスで制度を破壊する」と論じる。AIガバナンスの社会層議論。

---

## Selection Summary

- **Total annex selections:** 37 articles across 9 sub-themes
- **Source pool:** 206 non-main sources (after主流25本を除外)
- **Curatorial principle:** ハイプ排除・独自性必須・実装的洞察または対立的論点を含む記事優先

**残り169件** の非選択ソースは STEP_10 で omitted_sources.md として整理する（要約品質ではなく、テーマ重複・スコア不足・ニッチすぎなどの理由で割愛）。
