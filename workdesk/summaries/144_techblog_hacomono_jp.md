## コードでみる Crossplane と kro

https://techblog.hacomono.jp/entry/2025/12/11/000000

hacomonoのエンジニアが、Kubernetes上で独自リソースを抽象化・管理するための主要OSSであるCrossplaneとkroを、コードレベルで詳細に比較し、それぞれの責務、柔軟性、複雑性からくる特性と適切なユースケースを解説します。

**Content Type**: ⚙️ Tools
**Language**: ja

**Scores**: Signal:4/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:5/5
**Main Journal**: 82/100 | **Annex Potential**: 83/100 | **Overall**: 84/100

**Topics**: [[Kubernetes, Platform Engineering, Crossplane, kro, カスタムリソース]]

hacomonoの基盤本部プラットフォームチームに所属する著者が、Kubernetes環境における独自リソースの管理を可能にする二つのOSS、Crossplaneとkroについて、具体的なコードを交えながらその詳細な挙動と違いを解説しています。両者ともにKubernetesの抽象化を通じて独自リソースを管理する共通の目的を持ちますが、その内部的なメカニズムと責務の範囲には大きな違いがあります。

Crossplaneは、CNCFのGraduated stageに昇格したKubernetesエコシステムで、Kubernetesリソースに加えてAWSやGCPといった外部クラウドリソースまでもKubernetesの抽象化されたインターフェース（Composite Resource: XR）で管理できます。XRの定義にはXRD（CompositeResourceDefinition）を使用し、リソース構成の解決にはFunctionと呼ばれるgRPCサーバーとのやり取りをCompositionを通じて行います。さらに、Providerと呼ばれるカスタムリソースを用いて外部リソースの管理も完結できる点が特徴です。このため、非常に柔軟性が高い一方で、約20種類のカスタムリソースと9万行を超えるGoコードに示されるように、責務が大きく複雑性も高まります。

一方、kro（Kube Resource Operator）はkubernetes-sigsで管理されており、CrossplaneのXRと同様に独自リソースを定義してKubernetesリソースを管理します。RGD（ResourceGraphDefinition）でスキーマ定義とリソース生成方法をCEL（Common Expression Language）で直接定義する点が特徴です。Crossplaneと比較してはるかにシンプルで、カスタムリソースはRGDのみ、Goコードも約3万行と少ないです。kroはリソース構成の解決とApplyに責務を限定しており、PodIdentityのようなKubernetes外の外部リソース管理には関与しません。そのため、外部リソースを管理する場合はACK（AWS Controllers for Kubernetes）やCrossplane Providerといった別途のコントローラーを導入する必要があります。

著者は、両者の違いを「責務」「柔軟性」「複雑性」の三点から深く掘り下げています。Crossplaneが外部リソース管理まで一元的に行える柔軟性を持つ一方で、その複雑性が運用・トラブルシューティングの課題となり得ることを指摘。kroはシンプルで学習コストが低いものの、CELによる柔軟性の限界や外部リソース管理の別途導入が必要となる点を挙げています。

最終的に、著者はユースケースに応じた使い分けを推奨しています。Kubernetesリソースのみを対象とする場合はkroのシンプルさが有利であり、外部リソースを含む場合やマルチクラウド環境ではCrossplaneの単一インターフェースでの管理が有効です。さらに、kroで構成リソースを解決し、Crossplane Providerで外部リソースを管理するハイブリッドな利用方法も提案しています。この記事は、プラットフォームエンジニアリングにおいて、開発者に提供する抽象化レイヤーの設計とツール選定に際して、具体的な技術的根拠と実践的な指針を与える点で非常に重要です。