# 工程6c K1：骨格の道具（tools/make_skeleton.py）と試験

- 版：2026-11-04
- 担当：K1（工程6c。共通の指示は [brief-build.md](brief-build.md) §1〜§3・§5）
- 書いたもの：`tools/make_skeleton.py`・`tests/tools/test_make_skeleton.py`・`tests/tools/fixtures/skeleton/`（README・目次7ファイル・空の data 4ファイル）・この報告
- 書いていないもの：リポジトリの `stubs/`（作っていない。本物の骨格は、data をまとめた後にメインが道具を流して作る）。読む層 `tools/lib/`（直したい点は §4 の3）。ほかの担当のファイルと試験用のファイル（読んだだけ）
- git と gh は使っていない。Web は使っていない。止められた操作はない。D3・D4 が書いている `planning/batches/step6/data/` は、D1.yml・D2.yml を読んだだけ（§2.4 の試し）

## 1. 作ったファイルと中身

### 1.1 `tools/make_skeleton.py`（設計書 §5.2 の5・§8.5・§10.1 の 6c）

```sh
uv run python tools/make_skeleton.py              # 目次のページのうち、まだないものの骨格を stubs/<field>/<id>.md に作る
uv run python tools/make_skeleton.py --dry-run    # 書かずに、作る・作り直す・そのままの数を出す（--force と組める）
uv run python tools/make_skeleton.py --force      # stubs/ にある骨格も目次から作り直す（updated のほかが同じものは書かない）
uv run python tools/make_skeleton.py --check      # 目次と stubs/ の front matter の差を出す（書かない。差があれば 1）
uv run python tools/make_skeleton.py --date 2026-11-05   # updated に書く日（既定は今日）
uv run python tools/make_skeleton.py --root DIR   # 根を変える（試験用）
```

終了コード：0＝書き終えた・数え終えた・差がない、1＝`--check` で差がある、2＝作れない（site.yml・keys.yml・page.schema.json・目次が読めない、目次の同じ id、作った front matter が page.schema.json に通らない。このときは1ページも書かない）。`--check` と `--force` は一緒に使えない。

**front matter**（キーの並びは `schema/keys.yml` の page の節の順＝design §3.3 の台帳の表の順。形は design §3.3 の例と同じ：値は1行、signs・routes・sections は1項目1行の `- {…}`、日付は引用符なし）

| キー | 作り方 |
| --- | --- |
| 目次から写すキー | keys.yml で `catalog: true` の23キー（`load_ledger(ROOT).catalog_keys()`）。目次にないキーと値が null のキー（本物の目次では `nav_title: null` の47ページ）は書かない。空のリストは目次のとおり書く |
| field | 目次の分野のファイルの field |
| order | 分野のファイルの pages の並び × 10（10・20・30…） |
| stage | site.yml の stages の最初（stub） |
| updated | `--date`（既定は今日） |
| sources | keys.yml の required（`types_except: [guide, hub]`）を道具が読み、必須のページにだけ `[]`。guide・hub は書かない |
| 書かないキー | verified・verified_with・checked（骨格では書けない）。目次だけの項目（materials・templates・visual・level_evidence・notes） |

書く前に、全ページの front matter を page.schema.json に当て、書いた YAML を読む層で読み直して同じ値になるかを確かめる。1つでも通らなければ、どのページも書かずに 2 で終わる。

**本文**（§3 の1で決めた）：目次の sections を並びのとおり `## <title> {#<anchor>}` で置く。routes を持つページ（症状）は、診断の節（anchor が `diagnosis`）の見出しの下に `<!-- gen:begin routes -->` と `<!-- gen:end routes -->` を置く（執筆者は、診断のチェックリストを見出しと目印の間に書く。symptom.md §3 の例の並び）。ほかは何も置かない（sections のないページは front matter だけ）。

```markdown
---
id: keeps-stopping
title: 確認ばかりで進まない・途中で止まる
（略：aliases から volatility まで）
sections:
  - {title: 原因を安く確かめる順, anchor: diagnosis}
stage: stub
updated: 2026-11-04
---

## 原因を安く確かめる順 {#diagnosis}

<!-- gen:begin routes -->
<!-- gen:end routes -->
```

**すでにあるページ**：docs/ か stubs/ に同じ id（か同じパス）のページがあれば書かない。docs/ のページには `--force` でも触れない。`--force` は stubs/ の自分のパス（`stubs/<目次の分野>/<id>.md`）の骨格だけを作り直し、updated のほかが同じなら書かない（何度流しても差が出ない）。作り直したものの updated は流した日。ほかの分野のフォルダに同じ id の骨格があれば、作らずに「注意」に出す。

