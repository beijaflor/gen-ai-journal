# Curated Annex Journal Sources - 2026-01-06

## Advanced Tactics & Unconventional Wisdom

- [ ] 025. https://nowokay.hatenablog.com/entry/2025/12/28/045145
<!-- 編集コメント: 規約ベースのフレームワーク（Rails等）がAI時代に不利だという、LLMのAttention特性を数理的根拠に基づいて論じた独自の視点。設定より規約という長年のベストプラクティスを、AIにとっての扱いやすさという観点から再評価する斬新なアプローチ。 -->

- [ ] 031. https://azukiazusa.dev/blog/enable-claude-code-tool-search-to-reduce-mcp-token-usage/
<!-- 編集コメント: MCPツールのトークン消費を90%削減する環境変数 `ENABLE_TOOL_SEARCH=true` の実装解説。公式ドキュメント未記載の実験的機能を実戦投入する高度な最適化テクニック。 -->

- [ ] 033. https://qiita.com/riiiii/items/b642f039c30d4e9c1bec
<!-- 編集コメント: Claude Codeを3ヶ月実務投入した結果から得た「セッション間の忘却対策」「設計密度の重要性」「類似機能のまとめ実装」など、AIエージェント運用における実践的な5つの教訓。理論ではなく現場の痛みから生まれた知見。 -->

- [ ] 040. https://qiita.com/qwer123123/items/2f1db6bd52f2e05eb524
<!-- 編集コメント: Transformerの数理的特性に基づき、プロンプトを「Role」「Goal」「Constraints」「Output」の4要素に完全分解する構造化手法。LLMの挙動を予測可能なシステムコンポーネントとして制御したいエンジニア向けの実用的リファレンス。 -->

- [ ] 073. https://techblog.kayac.com/2025/12/24/100000
<!-- 編集コメント: AIエージェントにSOLID原則を徹底的に叩き込むことで、設計品質を劇的に向上させた新卒エンジニアの実践報告。AIに「何を作らせるか」ではなく「どう作らせるか」を定義する高度なプロンプトエンジニアリング。 -->

## Substantive Critique & Contrarian Views

- [ ] 012. https://teodordyakov.github.io/brainfuck-agi/
<!-- 編集コメント: データが希少な難解言語「Brainf*ck」こそがLLMの真の推論能力を測る究極のベンチマークだとする、挑発的かつ論理的な提言。パターン模倣を無効化し、純粋な論理推論を要求する視点が独創的。 -->

- [ ] 027. https://theconversation.com/the-doorman-fallacy-why-careless-adoption-of-ai-backfires-so-easily-268380
<!-- 編集コメント: 人間の仕事を単純タスクに還元してAIに置き換える「ドアマンの謬見」を指摘。オーストラリア・コモンウェルス銀行の解雇撤回など、AI導入の失敗事例を通じた辛辣な警告。 -->

- [ ] 028. https://syu-m-5151.hatenablog.com/entry/2025/12/27/140231
<!-- 編集コメント: AI時代だからこそ要件定義が重要だという逆説。AIが「作る」を10倍速くするなら、間違ったものを10倍速く作らないための「選ぶ」作業の重みが増す。痛みを伴う意思決定こそ人間の聖域という主張。 -->

- [ ] 030. https://fortune.com/2025/12/25/cursor-ceo-michael-truell-vibe-coding-warning-generative-ai-assistant/
<!-- 編集コメント: CursorのCEO自らが「バイブ・コーディング」の危険性を警告。AIに丸投げして中身を確認しないと、脆弱な基盤の上にシステムが崩壊すると指摘する内部者からの警鐘。 -->

- [ ] 088. https://takagi-hiromitsu.jp/diary/20251227.html
<!-- 編集コメント: 政府のAIプリンシプル・コード案を、金融業界規範の劣化コピーと断じる痛烈な批判。最上位目的の欠如と論理的破綻を、LLMによる比較分析で暴く高木浩光氏の鋭い論考。 -->

## Niche Explorations & Deep Dives

- [ ] 026. https://note.com/cyberagent_ai/n/n111eaa3b772c
<!-- 編集コメント: Gemma Scope 2を用いてLLMの内部表現を解剖し、アニメ・漫画の過剰拒絶問題を可視化。疎自己符号化器（SAE）という高度な解釈可能性ツールを実戦投入した技術的深掘り。 -->

- [ ] 048. https://zenn.dev/oharu121/articles/efd3d038afc6da
<!-- 編集コメント: RAGの精度を73%から100%へ改善したチャンキング戦略の詳細検証。リランクが逆効果になる条件や、ドキュメント再構成の重要性など、実務で直面する課題への具体解。 -->

- [ ] 075. https://www.deeeet.com/writing/exe-dev
<!-- 編集コメント: AI時代の「Just in Time Software」を実現するVMホスティング「exe.dev」の紹介。Tailscale元CTOによる、AIエージェント時代のインフラ設計思想を深掘り。 -->

- [ ] 079. https://tdx.treasuredata.com/guide/td-skills.html
<!-- 編集コメント: Treasure Data特有のTrino/Hive関数やDigdagワークフローをClaude Codeで扱うための専用スキル群。ドメイン特化型AIツールの実装パターンとして参考になるニッチな事例。 -->

- [ ] 081. https://github.com/MarkShawn2020/lovcode
<!-- 編集コメント: Claude Codeの対話履歴やMCP設定をGUIで統合管理するTauri製デスクトップアプリ。CLIツールの限界を補完する、AIワークフロー管理の新しいアプローチ。 -->

- [ ] 086. https://github.com/breaking-brake/cc-wf-studio
<!-- 編集コメント: Claude Code用のビジュアルワークフローエディタ。MCP連携、条件分岐、サブエージェントをドラッグ＆ドロップで設計し、自然言語で微調整できる革新的ツール。 -->

## Technical Deep Dives

- [ ] 042. https://qiita.com/moritalous/items/bd4e1cdfadb80b04065a
<!-- 編集コメント: Claude Agent SDKとAmazon Bedrock AgentCoreを組み合わせ、エージェント構築の標準解を提示。MCPやスキル開発に注力できるアーキテクチャの実装ガイド。 -->

- [ ] 083. https://zenn.dev/openjny/articles/43e010c65faa9a
<!-- 編集コメント: GitHub Copilot Chatの「Plan」モードが、実はカスタムエージェントのラッパーであることをソースコードレベルで解明。VS Codeの拡張機構を深掘りした技術考察。 -->
