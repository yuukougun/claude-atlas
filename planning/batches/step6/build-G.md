# 工程6a 2段目 G（作る層）の報告

- 版：2026-11-04
- 担当：G（[brief-build2.md](brief-build2.md) §1 の G の行、§3 の G。共通の指示は [brief-build.md](brief-build.md) §1〜§3・§5）
- 書いたもの：`tools/gen/`（17ファイル）・`tools/gen_site.py`・生成物（道具で書いた `nav.yml`・`docs/llms.txt`・`docs/assets/data/pages.json`・`docs/assets/data/graph.json`）・`tests/tools/gen_helpers.py`・`tests/tools/test_gen_site.py`・`test_gen_parts.py`・`test_gen_catalog.py`・`tests/tools/fixtures/gen/`（33ファイル）・この報告
- 変えていないもの：読む層（`tools/lib/`。直したい点は §4）、ほかの担当のファイル（読んだだけ：C の `tools/checks/`・`check_pages.py`、V の `overrides/`。受け渡しをそろえるため）
- git と gh は使っていない。Web は使っていない。手本の `../kyopro-atlas` は読んだだけ（`tools/gen_site.py`・`overrides/main.html`）。止められた操作はない

## 1. 作ったファイルと中身

### 1.1 作る層 `tools/gen/`（design §8.3。生成物の種類ごとに1つの部品）

| ファイル | 中身 |
| --- | --- |
| `config.yml` | 作る層の設定：`held_back`（公開から外す試作のページ）・`roles`（症状の型・症状辞典の分野・値を書いてよい status）・`labels`（語彙の値 → 表示の言葉。型・段階・面・sign の種類・原因の軸・機能の属性・生成の部分の見出しの言葉）・`page_links`・`references`・`snippets`・`lists`（一覧の4つ）・`entrance`（contest の入口の節）・`reverse`（逆引きの分け方と、分野から症状辞典の章への対応表。DR-15）・`terms`・`hosts`（本体を生成するページ → 置く生成の部分。design §8.4）・`llms`（冒頭の決定の文） |
| `config.py` | 設定と mkdocs.yml（site_name・site_url・site_description）を読む |
| `core.py` | `Gen`：読む層の `Atlas`（held_back を渡す）と設定を合わせ、公開の判定・リンクの書き方（未公開は「題名（準備中）」）・表示の言葉・逆向きの参照（次に読む・振り分け元・台帳の逆リンク）・期限の日（読む層の `expiry` に fact-table の数値を足す） |
| `blocks.py` | 生成の部分（`gen:begin 名前`）の登録（block と inline） |
| `markers.py` | 目印の間を書く（gen・fact・link）。目印の外は1字も変えない。参考の節とページ下部の目印がないページには末尾に足す |
| `pagebits.py` | `references`・`page-links`・`graph` |
| `facts.py` | fact の目印・`fact-table`・`feature`（inline）・`compare` |
| `routes.py` | `routes`（症状の診断の節）・`causes`（症状の原因別の表） |
| `snippets.py` | `snippet <id>/<名前>` |
| `reverse.py`・`terms.py`・`roadmap.py`・`ledger.py` | `signs <type>`・`terms kana／latin／old`・`roadmap`・`ledger` と `timeline` |
| `pages_out.py` | 生成するファイル：nav.yml・分野の入口・一覧・llms.txt・pages.json・graph.json |
| `build.py` | 生成物の全体（ファイル → 中身）と、消す古い生成物 |
| `text.py` | Markdown のエスケープ・表・相対リンク・YAML と JSON の書き方 |

入口 `tools/gen_site.py`：

```sh
uv run python tools/gen_site.py                  # 作り直して、変わったファイルだけ書く（古い生成物は消す）
uv run python tools/gen_site.py --check [--diff] # 比べるだけ（古ければ終了コード 1。CI と commit の前）
uv run python tools/gen_site.py --page <id>      # そのページ（docs/ か stubs/）の目印の間だけを書く（執筆の担当）
uv run python tools/gen_site.py --list-blocks    # 生成の部分の名前の一覧
```

