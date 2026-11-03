# 工程4（設計の見直し）のバッチ

設計書（[../../design.md](../../design.md)）と目次（[../../catalog/](../../catalog/)）を、作った担当とは別の担当が批判的に読む。共通の指示は [brief-review.md](brief-review.md)。

- design §10.1 は見直しの観点を3つ（読者の立場・要件と決定の照合・目次の質）としていたが、技術と進め方（§8〜§11）を見る担当を足して4つにした。設計書の後半は、まだ誰も批判的に読んでいないため
- 担当は報告をファイルに書いてから終える。止まったときは、報告のない担当だけを同じ割り当てで流し直す
- 指摘への対応は、メインが [../../design-review.md](../../design-review.md) に決める

| 担当 | 観点 | 報告 | 状態 |
| --- | --- | --- | --- |
| R1 | 読者の立場（課題から目的のページに着けるか、欠け） | `review-R1.md` | 完了（18件：重大1・中11・軽6。読者の課題34件） |
| R2 | 要件と決定との照合 | `review-R2.md` | 完了（33件：重大3・中13・軽17。読むだけの git status を1回使ったと報告） |
| R3 | 目次の質（粒度・境界・レベル・優先度と第一波・前提・文・症状辞典・台帳） | `review-R3.md` | 完了（25件：重大2・中11・軽12） |
| R4 | 技術と進め方（§8〜§11） | `review-R4.md` | 完了（37件：重大3・中21・軽13） |

## 2段目：指摘への対応の反映（見直しの後、並列）

メインが指摘への対応を [../../design-review.md](../../design-review.md) に決めた（DR-01〜DR-19）。設計書は D1 が第2版にし、検査の道具は T3 が `routes` に合わせ、目次は分野ごとの担当（F1〜F7）が直す。分野ごとに持ち主を1人に決め、同じファイルを2人が書かないようにした。共通の指示は [brief-fix.md](brief-fix.md)。重なった別名の主のページは [fix-aliases.md](fix-aliases.md)。メインは先に、id を3つ改めた（DR-19 n）。

| 担当 | 受け持ち | 主な行（DR-19） | 報告 | 状態 |
| --- | --- | --- | --- | --- |
| D1 | `planning/design.md`（第2版） | DR-01〜DR-18 の設計書の部分 | `fix-D1.md` | 完了 |
| T3 | `tools/check_catalog.py`・試験・catalog/README §3・§4・§6 | DR-02（routes の検査と第一波の内訳） | `fix-T3.md` | 完了 |
| F1 | start・changes・basics・judgment | a・b（changes の一般的な sign）・d・e・k（judgment 側）・p（lost-in-the-middle）・DR-17（how-to-use・ai-and-sources の notes） | `fix-F1.md` | 完了 |
| F2 | surfaces・models・cost・api・app | a・d・e・g・i・j（suspected-degradation）・o（thinking-keywords）・v（what-uses-up-limits） | `fix-F2.md` | 完了 |
| F3 | prompting・japanese・context | a・d・e・h（R1-18）・q（does-double-check-work）・u・v（inspect-context）・w | `fix-F3.md` | 完了 |
| F4 | cli・extend・contest | a・d・e・h（R1-17）・l・m（recover-lost-work）・q（completion-notifications）・r・w（settings-layers） | `fix-F4.md` | 完了 |
| F5 | verify・eval・enforce | a・d・e・h（R1-13 の hook-recipes・R1-14 の sandboxing・R1-15）・k（own-generated-code） | `fix-F5.md` | 完了 |
| F6 | safety・delegate・team | a・d・e（付表B）・f・h（R1-14・R1-16）・m（protecting-secrets・when-requests-are-refused）・o（cloud-schedules・enterprise-vs-team-plans）・p（ai-amplifies-organizations）・q（curb-sycophancy-and-overtrust）・s | `fix-F6.md` | 完了 |
| F7 | symptoms・recipes | x（routes。T3 の後に始める）・b・c・d・e・h（R1-13）・i（unexpected-memories）・j・m・q（add-tests）・t | `fix-F7.md` | 完了 |

## 3段目：反映を確かめる（2段目の後）

共通の指示は [brief-verify.md](brief-verify.md)。書いた担当とは別の担当が、決定どおりかを確かめる（design §10.2「メインが書いた直しも、別の担当が確かめる」）。

| 担当 | 見るもの | 報告 | 状態 |
| --- | --- | --- | --- |
| V1 | 設計書の第2版（design.md）と catalog/README・schema/site.yml を、design-review の DR-01〜DR-20 と §6 に照らす | `verify-V1.md` | 完了（24件：直す3・直したほうがよい9・軽い12。メインが直した） |
| V2 | 目次（planning/catalog/）の直しを、DR-19 の各行・fix-aliases.md・担当の報告に照らす。検査の道具を流す | `verify-V2.md` | 完了（14件：直す1・直したほうがよい2・軽い11。メインが直した） |
| V3 | メインが最後に行った直し（V2 の指摘への対応）だけ | `verify-V3.md` | 完了（9件：直す0・直したほうがよい3・軽い6。メインが直した） |
