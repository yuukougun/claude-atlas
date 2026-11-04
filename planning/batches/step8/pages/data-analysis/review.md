# review.md：data-analysis（データを分析する）

## 指摘
| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 軽い | `#when-it-fails` の表 | 「上の『再実行できる形で集計させる』で」と節名で指す。表を断片で読むと「上の」が節を探させる | 直さない（節名が書いてあり通じる） |
| 2 | 軽い | `#how-to-check` | `#check-raw-data` と内容が一部重なる | 直さない（recipe の「全体の確かめ方」として一覧に使える） |
| U6 | 問題なし | 全体 | write.md の対応と本文を突き合わせた。手順（`#reproducible-queries`・`#check-raw-data`）、守りへの道（`#guards`、前提・関連も）、level（任せる）、構成の目安の並びが本文と合う | - |

U1〜U5・U7〜U10 は「直す」「直したほうがよい」の指摘なし（要点と summary は一致、判断例は 4 行で答えが見え両候補が筋が通る、タブは surfaces と合う）。

## 検査の結果
- `check_page.py data-analysis` 1 回：エラー 0・警告 0

## stage
- 指摘 0 件のため stage を draft から reviewed にした

## メインに判断してほしいこと
- write.md の判断事項（A-8 雛形の正本を本ページにしたこと）はそのまま引き継ぐ

## 使用量
- 道具の呼び出し：Read 5・Edit 1・Bash 1・Write 1、Web の取得 0 回
