## Claude Codeにおける8つの任意コマンド実行の脆弱性と防御の教訓

https://flatt.tech/research/posts/pwning-claude-code-in-8-different-ways/

**Original Title**: Pwning Claude Code in 8 Different Ways

AnthropicのAIエージェント「Claude Code」において、読み取り専用コマンドを装って承認なしに任意のコードを実行できる8つの脆弱性が発見され、AIエージェントにおけるブラックリスト方式の防御の限界が浮き彫りになった。

**Content Type**: 🔬 Research & Analysis
**Language**: en

**Scores**: Signal:5/5 | Depth:5/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 93/100 | **Annex Potential**: 92/100 | **Overall**: 93/100

**Topics**: [[Claude Code, セキュリティ, AIエージェント, プロンプト注入, 脆弱性診断]]

GMO Flatt SecurityのセキュリティエンジニアであるRyotaK氏が、Anthropic社のCLI AIエージェント「Claude Code」において、ユーザーの承認なしに任意のコマンドを実行できる8つの脆弱性（CVE-2025-66032）を報告した。これらの脆弱性は、Claude Codeが利便性のために導入していた「読み取り専用コマンド（echo, man, sed, sort等）」の自動承認ロジックと、その安全性を担保するための正規表現ベースのブラックリスト方式をバイパスすることで発生する。

著者は、一見無害に見える「読み取り専用」コマンドに潜む危険な引数や仕様を突き止めることで、8つのバイパス手法を提示している。例えば、`man`コマンドの`--html`オプション、`sort`コマンドの`--compress-program`経由でのシェル起動、さらにはGitの引数短縮仕様（`--upload-pa`が`--upload-pack`として解釈される挙動）を利用した検知回避などが挙げられる。特に独創的なのは、Bashの変数展開（`${var@P}`）を悪用し、Claude Codeがブロックしている`$(...)`という文字列を動的に生成・実行させる手法だ。これにより、AIがコマンドを「単純なecho」だと誤認している間に、裏で任意のペイロードを走らせることが可能になる。

筆者によれば、この問題が極めて重要な理由は「間接的なプロンプト注入（Indirect Prompt Injection）」の経路になる点にある。攻撃者がGitHubリポジトリやウェブページに悪意のある指示を埋め込んでおけば、Claude Codeがそのプロジェクトをスキャンした際に、開発者のマシン上で自動的にバックドアが設置されたり、環境変数が盗まれたりするリスクがある。Anthropic社はこの報告を受け、従来のブラックリスト方式を廃止し、より厳格なホワイトリスト方式へとアーキテクチャを変更することで対応した。本記事は、AIエージェントの権限管理を設計する際、正規表現による「禁止」ではなく、完全に信頼できるパターンのみを「許可」する設計の重要性を、具体的な攻撃コードをもって実証している。