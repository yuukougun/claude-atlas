# make-slides 執筆報告

## 書いたファイル

- `docs/recipes/make-slides.md`（stub から移した。stage は draft、updated は 2026-11-05）
- front matter で変えたキー：`sections`（5 節）・`sources`（[hc-artifacts, claude-docs-m365-powerpoint, hc-files]。いずれも data/sources.yml にある）・`stage`・`updated`
- `snippets/make-slides/draft-request.txt`・`.expect.yaml`（目次の templates の案）
- `snippets/make-slides/check-request.txt`・`.expect.yaml`（足した雛形：資料と照らす依頼）
- `data/sources.d/make-slides.yml` は作っていない（新しい出典なし）

## 必ず持つものの対応

- 冒頭の要点：冒頭の `!!! abstract "要点"`
- 手順：`#steps`（各段に確かめ付き）
- 確かめる・縛るのページへの道：`prerequisites` の fact-checking（要点の前提と `#guard`・`#verify` で link）。ほかに `#guard` で looks-are-not-quality と ai-ideas-are-everyones
- level：front matter `level: 整える`（変更なし）
- 構成の目安（要点 → 先に整える守り → 手順 → 確かめ方 → 失敗したとき）：`#guard` → `#steps` → `#tools`（手順 5 の手段の選び方）→ `#verify` → `#when-it-fails`

## メインに判断してほしいこと

- 手順 6 で「2 割」を数にせず、目安の言い方で割合ではないと書いた（目次の notes に従った）。
- Marp は Claude Code タブで例として名前を出すだけにした。第三者ツールの成熟度と確認日は付けておらず、本文に「確かめていない」と書いた。

## 提案

- 用語集・prh・data・front matter の提案はなし。

## 検査の結果

- 1 回目：エラー 0・警告 3（助詞「に」の重なり）。直した後に流した 2 回目：エラー 0・警告 1。残りの 1 件（判断例の理由の文）は、報告の後に文を書き換えて直した。書き換え後は流していない（規定の回数のため）。

## 確かめていないこと

- 雛形 2 つの動作（実際に Claude へ依頼して出力を見ていない）。
- アーティファクト・PowerPoint のアドインのスライドの機能の細部と成熟度の食い違い（本文は表の `compare` と各ページへのリンクに任せた）。
- Marp の現在の状態と書き方。Claude Code でスライドのファイルを直接作らせる方法。
- Claude Code タブの「リポジトリに置くと差分が追える」は一般の説明で、出典はない。

## 使用量

- 道具の呼び出し：約 20 回。Web の取得：0 回。
