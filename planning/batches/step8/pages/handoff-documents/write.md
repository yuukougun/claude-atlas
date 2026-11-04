# write.md：handoff-documents

## 書いたファイル
- docs/context/handoff-documents.md（stub から移動。stage を draft、updated を 2026-11-05、sections に guard・check・troubleshoot を足した。既存 4 つの anchor は不変。sources に既存 id 7 件を設定）
- snippets/handoff-documents/：handoff-request（prompt）・skill-handoff（skill）・resume-request（prompt）と各 expect.yaml
- data/sources.d は作っていない（新しい出典なし）

## 必ず持つものの対応
- 手順：four-items（書かせる・読んで確かめる）／where（置く）／resume（区切る・再開）。各段に「確かめ：」を付けた
- 確かめる・縛るのページへの道：guard（define-done・evidence-not-reports・promises-after-compaction を link）。front matter の related にも同じものがある
- level：任せる（front matter に既存）
- 構成の目安：要点 → guard → 手順（four-items/where/resume）→ check → troubleshoot（失敗したとき）→ vs-compact

## メインに判断してほしいこと
- 構成の目安（先に整える守りが先）に合わせ、順を guard 先頭にした。vs-compact は order を末尾にした（既存 anchor は変えていない）
- 分野の症状ページの id が束になく、troubleshoot は症状ページでなく概念ページへ振り分けた

## 提案
- なし（用語集・prh・data・front matter の提案はない）

## 検査の結果
- 1 回目：エラー 0・警告 4（max-ten 1・no-doubled-joshi 2・四つ 1）。直したのは「四つ」と文の分割
- 2 回目：エラー 0・警告 4（max-ten 1 件〔導入段落〕・no-doubled-joshi 3 件）。2 回の上限のため、残りは直していない

## 確かめていないこと
- 3 つの雛形の動作（実際に Claude で流していない）
- アプリで文書を持ち越す仕組み（Projects 等）。本文で未確認と書いた
- /resume で戻った会話が元の長さのままという記述は、/clear の data の note（前の会話は /resume で戻れる）からの推論
- 圧縮でファイルパスなどが変わりうる、という点は X4 の記述（実務家の経験談）で、一次資料では確かめていない
- PERFOPT-Bench は束の注記だけに基づき、論文は開いていない

## 使用量
- 道具の呼び出し 11 回前後、Web の取得 0 回
