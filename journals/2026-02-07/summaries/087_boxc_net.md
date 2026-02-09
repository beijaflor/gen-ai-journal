## Claude Codeで利用枠が切れた際にローカルモデルへ接続する方法

https://boxc.net/blog/2026/claude-code-connecting-to-local-models-when-your-quota-runs-out/

**Original Title**: Claude Code: connect to a local model when your quota runs out

AnthropicのCLIツール「Claude Code」のAPI利用制限に達した際、LM Studio等を通じてローカルLLMに接続し開発を継続する回避策を解説する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[Claude Code, LM Studio, ローカルLLM, Anthropic API, Qwen2.5-Coder]]

Anthropicが提供するエージェント型CLIツール **Claude Code** のAPI利用枠（Quota）を使い切った際の回避策として、**LM Studio** や **llama.cpp** を介してローカルLLMに接続し、開発を継続する具体的なワークフローを解説しています。

主な手法は、**LM Studio** 等でローカルサーバーを起動し、環境変数 **ANTHROPIC_BASE_URL** を `http://localhost:1234` に、**ANTHROPIC_AUTH_TOKEN** を任意の値に設定することで、**Claude Code** のリクエスト先をローカルホストへリダイレクトさせるものです。実行時に `claude --model openai/gpt-oss-20b` のようにモデルを指定することで、Anthropicのサーバーを介さずに動作させることが可能になります。

記事では、`/usage` コマンドによる枠の消費確認や、`/model` コマンドでのモデル切り替え、さらには **GLM-4.7-Flash** や **Qwen3-Coder-Next** といった推奨のローカルモデルについても言及しています。ローカル環境では推論速度や精度が低下するという現実的なトレードオフを認めつつも、制限解除までの「バックアップ」として実用的な手段を提示しています。

**Claude Code** を日々の開発に組み込んでおり、API制限による作業中断を最小限に抑えたいWebアプリケーションエンジニアにとって、即座に役立つトラブルシューティングガイドです。