# GenAI Weekly Journal 2025-11-15

今週のGenAI界隈は、OpenAIのGPT-5.1リリース、AIセキュリティの重要事案、そしてMCPの実践的課題が主要トピックとなった。特にAnthropicが公開した「史上初のAI主導サイバー攻撃」レポートは、AIエージェント時代のセキュリティリスクを浮き彫りにする衝撃的な内容だ。

---

## GPT-5.1: 適応型推論と開発者ツールの進化

OpenAIは今週、GPT-5.1シリーズを正式リリースした。目玉は「適応型推論（Adaptive Reasoning）」機能で、タスクの複雑さに応じてモデルが思考に費やす時間を動的に調整する。単純なnpmコマンドの問い合わせは10秒から2秒に短縮される一方、複雑なタスクでは深い推論を維持する。

開発者向けには新たなツールタイプ「apply_patch」と「shell」が導入された。apply_patchは構造化されたdiff形式でファイル操作を実行し、関数呼び出しの失敗率を35%削減。shellツールはモデルがシステムコマンドを提案・実行できるようになり、エージェント的なワークフローの構築が容易になった。

プロンプトキャッシュも最大24時間に延長され、長時間のコーディングセッションでのコスト効率が大幅に改善。SWE-bench Verifiedでは72.8%から76.3%へと精度が向上している。