終了コード：0＝最新か書き終えた、1＝--check で古い、2＝読めない（site.yml・mkdocs.yml・設定がない、--page の id がない）。「注意」（ない id・閉じていない目印など）は終了コードを変えない（止めるのは check_pages.py）。

### 1.2 目印の名前（執筆者とメインが本文に置くもの）

| 目印 | 置き方 | 書くもの |
| --- | --- | --- |
| `<!-- link:begin <id>[#<anchor>] -->`〜`<!-- link:end -->` | 文の中 | 公開なら `[題名](相対リンク)`、anchor があれば「題名 › 節の題名」と `#anchor`。未公開なら「題名（準備中）」 |
| `<!-- fact:begin <id> -->`〜`<!-- fact:end -->` | 文の中 | 決まった文（`{value}`・`{unit}`・`{checked}`）。sentence がなければ「{value} {unit}」に「（{checked} 時点）」 |
| `<!-- fact:begin <id> <行> <列> -->` | 文の中 | facts の table の1つのセル |
| `gen:begin references` | 1行ずつ | 見出し `## 参考 {#references}`（手書きの同じ見出しがあれば書かない）と出典。**目印がなく sources があれば末尾に足す** |
| `gen:begin page-links` | 1行ずつ | 前提・次に読む・関連。**目印がなければ末尾に足す**（どのページにも出る） |
| `gen:begin routes` | 1行ずつ | 症状の振り分けの表（原因は site.yml の順、先は routes の順） |
| `gen:begin feature <属性>`・`feature <機能>/<属性>` | 文の中 | 機能の属性（強制力など。機能を省くと tracks の最初） |
| `gen:begin compare` | 1行ずつ | tracks の機能の比較の表（値のある属性だけ） |
| `gen:begin fact-table <id>` | 1行ずつ | facts の table の全体・確認日・出典・食い違い |
| `gen:begin snippet <id>/<名前>` | 1行ずつ | 動作確認を通った雛形を折りたたみ（`??? example`）の中のコードに。通っていなければ「雛形「名前」は、動作確認の後に載せる。」 |
| `signs symptom`・`signs goal`・`signs situation` | reverse-index | 逆引き（§3 の14） |
| `terms kana`・`terms latin`・`terms old` | term-index | 用語索引と旧名（§3 の15） |
| `roadmap`・`graph`・`causes`・`ledger`・`timeline` | roadmap・knowledge-map・six-causes・outdated-advice-ledger・change-timeline-2026 | §3 の16・17。graph は `<div class="ca-graph" data-graph="../../assets/data/graph.json"></div>` |

本体を生成するページと置く部分は `config.yml` の `hosts`（目印がなければ「注意」）。生成の部分の中身は `<!-- textlint-disable -->`〜`<!-- textlint-enable -->` で囲む（B3 の P2）。

### 1.3 生成するファイルと、V への受け渡しの形

| ファイル | 中身 |
| --- | --- |
| `nav.yml` | `nav`：トップ → 公開するページのある分野（site.yml の順）ごとに、入口・chapter のないページ・chapter ごとのページ（order の順。題名は nav_title か title）→ 一覧。`exclude_docs`：docs/ にあって公開しないページ（held_back と、stage が公開の段階でないページ）。`extra.ca`：下 |
| `docs/<field>/index.md` | 公開するページのある分野だけ。chapter ごとの箇条書き（題名・「（整える・下書き）」の印・要約の1文目）。contest の入口に、コンテストの場面を持つほかの分野のページの節 |
| `docs/lists/` | `index.md` と `by-level.md`・`by-surface.md`・`by-principle.md`・`by-scene.md`（値ごとの `## 値 {#値を小文字にし空白を-にしたもの}`。値のあるものだけ。検索から外す） |
| `docs/llms.txt` | 1ページ1行 `- [題名](URL)（id・型・レベル・段階・確認日）：要約`（確認日がなければ「未検証」）。分野ごとの節 |
| `docs/assets/data/pages.json` | 下 |
| `docs/assets/data/graph.json` | 下 |

