# 工程3（設計）のバッチ

設計書（[../../design.md](../../design.md)）の第1版はメインが書いた。ここでは、目次（catalog）を担当に分けて作る。規則は [../../catalog/README.md](../../catalog/README.md)、語彙は `schema/site.yml`。

- 担当は報告をファイルに書いてから終える。止まったときは、報告のない担当だけを同じ割り当てで流し直す
- 担当が書くのは割り当てたファイルと自分の報告だけ。共有のファイル（registry・features・設計書）への変更は、報告に「提案」として書く

## 1段目：一覧と検査の道具（並列）

| 担当 | 書くもの | 報告 | 状態 |
| --- | --- | --- | --- |
| C0 | `planning/catalog/registry.yaml`（全候補の id・分野・題名・優先度・レベルの見当・出どころ、台帳の項目の id） | `registry-C0.md` | 実行中 |
| T1 | `tools/check_catalog.py` と `tests/tools/test_check_catalog.py` | `tool-T1.md` | 実行中 |

## 2段目：分野ごとの目次（一覧ができてから、並列）

一覧（registry.yaml）を見てから、分野のまとまりを決めて割り当てる。
