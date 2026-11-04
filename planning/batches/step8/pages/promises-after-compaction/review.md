# review.md：promises-after-compaction

| 番号 | 重さ | 場所 | 問題 | 直したこと |
|---|---|---|---|---|
| 1 | 直したほうがよい | #misconceptions | 見出しが誤解か事実か区別しにくい（「スキルの一覧は圧縮で戻らない」が事実に読める） | 各項目を「誤解：…」の形に統一 |
| 2 | 直したほうがよい | #where-to-put の deny 雛形 | 本文は「main への push」だが雛形は push 全部を止める | 雛形の後に、全 push を止める旨と書き換えの 1 文を追記 |
| 3 | 直したほうがよい | #where-to-put | 「auto モードの分類器」が未定義（U5） | 括弧で動作を短く定義 |
| 4 | 軽い | #where-to-put | 「compact に合う SessionStart フック」が曖昧 | 「compact を matcher にした」に変更 |
| 5 | 軽い | 冒頭 | 要点・導入は signs と合い、答えが先にある | 直さない |
| U6 | 問題なし | 全体 | write.md の対応を突き合わせた。principle・prevents は #effects で名指しあり、pitfalls は空で対象なし、level と「何が分かるか」は冒頭にあり、構成は目安どおり | 直さない |

## 検査の結果
- 直した後の check_page：エラー 0・警告 4（no-doubled-joshi。執筆時と同じ、残した）

## メインに判断してほしいこと
- 図の案を表で代えた件は、表で用が足りると見た。図は必須でない

## 使用量
- 道具の呼び出し：8 回（check_page 1 回）、Web の取得 0
