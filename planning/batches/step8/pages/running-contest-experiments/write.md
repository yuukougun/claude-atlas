# write.md：running-contest-experiments（執筆）

## 書いたファイル

- `docs/contest/running-contest-experiments.md`（`stubs/contest/` から移した。stage は draft）
- front matter で変えたキー：`sections`（「先に整える守り」`guards`・「手順の流れ」`steps`・「確かめ方」`check`・「失敗したとき」`when-it-fails` を足した。既存 5 節の anchor は変えず）・`sources`（既存の id 3 つ：terry-ahc040・kiri8128-relative-score-ahc・nvidia-winning-kaggle-competition-generative-ai）・`stage`・`updated`（2026-11-05）
- `snippets/running-contest-experiments/runner-request.md` と `.expect.yaml`（prompt。目次の templates は「なし」。実行器と集計を作らせる依頼を足した）
- `snippets/running-contest-experiments/win-rate-interval.py` と `.expect.yaml`（other。勝率の 95% 区間と見分けに要る試合数。手元で 4 通り実行して、expect の値と一致を見た）
- `data/sources.d/running-contest-experiments.yml` は作っていない（新しい出典がないため）

## 必ず持つものの対応

- 手順：`steps`（6 段、各段に終わりの確かめ）と、各段の本体の節 `more-cases`・`aggregation`・`games-for-win-rate`・`parameters-by-input`・`keep-all-runs`
- 確かめる・縛るのページへの道：`guards`（experiment-log・evaluators-by-format・selection-pressure・lockbox-and-holdout・open-ended-loop-trap・parallel-and-loop-costs へ link）。front matter の前提（experiment-log・evaluators-by-format）が比例則を満たす
- level：front matter に「仕組みにする」（変更なし）
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：`guards` → `steps` → 5 節 → `check` → `when-it-fails`

## メインに判断してほしいこと

- 資料にした 2 つのドメインが noai（threadreaderapp.com・chessprogramming.org）なので、Psyho の「2,000〜5,000 ケース」と SPRT の出典は引かなかった。前者は名指しせず「上位者の経験則」（根拠：弱）とし、出典の id は付けていない。後者は「境界を事前に決めた逐次の検定」と一言だけ書いた
- Halite III で 3 位の参加者の事例は、recursive.cc を `check_noai.py` で 2 回確かめたが「取得できない: timed out」で、確かめ済みにできなかったので、事例は載せず、対戦型への当てはめは（類推）の一般論にした。確かめが通れば、事例と出典を足せる

## 提案

```yaml
frontmatter: []
```

数値の提案はなし（本文の数値は、研究・解説の時点の記録と、二項分布の計算値。facts に置く変わりやすい値は書いていない）。

## 検査の結果

- 1 回目：エラー 0・警告 9（目印を 1 行ずつに置いていない 4 件・textlint 5 件）。2 回目（直した後）：エラー 0・警告 2
- 残した警告 2 件（textlint の no-doubled-joshi、58 行と 87 行）：link の目印の間に道具が入れる題名（「…が一致するテスタ」「…が膨らむ掛け算」）の中の「が」と、本文の「が持つ」「が」を二重と数えた誤検出。本文側は「が」を 1 回しか使っていない

## 確かめていないこと

- 本文の事実は、束の材料（research/10 第9章・11・24 B-53）に基づく。一次の記事（AHC040 の解説・相対スコアの解説・NVIDIA の記事）は開いていない。Web の取得は 0 回
- 勝率の数値は束の検算済みの値（標準誤差 0.0497・0.0249、下限約 50.1%）を使った。「約 2,400 試合（勝率 52%）」「半幅 ≈ 1/√n」は自分で計算した値で、`win-rate-interval.py` の出力と一致を見たが、他の担当は確かめていない
- 相対スコアの集計の表（3 行）と「基準の版で代用する」は、この辞典の推奨（推論）で、各大会の式は確かめていない
- 雛形 runner-request.md は、Claude Code で動かしていない

## 使用量

- 道具の呼び出し：約 20 回（Read 4・Bash 約 9・Write 6・Edit 1）。Web の取得：0 回（`check_noai.py` は 2 回）
