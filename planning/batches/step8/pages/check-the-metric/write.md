# write.md：check-the-metric（執筆）

## 書いたファイル
- docs/eval/check-the-metric.md（stubs から mv。stage draft、updated 2026-11-05）
  - front matter で変えたキー：`sections`（5 節に。mismatch はそのまま）・`sources`（3 件）・`stage`・`updated`
- snippets/check-the-metric/metric-check-request.md と .expect.yaml（目次の templates は「なし」。分かりやすさのために 1 つ足した）
- data/sources.d/check-the-metric.yml（新しい出典 2 件と、domains 2 件〔openai.com・cvpr.thecvf.com。check_noai.py で noai の指定なしを確認〕）
- 図は置かなかった（比喩付きの図は、薄くなるので省いた）

## 必ず持つものの対応
- どの原理に関わるか（`principle`：握る・確かめる）：`#why`（握る＝何を上げるかを決める権限）・`#what-it-affects`（握る・確かめる）
- どの原因に関わるか（`prevents`：確かめていない）：`#what-it-affects`
- `pitfalls`：空なので持たない
- level（任せる）・要点の最初が「何が分かるか」：冒頭の囲み
- 構成の目安：何が起きるか＝`#mismatch`、なぜ＝`#why`、頼み方の技法（Before/After 相当の雛形と判断例）＝`#check`、何に効くか＝`#what-it-affects`、誤解＝`#misconceptions`、関連＝テンプレート

## メインに判断してほしいこと
- OpenAI の出典（openai-expanding-on-sycophancy）：取得が 403 で本文を開けなかった。題名「Expanding on what we missed with sycophancy」と公開日 2025-05-02 は記憶による仮のもの。本文の記述は調査資料（10-contest-supplement.md）の要約に拠る。メインが開いて、題名・日付・内容（オフライン評価と A/B テストが良かった、専門テスターの懸念、ロールバック）を確かめてほしい
- CVPR の出典：published の `2023-06-01` は仮の値（大会の年から）。題名と要旨はポスターのページで確かめた
- 既存の出典の lukyanenko-kaggle-antigravity-s6e7 は開いていない（束と調査資料に拠る）。「accuracy と balanced accuracy」「CV 0.967・LB 0.874」を、ブログで確かめてほしい。本文の根拠の印は（根拠：弱）にした（材料は弱〜中）
- カード §1 は sources を「既にある id だけ」としているが、新しい出典 2 件を sources.d に足して sources に入れた（カード §8 の「新しい出典は sources.d」に従った）

## 提案
- 数値の提案なし。本文の数値（0.967・0.874・80 件・2025 年 4 月）は研究の時点の固定の記録として扱った（カード §7）
- front matter の提案なし。用語集・prh への提案なし

## 検査の結果
- check_page.py：1 回目 エラー 2（domains 未記載）・警告 9。直した後の 2 回目 エラー 0・警告 0

## 確かめていないこと
- 雛形の動作（返答の形）は試していない
- 事例 3 件の内容は、束の写しと、CVPR のポスターのページの要旨だけで確かめた。OpenAI と Kaggle のブログは本文を読んでいない
- link の先の節の中身（define-done・read-specs-yourself など）は、題名と要約だけで、本文は読んでいない
- 判断例（緊急の問い合わせの分類器）は想定の場面で、実在の事例ではない

## 使用量
- 道具の呼び出し：約 30 回、Web の取得：2 回（OpenAI は 403、CVPR は成功）
