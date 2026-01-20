## ファイルシステムベースのコンテキスト取得を実現する「bash-tool」をVercelがリリース

https://vercel.com/changelog/introducing-bash-tool-for-filesystem-based-context-retrieval

**Original Title**: Introducing bash-tool for filesystem-based context retrieval

AIエージェントがファイルシステム上でUnixコマンドを実行し、必要なコンテキストのみを動的に抽出することでトークン消費の削減と精度の向上を実現する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[Vercel, AI SDK, Context Retrieval, AI Agents, Open Source]]

Vercelは、AIエージェントがファイルシステムを効率的に探索・操作できるようにするためのBash実行エンジン「bash-tool」をオープンソース化した。AI開発における大きな課題の一つは、膨大なファイル内容をプロンプトに詰め込むことでコンテキストウィンドウが即座に埋まり、コスト増大や精度低下を招くことである。著者は、エージェントにUnixスタイルのワークフロー（find, grep, jq, パイプ操作など）を与えることで、必要な情報の「断片」だけをオンデマンドで取得させる手法が、この問題の解決に極めて有効であると主張している。

技術的な特徴として、本ツールは「just-bash」を基盤に採用している。これはTypeScript上で直接Bashスクリプトを解釈するエンジンであり、シェルプロセスの起動や外部バイナリの実行を伴わずにBashロジックを安全に実行できる。開発者は、エージェントの起動時にファイルシステムへデータをプリロードしておくことができ、エージェントは必要に応じてその中から検索や抽出を行う。

実行環境については、高速な「インメモリ」環境と、より高い隔離性とリアルなファイル操作を可能にする「Vercel Sandbox（分離された仮想マシン）」環境の両方をサポートしている。これにより、単純なコンテキスト抽出から、カスタムバイナリを必要とする高度なタスクまで柔軟に対応可能だ。

Vercelのテキストto SQLエージェントの再設計においても、このbash-toolの導入によってトークン使用量の削減、回答精度の改善、および全体的なパフォーマンス向上が確認されたという。AI SDK v6と組み合わせて利用することで、Webアプリケーションエンジニアは、コンテキスト管理を効率化した、より強力なAIエージェントを構築できるようになる。