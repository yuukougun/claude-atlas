# write.md：looks-are-not-quality（執筆）

## 書いたファイル
- `docs/verify/looks-are-not-quality.md`（stubs から mv）。front matter で変えたキー：`sections`（5 節）・`sources`（既存 id 6 件）・`stage`（draft）・`updated`（2026-11-05）
- 雛形・図・`data/sources.d/` は置いていない（目次に templates・visual なし。出典は data/sources.yml に既にある id を使った）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（`principle`＝確かめる、`prevents`＝確かめていない）：要点の「関わる原理と原因」と `#what-it-helps` で名指し
- 要点の最初の項目は「何が分かるか」：要点の囲み
- level（任せる）：front matter のまま
- 構成の目安（要点 → 何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：`#what-happens`・`#why`・`#what-to-check`（見た目の代わりに見るもの。目安に足した節）・`#what-it-helps`・`#misconceptions`。関連はテンプレートが出す
- `pitfalls` は空のため名指す対象なし

## メインに判断してほしいこと
- `#why` の「比喩付きの図」は置かなかった（一覧に合う比喩がない。表で代えた）。必要なら図の案を頼む
- SpecBench の注記（記憶したコンパイラは Claude の結果ではない）に従い、その例は本文に使っていない
- 修正中に、Write ではなく Bash（python3 で文字列置換）でページを 1 回直してしまった。内容は同じ趣旨の文の短縮だけ

## 提案
- front matter：なし（related の frontend-design・make-slides は本文で指した）

## 検査の結果
- 1 回目：エラー 0・警告 6（助詞の重複・読点・文長）。直して 2 回目：エラー 0・警告 2（`no-doubled-joshi`、「悪意で飾るわけではない」の次の文）。その文を言い換えたが、直した後の再検査は規則の回数（2 回）を使い切ったため流していない

## 確かめていないこと
- 最後の言い換え 1 文の textlint の結果
- 外部の URL の中身（束の写しと既存の sources.yml の記載に基づく。Web の取得は 0 回）
- Willison・SpecBench・Anthropic のブログ・システムカードの主張の細部は、束の第18章の写しに依る。システムカードの「根拠：強」は当時の世代の公式記録としての付け方
- Claude Code 以外の面（アプリ）の挙動は扱っていない

## 使用量
- 道具の呼び出し：Read 2・Bash 7 ほか Write 2・Edit 3（概算）。Web の取得 0