**`--check`**：目次のページごとに、stubs/ の骨格の front matter を、目次から写すキー＋field・order で比べる（updated・sources・stage は比べない）。出すもの：`ない:`（骨格がない）・`差:`（キーごとに値。リストは「目次にだけ」「stub にだけ」か「並びか数が違う」）・`置き場所:`（ほかの分野のフォルダにある）・`読めない:`・`重なり:`（docs/ と stubs/ の両方にある）・`目次にない:`（目次にない id の骨格）。docs/ にあるページは比べない（front matter が正のため）。

### 1.2 試験 `tests/tools/test_make_skeleton.py`（27件）

| 組 | 見るもの |
| --- | --- |
| TestMake（5） | 目次の全ページを作る（stubs/ には `<field>/<id>.md` だけ、docs/ に書かない）・**本物の page.schema.json に通る**（読む層の検査器と jsonschema の FormatChecker 付きの両方）・目次のキーを写し、null を書かず、目次だけの項目と verified 類を書かない・field・order・stage・updated・sources の値・キーの並び・yes・null・日付・`a: b` などが文字列のまま読める（読む層と PyYAML の SafeLoader）・design §3.3 の例の形 |
| TestBody（3） | 見出しが sections と同じ並びで H1 がない・routes の目印が診断の節の見出しの下（診断の節の前と後に節のある症状のページも）・節のないページは本文なし・診断の節がないときは本文の最後に置いて注意・**目印の名前が作る層の生成の部分にあり、本物の目次の routes を持つページがすべて診断の節を持つ** |
| TestOverwrite（4） | docs/ にあるページと stubs/ にある骨格を上書きしない・`--force` は変わった stubs/ の骨格だけを作り直し、2回目は何も書かない・ほかの分野のフォルダの骨格を重ねて作らない・読めない骨格を `--force` で作り直す |
| TestCheck（4） | 作った直後は差がない・**差を見つける**（題名・wave の削除・related の増減・sections の並び・order・骨格がない・ほかの分野のフォルダ・読めない・目次にない。updated と sources は差にしない）・書かない・docs/ のページは比べず、stubs/ との重なりを出す・`--force` と組めない |
| TestDryRun（2） | 書かない・`--force` と組むと作り直す数を出す |
| TestCannotMake（5） | page.schema.json・site.yml がない、目次の YAML が壊れている、目次に同じ id、schema に通らない front matter（tracks のない feature・語彙にない priority）で、2 で終わり1ページも書かない |
| TestWithCheckPages（1） | 骨格だけのサイト（data は空）で check_pages.py のエラーが0 |
| TestRealCatalog（3） | 本物の目次と schema を一時フォルダに写して作る：全ページが page.schema.json に通る・`--check` が差を出さない・症状のページの routes の目印が診断の節にある |

`fixtures/skeleton/` は試験用の小さな目次（6分野10ページ。9つの型をすべて持ち、参照は目次の中で解決する）と空の data。schema/ は置かず、試験が本物の `schema/` を写して当てる（keys.yml を変えたときに骨格が通らなくなれば、試験が落ちる）。

## 2. 確かめたこと

### 2.1 試験

- `uv run python -m unittest discover -s tests/tools`：481件 OK（skip 5。K1 の27件に skip はない。前の 454 件も通る）
- `uv run python -m unittest discover -s tests/guides`：14件 OK
- 手元の `python3`（3.10.12・PyYAML 5.4.1・jsonschema 3.2.0）でも K1 の27件が OK
- `uv run --with pyflakes python -m pyflakes`（道具と試験）：0件

### 2.2 本物の目次で作った骨格（一時フォルダの写し）

リポジトリを scratchpad に写し（node_modules・.venv・.git・site/ を除く）、写しの `tools/make_skeleton.py` を流した。

| 確かめたこと | 結果 |
| --- | --- |
| `--dry-run` → 書く | 357ページ（23分野）を作った。約1.9秒・579 KB。2回目は「作った 0・書かない 357」、`--force` は「目次と同じ 357」で何も書かない |
| 本文の形 | 見出しだけ 266・見出しと routes の目印 34（症状のページすべて）・本文なし 57。見出しは合わせて 924、H1 は 0 |
| `make_skeleton.py --check` | 差がない（終了コード 0） |
| `check_pages.py` | **エラー 0 件**、警告 693 件（終了コード 0）。内訳は下の表 |
| `gen_site.py --check` | 「生成物は最新」・注意 0（骨格は生成物を変えない） |
| `check_all.py --only make_schema,gen_site,check_pages,check_catalog,check_templates,check_svg,mkdocs` | 7段すべて通った（textlint と試験の段は写しに node_modules がないので流していない。試験はリポジトリで流した） |

`check_pages.py` の警告の内訳：

