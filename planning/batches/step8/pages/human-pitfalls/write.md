# write.md：human-pitfalls（執筆）

## 書いたファイル
- docs/judgment/human-pitfalls.md（stubs から mv。front matter で変えたのは `sources`・`stage`（draft）・`updated`（2026-11-05）だけ）
- snippets/human-pitfalls/five-questions.md と five-questions.expect.yaml（目次の templates の案：五つの問いのメモ）
- docs/img/human-pitfalls/two-axes.svg（二つの軸の図。目次の visual の案）
- data/sources.d は作らず（使った出典 11 件は、すべて data/sources.yml に既にある id）

## 必ず持つものの対応
- 冒頭の要点：先頭の `!!! abstract "要点"`（何が分かるか・いつ引くか・前提）
- 判断例（状況・迷う候補・選んだもの・理由の4行）：`rules-and-tools` の末尾（「判断例：頭打ちの方針を続けるか」）
- level：front matter の level: 整える
- 構成の目安（要点→何が起きるか→なぜ→判断例→握るもの→確かめ方）：何が起きるか＝`five-pitfalls`・`evidence-strength`、なぜ＝`separate-axis`、判断例と握るもの＝`rules-and-tools`、確かめ方＝`self-check`

## メインに判断してほしいこと
- 「先に人が答える」（Buçinca ほか 2021）を本文に使った。brief の notes は「一次資料を確かめていない」とするため、PDF を 1 回取得したが読み取れず（本文が取れない）確かめられなかった。束の 6.4 の写しの内容（誤った AI への依存を減らす／成績のよい設計ほど好まれない）を（根拠：中・類推）で書いた。確かめるまで強めない、または削る判断がほしい
- 「確かめる手間を下げる」（Vasconcelos ほか 2023）は、既存の over-reliance の記述（著者らの見立て・模擬の AI）に合わせ、（根拠：中・類推）で書いた

## 提案
- 数値の提案（facts）はなし。研究の結果は固定の記録として本文に書いた（card §7）
- 用語集・prh・front matter の提案はなし

## 検査の結果
- 1 回目：エラー 0・警告 4（文の長さ 1・「への」「に」の重なり 3）。直した後の 2 回目：エラー 0・警告 1
- 残した警告：105 行目の「に」の重なり。link の間（道具が書く題名「…着手前に書き、…」と節名「基準を着手前に書く」）に「着手前に」が 2 回入るためで、手書きの文では直せない誤検出

## 確かめていないこと
- Buçinca ほか（2021）の一次資料（PDF が読み取れなかった）。Vasconcelos ほか（2023）は over-reliance の記述に合わせただけで、再確認していない
- METR の 2025 年の RCT の数値（16 人・実測は遅くなった）は束の写しから書いた。出典に付けたのは 2026 年の追試（metr-2026-uplift-update）で、2025 年の原典は sources にない
- Dell'Acqua ほか（19% 低い）・Doshi と Hauser（2024）・Holzner ほか（2025）は束の写し（research/24 §2.3）から書き、Mollick の解説と ScienceDaily と arXiv 2505.17241 を出典の id に付けた。原典は開いていない
- 他ページへの link の節名（`id#anchor`）は束の「指せる節」にあるものだけ使った。相手のページの本文は読んでいない
- SVG の見た目は目で確かめていない。素の語句（「見せる・確かめる・縛る」を Claude 側に、「握る・確かめる」を人の側に当てた）は目次の案に沿った大づかみの対応で、厳密な対応表ではない

## 使用量
- 道具の呼び出し：約 17 回（Web の取得 1 回）
