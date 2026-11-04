# 工程6b：data の初版を作る担当への共通の指示

- 版：2026-11-04 v1。[brief-build.md](brief-build.md) の §1〜§3 と §5 をそのまま当てる。この文書はその差分

## 1. 目的と終わりの条件

data（design §9.1）の初版を、一次資料で確かめて作る。終わりの条件（design §10.1 の6b）：第一波のページが `tracks`・`outdated_advice` で指す id と、第一波のページの materials が挙げる一次資料の sources の項目がすべてある。features の各項目に主のページ（page）がある。

- 第一波のページの一覧：`uv run python tools/check_catalog.py --stats` の第一波（136ページ）。id の一覧は、目次（planning/catalog/）と site.yml の first_wave から道具で出す（tools/check_catalog.py の数え方。出し方が分からなければ、目次の wave: 1 のページと、その前提と、症状のページの routes の各原因の最初の必須の先と、default-safety-settings をたどる）
- 形は `schema/facts.schema.json`・`schema/sources.schema.json`・`schema/outdated-advice.schema.json`（schema/keys.yml から作る）。書き方の例は `data/facts.yml`・`data/sources.yml`・`data/outdated-advice.yml` の冒頭の注

## 2. 書く場所（担当どうしで同じファイルを書かない）

- 担当は data/ を直接書かない。自分の下書き `planning/batches/step6/data/<担当>.yml` に、data のファイルと同じ最上位のキー（`features`・`names`・`facts`・`sources`・`domains`・`advice`）で書く。メインが data/ にまとめる（sources の重なりは URL で見て、id をそろえる）
- sources の id は、担当の記号を頭に付けない、内容から作る短い id（例：`cc-docs-hooks`）にする。ほかの担当と同じ一次資料を使うことがあるので、URL を正確に書く（メインがまとめるときに同じ URL を1つにする）
- 下書きは、まとめた後の形で schema に通るように書く。jsonschema で自分の下書きを検査してから終える（`uv run python` の小さなスクリプトでよい。スクリプトは scratchpad に置く）

## 3. 確かめ方

- 値と属性は一次資料（公式の文書・CHANGELOG・リリースノート・ヘルプセンター・公式の料金のページ）で確かめる。調査資料（planning/research/22〜28 など）は手がかりにしてよいが、入れる値はその場で一次資料を開いて確かめる。確かめられないものは `status: 未確認` にし、報告に理由を書く
- 新しいドメインを資料に使う前に `uv run python tools/check_noai.py <URL>` で AI の利用を断る指定を確かめ、`domains` に結果と日付を書く。断る指定のあるサイトは使わない（atcoder.jp・codeforces.com は開かない）
- 一次資料の写しの URL（Internet Archive）は、すでにある写しを記録するだけにする（新しく写しを作らせない。外への書き込みになるため）
- 公式同士が食い違うときは、両方の出典を残し、食い違いを書く（design §6.7）
- 確認日は 2026-11-04（実際に確かめた日）

## 4. 担当

| 担当 | 受け持ち | 下書き |
| --- | --- | --- |
| D1 | features のうち、planning/catalog/features.yaml の「Claude Code の文脈と指示」「Claude Code の縛り」「Claude Code の操作」「Claude Code の任せ方」「Claude Code の面」の機能（属性・主のページ・照らす英語の語・出典）。読み込みの時期とコンテキストのコストの語彙は、公式の Extend Claude Code の比較の表の表記を見て決め、報告に書く（メインが site.yml に足す） | `D1.yml` |
| D2 | features のうち、「アプリ」「API・SDK」「面をまたぐもの」「プランと上限」「組織と提供の経路」の機能 | `D2.yml` |
| D3 | 古くなった助言の台帳の全行（planning/catalog/registry.yaml の ledger。37行）と、名称と旧名の表（names。機能の改名・プランの改名・コマンドの改名。DR-18：台帳の行は名称の id を指して時期を引く） | `D3.yml` |
| D4 | 第一波のページの materials が挙げる一次資料の sources と、その domains。あわせて、第一波のページごとに、使える一次資料の sources の id の一覧（執筆者に渡す） | `D4.yml` と `wave1-sources.yml` |

- features の主のページ（page）は、その機能を tracks に持ち、その機能そのものを扱うページ（ふつう型が feature のページ）。分かれるときは理由を報告に書く。features.yaml の題名と note は仮のもの
- 照らす英語の語（CHANGELOG とリリースノートで変更を見つける語。DR-11）は、公式の英語の名前と、コマンドや設定のキー