| 検査 | 件数 | 理由 |
| --- | --- | --- |
| tracks の id | 541（116種の id） | data の features が空。**骨格のページだけが指すときは警告**（C の検査。draft のページが指すとエラー）。見込みの「エラー」ではなく警告で出た |
| outdated_advice の id | 144（37種。registry の台帳の37行） | data の advice が空。同じく骨格だけなら警告 |
| 平文の欄 | 5 | **目次の値から来る**：signs に `` ` `` があるもの（block-with-exit-2・permission-rules の「`.env` や migrations を…」、protected-paths の「`.claude` や `.git` を…」）、aliases に `<` があるもの（asking-for-reasoning の「<thinking> タグに書かせる」、xml-tags の「<document> で包む」）。`check_pages.py --catalog` でも同じ5件が出る |
| 比例則 | 3 | 目次の警告と同じ（feature-to-api-mapping・prompt-caching-in-practice・agents-md。check_catalog.py の警告3と同じ） |

ほかの種類の誤り（形・置き場所・参照・循環・章・id の重複・目印など）は0件。

### 2.3 骨格から書き始めるときの形（写しで試した）

- `gen_site.py --page keeps-stopping`（骨格のページ）：routes の目印の間に原因ごとの振り分けの表（先は「題名（準備中）」）が入り、ページ下部が末尾に足される。目印の形は作る層が読める
- 骨格を4つ（symptom・guide・hub・concept）そのまま docs/ へ移して draft にすると、エラーは各ページ「要点」と「別名の行」の2つだけで、「sections」は0件（骨格の見出しが sections の検査を満たす）。執筆者は冒頭（要点・別名の行・導入）と各節の中身を書けばよい

### 2.4 data をまとめた後の見込み（写しで試した）

D1.yml・D2.yml の features（117）・domains（7）・sources（172）を、id で重ねを除いてそのまま写しの data/ に入れて流した。

- 骨格あり：エラー 0、警告 152（outdated_advice の id 144・平文の欄 5・比例則 3）。**tracks の id の警告は0**（D1 と D2 が目次の116種の tracks の id をすべて持つ）
- **骨格なし：エラー 117（data の参照 117）**。features の page（主のページ）が、まだどこにもページがないため解決しない（例：`features の「claude-md」の page「what-to-put-in-claude-md」のページがない`）

data をまとめた commit で骨格がないと、CI の check_pages が落ちる（§4 の1）。

## 3. 決めたこと（設計書に書いていない細部）

1. **本文は sections の見出しと、症状の routes の目印だけ**にした。手引き（planning/guides/）を読んだ判断：
   - 型の手引きの「構成の目安」の見出しは置かない。design §2.2「ページの構成は固定のテンプレートにしない」と common.md §4「型の手引きの構成は目安である。目安のための薄い節を作らない」のため。各型の「必ず持つもの」も、見出しの決まった節ではない（判断例は `!!! example` の囲み〔common.md §7〕、比較の表と台帳の表は目印、feature の属性はバッジ）
   - sections の見出しは置く。ほかのページが `id#anchor` で指す節で、anchor は骨格の後に変えない（common.md §2.2「既にある節（骨格で写した節を含む）の anchor は変えず、節も外さない」）。draft にすると check_pages.py「sections」が本文に求める
   - 症状の routes の目印は置く。symptom.md §3 が診断の節の中の位置と目印を決めていて、置き忘れても今はどの検査も気づかない（§4 の4）。症状のページの34すべてが診断の節を持つ
   - 置かないもの：H1（common.md §4。題名はテンプレートが出す）、要点の囲みと別名の行（中身のない項目が下書きで出るおそれがあり、骨格の後に front matter が変わると古くなる。書く人が common.md §3 で書き、check_pages が見る）、本体を生成するページの目印（作る層の hosts。どの節に置くかは書く人が決めることで、ないと gen_site.py が注意に出す）、参考とページ下部の目印（作る層が末尾に足す）
2. **null のキーは書かない、空のリストは書く**。null は読む層でも MkDocs のテンプレートでも書かないのと同じに読まれ、`nav_title: null` の47行が余計になる。空のリスト（`pitfalls: []` など）は目次が明示した「ない」なので残す。`--check` は null と「ない」を同じに比べる
3. **キーの並びは keys.yml の順**（目次の並びに頼らない）。入れ子のマッピング（signs・routes・sections の項目）のキーの並びは目次のまま
4. **order は10刻み**（後でページを挟めるように。B2・G の試験と同じ）。分野の中の pages の並びで、章をまたいで数える
5. **sources は keys.yml の required の条件を道具が読む**（型の名前をコードに書かない）。条件の読み方は lib/ledger.py の Builder.condition と同じにした（§4 の3）。stage は site.yml の stages の最初
6. **YAML は PyYAML の SafeDumper の流れの書き方で値を書き、引用符は要るときだけ付く**（`'yes'`・`'a: b'` など）。日付のキー（keys.yml の format が date のもの）だけ date として書き、引用符なしの `updated: 2026-11-04` にする（design §3.3 の例の形。ほかの日付に見える文字列は引用符で囲まれ、MkDocs でも文字列で読まれる）
7. **`--force` は updated のほかが同じなら書かない**。作り直すたびに357ファイルの日付が変わる差を出さないため。作り直したものの updated は流した日（骨格は読者に見えないので、updated は骨格を作った日の意味）
8. **`--check` は CI に入れない前提**で作った。骨格の後は front matter が正なので、メインが提案を front matter に反映すれば目次との差は出てよい。骨格を作った直後と、目次を直して作り直すかを決めるときに使う
9. **定数**：routes の目印の名前 `routes` と診断の節の anchor `diagnosis` は道具の定数（symptom.md §3 と catalog/symptoms.yaml の冒頭の決まり）。試験が、作る層の生成の部分の名前と本物の目次に合うかを見る
10. **作れないときは書かない**：目次の読み込みの指摘（YAML・形・registry がない、など）が1つでもあれば止める（check_catalog.py で直してから流す）。目次の同じ id・`index` の id も止める

