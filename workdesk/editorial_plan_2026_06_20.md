# Editorial Plan - Journal 2026-06-20

## Planning Status
- [x] Initial theme identification (AI-assisted)
- [x] Human review and refinement (round 1: Theme 8 removed, articles moved to annex)
- [x] Theme introductions drafted
- [x] Article-to-theme mapping complete
- [x] APPROVED - Ready for STEP_04 curation

---

## Corpus Overview

- **総ソース数**: 283（うち280件がunified_summaries.mdに集約済み。NYT/WSJ/FTの3件はペイウォール経由でHNスレッドの要約に置換されているため集約から外れているが、サマリーファイル自体は存在し、ID 173/179/258で参照可能）
- **キュレーションフラグ**（Supabase export 2026-06-22）:
  - ⭐ Standout: 196（Anthropic Claude Code Expertise 40万セッション解析）、214（Vercel eve docs）
  - 👍 Upvote: 034（Fable 5でcs-edu site「言語の庭」生成）、053（docswell SDD-in-loop-engineering）、124（Cloud Native ナデラ学習ループ）、170（Artificial Analysis GLM-5-2リーディング）、174（Browser-use Firecracker browser infra）
  - 👎 Downvote: 036（codeheal-scan AI生成コード診断）、209（Ollama×RAG長期記憶ボット）、282（Tailscale SSH Home Mac CC）
- **今週の中核ニュース**:
  - Anthropic「Claude Fable 5/Mythos 5」が米輸出管理指令で6/12にアクセス停止 → SKテレコム経由の中国懸念が真因と判明（WIRED報道）→ Stamosら40名超のサイバー専門家が解除要求公開書簡
  - Vercel Ship 2026で「eve」「Agent Stack」「Vercel Connect」フルセット発表
  - GLM-5.2がオープンウェイトモデルのArtificial Analysis Intelligence Indexで首位
  - Anthropicが40万Claude Codeセッション解析で「ドメイン専門性 > プログラミングスキル」を実証
  - OpenAIの2025年純損失385億ドル財務文書リーク／SpaceXがCursorを600億ドルで買収

---

## Identified Themes

**Reminder: Theme titles should be concrete, specific, and factual**
- ✅ 名指しのアンカー × 単一動詞 × 実体ある対象フレーズ
- ❌ 抽象的なカテゴリ名・em-dash・物語的接続詞は避ける

---

### Theme 1: Claude Fable 5/Mythos 5輸出規制発動・SKテレコム経由の中国懸念・Stamos公開書簡が示すAIモデルの地政学化

**Articles (IDs):** 242, 066, 104, 131

**Theme Introduction (2-3 sentences in Japanese):**
2026年6月12日、Anthropicの最新モデル「Claude Fable 5」と「Mythos 5」が米商務省の輸出管理指令を受けて全世界でアクセス停止となった。当初発表された「ジェイルブレイク脆弱性」という公式理由とは別に、WIREDの追加報道では韓国SKテレコムを介した中国側アクセス遮断が真因であった可能性が示され、David Sacks氏の独自報告やKatie Moussouris氏の防御側からの批判、Alex Stamosら40名超のサイバー専門家による解除要求公開書簡といった反応が同時並行で並んだ。

**Editorial Notes:**
- 242: WIRED報道、米ホワイトハウスがSKテレコムへのアクセス遮断を命令、AmazonリサーチャーのMythos脆弱性発見も背景
- 066: David Sacks氏が「FableがMythosにガードレールをかけたモデル、第三者がジェイルブレイク発見、Anthropicが修正拒否」という内幕を報告
- 104: TechCrunch分析、Katie Moussouris氏の指摘により「ジェイルブレイク」が技術的に脆弱な根拠と判明、政治的報復・恣意的介入の側面
- 131: Luta Security CEOによる正面からの批判、輸出規制は防御側のツールを奪い米国のサイバー防衛を損なう

---

### Theme 2: Vercel "eve"・Agent Stack・Vercel Connectが揃えるエージェント時代のフルスタック基盤

**Articles (IDs):** 214, 160, 161, 266

**Theme Introduction (2-3 sentences in Japanese):**
Vercel Ship 2026にて、AIエージェントを「Next.js相当」の標準フレームワークとして構築・運用するための新スタックが一挙に発表された。Markdownでスキル、TypeScriptでツールを記述するファイル構造の「eve」、モデル接続・耐久ワークフロー・サンドボックスを束ねる「Agent Stack」、短寿命OIDCクレデンシャルで外部サービス接続を担う「Vercel Connect」が同週に並び、Vercelがフロントエンドホスティングから「エージェント時代のフルスタックプラットフォーム」へ自社プロダクトを再定義した形となっている。

