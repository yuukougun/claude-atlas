# write.md：prompt-injection-in-practice

## 書いたファイル
- docs/safety/prompt-injection-in-practice.md（stub から移動。stage を draft、updated を 2026-11-05、sections に what-works・misconceptions を足し、sources に既存の 10 件を入れた）
- snippets/prompt-injection-in-practice/harmless-note.md と .expect.yaml（無害な再現。safety: true）
- docs/img/prompt-injection-in-practice/flow.svg（目次の図の案）
- stubs/safety/prompt-injection-in-practice.md は削除（移動の代わり）。data/sources.d は新しい出典がないので作らず

## 必ず持つものの対応
- 原理 principle「縛る」・原因 prevents「境界がない」の名指し：#what-works（冒頭の段落で両方を名指す）
- pitfalls：空なので持たない
- level あり、要点の最初は「何が分かるか」：冒頭の要点の囲み
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：#channels（図と経路）・#patterns（事例と再現）・#why-detection-fails（なぜ）・#what-works・#misconceptions。関連はテンプレートが出す

## メインに判断してほしいこと
- #patterns に Invariant Labs・Check Point の事例を会社名つき・手口の細部なしで載せた。方針 B1 に照らして問題ないか
- WhatsApp の事例の「確認画面に一部しか見えない形」は隠し方に触れる。強すぎれば削る

## 提案
- 空。research/22 #9（v2.1.317 でアカウントのメールアドレスを送る前に確認）は「入った版」に当たるので本文に書かず。要るなら data の facts に項目を足して #what-works から指す

## 検査の結果
- 1 回目：エラー 1・警告 5（prh の「全て」、助詞の重複など）。直して 2 回目：エラー 0・警告 1
- 残した警告：130 行の文の長さ（link の目印の間に道具が入れる長い題名のため。誤検出に近い）

## 確かめていないこと
- 雛形の動作（確認語が付くか）は試していない
- 事例・研究の内容は束の写しに基づく。一次資料は開いていない。OWASP の「1 位」は束の 4-1 による
- 公式の立場（MCP を審査・監査しない）は束の 4-4 の写しによる。原文は未確認
- 「後から差し替える型」「確認画面に一部だけ見える」は束の記述の範囲

## 使用量
- 道具の呼び出し 約 10 回、Web の取得 0 回
