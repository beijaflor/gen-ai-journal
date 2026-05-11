## ⚡製図革命2.0⚡draw.io で図を作る AI スキルを作ってみた🚀

https://qiita.com/aktsmm/items/199869941e2d6a8b46a0

**AIエージェントを用いて編集可能なdraw.io形式の図面を自動生成する仕組みを構築し、設計図作成の工数削減を実現する。**

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 89/100 | **Annex Potential**: 87/100 | **Overall**: 88/100

**Topics**: [[draw.io, VS Code, GitHub Copilot, Agent Skills, SKILL NINJA]]

本記事は、AIエージェントに専門的な手順を教える**Agent Skills**の枠組みを利用し、**GitHub Copilot**上で編集可能な**draw.io**形式の図面を自動生成するツール「drawio-diagram-forge」を紹介している。以前の「AG-Diagram Maker」をアップグレードし、**SKILL NINJA**拡張機能を通じてワンクリックで導入可能にした点が大きな進化だ。

最大の特徴は、**Mermaid**のようなコードベースの図とは異なり、GUIで直接微調整できる**.drawio**ファイルを出力する点にある。技術的には、**mxCell**のXML構造を定義したリファレンスや、**VS Code**での表示互換性を確保するための**azure2**形式アイコンの採用など、実用的なノウハウが詰め込まれている。内部では**flow-orchestrator**を含む3つのエージェントが連携し、入力分析から図面生成、自己検証までを行うワークフローが組まれている。

クラウド構成図やスイムレーン図を頻繁に作成するアーキテクトやエンジニアにとって、AIに「叩き台」を作らせてGUIで仕上げるフローは、作図工数を劇的に削減する手段となる。ドキュメント作成の自動化に関心がある開発者は必読だ。