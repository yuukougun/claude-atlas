# write.md：github-actions-with-claude（feature・delegate）

## 書いたファイル

- docs/delegate/github-actions-with-claude.md（stubs から mv。stage draft、updated 2026-11-05）
- snippets/github-actions-with-claude/minimal-workflow.yml と .expect.yaml
- snippets/github-actions-with-claude/scheduled-report.yml と .expect.yaml
- front matter で変えたキー：sections（when・minimal・templates・pitfalls・compare・outdated を足した。既存 3 つの anchor は不変）、sources（既存の 4 id）、stage、updated
- data/sources.d/github-actions-with-claude.yml は書いていない（新しい出典なし。束の 4 つの id はすべて data/sources.yml にある）

## 必ず持つものの対応

- 機能の属性のバッジ：テンプレートが出す。本文には成熟度を `feature github-actions/maturity` の目印で 1 か所（冒頭の導入）。強制力は、機能の項目に enforcement の属性がないため目印を使わず、要点の「強制力」の行に文で書いた
- tracks（github-actions）：front matter に既にある。ページ全体
- 使いどころ（どの原因を防ぐか）：#when
- 最小の使い方（面のタブ）：#minimal（surfaces は claude-code のみで、タブは「Claude Code」の 1 つ）。動き方の選び方は #modes
- 雛形：#templates（2 つ）
- 効かない場面・落とし穴：#pitfalls、外の人の本文は #untrusted-input
- 比べる相手：#compare
- 古くなった助言：#outdated（台帳への link を置いた）
- level：回す（front matter 既存）

## メインに判断してほしいこと

- 雛形の扱い：カード §10 は「GitHub Actions は試せない雛形なので載せず、条件と概念だけ」、brief §3 と目次は「雛形は載せる・最小権限の workflow を載せる」。目次と brief を優先して 2 つ載せた（折りたたみ・未確認の旨は道具が書く）。載せない方針なら、#templates の節を外し、expect を消す
- minimal-workflow の `permissions` は公式の例のとおり（contents は write）。目次の題は「最小権限」だが、Action が既定で GitHub App として認証するため、`permissions` を read に絞った効果は確かめていない。雛形の題は「最小権限の workflow（@claude に応える）」のまま。題を直すかどうか
- 要点の「強制力」の行は、`permission-modes/enforcement` のような目印を使わず文で書いた。github-actions の機能に強制力の属性を足す提案をするかどうか

## 提案

```yaml
frontmatter: []
```

- 用語集：なし。数値の提案：なし（本文に変わりやすい値の手書きはない。例の値は雛形のコメントに「例」と明記）
- 機能 github-actions の enforcement を data に足す案（値は鍵・お願いの混在のため、メインの判断）

## 検査の結果

- check_page.py を 2 回流した。最後はエラー 0・警告 10
- 警告はすべて textlint の ja-technical-writing（助詞「に」「で」「が」の重なり 9、1 文の長さ 1）。リンクの目印の間に道具が入れる題名が長く、その中身が文を長くする（165 行）。それ以外は自分の文で、意味を変えずには短くしにくいため残した
- 初回のエラー 6 は prh の「skill／plugin」。スキル・プラグインに直した

## 確かめていないこと

- 雛形 2 つの実際の動作（GitHub 上で動かしていない）。`concurrency` の group の式と `timeout-minutes` は、公式の例にないため未確認
- `permissions` を絞ったときの実際の効き方（GitHub App の権限との関係）
- 公式の文書は 1 回だけ取得した（2026-11-05）。GitHub 側の文書（security.md など）は開いていない。fork の PR で secrets が渡らないのは、公式のページの記述（review の workflow の節）による
- `bare-mode` と Action の組み合わせの動作（本文でも未確認と書いた）
- 定時の実行が動きのない期間で止まる件は、公式の記述のみ（期間の値は書いていない）
- 他の OS のランナーや GitHub Enterprise Server の扱い

## 使用量

- 道具の呼び出し：約 16 回、Web の取得：1 回
