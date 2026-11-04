# write.md：practice-vs-contest-day

## 書いたファイル
- docs/contest/practice-vs-contest-day.md（stubs から mv。stage を draft、updated を 2026-11-05 に。sections は変更なし）
- snippets/practice-vs-contest-day/practice-coach.md と practice-coach.expect.yaml（目次の templates は「なし」。分かりやすさのために 1 つ足した）
- data/sources.d は作らず、front matter の sources は空のまま

## 必ず持つものの対応
- 冒頭の要点（何が分かるか・いつ引くか・前提）：冒頭の囲み
- 原理 `principle`（握る・確かめる）を名指す：#what-to-ask-in-practice（握る）・#test-under-contest-conditions（確かめる）
- `pitfalls`（預けすぎる・体感を信じる）を名指す：#rules-change-the-line（末尾の段落）
- `prevents`：front matter が空のため、名指す対象なし
- level（整える）：front matter。要点の最初は「何が分かるか」

## メインに判断してほしいこと
- kyopro-atlas の practice-method への指し方：本文は URL なしで名前だけ書いた（導入の段落）。公開 URL か相対リンクの決まりがあれば反映してほしい
- 「AtCoder の規則は過去問の練習には適用されない」は書いていない（未確認のため）。「練習と本番で規則の扱いが違うことがある」の一般の注意にとどめた
- 根拠の弱い主張に印を付けた：「丸投げ OK／要確認／禁止」の線引きと、解説役・採点役の使い分けは（根拠：弱）、部門の使い分けも（根拠：弱）、本番条件の確かめ方の手順は（推論・実践例なし）。必須ページの中心が推論になっていないか、見てほしい
- 部門の類型や AHC の日付・「今後数回」の範囲は、変わりやすいので本文に書かず competition-rules を指した

## 提案
- front matter、用語集、data への提案なし

## 検査の結果
- check_page.py を 2 回流した。1 回目：エラー 1（半角と全角の間の空白）・警告 9。直した後：エラー 0・警告 8
- 残した警告：no-doubled-joshi 7 件（短い要点の囲み・箇条・リンク展開後の長い題名を含む行。列の位置は展開後の行で、本文では離れた助詞）、sentence-length 1 件（122 行は、道具が展開した雛形の行）。本文の文は短くしてある

## 確かめていないこと
- 事実の確認は束の材料の範囲。Web の取得はしていない
- 雛形 practice-coach は試していない（expect は未確認の記録）
- 囲み（`!!!`）の中の字下げした段落の textlint は、検査されない。判断例の各行は「。」で終えた

## 使用量
- 道具の呼び出し：約 12 回、Web の取得：0
