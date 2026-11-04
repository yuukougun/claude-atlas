# write.md：secrets-exposed

## 書いたファイル
- `docs/symptoms/secrets-exposed.md`（stubs から mv。雛形・図・sources.d は置かない）
- front matter で変えたキー：`sections`（forms・example・prevention を足した。first-response・diagnosis は据え置き）、`stage`（draft）、`updated`（2026-11-05）、`sources`（cc-docs-best-practices・cc-docs-data-usage・cc-docs-permissions・cc-docs-sandboxing・cc-docs-security。いずれも既存の id）

## 必ず持つものの対応
- 診断のチェックリスト（原因を安く確かめられる順。人の側の落とし穴も）：`#diagnosis`（項目 1 が出どころ、2 が縛っていない、3・4 が境界がない、5 が人の側）
- 原因ごとの振り分け先（routes）：`#diagnosis` の末尾の routes の目印（見出しは立てず、診断の節の一部にした）
- 冒頭の要点：最初の `##` より前の囲み
- 漏れた直後の初動（目次の備考の指定）：`#first-response`（貼った鍵・手元の記録・/feedback と共有リンクの確認を含む）
- 型の構成のうち、よくある形：`#forms`／判断例：`#example`／予防：`#prevention`

## メインに判断してほしいこと
- `#diagnosis` の項目 2 に、`git add` を許す規則と `.gitignore` の有無を見る、と書いた。束に出典がなく、一般の実務の知識である。要出典の扱いにするか、削るかを決めてほしい
- `#first-response` の「履歴から消す書き換えはキーの無効化の代わりにならない」も同じく一般の実務の知識で、束に出典はない
- `#prevention` のアプリのタブは「アプリでの同等の設定は未確認」と書いた。アプリ側の材料が束になかったため

## 提案
- なし（数値・用語集・data への提案はない。本文に変わりやすい値は書いていない）

## 検査の結果
- 1 回目：エラー 0・警告 2（max-ten、no-doubled-joshi）。直した
- 2 回目：エラー 0・警告 1（no-doubled-joshi。リンクの題名の「で」と重なった）。この警告は文を直したが、3 回目は流していない（回数の決まりのため）

## 確かめていないこと
- 2 回目の直しの後の再検査（警告 1 が消えたか）
- 診断の各項目の「偽のファイルで試して止まるか」は、手を動かして確かめていない
- 公式の文書の原文は開かず、束の写しだけに基づく。Web の取得は 0 回
- `/permissions` で設定を見られることは、束の data の names に基づく

## 使用量
- 道具の呼び出し：約 10 回。Web の取得：0 回
