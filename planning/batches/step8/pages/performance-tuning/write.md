# write：performance-tuning

## 書いたファイル

- `docs/recipes/performance-tuning.md`（`stubs/recipes/` から mv。stage を draft に）
- `snippets/performance-tuning/measured-speedup-request.txt` と `.expect.yaml`（prompt。目次の templates の案：出力が変わる候補を別コミットに分け、受け入れ条件を平均と最悪の帯に切り替える）
- `docs/img/performance-tuning/gates.svg`（目次の図の案：4 つの関門）
- `data/sources.d/performance-tuning.yml`（arxiv-2511-06090 の 1 件。ほかの出典は既存の id）
- front matter で変えたキー：`sections`（guard-first・steps・check-and-failure を足し、既存の 4 つの anchor は維持）、`sources`、`stage`（draft）、`updated`（2026-11-05）

## 必ず持つものの対応

- 手順：`#steps`（4 つの関門と各段の終わりの確かめ）と、詳細は `#profile-first`・`#same-output-and-timing`・`#output-changing-changes`・`#too-good-speedups`
- 確かめる・縛るのページへの道：front matter の prerequisites（suspect-too-good-results・differential-testing）と、本文の `#guard-first`（freeze-eval-assets・differential-testing・evidence-not-reports）
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：`#guard-first` → `#steps` ほか → `#check-and-failure`
- level：front matter（任せる）

## メインに判断してほしいこと

- sections を 3 つ足した。守り・手順・確かめ方と失敗したときを、recipe の構成の目安どおり独立の節にするため。不要なら統合してよい

## 提案

- なし（変わりやすい値は本文に置いていない。研究の数値はモデル・対象・年を添えた固定の記録として書いた）

## 検査の結果

- `check_page.py` を 2 回流した。エラー 0、警告 3。直せていない警告（3 件、いずれも文体の指摘で、意味を保ったまま分けると読みにくくなるため残した）：112 行の助詞「が」の重複（ISUCON14 の文）、137 行の助詞「に」の重複（link の題名が間に入る文）、141 行の文の長さ（PERFOPT-Bench の項）

## 確かめていないこと

- 雛形の動作（実際に Claude Code に出していない）
- arxiv-2511-06090：題名・著者・要旨は abs のページで確かめた。0.225 倍と「専門家の改善の 68% 超がモデルの編集しない関数にある」は調査資料（research/24 A-11）に拠り、論文 v3 の本文では確かめていない
- Wafer の事例のモデルは調査資料にないため、書いていない。PERFOPT-Bench の「Claude の構成は近道の表に出ない」は research/24 A-9 に拠る
- 「回数の例は 5 回」「2 倍を超えたら」は調査資料の実践の目安で、研究の値ではない（本文でも経験則と書いた）
- ISUCON14 の計装の項は、調査資料の要約に拠る（Splunk の記事の本文は開いていない）
- AtCoder のジャッジとローカルの速度差の資料は見つからなかった旨は、本文に入れていない

## 使用量

- 道具の呼び出し：約 14 回。Web の取得：1 回（arxiv の abs）
