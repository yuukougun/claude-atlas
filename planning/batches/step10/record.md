# 工程10（全体の検証）の記録

- 日付：2026-11-05。対象：公開するページ 193（第一波136・残りの必須54・ほか）。design §10.1 の10
- 事実の正しさは見ていない（decisions 2026-11-04「事実と出典の検証」）。確認日（verified）は、出典を読み直したページにだけ書く決めなので、いまはどのページにもない（バッジは「未検証」）

## 道具で見たもの

| 観点 | 道具 | 結果 |
| --- | --- | --- |
| 外のリンク | tools/check_links.py（573件） | 切れ0・正常563・転送3・要確認1・確かめない6。転送のうち2件（jinrai の記事、Simon Willison の記事の末尾の /）は転送先に書き換えた。Anthropic の system card の PDF は、転送先が CDN の名前つきの URL なので、公式の元の URL のままにした。要確認の1件は Notion の MCP の接続先（認証が要るので 401 は正常）。確かめない6件は AI の利用を断るドメイン（atcoder.jp・codeforces.com。リンクだけで、中身は開かない）と、例の URL |
| 内のリンク・前提・目印 | tools/check_pages.py・tools/check_catalog.py | エラー0。警告は目次の比例則3件（骨格のページ。推奨のページを書く波で直す） |
| 書き方 | textlint と prh（tools/textlint_targets.py） | エラー0・警告342（同じ助詞の重なり295・文の長さ21・漢数字13・読点の多さ9・ほか4）。下書きでは止める条件にしない（planning/batches/step8/rules.md） |
| 描画 | tools/render_pages.py（390px のライトとダーク） | 223ページでエラー0・警告0 |
| 雛形 | tools/check_templates.py | エラー0（設定のキーの許す一覧に、公式の文書で確かめた modelSettings と statusLine を足した） |

## 担当が見たもの

| 観点 | 担当 | 結果 |
| --- | --- | --- |
| 読者の課題から引いてみる | RT（reader-tasks.md） | 逆引きの20項目：着ける17・遠い3（答えが3節目以降：compact-and-auto-compact・checkpoints-and-rewind・hook-recipes）・着けない0。トップのページが3行の仮のページで、リンクがなかった（TP が書いた） |
| ページどうしの食い違い | XC1〜XC6（consistency-XC*.md。同じ機能を扱う6組・42ページ） | 直した7件、メインに上がった4件（止めるフックの登録例、クラウドの条件、目印と本文の言葉の重なり、ultrathink の版）。4件はメインが決め、FX10 が直した |

## 後に回すもの（初版の後）

- 逆引きの行が節を指せるようにする（signs に節の anchor を持たせる）。遠い3件が答えの節に直接着く（RT の案1）
- 逆引きの表で、同じ行き先の項目を束ねる（RT の案3）
- 書き方の警告342件の整理（同じ助詞の重なりが大半）
- planning/batches/step8/backlog.md に残るもの（アプリの手段の「未確認」を調べる、data の形、出典の差し替え など）
