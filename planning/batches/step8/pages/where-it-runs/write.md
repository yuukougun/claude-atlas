# where-it-runs 執筆報告

## 書いたファイル
- `docs/surfaces/where-it-runs.md`（stub から移動。stage を draft、updated を 2026-11-05、sources を既存の 5 件〔cc-docs-claude-code-on-the-web・cc-docs-remote-control・cc-docs-desktop・hc-cowork-surfaces・hc-cowork-and-chat〕に、sections に 3 節〔what-it-prevents・how-to-choose・misconceptions〕を足した）
- `snippets/where-it-runs/cloud-handoff.md` と `cloud-handoff.expect.yaml`（クラウドに送る依頼の雛形。動作は未確認）
- `data/sources.d/where-it-runs.yml` は作っていない（出典は data/sources.yml にある id だけを使った）

## 必ず持つものの対応
- どの原理・原因に関わるか（`principle`：見せる・縛る、`prevents`：見えていない・境界がない）：`#what-it-prevents`（2 項目で名指し）。`pitfalls` は空なので持たない
- 構成（要点 → 何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：要点は冒頭、何が起きるかは `#three-locations`・`#what-cloud-cannot-reach`・`#local-boundaries`・`#remote-control`、何に効くかは `#what-it-prevents`、誤解は `#misconceptions`、関連はテンプレートが出す。比喩付きの図は置かなかった（下の「メインに判断してほしいこと」）
- 要点の最初は「何が分かるか」：冒頭の囲み

## メインに判断してほしいこと
- 目次の図の案（実行場所と届くものの対応図）は、図でなく `#three-locations` の表にした。SVG の図が要るなら別途指示がほしい
- 「2026-10-06 から Pro・Max・Ultra の新しいタスクはクラウドで動く」は日付とプランの名前なので本文に書かず、`tasks-and-schedules-in-the-app#where-it-runs` を指した。data の app-tasks の note にあるので、必要なら主のページ側で扱う
- 競技の材料（11 第1節 p12#47、根拠が中〜弱で時点依存）は使わなかった

## 提案
- 用語集：プラグイン（plugin の訳）は prh が `plugin` を弾いたので本文を「プラグイン」にした。問題はない
- front matter の変更の提案はなし

## 検査の結果
- `check_page.py where-it-runs`：1 回目はエラー 1（prh：plugin）・警告 3（助詞「が」の重複）。直して 2 回目はエラー 0・警告 0

## 確かめていないこと
- クラウドのセッションで `/status` が使えて、読み込まれた層を同じ手順で確かめられるか（本文でも未確認と書いた）
- 「クラウドはリポジトリに入れたものだけ届く」「リポジトリの `CLAUDE.md` と `.claude/settings.json` は読まれる」は、束の「計画と縛りをリポジトリに置いてから送る」と「user 設定・local 設定・ローカル plugin を読まない」からの読み取りで、リポジトリ側の設定が読まれることを一次資料で直接は確かめていない
- 「ANTHROPIC_API_KEY をクラウドのセッションも Desktop も読まない」は research/26 §3.8 の写しによる。出典の公式文書は開いていない
- リモート操作で「手元の機械が止まるとセッションも続かない」は、実行が手元に残るという記述からの推論
- 雛形 cloud-handoff の動作、ほかの OS と IDE 拡張の挙動（未確認）
- 1 回の Write での執筆後、`outdated-advice-ledger#code-on-the-web-remote` と `control-from-phone` の実在は check_page の通過で確かめた（リンクの間は道具が埋めた）

## 使用量
- 道具の呼び出し 11 回前後（Read 4・Bash 5・Write 3 ほか）、Web の取得 0 回
