# write.md：repeating-the-same-explanation

## 書いたファイル

- `docs/symptoms/repeating-the-same-explanation.md`（stubs から mv。stage を draft に）
- `snippets/repeating-the-same-explanation/inventory-request.md` と `.expect.yaml`（目次の雛形は「なし」。分かりやすさのために 1 つ足した）
- front matter で変えたキー：`sections`（forms・causes・examples・prevention・outdated を足した。diagnosis は変えず）、`stage`（draft）、`updated`（2026-11-05）、`sources`（cc-docs-features-overview・hc-personalization・hc-projects-what。既存の id だけ）
- `data/sources.d/` は作っていない（新しい出典なし）

## 必ず持つものの対応

- 診断のチェックリスト（原因を安く確かめる順。関われば人の側の落とし穴）：`#diagnosis`。人の側の落とし穴は、`pitfalls` が空なので節に置かず、末尾の段落から six-causes#diagnosis へ指した
- 原因ごとの振り分け先（`routes`）：`#causes`（`routes` の目印）。診断の各項からも、見えていない・縛っていないの別に振り分けた
- 構成の目安の「よくある形」：`#forms`／「判断例」：`#examples`／「予防（仕組みに移す）」：`#prevention`

## メインに判断してほしいこと

- 診断の 1 項目目と末尾の段落に「書いてあるのに守られない」「毎回変わる部分」の確認を置いた（原因 2 つ以外の切り分け）。症状の言い換えと重なる所なので、不要なら削る
- 「回数を目安にした足し方」は when-to-add-what に任せ、公式の表の回数（2 回・3 回）は本文に書かなかった（数値の id がないため）

## 提案

- 数値の提案：なし
- 雛形の `control` は私の推測の書き方（「返りやすい」）。動作確認の担当が試すまで記録として扱う

## 検査の結果

- `check_page.py` 1 回目：エラー 0・警告 6（に の重複 4・読点 4 つ以上 1・「六つ」1）。直して 2 回目：エラー 0・警告 0

## 確かめていないこと

- 雛形の動作（実機で試していない）。`control` の内容は未確認
- 本文の置き場所の説明（Claude への指示・プロジェクトの指示・スキルの効く範囲）は束の要約と data の note による。一次資料は開いていない
- アプリのメモリを「Claude が覚える仕組み」とだけ書いた。自分で内容を決める置き場所にできるかは確かめていない
- `where-instructions-sit#why`・各 `id#anchor` の先の本文は読んでいない（束の節の題名だけを根拠にした）
- 画面での見え方（タブ・囲みの表示）は未確認

## 使用量

- 道具の呼び出し：約 10 回（Read 4・Bash 4・Write 3 ほか）。Web の取得：0
