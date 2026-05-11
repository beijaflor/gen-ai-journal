## Codex エージェントループの展開

https://openai.com/ja-JP/index/unrolling-the-codex-agent-loop/

**Original Title**: Unrolling the Codex Agent Loop

解説する。OpenAIのソフトウェアエージェント「Codex」におけるエージェントループの内部設計と、プロンプト制御によるパフォーマンス最適化の具体的手法を。

**Content Type**: Technical Reference
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 84/100 | **Annex Potential**: 82/100 | **Overall**: 84/100

**Topics**: [[Codex CLI, エージェントループ, Responses API, プロンプトキャッシュ, コンテキスト圧縮]]

OpenAIのソフトウェアエージェント**Codex CLI**の核となる「エージェントループ」の内部構造を、開発チーム自らが解説している。ユーザーの入力をどのように**Responses API**へ渡すプロンプトに構造化し、モデルの推論とツール実行（**shell**や**MCP**など）の反復を管理しているかを詳述する内容だ。

特に、パフォーマンス最適化のための**プロンプトキャッシュ**の仕組みについて、キャッシュヒット率を最大化するためのプロンプト構成順序の重要性や、バグによるキャッシュミスがコストに与える影響など、実運用上の洞察が共有されている。また、プライバシーへの配慮としてステートレスな設計を維持しつつ、**ゼロデータ保持（ZDR）**と両立させる実装方法や、増大するコンテキストを管理する**圧縮（Compaction）**技術についても触れられている。

自律型エージェントのハーネス（制御ロジック）を構築する開発者や、LLMのトークン効率とパフォーマンスのトレードオフを検討しているエンジニアにとって、OpenAI自身の設計判断を学べる極めて価値の高いリファレンスである。