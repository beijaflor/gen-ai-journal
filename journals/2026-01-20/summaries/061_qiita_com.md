## 自前の Claude Code 拡張機能 marketplace 開発サイクルの具体例

https://qiita.com/yoshiwatanabe/items/3c8feaaa1ac4d7288b09

Claude Code拡張機能のパッケージ化と配布における混乱を防ぐため、開発・パッケージ化・検証の3フェーズを独立したレポジトリで管理する堅牢なワークフローを構築する。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 83/100 | **Annex Potential**: 81/100 | **Overall**: 80/100

**Topics**: [[Claude Code, AIエージェント, Marketplace, 開発ワークフロー, Vibe Coding]]

Claude Codeの拡張機能（SkillsやCommands）を再利用可能な形式で配布するには、marketplaceとしてのパッケージ化が不可欠である。しかし、著者は現状の課題として、ローカル開発環境と配布用パッケージ構造の不一致や、LLM特有の挙動を挙げている。特に、拡張機能に不具合があってもLLMが自力で問題を回避して目的を達成してしまい、バグが潜在化しやすいという指摘は、AIエージェント開発における重要な視点である。

著者はこれらの問題を回避するため、開発フローを以下の3つの専用レポジトリに分離する手法を提唱している。

1. **開発フェーズ（marketplace-development）**: Claude Codeを用いた「バイブコーディング」で機能を構築する段階。ここでは動作確認用の`TESTING.md`に加え、次フェーズへの物理的なコピー手順を記した`MIGRATION.md`をLLMに作成させることが肝要である。
2. **パッケージ化フェーズ（marketplace-demo）**: 開発した機能をmarketplaceのディレクトリ構造に適合させる段階。`plugins`ディレクトリへの配置や、`marketplace.json`へのメタ情報追加など、配布可能な形式に整える。
3. **検証フェーズ（marketplace-testclient）**: 配布用パッケージが実際に別のプロジェクトから正しくインストール・実行できるかを検証する段階。ホームディレクトリの`.claude`環境にプラグインが正しく反映されるか、UIを通じて最終確認を行う。

筆者によれば、複数のレポジトリを跨ぐことで作業速度は多少落ちるものの、構造の理解しやすさと、更新後のバグ混入を確実に防げるメリットがそのコストを上回るとしている。AI coding Assistantを単なるコード生成ツールとして使うだけでなく、その拡張エコシステムを「製品」として管理するための実戦的な知見が示されている。ウェブアプリケーションエンジニアにとって、急速に進化するClaude Codeの拡張性を最大限に引き出し、チーム内で安全にツールを共有するための標準的な雛形として非常に価値が高い内容となっている。