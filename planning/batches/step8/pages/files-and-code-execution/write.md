# write.md：files-and-code-execution

## 書いたファイル
- docs/app/files-and-code-execution.md（stub から移して stage: draft。sections に when・usage・pitfalls・compare を追加、sources に既存の 3 件、updated を 2026-11-05 に）
- snippets/files-and-code-execution/request-spreadsheet.{md,expect.yaml}（kind: prompt）
- snippets/files-and-code-execution/request-private-analysis.{md,expect.yaml}（kind: prompt、safety: true）
- planning/batches/step8/pages/files-and-code-execution/facts-proposal.yml
- data/sources.d は新設なし（hc-files など 3 件は data/sources.yml に既にある）

## 必ず持つものの対応
- 要点のバッジ（強制力・読み込みの時期など）：冒頭はテンプレートが出す。`#when` の `compare` の目印で属性の表を出した。2 機能とも enforcement が null で強制力の列は出ない（提案を参照）
- tracks：front matter の tracks（file-creation・code-execution）を `#when` の compare で使用
- 1 機能 1 ページ・節に分ける：`#when`・`#usage`・`#network`・`#outputs`・`#pitfalls`・`#compare`
- level：front matter に「整える」
- 構成の目安：使いどころ `#when`／最小の使い方 `#usage`（面は app だけなのでタブなし）／雛形 `#usage`・`#network`／落とし穴 `#pitfalls`／比べる相手 `#compare`／古くなった助言は台帳に行がないので `#compare` の末尾に一言

## メインに判断してほしいこと
- ネットワークの既定・30MB の上限・共有の制限は、数値ファイルに置き場がない。本文は値なしで書いた（「参考に挙げた公式の文書で確かめる」）。facts-proposal.yml の 3 件を data へ入れれば `fact-table` で出せる
- 2 機能の enforcement が null。ネットワークの設定を「鍵」と見るか、機能ごとに何を入れるかを決めてほしい
- 本文で「依頼の文はお願いで、設定が鍵」と書いた。この言い方でよいか

## 提案
- facts-proposal.yml（3 件の fact と、tracks/enforcement の確認）

## 検査の結果
- check_page.py 2 回：1 回目 エラー 0・警告 5、直した後 エラー 0・警告 2
- 残した警告 2 件（171・177 行の no-doubled-joshi「に」）：「受け取ったあとに確かめる」「渡す前に見る」の自然な文で、誤検出に近いと判断

## 確かめていないこと
- 雛形 2 件の実際の動作（実行していない。expect は観察の記録）
- 公式の文書は WebFetch 1 回で確認（2026-11-05）。Team・Enterprise の既定の画面の名前や、モバイルの手順の細部は未確認
- 作ったファイルの共有の制限が Team・Enterprise でどうなるかは公式に記述がなく、本文は「プランによっては」とだけ書いた

## 使用量
- 道具の呼び出し 約 13 回、Web の取得 1 回
