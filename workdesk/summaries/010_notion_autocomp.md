## Autocomp: LLMによるテンソルアクセラレータコード最適化フレームワーク

https://adrs-ucb.notion.site/autocomp

**Original Title**: Autocomp: An ADRS Framework for Optimizing Tensor Accelerator Code

UC BerkeleyのSLICE Labが開発したAutocompは、LLMを活用してテンソルアクセラレータ向けコードを自動最適化する初のフレームワークで、AWS Trainiumで人間エキスパートのカーネルを最大17倍上回る性能を達成した。

**Content Type**: 🔬 Research
**Language**: en

**Scores**: Signal:5/5 | Depth:5/5 | Unique:5/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 92/100 | **Annex Potential**: 88/100 | **Overall**: 92/100

**Topics**: [[LLMコード生成, テンソルアクセラレータ, コンパイラ最適化, AWS Trainium, ADRS]]

UC BerkeleyのSLICE Labが開発したAutocompは、LLMを活用してテンソルアクセラレータ向けコードを自動最適化する初のフレームワークである。プロンプト変更だけで新しいハードウェアに適応可能な高い移植性を実現している。

テンソルアクセラレータの課題として、NVIDIAが市場を支配する理由はハードウェアだけでなく成熟したソフトウェアエコシステムにある点を指摘。Amazon、Apple、Cerebras、Google、Groq、Meta、Qualcommなど多くの企業が参入するも、固有のカーネル・コンパイラ・ランタイムが必要なため普及していない。アクセラレータプログラミングは固定サイズ行列乗算の効率的実行に特化し、明示的なデータ移動管理やソフトウェアパイプライニング等の高度な最適化が必要となる。

Autocompのアプローチは、Plan-then-Implement（2フェーズ最適化）を採用。Planフェーズでは LLMが最適化メニューから選択し自然言語で変換を記述、Implementフェーズでは計画に基づきLLMがコードを生成する。ビームサーチによる並列探索を行い、各候補は機能テストとサイクル精度シミュレーションで評価される。多様性向上のため、Optimization Menu Dropout（70-80%の確率でオプションをドロップアウト）とLLMアンサンブル（o4-miniとgpt-5の組み合わせ）を使用する。

AWS Trainium評価結果では、Tutorialワークロードで手動最適化コードを平均1.36倍上回り、入力コードから平均2.51倍高速化、PyTorchコンパイラ比13.52倍高速を達成。Advancedワークロード（AWSカーネルエンジニア作成）では平均1.9倍の高速化、1D Depthwise Convolutionで17.37倍の改善を実現した。対応プラットフォームはGemmini（学術）、AWS Trainium（産業）、Canaan K230（RISC-V）、NVIDIA L40S（GPU）。学習不要でLLMのインコンテキスト推論と事前学習済み知識を活用し、自然言語プランにより最適化トレースが解釈可能な点が特徴。
