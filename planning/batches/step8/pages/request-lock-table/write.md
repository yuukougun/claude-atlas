# write.md：request-lock-table

## 書いたファイル
- `docs/enforce/request-lock-table.md`（stubs から mv。stage を draft、updated を 2026-11-05、sources を既存 id の 8 件に）
- front matter の `sections` に 3 節を足した：`choose`（選び方（判断例））・`combine`（組み合わせ方と確かめ方）・`outdated`（古くなった助言）。既存の `table`・`where-locks-act`・`by-surface` は変えていない
- 雛形・図・`data/sources.d/request-lock-table.yml` は作っていない（目次の templates が「なし」。新しい出典も足していない）

## 必ず持つものの対応
- 冒頭の要点：最初の `##` の前（要点の囲み）。「何ができるか」が「〜なら鍵、〜ならお願い」の基準 1 文
- 比較の表（属性は道具が生成）：`#table`（`compare 面 強制力 圧縮で残るか`）。用途ごとの手書きの表も同じ節
- 判断例：`#where-locks-act`（返答の言語）、`#choose`（push の禁止・JSON の受け渡し）
- 組み合わせ方：`#combine`
- 確かめ方：`#combine` の後半（共通の手引き §6 の確かめ方を畳んだ）
- level：front matter に `任せる`（変更なし）

## メインに判断してほしいこと
- `#table` の手書きの表の「文体・表記」「返答の言語」の行は、research/27 §3.2 と textlint-hook・keep-replies-in-japanese の要約に基づく。Stop フックで言語を確かめる行を鍵として載せたが、言語の判定のしかたは公式の例がない（keep-replies-in-japanese 側の扱いと揃うか確認してほしい）
- `#combine` の「止めるのは壊れにくい手段に任せる」は research/28 の推論（試していない）で、本文に（推論・実践例なし）と付けた。残すか削るか

## 提案
- front matter・用語集・prh・data への提案はない

## 検査の結果
- 1 回目：エラー 0・警告 2（助詞「に」の重複。`#where-locks-act` 1 件、`#outdated` 1 件）
- 2 回目：同 2 件を直した後、エラー 0・警告 1（`#where-locks-act` の「画面に出る前に」）
- 3 回目は流していない。警告 1 件は「画面へ出る前に」に直しただけで、再検査していない。メインの検査で確かめてほしい

## 確かめていないこと
- 1 回目の検査以降、gen_site が目印の間を埋めたが、compare の表（面・強制力・圧縮で残るか）の見え方を目で確かめていない。structured outputs の「圧縮で残るか」は null のため「未確認」と出ると思われる
- 手書きの表の各行（Stop フックの続けて止める回数の上限、PostToolUse が Bash の書き込みで動かない点、MessageDisplay が止められない点）は束の写しによる。一次資料を開いていない
- `-p` で形を指定する方法を鍵として扱ってよいかは、structured-outputs-basics#claude-code の本文を読んでいない（表では「指示と検査の組み合わせ」と書き、鍵としては扱っていない）
- ledger の行への link の解決は検査に任せた。他の OS と IDE 拡張の動作は書いていない

## 使用量
- 道具の呼び出し：約 12 回（Read 3・Bash 6・Write 2・ほか）。Web の取得：0 回
