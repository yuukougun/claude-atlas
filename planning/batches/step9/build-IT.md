# 工程9 IT の報告

## 作ったファイル（planning/batches/step9/issue-template-draft/）
- report-error.yml、case-suggestion.yml、config.yml、README.md

## 作者の承認が要る文
詳細は README.md。要点：
- report-error の冒頭1行目、種類の選択肢、任意の2欄の名と説明、確認のチェック
- case-suggestion の「返事、採否、反映の時期は約束しない。…そのままページにするとも約束しない。」、各欄の名と説明、確認のチェック
- 返事と直す時期、公開、書かない情報の文は承認済みの文の再掲

## メインに判断してほしいこと
1. tools/gen/config.yml の `report_template` が未設定。`report-error.yml` を置くか（置かないと画面のリンクは欄に入らず本文に入る）。
2. config.yml は白紙の Issue を許さない案。許す場合は true にする。
3. 確認のチェックを必須にしてよいか（報告の手間が増える）。
4. 種類の「情報が古い」は design §9.5 による。ラベルは付けていない（存在しないラベルの扱いを避けた）。

## 数
- Web の取得：0（Issue forms の書き方は既知の形で、公式の文書は開いていない。構文は未検証なので、置いた後に GitHub 上で確認が要る）
- 道具の呼び出し：約 8 回（読み取り 2、書き込み 5）
