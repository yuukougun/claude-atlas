# write.md：not-what-i-meant（執筆）

## 書いたファイル

- `docs/symptoms/not-what-i-meant.md`（stubs から mv。stage を draft、updated を 2026-11-05、sources を 3 件、sections を 4 節に）
- `snippets/not-what-i-meant/restate-first.txt`・`.expect.yaml`（実行の前に理解と推測した点を書き出させる依頼）
- `snippets/not-what-i-meant/list-assumptions.txt`・`.expect.yaml`（外れた出力の直後に推測で埋めた点を挙げさせる依頼）
- 出典は既存の id（api-docs-prompting-best-practices・cc-docs-best-practices・arxiv-2403-08937）だけを使ったので、`data/sources.d/` は作っていない。図は置いていない（Before/After の図は four-specifics が持つ）

## 必ず持つものの対応

- 診断のチェックリスト（六つの原因を安く確かめる順）：`#diagnosis`（見えていない → 散らかっている → 合っていない。最後に人の側の落とし穴を six-causes#human-side へ）
- 人の側の落とし穴：`#diagnosis` の末尾の 1 段落で six-causes#human-side を指す。`pitfalls` は空なので、本文では詳しく書いていない
- 原因ごとの振り分け先（routes）：`#diagnosis` の末尾の `routes` の目印
- 構成の目安のうち、よくある形は `#forms`、判断例は `#examples`、予防は `#prevention`

## メインに判断してほしいこと

- 「回答が長すぎる・短すぎる」は、00 §4 では原因⑤（面・モデル）だが、front matter の `prevents` に「縛っていない」「効かせすぎ」などがないので、「見えていない」（形と分量の指定がない）と「合っていない」の両方で受けた。これでよいか
- 検査は 3 回流した（初回の警告 4 件、直して 1 件、さらに直して 0 件）。指示は 2 回だったので、超えた

## 提案

- なし（front matter のほかのキー・用語集・data への提案はない）

## 検査の結果

- 最後の `check_page.py`：エラー 0・警告 0

## 確かめていないこと

- 2 つの雛形の動作は試していない（動作確認の担当に任せる）
- 研究の割合（20.77%・15.27%）は束の写しに基づく。Web で確かめたのは arXiv の要旨（333 件・CodeGen・PanGu-Coder・Codex・2024 年）だけで、割合の値は本文で確かめていない
- 「訂正を重ねると外れた試みが次の答えを引きずる」は、束の rewind-dont-correct の要約に基づく。相手のページの本文は未確認
- 本文の `link` の節（`id#anchor`）は束の「指せる節」にあるものだけを使ったが、相手のページがまだ公開前のものが多い

## 使用量

- 道具の呼び出し：約 12 回（Read 3、Bash 7、Write 5 のうち report 含む）。Web の取得：1 回（arXiv の要旨）
