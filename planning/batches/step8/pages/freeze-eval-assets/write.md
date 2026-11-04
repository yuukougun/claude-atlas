# write.md：freeze-eval-assets（recipe・enforce）

## 書いたファイル
- `docs/enforce/freeze-eval-assets.md`（stubs から mv。stage を draft、updated を 2026-11-05、sources を [cc-docs-permissions, cc-docs-sandboxing] に）
- front matter の sections を 3 → 5 に（`before-freezing` と `when-it-fails` を足した。既存 3 つの anchor は不変）
- `snippets/freeze-eval-assets/freeze-settings.json`・`.expect.yaml`（kind settings、safety true。目次の templates の案）
- `snippets/freeze-eval-assets/freeze-canary-check.md`・`.expect.yaml`（kind prompt、safety true。分かりやすさのために足した、見張りのファイルで凍結を確かめる依頼）
- `data/sources.d/` は作っていない（出典 2 件は data/sources.yml にある）

## 必ず持つものの対応
- 用途ごとの進め方（手順）：`how-to-freeze`（手順 1〜6、各段に「終わりの確かめ」）
- 確かめる・縛るのページへの道：`before-freezing`（確かめる：verifier-three-conditions#audit・test-the-verifier#freeze・single-scorer）、`how-to-freeze`・`what-to-freeze`（縛る：sandboxing・permission-rules・protected-paths・lockbox-and-holdout・hook-recipes）。front matter の prerequisites・related にも全部ある
- level：仕組みにする（front matter のまま）
- 構成の目安（要点 → 先に整える守り → 手順 → 確かめ方 → 失敗したとき）：冒頭の要点 → `before-freezing` → `what-to-freeze`・`how-to-freeze` → `check` → `when-it-fails`

## メインに判断してほしいこと
- 雛形の `sandbox.filesystem` のパスを `./eval` の形で書いた。公式（sandboxing）は「`.` は project settings では根に解決」と書くが、`./eval` のような相対パスの細部は、参照先の settings-reference の節を未確認。動作確認の担当に確かめてほしい。外れたら `/` 始まりの絶対パスを使う案に変える
- 第三者の実践例（評価指標のファイルを凍結し、編集してよいファイルを 1 つに限った自律研究の例）を、名指しせず（根拠：弱）で 1 文だけ書いた。束の材料（11 p34#12）に基づく。名前や出典の URL は調べていない。要らなければ削ってよい

## 提案
- 数値の提案はなし（版・既定値・上限は本文に書かず、目印も使っていない）
- front matter の提案：なし

## 検査の結果
- `check_page.py` を 2 回流した。最後は エラー 0・警告 3（すべて textlint の no-doubled-joshi「に」「も」）。かなり長い手順の 1 文に残った。意味を割らずに直せるかは検証側の判断に委ねる

## 確かめていないこと
- 雛形の設定と見張りの依頼を、実際の環境で動かしていない。サンドボックスの `denyWrite`・`denyRead` が子プロセスの書き込み・読み取りを止めること、`Edit` の deny が `eval/.freeze-canary.txt` の新規作成を止めることは、束の材料と公式の文書の記述に基づく
- 「公式は Read・Edit の deny がサンドボックスの設定にも合わさると書く」は、束の research/23 #5 の記述に基づく。一次資料で原文を確かめていない
- 同じ利用者が OS のファイルの権限を付け直せること（手順 6 と表）は、一般的な Unix の挙動として書いた。一次資料はない
- 手順 5 のフックの注意は、束の材料（11 #19：jq がないと fail-open）に基づく。WSL・Linux 以外の動作は未確認
- 本文の `Write(...)` のルールが何にも当たらない記述は、束の research/23 #4 と research/28 #11 に基づく

## 使用量
- 道具の呼び出し：約 15 回。Web の取得：1 回（sandboxing の filesystem のパスの書き方）
