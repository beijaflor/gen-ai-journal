## Codex CLI が Skills をサポート

https://blog.lai.so/codex-skills/

Codex CLI は、Claude Skills と互換性のある「Skills」機能を導入し、ディレクトリベースのプロンプトとスクリプトを組み合わせることで、AIエージェントの特定の機能拡張と再利用を可能にしました。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 76/100 | **Annex Potential**: 73/100 | **Overall**: 76/100

**Topics**: [[AIコーディングツール, エージェント機能, Claude Skills, Codex CLI, プロンプトエンジニアリング]]

Codex CLIの最新版v0.65.0は、実験的機能として「Skills」サポートを導入しました。この機能は、AnthropicのClaude Skillsと同様に、YAMLメタデータとMarkdownファイル（SKILL.md）を組み合わせたディレクトリ構造（`~/.codex/skills`以下に配置）でスキルパッケージを定義します。これにより、単なる関数単位の登録とは異なり、プロンプトとスクリプトをディレクトリ単位でまとめることができ、AIエージェントに特定の機能や知識を容易に拡張できます。

Codexが採用した「Progressive Disclosure」の概念は、初期ロード時にはdescriptionなどのメタデータのみを読み込み、必要に応じてSKILL.mdの本文を展開するというもので、Anthropicの考え方と共通しています。これにより、効率的なスキル管理と利用が可能です。

この記事では、Anthropicが公式ブログで紹介していた`frontend-design`スキルをCodex CLIで利用し、LP（ランディングページ）のデザイン改善を試す実例を紹介しています。このスキルは、AIがウェブデザインをする際の最大公約数的なコードを、ネガティブプロンプトを用いて頻繁に矯正することで、汎用的なAI的デザインを避け、創造的で洗練されたコードとUIデザインを生成します。

実際に「Gemini 3 Proはデザインに強いのか？」で生成したLPの改善を依頼した結果、Before/Afterで比較すると、素人目にもAfter版の方が印象が良く、コンテンツ内容まで刷新されました。改善後のデザインをGeminiに評価させたところ、タイポグラフィの構造化、具体的な機能を備えたHigh-FidelityなUIモックアップ、情報を凝縮したBento Gridレイアウト、Dark Modeベースの発光表現によるアクティブ状態の強調など、多岐にわたる改善点がフィードバックされました。

このSkills機能は、開発者が日常的に使用するターミナル環境でAIエージェントの能力を拡張し、特定のタスク（例えばウェブデザインの自動改善）において、より洗練された結果を得るための実用的な手段を提供します。Claude Skillsとの高い互換性も、既存のエージェント開発資産を活用できる点で重要であり、今後の他のCLIツール（例：Gemini CLI）への展開も示唆されています。