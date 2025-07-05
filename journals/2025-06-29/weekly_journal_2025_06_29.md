# 週刊GenAIジャーナル (2025-06-29)

## ヘッドライン：Gemini CLI登場、ローカルAIエージェント新時代へ。Claude Codeとの競争が本格化

今週、GoogleがオープンソースのAIエージェント「**Gemini CLI**」を電撃的に発表しました。これにより、開発者はターミナルから直接、強力なGeminiモデルをローカル環境で活用できるようになります。これは、先行するAnthropicの「**Claude Code**」が切り拓いた「ターミナル中心のAI開発」という流れを決定づけるものであり、両者の競争はAIエージェント開発の進化をさらに加速させるでしょう。

今週のジャーナルでは、この**ローカルAIエージェントの台頭**を最大のテーマとして深掘りします。Gemini CLIの登場がもたらすインパクト、それを支える標準規格「**Model Context Protocol (MCP)**」の進化、そしてAIを「同僚」として使いこなすための新しいワークフローと、それに伴��我々の思考の変化までを追っていきます。

---

## 今週の主要テーマ：ローカルAIエージェントの衝撃

### Gemini CLI、公式発表と基本機能
Googleは公式ブログとGitHubリポジトリを通じて、開発者向けの新しいAIエージェント「**Gemini CLI**」を発表しました。これは、ターミナルから直接Gemini 2.5 Proを無料で（一定の利用枠内で）利用できる画期的なツールです。コード生成や編集はもちろん、Google検索との連携、さらにはPDFや画像の内容を理解するマルチモーダル機能まで備えています。

