# review.md：subagent-isolation（分かりやすさの検証と直し）

## 指摘の表
| 番号 | 重さ | 場所 | 問題 | 直したこと |
|---|---|---|---|---|
| 1 | 直したほうがよい | #what-happens 末尾 | 圧縮の1文だけの段落が孤立し、薄い（U4） | 前の段落の末尾に「なお」でつなげた |
| 2 | 直したほうがよい | #what-it-helps 末尾 | 「窓」が節の中で未定義（U3） | 「コンテキストウィンドウ」に書き換えた |
| 3 | 軽い | #misconceptions | 「報告書は確かめなくてよい」が #what-it-helps と重なる | 直さない（誤解の一覧として必要） |
| U6 | 問題なし | 全体 | write.md の対応と本文が1項目ずつ合う。principle・prevents は #what-it-helps で名指し、構成は目安どおり、比例則は #what-it-helps、台帳3行も指している | なし |

## 検査の結果
- check_page.py：エラー 0・警告 0（直した後の1回）

## メインに判断してほしいこと
- write.md の2点（面タブなし、pitfalls なし）に同意。追加はなし

## 使用量
- 道具の呼び出し：約 9 回（Read 5、Edit 2、Bash 1、Write 1）。Web の取得：0
