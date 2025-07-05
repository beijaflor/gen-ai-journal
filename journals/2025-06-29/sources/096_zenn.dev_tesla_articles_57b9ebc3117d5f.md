## [API GatewayのカスタムドメインをRoute53とCloudFrontで設定する](https://zenn.dev/tesla/articles/57b9ebc3117d5f)

**API Gatewayカスタムドメイン設定：Route53とCloudFront連携**

この記事では、API Gatewayにカスタムドメインを設定する手順を解説。Route53でドメインを取得し、CloudFrontを経由してAPI Gatewayに接続。ACMで証明書を発行し、CloudFrontに設定。Route53でCloudFrontへのエイリアスを設定し、カスタムドメインでAPIにアクセス可能にする。
