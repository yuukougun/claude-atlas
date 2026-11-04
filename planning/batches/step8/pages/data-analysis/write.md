# write.md：data-analysis（データを分析する）

## 書いたファイル
- `docs/recipes/data-analysis.md`（stubs から mv。stage を draft、updated を 2026-11-05、sections に `guards`・`how-to-check`・`when-it-fails` を足した。既存 3 節の anchor は変えず）
- `snippets/data-analysis/observe-and-hypothesize.{txt,expect.yaml}`（目次の templates の A-8）
- `snippets/data-analysis/aggregate-request.{txt,expect.yaml}`（分かりやすさのために足した）
- `data/sources.d/data-analysis.yml` は作らない（sources は空のまま。公式文書の出典は link 先のページが持つ）

## 必ず持つものの対応
- 手順：`#reproducible-queries`（4 点を決めて頼む）・`#check-raw-data`（段ごとに終わりの確かめを付けた 5 段）
- 確かめる・縛るのページへの道（比例則）：`#guards`（entrusted-data・where-your-data-goes・character-encodings・evidence-not-reports・ask-without-sycophancy を先に示す）。前提と関連にも front matter で持つ
- level：任せる（front matter のまま）
- 構成の目安：要点 → `#guards` → `#reproducible-queries`・`#check-raw-data`・`#observation-vs-interpretation`（手順）→ `#how-to-check` → `#when-it-fails`

## メインに判断してほしいこと
- A-8 の雛形は、目次では prompting の prompt-patterns と「snippets の1か所から取り込む」とある。prompt-patterns のページはまだ snippets にないので、この `snippets/data-analysis/observe-and-hypothesize` を正本にした。prompt-patterns の担当に、同じ id を gen の目印で取り込むよう伝えてほしい
- 目次の材料 6.3（ML のリーク、パイプラインの 50%）は、二次要約で原典未確認のため本文に書かず、audit-ml-pipelines と suspect-too-good-results へ link するだけにした

## 提案
```yaml
frontmatter: []
```
用語集・prh・data への提案はなし。変わりやすい値は本文に書いていないので facts-proposal.yml も作らない。

## 検査の結果
- `check_page.py data-analysis` 1 回：エラー 0・警告 0

## 確かめていないこと
- 雛形 2 つの動作（expect の内容）は、実際の Claude で試していない
- 「再実行すると数字が変わる」の確認点（入力の更新・除外条件の曖昧さ）は、一般的な見立てで、一次資料では確かめていない
- 「アプリでは隔離された環境でコードを実行して集計できる」は束の files-and-code-execution の要約に基づく。Claude Code の節は WSL・Linux 以外の動作を確かめていない
- textlint が検査しない囲み内の字下げ段落（要点・判断例・タブ）は、目で読んだだけ
- link の節（`id#anchor`）は束の「指せる節」から選んだが、相手のページ本文の内容は読んでいない

## 使用量
- 道具の呼び出し：約 12 回（Read 4・Bash 5・Write 7 を含む）、Web の取得 0 回
