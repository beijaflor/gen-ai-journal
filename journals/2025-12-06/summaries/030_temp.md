## ClaudeでオープンソースLLMをファインチューニング：Hugging Face Skillsを活用

https://huggingface.co/blog/hf-skills-training

**Original Title**: We Got Claude to Fine-Tune an Open Source LLM

Hugging Faceは、Claude Codeなどのコーディングエージェントが自然言語指示でLLMのファインチューニングをエンドツーエンドで実行できる新ツール「Hugging Face Skills」を発表し、複雑なMLOpsプロセスを自動化します。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[LLM Fine-tuning, コーディングエージェント, Hugging Face Skills, AI開発ワークフロー, モデルデプロイメント]]

Hugging Faceは、AIエージェント向けの新しい機能拡張である「Hugging Face Skills」を導入しました。これにより、Claude Code、OpenAI Codex、Google Gemini CLIといったコーディングエージェントが、自然言語の指示だけでオープンソースLLMのファインチューニングプロセス全体を管理できるようになります。

このツールは、データセットの検証、最適なGPUハードウェアの自動選定、トレーニングスクリプトの生成、クラウドGPUでのジョブ提出、進捗監視、そして学習済みモデルのHugging Face Hubへのプッシュに至るまで、従来専門知識を必要とした全ての工程を自動化します。例えば、「Qwen3-0.6Bをopen-r1/codeforces-cotsデータセットでファインチューニングして」と指示するだけで、エージェントが最適なハードウェア（例：0.6Bモデルにはt4-small）を選定し、予想される時間とコストを提示します。

サポートされるトレーニング手法には、SFT（教師ありファインチューニング）、DPO（直接選好最適化）、GRPO（グループ相対方策最適化）の3種類があり、モデルサイズに応じてLoRA（低ランク適応）も自動適用され、大規模モデルの効率的な学習を可能にします。また、Trackioとの連携によりリアルタイムでトレーニングの損失を監視でき、学習完了後にはモデルをGGUF形式に変換してローカルデプロイすることも可能です。

Webアプリケーションエンジニアにとって、この「Hugging Face Skills」は、LLMのカスタマイズとデプロイにおける障壁を劇的に低減します。専門的なMLOpsの知識がなくても、会話形式で独自のモデルを開発できるため、特定タスクに特化したAIを迅速にプロトタイプし、アプリケーションに組み込むことが可能になります。これにより、LLMを活用した新機能開発のサイクルを大幅に加速させることができるでしょう。