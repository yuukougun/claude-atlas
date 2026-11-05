# XC9 整合の検証（プランと上限の組）

対象：choosing-a-plan・before-using-top-model・usage-credits-basics・check-billing-path・how-usage-limits-work・what-uses-up-limits・when-ai-is-unavailable。直したページ：なし。

| 重さ | ページと節 | 食い違い | 直したこと |
| --- | --- | --- | --- |
| 直したほうがよい | before-using-top-model#which-limit と、how-usage-limits-work#limit-types・choosing-a-plan#plan-table | 前者は「最上位のモデルに別の週の上限はなく、通常の週の上限の内側」に合わせて書く（公式の食い違いを警告で明記）。後者 2 つは data の表（usage-limit-types-by-plan）と本文の箇条で、Max・Ultra に「別の週の上限がある」と断定する。data の note にも、正本の見直しは持ち主へ、とある | 直さなかった。どちらが正しいか決められず、表は data の生成物で手では直せない |
| 軽い | when-ai-is-unavailable#fallbacks「別の経路を使う」 | API を別の経路とし、違いの参照先を usage-credits-basics#vs-api-credits にする。そこは usage credits とプラン付き API credits の違いの節で、API 経路の課金（キーが要る・従量）は check-billing-path が持つ | 直さなかった。参照先の変更は推奨の変更に近いので、メインが決める |
| 軽い | usage-credits-basics#how-it-works の日付 | 失効の期間の目印が「2026-11-06 時点」で、他ページの確認日（11-04・11-05）より新しい。data 側の値で、本文の誤りではない | 直さなかった（data） |

他の観点（面をまたいだ一つの枠・/clear で戻らない・3 回までの継続・Wrap-Up Allowance・API credits は対話の Claude Code に使えない・鍵や認証の順・usage credits の旧名）は、全ページで合っていた。

## メインに決めてほしいこと

1. 最上位のモデルの別の週の上限の有無。before-using-top-model と、data の表および 2 ページの本文が食い違う。正本を決めたうえで、片方に合わせる。
2. when-ai-is-unavailable の「別の経路を使う」の参照先を check-billing-path にするか。

## check_page.py

ページを直していないので実行していない。

## 道具の呼び出し

Bash 7 回・Write 1 回。
