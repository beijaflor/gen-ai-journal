## Qwen2.5-TTS：高い自然度と統一された構造を持つ次世代テキスト読み上げシステム

https://qwen.ai/blog?id=qwen3tts-0115

**Original Title**: Qwen2.5-TTS: An Advanced Text-to-Speech System with Unified Model Structure and High Naturalness

LLMベースの統一アーキテクチャを採用し、高い自然度とゼロショット音声複製を実現した次世代TTS「Qwen2.5-TTS」を公開。

**Content Type**: 📰 News & Announcements
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[Qwen2.5-TTS, テキスト読み上げ(TTS), 音声複製, FACodec, LLMバックボーン]]

AlibabaのQwenチームが、LLMのアーキテクチャを基盤とした新しいTTS（テキスト読み上げ）モデル「**Qwen2.5-TTS**」を発表しました。従来の複数の独立したコンポーネントを組み合わせるパイプライン型ではなく、**Qwen2.5 LLM**をバックボーンとして採用し、音声トークンを直接予測・生成する統一的な構造を特徴としています。

技術的には、**FACodec**を用いて音声を離散トークン化し、フローマッチングベースのデコーダーを組み合わせることで、極めてノイズの少ない高品質な出力を実現しています。わずか数秒の音声サンプルから話者の特徴を再現する**Zero-shot Voice Cloning**や、感情、スピード、ピッチの精密な制御が可能です。特に長文生成におけるプロソディ（抑揚）の一貫性が大幅に向上しており、ドキュメントの読み上げや対話型AIへの応用に適しています。音声アシスタントやナレーション機能を自社サービスに組み込みたい開発者にとって、有力な選択肢となるでしょう。