`nav.yml` の `extra.ca`（V の main.html が読む形にそろえた）：`fields`（id → 表示名）・`types`・`stages`・`surfaces`（id → 言葉）・`levels`（低い順）・`published_stages`・`pages_json: assets/data/pages.json`・`graph_json: assets/data/graph.json`・`lists`（front matter のキー → 一覧のページ。level・surfaces・principle・scenes。type はない）・`expires`（ページの id → 期限の日。値のあるページだけ）・`badges`（ページの id → {maturity, enforcement}。tracks の最初の確認済みの機能）。

`pages.json`（公開するページだけ。1ページ1行）：

```json
{"about": "…", "fields": [{"id","title"}], "types": [{"id","label"}], "levels": [...], "stages": [{"id","label"}],
 "surfaces": [{"id","label"}],
 "pages": [{"id","url"（サイトの根から。symptoms/x/）,"title","nav_title","field","chapter","type","level","stage",
            "surfaces","principle","volatility","summary","updated","verified","checked",
            "confirmed"（verified と checked の新しいほう。verified がなければ null）,"verified_with",
            "expires"（期限の日 YYYY-MM-DD か null）,"expires_by"（page・fact:<id>・feature:<id>）,
            "features": [{"id","title","status","checked", 確認済みなら "maturity","enforcement","load_timing",…}]}]}
```

`graph.json`（ノードは公開するページ、辺は両端が公開のものだけ）：

```json
{"about": "…", "fields": [{"id","title"}], "levels": [...],
 "nodes": [{"id","title","nav_title","aliases","url","field","chapter","type","level","stage","summary",
            "prerequisites": [id],"routes": [{"cause","to": [id]}],"related": [id]}],
 "edges": [{"from": 前提,"to": ページ,"kind": "prerequisite"}, {"from": 症状,"to": 振り分け先,"kind": "route","cause": …}]}
```

辺の from → to は読む向き（前提 → ページ、症状 → 対処）。V の `map.js`・`expiry.js`・`main.html`・`ca.css` は、作業中の版を読んだ限りこの形とキーを受ける（ca-page-links・ca-graph・extra.ca を含む）。

### 1.4 試験 `tests/tools/`

| ファイル | 件数 | 見るもの |
| --- | --- | --- |
| `test_gen_site.py` | 39 | 試験用の置き場所で全体を作る：nav（公開するページだけ・並び・nav_title・exclude_docs・extra.ca と手で数えた期限の日）・入口・一覧・llms.txt・pages.json・graph.json・link と fact と各生成の部分の中身・目印の外が変わらない・参考とページ下部を足す位置・次に読むの上限・textlint の印・--check（書かない・手で書き換えた差を見つける）・公開すると他のページのリンクが書き直る・古い生成物を消す・手書きの入口を上書きしない（--force）・--page（docs/ と stubs/）・全体の生成は stubs/ に触れない・同じ入力で同じバイト・**MkDocs と Zensical の --strict のビルド**（Zensical は入っているときだけ） |
| `test_gen_parts.py` | 22 | 文字の部品・かなの行と語の種類・時期の文字、目印の端の場合（知らない名前・閉じていない・文の中の block・引数の誤り・入れ子・ない anchor とページ・sections にあるが本文にない anchor・数値と機能と雛形の誤り・verified.yaml がない・字下げ・フェンスの中・hosts の目印がない・言葉がない語彙・手書きの参考の見出し） |
| `test_gen_catalog.py` | 10 | **本物の目次から骨格の形のサイトを一時フォルダに作り**（B2 の §4.6 の形）、wave: 1 を draft で docs/ に、ほかを stubs/ にして生成：注意0・nav は第一波の核だけ・生成物のリンクは公開するページだけ・--check・MkDocs の --strict。全ページを draft にしても注意0で作り直しても同じ。本物の config.yml が site.yml の語彙をすべて覆い、対応表と hosts が目次に合う。**本物のリポジトリの生成物が最新** |
| `gen_helpers.py`・`fixtures/gen/` | | 置き場所：docs/ のページ19（stub の段階のもの1・held_back で外すもの1を含む）・docs/index.md・stubs/ の2・data/ の各ファイル・snippets/ の雛形（通ったもの・通っていないもの）・試験用の mkdocs.yml（テーマの上書きを読まない） |

