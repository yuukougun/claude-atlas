# review.md：pruning-extensions

## 指摘

| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | #guards | `skillOverrides` が定義の前に出る（U5） | 「切る手順」の節への指しを足した |
| 2 | 直したほうがよい | #measure 手順 3 | 「Stats タブに開く」は何が開くか不明（U3） | 「タブが開く」に直した |
| 3 | 直したほうがよい | #criteria 表 2 行目 | 「自動起動を禁じて」が設定名なしで再現できない（U5） | `disable-model-invocation: true` を添えた |
| 4 | 軽い | #cut 見出し | 末尾の空白 | 削った |
| 5 | 問題なし | U6 | write.md の対応と本文が一致。手順は #measure・#cut、守りへの道は #guards と front matter、構成は目安どおり、level あり | 直しなし |

U1・U2・U4・U8 は問題なし。判断例は 4 行で、どちらの候補も筋が通る。

## 検査の結果

`check_page.py pruning-extensions`：エラー 0・警告 0（直した後の 1 回）

## メインに判断してほしいこと

- 直したので stage は draft のまま（別の担当が差分を確かめるまで）

## 使用量

- 道具の呼び出し：約 8 回。Web の取得：0 回
