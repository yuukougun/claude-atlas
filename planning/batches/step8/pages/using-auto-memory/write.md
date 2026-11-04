# write：using-auto-memory（自動メモリ）

## 書いたファイル
- docs/extend/using-auto-memory.md（stubs から移した。stage を draft、updated を 2026-11-05、sources を [cc-docs-memory, cc-docs-context-window]、sections を 5 節に。既存の anchor `review` は維持）
- snippets/using-auto-memory/review-prompt.md と review-prompt.expect.yaml（目次の templates の案：記録を一覧させ、誤りと古い記録を挙げさせるプロンプト）
- planning/batches/step8/pages/using-auto-memory/facts-proposal.yml
- data/sources.d/using-auto-memory.yml は書いていない（新しい出典なし。既存の cc-docs-memory・cc-docs-context-window を指す）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力）：#when の前、冒頭の要点の「強制力」（`gen feature enforcement`）。読み込みの時期は #when の `fact auto-memory-startup-load`。ほかの属性のバッジはテンプレートが出す
- tracks：front matter の `tracks: [auto-memory]`（変更なし）
- level：front matter の `level: 任せる`（変更なし）
- 構成の目安：要点→使いどころ #when→最小の使い方（面のタブ）#usage→雛形（#review の中）→効かない場面・落とし穴 #limits→比べる相手 #compare。古くなった助言は台帳の行がないので置かない

## メインに判断してほしいこと
- 面のタブは surfaces が claude-code だけなので、タブは「Claude Code」1 つだけにした。1 つだけのタブが不自然なら、通常の番号付き手順にしてよい
- 雛形（#review）は節 #review の中に置いた。#usage に移すかは任せる

## 提案
- data/facts.yml：ローカルのセッションでの既定の状態を数値ファイルに置く案（facts-proposal.yml）。本文は既定を書かず、「環境ごとに /memory のトグルで確かめる」にした。置かれたら #usage に目印を足す
- 用語集：特になし

## 検査の結果
- check_page.py を 2 回流した。最後はエラー 0・警告 3（no-doubled-joshi）。
- 警告のうち 2 件（152・155 行）は、link の目印が生成した題名つきのリンクの中の助詞で、手で直せない。1 件（157 行「既定の状態が違うことがある」）は残した

## 確かめていないこと
- 雛形の動作（実際の自動メモリで試していない）
- 公式の文書の記述（保存先・`autoMemoryEnabled`・`CLAUDE_CODE_DISABLE_AUTO_MEMORY`・`autoMemoryDirectory`・`modified` の項目・「Saved N memories」の表示）は、2026-11-05 に memory のページ 1 回の取得で確かめた。実機では見ていない
- ほかの OS と IDE 拡張の動作は未確認と本文に書いた
- 「単独の経験談」（誤った結論が後続の実験を汚染）は束の写し（11 p34#114）によるもので、元の記事は開いていない

## 使用量
- 道具の呼び出しは約 15 回、Web の取得は 1 回