**Editorial Notes:**
- 214: Vercel eveの公式ドキュメント、耐久セッション・サブエージェント・サンドボックスを標準装備、Vercel内部100エージェント稼働実績（⭐ standout）
- 160: Vercel Ship 2026 リキャップ、Agent Stack・eve・Vercel Connect・Vercel Services・Vercel Agent・BYOC on AWSをまとめて提示
- 161: Agent Stack詳細、AI Gateway・Workflow SDK・Sandbox・Chat SDKの3層構造でエージェント本番運用の足回りを抽象化
- 266: 日本語実践レポート、Eveのディレクトリベース設計を執筆エージェント構築で検証

---

### Theme 3: GLM-5.2フルオープン・Kimi K2.7 Code・Mac StudioでローカルLLMが商用ラインに到達

**Articles (IDs):** 170, 092, 101

**Theme Introduction (2-3 sentences in Japanese):**
Z.ai（Zhipu AI）のGLM-5.2がArtificial Analysis Intelligence Indexでスコア51を獲得し、オープンウェイトモデルの首位に立った（クローズドモデルのGPT-5.5に匹敵するGDPval-AA v2スコア1524）。同週にMoonshot AIはエージェント特化型「Kimi K2.7 Code」（1兆MoE、推論トークン30%削減）を公開、Vicki Boykis氏はM2 Mac 64GBでGemma 4／GPT-OSSをDockerサンドボックス内で運用する実践レポートを公開し、オープンウェイト＋ローカル実行が「実験」フェーズから「商用ライン」フェーズへ移行した週となった。

**Editorial Notes:**
- 170: Artificial Analysis公式評価、GLM-5.2がオープンウェイト首位、GPT-5.5に匹敵するエージェント能力を実証（👍 upvoted）
- 092: Moonshot AI Kimi K2.7 Codeリリース、1Tパラメータ・MoE 32B active、Kimi Code Bench v2で21.8%スコア向上、256Kコンテキスト
- 101: Vicki Boykis氏「Running local models is good now」、M2 Mac 64GB＋LM Studio＋Pi＋Dockerで日常開発を回す実践検証

---

### Theme 4: Anthropic「Claude Code Expertise」40万セッション解析・Addy Osmani新SDLC・Charity Majors『規律強化』論が示すAIコーディング規律の再定義

**Articles (IDs):** 196, 248, 172

**Theme Introduction (2-3 sentences in Japanese):**
Anthropicが2025年10月〜2026年4月の約40万件のClaude Codeセッションを解析し、「人間が計画の70%を、Claudeが実行の80%を担う」という分業構造と、プログラミングスキルよりドメイン専門性が成果を決めるという実証データを公開した。同時にAddy Osmani氏は「エージェントの能力はモデル10%・ハーネス90%」とする新SDLC論を、Charity Majors氏は「AIによりコード生成は無料化されたが、エンジニアリング規律はむしろ強化されるべき」とする論考を発表し、AIコーディングの規律と職能像が一斉に再定義された週となった。

**Editorial Notes:**
- 196: Anthropic Research、40万Claude Codeセッション分析、人間が計画70%/Claudeが実行80%、ドメイン専門性が成果を決定（⭐ standout）
- 248: Addy Osmani「The New Software Lifecycle」、エージェントの能力はモデル10%・ハーネス90%、Vibe Codingからエージェント工学への移行
- 172: Charity Majors「AI demands more engineering discipline. Not less」、コードを「キャッシュ」と再定義、短いフィードバックループ＋オブザーバビリティの徹底

---

### Theme 5: Bayer Reliable Agentic RAG・LayerX prompt-log driven・5万スターClaude Code Tipsが体系化するハーネス工学の実践

**Articles (IDs):** 147, 053, 244

**Theme Introduction (2-3 sentences in Japanese):**
Bayer AGとThoughtworksが構築した製薬データプラットフォーム「PRINCE」のマルチエージェントRAG事例（LangGraphベース、Process-reflectとData-reflectの分離、RAGAS／Langfuseによる継続監視）と、LayerX社のプロンプト履歴を意味的にグルーピングしSkill化を自動提案する「prompt-log driven AI workflow」、そしてdocswellで公開された「SDD in loop engineering」（仕様駆動開発をループの中核資産として再定義）が並び、ハーネス工学が個別ハックから組織運用の標準パターンへ昇格しつつある現在地が見えてきた。

