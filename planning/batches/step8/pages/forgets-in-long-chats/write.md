# write.md：forgets-in-long-chats（執筆）

## 書いたファイル
- docs/symptoms/forgets-in-long-chats.md（stub から移した。stage: draft、updated: 2026-11-05）
- front matter で変えたキー：`sections`（forms・routes-to-fixes・lookalikes・example・outdated・prevention を足した。diagnosis は据え置き）、`sources`（cc-docs-how-claude-code-works・cc-docs-best-practices・cc-docs-large-codebases・cc-docs-context-window）、`stage`、`updated`
- snippets/forgets-in-long-chats/premises-check.txt と premises-check.expect.yaml（前提を列挙させる依頼。目次の templates は「なし」だったが、診断の確かめに要るので足した）
- data/sources.d/forgets-in-long-chats.yml は作っていない（出典はすべて既存の id）

## 必ず持つものの対応
- 診断のチェックリスト（6 つの原因を安く確かめる順）：`#diagnosis`（見えていない → 散らかっている → 人の側）。このページの prevents は 2 原因だけなので、その 2 つと人の側を置いた
- 人の側の落とし穴：`#diagnosis` の 3 番目（six-causes#human-side を指す）
- 原因ごとの振り分け先（routes）：`#routes-to-fixes`（`routes` の目印）
- 型の構成の目安：要点 → `#forms` → `#diagnosis` → `#routes-to-fixes` → `#example` → `#prevention`。`#lookalikes` と `#outdated`（台帳 2 行）は足した

## メインに判断してほしいこと
- 診断の人の側の項目は、five の落とし穴の中身を束で見ていないため、特定の落とし穴の名を挙げず「前提が文面にない・後の指示と食い違う」と書いた。six-causes の内容と合うか確認してほしい
- `outdated-advice-ledger` ページは準備中のため、台帳の 2 行を link の目印で指した

## 提案
なし（数値・front matter・用語集への提案はない）。

## 検査の結果
- 1 回目：エラー 0・警告 5。直した後の 2 回目：エラー 0・警告 2（max-ten は直った）
- 2 回目の後に、残った警告 2 件（no-doubled-joshi：診断 3 の「は」、台帳の節の「に」）を文言を替えて直した。3 回目は流していない（回数の決めのため）。メインの一括検査で確かめてほしい

## 確かめていないこと
- 雛形 premises-check の動作（実際に会話で試していない）
- API の面の「履歴は呼び出す側が毎回送る」は一般の知識で、束の出典（api-docs-context-windows）を開いて確かめていない
- アプリの自動管理・`/context` の見方は、リンク先のページの内容を信じて書いた（本文では詳細を繰り返していない）
- Web の取得はしていない。出典の文言を一次資料で再確認していない（束の写しによる）
- 他の OS・IDE 拡張の動作は書いていない

## 使用量
- 道具の呼び出し：約 12 回、Web の取得：0 回
