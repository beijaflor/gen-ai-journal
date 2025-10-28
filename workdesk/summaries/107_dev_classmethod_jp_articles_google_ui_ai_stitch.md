## GoogleのUI生成AIツール「Stitch」を試してみた

https://dev.classmethod.jp/articles/google-ui-ai-stitch/

ClassmethodのエンジニアがGoogle LabsのUI生成AIツール「Stitch」を実際に使用し、その実用性と限界を検証しています。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:3/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 71/100 | **Annex Potential**: 70/100 | **Overall**: 72/100

**Topics**: [[UI生成AI, Google Stitch, プロトタイピング, Web開発ツール, Geminiモデル]]

著者は、カナダのエンジニアから勧められたGoogle LabsのUI生成AIツール「Stitch」を実際に試し、その機能と使用感を共有しています。Stitchは、自然言語や画像入力でWeb/モバイルUIを生成し、HTMLコード表示やFigmaエクスポートに対応。現時点（2025/10/16）では完全無料で、GoogleのマルチモーダルLLM「Gemini 2.5 Pro」または「Gemini 2.5 Flash」を搭載している点が特長です。月ごとのプロンプト制限はFlashで350回、Proで200回と、個人開発レベルでは十分な回数が提供されています。

実際に著者は、簡単な物体検出Webアプリ用のUIをStitchで生成する過程を詳細に説明しています。初期プロンプトでシンプルなUIが生成された後、不要な要素の削除や「戻る」ボタンの追加といった指示を自然言語で与えることで、イメージ通りのUIへと調整できることを実証しました。生成されたHTMLコードは既存のアプリに容易に統合でき、質素な画面が見違えるほど洗練されたと評価しています。

本記事の著者は、Stitchがモックアップ制作には非常に有用なツールであると結論付けています。「とりあえずアプリは作ったがUI実装が面倒」といった場面で、自然言語入力だけで質の高いUIを迅速に作成できる点は大きなメリットです。しかし、独自性やピクセル単位の精度が求められるプロダクト、あるいは10画面以上の大規模なUI管理には不向きであり、あくまでプロトタイプ作成用として割り切った使い方が適切であると指摘しています。Beta版であり、今後の機能拡充に期待が寄せられています。