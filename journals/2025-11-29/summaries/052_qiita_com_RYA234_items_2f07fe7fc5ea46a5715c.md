## Antigravityを使ってWindows FormsからBlazor Hybridへの移行と動作確認用のテストを実装してみた #C#

https://qiita.com/RYA234/items/2f07fe7fc5ea46a5715c

AntigravityとGoogle Gemini 1.5 Proを活用することで、レガシーなWindows FormsアプリケーションのBlazor Hybridへの移行と、堅牢なbunitによるコンポーネントテストの実装が効率的に実現できることを実証した。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 86/100 | **Annex Potential**: 84/100 | **Overall**: 84/100

**Topics**: [[Blazor Hybrid, Windows Forms Migration, bunit, AI-assisted Development, Antigravity]]

著者は、レガシーなWindows FormsアプリケーションをモダンなBlazor Hybrid（WPFホスティング）へ移行し、bunitを用いたコンポーネントテスト環境を構築した手順とその効果を解説している。この移行作業は、AI開発環境「Antigravity」と「Google Gemini 1.5 Pro」を全面的に活用して進められた。

この取り組みの意義は、AIがコード解析からBlazor Hybridコード生成（Razor, CSS, C#）、bunitテストコードの実装、さらにはドキュメント作成に至るまで、開発プロセスの大部分を自動化した点にある。特に、Windows Formsのロジックをプラットフォーム非依存のCalculatorServiceクラスに抽出し、UIをCalculator.razorとして再実装することで、UIとロジックの明確な分離を実現している。

テスト戦略では、当初検討したWinAppDriverがWebView2内の要素認識に課題を抱えたため、より堅牢で高速なbunitへの転換が図られた点が重要だ。bunitを採用することで、ブラウザを起動せずC#コードのみでBlazorコンポーネントのロジックとレンダリング結果を検証できるようになり、WinAppDriverと比較してテスト実行時間が大幅に短縮（数十秒〜数分から0.8秒へ）され、安定性も向上した。

定量的効果として、AI支援により開発工数は約0.5時間と大幅に短縮され、コード行数はWindows Forms版の約350行からBlazor Hybrid版の約200行へと約40%削減された。また、ロジックとUIの分離により、将来的なMAUIへのクロスプラットフォーム展開が容易になり、CSSによる柔軟なデザインも低コストで実現可能になった。AIのトークン使用量も合計約33,000トークンと、Gemini 1.5 Proの費用感から見ても非常に効率的だったと報告されている。

著者はAntigravityの直感的な操作感や、ビルド・テスト実行の自動化機能に驚きを示し、古いフレームワークからの移行作業におけるAIの想像以上の実用性を高く評価している。一方で、現時点ではVisual Studioでのビルドに未対応という課題も指摘しつつ、今回の経験を通じてBlazor学習の必要性を感じ、データベース連携など、より実践的な機能のリファクタリングへの意欲を語っている。この事例は、レガシーコードのモダン化においてAIと適切なテスト戦略がいかに強力なツールとなるかを示唆している。