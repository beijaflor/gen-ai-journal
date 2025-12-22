## 【Backstage】GitHubをSupercharge！ 開発を加速するBackstageとの連携

https://techblog.ap-com.co.jp/entry/2025/12/08/110000

AI駆動開発時代に顕在化するリポジトリ管理の課題に対し、BackstageがGitHub連携を通じて開発生産性を向上させる方法を解説する。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:3/5
**Main Journal**: 74/100 | **Annex Potential**: 70/100 | **Overall**: 72/100

**Topics**: [[Backstage, GitHub, Platform Engineering, AI-driven Development, Developer Productivity]]

AI駆動開発が普及し、GitHub Copilotなどが開発効率を高める一方で、組織内でリポジトリが乱立する「リポジトリ・スプロール」が新たな課題として浮上しています。著者は、この状況が以下の3つの問題を引き起こすと指摘します。第一に、類似機能の乱立や再利用機会の損失により、情報を探す時間が増加し、結果的に開発生産性が低下する点。第二に、多数のリポジトリが存在することでオーナーシップが不明確になり、責任の所在や依存関係の問い合わせ先が曖昧になる点。第三に、新規リポジトリ作成時にブランチ保護ルールやGitHub Actions、Copilot Instructionなどの共通設定を手動で繰り返す手間とミスが発生する点です。これらの課題は以前から存在しましたが、AI駆動開発によりその頻度と影響が拡大しています。

記事は、これらの課題解決に効果的なツールとしてBackstageを紹介します。Backstageは、開発資産をカタログとして一元管理し、検索性向上と情報探索時間の削減を実現します。さらに、各カタログにオーナーを明示し、リポジトリ間の依存関係をグラフで可視化することで、オーナーシップの明確化を促進。また、Scaffolder Template機能により、GitHub ActionsやCopilot Instructionを含むリポジトリの初期設定をテンプレート化・自動化し、繰り返される共通設定作業の手間とミスを解消します。

Spotify社の調査では、Backstage導入によりGitHubアクティビティが2.3倍、開発者のコード変更頻度が2倍に増加し、デプロイ頻度向上や開発者定着率の改善が見られたと報告されています。これらのBackstageによる生産性向上効果は、AI駆動開発がもたらす効率と相まって、開発体験を大きく「スーパーチャージ」する可能性を秘めていると筆者は強調します。最後に、筆者の所属企業が提供するBackstageマネージドサービス「PlaTT」が、導入・運用・活用における「面倒」を解消すると締めくくっています。