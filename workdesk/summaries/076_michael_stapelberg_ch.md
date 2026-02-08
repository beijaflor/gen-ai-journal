## NixOSとmicrovm.nixを用いたコーディングエージェント用VMの構築

https://michael.stapelberg.ch/posts/2026-02-01-coding-agent-microvm-nix/

**Original Title**: Coding Agent VMs on NixOS with microvm.nix

信頼できないコマンドを自動実行するAIエージェントの安全な実行環境として、NixOS上でリソースを分離した使い捨て可能なMicroVMを構築する手法を解説する。

**Content Type**: ⚙️ Tools
**Language**: en

**Scores**: Signal:5/5 | Depth:4/5 | Unique:4/5 | Practical:4/5 | Anti-Hype:4/5
**Main Journal**: 82/100 | **Annex Potential**: 80/100 | **Overall**: 84/100

**Topics**: [[NixOS, microvm.nix, AI Agents, Sandboxing, Claude Code]]

**NixOS**の強力な再現性を活かし、コーディングエージェント専用の軽量かつ使い捨て可能な実行環境を**microvm.nix**で構築する実戦的なガイド。AIエージェントが生成する信頼できないコードやコマンド実行からホスト環境を保護するため、プライベートデータへのアクセスを遮断した**MicroVM**のセットアップ手順を詳説している。

具体的には、**systemd-networkd**を用いたブリッジ接続設定、**virtiofs**によるホストの**Nix store**や特定ワークスペースの効率的な共有、そしてエージェントに権限確認をスキップさせる`--dangerously-skip-permissions`フラグを安全に運用するための構成例を紹介している。特筆すべきは、**Claude Code**の「Skills」機能を活用し、プロンプト一つで新しいプロジェクト用のVM構成定義からリポジトリのクローンまでをAI自身に自動完結させるメタな自動化手法だ。

AIエージェントの利便性を享受しつつ、セキュリティと環境のクリーンさを両立したいエンジニアにとって、インフラのコード化（IaC）による究極のサンドボックス環境として非常に参考になる。