**Editorial Notes:**
- 147: Bayer × Thoughtworksの本番品質Agentic AI、LangGraphによるエージェント分業、Process-reflect/Data-reflect、コンテキスト管理＋リトライ＋永続化のハーネス設計
- 053: 仕様駆動開発（SDD）をループエンジニアリングの中核資産として再定義、コンテキストエンジニアリングと実行履歴からの選別（👍 upvoted）
- 244: LayerX、全プロンプトをローカルJSONLに記録、LLM分析で3回以上の反復パターンを自動検出しSkill化通知、PR/CI修正の7割を仕組み化

---

### Theme 6: SoftBank "Patching as a Service" 1万500件発見・JetBrainsプラグイン窃取・Cloudflare脆弱性ハーネスが形作るAIサイバー攻防

**Articles (IDs):** 192, 229, 143

**Theme Introduction (2-3 sentences in Japanese):**
ソフトバンクとOpenAIの合弁SB OAI JapanがGPT-5.5 Cyberを用いた「Patching as a Service」を発表し、自社診断で1万500件の未知脆弱性を発見したと公表。Cloudflareは脆弱性発見ハーネス（VDH）と検証システム（VVS）のアーキテクチャを公開し、2万件以上の候補から7,000件以上の有効修正案を導出した実績を共有した。一方Aikido Securityは、JetBrains Marketplaceで7万回インストールされた15個以上のAI関連プラグインが、ユーザーのOpenAI/DeepSeek APIキーを攻撃者サーバーへ送信していることを報告しており、AI時代のセキュリティが防御側のハーネス整備と攻撃側のサプライチェーン狙いの両面で具体化している。

**Editorial Notes:**
- 192: 孫正義氏「黒船来航以来の危機」、SoftBank×OpenAI合弁、GPT-5.5 Cyberで自社1万500件発見、日本重要インフラ向け優先提供
- 229: Cloudflare「Build your own vulnerability harness」、VDH+VVSの2系統構成、エージェントを入れ替え可能コンポーネントとして扱い相互検証で誤検知削減
- 143: Aikido Security調査、JetBrains Marketplaceで15+プラグイン70,000インストール、APIキー窃取＋盗難キーを別ユーザーへ「再販」する収益化構造

---

### Theme 7: OpenAI 385億ドル純損失リーク・SpaceX 600億ドルでCursor買収・DOJのxAI擁護が映すAI事業の資本市場現実

**Articles (IDs):** 180, 103, 169

**Theme Introduction (2-3 sentences in Japanese):**
OpenAIの2025年監査済み財務文書がリークされ、売上130.7億ドルに対し純損失385.3億ドル（うち実質営業損失約80億ドル）、Microsoft支払い172億ドルというコスト構造が明らかになった。同週SpaceXはIPO直後にAIコーディングのCursor（旧Anysphere）を600億ドルの株式交換で買収する合意を発表、米司法省（DOJ）はxAIメンフィスのデータセンターで稼働する57基の無許可ガスタービンが「国家・経済・エネルギー安全保障」上不可欠であるとして環境訴訟に反論しており、AI事業の収益性疑義と国家インフラ化が同時に資本市場の文脈で表面化した週である。

**Editorial Notes:**
- 180: OpenAI財務リーク（Ars Technica版）、売上130.7億ドル／R&D 191.8億ドル／Microsoftへ105.9億ドル、Soraプロジェクト縮小と中核業務集中、2030年黒字化目標
- 103: SpaceXがCursorを600億ドル株式交換で買収、xAI統合とAIインフラ・エンタープライズで28兆ドルTAM主張、IPOで時価総額1兆ドル増加
- 169: DOJ準備書面、xAI 57基無許可ガスタービンがGrok運用＋Project Maven軍事支援に不可欠と主張、NAACPの公衆衛生提訴に対抗

---

## Highlight Draft ("今週のハイライト")

**今週の主な話題:**

