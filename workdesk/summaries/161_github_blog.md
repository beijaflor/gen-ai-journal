## GitHub Copilot SDKのテクニカルプレビュー開始：あらゆるアプリにエージェント機能を組み込み可能に

https://github.blog/news-insights/company-news/build-an-agent-into-any-app-with-the-github-copilot-sdk/

**Original Title**: Build an agent into any app with the GitHub Copilot SDK

GitHub Copilot CLIの基盤となる自律型エージェントの実行ループを、任意のアプリケーションに統合できるSDKを公開。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 85/100 | **Overall**: 84/100

**Topics**: [[GitHub Copilot SDK, AI Agents, MCP, Developer Tools, LLM Orchestration]]

GitHubは、自律型エージェントの機能を任意のアプリケーションに統合できる**GitHub Copilot SDK**をテクニカルプレビューとして公開しました。本SDKは、**GitHub Copilot CLI**で実績のある「プランニング、ツール呼び出し、ファイル編集、コマンド実行」の実行ループをプログラムから直接制御可能にするものです。従来、開発者が自前で構築していたコンテキスト管理やツールのオーケストレーション、モデルのルーティングをSDKが肩代わりするため、エンジニアは独自の製品ロジックの実装に集中できます。

主要な機能として、**Node.js**、**Python**、**Go**、**.NET**の各言語をサポートし、**Model Context Protocol (MCP)**サーバーとの統合も可能です。また、GitHubによる認証やストリーミング出力も標準で備えています。独自のGUIを持つAIエージェントや、社内ワークフローに特化したエージェントを迅速に構築したい開発者、特に**RAG**を超える高度な推論・実行機能を求めるエンジニアにとって、実装の難易度を劇的に下げる強力な選択肢となるでしょう。