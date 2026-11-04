# write.md：unfaithful-reasoning（執筆）

## 書いたファイル
- docs/basics/unfaithful-reasoning.md（stubs から mv。stage: draft、updated: 2026-11-05）。front matter で変えたキー：sections（4 節を足した）・sources（4 件）・stage・updated
- data/sources.d/unfaithful-reasoning.yml（anthropic-research-reasoning-models-dont-say-think を 1 件足した）
- 雛形・図：なし（目次の templates・visual が「なし」。比喩の図も作らず、表と判断例で足りるとした）

## 必ず持つものの対応
- 用途（なぜそうなるか。原理・仕組み）：#what-happens（例の表）・#why（仕組み）
- どの原理・原因に関わるか（principle「確かめる」・prevents「確かめていない」を名指す）：#effects
- pitfalls：front matter に無いので本文でも名指さない
- level（整える）を持つ。要点の最初は「何が分かるか」：冒頭の要点
- 構成の目安（要点 → 何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：#what-happens・#why・#effects・#misconceptions。関連はテンプレートが出す
- 台帳（thinking-tags）：#effects の末尾で link の目印で指した

## メインに判断してほしいこと
- 「なぜそうなるか」の比喩付きの図は置いていない。比喩の一覧に合うものがなく、図の案も無かったため。必要なら別の担当に図の案を頼む

## 提案
- front matter・用語集・data への提案はない。なお signs の goal「なぜその答えになったのか、過程を全部見せてほしい」に、このページは「見せても一致するとは限らない」を答えている（変更の提案ではない）

## 検査の結果
- check_page.py を 2 回流した。最後はエラー 0・警告 2
- 警告 2（残した）：行 35（要点の囲み）と行 93（誤解の節）の no-doubled-joshi（助詞「に」「が」の重なり）。意味を保つと避けにくい長さの文なので、検証と直しの担当が読んで判断してほしい

## 確かめていないこと
- 事実は Web の取得 2 回（Anthropic の 2 つの研究の解説ページ）で確かめた。論文の本文は読んでいない。数値（25%・41%）は解説ページの記述による
- tracing-thoughts のページは、思考の忠実さの例（cosine・ヒント）がどのモデルのものかを書いていない。本文は「中心は Claude 3.5 Haiku」と書いたので、例ごとのモデルは断定していない。ここが強すぎないか、検証で見てほしい
- 「推論を見せるとレビューが同じ道筋に引かれやすい」は、independent-review#hide-reasoning の題名と要約に基づく言い換えで、そのページの本文は読んでいない
- 判断例は想定の場面で、実際に動かして確かめたものではない
- 雛形がないので、動作確認はない

## 使用量
- 道具の呼び出し：約 15 回（Web の取得 2 回。check_noai は 2 回）