今週のAI業界は「Claude Fable 5/Mythos 5の急停止」という地政学的事件を中心に動いた。6月12日に米商務省の輸出管理指令でAnthropicの最新モデルが全世界でアクセス停止となり、当初は「Amazonリサーチャーが見つけたジェイルブレイク」が理由とされていたが、WIREDの追加報道では韓国SKテレコムを介した中国側アクセス遮断が真因であったことが明らかになった。David Sacks氏は「FableはMythosにガードレールをかけたモデルで、Anthropicが第三者発見の脆弱性修正を拒否した」と詳述し、Luta SecurityのKatie Moussouris氏は「指摘されたバイパスは『コードのレビュー』と『コードの修正』の差異に過ぎず、輸出規制を適用すべきものではない」と批判、Alex Stamos氏ら40名超のサイバー専門家が解除要求公開書簡を提出した。AIモデルが「ソフトウェア」から「兵器に準ずる輸出管理対象」へ変質する歴史的転換点が示された。

設計と運用の側面では、Vercel Ship 2026で「eve」（Markdown＋TypeScriptのエージェントフレームワーク）、Agent Stack、Vercel Connect（短寿命OIDCクレデンシャル）がフルセットで発表された。Vercelはフロントエンドホスティング会社からエージェント時代のフルスタックプラットフォームへ自社を再定義しており、Vercel内部だけで100以上のエージェントがeve上で稼働している実績も併せて公開された。同時にAnthropicは約40万件のClaude Codeセッションを解析し「人間が計画の70%、Claudeが実行の80%を担い、ドメイン専門性が成果を決定する」という実証データを公開、Addy Osmani氏は「エージェント能力はモデル10%・ハーネス90%」とする新SDLC論を、Charity Majors氏は「AIによってコード生成が無料化された今こそエンジニアリング規律は強化されるべき」とする論考を発表した。BayerのProduction品質Agentic RAGとLayerXのprompt-log driven自動化、5万スターのClaude Code Tipsまで含めると、ハーネス工学が個別ハックから組織標準へ昇格する転換点が今週同時並行で表面化している。

オープンウェイトモデル側では、Z.ai（Zhipu AI）のGLM-5.2がArtificial Analysis Intelligence Indexで首位を獲得（GPT-5.5に匹敵するGDPval-AA v2スコア1524）、Moonshot AIはエージェント特化型Kimi K2.7 Code（1T MoE、256Kコンテキスト、推論トークン30%削減）を公開した。Vicki Boykis氏はM2 Mac 64GBでGemma 4／GPT-OSSをDockerサンドボックス内で日常開発に投入できると報告しており、ローカルLLMが「実験」から「商用ライン」フェーズへ移行している。Anthropicの輸出規制と並列で、欧米の特定モデルへの依存リスクが地政学的に顕在化したことで、オープンウェイトとローカル実行への「保険」需要が一気に表面化した週でもある。

資本市場とセキュリティの側面でも具体的な数字が動いた。OpenAIの2025年財務文書リークは売上130.7億ドル・純損失385.3億ドル（実質営業損失約80億ドル）・Microsoft支払い172億ドルというコスト構造を露わにし、SpaceXはIPO直後にCursorを600億ドル株式交換で買収。米司法省はxAIメンフィスの無許可ガスタービン57基を「国家・経済・エネルギー安全保障」案件として擁護し、AI事業の収益性疑義と国家インフラ化が資本市場の文脈で同時表面化した。ソフトバンク×OpenAIの「Patching as a Service」は孫正義氏が「黒船来航以来の危機」と表現する規模（自社1万500件発見）、CloudflareのVulnerability Harness、JetBrainsプラグインの APIキー窃取と、AIサイバー攻防が防御側のハーネス整備と攻撃側のサプライチェーン狙いの両面で具体化している。

**Key Points to Cover:**
1. Claude Fable 5/Mythos 5の輸出規制発動・SKテレコム経由の中国懸念・Stamos公開書簡（AIモデルの地政学化）
2. Vercel "eve"・Agent Stack・Connectが揃えるエージェント時代のフルスタック基盤
3. GLM-5.2フルオープン・Kimi K2.7 Code・Mac StudioでローカルLLM商用ライン到達
4. Anthropic 40万セッション解析・Addy Osmani新SDLC・Charity Majors規律論によるAIコーディング規律の再定義
5. Bayer Agentic RAG・LayerX prompt-log・5万スターCC Tipsが体系化するハーネス工学
6. SoftBank PaaS 1万500件・JetBrainsプラグイン窃取・Cloudflare脆弱性ハーネスが形作るAIサイバー攻防
7. OpenAI 385億ドル損失リーク・SpaceX 600億ドルCursor買収・DOJのxAI擁護が映す資本市場現実

---

## Curation Signal Summary

**⭐ Standout Articles Used:**
- 196 → Theme 4（Anthropic Claude Code Expertise 40万セッション解析、Leadとして配置）
- 214 → Theme 2（Vercel eve docs/site、Leadとして配置）

