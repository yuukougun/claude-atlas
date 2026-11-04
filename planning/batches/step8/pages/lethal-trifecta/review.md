# lethal-trifecta 検証と直しの報告

## 指摘
| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直す | what-it-prevents の表の前 | A・B・C が節の中で定義されず、節だけ読むと表の「外すもの」が分からない | 「3 つの能力（A 信頼できない入力、B 私的なデータ、C 外への送信や変更）のどれを外すか」に直した |
| 2 | 直す | by-surface の最初の文 | 「この原則」が節の中に指すものがない | 「3 つを同時に持たせない原則」に直した |
| U6 | 確認済み | 全体 | write.md の対応を 1 項目ずつ突き合わせた。principle は what-it-prevents、prevents も what-it-prevents、pitfalls は空、要点の最初は「何が分かるか」、構成は example→three-capabilities→what-it-prevents→misconceptions で本文と合う | 直しなし |
| 3 | 軽い | 警告 12 件（no-doubled-joshi 9・sentence-length 1・max-ten 1・redundant 1） | 文体の警告 | 直さなかった。意味を変えずに直すと文が増えるため。メインが判断 |

## 検査の結果
- `check_page.py lethal-trifecta`（直した後に 1 回）：エラー 0・警告 12

## メインに判断してほしいこと
- write.md の 2 件（アプリの二条件の読み。材料 5 の v2.1.317 の扱い）はそのまま引き継ぐ
- 警告 12 件を直すか残すか

## 使用量
- 道具の呼び出し 約 7 回（Read 3・Bash 4）。Web の取得 0 回
