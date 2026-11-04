# build-WS 報告

## 直した所
| ファイル：行 | 前 | 後 |
| --- | --- | --- |
| checklists/common.md:51 | 全観点の指摘が解決したら、検証役が reviewed にし verified・verified_with を書く | 指摘0件のときだけ reviewed。直したら draft のまま。stage だけ変え verified は書かない |
| checklists/common.md:52 | verified は事実・出典・鮮度の検証役が読み直した日 | 出典を読み直した担当か tools/freshness.py が書く。事実の検証の担当は置かない |
| checklists/common.md:53 | verified_with は確かめた版 | verified と一緒に書く、と補足 |
| checklists/clarity.md:8 | 事実の正しさは事実・出典・鮮度の検証役が見る | この検証では確かめない（担当は置かない） |
| checklists/fact.md:37 | verified_with の版を検証役が決める | 出典を読み直した担当が書くときに決める |
| design.md:672 | reviewed は「指摘0件か、直しの差分を確かめ直した」 | 指摘0件のときだけ。直したら draft のまま |
| design.md:676 | 執筆と事実の検証は上位のモデル | 執筆と分かりやすさの検証 |

## 直さなかった所
- guides/common.md の 37・41・208・348〜350、design.md の 216・218・614・800、feature.md・card.md・design の強制力の語彙（4値）は、すでに決めに合っている。
- 強制力の2値前提の文は見つからなかった（「お願いと鍵」は用語の見出しとしての使用）。

## メインに判断してほしいこと
1. checklists/fact.md 全体と guides/README.md の 15 行・checklists/common.md の観点の表、design.md:665（検証（事実・出典・鮮度））は、置かないと決めた事実の検証の観点そのまま残っている。廃止か、出典を読み直す担当用の手順への改名かは決めがないので触れていない。
2. checklists/common.md:47「直しの後は…差分を確かめ直し」は、決め 2026-11-05 の「直したら draft のまま」と運用がずれる可能性がある。差分確認の手順を残すか決めてほしい。
3. guides/common.md:250・254 と checklists/template.md の「雛形の動作の検証役」（verified.yaml）は、機械の検査にした決め（2026-11-04）との関係が未決。
4. design.md:625 の「別の担当の検証」は更新時の確認の意味で、そのままにした。

## 試験
tests/guides: 下に結果（実行済み、出力末尾は最後の返答で確認）。道具の呼び出し: 約6回。