**👍 Upvoted Articles Used:**
- 053 → Theme 5（docswell SDD-in-loop-engineering、ハーネス工学の中核資産論）
- 170 → Theme 3（Artificial Analysis GLM-5.2リーディング評価、Leadとして配置）

**👍 Upvoted Articles Held for Annex:**
- 034（Fable 5でcs-edu site「言語の庭」生成）→ annex候補（Fable 5実用デモとして annex Group A の主力候補）
- 124（Cloud Native ナデラ学習ループ）→ annex候補（学習ループ／SaaSガバナンス論として annex で扱う、T4「規律」とは焦点が異なる）
- 174（Browser-use Firecracker browser infra）→ annex候補（具体技術解説として annex Group B のインフラ深掘り候補）

**Societal Reception Articles (formerly Theme 8, moved to Annex per round 1 review):**
- 176（Pew Research AI肯定派16%）→ annex候補（AI受容の社会的壁を示す authoritative data）
- 255（Nature脱技能化研究）→ annex候補（医師アデノーマ発見率28.4%→22.4%／Anthropic RCT、デスキリング論考の主軸）
- 253（Matthew Hughes「Herbalife」アナロジー）→ annex候補（Replit/Cursor略奪的マーケティング批判）

**👎 Downvoted Articles:**
- 036（codeheal-scan AI生成コード診断）→ annex候補（T6 セキュリティ補助記事として検討、ただし👎により主力には据えない）
- 209（Ollama×RAG長期記憶ボット）→ annex候補（T3 ローカルLLM補助として検討、ただし👎により主力には据えない）
- 282（Tailscale SSH Home Mac CC）→ annex候補（個人開発Tips、👎により主力からは除外）

**Omitted Articles:** Supabase上のomitフラグはゼロ（export_curation_flags.pyの「No summaries flagged for omission」報告に従う）

---

## Theme Coverage Summary

**Target Distribution:**
- Main Journal: 23 articles across 7 themes
- Annex Journal: 残り257記事（283 - 23 - 3パイウォール代替）から、Fable 5実用検証・ローカルLLM実機事例・社会受容の論考（旧T8）・国内コミュニティ記事・MCP/A2Aプロトコル深掘り・批評論考を中心にcurate

**Article Count by Theme (Planned):**
- Theme 1（Fable 5/Mythos 5輸出規制・地政学化）: 4 articles
- Theme 2（Vercel eve/Agent Stack/Connect）: 4 articles
- Theme 3（GLM-5.2・Kimi K2.7・ローカルLLM商用ライン）: 3 articles
- Theme 4（Anthropic 40万解析・Addy・Charity Majorsの規律再定義）: 3 articles
- Theme 5（Bayer・LayerX・5万スターCCのハーネス体系化）: 3 articles
- Theme 6（SoftBank PaaS・JetBrains・CloudflareのAIサイバー攻防）: 3 articles
- Theme 7（OpenAI財務・SpaceX買収・DOJ xAI擁護の資本市場現実）: 3 articles

*Note: 全テーマが3記事以上を確保。Theme 1とTheme 2は今週の中核ニュースであるため4記事構成。単一記事テーマは設定していない。*

**Total Planned for Main:** 23 articles
**Remaining for Annex:** 約257 articles（うち主要annex候補は👍 034/124/174、👎 036/209/282、および旧T8の176/255/253を含むカテゴリー別）

---

## Review Notes (Human Editor)

**Date Reviewed:** 2026-06-22 (round 1)
**Reviewer:** beijaflor

**Round 1 Changes:**
- 削除：旧Theme 8「Pew 16%肯定・Nature脱技能化・Herbalifeアナロジー」
  - 理由：AI受容と社会的負荷の論考は今週の中核ニュース性より evergreen 寄りで、annex 側でカタログ形式の方が読者の判断に資する
  - 影響：176（Pew Research）、255（Nature脱技能化）、253（Herbalife）の3記事を annex 候補へ移動
  - メイン記事数：26 → 23、テーマ数：8 → 7

**Approval:** ✅ APPROVED / ❌ NEEDS REVISION

---

## Implementation Checklist

After approval:
- [ ] Proceed to STEP_04 (Curate Main Journal)
- [ ] Use this plan as blueprint for article selection
- [ ] Organize curated_journal_sources.md by themes
- [ ] Carry forward theme introductions to STEP_08 (Assembly)
