# review.md：using-projects

## 指摘
| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | knowledge 冒頭 | prevents（見えていない・散らかっている）を本文で名指していない（feature の「どの原因を防ぐか」） | 1 文を足して名指した |
| 2 | 軽い | knowledge の 3 点目 | 「資料の版がそろう」は束の材料に直接の裏付けがない（事実は検証の担当） | 直さず。事実検証へ |
| 3 | 軽い | 導入・scope | U1・U3・U5・U8 は問題なし（要点と summary は一致、判断例は 4 行で答えあり、節は単独で通じる） | なし |
| 4 | 確認済み | U6 | write.md の対応と本文が合う：バッジ（要点・導入・instructions の feature 目印）、tracks・level（front matter）、構成（scope・knowledge→雛形→pitfalls→compare）。最小の使い方のタブは surfaces が app のみで省略、古くなった助言は台帳の行なしで省略。理由は妥当 | なし |

## 検査の結果
- check_page.py（直した後）：エラー 0・警告 1（78 行目 no-doubled-joshi。link の目印の間に道具が書いた題名が原因の誤検出。write.md と同じ）

## メインに判断してほしいこと
- 提案 projects-free-limit（write.md）は、本文が数字なしで読めるので急がない
- 2 の裏付けの確認を事実検証の担当へ

## 使用量
- 道具の呼び出し 8 回前後・Web の取得 0 回
