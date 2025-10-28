## Foundation Models Frameworkで絵文字を推薦させる仕組み

https://zenn.dev/azookey/articles/153b1bf4da1119

AppleのFoundation Models Frameworkを活用した絵文字推薦機能の実装について、オンデバイスLLMの利用と、CoreTextで複数のコードポイントから成る見かけ上1文字の絵文字を正確にフィルタリングする技術的課題とその解決策を解説する。

**Content Type**: ⚙️ Tools

**Scores**: Signal:5/5 | Depth:5/5 | Unique:5/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 98/100 | **Annex Potential**: 97/100 | **Overall**: 96/100

**Topics**: [[Foundation Models Framework, On-device LLM, Emoji Recommendation, Unicode Text Segmentation, CoreText API]]

キーボードアプリ「azooKey」がiOS 26で導入されたFoundation Models Frameworkを活用し、文脈に応じた絵文字推薦機能を実装した経緯が詳細に語られています。このフレームワークは、Apple Intelligenceにも使われるオンデバイスLLMをアプリに簡単に組み込めるため、知的な振る舞いをアプリケーションに追加する有力な手段となります。特に、`@Generable`マクロを用いたStructured Outputへの円滑な対応は、LLMの応答をアプリケーションで扱いやすくする点で画期的です。

しかし、実装過程では予期せぬ技術的課題に直面しました。「1文字の絵文字」という要件に対し、Swiftの`String.count`プロパティではZero-Width Joiner (ZWJ)などの特殊文字が結合された絵文字を正しく判別できないという問題が発生しました。例えば、「😴‍💨」のように複数のコードポイントとZWJが結合し、Swift上は1文字と認識されながらも実際には2文字として描画されるケースです。これは、LLMがUnicodeの「Emoji ZWJ Sequence」に定義されていない、非標準の組み合わせを生成してしまうことで顕在化しました。

この課題に対し、Emoji ZWJ Sequenceリストをアプリに組み込む手法では、Unicodeの更新頻度やOSバージョン対応によるメンテナンスコストの高さが指摘されます。azooKeyが採用したのは、CoreTextのAPI（`CTLineCreateWithAttributedString`や`CTRunGetGlyphCount`）を利用して、対象の文字列が実際に1つのグリフとしてレンダリングされるかをチェックするという洗練された解決策です。これにより、OSがサポートするUnicodeバージョンに依存せず、レンダリング結果として確実に1文字であることを保証し、メンテナンスコストを大幅に削減できるという実用的な知見が提供されています。

本記事は、オンデバイスLLMの導入事例としてだけでなく、テキスト処理におけるUnicodeの複雑さと、それを回避するための低レベルAPI活用術という、Webアプリケーションエンジニアにとっても普遍的な学びを提供する点で非常に価値が高いです。LLMの出力を鵜呑みにせず、基礎的な文字コード・レンダリング技術を深く理解し組み合わせることで、より堅牢でユーザーフレンドリーな機能を実現できる「なぜそれが重要なのか」を具体的に示しています。