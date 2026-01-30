## yolo-cage: AIエージェントの暴走を防ぐセキュアなサンドボックス実行環境

https://github.com/borenstein/yolo-cage

**Original Title**: yolo-cage: AI coding agents that can't exfiltrate secrets or merge their own PRs.

AIエージェントの行動範囲をサンドボックス内に制限し、開発者の承認コストを下げながら機密情報の流出や勝手なPRマージを防止します。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 82/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[AIエージェント, サンドボックス, セキュリティ, Claude Code, GitHub]]

「**yolo-cage**」は、**Claude Code**などの自律型AIコーディングエージェントに自由な操作を許可しつつ、致命的な破壊操作や情報の持ち出しを技術的に防ぐオープンソースのサンドボックス環境です。**Vagrant**（MicroK8s）上に構築された隔離環境により、エージェントが実行できるアクションの「ブラスト半径」を最小化します。

技術的には、HTTP/HTTPS通信を監視する**Egress Proxy**による**シークレットスキャン**（APIキーやSSH鍵の検知）や、**Dispatcher**による**Git/GitHub CLI**コマンドのインターセプトが中核です。エージェントは割り当てられた特定のブランチ以外への操作ができず、プルリクエストのセルフマージやリポジトリの削除も物理的にブロックされます。

これにより、開発者はエージェントからの絶え間ない承認リクエストによる「意思決定の疲労」を回避し、最終的なPRレビューの段階でまとめて変更を確認できるようになります。自律型AIツールの利便性を享受しつつ、セキュリティガバナンスを維持したい開発チームや、エージェントの監視コストを下げたいエンジニアに推奨されます。