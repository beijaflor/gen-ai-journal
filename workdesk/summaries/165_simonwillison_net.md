## Qwen3-TTSファミリーがオープンソース化：音声デザイン、クローン、生成が可能に

https://simonwillison.net/2026/Jan/22/qwen3-tts/

**Original Title**: Qwen3-TTS Family is Now Open Sourced: Voice Design, Clone, and Generation

わずか3秒の音声からクローンを生成できる多言語TTSモデル「Qwen3-TTS」をQwenチームがオープンソースで公開した。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 85/100 | **Annex Potential**: 81/100 | **Overall**: 80/100

**Topics**: [[Qwen3-TTS, 音声クローン, オープンソース, Text-to-Speech, mlx-audio]]

Alibabaの**Qwen**チームが、最新のオープンソース音声合成モデル**Qwen3-TTS**シリーズをリリースしました。このモデルは10言語に対応し、わずか3秒の音声サンプルから高精度な**音声クローン**を作成できるほか、テキストによる記述（例：「しわがれた声」）で音声の質感を細かく制御できるのが特徴です。モデルサイズは**0.6B**（約2.5GB）と**1.7B**（約4.5GB）の2種類が用意され、**Apache 2.0**ライセンスで提供されています。

**Hugging Face**のデモを通じてブラウザ上ですぐに試用できるほか、**mlx-audio**ライブラリや**uv**コマンドを利用したCLI実行も可能です。筆者のSimon Willison氏は、高性能な音声クローン技術がGPU搭載PCやブラウザだけで完結するほど身近になったことの重要性を指摘しています。アプリケーションへの高品質な音声合成の組み込みや、エッジデバイスでの実行を検討しているエンジニアにとって、非常に実用的な選択肢となります。