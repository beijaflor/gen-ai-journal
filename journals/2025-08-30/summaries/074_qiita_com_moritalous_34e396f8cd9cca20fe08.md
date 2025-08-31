## OpenAI Codex CLIでAmazon Bedrockのgpt-ossを使う方法（Clineでも使えました）

https://qiita.com/moritalous/items/34e396f8cd9cca20fe08

OpenAI Codex CLIがAmazon Bedrockの低コストなgpt-ossモデルをOpenAI互換API経由で利用し、効率的なコード生成エージェントを構築する手順を詳述します。

**Content Type**: Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[AIコーディングエージェント, Amazon Bedrock, gpt-oss, CLIツール, コスト最適化]]

この記事は、新しくAmazon Bedrockで利用可能になったOpenAIのオープンウェイトモデル「gpt-oss」を、OpenAI Codex CLIと連携させて活用する具体的な方法を解説します。ウェブアプリケーションエンジニアにとって、このアプローチが重要なのは、極めて低コストで高性能なAIコーディング環境を構築できる点にあります。

gpt-ossモデルにはgpt-oss-120bとgpt-oss-20bの2種類があり、特にgpt-oss-120bはo4-miniに匹敵するとされながら、AnthropicのClaude Sonnet 4と比較して入力で20分の1、出力で25分の1という驚異的な安価さを実現しています。このコストパフォーマンスは、日常的な開発ワークフローにAIエージェントを深く組み込みたい開発者にとって、大きなメリットとなります。

本記事では、まずBedrockのオレゴンリージョンでAPIキーを発行し、次にGitHubからCodex CLIのバイナリをダウンロードして環境パスを設定する方法を詳述しています。最大のポイントは、Codex CLIの`config.toml`ファイルにBedrockのエンドポイントと環境変数`AWS_BEARER_TOKEN_BEDROCK`を定義することで、Codex CLIがOpenAI Chat Completions API互換としてgpt-ossを呼び出せるようにする設定です。これにより、既存のOpenAIエコシステムのツールをBedrockの低コストモデルとシームレスに連携させることが可能になります。

実際にCodex CLIを起動し、簡単な指示でHTML、JavaScript、CSSを用いたテトリスゲームのソースコードを生成する具体例が示されており、その実用性が強調されています。また、人気のCLIツール「Cline」も「OpenAI Compatible」プロバイダーとして同様にgpt-ossを利用できる点も紹介されており、開発者は自身の好みに合わせてツールを選択できます。

この方法は、特に頻繁なコード生成や自動化を求める開発チームにとって、開発コストを大幅に削減しつつ、AIによる生産性向上を享受するための実践的な選択肢となるでしょう。安価なgpt-ossとCodex CLIの組み合わせは、まさにコスト効率と開発効率を両立させる「ゲームチェンジャー」と言えます。