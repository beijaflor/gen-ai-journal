## AIエージェントによるコード変更の背景と履歴を記録する共通規格「Agent Trace」が提唱

https://www.publickey1.jp/blog/26/aiagent_tracecursorcognitiongoogle_jules.html

統一フォーマットでAIによるコード変更の背景と履歴を記録し、ツール間の相互運用性と透明性を高める共通規格「Agent Trace」を提唱する。

**Content Type**: 📰 News & Announcements
**Language**: ja

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 81/100 | **Overall**: 80/100

**Topics**: [[Agent Trace, Cursor, AIエージェント, コーディング標準, コード履歴管理]]

**Cursor**、**Devin**の開発元である**Cognition**、**Google Jules**、**Vercel**、**Cloudflare**らが、AIによるコード操作の履歴を記録・交換するための共通フォーマット**Agent Trace**を提唱しました。AIエージェントによる高速かつ大量のコード生成・変更が常態化する中、従来のコミットログでは不十分だった「どのモデルが、どのコンテキスト（対話）に基づき、なぜその行を書いたのか」という詳細な履歴を、ツールを跨いで追跡可能にすることを目指しています。

仕様**v0.1.0**では、タイムスタンプ、対象ファイルの範囲、対話内容へのポインタ（URL）、AIモデルのIDなどを保持する**JSON**形式が定義されています。これにより、開発者はAIによる変更の意図を正確に監査できるほか、後続のエージェントが過去の経緯を効率的に理解できるようになります。現在は**v0**や**Cursor**などの提唱元での実装が進められており、今後は**GitHub Copilot**や**Claude Code**といった主要ツールの対応が普及の鍵となります。複数のAIツールを併用し、コードの透明性やメンテナンス性に課題を感じている開発チームのリードエンジニアにとって、この標準化の動向は注視すべき重要なトピックです。