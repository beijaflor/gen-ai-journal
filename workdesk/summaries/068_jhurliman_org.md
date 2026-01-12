## Ableton MCPを用いたAIによる音楽制作の実験：DAW操作の自動化とエージェント化への挑戦

https://jhurliman.org/post/804323197731373056/experiments-with-ableton-mcp-dec-2025

**Original Title**: Experiments with ableton-mcp (Dec 2025)

MCP（Model Context Protocol）を介してDAW（デジタル・オーディオ・ワークステーション）とLLMを統合し、AIエージェントによる楽曲制作と自動化の新たなワークフローを提示する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:5/5 | Practical:3/5 | Anti-Hype:4/5
**Main Journal**: 82/100 | **Annex Potential**: 86/100 | **Overall**: 84/100

**Topics**: [[MCP, Ableton Live, AI Agents, Music Production, Claude Code]]

著者のJohn Hurliman氏は、2025年12月の実験として、Model Context Protocol（MCP）を利用してプロフェッショナル向けDAWである「Ableton Live」をLLM（Claude 4.5 Opus）から操作する試みを行いました。既存のオープンソースプロジェクト「ableton-mcp」をベースに、LLM自身にドキュメントを読み込ませ、70以上のオートメーションツールを自律的に開発・実装させることで、音楽制作における「AIペアプログラマー」としての可能性を追求しています。

技術的な側面では、Python APIで公開されていない機能を操作するために、LLMがAbletonのプロジェクトファイル（.als）をリバースエンジニアリングして直接編集する手法を採用しました。これにより、テンポや音量のオートメーション、ワープマーカーの挿入といった高度な操作が可能になっています。さらに、LLMの最大の弱点である「音が聞こえない（聴覚的フィードバックの欠如）」を克服するため、Max4Liveを用いた録音機能と、Replicate上で動作する音楽解析モデル（Music Flamingo等）を組み合わせたフィードバックループを構築しました。これにより、LLMが生成した音声を「聴き」、その構造や特徴に基づいて次の編集操作を決定するエージェント的な動作を実現しています。

著者はこの仕組みを用いて、実際に2つの既存楽曲を組み合わせたマッシュアップ制作を行い、そのプロセスを公開しました。筆者によれば、このアプローチの真価は単なる自動化ではなく、DAWのような学習曲線が急峻で複雑なツールの習得を劇的に加速させる点にあります。AIを「操作の代行者」としてだけでなく「対話的な共同制作者」として扱うことで、未経験に近い状態から数日で完成度の高い成果物を得られた経験は、エンジニアリングにおける生成AIの活用（Vibe Coding等）と音楽制作の境界線が消失しつつあることを示唆しています。Webエンジニアにとっても、MCPがいかにして複雑なデスクトップアプリケーションやバイナリフォーマットをLLMの操作対象へと変貌させるかを示す、極めて示唆に富む実例となっています。