## 2. 確かめたこと

- `uv run python -m unittest discover -s tests/tools`：449件 OK（skip 5。作る層の71件に skip はない。skip は他の担当の試験）。`tests/site` 66件 OK（skip 10）、`python3 -m unittest discover -s tests/hooks` 47件 OK
- `tests/guides` は1件落ちる：C の check_pages.py に検査「sections」が登録され、手引きの「作る予定：check_pages.py「sections」」の書き換えを求めている（意図した動き。B5 の報告 §4 の3）。gen_site.py ができたので、その次に「作る予定：gen_site.py --check／--page」（手引きとチェックリストの8か所）も求められる（§4 の4）
- ビルド（MkDocs 1.6.1・Material 9.8.0・Zensical 0.0.74。uv.lock の版）：
  - 試験用の置き場所：`mkdocs build --strict`（anchor・リンク・nav・exclude_docs の検査が効く設定）と `zensical build --strict` の両方で 0件。外したページと stub の段階のページは作られない。`<div class="ca-page-links" markdown>` は両方で div の中の Markdown が描かれる。`{#使う}` の anchor も両方で h2 の id になる
  - 本物の目次の全357ページを draft にした一時のサイト：生成 0.7秒・注意0、`mkdocs build --strict` 0件（約5秒）。pages.json 252KB・graph.json 324KB・llms.txt 148KB（357ページのとき）
  - 本物のリポジトリ（ページなし）：道具で書いた nav.yml を入れ、本物の mkdocs.yml と今の overrides/（V の作業中の版）で `mkdocs build --strict` 0件（一時のフォルダに出力）
  - B2 の読む層の試験用の置き場所（fixtures/lib の写し）でも止まらずに生成し、--strict が通る
- textlint（B3 の設定）：生成したページで0件。生成の部分の中に置いた表記の揺れは指摘されず、外に置いた揺れは指摘される（試しのファイルで確かめた）
- 同じ入力から同じバイト（2回作って比べる試験）、作った後の --check が通る。日時とハッシュは入れていない
- `uv run --with pyflakes python -m pyflakes`（作る層と試験）：0件（`__init__.py` の登録のための import と、mkdocs があるかを見る import だけ）
- 道具で書いた本物の生成物：`nav.yml`（B1 の仮の手書きの注釈は道具の注釈に替わった）・`docs/llms.txt`・`docs/assets/data/pages.json`・`graph.json`。`gen_site.py --check` は「生成物は最新」

## 3. 決めたこと（設計書に書いていない細部）

