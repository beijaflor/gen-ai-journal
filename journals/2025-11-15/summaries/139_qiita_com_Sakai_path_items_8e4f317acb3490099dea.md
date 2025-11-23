## 【Visual Studio 2026】MCPがついに標準化！NuGet MCPを有効化して動作確認してみた

https://qiita.com/Sakai_path/items/8e4f317acb3490099dea

Visual Studio 2026がModel Context Protocol (MCP) を標準搭載し、GitHub Copilotのエージェント化を推進する機能統合とその検証手順を解説します。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 79/100 | **Overall**: 80/100

**Topics**: [[Visual Studio 2026, Model Context Protocol (MCP), GitHub Copilot Agents, NuGet Integration, AI Assisted Development]]

この記事は、Visual Studio 2026でModel Context Protocol (MCP) が標準対応し、GitHub Copilotが外部ツールを呼び出すエージェントへと進化する基盤を築いたことを解説しています。筆者は、このMCPの標準化をVS2026最大のアップデートの一つと位置づけ、その重要性を強調しています。これまでのCopilotがコード補完や提案に主眼を置いていたのに対し、VS2026ではMCPを通じてCopilotがNuGetパッケージ管理といった外部機能を直接操作できるようになり、開発者のワークフローを大幅に強化する可能性を秘めていると説明しています。

記事では、まずVisual Studio 2026のインストールから、GitHub Copilotのセットアップ、そして新機能であるビルトインのNuGet MCPサーバーを有効化する具体的な手順を詳細に解説しています。特に、Copilotチャット内の「ツール」メニューからNuGet MCPサーバーの項目をすべてオンにするステップは、エージェント機能の核となる部分です。

さらに、実際にMCPが動作していることを確認するための検証方法も示されています。具体的には、プロジェクトに参照がない状態で「Newtonsoft.Jsonの最新バージョンをnugetツールを使って調べて」というプロンプトをCopilotに投げかけます。すると、通常のCopilotがローカル情報のみで回答しようとするのに対し、MCPを有効化している場合は「外部ツール実行の確認ダイアログ」が表示され、ユーザーの許可を得てからNuGet.orgへアクセスし、正確な最新バージョン情報を取得・提示する様子がスクリーンショットと共に紹介されています。これは、Copilotが単なる推測ではなく、MCPを介して外部の実データに基づいたアクションを実行している明確な証拠となります。

著者は、このビルトインNuGet MCPサーバーの動作を理解することが、将来的に社内APIやデータベースにアクセスする「自分専用MCPサーバー」をC#や.NETで自作する際の重要な第一歩となると主張しており、生成AIを活用した開発ワークフローのさらなる可能性を示唆しています。このアップデートは、開発者が日常的に使うIDEにAIエージェント機能が深く統合される時代の幕開けを告げるものとして、ウェブアプリケーションエンジニアにとって見逃せない進展と言えるでしょう。