# write.md：old-advice-doesnt-work

## 書いたファイル
- `docs/symptoms/old-advice-doesnt-work.md`（stub を mv。front matter の変更：stage を draft、updated を 2026-11-05、sources に cc-docs-best-practices・cc-changelog・cc-docs-changelog・cc-docs-commands、sections に forms・ask-claude・example・prevention を足した）
- `snippets/old-advice-doesnt-work/check-article.md` と `.expect.yaml`（目次の templates は無いので、分かりやすさのために足した依頼の雛形 1 つ）
- `data/sources.d/` は新しい出典がないので作っていない

## 必ず持つものの対応
- 冒頭の要点：先頭の `!!! abstract "要点"`（anchor なし）
- 診断のチェックリスト（原因を安く確かめる順。人の側の落とし穴も）：`#diagnosis`（番号付き 6 項目。人の側の落とし穴は同節の小見出し「人の側の落とし穴」）
- 原因ごとの振り分け先（routes）：`#diagnosis` の末尾の `gen:begin routes`
- 構成の目安のうち、よくある形は `#forms`、判断例は `#example`、予防は `#prevention`
- 六つの原因を全部並べてはいない：prevents が「確かめていない」「合っていない」の 2 つだけなので、この 2 つに絞り、他の原因は doesnt-know-latest・seems-less-capable・six-causes への案内にした

## メインに判断してほしいこと
- 台帳の行ごとの節（`outdated-advice-ledger#<行の id>`）は束の「指せる節」にないため指さず、台帳の入口と `#find-in-your-setup` を指した。カード §11 は行の id で指すとあるので、指せる節が増えたら差し替えるか判断してほしい
- 判断例は `/agents` を使った。台帳の行の内容（作成の画面が撤回）に基づく。版の数値は本文に書いていない

## 提案
なし（front matter・用語集・数値への提案は無い）

## 検査の結果
- 1 回目：エラー 1（要点の前提は「なし」と書く）・警告 8。直した
- 2 回目：エラー 0・警告 1（`no-doubled-joshi` の「が」、line 74）。その後、文を「名前は残っていても、指す先の機能が変わる」に直したが、再検査はしていない
- 回数の超過：1 回目の修正の途中で、置換スクリプトが失敗した（何も書かれていない）のに検査が続けて流れ、検査が合計 3 回流れた

## 確かめていないこと
- 公式の文書そのものは開いていない。束の data（台帳の行・names）だけに基づく
- Desktop の予定のタスクや `/loop` が、クラウドの予定のタスクと別の機能であるという記述は台帳の how_to_find に基づき、一次資料では確かめていない
- 雛形の動作は未確認
- 描画の確認（生成後の見た目）はしていない

## 使用量
- 道具の呼び出し：約 14 回（Read 4・Bash 6・Write 4）、Web の取得：0
