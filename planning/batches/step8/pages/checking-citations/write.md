# write.md：checking-citations

## 書いたファイル
- docs/verify/checking-citations.md（stubs から mv。stage draft、updated 2026-11-05）
- front matter で変えたキー：sections（guard・overall-check・when-it-fails を足した。既存の error-types・steps は変えず）、sources（api-docs-reduce-hallucinations を足した。data/sources.yml に既存）、stage、updated
- snippets/checking-citations/citation-table.md ＋ .expect.yaml（目次の templates の案：出典の確認表）
- snippets/checking-citations/checkable-list.txt ＋ .expect.yaml（足した雛形：確かめやすい一覧を出させる依頼）
- data/sources.d/checking-citations.yml は作っていない（新しい出典なし）

## 必ず持つものの対応
- 手順：steps（6 段、各段に終わりの確かめ付き）
- 確かめる・縛るのページへの道：front matter の prerequisites（fact-checking）と本文の要点の前提、guard（fact-checking#sources-only・#quotes）、when-it-fails（plausible-falsehoods#diagnosis ほか）
- 冒頭の要点：abstract の囲み
- level を持つ：front matter の level（整える）
- 構成の目安（要点→守り→手順→確かめ方→失敗したとき）：guard → steps → overall-check → when-it-fails（前に error-types を置いた）

## メインに判断してほしいこと
- 事例の扱い：材料 6.2 の訴訟の事例の出典は techcrunch.com で、check_noai.py が「noai あり」と判定した（deny にある）。そのため事例は本文に書かず、誤りの形を一般形で書いた。目次の「Anthropic の訴訟の事例」の位置づけは、noai でない別の一次の出典（裁判所の記録など）が見つかれば足せる。足すか、事例なしのままにするかを判断してほしい
- 「よくある誤りの形」の 4 形のうち、「引用が原文にない」「出典が主張を支えていない」は材料 6.2 にはなく、目次の確認表の列（引用の文言・主張を支えているか）から立てた。出典を付けていない

## 提案
なし（用語集・data・front matter の提案なし）

## 検査の結果
- check_page.py を 2 回流した。エラー 0・警告 2
- 残した警告：66 行（link の目印の間に道具が書く題名の中の助詞。自分では直せない）、93 行（「Claude 自身に…聞き直しても、…確かめにならない。同じ記憶から…」の「が」の重なり。文を割ると主旨が崩れるため残した）

## 確かめていないこと
- 外の事実（訴訟の事例など）は本文に入れていない。公式の hallucination 対策の記述は、材料 6.2 の写し（Reduce hallucinations）を言い換えたもので、原文は開いていない
- 手順の「Claude Code で原文を取得させて照合」は、特定の機能名を出さず一般形で書いた。実際の動作は試していない
- 2 つの雛形は動作確認していない（expect は観察の形）
- Web の取得は 0 回。check_noai.py は 1 回

## 使用量
- 道具の呼び出し：約 12 回（Read 2、Bash 5、Write 6 〔雛形 4・ページ 1・報告 1〕）、Web の取得 0 回
