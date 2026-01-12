## Apple、単一画像から高品質な3DGSを生成する技術「SHARP」公開！ 一般的GPU環境で高速3Dシーン構築可能

https://cgworld.jp/flashnews/01-202601-SHARP.html

1枚の静止画から1秒未満で高品質な3D Gaussian Splatting（3DGS）を生成する新技術「SHARP」をAppleが公開した。

**Content Type**: 📰 News & Announcements
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 88/100 | **Annex Potential**: 85/100 | **Overall**: 84/100

**Topics**: [[3D Gaussian Splatting, Apple, SHARP, 生成AI, 3Dモデル生成]]

Appleが発表した「SHARP（Sharp Monocular View Synthesis in Less Than a Second）」は、単一の画像からフォトリアルな3Dシーンを瞬時に構築する単眼視点合成（MVS）技術である。最大の突破口は、ニューラルネットワークを用いた単一の順伝播パス（Feedforward pass）のみで、約120万個ものガウス分布パラメータを直接回帰・出力する点にある。これにより、従来の技術では困難だった「処理速度」と「ジオメトリの正確性」の両立を実現し、一般的なGPU環境においても1秒未満で3DGS（3D Gaussian Splatting）の生成を可能にした。

著者（Appleの研究チーム）によれば、この手法は特定の環境に特化した再学習を必要としない「Zero-shot generalization」を採用しており、未知の屋内・屋外風景に対しても即座に適用できる汎用性を持つ。また、生成される3D空間が現実世界の尺度であるメートル法（メトリックスケール）を保持している点も重要である。これにより、カメラの物理的な移動距離に基づいた正確な視点操作が可能となり、XRデバイスなどでの実用性が極めて高い。実験データでは、画像品質指標であるLPIPSやDISTSが大幅に改善され、合成時間は従来手法比で数千倍の高速化を達成したとしている。

Webアプリケーションエンジニアの視点では、生成された3DGSが既存のリアルタイムレンダラと親和性が高く、100fpsを超える高解像度描画に対応している点が注目に値する。すでにコミュニティでは本技術を用いたWebアプリなどの実装が始まっており、空間コンピューティングやWebXRコンテンツの制作フローを劇的に効率化する可能性を秘めている。コードとモデルウェイトはGitHubおよびHugging Faceで公開されているが、ライセンスはApple独自の「Apple Software License」および「Apple ML Research Model License」が適用され、主に研究・非営利目的が前提となっている点には注意が必要だ。