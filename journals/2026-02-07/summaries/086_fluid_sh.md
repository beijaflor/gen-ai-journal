## インフラ版Claude Code「Fluid」：サンドボックスで試行してIaCを自動生成するターミナルエージェント

https://www.fluid.sh/

**Original Title**: Fluid - Claude Code for infrastructure

インフラのクローン環境でAIが変更を試行・検証し、動作確認済みの構成からAnsible等のIaCを自動生成する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 94/100 | **Annex Potential**: 93/100 | **Overall**: 92/100

**Topics**: [[Infrastructure as Agent, Ansible, Sandbox Isolation, IaC Generation, SRE]]

**Fluid**は、LLMの推測に頼らず、実際の環境で「試行錯誤」してからコードを書くインフラ版の**Claude Code**とも言えるターミナルエージェントだ。従来のLLMによる**IaC**（TerraformやAnsible）生成は、既存の複雑な本番環境の仕様を正しく把握できないという課題があった。これに対し本ツールは、本番環境の**Sandboxクローン**を瞬時に作成し、その中でAIエージェントにコマンド実行や疎通確認を自由に行わせるアプローチを採る。エージェントが正常動作を確認した後、その手順を**Ansible Playbook**などの再現可能な**IaC**として自動出力するため、確実性の高いデプロイが可能になる。

セキュリティ面では、ローカルからの直接的なSSH接続を避け、**一時的なSSH証明書**によるサンドボックス制御と変更履歴の全ログ記録（**Audit Trail**）を統合している。さらに、リソース消費の激しい操作や外部通信には人間の承認を求める仕組みを備える。インフラ構築の自動化やSRE業務において、生成AIを安全かつ実戦的に活用したいエンジニアにとって、開発体験を劇的に変える可能性のあるツールである。インフラ運用の自動化に課題を感じているSREやプラットフォームエンジニアは、まずローカルへのインストールを検討すべきだ。