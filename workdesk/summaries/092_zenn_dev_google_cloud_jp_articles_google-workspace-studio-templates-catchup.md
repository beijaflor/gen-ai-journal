## Google Workspace Studio のテンプレートを使ってみる - 日々の情報のキャッチアップ

https://zenn.dev/google_cloud_jp/articles/google-workspace-studio-templates-catchup

Google Workspace Studioのテンプレートを活用し、Geminiで生成AI関連ニュースを要約してGoogle Chatへ自動通知する具体的な手順を解説します。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:2/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 90/100 | **Annex Potential**: 83/100 | **Overall**: 68/100

**Topics**: [[Google Workspace Studio, Gemini, ワークフロー自動化, プロンプトエンジニアリング, Google Chat]]

この記事では、Google Workspace Studio (Workspace Studio) のテンプレートを利用して、日々の情報収集を自動化する具体的な方法を紹介しています。特に、Geminiを搭載したワークフローで生成AI関連のニュース速報を毎日Google Chatへ通知するフローの構築手順に焦点を当てています。

著者は、Workspace StudioがGoogle Workspaceで利用可能なGemini搭載の自動化サービスであり、提供されるテンプレートを活用することで一般的なユースケースを容易に構築できると説明しています。テンプレートはカテゴリ別に整理されており、Workspace Studioで実現できることの方向性を示しているため、フロー作成の指針にもなると強調しています。

具体的なニュース速報自動化フローは以下のステップで構成されます。まず「Step 1: 定期実行」で、[On a schedule]トリガーにより、指定した時間や周期（例：毎日、平日）でフローを実行するよう設定します。次に「Step 2: Geminiでニュース速報を生成」では、[Ask Gemini]アクションを使用し、過去24時間以内のGoogle Workspace AIトレンド、Gemini、Agentsなど、特定のAIトレンドに焦点を当てたニュース速報を生成するようGeminiに指示します。記事では、ニュースを効率的に要約し、関連リンクと絵文字を付けて読みやすくフォーマットするための詳細なプロンプト例が提示されており、プロンプトエンジニアリングの参考として重要です。最後に「Step 3: Google Chatでお知らせ」では、[Notify me in Chat]アクションで、Geminiが生成したニュース要約結果をGoogle Chatに通知するよう設定します。

著者は、この自動化されたフローにより、目覚ましい進化を遂げる生成AIの最新情報を効率的にキャッチアップし、情報収集にかかる時間を大幅に削減できるため、エンジニアがより戦略的な業務に集中できる環境を整えられると述べています。テンプレートの活用と簡単なカスタマイズで、迅速な知識アップデートが可能になる点が、このソリューションの重要な価値です。