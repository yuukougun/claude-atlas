# write.md：inconsistent-japanese-style

## 書いたファイル

- `docs/symptoms/inconsistent-japanese-style.md`（stubs から mv。stage を draft に、updated を 2026-11-05 に）
- front matter で変えたキー：`sections`（forms・examples・prevention を足した。diagnosis は据え置き）・`sources`（既存の id 7 件を足した）・`stage`・`updated`
- 雛形・図・`data/sources.d/` は作っていない（目次の templates と visual が「なし」。新しい出典もない）

## 必ず持つものの対応

- 診断のチェックリスト（原因を安く確かめる順）：`#diagnosis`（1 見えていない・2 散らかっている・3 縛っていない。上から安い順）
- 人の側の落とし穴：`#diagnosis` の 1 の中（揃える基準の正本を自分が決めていない）。front matter の `pitfalls` は空なので、独立の項目は立てていない
- 原因ごとの振り分け先（routes）：`#diagnosis` の末尾の `routes` の目印
- 型の構成の目安（要点→よくある形→診断→routes→判断例→予防）：冒頭の要点、`#forms`、`#diagnosis`、`#examples`、`#prevention`

## メインに判断してほしいこと

- 「いつ引くか」と「よくある形」で、sign の「サーバー」と「サーバ」を、prh の誤検出を避けるため「同じ語の表記が混在する」と言い換えた（`#forms` にだけ例を出し、`textlint-disable prh` で囲んだ）。sign の文字そのものを要点に出したいなら、検査の結果を見て判断してほしい
- アプリと API の「機械で確かめて差し戻す仕組み」は、他の症状ページ（replies-in-english）に合わせて「未確認」と書いた

## 提案

用語集・prh・data・手引きへの提案はない。

## 検査の結果

- 1 回目：エラー 0・警告 3（助詞の重複 `no-doubled-joshi`）
- 直した後：エラー 0・警告 1。残りの 1 件（`にも`）も文を直したが、その直しの後の検査は流していない（2 回の決まりのため）

## 確かめていないこと

- 最後の直し（`#diagnosis` の 1 の「決まっていない基準は、指示に書けず、検査に使うこともできない」）は、検査を流していない
- `gen:begin feature hooks/enforcement`・`skills/enforcement` の目印が、意図した値（鍵・お願い）で埋まるかの目視確認と、リンク先の題名が入った後の文の読みやすさ
- `grep -nE` の例の正規表現を実際に流して確かめていない
- 「長い文章の途中で崩れる」原因を切り分けた資料は束にない。診断では確かめ方（位置と直前に読んだものを控える）だけを書き、機序は断定していない
- アプリの Styles が今の画面に出るかは確かめていない（台帳の note のとおり）。本文は台帳へのリンクだけで、時期や名称の値は書いていない

## 使用量

- 道具の呼び出し：約 14 回（Read 4・Write 2・Bash 8 前後）。Web の取得：0 回