1. **公開の判定**：読む層の `Atlas.is_published`（docs/ にあり、stage が published_stages、held_back にない）をそのまま使う。held_back は作る層の設定 `tools/gen/config.yml` の `held_back` に書き（メインが書き換える）、生成した `nav.yml` の `exclude_docs` に出る。C の検査の層は exclude_docs から未公開を数える（C のコードを読んで確かめた）ので、正本は config.yml の1か所
2. **exclude_docs**：held_back のページに加えて、docs/ にあって stage が公開の段階でないページ（docs/ に置いた stub など）も書く。MkDocs の omitted_files で --strict が止まらず、公開しないものが漏れない（置き場所の誤りは C が見る）
3. **stubs/ は全体の生成で触らない**（公開しないうえ、公開のたびに数百の骨格のページに差が出るため）。`--page <id>` は stubs/ のページにも効き、docs/ へ移したときの相対リンクで書く
4. **参考の節とページ下部は、目印がなければ末尾に足す**（参考はページ下部の前、sources があるときだけ）。執筆者が置き忘れても出る。足すのは目印の組だけで、ほかの手書きの文は変えない
5. **参考の節の見出しは目印の間に道具が書く**（`## 参考 {#references}`）。目印の前に同じ anchor の見出しを手で書いたページでは書かない
6. **ページ下部の形**：`<div class="ca-page-links" markdown>` の中に「**前提**」「**次に読む**」「**関連**」と箇条書き。前提がなければ「なし」、次に読むと関連は空なら出さない。次に読むは、症状のページなら routes の先（原因の順）→ このページを前提にするページ（公開を先に、ナビの順）。上限8（`page_links.next_max`）で「ほか N ページ」。関連は前提と次に読むに出したページを重ねない（節を指す関連は出す）
7. **節へのリンク**：文字は「題名 › 節の題名」。#anchor は、相手の本文にその見出し（手書きの `{#anchor}` か、生成の部分が作る見出し）があるときだけ付け、なければページへのリンクにして注意に出す（sections にあっても本文にない anchor で、MkDocs の --strict の anchor の検査が落ちないため）
8. **目印の置き方**：block の生成の部分は目印をそれぞれ1行に置く（文の中に置いたら書かずに注意）。inline は文の中。入れ子は外側だけを書く。閉じていない目印・知らない名前・引数の誤りは書かずに残す。中身の前後に空行を入れる（Python-Markdown の HTML の塊に飲まれないため）。字下げした目印（囲みの中）は同じ字下げで書く
9. **未確認の値は出さない**：data の status が `roles.fact_confirmed`（確認済み）でない数値・機能の属性・名前の変更は、値を書かずに「未確認」とだけ書く（比較の表の行も同じ）。旧名の対応と年表と用語索引の機能名にも載せない
10. **数値の表の1つのセル**は `fact:begin <id> <行> <列>`（読む層の `fact_ids` が最初の語を id と読む形に合わせた）。表の全体は `fact-table <id>`。null のセルは「—」
11. **雛形**：`snippets/<id>/<名前>.<拡張子>`（`.expect.yaml` を除く1つ）を、`snippets/<id>/verified.yaml` の `<名前>.result` が `pass` のときだけ、`??? example "雛形：<expect.yaml の title か名前>"` の中のコードにして写す（中に ``` があれば囲みを長くする）。後ろに「確かめた環境：Claude Code <版>（<系列>）・<モデル>・<OS>・<日付>。要る最低の版：Claude Code <版>」。要る最低の版は expect.yaml の `features`（なければページの tracks）の `since.claude_code` のうち新しいもの。verified.yaml の形は snippets.py の冒頭（案。§4 の3）
12. **機能の属性**は `feature <属性>`（tracks の最初の機能）か `feature <機能>/<属性>` で値だけを書く（成熟度・強制力・圧縮で残るか・入った版など）。比較の表 `compare` は tracks の機能を行、値のある属性を列にし、機能の名前を主のページ（features の page）へのリンクにする
13. **routes の表**は、原因を site.yml の prevents・pitfalls の並び（診断の順）に並べ替え、先は routes の順（近い順）。`causes` は全11の原因を「軸｜原因｜症状のページ」の表にし、ない原因は「—」
14. **逆引き**（DR-15）：同じ文（NFKC・大文字小文字・空白をそろえる）は1行に束ね、行き先に「（アプリ・Claude Code、考え方）」の印。困りごとは症状辞典の章で分け、対処のページは振り分け元の症状のページ（ナビの順の最初）の章、どの routes にもないページは `reverse.field_to_symptom_chapter` で分野から章を選ぶ。この対応表は私が目次の困りごとを読んで決めた（§4 の9）。やりたいことと状況は分野で分ける。束ねた行は最初の行き先で節を決める
15. **用語索引**：語は公開するページの title・nav_title・aliases と、確認済みの機能の title（主のページへ）。機能の主のページを先に、ほかを「（型）」の印付きで。ほかのページの題名と同じ別名は外す。かなは五十音の行、漢字と記号で始まる語は最初の字の順（読みの辞書がないので。見出しにそう書く）、英数字は A〜Z と 0〜9
16. **ロードマップ**：段ごとに、同じ段の前提が先に来る並び（同じ位置はナビの順）。比例則の段で守りの分野でないページは、前提・関連（症状は routes も）に持つ同じ段の守りのページを手前に置く（守りのページがそのページを前提にたどるときは前提を優先）。見出しは `### <段> {#reading-order-<番号>}`
17. **台帳**：行ごとに `### <古い助言> {#<台帳の id>}` と、今どうするか・変わった時期（name の行は names の時期）・状態・原理・かつてなぜ・見つけ方・関わるページ（outdated_advice の逆リンク）・出典。年表は names と advice を時期の順に。時期の書き方は「2026-10 ごろ・Claude Code 2.1.300」
18. **一覧**は design §7 の4つ（レベル別・面別・原理別・場面別）を1ページずつ、値ごとの節にした（値ごとのファイルにすると値から ASCII の名前を作る表が要るため）。値のある節だけ。検索から外す（要約の繰り返しで検索がにごるため）。分野の入口は検索に残す
19. **生成するページ**の front matter は title だけ（一覧は `search: exclude`）。本文に `# 題名` と「tools/gen_site.py が生成する。手で直さない」の印。印のない docs/<field>/index.md は上書きせず注意に出す（`--force` で上書き）
20. **llms.txt の冒頭**：mkdocs.yml の site_name と site_description、決定の最小の文（「この辞典は Anthropic の公式の教材ではない。」。config.yml の `llms.notice`）、行の形・型・レベル・段階の説明（draft は「下書き・未検証」。DR-10 の帯の文）とページ数。「完成」の意味は書かない
21. **JSON** は1要素1行（差を読みやすく、並列の直しで衝突しにくく）。キーの並びは作った順
22. **表示の言葉**は config.yml の `labels`（型・段階・面などの語彙の値 → 言葉）に置き、道具のコードには既定だけを持つ。言葉のない値は値をそのまま出して注意に出す。試験が、本物の site.yml の語彙をすべて覆うことを見る

