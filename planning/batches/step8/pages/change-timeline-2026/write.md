# write.md：change-timeline-2026（執筆）

## 書いたファイル
- docs/changes/change-timeline-2026.md（stubs から mv。stage を draft、updated を 2026-11-05、sections に `how-to-read`「年表の読み方」を足した。ほかのキーは変更なし）
- 雛形・図・出典ファイルはなし（templates の案なし。sources は空のまま）

## 必ず持つものの対応
- データから作る表：`#timeline`（`gen:begin timeline` の目印。中身は道具が書く）
- 要点 → 生成の表 → 読み方：要点（冒頭の囲み）→ `#trends`（流れの説明）→ `#timeline`（生成の表）→ `#how-to-read`（読み方）。目次の sections に従い、流れを表の前に置いた
- level：持たない（front matter にもなし）

## メインに判断してほしいこと
- 流れの説明（`#trends`）に日付・版・数・モデル名を書かず、台帳の行への link で時期を示した（変わりやすい値を手で書かない規則のため）。足りなければ指示がほしい
- 目次 visual の「四つの列の年表」は図にしていない。`timeline` の生成物の形に依存するため
- 「2027 年の変更は次の年のページ」という約束に当たる文は書いていない（公開の約束の扱い）

## 提案
- front matter：related に `default-safety-settings` を足す案（本文で `default-safety-settings#by-stage` を指したため）

```yaml
frontmatter:
  - {id: change-timeline-2026, key: related, before: [outdated-advice-ledger, term-index, checking-for-updates, dating-information], after: [outdated-advice-ledger, term-index, checking-for-updates, dating-information, default-safety-settings], reason: "自律の既定化の流れで守りの正本を指したため"}
```
- 用語集・prh：「skills」は prh で「スキル」に直される（本文は「スキル」に直した）。「auto mode」「effort」の扱いは用語集のとおり

## 検査の結果
- `check_page.py` 2 回：1 回目 エラー 1（prh：skills → スキル）、直した後 エラー 0・警告 0

## 確かめていないこと
- `timeline` の目印が実際に出す表の中身と、`#trends` の主張（統合・自律の既定化・effort）との食い違い（表は道具が生成するため、中身を見ていない）
- 束の抜き出しが切れている所（00 §1 の表の後半、01 4-1 の後半）は読んでいない。流れの主張は読めた範囲と台帳の行の題名に基づく
- 台帳の行 id への link（`outdated-advice-ledger#<行の id>`）は検査を通ったが、相手ページの本文との整合は見ていない
- ultrathink の「効く範囲が段階的に広がった」は束の 23 §3.5 に基づく。一次資料は開いていない

## 使用量
- 道具の呼び出し：約 9 回（Read 3、Bash 4、Write 2、Edit 1）。Web の取得：0 回
