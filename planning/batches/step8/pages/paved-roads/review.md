# review.md：paved-roads（concept・team）

## 指摘

| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | #amplifier 1文目 | DORA が何の調査か説明なしに出る（U5） | 「開発の成果を測る調査研究 DORA（Google Cloud）の」と添えた |
| 2 | 直したほうがよい | #misconceptions 3つ目 | 「という使い方にとどめる」が何を指すか不明（U3） | 「この調査から言えるのは、…という注意までである」に直した |
| 3 | U6（問題なし） | 全体 | write.md の対応は本文と合う。`principle`（縛る・握る）と `prevents`（境界がない・縛っていない）は #principles-and-causes で名指し。level・要点の先頭「何が分かるか」あり。図なしの理由も妥当 | なし |
| 4 | 軽い | 冒頭・U1/U2/U4/U7/U8 | 要点は summary と合い、判断例は4行で迷う候補が両立、守りが広げる話に先行、薄い節なし | なし |

## 検査の結果

- 直した後の check_page.py：エラー 0・警告 0

## メインに判断してほしいこと

- stage は draft のまま（直したため）。write.md にあった `dora.dev` の domains の件は check_page が通っている

## 使用量

- 道具の呼び出し：約 9 回。Web の取得：0 回
