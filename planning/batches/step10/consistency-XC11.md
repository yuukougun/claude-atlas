# XC11 整合の確認（自動化・非対話・背景の 8 ページ）

| 重さ | ページと節 | 食い違い | 直したこと |
| --- | --- | --- | --- |
| 直したほうがよい | choosing-automation「どの課金の経路か」 | 「環境に API キーがあると API の従量になる」と一般に書くが、持ち主の cloud-schedules は、クラウドでは鍵を置いてもサブスクリプションの認証が使われると書く | 例外の 1 文を足し、cloud-schedules#pitfalls を link で指した |
| 軽い | github-actions-with-claude「効かない場面・落とし穴」の手元の設定 | `--bare` を勧める書き方だが、bare-mode は OAuth を読まないと書く（OAuth のトークンを使う Action では API キーの secret が別に要る）。choosing-automation は注意済み | API キーが要る旨の 1 文と bare-mode#authentication への link を足した |
| 軽い | cloud-schedules / loop-and-scheduling / choosing-automation の名称 | 本文は「定期タスク」、choosing-automation と name の目印は「予定のタスク」。同じ機能を 2 通りに呼ぶ | 直さず（用語の方針の話） |
| 軽い | headless-basics と cloud-schedules の auto の分類器 | 止めが重なったとき、-p は拒むだけで実行は続く、クラウドは止まって待つ。環境が違うので矛盾とは言えない | 直さず |

ほかの組（強制力の言い方〔鍵・お願い〕、止まる上限、`--bare` の読み込まないもの、間隔の下限と失効、課金の経路、権限の層）は食い違いなし。

## メインに決めてほしいこと

- 名称：機能 scheduled-tasks の呼び名を「クラウドの定期タスク」「クラウドの予定のタスク」のどちらに寄せるか（title・aliases・name の目印に関わるので担当は直さない）。
- bare-mode の pitfalls の fact `setting-sources-leak-fix-version` が「2026-11-06 時点」で、今日（11-05）より先の日付。data 側の確認を。

## check_page.py

- choosing-automation：エラー 0・警告 4（既存の助詞の重複）
- github-actions-with-claude：エラー 0・警告 11（既存。長文と助詞）
- 各 1 回

## 道具の呼び出し

Bash 9 回・Write 1 回
