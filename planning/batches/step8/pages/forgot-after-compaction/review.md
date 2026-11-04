# review.md：forgot-after-compaction

## 指摘
| 番号 | 重さ | 場所 | 問題 | 直したこと |
|---|---|---|---|---|
| 1 | 直したほうがよい | #diagnosis 項目1 | 「雛形の依頼」が、まだ出ていない雛形を指す（U3） | 「この節の末に置いた雛形」と明示 |
| 2 | 直したほうがよい | #diagnosis 項目6 | 版が原因のとき何をするかがない（U2） | 版を上げて再確認する一文を足した |
| 3 | 直したほうがよい | #diagnosis 雛形の後 | 診断の途中に「Claude Code 基準・アプリと API は未確認」の段落が浮く（U3・U7） | 冒頭の導入段落の末へ移した |
| 4 | 軽い | 判断例2 | 迷う候補の片方（全文を CLAUDE.md へ）がやや弱い | 直さない（筋は通る） |
| U6 | 問題なし | 全体 | write.md の対応と本文が一致。診断6項目・routes の目印・構成順（要点→forms→diagnosis→routes→examples→prevention）を確認。人の側の落とし穴は節末の1段落で six-causes#diagnosis を指す | 直し不要 |

## 検査の結果
- check_page.py 1回：エラー 0・警告 1（no-doubled-joshi。link の題名が入った文での誤検出と見る。write.md と同じ）

## メインに判断してほしいこと
- 項目6の版の目印は、write.md の提案（compaction-bugfix-min-version）を採るかの判断待ち

## 使用量
- 道具の呼び出し：約 8 回。Web の取得：0
