## OpenAIの「gpt-oss-20b」をM2 Pro Mac minで動かしてみた

https://zenn.dev/shakshi3104/articles/53e7f35ae376df

OpenAIが公開したOSS LLM「gpt-oss-20b」をM2 Pro Mac miniでローカル実行し、LM Studioを使った回避策と実測性能、そして生成例を詳述します。

**Content Type**: ⚙️ Tools

**Scores**: Signal:4/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 84/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[OpenAI, LLM, Apple Silicon, Local LLM Deployment, LM Studio]]

本記事は、OpenAIが公開したOSSのLLM「gpt-oss-20b」をM2 Pro Mac mini上で動作させた際の詳細な検証結果を報告します。筆者はまず、一般的な`transformers`ライブラリでの実行を試みましたが、MXFP4量子化がNVIDIA GPUを必須とするため、Apple Siliconではエラーが発生するという課題に直面しました。

この問題を解決するため、ローカルLLM実行ツール「LM Studio」を利用したところ、無事に動作に成功。具体的な性能として、約35.45トークン/秒の出力速度と、RAM約28GBのメモリ使用量で安定して動作することを確認しました。これは、M2 Proのような一般的な消費者向けハードウェアでも200億パラメータ級のLLMを実用的な速度でローカル実行できる可能性を示す、エンジニアにとって非常に重要な示唆です。

生成例として、正確な情報（たまごっちの説明）と、事実と異なる情報（なにわ男子のメンバー構成における幻覚）の両方が示されており、ローカルでLLMを利用する際にも、出力の正確性検証が不可欠であることが強調されています。

本検証は、ウェブアプリケーションエンジニアが、API利用に頼らずローカル環境でLLMの機能を取り入れたり、プライバシー要件の高いタスクでLLMを活用したりする際の具体的な指針となります。特に、Apple Siliconユーザーにとっては、強力なモデルをオンプレミスで動かす現実的な選択肢と、その際のパフォーマンスや注意点を知る上で貴重な情報であり、開発ワークフローの可能性を広げる一歩となるでしょう。