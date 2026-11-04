# 工程6a 2段目：作る層・検査の層・見た目の担当への共通の指示

- 版：2026-11-04 v1。[brief-build.md](brief-build.md)（1段目の共通の指示）の §1〜§3 と §5 をそのまま当てる。この文書はその差分
- 1段目の報告（build-B1〜B5.md）と、README の「1段目の報告への判断」を先に読む

## 1. 受け持ち（同じファイルを2人が書かないように分けた）

| 担当 | 書くもの |
| --- | --- |
| G 作る層 | `tools/gen/`・`tools/gen_site.py`・`nav.yml`（以後は生成物）・生成物（`docs/<field>/index.md`・`docs/lists/`・`docs/llms.txt`・`docs/assets/data/`）・`tests/tools/` の作る層の試験と試験用の目次・ページ |
| C 検査の層 | `tools/checks/`・`tools/check_pages.py`・`tools/check_templates.py`・`tools/check_all.py`・`tools/render_pages.py`・`tools/check_svg.py`・`tests/tools/` の検査の層の試験・`.github/workflows/check.yml`・`.claude/settings.json` の deny への追加と `tests/hooks/` の対応する試験 |
| V 見た目 | `overrides/`（テンプレートの部品・CSS・JS）・`tests/site/` の見た目の試験 |

## 2. 担当どうしの受け渡しの形（ここに合わせて作る）

- **読む層**は1段目の `tools/lib/`（`from lib import load_atlas`）を使う。読む層を直したいときは、直さずに報告の「提案」に書く（メインがまとめて直す）
- **ページの置き場所**：stub は `stubs/<field>/<id>.md`、draft 以上は `docs/<field>/<id>.md`（design §8.5）。試作のページで波の来ていないものは nav に載せず `exclude_docs` に書く
- **未公開のページ**：stub と、公開から外した試作のページ（design §8.4 の定義）
- **目印**（design §8.4）：手書きのページの中の生成部分は `<!-- gen:begin <名前> -->`〜`<!-- gen:end <名前> -->`。数値は `<!-- fact:begin <id> -->`〜`<!-- fact:end -->`。本文のリンクは `<!-- link:begin <id>[#<anchor>] -->`〜`<!-- link:end -->`（公開しているページならリンク、未公開なら「題名（準備中）」）。参考の節は `<!-- gen:begin references -->`。雛形は `<!-- gen:begin snippet <id>/<名前> -->`（動作確認を通ったものだけを写し、通っていないものは「動作確認の後に載せる」）。G が書き、C が「目印の外の手書きのリンクで未公開のページを指す」「目印の中を手で書き換えた（`gen_site.py --check` の差）」を検査する
- **サイト用のデータ**：G が `docs/assets/data/pages.json` を作る（公開するページごとに id・URL・題名・型・level・stage・分野・期限の日〔design §9.2・DR-11：ページの確認日＋ページの期限と、ページが含む数値の確認日＋数値の期限のうち早いもの〕・確認日・volatility）。知識マップの `docs/assets/data/graph.json`（ノードは公開するページ、辺は prerequisites と症状の routes）。V の JS はこの2つを読む（今日の日付と期限の日を比べるのはブラウザ）。形は G が決めて報告に書き、V は G の報告がまだなければ、この段落の項目を前提に作る
- **ページの見た目**：バッジ（level・型・stage・面）と下書きの帯は、V がテンプレートで front matter（`page.meta`）から出す。ページ下部の前提・次に読む・関連と、症状のページの振り分けの表は、G が目印の間に Markdown で書く（未公開の先は「題名（準備中）」）
- **生成物を手で書き換えない**：H2 の deny は Edit と Write の道具に効く。道具（Python）が書くのはよい。C は deny に `nav.yml`・`schema/*.schema.json`・`docs/assets/data/**` を足し、hooks の試験を合わせる

## 3. 担当ごとの要点

- **G**：design §7（横断のページの作り方）・§8.3・§8.4・DR-01・DR-02・DR-15（逆引きの束ね方と分け方、用語索引の主のページ）・§8.6 の生成物の鮮度。`gen_site.py` は `--check`（作り直して差がないか）と `--page <id>`（自分のページの目印だけを書く。担当が使う）を持つ。毎回変わる値（日時・内容のハッシュ）を生成物に入れない。作る順は、骨格と試作に要るもの（nav・分野の入口・目印の中身・pages.json・llms.txt）を先に、索引の類（逆引き・用語索引・知識マップ・ロードマップ・症状の原因別の表・台帳・比較表）を後に。終わらないものは報告に書く
- **C**：design §8.6 の表。`check_pages.py` は front matter（page.schema.json）、参照（id・anchor・循環・段階の逆転・必須の前提は必須・比例則・routes・推移的な前提・逆引きの重複）、置き場所と stage、未公開のページへの手書きのリンク、目印の外の数値（照合の型を持つ項目だけ。DR-16）、確認日の期限（警告）。規則は目次の検査（`tools/check_catalog.py`）と同じ中身を、検査の層の関数として front matter に当てる（DR-16。check_catalog は骨格の後に退く）。`check_templates.py` は静的な検査（DR-07：スキーマの写しと許すキーの一覧）。`render_pages.py`・`check_svg.py` は kyopro-atlas から写して直す（読むだけ）。`check_all.py` は CI と同じ組（`make_schema.py --check`・`gen_site.py --check`・`check_pages.py`・目次の検査・textlint・試験）を流す入口で、CI の check.yml もそれに合わせる。G の道具がまだ途中なら、その段は「G の道具ができたら入れる」と報告に書いて飛ばしてよい
- **V**：design §8.5・DR-10（帯の文「下書き・未検証」）・DR-11・DR-14（外のサイトから読まない）。kyopro-atlas の overrides の部品・CSS・JS（バッジ・前提と次に読む・知識マップ・絞り込みの欄）を写して直す（読むだけ。進捗の部品〔解いた・理解した〕は外す。D17）。期限切れの注意書きは、pages.json の期限の日とブラウザの今日を比べて出す。描画の試験は Chrome があるときだけ動く形でよい（B1 の tests/site と同じ）
