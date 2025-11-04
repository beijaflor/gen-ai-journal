## BedrockのClaudeクォータ緩和申請の手順が簡単になったよ！

https://qiita.com/minorun365/items/bc58bbb2490ef1b5fdee

AWS BedrockにおけるClaudeモデルのクォータ緩和申請が、Service Quotasコンソールから直接可能となり、手続きが大幅に簡素化された。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 84/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[AWS Bedrock, Claude, クォータ管理, Service Quotas, AIエージェント]]

AWSの生成AIサービスであるAmazon Bedrockを利用してClaudeなどのモデルAPIを使用する際、新規アカウントでは分間リクエスト回数（RPM）などにレートリミットが設定されています。これまではクォータの引き上げにAWSサポートへのチケット起票が必要で、その煩雑さが課題でした。

しかし、今回の更新により、BedrockのClaude利用クォータ緩和申請がAWSマネジメントコンソールの「Service Quotas」画面から直接行えるようになり、手順が大幅に簡素化されました。この変更は、開発者にとってBedrockを使ったAIモデルの利用開始やスケールアップの大きな障壁が取り除かれたことを意味します。

新しい手順では、Bedrockを利用したいリージョンで「Service Quotas」にアクセスし、「Amazon Bedrock」を選択します。「クォータの表示」から「Cross-region model inference requests per minute for <モデル名>」や「Cross-region model inference tokens per minute for <モデル名>」といった主要なクォータを探します。特に、「調整可能性」が「アカウントレベル」となっているものが直接申請可能になった対象です。該当するクォータ名をクリックし、「アカウントレベルでの引き上げをリクエスト」から簡単に緩和申請を送信できるようになりました。

著者は、この改善が「めちゃくちゃ簡単になった」と評価し、「最初からこうしといてくれ！！！」と、長らく待望されていた機能であることを強調しています。特に、AIエージェントの構築や運用においてBedrockの利用が不可欠となるケースが多いため、この簡素化は開発ワークフローに即座にポジティブな影響を与えるでしょう。