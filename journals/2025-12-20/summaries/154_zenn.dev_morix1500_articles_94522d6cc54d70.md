## STTとTTSの性能比較をするツール「Hikaku-Voice」を作った

https://zenn.dev/morix1500/articles/94522d6cc54d70

Morix氏がSTTとTTSの進化の速さに対応するため、複数モデルの認識精度やレスポンス速度を簡単に比較できるツール「Hikaku-Voice」を開発し、その導入方法と開発背景を解説します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 81/100 | **Annex Potential**: 80/100 | **Overall**: 80/100

**Topics**: [[音声AI, STT, TTS, 性能比較ツール, LiveKit Agents]]

著者のMorix氏は、仕事で音声AIアプリケーションを開発する中で、STT（Speech to Text）とTTS（Text to Speech）技術の急速な進化と、それら新モデルの性能評価の困難さに直面しました。日々登場する新しいSTT/TTSモデルの認識精度や音声品質、レスポンス速度の改善を自社製品に迅速に組み込むためには、効率的な検証が不可欠です。しかし、既存の検証プロセスは時間と労力がかかり、エンジニア以外のプロダクトマネージャー（PdM）が簡単に性能を評価できる環境がないことが課題でした。

この課題を解決するため、Morix氏は、複数のSTTおよびTTSモデルの性能を簡単に横並びで比較できるツール「Hikaku-Voice」を開発しました。このツールは、STTの比較画面ではマイク入力に対する書き起こし結果とレスポンス速度を、TTSの比較画面ではテキスト入力に対する音声変換結果とレスポンス速度（TTFB: Time to First Byte）をリアルタイムで表示します。これにより、開発者はもちろん、PdMも直感的に異なるモデルの性能差を把握し、導入判断の材料とすることができます。

「Hikaku-Voice」のモデル追加の肝は、LiveKit Agentsのプラグイン機構を利用している点です。LiveKit AgentsがSTT/LLM/TTSをプラグイン形式で容易に追加できる仕組みを提供しているため、ユーザーはLiveKit Agentsのプラグインをインストールし、設定ファイルに記述するだけで、Deepgram Nova 2/3やOpenAI RealtimeといったSTTプロバイダの異なるモデルを自由に組み合わせて比較検証が可能です。

Morix氏はこのツールを、Google Antigravityの検証を兼ねてわずか2日間で開発したと述べています。開発終盤でRateLimitに遭遇し、Claude Codeに助けを求めるという具体的なエピソードも語られています。本ツールは、音声AIアプリケーション開発におけるモデル選定と評価の負担を軽減し、開発プロセスの加速と製品品質の向上に大きく貢献する実用的なソリューションです。音声AIに関わる多くの開発者にとって価値のあるツールとなるでしょう。