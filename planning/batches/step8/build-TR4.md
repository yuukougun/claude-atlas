# TR4：バッチ4の終わりの扱い

## 直したページ（2ページ・2件）
- images-and-voice：front matter の related に keep-replies-in-japanese を追加（先例「related への追加」）
- permission-modes-in-the-app：コネクタの許可の箇条に（推論・実践例なし）の印を追加
- say-what-you-want のフックの stderr の記述は、公式 Hooks の文書（Exit code 2）で確認。直し不要

## backlog に足した件数
約 45 行（数値の提案の表 15 行・用語集 6・道具と data の形 強制力 7 機能＋そのほか 8・調べる担当 4）。強制力の値の案は ultrathink（お願い）・compaction（なし）・code-execution（分ける案）・artifacts（なし）・connectors・app-tasks・extensions 系。

## batch4-decisions.md：9 行

## MV2 の直しの確かめ（git diff HEAD の8ファイル）
| 重さ | 場所 | 問題 | 直し方 |
| --- | --- | --- | --- |
| 直す | brief-page §4.2 手順5・decisions「段階 reviewed の付け方」と schema/page.schema.json l.362・375 | 検証と直しの担当が reviewed にすると、スキーマが `verified`・`verified_with` を要求する。一方 common l.41 は執筆者は書かないとし、検証役（分かりやすさの担当）が出典を読み直す役でもない。reviewed にした瞬間にスキーマ検査が落ちる恐れ | reviewed のページに verified を要求する条件を、決め（事実の検証の担当は置かない）に合わせて緩めるか、reviewed にする担当が verified を書く条件（出典を読み直した）を brief に書く。どちらか |
| 直したほうがよい | common.md l.205・l.405、design.md l.366・l.673・l.677 | 「検証役が出典と照らす」が残り、「事実の検証の担当は置かない」と食い違う（MV2 の指摘5の残り。keys.yml・l.41・l.208 は直っている） | 「点検の担当」「別の担当」などに置き換える |
| 軽い | brief-page l.3 | 先頭の「版：2026-11-05 v3.1」は工程7と同じ表記のまま。次行の「工程8の版 v3.2」で補っているが、先頭の行が古いまま | 先頭を「工程8の版 v3.2（…）」にまとめるか、v3.1 に「工程7の」を付ける |
| 軽い | step8-wave.js roleText | 検査の回数は直った（執筆は2回まで・検証は1回）。ただし brief-page の「Web の取得は3回まで」と rules.md の「1ページ2回まで」の区別は rules.md の主語追加で解けている | 対応不要（解けている） |
| 解けている | README.md・CLAUDE.md の括弧・rules.md 主語・REPLY の Write 止め・強制力の線引き・keys.yml の writer | MV2 の指摘1〜4・6〜8 は解けており、新しい食い違いなし | — |

## check_page.py
images-and-voice：エラー0・警告2。permission-modes-in-the-app：エラー0・警告6（助詞の警告は残す）。

## 数
Web の取得 1（code.claude.com の Hooks。check_noai 済み）。道具の呼び出し 約 14。
