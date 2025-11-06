## OpenAIやマイクロソフト、メタ、シスコ、AMDらがイーサネットをAI向けに広帯域かつ低遅延にする「Ethernet for Scale-Up Networking 」（ESUN）プロジェクト開始

https://www.publickey1.jp/blog/25/openaiamdaiethernet_for_scale-up_networking_esun.html

OpenAIやマイクロソフト、メタ、AMDなどの主要企業が、AI処理の高速化と効率化のため、広帯域かつ低遅延なイーサネットのオープン標準を確立する「Ethernet for Scale-Up Networking (ESUN)」プロジェクトを開始しました。

**Content Type**: News & Announcements
**Language**: ja

**Scores**: Signal:5/5 | Depth:3/5 | Unique:4/5 | Practical:3/5 | Anti-Hype:4/5
**Main Journal**: 80/100 | **Annex Potential**: 78/100 | **Overall**: 76/100

**Topics**: [[AIネットワーク, データセンターインフラ, イーサネット標準, 高性能計算, オープンハードウェア]]

生成AIの急速な普及と成長に伴い、データセンターではAIの学習や推論処理を高速かつ効率的に行うための、より広帯域で低遅延な高密度ネットワークの需要が高まっています。しかし、Compute Express Link (CXL) やNVIDIA NVLinkといった既存のソリューションは、多くのベンダーが求めるオープンで相互運用可能なニーズには最適化されていないとされています。

このような背景から、Open Compute Project (OCP) は、AI向けネットワークの課題を解決するため「Ethernet for Scale-Up Networking (ESUN)」プロジェクトの開始を発表しました。このプロジェクトの設立メンバーには、AMD、Arista、ARM、Broadcom、Cisco、HPE Networking、Marvell、Meta、マイクロソフト、NVIDIA、OpenAI、Oracleといった業界を牽引する企業が名を連ねています。

ESUNプロジェクトは、AI向けのアクセラレータプロセッサ（XPU）で高性能クラスタを構築するために、イーサネットをベースとした、より広帯域かつ低遅延なオープンスタンダードソリューションの実現を目指しています。Aristaのブログによれば、このプロジェクトではまず以下の技術アプローチに焦点を当てています。

*   **L2/L3フレーミング**: 広帯域・低遅延が求められるAIワークロードのために、AIヘッダをイーサネット上でカプセル化します。
*   **エラーリカバリ**: パフォーマンスを損なうことなく、ビットエラーの検出と修正を行います。
*   **効率的なヘッダー**: ヘッダーの最適化により、回線効率を改善します。
*   **ロスレストランスポート**: 既存の標準化された仕組みを活用し、一部のAIワークロードに不可欠なネットワーク輻輳による性能低下を防ぎます。

筆者は、この取り組みが、AI時代のデータセンターネットワークにおいて、特定のベンダーに依存しないオープンな標準化が重要であるという認識を業界全体で共有し、具体的な技術開発へと進んでいることを示していると強調しています。これにより、将来のAIインフラ構築において、より柔軟で高性能な選択肢が提供されることが期待されます。