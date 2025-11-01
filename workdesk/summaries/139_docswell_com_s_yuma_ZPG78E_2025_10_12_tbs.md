## GitHub Copilotでバックエンドのバイブコーディングを極めた話

https://www.docswell.com/s/yuma/ZPG78E-2025-10-12-tbs

GitHub CopilotによるバックエンドでのVibe Codingの課題と、外部リソース情報をAIに的確に伝えるためのCustom Chat Mode活用法を解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[GitHub Copilot, Vibe Coding, Azure Functions, Custom Chat Mode, Context Engineering]]

GitHub Copilotを用いたバックエンドのVibe Coding（自然言語指示によるAI駆動開発）について、筆者は自身の経験を元にその課題と解決策を詳細に解説しています。最初の試みでは、GitHub CopilotがCosmos DBのパーティションキーなどのAzureリソース構成を自律的に把握できず、期待通りのコード生成に失敗しました。これは、フロントエンド開発とは異なり、バックエンド開発ではコード外のインフラ側のコンテキストが不可欠であるため、AIにその情報が不足していたことが主な原因と分析されています。

この課題に対し、筆者はAIにインフラ情報をコンテキストとして与える方法を模索します。Infrastructure as Code (IaC) による情報提供の限界と、MCP (Microsoft Copilot Plugin) ServerやAzure CLIを活用してインフラの状態を動的に取得するアプローチを比較し、汎用性の高い後者に着目しました。しかし、Azure MCP Serverが意図した場面で呼ばれない、Azure認証の問題、Copilotの指示無視など、さらなる課題に直面します。

これらの失敗から得た教訓を活かし、筆者は「Custom Chat Mode」の活用を提案します。これは、特定のツール使用や指示（例：「必ずAzure MCP Server、Azure CLIを使ってAzure側の構成を把握してから実装を考えてください」）をCopilotチャットのやり取りに組み込む機能です。これにより、Copilotがインフラ構成を「捏造」して誤ったコードを生成することを防ぎ、必要な情報がない場合は人間へ質問を促すように改善されました。Custom Chat Modeは`settings.json`への直接書き込みよりも柔軟で、使用するツールを絞り込み、詳細な処理フローや出力形式を定義できるため、成果物のブレを大幅に抑制できます。

さらに、成果物の安定性を高める「Spec-Driven」開発手法や、Copilotに自分好みの「人格」を与えることで開発体験を向上させるTipsも紹介されています。バックエンドのVibe Codingを極めるためには、インフラ側のコンテキストをAIに正確に伝える設定、Custom Chat Modeの戦略的な利用、そして適切なAIモデルの選択が重要であると結論付けています。これにより、AIによるコード生成の精度と開発者の生産性が飛躍的に向上することが期待されます。