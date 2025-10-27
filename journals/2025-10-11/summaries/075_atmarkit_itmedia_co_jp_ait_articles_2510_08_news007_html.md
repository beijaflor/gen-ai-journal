## gpt-ossでMCP実践、Open WebUIとmcp-grafanaで障害解析AIエージェントを構築する方法：クラウドサービスだけじゃない！　ローカルPCやサーバ、Kubernetesで生成AI（8）

https://atmarkit.itmedia.co.jp/ait/articles/2510/08/news007.html

本記事は、OpenAIのオープンウェイトモデル「gpt-oss」とOpen WebUI、mcp-grafanaを組み合わせ、Kubernetes環境上で障害解析AIエージェントを構築する具体的な手法とアーキテクチャを詳述します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[AIエージェント, gpt-oss, Kubernetes, Open WebUI, mcp-grafana]]

OpenAIがリリースしたオープンウェイトモデル「gpt-oss」は、自律的な意思決定と行動を可能にするAIエージェント能力と、Tool Calling性能の飛躍的向上により、外部ツール連携を伴う高度なタスク実行に適しています。本記事は、このgpt-ossとOpen WebUI、そしてGrafana連携を可能にするmcp-grafanaを組み合わせ、Kubernetes環境で障害解析AIエージェントを構築する実践的な方法を詳述します。

重要なのは、gpt-ossが20Bや120Bのモデルサイズで、16GB VRAM GPUやApple Silicon Macといった少リソース環境でも実用的な速度で動作し、オープンウェイトながらModel Context Protocol (MCP) を実用レベルで利用できる点です。これにより、Webアプリケーションエンジニアは商用モデルに依存せず、オンプレミス環境で強力なAIエージェントを構築する選択肢を得られます。

具体的な構築手順として、KubernetesのDynamic Resource Allocation (DRA) を活用したGPUクラスタ上にOpen WebUIとOllamaをデプロイし、Grafanaのサービストークンを取得してmcp-grafanaをインストールします。その後、Open WebUIにmcp-grafanaを外部ツールとして登録し、モデルパラメータやプロンプトテンプレートを設定します。これにより、チャットインターフェースからGrafanaのメトリクス（例：負荷の高いPod）やKubernetesイベントログを検索し、AIエージェントがPromQLクエリ生成から結果解析までを自律的に実行できるようになります。

このアプローチの「なぜ重要か」は、従来の監視システムと生成AIを統合し、障害発生時の原因特定や解決策提示を自動化する新しい運用パラダイムを提示している点です。運用負荷の大幅な軽減と迅速な問題解決が期待できるだけでなく、オープンソースモデルとKubernetesの組み合わせが、クラウドベンダーに依存しない柔軟なAI活用基盤の可能性を広げます。