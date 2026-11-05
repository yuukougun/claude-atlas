# 工程10 整合の確認 XC7

対象：settings-layers・claude-md-loading-order・init-and-first-claude-md・isolate-with-safe-mode・output-style-modes・using-auto-memory・agents-md

結果：直すべき食い違いは見つからなかった。ページは1つも変えていない。

| 重さ | ページと節 | 食い違い | 直したこと |
| --- | --- | --- | --- |
| 軽い | isolate-with-safe-mode 要点「止められるもの」と `what-is-disabled` | 要点は「権限は通常どおり働く」と書く。節は「自分の `allow`・`deny` ルールとフックは外れる」と書く。節を読めば解けるが、要点だけ読むと deny も効くと取れる | 直さなかった。言葉の選び方の問題で、事実の食い違いではない。「権限（操作ごとの確認の仕組み）は残るが、自分の deny ルールは外れる」と要点に足すかどうかはメインが決める |
| 軽い | isolate-with-safe-mode `what-is-disabled` と claude-md-loading-order `limits` | 前者は「管理が配った CLAUDE.md は外れる」、後者は「管理の CLAUDE.md は `claudeMdExcludes` で外せない」。仕組みが違う（起動オプションと除外設定）ので矛盾ではないが、並べて読むと取り違えやすい | 直さなかった。どちらかが誤りとは言えない。必要なら相互の一言をメインが判断 |

確認して合っていたもの：

- 層の順位と合わさり方：settings-layers と、claude-md-loading-order の `claudeMdExcludes`、output-style-modes の保存先（local は user に勝つ）が合っている
- クラウドで届かないもの：settings-layers と claude-md-loading-order が合っている
- 強制力：facts の features と各ページの要点の「お願い」が合っている。鍵は管理の層だけという説明も、全ページで一貫している
- AGENTS.md の既定の読まれ方：agents-md と claude-md-loading-order と init-and-first-claude-md が合っている
- 自動メモリの扱い：using-auto-memory と safe-mode の表（自動メモリは外れる）が合っている

## メインに決めてほしいこと

- 上の軽い2件に手を入れるか。入れないなら対応不要

## check_page.py の結果

ページを変えていないので流していない（0回）。

## 道具の呼び出し数

Bash 8、Write 1（計9）