## 4. 提案

1. **held_back の置き場所（メイン）**：いまは config.yml → nav.yml の exclude_docs → C が読む、で1か所。読む層の `load_atlas` が既定で同じ値を読むようにするなら、held_back を site.yml（published_stages の隣）に移し、lib の `Site` に読ませ、作る層の config.yml から外す。どちらでもよいが、2か所に持たない。また、8a で「波が来た」ページを手で外すのが手間なら、第一波の閉包（check_catalog の数え方）を読む層の関数にし、config.yml に `publish_waves: [1]` のように書いて held_back を道具が出す形にできる（今は作っていない）
2. **site.yml（メイン）**：型・面・段階の表示名を site.yml に `{id, title}` で持つなら、作る層は config.yml の labels の代わりにそちらを読む（今は config.yml にある。語彙の正本は site.yml のまま）
3. **雛形の記録の形（メイン・C の check_templates.py）**：`snippets/<id>/verified.yaml` は「`<名前>: {result: pass か fail, date, claude_code, channel, models, os}`」、`<名前>.expect.yaml` から作る層が読むのは `title` と `features` だけ。キーの台帳（keys.yml）に節を足すなら、この形に合わせるか、形を決めて知らせてほしい
4. **手引き（B5 のファイル。メイン）**
   - 「作る予定：gen_site.py --check」「作る予定：gen_site.py --page」（guides/common.md の 47・233・244・357 行、guides/comparison.md 25、guides/symptom.md 38、checklists/fact.md 20、checklists/template.md 12 の8か所）を「検査：」に書き換える（tests/guides が求める）
   - common.md §4・§10 の「前提・次に読む・関連はテンプレートが出す」を「道具がページ下部の目印の間に書く（目印がなければ末尾に足す）」に、§11 の参考の節に「見出しも道具が書く」を足す
   - 目印の名前を決めた：症状の診断の節は `routes`（symptom.md の案のまま）、比較の表は `compare`、機能の属性は `feature <属性>`、表の数値は `fact:begin <id> <行> <列>` か `fact-table <id>`、雛形の折りたたみは `??? example`（作る層が書くので、執筆者は目印だけを置く）。型の手引き（symptom・comparison・feature）の「目印の名前は、道具とともに確定する」を、§1.2 の表の名前に書き換える
