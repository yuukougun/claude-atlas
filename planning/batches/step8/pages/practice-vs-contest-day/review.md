# review.md：practice-vs-contest-day

## 指摘
| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直す | #what-to-ask-in-practice 判断例 | 「選んだもの」が迷う候補のどちらでもなく、理由の「どちらの候補も筋は通る」と合わない | 候補を「観察だけ頼む」「別の問題に移り後で戻る」に直し、選んだものと理由をそろえた |
| 2 | 直したほうがよい | #choosing-divisions 判断例 | 「次の大会」がどの大会か不明 | 「AI を禁じる大会までの期間が短い」に直した |
| 3 | 直したほうがよい | #test-under-contest-conditions | 原理「確かめる」を名指す語が弱い | 「（原理でいう「確かめる」）」を足した |
| 4 | 軽い | #what-to-ask-in-practice 表 | 行き先の列が右端（スマホ） | 直さない（列の意味が行頭の役から読め、支障は小さい） |
| U6 | 確認 | 全体 | write.md の対応と本文を突き合わせた。握る・確かめる・pitfalls・level は対応どおり。prevents は空で対象なし。型の目安の並びとの違い（誤解の節なし）は内容上問題なし | 3 で補強 |

## 検査の結果
- check_page.py（直した後の 1 回）：エラー 0・警告 8（write.md と同じ種類。no-doubled-joshi 7、展開後の雛形行の sentence-length 1）

## メインに判断してほしいこと
- 直したため stage は draft のまま。kyopro-atlas の practice-method の指し方は write.md の判断待ち

## 使用量
- 道具の呼び出し：約 8 回、Web の取得：0
