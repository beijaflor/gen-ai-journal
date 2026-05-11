## OllamaがAnthropic API互換に対応：ローカルモデルでClaude Codeの実行が可能に

https://ollama.com/blog/claude

**Original Title**: Claude Code with Anthropic API compatibility

実現する：OllamaがAnthropic Messages APIへの互換性を提供し、高性能なエージェントツールであるClaude CodeをローカルLLMで直接実行することを可能にする。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 85/100 | **Overall**: 84/100

**Topics**: [[Ollama, Claude Code, Anthropic API, AI Agent, Local LLM]]

**Ollama v0.14.0**以降において、**Anthropic Messages API**との互換性が正式にサポートされました。これにより、Anthropicが提供するターミナル完結型AIエージェント**Claude Code**を、ローカルで動作する**gpt-oss:20b**や**qwen3-coder**といったオープンソースモデルと接続して利用できるようになります。

利用者は環境変数の`ANTHROPIC_BASE_URL`をローカルの**Ollama**に向けるだけで、高度なエージェント機能をプライバシー重視の環境で実行可能です。さらに、既存の**Anthropic SDK**（Python/JavaScript）を使用しているアプリケーションも、エンドポイントの変更のみで**Ollama**上のモデルへ容易に切り替えられます。**Tool calling**、**Streaming**、**Vision**、**Extended thinking**などの主要機能を網羅しており、開発者は用途に応じてクラウドとローカルを柔軟に使い分けることができます。

ローカル環境で機密コードを扱いながら**Claude Code**の利便性を享受したいエンジニアや、エージェント開発においてモデルの柔軟性を求める開発者に推奨されます。