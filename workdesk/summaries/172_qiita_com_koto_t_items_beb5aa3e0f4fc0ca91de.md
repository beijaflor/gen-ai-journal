## 【Slack自動化】休暇表示をミスらない！Bolt×AWSで作る休暇報告アプリ #Python - Qiita

https://qiita.com/koto-t/items/beb5aa3e0f4fc0ca91de

Bolt for PythonとAWSを活用し、Slackの休暇報告・表示名変更を自動化する社内アプリの開発プロセスと、権限管理やデプロイにおける実践的な課題解決策を解説します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 84/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[Slack Bot Development, AWS Lambda, Infrastructure as Code, OAuth/API Permissions, Internal Tooling]]

リモートワークやフレックス勤務環境下で、チームメンバーの休暇状況を把握することは課題となりがちです。Slackの表示名での休暇通知は効果的ですが、変更や復元を忘れやすいという問題がありました。本記事は、この課題を解決するため、**Bolt for Python**と**AWS（Lambda、EventBridge Scheduler）**を組み合わせた社内Slackアプリ「休み報告お助け君」の開発事例を詳述しています。このアプリは、ユーザーの表示名を自動で休暇情報付きに変更し、休暇終了後にはEventBridge Schedulerで元の表示名に自動で戻す機能を核とします。また、勤怠チャンネルへの報告も自動化し、シンプルな操作性を実現しています。

Webアプリケーションエンジニアにとって重要な知見は、開発過程で直面した具体的な課題とその解決策にあります。一つは、SlackのカスタムワークフローからBoltアプリで直接モーダルを開けない問題。`trigger_id`の取得が必要なため、毎朝ボタン付きメッセージを送るアプローチを採用した点は、Slack APIの挙動理解に役立ちます。もう一つはOAuth権限の不足です。開発者自身の権限では動作しても、他のユーザーで機能しない落とし穴を指摘し、`as_user=True`の適用と早期の複数ユーザーテストの重要性を強調しています。これはAPI連携における権限管理の典型的な課題です。

表示名を元に戻す仕組みは、EventBridge SchedulerがLambdaを起動し、現在の表示名がアプリが設定した休暇情報と一致するかを確認することで、手動変更との競合を避ける堅牢な設計です。さらに、AWS CDKの導入が本番環境へのスムーズな移行に大きく貢献しました。環境ごとのスタック分離や、DBとアプリのスタック管理を分けることで、デプロイの安全性と再現性を高め、インフラのコード化のメリットを実証しています。

この事例は、Slack APIとAWSの組み合わせによる業務効率化の実践的なアプローチを示し、特にAPI連携時の権限管理、堅牢な機能設計、そしてAWS CDKを用いた効率的なインフラデプロイ戦略は、同様の社内ツール開発や自動化プロジェクトに取り組むエンジニアにとって貴重な学びとなります。