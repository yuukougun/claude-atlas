# review.md：verifier-defines-problem

| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | #loops-amplify | 「アブレーション」が未定義で、読者が止まる | 「要素を 1 つずつ足して効果を比べた実験」と言い換えた |
| 2 | 軽い | #why | 「scaffold」が説明なし | 「足場（scaffold）」にした |
| 3 | 直したほうがよい | #verifier-first | 「検証器が通ると人は中身を見なくなる」が断定で、根拠がない | 「見なくなりやすい（推論）」にした |
| 4 | 軽い | #why 1 つ目の箇条 | C コンパイラと CORE-Bench が 1 箇条に入り密 | 直さない（分けると薄くなる） |
| 5 | 軽い | #map | related の案内で hub と重なる | 直さない（総論の節として sections にある。write.md の判断待ち） |
| U6 | 問題なし | 全体 | write.md の対応と本文が一致。#verifier-first が principle・prevents・pitfalls を名指し、構成は目安どおり | なし |

U1〜U3・U5・U8：冒頭で用が足り、節は単独で通じ、Before/After に注記、判断例は 4 行で答えが両側とも筋が通る。

## 検査の結果
エラー 0・警告 1（62 行目の sentence-length。After の依頼文の「」書きで、執筆の報告と同じ。残した）。

## メインに判断してほしいこと
- #map を残すか（write.md と同じ論点）。

## 使用量
道具の呼び出し：約 8 回（Read 3、Bash 4、Write 1）。Web の取得：0。
