## 複数環境でのClaude Code利用統計をOpenTelemetryで一元管理する

https://yag.xyz/post/claude-code-otel/

**OpenTelemetry**のテレメトリ送信機能を活用し、複数環境に点在する**Claude Code**の利用コストやモデル使用状況を一元管理する仕組みを構築する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 84/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[Claude Code, OpenTelemetry, Grafana, VictoriaMetrics, 可視化]]

**Claude Code**が標準で備えている**OpenTelemetry**（**OTEL**）連携機能を活用し、ローカルやリモートの複数環境に分散した利用統計を一元管理する手法を解説している。従来は`ccusage`を用いて環境ごとに確認する必要があったが、本構成では**OpenTelemetry Collector**を受信ポイントとし、時系列データベースの**VictoriaMetrics**やログ管理の**Loki**にデータを集約・保存する。

記事では`settings.json`の`env`セクションにおける具体的なエンドポイント設定や、**chezmoi**のテンプレート機能を用いたホスト名識別の自動化について触れている。また、拠点間の通信には**Tailscale**を採用することで、ネットワーク設定の複雑さを回避しつつ安全にテレメトリを送信できる実戦的なアーキテクチャが示されている。**Grafana**のダッシュボードで利用コストや使用モデルを定量的に可視化できるため、開発ワークフローの振り返りや予算管理に極めて有効だ。

ラップトップ、GPUサーバ、開発用仮想マシンなど、複数の開発拠点を併用しており、AIツールの使用状況を中央集権的に把握したいエンジニアにとって、導入の指針となる一稿だ。