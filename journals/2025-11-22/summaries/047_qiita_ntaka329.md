## 【徹底比較】AI自律実装ツールでFedGAN論文を実装してみた - Copilot vs Antigravity × Claude/Gemini

https://qiita.com/ntaka329/items/3b02073156239125bd6a

著者は、GitHub Copilot Plan modeとGoogle Antigravity（Claude/Gemini連携）というAI自律実装ツールを比較し、FedGAN論文の実装を通じて、現時点での実用性と開発体験における重要な選択基準を明確にした。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:5/5
**Main Journal**: 91/100 | **Annex Potential**: 90/100 | **Overall**: 92/100

**Topics**: [[AI自律実装ツール, FedGAN, LLM比較, 開発体験, コード品質]]

本記事では、GMOコネクトの永田氏が、AIによる自律実装支援ツールの実力を検証した。具体的には、GitHub Copilot Plan mode（Claude Sonnet 4.5連携）、Google Antigravity（Gemini 3.0 Pro連携）、そしてAntigravity（Claude Sonnet 4.5連携）の3パターンを比較対象とし、FedGAN論文の「Algorithm 1」のPoC実装を試みている。実装品質、コード品質、GANの学習結果、そして開発体験の4つの観点から定量・定性評価が実施された。

検証の結果、AntigravityとClaude Sonnet 4.5の組み合わせが、実装精度、コード品質、GANの学習収束のすべてにおいて最高の評価を獲得した。この組み合わせで生成されたコードは、著者の好みにも合い、非常に分かりやすかったと評価されている。一方、AntigravityとGemini 3.0 Pro、およびCopilot Plan modeとClaude Sonnet 4.5の組み合わせでは、FedGANにおける重み加重平均の欠落やGPU最適化の漏れ、学習の不安定性といった実装上の不備が散見された。特にCopilotの生成コードはクラス定義がなく、学習結果も不安定であったと報告されている。

開発体験の観点では、Antigravityは実装計画への行単位でのコメント機能や、CLI実行ログがAgentウィンドウ内に統合されている点、さらに作業結果をwalkthroughとしてまとめてくれる点がメリットとして挙げられた。これにより、フィードバックのしやすさや状況把握の効率性が向上するとされている。ただし、著者の環境ではAgent Managerがフリーズするという課題も指摘されている。また、Plan段階でAIが確認してくる質問の質や量も、ツールやモデルによって大きく異なり、これが実装品質を左右する重要な要素であると強調している。

結論として、現時点で実務投入の現実味があるのはAntigravityとClaude Sonnet 4.5の組み合わせのみであり、他のツール・モデルはレビューや修正が前提となると著者は述べている。AI自律実装ツールの選定においては、計画段階での質問の質、フィードバック機能、そして実行ログの統合といった開発体験が実装品質に直結する鍵となると結論付けている。