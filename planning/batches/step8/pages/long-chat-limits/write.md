# write.md：long-chat-limits（執筆）

## 書いたファイル
- docs/app/long-chat-limits.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に hc-context-window・hc-usage-limits・hc-release-notes〔feature の出典と同じ既存 id〕を追加）
- sections を追加（既存の auto-management・at-the-limit は不変）：what-remains・effects・pitfalls・compare
- planning/batches/step8/pages/long-chat-limits/facts-proposal.yml
- 雛形・図・data/sources.d は無し（目次の templates が「なし」。コードの実行の設定は files-and-code-execution へ）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが tracks の app-context-management から出す（本文に手書きなし）。強制力は data の機能に無い（enforcement 欄なし）ため、本文では強制力に触れていない
- tracks：front matter に app-context-management・context-window（変更なし）
- 1機能1ページ：anchor auto-management（仕組み）・what-remains・at-the-limit に分けた
- level：整える（変更なし）
- 構成の目安：使いどころ・防ぐ原因 = effects／最小の使い方 = at-the-limit（面が app だけなのでタブなし）／雛形 = 無し（理由は上）／効かない場面 = pitfalls／比べる相手 = compare／古くなった助言 = 台帳の行がないため節なし

## メインに判断してほしいこと
- 窓の大きさの数値は本文に書かず、facts-proposal.yml で提案（採用なら auto-management に fact の目印を置く）
- 公式の 2 記事で「有料のプランに限る」の書き方が食い違う（data の note と同じ）。pitfalls で「画面と公式で確かめる」と書いて留めた

## 提案
- facts-proposal.yml（上記）
- 用語集：「拡張思考」が prh の正。extended thinking を本文に出さないよう直した

## 検査の結果
- 1 回目：エラー 1（extended thinking → 拡張思考）・警告 4。直した後：エラー 0・警告 2（no-doubled-joshi。pitfalls の 2 行。読みにくくないと判断して残した）
- 直しは Write でなく Bash の置換で入れた（1 箇所ずつの Edit を避けるため）

## 確かめていないこと
- 一次資料を開いていない（束の写しに基づく）。Web の取得は 0 回
- 自動の要約が画面でどう見えるか、コードの実行がオフの会話での挙動、プランごとの有無は未確認。本文は「確かめられていない」「公開されていない」と書いた
- 「言い直させて確かめる」は（推論・実践例なし）の印を付けた独自案
- 長さの上限への公式の対処 6 項目は、束の写しでは「上限に当たったとき」の一覧だが、利用上限の対処と重なる。本文で重なりを注記した

## 使用量
- 道具の呼び出し：約 9 回（Read 3・Bash 3・Write 3）。Web の取得：0 回