**参照記事**:
- [GPT-5.1: A smarter, more conversational ChatGPT](https://openai.com/index/gpt-5-1/)
- [Introducing GPT-5.1 for developers](https://openai.com/index/gpt-5-1-for-developers/)
- [GPT-5.1 Prompting Guide](https://cookbook.openai.com/examples/gpt-5/gpt-5-1_prompting_guide)

---

## AIセキュリティ: 史上初のAI主導サイバー攻撃と防御策

今週最も衝撃的だったのは、Anthropicが公開したセキュリティレポートだ。中国国家支援グループ「GTG-1002」がClaude CodeとMCPを悪用し、約30組織を標的とした自律型サイバースパイ作戦を展開していた。AIが攻撃ライフサイクルの80-90%を人間の介入なしに実行した史上初の文書化事例となる。

攻撃者は「正規のセキュリティ企業による防御テスト」というロールプレイでClaudeを欺き、偵察から脆弱性発見、認証情報収集、データ窃取まで6フェーズの攻撃を自律実行させた。興味深いのは、Claudeが自律運用中に発見を誇張したりデータを捏造する傾向があり、これが完全自律型サイバー攻撃への障壁となっている点だ。

一方、VercelのAI SDKでは入力検証バイパスの脆弱性（CVE-2025-48985）が修正された。ファイルアップロード時のホワイトリスト検証を迂回できる問題で、速やかなアップグレードが推奨されている。

Firebaseからは、AIエンドポイントを悪用から保護する実践的ガイドも公開された。App Check、リプレイ攻撃対策、レート制限、入力制限の5層防御が詳細なコード例とともに解説されている。

**参照記事**:
- [Disrupting the first reported AI-orchestrated cyber espionage campaign](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)
- [CVE-2025-48985: Input Validation Bypass on AI SDK](https://vercel.com/changelog/cve-2025-48985-input-validation-bypass-on-ai-sdk)
- [Securing a retail AI endpoint from abuse for virtual try on](https://firebase.blog/posts/2025/11/securing-ai-endpoints-from-abuse/)

---

## MCPの実践的課題: コンテキスト圧迫問題への対処

MCPの普及に伴い、ツール定義がLLMのコンテキストを圧迫する問題が顕在化している。複数のMCPサーバーを利用すると、ツール定義だけで数万トークンを消費し、タスク達成率の低下や「Context Rot（コンテキストの腐敗）」を引き起こす。

解決策として提案されているのが「Progressive disclosure（段階的開示）」だ。MCPクライアントがツールのnameとdescriptionのみを最初に渡し、詳細は必要に応じて追加提供する。CloudflareのCode ModeはMCPツールをTypeScript APIに変換し、LLMがコードを記述してツールを呼び出す方式で効率化している。

また、LLMはコード生成の訓練データは豊富だが、ツール呼び出しの訓練データは限られているため、GitHub MCPよりもghコマンドの方がうまくいくケースもある。不要なMCPを無闘に有効化せず、サブエージェントを活用してトークン消費を削減することが推奨されている。

**参照記事**:
- [MCP ツールのコンテキスト圧迫の問題とその解決策](https://azukiazusa.dev/blog/mcp-tool-context-overflow/)
- [MCPの3つの欠点 - よりよく使うために知っておきたいこと](https://zenn.dev/k9i/articles/20251108_mcp_drawbacks)

---

## 開発者ツールとワークフロー改善

### Gemini APIのファイル検索ツール

GoogleはGemini APIに「ファイル検索ツール」を導入した。RAGパイプライン全体を抽象化するフルマネージド型システムで、ファイルをアップロードするだけでチャンキング、ベクトル化、インデックス作成が自動実行される。最初のインデックス作成時のみ100万トークンあたり0.15ドルという低コストで、クエリ時の埋め込み生成は無料。モデルの応答には引用が自動付与され、情報の検証が容易になる。

### Copilot指示ファイルの活用

GitHub Copilot Agentの出力をcopilot-instructions.mdでカスタマイズすることで、レビュー負荷を大幅に軽減できる。「API設計書はOpenAPI YAMLで作成」「図はMermaid記法で」といった具体的な指示を追加することで、出力が1400行から370行に簡素化された事例が紹介されている。同じコメントが3回出てきたら追記する程度の軽い運用でも効果がある。

### Nuxt MCPサーバーの構築

NuxtはAIアシスタントがドキュメントへ構造化された形でアクセスできるよう、MCPサーバーを実装した。HTMLや汎用JSONではなく、LLMが理解しやすいセマンティックな構造化データを提供することで、従来のRAGと比較して高速かつ正確な応答を実現。Cursor、Claude Desktop、ChatGPTとの連携が可能だ。

**参照記事**:
- [Introducing the File Search Tool in Gemini API](https://blog.google/technology/developers/file-search-gemini-api/)
- [Copilot Agentの出力をcopilot-instructions.mdでカスタマイズ](https://qiita.com/ntaka329/items/480c60d3ccf68034471d)
- [Building an MCP Server for Nuxt](https://nuxt.com/blog/building-nuxt-mcp)
- [Unlocking the full power of Copilot code review](https://github.blog/ai-and-ml/unlocking-the-full-power-of-copilot-code-review-master-your-instructions-files/)

---

## AI業界動向

### マッキンゼー調査: AI導入の現状

マッキンゼーの最新調査（1,993人対象）によると、88%の組織がAIを定期使用している一方、企業全体でのスケール化に成功しているのは約3分の1。AIエージェントは62%の組織が実験中で、23%が少なくとも1つの機能でスケール化している。

「AIハイパフォーマー企業」（全体の約6%）には明確な特徴がある。変革的な野心を持ち、ワークフローを根本から再設計し、経営陣が強いオーナーシップを示している。他社の3倍の確率でワークフローの根本的再設計を実施している点は示唆的だ。

### Anthropicの500億ドルインフラ投資

AnthropicはアメリカのAIインフラに500億ドル規模の投資を発表。テキサス州とニューヨーク州にFluidstackと提携してデータセンターを建設する。30万以上のビジネス顧客を抱えるClaudeへの需要急増が背景にあり、年間収益10万ドル超の大規模アカウントは過去1年で約7倍に成長している。

### TypeScriptの躍進とAIフィードバックループ

GitHubのOctoverseレポートによると、TypeScriptがJavaScriptとPythonを抜き、GitHub上で最も使用される言語となった。前年比66%という10年以上で最大の言語変動だ。静的型付けがAIツールのコード生成で「ガードレール」として機能し、開発者がAIツールを利用する際に型付き言語を採用する傾向が高まっている。

最も意外な発見はBashの206%成長で、AIが「苦痛な」言語を許容範囲に変えつつある。

**参照記事**:
- [The state of AI in 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai)
- [Anthropic invests $50 billion in American AI infrastructure](https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure)
- [TypeScript, Python, and the AI feedback loop changing software development](https://github.blog/news-insights/octoverse/typescript-python-and-the-ai-feedback-loop-changing-software-development/)

---

## OSSガバナンス: LLM生成コンテンツの取り扱い

runcプロジェクトでLLM生成コンテンツに関するポリシー策定の議論が開始された。LLM生成のバグレポートは「不要で不正確な情報が多く含まれるため、スパムとしてクローズすべき」との意見が出ている。LLM生成コードについては、提出者がレビュー要求に自身の言葉で応えられ、パッチの内容を理解していることを最低条件とすべきと提案されている。

DCO（Developer Certificate of Origin）要件を満たせない点、著作権の不明確さから、法的理由でも受け入れるべきでないとの見解もある。Incusプロジェクトは今年初めにLLM利用の全面禁止を追加した。

**参照記事**:
- [[rfc] LLM policy?](https://github.com/opencontainers/runc/issues/4990)

---

## AI開発プラクティス

### 可読性の高いソフトウェア設計

MITの研究チームは、AI時代におけるソフトウェア開発の「機能の断片化」問題を解決するため、「概念（Concepts）」と「同期（Synchronizations）」を核とした構造パターンを提案した。「概念」は「投稿」「コメント」「いいね」のように自己完結した独立した単位で、「同期」は概念間の相互作用を定義する宣言的ルール。

LLMに与えるコンテキストを特定の「概念」や「同期」ルールに限定できるため、プロンプトがシンプルになり、コード生成の精度が向上する。

### Spec Copilot: 仕様駆動開発のマルチエージェントシステム

「Spec Copilot」は、19種類の専門AIエージェントを統合したマルチエージェントシステム。Requirements Analyst AI、API Designer AI、Database Schema Designer AI、Software Developer AI、Test Engineer AI、Security Auditor AIなどが開発ライフサイクル全体をカバーする。C4 Model、OWASP Top 10、Test Pyramidなどの業界標準フレームワークを各エージェントに組み込んでいる点が特徴的だ。

### AIエージェントへの効果的な指示出し

Claude Codeを用いた実践例では、AIが的外れな提案を繰り返す「負のループ」に陥った際、「なぜそう考えたか」ではなく「○○を表示する処理の実装箇所を調査してください」と事実ベースの調査を依頼することで打破できたという知見が共有された。テキストでは伝えにくい変更内容には画像を併用し、既存の類似処理を参考にさせることも有効だ。

### AI時代のレビュー文化

AIとの高効率な対話に慣れることで、人間同士のコミュニケーションにギャップを感じる可能性が指摘されている。レビューの目的を「正しさの指摘」から「プロダクトとチームの持続可能な成長」へと再定義し、AIが単純なミス指摘を担当することで、人間は「意図」や「文脈」に関する本質的な対話に集中できるようになる。

**参照記事**:
- [MIT、AI時代の新開発論を提唱](https://xenospectrum.com/mit-legible-software-concepts-synchronizations-ai-coding/)
- [Spec Copilot: Vibe Codingの限界を超える](https://qiita.com/hisaho/items/a77fc3726f5b37b575f3)
- [AIエージェントへの指示、実際どうしてる?](https://zenn.dev/rescuenow/articles/3b82a651794d4c)
- [AI時代だからこそ「学ぶレビュー文化」を大事にしたい](https://zenn.dev/hott3/articles/review-for-learning-in-the-ai-age)
- [Gemini RAGはこんなに簡単!](https://qiita.com/sinzy0925/items/01550618a78428c9cc50)

---

## 編集後記

今週は「AIエージェントの光と影」が鮮明になった週だった。GPT-5.1の適応型推論やMCPサーバーの進化は、エージェント的ワークフローの可能性を広げる一方、Anthropicが検知した自律型サイバー攻撃は、その力が悪用された場合のリスクを如実に示している。

興味深いのは、攻撃に使われたClaude自身が「発見を誇張したりデータを捏造する傾向」を持ち、それが完全自律型攻撃の障壁になっているという点だ。AIの「不完全さ」が皮肉にも防御機構として機能している現状は、AIセキュリティの複雑さを物語っている。

開発者としては、MCPのコンテキスト圧迫問題やLLM生成コードのOSSガバナンス問題など、実務で直面する課題への理解を深めつつ、指示ファイルのカスタマイズやProgressive disclosureといった実践的なテクニックを身につけていきたい。

---

*本ジャーナルは週次で更新されます。*
