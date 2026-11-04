# write.md：what-each-surface-cannot-do

## 書いたファイル
- `docs/surfaces/what-each-surface-cannot-do.md`（stub から移した。stage は draft、updated は 2026-11-05）
- front matter で変えたキー：`sections`（`gaps-within-a-surface` を足した）・`sources`（既存の id 7 つ）・`stage`・`updated`
- 雛形・図・`data/sources.d` は置いていない（目次の templates・visual が「なし」）

## 必ず持つものの対応
- データから作る表：`#table`（`compare 面 成熟度 確認日`。tracks の 5 機能）
- 構成の目安（要点 → 生成の表 → 読み方）：要点（冒頭）→ `#table` → `#gaps-within-a-surface` → `#moving-between-surfaces`（読み方と判断）。台帳の行（outdated_advice）が空のため `ledger` の目印は置かない
- level：持たない（front matter に level なし）

## メインに判断してほしいこと
- `#gaps-within-a-surface` は、data にない制約（シークレットチャット以外のアプリ内の差・Claude Code のクラウドの設定）を、調査資料（確認日 2026-10-29）から手で書いている。data の features へ入れるか判断してほしい
- 台帳の行 `cowork-separate-app` を link で指した。ページの `outdated_advice` は空のまま（直す提案はしていない）

## 提案
```yaml
frontmatter: []
```
- data の提案：アプリ内の面（Web・Desktop・モバイル）ごとの対応を持つ属性が data にない。表が「アプリ」1 行になる。`features` に面の細分か「統合の後の制約」の項目を足すと、表で出せる

## 検査の結果
- `check_page.py` を 2 回流した。1 回目はエラー 1・警告 2（prh の plugin、助詞の重複、「一つ」）。直して 2 回目はエラー 0・警告 0

## 確かめていないこと
- 本文の制約の内容は束の写し（02 §1-1・§1-15・§1-16、01 P-1、research/26）に基づく。一次資料は開いていない（Web の取得 0）
- 「モバイルでは artifact が使えない」（00 §3 の例）は束に裏付けがなく、本文に書いていない
- API 側の code execution tool の有無は束にない。本文は「別の機能として扱われる」とだけ書いた
- 画面操作が Web・モバイルで使えないかは確かめていない（本文もそう書いた）
- `incognito-chats#limits` などの節の中身と、link の表示は、公開前の生成で確かめていない

## 使用量
- 道具の呼び出し 11 回（Read 4・Bash 5・Write 2 ほか）、Web の取得 0
