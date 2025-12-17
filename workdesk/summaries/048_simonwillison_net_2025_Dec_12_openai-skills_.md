## OpenAIが静かにスキルを導入、ChatGPTとCodex CLIで利用可能に

https://simonwillison.net/2025/Dec/12/openai-skills/

**Original Title**: OpenAI are quietly adopting skills, now available in ChatGPT and Codex CLI

OpenAIがChatGPTとCodex CLIに「スキル」メカニズムを導入し、ファイルシステムベースのシンプルな設計でLLMの自動化能力を大幅に拡張している。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 91/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[AIコーディングエージェント, LLM機能拡張, 開発ツール統合, 自動コード生成, プロンプトエンジニアリング]]

この記事は、OpenAIがChatGPTとCodex CLIに「スキル」メカニズムを静かに導入したことを報じています。これはAnthropicが以前発表したスキルと同様に、特定の機能やタスクを実行するための指示とリソース（Markdownファイルとオプションのスクリプト）をフォルダとして構造化するシンプルなファイルシステムベースの設計が特徴です。著者のSimon Willison氏は、この仕組みがLLMの能力を大きく拡張し、開発者のワークフローに重要な影響を与えると指摘しています。

ChatGPTのCode Interpreter機能では、新たに`/home/oai/skills`フォルダが追加され、ユーザーはプロンプトを通じてこれにアクセスできるようになりました。OpenAIは、スプレッドシート、docx、PDFなどのドキュメントを扱うためのスキルを提供しています。特にPDFや文書に対しては、レイアウトやグラフィック情報を保持するため、ページごとにPNGに変換し、ビジョン対応のGPTモデルに渡すという高度なアプローチを採用しており、テキスト抽出だけでは失われる情報を活用できると著者は説明しています。Willison氏はカカポの繁殖に関するPDF作成スキルを試用し、LLMがマクロン非対応フォントを自律的に修正するなど、その細部にわたる調整能力を高く評価しています。

さらに、OpenAIのオープンソースツールであるCodex CLIにも実験的なスキルサポートが追加されました。`~/.codex/skills`フォルダにスキルを配置し、`--enable skills`オプションで実行することで、特定のタスク（例えばDatasetteプラグインの作成）を自動化できます。著者は、Claude Opus 4.5でDatasetteプラグイン作成スキルを生成し、Codex CLIで実際に機能するPythonプラグインを生成することに成功し、その精度と実用性を実証しています。

Willison氏は、自身が以前から「スキル」のコンセプトを高く評価していたことが、OpenAIの今回の動きによって裏付けられたと感じています。このメカニズムのシンプルな仕様は、他のプラットフォームへの実装を容易にし、将来的にAgentic AI Foundationのような組織によって正式な標準として文書化されるべきだと提言しています。これは、ウェブアプリケーション開発者にとって、LLMがより高度な自動化、複雑なタスクの直接処理、そして柔軟なツール連携を可能にする重要な進展であり、より自律的なコーディングエージェントの進化を加速させるものとして注目されます。