## 4. 提案

1. **流す順（メイン）**：data をまとめる commit と骨格を同じ commit にする（か、骨格を先に作る）。骨格のない data は features の page が解決せず、check_pages のエラーが117件出る（§2.4）。骨格は今の空の data でもエラー0で作れる。手順：
   1. `uv run python tools/make_skeleton.py --dry-run`（作る 357）
   2. `uv run python tools/make_skeleton.py`
   3. `uv run python tools/make_skeleton.py --check`（差がない）
   4. `uv run python tools/check_pages.py`（エラー0。警告は data にない id の参照と、§2.2 の目次から来る8件）
   5. `uv run python tools/gen_site.py --check`（生成物は最新のまま）と `uv run python tools/check_all.py`
   6. stubs/ を commit する。design §8.3 のとおり、骨格の後は check_catalog.py が退く（check_all.py の check_catalog の段は「骨格の後に外す」と書いてある）
2. **目次（メイン）**：平文の欄の警告5件（§2.2）は目次の値から来る。骨格の前に目次で直せば、骨格はきれいに出る（骨格の後は front matter が正なので、直すなら front matter で）。比例則の3件は notes に理由があるので、そのままでよい
3. **読む層（B2・メイン）**：keys.yml の required の条件を、あるページに当てて「必須か」を返す関数を lib/ledger.py に置く（例：`Ledger.required_for(key, meta, site)`）。今は schema を作る Builder.condition と、骨格の道具の `Skeleton.holds` が同じ読み方を別々に持つ（読む層を直さない指示なので写した）。検査の層が型ごとの必須を言うときにも使える
4. **検査の層（C）か作る層（G）**：docs/ の症状のページに routes の目印がなくても、今はどの検査も気づかない（gen_site.py は hosts のページの目印だけを注意に出し、check_pages.py に規則がない）。check_pages.py に「症状のページ（routes を持つページ）の本文に `<!-- gen:begin routes -->` がない」を足す（design-review の DR-02 と symptom.md §3。重さは誤りでよいと考える）。目印の名前と診断の節の anchor を設定に持つなら、作る層の config.yml の roles に `diagnosis_anchor: diagnosis` を足し、骨格の道具もそこから読む形にできる
5. **手引き（B5 のファイル・メイン）**：common.md §19（段階と更新日）か §2.1 に、骨格から書き始める手順を足す。「stub を draft にするときは `stubs/<field>/<id>.md` を `docs/<field>/<id>.md` へ移し、stubs/ に残さない（残すと check_pages.py「id の重複」）。骨格の本文には sections の見出しと、症状のページは routes の目印がある。冒頭（要点・別名の行・導入）と各節の中身を書き足す」。design §8.5 の「draft にするときに docs/ へ移す」を、誰が移すか（執筆者）まで書く
6. **設計書（メイン）**：§8.3 の入口の CLI の `make_skeleton.py` ができた。§10.1 の 6c の終わりの条件「全ページが stub 以上」は、§4 の1の手順の後に満たす

## 5. 確かめていないこと

- リポジトリの stubs/ に作ったときの結果（指示どおり作っていない。写しでの結果は §2.2）。D3・D4 の data（台帳・第一波の出典）が入った後の結果（§2.4 は D1・D2 の features・domains・sources を重ねを除いて入れただけで、メインのまとめ方とは違いうる）
- Zensical のビルド（骨格は docs/ の外なので読まないはずだが、写しで流していない）と textlint（textlint_targets.py は docs/ だけを見るので、stubs/ は対象外）
- 執筆者が骨格から書き始めたときの使い勝手（工程7の試作で見る）
- Windows のパスと CRLF の骨格（CRLF は LF に直して比べる）
- 使用量：道具の呼び出し 約60回。Web の取得 0回
