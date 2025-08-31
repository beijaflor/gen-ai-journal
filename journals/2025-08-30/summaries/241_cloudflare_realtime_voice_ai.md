## Cloudflare is the best place to build realtime voice agents

https://blog.cloudflare.com/cloudflare-realtime-voice-ai/

Cloudflareは、エッジネットワークを活用したリアルタイム音声AIエージェント構築のための新機能「Realtime Agents」やWebRTCとWorkers AIの連携を発表し、自然な会話体験を実現する低遅延AIアプリ開発を大幅に簡素化します。

**Content Type**: 📰 News & Announcements

**Scores**: Signal:5/5 | Depth:4/5 | Unique:3/5 | Practical:5/5 | Anti-Hype:3/5
**Main Journal**: 83/100 | **Annex Potential**: 77/100 | **Overall**: 80/100

**Topics**: [[リアルタイム音声AI, エッジコンピューティング, WebRTC, Workers AI, 会話型AIエージェント]]

Cloudflareは、人間とAIの自然な音声対話を可能にするリアルタイム音声AIエージェントを構築するための新機能を発表しました。従来のテキストベースAIでは実現が困難だった、割り込みや即時応答といった自然な会話体験には、厳格な低遅延（800ミリ秒以内）が不可欠であり、音声認識（STT）、大規模言語モデル（LLM）、音声合成（TTS）の連携、そして複雑なオーディオパイプラインの管理が大きな課題となっていました。

今回発表された「Cloudflare Realtime Agents」は、この課題を解決するための専用ランタイムです。ユーザーに最も近いCloudflareのエッジネットワーク上で音声AIパイプライン（STT→LLM→TTS）をオーケストレーションし、遅延を最小限に抑えます。開発者は、WebRTCを介してオーディオをストリーミングし、JavaScriptクラスとしてエージェントを定義するだけで、中断検出やターンテーキングといった高度な会話ロジックを容易に実装できます。このフレームワークは、Workers AI、OpenAI、Anthropicなど複数のAIプロバイダーとの連携、テキストと音声の両入力/出力モード、ステートフルな会話コンテキスト維持に対応し、高い柔軟性を提供します。

さらに、CloudflareはWorkersでWebRTCオーディオをPCM形式で直接処理する機能を提供します。これにより、開発者はカスタムAIパイプラインを構築したり、リアルタイム文字起こしを行ったりする際に、WebRTCの低遅延特性（UDP、Opusコーデック、エコーキャンセル）を活かしつつ、Cloudflareネットワーク内でオーディオ処理を完結させることが可能になります。WebSocketsはサーバー間通信に適していますが、クライアントからサーバーへのリアルタイム音声にはWebRTCが優位であり、この組み合わせにより、開発者は既存のWebRTCクライアントやWebSockets経由で柔軟に接続できます。

また、Workers AIはWebSocket接続をサポートし、PipeCatのsmart-turn-v2モデルのようなターン検出AIを低遅延で利用できるようになります。これは、AIがユーザーの発言終了を自然に判断し、スムーズな対話を実現するために不可欠です。DeepgramのSTT/TTSモデルもWorkers AI上で利用可能となり、世界330以上の都市に展開されたCloudflareのグローバルネットワークを介して、エッジでの低遅延音声処理を実現します。

これらの機能により、ウェブアプリケーション開発者は、複雑なインフラ管理から解放され、自然な会話のような、これまでにない高速かつ応答性の高い音声AIアプリケーションを容易に構築できるようになります。特に、リアルタイム性とグローバルなスケーラビリティが求められるアプリケーションにおいて、Cloudflareのエッジプラットフォームは強力な基盤となるでしょう。