## AgentのToolを公開MCPから自作に変えたらToken使用料が9割削減した

https://zenn.dev/leverages/articles/github-zenn-linkage-20251201-1

Agent開発において、公開されているMCP（Model Context Protocol）ツールではなく、必要な情報のみを取得する自作ツールを使用することで、Token使用料を9割削減する方法を解説する。

**Content Type**: Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 86/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[Agent開発, LLMコスト最適化, Token使用量削減, GitHub API, Custom Tools]]

レバレジーズ社が開発中の引き継ぎ自動化Agent「ko☆shi」において、LLMのToken使用料が高額になっている問題が発生しました。調査の結果、GitHubの最新PRを取得する際に、Strands Agentsの公開MCP（Model Context Protocol）が提供するToolを使用していたことが原因と判明。このToolはGitHub APIから必要以上の情報を取得し、その膨大なJSONデータがそのままLLMの入力として渡されていたため、1回の呼び出しで約34万ものTokenを消費していました。

著者はこの問題に対し、不要な情報を削減することの重要性を強調しています。具体的には、PR番号、タイトル、状態、作成者、ブランチ名、作成日時、更新日時、WebページURLなど、ko☆shiにとって本当に必要なフィールドのみを抽出する自作のPython関数を作成し、これをStrands AgentsのToolとして登録しました。このアプローチにより、1回の呼び出しにおけるToken使用量を約34万Tokenから約3万Tokenへと、実に9割も削減することに成功し、コストを大幅に抑制できることを実証しました。

この経験から著者は、公開されているMCPツールは便利である一方で、APIを叩くようなAgentのToolとしては、必要な情報だけを取得する関数を自作する方がToken使用料を抑えられると結論付けています。さらに、Toolの設計段階で最低限の権限や機能に絞ることで、Agentの意図しない暴走を防ぐという副次的な効果も得られると指摘。人間が介入しにくいAgent開発だからこそ、より厳格なTool設計が不可欠であると、その重要性をウェブアプリケーションエンジニアの視点から力強く提言しています。MCPと自作Toolを適材適所で使い分けることが、効率的かつ安全なAgent開発の鍵であるとまとめています。