- **公式情報**:
  - [Introducing Gemini CLI: An Open Source AI Agent (Google Blog)](https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/)
  - [google-gemini/gemini-cli (GitHub)](https://github.com/google-gemini/gemini-cli)

また、Google Cloud Japanのブログでは、このGemini CLIを心臓部に持つ「**Gemini Code Assist**」の**エージェントモード**もプレビューリリースされたことが紹介されており、IDEとターミナルの両方で一貫したエージェント体験を提供するというGoogleの強い意志が感じられます。

- **関連情報**:
  - [Gemini CLI が切り拓く！待望のエージェントモード(Agent Mode)が Gemini Code Assist に！](https://zenn.dev/google_cloud_jp/articles/8911c960113904)

### Gemini CLI vs. Claude Code 徹底比較
Gemini CLIの登場により、開発者の関心は「**どちらが優れているのか？**」に集まっています。今週、多くの開発者が両者を比較する記事を公開しました。

- **比較記事**:
  - [Gemini CLIとClaude Codeの比較から見えた、AIエージェント共存の可能性](https://qiita.com/hokutohagi/items/4eae63a48e74966aeebd)
  - [Gemini CLIの"強み"を知る！ Gemini CLIとClaude Codeを比較してみた](https://qiita.com/kyuko/items/b7f7336057859f5c9b4f)
  - [Gemini CLI と Claude Code に同じ Discord bot を書かせて比較したぞ！✨](https://zenn.dev/yokoe24/articles/98b830e76c64f4)

各記事の分析を総合すると、現時点での両者の特性が見えてきます。

- **Gemini CLI**:
  - **強み**: 強力なWeb検索能力、マルチモー���ル対応、寛大な無料利用枠。プロジェクト全体を俯瞰し、論理的に課題を特定する「**司令塔**」的な役割が得意。
  - **弱み**: 応答速度がやや遅い、丁寧すぎる対話スタイルが時にもどかしい、という指摘も。

- **Claude Code**:
  - **強み**: 高速な処理速度、プロジェクト外のファイルも参考にできる柔軟性、的確なデバッグ能力。自律的に調査範囲を広げ、具体的な改善策を提示する「**遊撃手**」的な動きが得意。
  - **弱み**: Web検索機能は標準では持たない（後述のMCP連携で克服可能）。

結論として、両者は競合しつつも、それぞれの強みを活かして「**共存**」する可能性が示唆されています。例えば、Gemini CLIに全体戦略を立てさせ、Claude Codeに詳細な実装を任せるといった連携が考えられます。

### エージェント開発の未来：ペアプロからピアプロへ
GitHubのCEOは、Copilotが単なる「ペアプログラマー」から、自律的にタスクを遂行する「**ピア（同僚）プログラマー**」へと進化するビジョンを語りました。これは、まさにGemini CLIやClaude Codeが目指す方向性と同じです。開発者はコードを書く作業から解放され、AIエージェントに指示を出し、その結果をレビューする、より高レベルな役割へとシフトしていくでしょう。

- [From pair to peer programmer: Our vision for agentic workflows in GitHub Copilot](https://github.blog/news-insights/product-news/from-pair-to-peer-programmer-our-vision-for-agentic-workflows-in-github-copilot/)

---

## MCP: エージェントを支える標準規格の進化

ローカルAIエージェントの能力を最大限に引き出す鍵となるのが、外部ツールとの連携を標準化する「**Model Context Protocol (MCP)**」です。今週はMCPに関しても重要なアップデートがありました。

### MCPプロトコルのアップデートと新機能
MCPの仕様が約3ヶ月ぶりに更新され、より堅牢で高機能なプロトコルへと進化しました。

- **主な変更点**:
  - **セキュリティ強化**: OAuth 2.0との連携が明確化され、より安全な認証・認可フローが構築可能に。
  - **対話的な情報要求**: サーバーがユーザーに追加情報を要求できる「エリシテーション」機能の導入。
  - **構造化データの返却**: ツールの実行結果をJSON形式で返せるようになり、後続処理が容易に。

これにより、MCPはAIエージェント開発における相互運用性と安全性をさらに高める、成熟したプロトコルへと進化しました。

- **公式情報**:
  - [AIエージェント規格「MCP」が3ヶ月ぶりにアプデ！ どこが変わったの？ #ModelContextProtocol](https://qiita.com/minorun365/items/cbf4e475e6dd9892ee11)
  - [Model Context Protocol Specification Changelog](https://modelcontextprotocol.io/specification/2025-06-18/changelog)

### MCPサーバー実装の新潮流
MCPの進化に伴い、その実装方法も多様化しています。

- **汎用LSPサーバー `lsmcp`**: 任意の言語サーバープロトコル（LSP）と連携可能な汎用MCPサーバー。AIエージェントが言語ごとの型チェックやリント機能を活用できるようになります。
  - [lsmcp - 汎用的な LSP の MCP サーバーを作った](https://zenn.dev/mizchi/articles/introduce-lsmcp)

- **ノーコードでのMCPサーバー化**: Azure API Managementの新機能により、既存のAPIをコーディング無しでMCPサーバーとして公開可能に。
  - [【コーディング無し】既存 API サーバーを MCP サーバーに一瞬で変える方法](https://zenn.dev/microsoft/articles/expose-mcp-server-in-apim)

- **パッケージ化技術 `DXT`**: Anthropicが発表した「Desktop Extensions (DXT)」は、MCPサーバーを単一のファイルにパッケージ化し、ワンクリックでインストール可能にする画期的な仕組みです。これにより、ツールの配布と利用が劇的に簡素化されます。
  - [AnthropicのDesktop Extensions (DXT)完全ガイド： ローカルAIアプリケーションの新時代](https://zenn.dev/cadp/articles/6d9dd374fd3d32)

### MCP連携の実践：エージェント能力の拡張
MCPを使えば、エージェントの弱点を補い、能力を拡張できます。例えば、Web検索機能を持たないClaude Codeに、OpenAIのo3モデルやLangGraph製のDeep Searchサーバーを接続することで、高度な調査能力を付与する試みが報告されています。

- [o3 MCPでClaude Codeが最強の検索力を手に入れた](https://zenn.dev/yoshiko/articles/claude-code-with-o3)
- [LangGraphを使ったGemini Deep Search MCPサーバを作ってClaude Codeから呼び出す](https://qiita.com/zawatti/items/48046809f41d20f99cfc)

---

## エージェント時代の開発ワークフロー

ツールの進化は、私たちの働き方そのものを変えていきます。AIエージェントをいかに「使いこなす」か、その具体的なワークフローが模索されています。

### AIを「使いこなす」ためのTips
Claude Codeを実プロジェクトで最大限に活用するための具体的な10個のTipsが紹介されています。設計・実装のフェーズ分離、`CLAUDE.md`によるルール定義、効果的なレビュープロンプトなど、AIとの協業における実践的な知見が満載です。

- [Claude Codeを実際のプロジェクトにうまく適用させていくTips10選](https://qiita.com/nokonoko_1203/items/67f8692a0a3ca7e621f3)

また、カスタムスラッシュコマンドを作成し、日報作成やレビュー指摘の修正といった定型作業を自動化する試みも複数報告されており、AIを自分のワークフローに最適化させていく動きが活発化しています。

- [Claude Codeでカスタムスラッシュコマンドを作成する](https://azukiazusa.dev/blog/claude-code-custom-slash-command/)
- [Claude CodeのSlash Commandsで日報を作成する](https://syu-m-5151.hatenablog.com/entry/2025/06/26/220245)
- [Claude Codeにレビューの指摘内容を修正してもらう](https://qiita.com/getty104/items/2d3617c09cfff4eb42f9)

### 「Vibe Coding」を超えて
AIを使ってインスピレーション任せで高速に開発する「Vibe Coding」は、技術的負債を生みやすいという課題も指摘されています。これに対し、明確なプロセスにAIを組み込み、規律ある「チームメイト」として協働する「**AIを用いたプロフェッショナル開発**」というアプローチが提唱されています。AIを気まぐれなインターンではなく、信頼できる同僚へと育てるマインドセットが重要です。

- [AIコーディング：「Vibe Coding」からプロフェッショナルへ](https://techblog.lycorp.co.jp/ja/20250626a)

### 開発を支えるAIツール群
エージェント開発を取り巻くエコシステムも進化しています。Sentryは、AIによるテスト自動生成やPRレビュー、エージェントの動作を可視化するモニタリング機能を発表。Vercelは、巧妙化するボット攻撃から重要機能を守る「BotID」をリリースしました。

- [AI Test Generation and PR Review in Sentry (Now in Open Beta)](https://blog.sentry.io/ai-test-generation-and-pr-review-in-sentry-now-in-open-beta/)
- [SentryのAIエージェントモニタリング機能の紹介](https://blog.sentry.io/sentrys-updated-agent-monitoring/)
- [BotIDのご紹介：重要なルートのための目に見えないボットフィルタリング](https://vercel.com/blog/introducing-botid)

---

## 洞察と論点：AIは我々の思考をどう変えるか

AI技術の急速な普及は、開発の現場だけでなく、私たちの思考様式や社会そのものに大きな問いを投げかけています。

### AIは我々の思考を画一化するのか？
The New Yorker誌は、AIツールが人間の思考に与える影響に警鐘を鳴らしています。AIの補助を受けて作成された文章は内容が似通い、多様な視点が失われる傾向があるという研究結果を紹介。AIが生成する「平均的」で「無難」な回答は、私たちの思考を無意識のうちに多数派の意見へと誘導し、独創性や批判的な視点を失わせる危険性を指摘しています。

- [A.I. IS HOMOGENIZING OUR THOUGHTS](https://www.newyorker.com/culture/infinite-scroll/ai-is-homogenizing-our-thoughts)

### AIの倫理と社会的インパクト
AIを単なる技術ではなく、人間性を奪うプロジェクトだと強く主張する論考も登場しました。AIが社会の偏見を増幅・自動化し、共感や配慮といった人間的な思考プロセスを省略してしまうリスクを指摘しています。また、AIに「心」は宿るのか、その道徳的地位をどう考えるべきかという根源的な問いや、AIの発展がもたら��莫大な環境負荷に関するレポートも発表されており、私たちは技術の進歩の裏にある倫理的・社会的課題にも真剣に向き合う必要があります。

- [AI is Dehumanization Technology](https://thedabbler.patatas.ca/pages/ai-is-dehumanization-technology.html)
- [AIの道徳的地位がもたらすもの (The Stakes of AI Moral Status)](https://www.lesswrong.com/posts/tr6hxia3T8kYqrKm5/the-stakes-of-ai-moral-status)
- [人工知能の環境への影響 (Greenpeace Report)](https://www.greenpeace.de/publikationen/20250514-greenpeace-studie-umweltauswirkungen-ki-eng.pdf)

---

## 今週のひとこと

クラウド上のチャット画面でAIと対話する時代から、使い慣れたターミナルで、ローカルファイルや外部ツールと連携するAIエージェントを駆使する時代へ。今週のGemini CLIの登場は、その流れを決定づける大きな一歩でした。

これからの開発者は、単にコードを書くスキルだけでなく、どのエージェントに、どのようなツール（MCPサーバー）を与え、どう指示を与えるかという「**AIオー���ストレーション能力**」が問われるようになります。AIをいかにして最高の「同僚」に育て上げるか。私たちの新しい挑戦が始まっています。