## Rust製軽量エディタZedでDev Containers + GitHub Copilot + Claude Code生活はじめました

https://zenn.dev/dyoshikawa/articles/zed-devcontainers-copilot-claudecode

Rust製の高速エディタZedを活用し、Claude Code使用時の安定性向上とDev Containers環境での快適なAI開発ワークフローを構築する手法を提示する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[Zed, Dev Containers, Claude Code, GitHub Copilot, DevPod]]

Rust製エディタ「Zed」を核に、現代的なAIツール群（GitHub Copilot, Claude Code）と開発環境（Dev Containers）を統合する実践的なワークフローが紹介されています。著者がVS Codeから移行した最大の動機は、Claude Codeとの併用時にVS Codeが頻繁にクラッシュするという安定性の課題を解決することにありました。Zedは起動や動作が極めて軽量であり、VS Codeからの設定インポートも容易であるため、乗り換えのハードルが低い点が強調されています。

技術的な核心となるのは、ZedにおけるDev Containersの運用です。著者は、安定性を重視して「DevPod」という外部ツールを介したコンテナ起動を推奨しています。CLIから `devpod up . --ide none` を実行し、Zedのプロジェクトパレットからリモート接続する手順は、現時点でのZedの機能制限（安定版でのビルトイン未実装）を補う賢明なプラクティスと言えます。また、Zedのプレビュー版におけるビルトイン機能の動向にも触れられており、今後の進化にも期待を寄せています。

設定面では、`settings.json` を通じたGitHub Copilotの「edit prediction（タブ補完相当）」の有効化や、`oxfmt` 等の外部フォーマッタをプロジェクト単位で柔軟に適用する方法が具体的に解説されています。特に、Claude CodeをZed内蔵のターミナルで動かしつつ、Dev Containersによるサンドボックス環境で `--dangerously-skip-permissions` モードを利用する運用は、AIエージェントにコード操作を委ねる際の利便性と安全性のバランスを取る手法として非常に合理的です。

筆者は、エディタの軽快さが単なる「気持ちよさ」に留まらず、AIとの長時間の対話や大規模なコード操作におけるシステムの安定性に直結すると主張しています。VS Codeの重厚なエコシステムに依存せず、より高速なレスポンスと安定したAI開発体験を求めるエンジニアにとって、本書で示された「Zed + DevPod」の構成は、即戦力の代替案となるでしょう。