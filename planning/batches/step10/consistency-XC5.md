# 整合性の検証 XC5（圧縮・文脈の組 7 ページ）

| 重さ | ページと節 | 食い違い | 直したこと |
| --- | --- | --- | --- |
| 軽い | compact-and-auto-compact#auto-compact | 「CLAUDE.md は読み直される」。持ち主の what-survives-compaction は「根の CLAUDE.md は入れ直され、サブフォルダのものは引き金まで戻らない」 | 「プロジェクトの根の CLAUDE.md は入れ直される」に直した |
| 軽い | compact-and-auto-compact#settings | 窓と idle compaction の設定を「鍵に近い」と書く。この教材で鍵は強制の仕組み（圧縮の強制力はなし）を指す | 「圧縮の動きそのものを変える」に直した |

ほかの観点（根の CLAUDE.md・サブフォルダ・paths 付き rules・スキルの本文と説明・フックの文脈・自動メモリ・/clear と /compact で常駐が減らないこと・窓の広がり）は、7 ページの間で食い違いなし。

## メインに決めてほしいこと

なし。

## check_page.py

compact-and-auto-compact：エラー 0・警告 4（助詞の重複。うち 101 行目の文は今回の直しで 1 文が長くなったが、他の 3 件は元からの文）。1 回実行。

## 道具の呼び出し

Bash 7・Write 1。
