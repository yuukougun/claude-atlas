# 整合の検証 XC8（stop-hooks・protected-paths・lock-side-effects・freeze-eval-assets・move-judgment-into-scripts・approval-fatigue・when-to-lock）

| 重さ | ページと節 | 食い違い | 直したこと |
| --- | --- | --- | --- |
| 直したほうがよい | freeze-eval-assets「設定で止める」末尾 | 「どの権限モードでも保護される場所」と書くが、持ち主の protected-paths は bypassPermissions で許可、auto で分類器と書く | 「Claude Code が書き込みを事前承認しない場所（モードによっては止まらない）」に直した |
| 直したほうがよい | protected-paths 要点「何ができるか」 | 「どのモードでも確認なしには書かせない」が、同ページの表（bypassPermissions は許可）と食い違う | 「allow ルールでは事前承認されない場所」に直した |
| 軽い（直さず） | protected-paths 要点「強制力」 | 目印の生成値が「鍵」だが、同ページの節 protected と pitfalls は「保護された場所は鍵ではなく確認」と書く。data/facts.yml の features にこのページを page に持つ項目がなく、値の出どころが不明 | 直さず（data の判断） |
| 軽い（直さず） | approval-fatigue「確認を減らす順番」 | 「何も設定していなければ対話は auto モードで始まる」。protected-paths は default（Manual）を前提に書く。どちらが今の既定かは権限モードのページと data で決まる | 直さず（他組のページが持つ） |

ほかの組（フックの鍵と非鍵、fail-open、deny・サンドボックスの効く範囲、お願い／鍵の用語）に食い違いは見つからなかった。

## メインに決めてほしいこと
- protected-paths の要点「強制力」を、データの値のまま「鍵」にするか。本文は「鍵ではなく確認」と言う。強制力の値を持つ feature 項目の有無も確認してほしい。
- approval-fatigue の「既定は auto」が permission-modes-overview・data の今の既定と合っているかの確認。

## check_page.py
freeze-eval-assets：エラー0・警告3。protected-paths：エラー0・警告5（既存の textlint 警告）。各1回。

## 道具の呼び出し
Bash 8、Write 1
