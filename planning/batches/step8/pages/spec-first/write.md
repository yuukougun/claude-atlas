# spec-first 執筆報告

## 書いたファイル
- docs/recipes/spec-first.md（stubs から mv。stage: draft、updated: 2026-11-05。front matter の変更は sections に guards-first・verify・when-it-fails の 3 節を足したことと、sources に cc-docs-best-practices・cc-docs-goal・cc-docs-permission-modes・cc-docs-tools-reference・arxiv-2403-08937 を入れたこと）
- snippets/spec-first/spec-outline.md・mock-request.txt・fresh-session-start.txt と、それぞれの .expect.yaml
- docs/img/spec-first/flow.svg
- 本文は、目次の templates の 3 案のうち A-6 は let-claude-ask/interview-feature、A-14 は goal-until-done/stop-condition を、他ページの雛形のまま取り込んだ

## 必ず持つものの対応
- 手順：guards-first（先に整える）→ interview → what-goes-in-the-spec → mock-first → implement-fresh → goal-with-stop-conditions。各段に「終わりの印」を置いた
- 確かめる・縛るのページへの道：guards-first（define-done・state-the-scope）、goal-with-stop-conditions（tests-first・define-done）、verify（does-more-than-asked）。front matter の前提に define-done、関連に state-the-scope・tests-first がある
- level：任せる（goal-with-stop-conditions だけ仕組みにする）
- 構成の目安：要点 → guards-first → 手順 → verify → when-it-fails

## メインに判断してほしいこと
- mock-first は、束にモックの根拠の資料がない。「この辞典の推奨（推論・実践例なし）」と書いた。必須ページの題名に入る節なので、根拠の資料を足すか、節を軽くするかの判断がほしい
- 他ページの雛形（let-claude-ask/interview-feature、goal-until-done/stop-condition）を `gen:begin snippet` で取り込んだ。生成は通ったが、別ページの snippet を使う形がよいかの確認がほしい

## 提案
- 数値の提案なし。AskUserQuestion の 1 回の質問数は、本文に書かず、目印も使っていない
- 用語集・prh への提案なし

## 検査の結果
- check_page.py を 2 回流した。最後はエラー 0・警告 6（doubled-joshi 5・max-ten 1）
- 警告のうち 3 件（54・56・58 行）は、生成された link の題名が入った行で、本文では直しにくい

## 確かめていないこと
- Tambon らの研究の対象モデルは、束に書かれていないため「当時のコード生成モデル」とだけ書いた。公刊の年（2024）は arXiv の番号からの推定
- アプリで SPEC.md を渡す手順と、選択式の質問の出方は未確認と書いた
- 雛形 3 つは動かして確かめていない
- plan mode で計画の段を行う記述は、束の when-to-plan の要約に基づく。編集が止まる点以外の挙動は見ていない

## 使用量
- 道具の呼び出し 約 14 回、Web の取得 0 回
