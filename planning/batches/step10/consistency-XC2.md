# XC2 整合の検証（permission 系 7 ページ）

| 重さ | ページと節 | 食い違い | 直したこと |
| --- | --- | --- | --- |
| 直したほうがよい | permission-rules「使いどころ」 | 「CLAUDE.md に書くのは依頼にとどまる」。他ページ（request-lock-table ほか）と同じ用語は「お願い」 | 「お願い」に直した |
| 軽い | where-bypass-is-ok「なぜ隔離した環境だけか」 | 無人では「確認を外すか全部拒むかの二択に寄りやすい」と書くが、permission-modes-overview は `dontAsk` + allow ルールを無人の第三の道に挙げる（同ページの誤解の節も「外さずに走らせる道」に触れる） | 直さなかった。「寄りやすい」で矛盾とまではいえない |

確認して合っていた点：強制力（permission-rules・sandboxing・modes は鍵、auto はモデルの判定）、deny が全モードで先に評価されること、サンドボックスの内側と外側の分け、blockWritesOutsideWorkingDirectories の効き方、defaultMode の auto・bypass が project 設定で無効なこと、既定モードの値（fact 目印）。

## メインに決めてほしいこと
なし。

## check_page.py
permission-rules：エラー 0・警告 3（既存の助詞の重なり。今回の変更箇所ではない）。

## 道具の呼び出し
約 10 回。
