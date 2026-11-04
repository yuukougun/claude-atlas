# selection-pressure 執筆報告

## 書いたファイル
- docs/eval/selection-pressure.md（stubs から mv。stage: draft、updated: 2026-11-05）
- docs/img/selection-pressure/best-so-far.svg（模式図）
- front matter で変えたキー：sections（what-happens・what-it-affects・misconceptions を足した。既存の why・defenses・retry-cap は不変）、sources（既存 id 4 件）、stage、updated
- 雛形なし（目次の templates は「なし」）。data/sources.d/selection-pressure.yml は新しい出典がないので作っていない

## 必ず持つものの対応
- どの原理・原因に関わるか（principle 握る・確かめる／prevents 確かめていない）：#what-it-affects。pitfalls は空なので名指しなし
- level を持つ・要点の最初は「何が分かるか」：front matter level＝仕組みにする。要点の先頭項目は「何が分かるか」（冒頭）
- 構成の目安（要点→何が起きるか→なぜ→何に効くか→誤解→関連）：#what-happens → #why（図つき）→ #defenses → #retry-cap → #what-it-affects → #misconceptions。関連は末尾にテンプレートが出す

## メインに判断してほしいこと
- Fishtest FAQ の「おおむね 4〜5 回」は変わりうる慣行なので、本文に手で書いた（FAQ の引用として、根拠の印付き）。fact 化するなら下の提案を採り、本文を目印に差し替える
- 53 件中 16 件（約 30%）は二次の報道 1 本で原典未確認。根拠：弱と明記して本文に置いた（summary・signs には不使用）。不要なら削る

## 提案
```yaml
proposals:
  - fact: {id: fishtest-retry-cap, title: Fishtest が同じアイデアの再挑戦に置く上限（回数の目安）, value: "おおむね 4〜5 回", sources: [github-official-stockfish-fishtest], checked: 2026-11-05, status: 束の材料（research/24 B-50）による。FAQ 本文は未再確認}
    used_in: [selection-pressure#retry-cap]
```

## 検査の結果
- check_page.py 2 回：1 回目 エラー 0・警告 4、直した後 エラー 0・警告 2
- 残した警告 2 件（textlint no-doubled-joshi、76・78 行）：生成されたリンク文字列（「変更が効いたかを測る」など長い題名）が文に入るための誤検出。本文側の文は短くした

## 確かめていないこと
- 事実は束の写しに基づく。一次資料は開いていない（Web 取得 0 回）。AI Weekly・Fishtest FAQ・Anthropic の記事の原文は再確認していない
- 図は模式図で、数値の根拠はない。SVG の見え方（ブラウザ表示）は未確認
- 「見せないデータを何度も見れば選ぶ根拠になる」は推論として印を付けた
- lockbox-and-holdout など前提・関連先のページ本文は読んでいない（束の要約と指せる節のみ）

## 使用量
- 道具の呼び出し 13 回（Read 3、Bash 8 ほか）・Web の取得 0 回
