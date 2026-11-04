# review.md：skill-descriptions

## 指摘

| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直したほうがよい | #old-advice | 「台帳に載せる古い助言は、このページにはない」が読者には唐突で、数値の確かめ先も曖昧 | 冒頭を言い直し、確かめ先を #front-load の数値に指定 |
| 2 | 軽い（直した） | #limits の最後の箇条 | 見出し語「数を測ってから足す」が中身（長くしても確実にならない）と合わない | 見出し語を「長くしても確実にはならない」に変更 |
| 3 | 軽い | #usage | `when_to_use` が定義なしに出る | 直さず。#front-load で説明があり、材料に詳細がないため |
| U6 | 問題なし | 全体 | write.md の対応と本文が合う（強制力は冒頭、load_timing は #purpose、構成の並びは目安どおり、tracks と level は front matter） | なし |

U1〜U5・U7〜U10 は指摘なし（Before/After に注記あり、判断例は 4 行で答えが見える、面のタブは surfaces と一致）。

## 検査の結果

- 直した後：エラー 0・警告 0（write.md の言う手での見出し語の直しも、この検査で問題なしと確認した）
- stage：直したので draft のまま

## メインに判断してほしいこと

- write.md の提案（related に skills-in-the-app・hook-vs-skill・instructions-ignored を足す、glossary に description）は未判断のまま残る
- #old-advice は薄い。write.md のとおり、節ごと削るか判断が要る

## 使用量

- 道具の呼び出し：約 9 回。Web の取得：0 回
