## Claude Codeで記憶領域を持つための独自のAgent Skillsを使っている

https://zenn.dev/yamadashy/articles/claude-code-agent-skills-agent-memory

開発中のコンテキストをリポジトリ内のMarkdownファイルとして永続化し、Claude Codeに「記憶」と「想起」の能力を付与する独自のAgent Skillの実装方法を紹介する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 87/100 | **Annex Potential**: 86/100 | **Overall**: 88/100

**Topics**: [[Claude Code, Agent Skills, コンテキスト管理, LLM Memory, 開発効率化]]

開発作業における「中断と再開」のコストを最小化するため、Claude Codeにリポジトリ単位の記憶領域を持たせる独自スキル「agent-memory」の実装と運用について解説された記事である。著者は、マルチタスクをこなす上で「メモを残して一旦忘れること」の重要性を説き、履歴を遡る手間の解消を目的としている。

このスキルの仕組みは非常にシンプルで、`.claude/skills/agent-memory/` 配下に要点をまとめたMarkdownファイルを生成・検索するというものだ。
特徴的なのは、エージェントが「思い出して」と指示を受けた際の挙動である。まず `ripgrep` (rg) を用いて全記憶ファイルのFrontmatterにある `summary` 行のみを抽出。そこから読むべきファイルを判断して詳細を読み込むという「Progressive Disclosure（段階的開示）」の考え方を採用している。これにより、大量の記憶があってもトークン消費を抑えつつ的確にコンテキストを復元できる。

著者が公式の「Memory MCP」や他のプラグインではなく、あえてファイルベースのAgent Skillsを自作した理由は、その「ポータビリティ」と「透明性」にある。
1. **ポータビリティ**: Markdownファイルと単純なテキスト検索に基づいているため、Claude CodeだけでなくCursorやGitHub Copilotなど他のエージェントツールからも参照が可能である。
2. **透明性**: 記憶がプレーンテキストとしてリポジトリ内に存在するため、人間が内容を確認・修正しやすく、ブラックボックス化を防げる。
3. **柔軟性**: `.gitignore` で除外することでプライベートな記憶領域として運用でき、リポジトリごとに独立した文脈（調査結果、決定事項、作業方針など）を保持できる。

筆者は、AIエージェントとの対話を通じて整理された「意図」や「判断」こそが、再開時に最も価値のある情報であると主張している。複雑なエコシステム（MCPなど）を導入せずとも、ファイルベースのシンプルな構造で十分に実用的な「自己成長するスキル」が構築できることを示す、極めて実践的な知見である。