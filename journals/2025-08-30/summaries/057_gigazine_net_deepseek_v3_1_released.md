## 「DeepSeek-V3.1」登場、推論モードと非推論モードを両立させてDeepSeek-R1より高速化したハイブリッドモデル

https://gigazine.net/news/20250822-deepseek-v3-1-released/

DeepSeekは、エージェント時代に向けた第一歩として、推論と非推論のハイブリッドモードを両立させ、高速化とエージェントスキルを強化した新モデル「DeepSeek-V3.1」をリリースしました。

**Content Type**: News & Announcements

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 75/100 | **Annex Potential**: 73/100 | **Overall**: 72/100

**Topics**: [[DeepSeek, LLM, AI Agent, Hybrid Inference, Benchmarking]]

中国のAI企業DeepSeekが、エージェント時代への重要な一歩としてハイブリッドモデル「DeepSeek-V3.1」をリリースしました。この新モデルの最大の特徴は、思考を伴う「Think」モードと直感的な「Non-Think」モードを一つのモデル内で両立させる「ハイブリッド推論スタイル」です。これにより、旧モデルDeepSeek-R1と比較してThinkモードでの思考速度が向上し、より短時間で高精度な回答を生成可能になりました。

Webアプリケーションエンジニアにとって重要なのは、DeepSeek-V3.1がツール使用や複数ステップを要するエージェントタスクのスキルを大幅に強化している点です。SWE-benchやTerminal-Benchといったベンチマークで旧モデルを上回るスコアを記録し、複雑な検索タスクにおける推論能力と効率が向上しています。APIも「deepseek-reasoner」(Thinkモード)と「deepseek-chat」(Non-Thinkモード)として提供され、128Kの長文コンテキスト長、Anthropic APIフォーマット、ベータ版では厳密な関数呼び出し(Strict Function Calling)に対応。これは、より賢く、より信頼性の高いAIエージェントや自動化された開発ワークフローを構築するための強力な基盤となります。

また、出力トークン数の削減は効率向上だけでなく、API利用コストの最適化にも直結します。開発者は、この高機能かつコスト効率の良いモデルを活用し、より洗練されたAI駆動型アプリケーションやサービスの開発を進められるでしょう。Hugging Faceでモデルデータが公開されている点も、開発者コミュニティにとってアクセスしやすく、多様な応用が期待されます。