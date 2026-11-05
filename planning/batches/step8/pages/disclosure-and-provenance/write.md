# write.md：disclosure-and-provenance

## 書いたファイル

- docs/safety/disclosure-and-provenance.md（stubs から移した。stub のファイルは削除）
- snippets/disclosure-and-provenance/provenance-log.md と provenance-log.expect.yaml
- front matter で変えたキー：sections（`effects`・`misconceptions` を足した。既存の 3 つはそのまま）、sources（既存の id の `mext-genai-university-overview`・`anthropic-fable-mythos-5-1`）、stage（draft）、updated（2026-11-05）
- data/sources.d/disclosure-and-provenance.yml は作っていない（出典は既存の id だけで足りた）

## 必ず持つものの対応

- 冒頭の要点：本文の先頭の `!!! abstract`（最初の項目は「何が分かるか」）
- level（整える）：front matter。要点と {#provenance}・{#explainable} が成果物を人に出す段階の話
- どの原理・原因に関わるか（principle：握る）：{#effects}。`prevents`・`pitfalls` は空なので名指す値がない。{#effects} の最後の段落でその旨を本文に書いた
- 構成の目安（原理・仕組み）：要点 → {#four-points}（何が起きるか）→ {#provenance}・{#explainable}（なぜ・どうするか）→ {#effects}（何に効くか）→ {#misconceptions}（誤解）→ 関連（テンプレート）。比喩付きの図は置かなかった

## メインに判断してほしいこと

- 節の題名「開示・相談・出所・意図の四つの観点」は textlint の「四つ」の対象になりうる。今回の検査では出なかった。出る場合は題名を「4 つの観点」にする提案（anchor は変えない）
- 文部科学省の通知の記述は、束の材料（11 第2節 p56#108）に基づく。通知の本文は開いていない。「今の版を確かめる」と書いた。版（年）は本文に書いていない

## 提案

数値の提案はなし。front matter の提案もなし（prevents・pitfalls が空であることは目次側の判断に任せる）。

## 検査の結果

- `check_page.py` を 1 回流した：エラー 0・警告 1
- 警告 1 件：誤の可能性が高い。本文 {#misconceptions} の 4 つ目の項目で、link の目印の間に道具が書く節の題名（「課題資料・問題文に仕込まれた指示 › 規則を先に確かめる」）に助詞「に」が重なると出る。生成される文字なので直していない

## 確かめていないこと

- 雛形 provenance-log は動作を確かめていない（記録の型で、実行するものではない）
- 文部科学省の通知と Anthropic の透かしの説明は、束の写しに基づく。一次資料を開き直していない。透かしの対象時期・検出 API の提供範囲は、本文に日付を書かず「発表で確かめる」とした
- Claude Code・アプリで、使った記録をセッションから取り出す方法は書いていない（束に材料がなく、未確認）
- 大会ごとの開示の求め方は、条文を要約せず competition-rules に任せた

## 使用量

- 道具の呼び出し：約 12 回。Web の取得：0 回
