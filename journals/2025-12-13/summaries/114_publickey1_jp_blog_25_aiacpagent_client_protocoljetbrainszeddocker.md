## AIエージェントをどのコードエディタでも使えるようにする「ACP（Agent Client Protocol）」、JetBrainsがベータ提供開始

https://www.publickey1.jp/blog/25/aiacpagent_client_protocoljetbrainszeddocker.html

JetBrainsは、ZedやDockerと共に、AIエージェントとコードエディタ間の相互運用性を高める業界標準プロトコル「Agent Client Protocol (ACP)」のベータ版をJetBrains IDEsで実装し、提供を開始しました。

**Content Type**: Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[AIエージェント, コードエディタ, 開発ツール, プロトコル, 相互運用性]]

JetBrainsは、AIエージェントを任意のコードエディタや開発ツールで利用可能にするための業界標準プロトコル「Agent Client Protocol (ACP)」のベータ版を、同社のJetBrains IDEsに実装し、提供開始したことを発表しました。この取り組みは、Zed、Dockerといった主要な開発ツールベンダーが主導しており、プログラマの指示により自律的にコーディングを行うAIエージェントが特定の開発環境に縛られずに機能することを目的としています。

現代のAIエージェントの多くは、Visual Studio CodeやClaude Codeなど特定の開発ツールと深く統合されていますが、ACPはこうした制限を取り払い、開発者が愛用するエディタと好みのAIエージェントを自由に組み合わせられるようにすることを目指します。これは、コード補完機能の事実上の標準となったLanguage Server Protocol (LSP)が、どの開発ツールでもコード補完を可能にした成功例をAIエージェントの分野で再現しようとするものです。

ACPはすでにZedやDockerによって実装されており、AIエージェントとしてはClaude Code、Codex CLI、Gemini CLI、OpenCode、OpenHands、Dockerのcagentなどがサポートしています。この標準化されたプロトコルの普及により、ウェブアプリケーションエンジニアは開発環境の選択肢が広がり、AIエージェントを活用したコーディングの柔軟性と効率が大幅に向上することが期待されます。特定のツールに依存することなく、最適な組み合わせで開発を進められるようになる点は、今後の開発ワークフローに大きな影響を与えるでしょう。