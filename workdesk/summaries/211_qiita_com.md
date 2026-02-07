## 【Qiita最速？】OpenClaw(旧Clawdbot) + Discordで自分専用AIアシスタントを構築する【Proxmox/Ubuntu】

https://qiita.com/yu_720/items/4b3bc75731f109927ebd

構築する：サーバー上に**OpenClaw**（旧**Clawdbot**）をデプロイし、Discord経由で自己設定やスキル拡張が可能なAIアシスタントを運用可能にする。

**Content Type**: 📖 Tutorial & Guide
**Language**: ja

**Scores**: Signal:4/5 | Depth:3/5 | Unique:4/5 | Practical:5/5 | Anti-Hype:4/5
**Main Journal**: 83/100 | **Annex Potential**: 81/100 | **Overall**: 80/100

**Topics**: [[OpenClaw, AI Agent, Discord Bot, Self-Configuration, Infrastructure]]

本記事は、自分専用のAIアシスタントをサーバー（**Proxmox/Ubuntu**）上に構築できるオープンソースプロジェクト「**OpenClaw**（旧**Clawdbot**）」の導入から**Discord**連携までの手順を網羅した実践ガイドです。**OpenClaw**の特筆すべき点は、チャット経由で指示を出すだけでBot自身が自身の構成ファイルを編集・反映する**自己設定能力**にあり、従来のSSHを通じた手動のコンフィグ管理を不要にします。

セットアップには**Node.js 22**以上と**Homebrew**が必要で、**Anthropic API**や**Brave Search API**などの外部ツールと組み合わせることで、Web検索やカレンダー操作、リマインダー管理などの多岐にわたるタスクを自動化できます。記事では**Discord Developer Portal**でのBot作成手順や**Privileged Gateway Intents**の設定、さらにトラブルシューティング用の**clawdbot doctor**コマンドについても具体的に触れられています。

**ClawdHub**を通じたエコシステムにより、必要な機能をAIが自ら提案・インストールする体験は、エージェント構築のハードルを大きく下げます。プライベートな環境でセキュアに、かつ拡張性の高い自分専用のコーディング・生活支援エージェントを運用したいエンジニアにとって、決定版とも言える導入資料です。