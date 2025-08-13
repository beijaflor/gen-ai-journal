## Slack上でみんなで育てるAI bot 「resident-ai」

https://developer.hatenastaff.com/entry/2025/08/05/180610

はてなは、SlackのCanvasをシステムプロンプトとして活用し、チャンネルごとにパーソナリティが変化する独自AIボット「resident-ai」を構築、その技術的詳細と実装課題を公開しました。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 90/100 | **Annex Potential**: 93/100 | **Overall**: 92/100

**Topics**: [[Slack Bot Development, AI System Prompts, Canvas API, LLM Integration, Internal Tooling]]

はてな社内で開発されたAIボット「resident-ai」は、Slackの各チャンネルに設定されたCanvasをAIのシステムプロンプトとして活用する画期的な仕組みを導入しました。これにより、チャンネルごとに異なるAIの個性や振る舞いを柔軟に設定でき、例えばウニのキャラクターで返答したり、返答後に川柳を詠んだりするなど、多様な対話が可能になります。

このアプローチの重要性は、従来のプロンプト管理の煩雑さを解消し、ユーザー体験を大幅に向上させた点にあります。これまでのボットでは、DataStoreにプロンプトを保存し、コマンドやプロンプト名を毎回指定する必要がありましたが、「resident-ai」はチャンネルのCanvasを自動で読み込むため、ユーザーは追加操作なしでコンテキストに応じたAIとの対話を開始できます。

実装面では、Slack APIの深い理解と工夫が光ります。特に、`conversations.info`でCanvasの`file_id`を取得し、`files.info`経由でCanvasのHTMLコンテンツをダウンロードする手法は、ドキュメントに明記されていない部分をSandboxワークスペースでの調査で見つけ出したものです。取得したHTMLからは、無駄なトークン消費を避けるために不要なID属性を除去し、チェックボックスやテーブルなどの要素もAIが適切に解釈できるよう指示を追加しています。また、スレッド内での連続会話を実現するため、自身のボットユーザーIDを`users.profile.get`と`bots.info`から取得する技術も詳細に解説されています。

この「resident-ai」は、開発者が日常的に利用するSlackというプラットフォーム上で、AIをより身近で実践的なツールとして活用するための具体的なソリューションを示しています。チャンネルの特性に合わせてAIの振る舞いを細かく調整できるため、チームやプロジェクトの生産性向上に直結する可能性を秘めています。これは、内部ツールとしてのAI活用において、コンテキスト管理の課題に対する非常に有効なアプローチであり、今後のAIツールの設計にも示唆を与えるでしょう。