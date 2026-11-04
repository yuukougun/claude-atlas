# write: uses-nonexistent-apis

## 書いたファイル
- docs/symptoms/uses-nonexistent-apis.md（stub から移して draft。front matter は sections〔forms・to-fixes・example・prevention を足した〕・sources〔9 件、すべて data/sources.yml にある〕・stage・updated だけ変更）
- snippets/uses-nonexistent-apis/read-then-write.{md,expect.yaml}（prompt）、new-dependency-rule.{md,expect.yaml}（claude-md）
- data/sources.d/uses-nonexistent-apis.yml は作っていない（新しい出典なし）

## 必ず持つものの対応
- 診断のチェックリスト（原因を安く確かめる順）：#diagnosis（見えていない→版→確かめ→境界の 4 項目、人の側の落とし穴は末尾の段落で six-causes を指す）
- 原因ごとの振り分け先（routes）：#to-fixes（routes の目印）
- 構成の目安の「よくある形」：#forms／「判断例」：#example／「予防（仕組みに移す）」：#prevention

## メインに判断してほしいこと
- 「知識の古さ」は六つの原因の名前が束にない（prevents は 3 つ）ため、診断の 2 番目に「版が合っているか」として置いた。六つの原因の並びと名前が site.yml と合うか見てほしい。
- 診断の 2 番目は routes に行き先がなく、前提と doesnt-know-latest#diagnosis を本文で指した。routes に knowledge-cutoff 等を足す案は出していない。

## 提案
- 用語集・prh・data への提案なし。front matter の提案なし。

## 検査の結果
- 1 回目：エラー 0・警告 5。直した後の 2 回目：エラー 0・警告 2（長文 1、「出力を実行」の冗長表現 1）。
- 2 回目の後に、その 2 つの警告の文だけを直した（再検査はしていない。回数の決めのため）。

## 確かめていないこと
- 雛形 2 つの動作（未実行）。
- 最後の文の直しによる警告の解消（再検査なし）。
- 研究の数値は束の写しによる。一次資料は開いていない。SimdBench の対象モデルは束にないため書いていない。
- 「型のある言語で編集後の型エラーが返る」は束の写し（公式の costs・best-practices）による。

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回。
