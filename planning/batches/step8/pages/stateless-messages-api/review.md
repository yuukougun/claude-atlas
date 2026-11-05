# review.md：stateless-messages-api

## 指摘
| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | #message-threads の 3 つ目の項目 | ZDR・HIPAA が定義なしに出る（U5） | 「ZDR（ゼロデータ保持の契約）と HIPAA 対応の利用」に直した |
| 2 | 軽い | #effects 判断例の理由 | 助詞「と」が重なる（write.md の残した警告） | 「読む量、料金、rate limits は変わらず」に直した |
| 3 | 軽い | 冒頭の囲み | 3 項目目「message threads」は標準の 3 項目の外 | 直さず（要点として有用で、summary と食い違わない） |
| U6 | 問題なし | 全体 | write.md の対応と本文が合う（要点・#stateless・#message-threads・#effects・#misconceptions。pitfalls は front matter にキーなし） | なし |

U1〜U5・U8〜U10 の他の点は問題なし（節の単独読み、判断例 4 行、表の幅）。

## 検査の結果
- check_page.py（直した後の 1 回）：エラー 0・警告 0
- stage：指摘（直したほうがよい）を直したので draft のまま

## メインに判断してほしいこと
- write.md の提案（message-threads-lifetime の fact）の反映。反映後、#message-threads の 1 つ目の項目に目印を置ける
- ZDR の言い換え「ゼロデータ保持の契約」と「HIPAA 対応の利用」は事実の検証をしていない。用語集に ZDR を足すか検討してほしい

## 使用量
- 道具の呼び出し：約 9 回、Web の取得：0 回
