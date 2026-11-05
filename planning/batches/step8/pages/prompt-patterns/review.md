# review.md：prompt-patterns

| 番号 | 重さ | 場所 | 問題 | 直したこと |
|---|---|---|---|---|
| 1 | 直す | #analysis | 雛形 analysis-request.md がなく「準備中」と出る | Write が止められ書けず。案を最後の返答に載せた |
| 2 | 直したほうがよい | #guards 3 つ目 | 「余地も、そのまま使い回す」が読み取りにくい | 「使い回すと…毎回そのまま残る」に直した |
| 3 | 軽い | #plan-and-bug 164 行 | 助詞「に」の重なり | 直さず（読める） |
| U6 | 問題なし | #procedure・#guards・#check・#when-it-fails | write.md の対応と本文が合う。手順・確かめる縛るへの道・level・構成の目安あり | - |

## 検査の結果
直した後：エラー 0・警告 3（雛形なし 1・助詞 2）

## メインに判断してほしいこと
- analysis-request.md を作る（案は最後の返答）。作ったら gen_site --page で埋める
- stage は draft のまま（直しあり）

## 使用量
道具の呼び出し 8 回、Web 0 回
