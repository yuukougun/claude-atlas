# review.md：long-running-agent-context

## 指摘
| 番号 | 重さ | 場所 | 問題 | 直したこと |
| --- | --- | --- | --- | --- |
| 1 | 直す | #what-happens 導入 | 無人で長く回す話なのに、守り（確かめ）が #effects の末尾まで出ない（比例則） | 導入の段落に checking-unattended-runs#guards-first への link を足した |
| 2 | 直したほうがよい | #external-state | path traversal が定義なしで出る（U5。用語集にもない） | 括弧で短く定義した |
| 3 | 直したほうがよい | #three-tools の表 | memory tool の「失うもの」が「なし」で、誤解の節（読まなければ効かない）と食い違う | 「書き忘れたこと、読み忘れた記録」に変えた |
| 4 | 直したほうがよい | #effects の冒頭 | 「この 3 つ」が節内で指すものがない（U3） | 3 つの名を書いた |
| 5 | 軽い | #what-happens の例 | 決めたことが消えた原因を断定していた | 「考えられる」と推測の形にした |
| U6 | 問題なし | write.md の対応 | principle・prevents は #effects で名指し、pitfalls は値なし、level あり、構成は目安どおり（#external-state は足した節）。write.md と本文が合う | 直しなし |

## 検査の結果
- 1 回流した。エラー 0・警告 1（no-doubled-joshi の「が」。執筆の担当が残した警告と同じもの）

## メインに判断してほしいこと
- 用語集に path traversal を足すか（執筆の提案のまま。本文には短い定義を入れた）
- 直したので stage は draft のまま

## 使用量
- 道具の呼び出し：約 15 回。Web の取得：0
