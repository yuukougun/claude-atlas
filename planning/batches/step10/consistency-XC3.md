# XC3 一貫性の検証（CLAUDE.md・rules・置き場所の7ページ）

対象：what-to-put-in-claude-md・claude-md-length・path-scoped-rules・claude-md-vs-rules-skills-styles・where-instructions-sit・where-to-put-instructions・instructions-ignored

見た点：強制力（お願い／鍵）、読み込みの時期（根・サブフォルダ・paths あり／なし）、圧縮の後の扱い、200 行の目安、システムプロンプトとの位置、Explore/Plan・クラウドの届き方、アプリと Claude Code の対応。

| 重さ | ページと節 | 食い違い | 直したこと |
| --- | --- | --- | --- |
| 軽い | claude-md-length #deletion-test の「行数の目安の幅」 | 「公式の立場：目安は <fact>目安は 1 ファイル 200 行以内…</fact>で」と、fact 目印の中身が「目安は」で始まり、本文の「目安は」と重なる（読むと「目安は 目安は」）。ほかのページとの食い違いではなく表記の重複 | 直さなかった（目印の中身は data の値で、本文の言い回しだけを変える判断が要る。メインに任せる） |

ページどうしの食い違いは見つからなかった。確かめた一致：

- 強制力：全ページが CLAUDE.md・rules を「お願い（文脈。守られる保証なし）」とし、例外を許さない規則は鍵（フック・deny）へ、で揃う。持ち主 what-to-put-in-claude-md の data 値（お願い）とも合う。
- 圧縮の後：根の CLAUDE.md と paths なしの rules はディスクから入れ直し、入れ子の CLAUDE.md と paths 付きの rules は一致するファイルを再び扱うまで戻らない。5ページで同じ。
- 読み込み：作業ディレクトリから上は開始時、サブフォルダは該当ファイルを読み書きしたとき、paths なしの rules は開始時。揃う。
- CLAUDE.md の位置：システムプロンプトの後のユーザーメッセージ（system reminder）。where-instructions-sit と他ページが合う。
- Explore/Plan は CLAUDE.md を受け取らない、クラウドは `~/.claude/CLAUDE.md` を読まない、の説明が揃う。
- app/where-to-put-instructions の Claude Code 対応表は、extend の置き場所のページと矛盾しない。

## メインに決めてほしいこと

- 上の軽い1件の扱い（fact 目印の中身の頭の「目安は」を、data 側で直すか）。

## check_page.py の結果

ページを直していないので実行しなかった。

## 道具の呼び出しの数

Bash 6 回、Write 1 回（Read・Edit なし）。
