## Output StylesやAgent SkillsでClaude Codeの活用幅を広げる

https://www.wantedly.com/companies/wantedly/post_articles/1032201

ターミナル完結型のAIエージェント「Claude Code」を、Output StylesやAgent Skills、独自のプラグイン管理手法によって、コーディング以外の「思考・調査・自動化」の領域まで拡張する具体的な実践方法を提示する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Claude Code, AI Agent, LLM Workflows, Agent Skills, Developer Productivity]]

Wantedlyのバックエンドエンジニアである著者が、AnthropicのAIコーディングエージェント「Claude Code」を、単なるコード生成ツールを超えた「思考・調査・自動化」のパートナーとして活用するための高度なカスタマイズ手法を解説している。

著者は、Claude Codeが持つ「作業計画の立案」「コードベース探索」「ファイル編集」という自律的なループを、コーディング以外のタスクに転用することを提案している。中心となるのは「Output Styles」と「Agent Skills」の2つの機能だ。Output Stylesは、システムプロンプトを上書きすることで回答の方向性を制御する仕組みであり、著者はこれを利用してClaude Codeを対話重視の解説モード（Claude Desktop Style）や、課題分解に特化したエージェントへと切り替えて運用している。

また、特定の専門知識をAIに提供する「Agent Skills」の有用性についても詳しく触れている。ここでは、必要な時に必要なナレッジのみをコンテキストにロードする「Progressive Disclosure（段階的開示）」の仕組みが、限られたコンテキストウィンドウを有効活用する上で極めて重要であると、著者はその技術的合理性を強調している。

さらに、実践的な運用フローとして、SubagentsやAgent Skills、MCP（Model Context Protocol）サーバーなどを一元管理する「Private Plugins」の構成や、安全性を高めるための`settings.json`の設定例を紹介している。特に、エージェントによる誤削除を防ぐために標準の`rm`コマンドを拒否（deny）し、ゴミ箱への移動を行う`safe-rm`のみを許可（allow）する設定は、実務レベルでの安全性を考慮した具体的な知見である。

筆者は、Claude Codeの「ターミナルで完結する」というUnix哲学的な性質が、他のCLIツールやスクリプトとの組み合わせにおいて無限の可能性を秘めていると主張している。ツールの進化に合わせ、エージェント自体の定義やプラグインをClaude Code自身に生成・改善させるという「セルフホスティング」的な運用サイクルを回すことで、開発ワークフロー全体の自動化と高度化が実現できることを示唆している。