# write.md：suspect-too-good-results（良すぎる結果を疑う）

## 書いたファイル

- `docs/verify/suspect-too-good-results.md`（stubs から移した。stage を draft、updated を 2026-11-05、sources に arxiv-2607-07744・arxiv-2607-16241・arxiv-2605-21384、sections に why・what-it-affects・misconceptions を足した。既存の anchor と節は変えていない）
- `snippets/suspect-too-good-results/self-check-before-report.txt` と `.expect.yaml`（目次の templates の案。kind: prompt、safety: false）
- `data/sources.d/suspect-too-good-results.yml`（arxiv-2607-16241 の 1 件。KernelBench-Verified。要旨だけを WebFetch で確かめた）

## 必ず持つものの対応

- 冒頭の要点（何が分かるか・いつ引くか・前提）：冒頭の囲み。「何が分かるか」が最初の項目
- level（任せる）：front matter。変更なし
- principle「確かめる」を名指す：`#what-it-affects` の第 1 段落
- prevents「確かめていない」を名指す：`#what-it-affects` の第 1 段落
- pitfalls：front matter が空のため、本文で結ぶものはない（持たない理由）
- 構成の目安（何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：`#what-to-suspect` → `#why` → `#self-check`（技法の Before/After と判断例）→ `#what-it-affects` → `#misconceptions` → 関連はテンプレート

## メインに判断してほしいこと

- 束の 6.3 のとおり、「漏洩変数で QWK≈1.0、LB 0.44」の例は原典未確認なので、本文に使っていない
- 「2倍を超える向上」の目安は規則として書かず、「桁違い」「改善の幅が不自然に大きい」とした

## 提案

- 用語集・prh・data・front matter への提案はない

## 検査の結果

- 1 回目：エラー 0・警告 4。直した（読点の数・助詞の重複・冗長表現）
- 2 回目：エラー 0・警告 2。残り 1 件は生成された link の題「三層に分ける」と「にある」が重なる誤検出（生成物は手で直さない）。もう 1 件（行 54 の助詞「に」の重複）は 2 回目の後に文を直した。3 回目は流していない

## 確かめていないこと

- 雛形の動作（新しいセッションでの実行）は未確認
- 研究の数値は束の写しと、KernelBench-Verified の arXiv の要旨に基づく。PERFOPT-Bench と SpecBench は原典を開いていない（research/24 の訂正に従って書いた）
- 「作業者としての Claude は自分の出来を高く評価しがち」は束 6.2 の Anthropic Engineering の記述に基づく。出典の id がなく、sources に載せていない（根拠の印も付けていない）
- 行 54 の直した文の再検査

## 使用量

- 道具の呼び出し：約 14 回。Web の取得：1 回（arxiv.org/abs/2607.16241）