5. **C（検査の層）**：(a) 台帳のページ（outdated-advice-ledger）の anchor には、data の advice の id（作る層の見出し）が加わる。`outdated-advice-ledger#<台帳の id>` を指すリンクの anchor の検査は、front matter の sections に加えてこれを数える。ほかに作る層が作る anchor は `references`・`terms-*`・`terms-latin-*`・`reading-order-<番号>`（作る層の `Gen.anchors(page)` が数える）。(b) check_all.py と CI に `uv run python tools/gen_site.py --check`。(c) exclude_docs には stub の段階の docs/ のページも入る（§3 の2）
6. **縛り（C と B4）**：作る層が書くファイルは `nav.yml`・`docs/*/index.md`・`docs/lists/**`・`docs/llms.txt`・`docs/assets/data/**`（と、手書きのページの目印の間。これは deny にできない）。H2 の deny と試験の例は、この5つに合わせる
7. **V**：§1.3 の形で出している。一覧は by-level・by-surface・by-principle・by-scene で、`extra.ca.lists` に type はない。期限の日はページの上部の data 属性に `extra.ca.expires` から出せる（pages.json を読まずに済む）
8. **設計書（メイン）**：§8.2 の「overrides/ … 生成したサイト用のデータ」を `docs/assets/data/`（pages.json・graph.json。brief-build2 §2）に、§8.2 に `tools/gen/config.yml`（作る層の設定）を足す。§8.5 の「ページ下部：前提・次に読む・関連」は作る層が本文の目印の間に書く（brief-build2 §2）と書く。§7 の一覧は4つで1ページずつ
9. **逆引きの分野から章への対応表（メイン）**：config.yml の `reverse.field_to_symptom_chapter` は、目次で振り分け元のない対処のページの困りごと（111ページ）を読んで私が決めた（例：surfaces → 指示と仕組み、cli → 会話と文脈、api → 返答と品質、team → 長い作業と方針、contest と recipes → 完了と検証）。工程7の「逆引きを生成し、R1 の読者の課題で引いて確かめる」で見直す
10. **llms.txt の冒頭（メイン）**：決定の最小の文のほかに、行の形と語彙の説明の行を書いた（方針の文ではなく形の説明と考えた）。「最小の文だけ」の決まりに当たると判断するなら、config.yml の `llms` と pages_out.py の4行を外す
11. **B3 の P4（textlint_targets.py）**：生成物のパス（§4 の6）を道具の間で共有するなら、作る層の定数を読む形にできる。今は作る層の build.py と pages_out.py に持つ

## 5. 確かめていないこと

- 本物のページ（まだない）での出来：逆引き・用語索引・ロードマップの読みやすさ、ページ下部の長さ、スマホの幅（工程7の試作と V の CSS で見る）
- data が空（6b の前）なので、data から作る部分（台帳・年表・比較の表・数値の表・旧名・機能のバッジ）は試験用の作りものの data でしか確かめていない。load_timings・context_costs の語彙はまだ site.yml にない
- verified.yaml と expect.yaml の形は案のまま（check_templates.py と合うかは C の報告を待つ）
- C の check_pages.py が、作る層の書いたもの（生成の部分の中のリンク・作る層が作る anchor）をどう扱うか：C のコードの一部を読んだだけで、組み合わせて流していない
- V の JS（map.js・expiry.js・filter.js）が、この pages.json・graph.json で実際に描けるか（V の作業中のファイルの冒頭の説明を読んだだけ）
- Zensical の `search: exclude` の扱い（ビルドは通るが、検索から外れるかは見ていない）
- Windows のパス、CRLF のファイル（読む層が改行をそろえて読むので、中身が変わらなければ書かない。変わるときは LF で書く）
- 範囲の外のこと：`uv run --group zensical` で、Zensical の組の依存をこのリポジトリの .venv に入れた（追跡しない環境。`uv sync --locked` で戻る）。ほかの担当の作業中のファイル（tools/checks/・overrides/）を、受け渡しをそろえるために読んだ（変えていない）
- 使用量：道具の呼び出し 約110回。Web の取得 0回
