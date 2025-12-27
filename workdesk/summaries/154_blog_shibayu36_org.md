## Claude CodeからPull Requestのレビュー操作を便利に行うClaude Skillsを作った

https://blog.shibayu36.org/entry/2025/12/17/173000

GitHub CLIの出力をAWKで整形し、Claude CodeによるPull Requestレビューの正確性を大幅に向上させるカスタムスキルを公開。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[Claude Code, GitHub CLI, PRレビュー, AIエージェント, Claude Skills]]

Claude CodeやClaude Code Actionを利用してAIに自律的なPull Request（PR）レビューを行わせる際、著者は「インラインコメントを付ける行を間違える」「過去のコメントやインラインコメントを正しく取得できない」「特定のコメントへの返信に失敗する」といった課題に直面した。これらの問題は、LLMがGitのdiff形式から正確に行番号を計算し、APIに渡すべきパラメータ（`side`や`line`）を特定する際の確率論的な誤りに起因している。

著者はこの解決策として、PRレビュー操作に特化したClaude Skill「github-pr-review-operation」を自作し、公開した。このスキルの核心は、`gh pr diff`コマンドの出力を独自のAWKスクリプトで加工する手法にある。標準のgit diff形式ではなく、各行に「L163」（Base側の163行目）や「R164」（Head側の164行目）といった明示的なプレフィックスを付与することで、GitHubのWeb UI上の「Files changed」に近い視認性の高いテキスト情報を生成する。これにより、Claude Codeが「どの行にコメントすべきか」を判断する際の計算負荷が劇的に軽減され、インラインコメントの配置精度がほぼ100%まで改善されたという。

また、本スキルはPR情報の取得、コメント一覧の取得、返信操作なども網羅しており、特にGitHub APIを直接叩く際の`-F`（数値パラメータ用）と`-f`（文字列パラメータ用）の使い分けといった、LLMがミスしやすい詳細な仕様も`SKILL.md`内に定義されている。筆者によれば、ClaudeのSkill Generatorを活用してベースを作成し、実用を通じた微調整を繰り返すことで、極めてシンプルかつ強力なツールとして完成させたとしている。既存のAIコーディングツールのレビュー精度に不満を感じているエンジニアにとって、プロンプトエンジニアリングとCLIツールを組み合わせた実用的な解法として非常に価値が高い。