## 【デザイナーの視点が変わる】Cursor と Devin で爆速化した UI 改善

https://zenn.dev/kikagaku/articles/79368e7981a00f

CursorとDevinがデザイナーのUI改善ワークフローを革新し、Figmaとコード間のギャップを埋める。

[[UI/UXデザイン, AI開発ツール, デザイナーワークフロー, Figma連携, DevOps]]

この記事は、AIツールであるCursorとDevinがUI改善におけるデザイナーの役割と視点をどのように変革しているかを解説しています。従来、デザイナーはFigmaでデザインを作成し、エンジニアに実装を依頼していましたが、これらのツールにより、デザイナー自身が開発環境でUIを直接修正し、プルリクエストを作成できるようになりました。

CursorはFigmaのデザインとコードを直接連携させ、デザインと実装の差異を即座に確認・修正することを可能にし、デザイナーの作業負担を軽減します。特に`html.to.design`のようなプラグインは、コードからFigmaへのUIコンポーネントのインポートを容易にします。これにより、Figmaコンポーネントをコードに反映させる障壁が低くなり、UIの一貫性をコードベース内で確保できるようになります。

Devinは、これまでエンジニアの関与が必要で遅延しがちだった小さなUI改善のプルリクエストを、デザイナーが自ら作成することを可能にします。自然言語での指示を通じて、修正からPR作成までのプロセスを簡素化し、エンジニアの手を煩わせることなくUI改善を推進できます。これにより、デザインと実装のサイクルが加速し、発見された改善点を粒度や優先度に関わらず迅速に反映できるようになります。

これらのツールの導入は、デザイナーがFigmaとコードを連携させ、実装イメージを確認・修正し、Devinを用いて自らPRを作成し、レビュー後に即座に本番環境に反映させるという新しいワークフローを確立します。これは、デザインシステム運用の効率化と、小さなUI変更の迅速な反映を可能にし、デザイナーとエンジニア間の協業をよりシームレスにする点で重要です。

---

**編集者ノート**: Webアプリケーションエンジニアの視点から見ると、この記事はデザイナーと開発者の間の長年の課題であった「デザインと実装の乖離」に、AIが具体的な解決策をもたらし始めていることを示唆しています。CursorやDevinのようなツールが普及すれば、デザイナーはよりコードに近い場所で作業するようになり、UIの微調整や改善が開発サイクルにボトルネックとなることが劇的に減少するでしょう。これは、エンジニアがより複雑なロジックやパフォーマンス最適化に集中できる時間を増やし、結果として開発全体の生産性を向上させます。将来的には、デザイナーが簡単なUI変更であればコードを直接編集し、AIがその変更をレビューして自動でPRを作成するような、より統合された「デザイン・開発パイプライン」が標準となる可能性が高いと予測します。エンジニアは、AIが生成したコードの品質を評価し、デザインシステムとの整合性を保つための新たなスキルが求められるようになるでしょう。

