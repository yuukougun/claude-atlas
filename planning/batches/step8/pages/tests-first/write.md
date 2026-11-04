# tests-first 執筆報告

## 書いたファイル
- docs/verify/tests-first.md（stub から mv。stage を draft、updated を 2026-11-05）。front matter で変えたキー：sections（5 節に増やした。既存の steps・review-test-changes の anchor は変えていない）・sources（既存の cc-docs-best-practices・harper-basic-code・dolthub-claude-code-gotchas）・stage・updated
- snippets/tests-first/request.txt、request.expect.yaml（目次の templates の案 1 つ）
- data/sources.d/tests-first.yml（新しい出典はなく `sources: []`）

## 必ず持つものの対応
- 手順：steps（5 段。各段に確かめを付けた）
- 確かめる・縛るのページへの道：前提の define-done（要点の前提・guards-first）、protect-tests（guards-first・review-test-changes）、pitfalls-of-ai-written-tests（steps・verify）、verification-ladder・test-the-verifier（verify）。front matter の prerequisites と related にも全部ある
- level：任せる（front matter のまま）
- 構成の目安：要点 → guards-first（先に整える守り）→ steps → review-test-changes → verify（確かめ方）→ when-it-fails（失敗したとき）。振り分け先の routes はなし（束のとおり）なので、症状は本文から fix-a-bug・spec-first へ指した

## メインに判断してほしいこと
- when-it-fails の末尾の段落（実践者の報告を（根拠：弱）で一文）は、一次資料を開かず、束の 03 W7 の写しだけに基づく。残すか削るか
- 5 節の追加（guards-first・verify・when-it-fails）はカード §3 の「型の構成は目安」に従った

## 提案
なし

## 検査の結果
- check_page.py：書いた直後に エラー 1・警告 2（hook の表記・助詞「に」の重複 2 件）→ 直して エラー 0・警告 0

## 確かめていないこと
- 雛形の動作（実機で試していない）
- 「テストを人が直して意図を示すほうが効く」（束 04 Q2）は、根拠の出典が sources になく、本文に入れなかった
- 公式 Best practices の現行の版との突き合わせは、束の 00 の記述（検証の段階）だけに頼った。Web は取得していない
- 実在の docs/verify の他ページとの重複（define-done や protect-tests の本文との言い回し）は読んでいない

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
