## Claude Code GitHub Actions で Dependabot が作成した PR を自動マージ

https://developers.cyberagent.co.jp/blog/archives/60598/

CyberAgentは、Claude Code GitHub Actionsを活用し、Dependabotが作成するPRをAIでレビューして安全に自動マージするワークフローを構築しました。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[AI Code Review, GitHub Actions, Dependabot Automation, LLM in DevOps, Workflow Automation]]

本記事では、CyberAgentがDependabotによる依存パッケージのバージョンアップPRの自動マージを、AIを活用して安全に実現した事例を紹介しています。大規模システムでは依存パッケージが多く、セキュリティ維持のためには定期的な更新が不可欠ですが、全てのPRを手動で確認するのは開発者にとって大きな負担です。多くのDependabot PRは軽微な変更であり、安全にマージできるため、この手作業の自動化が求められていました。

著者は、「そのままマージしても安全にリリースできるPR」の条件として、「patch/minorバージョンアップ」「信頼できる開発元」「CI通過」「破壊的変更なし」「利用中の関数への影響なし」の5つを定義。このうち最初の2つはGitHub Scriptによるルールベースで判定し、残りの「破壊的変更なし」「利用中の関数への直接的な影響なし」の2点を、Claude Code GitHub Actionsを用いたAIレビューで判断するハイブリッドなワークフローを設計しました。

具体的には、ルールベースの条件が満たされた場合にPRのAuto Mergeを有効化。その後、Claude Code GitHub ActionsがPRの変更内容を詳細にレビューし、破壊的変更の有無やコードの実際の利用箇所への影響を評価します。安全であると判断されればAIがPRを承認し、CIが通過した時点で自動マージが実行される仕組みです。プロンプトには、レビューの観点、禁止事項、出力フォーマット、そして承認コマンド「`gh pr review -a`」の使用方法が詳細に指示されています。

このシステムにより、安全と判断されたPRはDependabot作成からわずか2分でマージされるケースが確認され、開発者のレビュー負荷が大幅に軽減されることが実証されました。信頼できないパッケージのPRは意図通りスキップされ、安全性が担保されています。著者は、生成AIが「要件は明確だがルールベースでは判断しにくい」タスクの自動化を可能にする一方、この成功は充実したCI/CDやデプロイフローといった、従来のソフトウェアエンジニアリングのベストプラクティスが基盤として存在していたからこそ実現できたと強調しています。