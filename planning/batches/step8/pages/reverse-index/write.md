# write.md：reverse-index（執筆）

## 書いたファイル
- `docs/start/reverse-index.md`（`stubs/start/reverse-index.md` から mv）。front matter は `stage`: stub→draft、`updated`: 2026-11-05 のみ変更
- 雛形・図・`data/sources.d/reverse-index.yml` は置かない（hub で雛形なし。出典は本文で使わず、`sources` も足していない）

## 必ず持つものの対応
- 表とリンクが本体：`#by-symptom`・`#by-goal`・`#by-situation` に `signs symptom`・`signs goal`・`signs situation` の目印（空で置き、道具が生成）。`#how-to-read` と `#disambiguation` はリンクと手書きの注記
- level なし／`sources` は任意：どちらも持たない（hub）

## メインに判断してほしいこと
- 3 つの `signs` の目印の型名（symptom・goal・situation）は、`check_page.py` が通ったので有効と見た。ただし各ページの signs が未整備のため、生成結果はいまは「（まだない）」である。signs が入った後に、表の見え方と節の導入の文（章立て・面や型の印の説明）が実際の生成と合うか、確かめてほしい
- `field:symptoms` の link は「症状辞典（準備中）」と出る（公開ページがないため）

## 提案
- 特になし（front matter・用語集・data への提案なし）

## 検査の結果
- 1 回目：エラー 2（前提の「なし」の書き方、prh の front matter→フロントマター）・警告 3 → 直した
- 2 回目：エラー 0・警告 2（`no-doubled-joshi` の「が」。96 行「ページが並ぶことがある」、99 行「手段が違うことが多く」）。自然な文で、直すと読みにくくなるため残した

## 確かめていないこと
- 生成後の表の内容（signs が未整備で空）。「対処のページが先に出る行」「面や型の印」の記述は、設計（design §7・DR-15）に基づく説明で、実際の生成物では確かめていない
- 節の導入が挙げる症状辞典の章名（返答の品質・会話と文脈・指示と仕組み）は、調査資料 00 §4 の見出しに基づく。実際の章名と合うかは未確認
- リンク先ページの本文は未公開で、指せる節の内容は束の題名だけで判断した

## 使用量
- 道具の呼び出し：Read 3・Bash 3・Write 2・check_page 2（Bash の中）。Web の取得 0
