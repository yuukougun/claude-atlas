# 工程3（設計）のバッチ

設計書（[../../design.md](../../design.md)）の第1版はメインが書いた。ここでは、目次（catalog）を担当に分けて作る。規則は [../../catalog/README.md](../../catalog/README.md)、語彙は `schema/site.yml`。

- 担当は報告をファイルに書いてから終える。止まったときは、報告のない担当だけを同じ割り当てで流し直す
- 担当が書くのは割り当てたファイルと自分の報告だけ。共有のファイル（registry・features・設計書）への変更は、報告に「提案」として書く

## 1段目：一覧と検査の道具（並列）

| 担当 | 書くもの | 報告 | 状態 |
| --- | --- | --- | --- |
| C0 | `planning/catalog/registry.yaml`（全候補の id・分野・題名・優先度・レベルの見当・出どころ、台帳の項目の id） | `registry-C0.md` | 完了（候補378：必須164・推奨161・任意53。台帳35。核の候補47） |
| T1 | `tools/check_catalog.py` と `tests/tools/test_check_catalog.py` | `tool-T1.md` | 完了（検査31：エラー10・警告21。試験114が通る） |

## 2段目：分野ごとの目次（一覧ができてから、並列）

共通の指示は [brief-catalog.md](brief-catalog.md)。1つの担当が22〜39ページほどになるよう分けた。symptoms はほかのすべての分野へ振り分けるので、1つの担当にした。

| 担当 | 分野（registry の候補数） | 報告 | 状態 |
| --- | --- | --- | --- |
| C1 | start（8）・changes（5）・basics（20） | `catalog-C1.md` | 実行中 |
| C2 | surfaces（11）・models（14）・cost（12） | `catalog-C2.md` | 実行中 |
| C3 | prompting（24）・japanese（12） | `catalog-C3.md` | 実行中 |
| C4 | context（19）・cli（19） | `catalog-C4.md` | 実行中 |
| C5 | app（22）・api（14） | `catalog-C5.md` | 実行中 |
| C6 | extend（26） | `catalog-C6.md` | 実行中 |
| C7 | enforce（15）・safety（17） | `catalog-C7.md` | 実行中 |
| C8 | verify（17）・eval（13） | `catalog-C8.md` | 実行中 |
| C9 | delegate（23）・team（16） | `catalog-C9.md` | 実行中 |
| C10 | judgment（11）・contest（12） | `catalog-C10.md` | 実行中 |
| C11 | recipes（22） | `catalog-C11.md` | 実行中 |
| C12 | symptoms（26） | `catalog-C12.md` | 実行中 |
