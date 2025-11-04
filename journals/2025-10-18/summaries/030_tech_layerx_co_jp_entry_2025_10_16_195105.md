## Claude Agent SDK で 自分用株式分析 Agent を作ってみた

https://tech.layerx.co.jp/entry/2025/10/16/195105

LayerXのエンジニアがClaude Agent SDK、yfinance、および独自のMCPツールを活用し、カギ足チャート分析に対応した自分用の株式分析AIエージェントを構築する手法を解説した。

**Content Type**: Tutorial & Guide
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 76/100 | **Overall**: 80/100

**Topics**: [[AI Agent, Claude Agent SDK, 株式分析, Python, カギ足チャート]]

LayerXのAi Workforce事業部のエンジニアが、Claude Agent SDK、yfinance、Claude Code、Codex CLIといった技術スタックを用いて、自分用にカスタマイズされた株式分析AIエージェントを開発した経緯を詳述している。この記事はLayerX AIエージェントブログリレーの一環として公開された。

このエージェントは、ユーザーが指定した期間に基づいて株価データを取得し、それを基にカギ足チャートを用いた分析を行い、売買シグナルとパフォーマンスを提示する。著者は、ChatGPTのような汎用的な分析ツールとは異なり、エージェントとして構築することで、自身のルールや分析手法を柔軟に組み込める点に意義を見出している。

実装の中心となるのは、以下の3つのMCP (Message Communication Protocol) ツールである。
1.  **`fetch_latest_nikkei_data`**: yfinanceを利用して直近の株価（始値と終値）を取得する。将来的には定期的な株価取得と分析への活用を見据えている。
2.  **`fetch_nikkei_history`**: 指定した期間の日経平均先物の15分足データを取得し、後続ツールでの分析のためにCSV形式で出力する。トークン数を節約するため、JSONではなくCSV形式を選択した点が工夫として挙げられる。
3.  **`analyze_kagi_chart`**: `fetch_nikkei_history`で得られたデータからカギ足チャートを生成し、売買シグナルとパフォーマンスを分析する。カギ足は、反転幅を厳密に定義できるため分析に適していると判断され、デフォルトの反転幅は50円に設定されている。

約1ヶ月のシミュレーション結果では、決済損益として+3700円という成果が示された。著者は、このカスタムエージェントがサブエージェントの組み合わせによる他の分析手法との統合や、さらなる拡張性を持つ可能性を強調している。このアプローチは、webアプリケーションエンジニアが特定の業務要件に合わせたAIエージェントを構築する上で、具体的な実践例と技術的なヒントを提供するものとなっている。