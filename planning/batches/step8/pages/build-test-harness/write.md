# write.md：build-test-harness

## 書いたファイル

- `docs/recipes/build-test-harness.md`（`stubs/recipes/` から `mv`）。front matter の変更は `sections`（`guard-first` と `when-it-fails` を足した。既存の 3 つは変えていない）・`stage`（draft）・`updated`（2026-11-05）だけ
- `snippets/build-test-harness/repo-layout.txt`・`.expect.yaml`（kind: other。目次の「検証の資産を分けたリポジトリの構成例」）
- `snippets/build-test-harness/build-harness-request.txt`・`.expect.yaml`（kind: prompt、open: true。目次の「検証環境を作らせる依頼の型」）
- 出典のファイル（`data/sources.d/build-test-harness.yml`）は置かない。`sources: []` のまま

## 必ず持つものの対応

- 手順：`what-to-build`（5 段、各段に「確かめ」）
- 確かめる・縛るのページへの道：front matter の `prerequisites`（verifier-three-conditions）と `related`。本文では `guard-first`（verifier-defines-problem・verifier-three-conditions・freeze-eval-assets）、`check-the-harness`（test-the-verifier・pitfalls-of-ai-written-tests）、`separate-eval-assets`（lockbox-and-holdout・freeze-eval-assets）
- level：front matter の `level: 任せる`（変えていない）
- 構成の目安（先に整える守り → 手順 → 確かめ方 → 失敗したとき）：`guard-first` → `what-to-build` → `check-the-harness` → `separate-eval-assets`（置き場所の守り）→ `when-it-fails`

## メインに判断してほしいこと

- 図の案（解・評価・記録を分けた構成図）は描かず、同じ内容を雛形 `repo-layout` で出した。図が要るなら別途
- `separate-eval-assets` は「縛る」の置き場所の話で、実際の止め方（deny・サンドボックス）は freeze-eval-assets へ送った。節の順は目安から少し外し、守りの節を先頭に足した

## 提案

- 用語集・数値・front matter の提案はなし

## 検査の結果

- 1 回目：エラー 0・警告 5（no-doubled-joshi）。直して 2 回目：エラー 0・警告 3
- 残した警告（no-doubled-joshi。68 行・105 行・108 行の展開後の行番号）：リンクの目印が展開されて題名が入った行で、助詞の連続を数えている。書き手の文は短く切ったが、2 回の上限に達したため再確認していない。検証の担当が直してよい

## 確かめていないこと

- 雛形 2 つの動作（動作確認はしていない。expect は想定）
- 並列の実行で出力先を分ける、一時ファイルが衝突しやすい、という記述は、束にない一般の知識で書いた。出典を付けていない
- 研究由来の数値（ImpossibleBench・Psyho・採点バグの割合など）は、出典を用意しない方針で本文に載せていない
- 冒頭の「何ができるか」の文字数（90 字ほど）は検査に任せた

## 使用量

- 道具の呼び出し：約 14 回（Bash 5・Read 3・Write 6 に近い数。Edit 7 を含む）
- Web の取得：0 回
