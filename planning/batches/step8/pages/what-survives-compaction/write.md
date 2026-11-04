# write.md：what-survives-compaction（執筆）

## 書いたファイル
- docs/basics/what-survives-compaction.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を 5 件、sections に what-happens・why・effects・misconceptions を足した。既存の 4 anchor は変えていない）
- docs/img/what-survives-compaction/four-groups.svg（4 つの群の図）
- facts-proposal.yml（数値の提案 4 件）。雛形・data/sources.d は作っていない（目次の templates なし、出典は sources.yml に既存）

## 必ず持つものの対応
- どの原理・どの原因に関わるか：`effects`（見せる・縛る／散らかっている・縛っていない を名指し）
- level（任せる）：front matter。要点の最初は「何が分かるか」
- 構成の目安（要点→何が起きるか→なぜ→何に効くか→誤解→関連）：`what-happens`→`why`（図と比喩）→`kept`〜`dissolved`→`effects`→`misconceptions`→関連（テンプレート）
- pitfalls：front matter に値がないので名指しなし

## メインに判断してほしいこと
- 4 つの群の見出しと、公式の表の項目の対応は次のとおり。「動き続ける」「もう一度走る」を kept に、「作り直して入れ直す」「上限付きで入れ直す」「一部を読み直す」を reloaded にまとめた
- compare の表に compaction 自身の行が「未確認」で出る。tracks に compaction があるため。表から外すには tools 側の対応か tracks の見直しが要る（提案）
- 数値は skill-reattach-tokens-each/total の目印だけ使い、他は本文に書かず facts-proposal.yml に提案した。目印を置く場所は reloaded と kept

## 提案
- facts-proposal.yml の 4 件（used_in を付けた）。取り込まれたら、reloaded のファイルの項と kept のフックの項に目印を足してほしい
- 用語集：prh が「サブエージェント」「自動メモリ」「出力スタイル」「システムプロンプト」を求めた。本文はそれに従った

## 検査の結果
- check_page.py：1 回目 エラー 5・警告 1（prh の表記と代替テキストの長さ）、直して エラー 0・警告 0（最後に細部の直しで 1 回余分に流した）

## 確かめていないこと
- 公式の表の最新の版との照合は束の写しだけ。Web は取得していない（0 回）
- 「会話の中だけの指示は要約に載ることもある」は、公式の分類（要約に溶ける）からの言い換えで、載り方の実測はしていない
- 散らかっている／縛っていない の説明（effects）は束の材料からの解釈で、研究の根拠はない
- アプリと API の挙動は未確認として、範囲外と書いた

## 使用量
- 道具の呼び出し 約 14 回・Web の取得 0 回
