## IaCを活用して最速でAzure × RAGを概念検証

https://zenn.dev/kinosh/articles/iac-azure-rag-fastest-poc

Azure上でRAGシステムを迅速に概念検証するため、IaCテンプレートとAzure Developer CLIを活用した最速デプロイ手法を詳細に解説し、その再現性と本番移行への適応性を示す。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[Azure, RAG, IaC, Azure Developer CLI, PoC]]

この記事は、Azure上でRAG (Retrieval Augmented Generation) システムを迅速に概念検証（PoC）するための最速デプロイ手法を、IaC (Infrastructure as Code) とAzure Developer CLI (azd) を活用して解説します。手動でのAzure Portal構築が抱える数日間の時間コスト、設定ミス、環境差異といった課題は「PoC貧乏」のリスクを高めますが、IaCはこれらの問題を解決し、1〜2時間での再現性の高いデプロイを可能にします。

RAGシステムの基盤リポジトリ選定では、`azure-search-openai-demo`、`Chat with your data Solution Accelerator (CWYD)`、`GPT-RAG`を比較検討。著者は、PoCにはCWYDが最もバランスが取れていると判断。その理由は、デモ用途に特化し本番移行に課題がある`azure-search-openai-demo`や、エンタープライズ向けで学習・維持コストが高い`GPT-RAG`と比較して、CWYDがカスタマイズ性、デプロイ速度、本番移行のしやすさ、基本的なセキュリティ機能を兼ね備えているためです。これにより、PoC段階から将来的な拡張を見据えた柔軟な基盤を迅速に構築できます。

実践的なデプロイガイドでは、azdとazコマンドを使ったCLI中心の環境構築手順を提供。AzureサブスクリプションやCLIツールの準備から、GitHubリポジトリのフォーク、環境変数の設定、デプロイ実行、そして必須の認証設定までを網羅します。特に、アプリケーションコードを正しくデプロイするための`AZURE_APP_SERVICE_HOSTING_MODEL="code"`設定、Azure OpenAIのクォータ不足対策、およびWebアプリへのアクセスに不可欠な認証設定の重要性を強調。デプロイ時に発生しがちなエラー（クォータ不足、コードデプロイ未実行、認証未設定）の解決策も具体的に解説しています。著者は、Claude CodeなどのAIエージェントを活用することで、これらのCLI操作を自動化し、デプロイ作業を大幅に効率化できると述べ、時間の節約とスムーズなPoC実施を推奨しています。