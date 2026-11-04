# 工程6a B2：読む層と data（tools/lib/・schema を作る道具・data の schema と雛形）

- 版：2026-11-04
- 担当：B2（[README.md](README.md) の 6a 1段目）
- 書いたもの：`tools/lib/`（12ファイル）・`tools/make_schema.py`・`schema/keys.yml`・`schema/*.schema.json`（5つ。make_schema.py の生成物）・`data/`（雛形4つと `data/sources.d/.gitkeep`）・`tests/tools/test_lib_read.py`・`test_lib_schema.py`・`test_lib_model.py`・`tests/tools/fixtures/lib/`・この報告
- 変えていないもの：`tools/check_catalog.py`・`tests/tools/test_check_catalog.py`・`tests/tools/fixtures/small/`（読むだけ。試験は一時フォルダに写してから変える）・`schema/site.yml`（語彙を足す案は §4 の1）
- git の操作はしていない。Web は使っていない（依存の版は B1 の pyproject.toml と uv.lock で入ったものを確かめた）。手本の ../kyopro-atlas は読んだだけ
- メインの途中の決定を2つ受けて反映した：outdated_advice の書く人（§3 の11）、stub の置き場所 stubs/（§3 の10）

## 1. 作ったファイルと中身

### 1.1 読む層 `tools/lib/`（設計書 §8.3）

作る層と検査の層が、ファイルを直に読まずに通す層。値を直さず、止まらずに読む（形の違う値は空として読み、YAML の誤りなどは `Problem`〔ファイル・行・文・種類〕に記録する）。誤りとして出すのは検査の層。依存は PyYAML だけ。使い方は `tools/lib/__init__.py` の冒頭にある。

| ファイル | 中身 |
| --- | --- |
| `base.py` | Problem・Fatal、値の読み方（as_text など。check_catalog から写した）、日付（parse_date・partial_date_key）、参照 Ref（id か id#anchor）・Route、YAML の1項目 Record、**PageRecord**（front matter と目次に共通のページの読み方：type・level・prerequisites・routes・anchors・signs・tracks など） |
| `yamlio.py` | YAML を行番号つきで読む（check_catalog の _Loader を写した）。マッピングは LineDict（.line とキーごとの .key_lines）。同じキーの二重を記録。**日付は文字列のまま**読む。front matter の行のずらし（line_offset）。to_jsonable・line_at（schema の誤りの場所 → ファイルの行） |
| `site.py` | schema/site.yml。`Site.vocab(名前)` が任意のキーを語彙のリストとして読む（文字列のリスト・{id, title} のリスト・マッピングのキー。名前のリストはつなぐ）。rank・volatility_days・default_fact_volatility・published_stages・guard_fields など |
| `markdown.py` | front matter と本文の分け方（MkDocs と同じ ---…--- か ...）、フェンス（kyopro-atlas の fence_spans を写した）、見出しと `{#anchor}`、**目印**（gen・fact・link の begin/end。位置を返すので作る層が中身を書き換えられる。対の合わないものは Problem） |
| `pages.py` | `docs/<field>/<id>.md` と `stubs/<field>/<id>.md` → Page（PageRecord に置き場所・URL・本文・目印・見出し）。生成物（docs/<field>/index.md・docs/lists/）は読まない。置き場所の違う Markdown は Problem。Docs.duplicate_ids（同じ id のページ） |
| `catalog.py` | planning/catalog/ → CatalogPage（PageRecord）と registry・merged・dropped・chapters。check_catalog.py の読む層を写したもの |
| `data.py` | data/ の各ファイル → Item。facts・features・names・domains・sources（sources.yml と sources.d/*.yml をまとめる。重なりは捨てずに entries に残す）・advice・inspection。domain_entry（サブドメインはいちばん長く一致するドメイン）・noai_domains・url_key |
| `schema.py` | 小さな JSON Schema（Draft-07 の一部）の検査器。kyopro-atlas の check_pages.py の Validator を写して、format（date・partial-date・regex）・minProperties・required の x-message・誤りの場所（path）を足した。誤りは日本語 |
| `ledger.py` | キーの台帳（schema/keys.yml）を読み、JSON Schema を作る（§1.2） |
| `graph.py` | 強連結成分（check_catalog から写した）・循環・到達・逆向き・前提が先に来る並び |
| `model.py` | **Atlas**：site・ページ・data を合わせたモデル。by_id・duplicates・resolve・anchor_ok・ordered（ナビゲーションの順）・prerequisite_graph・route_graph・prerequisite_order・is_published・**expiry**（期限の日。design §9.2）。`load_atlas(root)`（docs/ と stubs/ と data/）、`load_catalog_atlas(root)`（目次を同じモデルで） |

check_catalog.py の読む層は**写した**（共通にしなかった）。理由：check_catalog.py は変えない指示があり、骨格の後に退く（design §8.3）。検査の層が目次と front matter の両方に同じ規則を当てるには、共通の読み方（PageRecord）が要る。写したものが同じ結果を返すことは試験で確かめた（§2）。読む層の重なりは check_catalog が退くまでの間だけ。

### 1.2 schema を作る道具：`schema/keys.yml` と `tools/make_schema.py`（DR-16）

- `schema/keys.yml`：キーの台帳（design §3.3）の、道具が読む形。page の節は §3.3 の表の31キーを同じ並びで持ち、キーごとに required（all・optional・{types|types_except|stages|stages_except|with|without}）・forbidden・format・writer（書く人）・shows（写る先）・note（検査の層が見る規則）・catalog（骨格で目次から写すか）を書く。**語彙は書かず**、`{vocab: <site.yml のキー>}` で指す。data の節（facts・sources・outdated-advice・inspection）も同じ書き方
- `tools/make_schema.py`：keys.yml と site.yml から `schema/page.schema.json`・`facts.schema.json`・`sources.schema.json`・`outdated-advice.schema.json`・`inspection.schema.json` を作る。`--check` は作り直して比べるだけ（書かない）。終了コード 0＝最新か書いた、1＝古い・ない・keys.yml の誤り、2＝読めない。「注」に、site.yml にない語彙（その語彙は enum にせず、空でない文字列かだけを見る）と、design §3.3 の表と keys.yml の page のキーの食い違いを出す（終了コードは変えない）。生成物に日時やハッシュは入れない

使い方：

```sh
uv run python tools/make_schema.py           # 作り直して、変わったファイルだけを書く（keys.yml か site.yml を直したら流す）
uv run python tools/make_schema.py --check   # CI と commit の前（古ければ終了コード 1）
```

読む層と schema の当て方（作る層・検査の層から）：

```python
from lib import load_atlas
from lib.schema import load_validator
from lib.yamlio import to_jsonable, line_at
atlas = load_atlas(ROOT)                      # docs/ と stubs/ の front matter・data/・site.yml
v = load_validator(ROOT / "schema/page.schema.json")
for page in atlas.ordered():
    for issue in v.errors(to_jsonable(page.raw)):
        print(page.file, line_at(page.raw, issue.path), issue.format())
    atlas.expiry(page).date                   # 期限の日
```

### 1.3 data の schema と空の雛形（design §9.1・§6.8・DR-11・DR-18）

| ファイル | 最上位 | 1項目の主なキー（必須は太字） |
| --- | --- | --- |
| `data/facts.yml` | facts | **id・title**・value か table（どちらか1つ）・unit・sentence（決まった文の型）・match（照合の型：units・before・after・pattern）・**sources・checked・status**・volatility（省くと既定）・versions・conflict（公式同士の食い違い）・note |
| 〃 | features | **id・title・page**（主のページ）・surfaces・maturity・enforcement・load_timing・context_cost・survives_compaction・since（claude_code・date）・match_terms（CHANGELOG で照らす英語の語）・**sources・checked・status**・volatility・note |
| 〃 | names | **id・current・old・changed**（date・until・approx・version）・feature・**sources・checked・status**・note |
| `data/sources.yml`・`data/sources.d/<id>.yml` | domains | **domain・checked・noai**（true・false・null）・url・note |
| 〃 | sources | **id・url・title・kind・publisher・lang・checked**・published・archive（Internet Archive の写し）・note |
| `data/outdated-advice.yml` | advice | **id・title**（古い助言）**・now**（今どうするか）・changed か name（どちらか1つ）・**status・principle**・why_then・how_to_find・**sources・checked**・note |
| `data/inspection.yml` | last | **date・claude_code・release_notes・news**（どれも null 可。前回の点検の版と日付） |

- table（面やモデルで違う値）：`{rows: 行が何か, columns: [列の id か {id, title}], cells: [{row: 行の名前, <列の id>: 値}]}`。値は文字列・数・真偽・null（値を書いた文書がない）か `{value, note, sources}`。モデル × 面の既定の effort（research/23 §3.2）や面の属性の表を、この形で持てる
- 雛形は空のリストと、冒頭の注釈の書き方の例（値はすべて `<…>` の置き場所の印で、実際の値を書いていない）

### 1.4 試験 `tests/tools/`

| ファイル | 件数 | 見るもの |
| --- | --- | --- |
| `test_lib_read.py` | 39 | yamlio（行・二重のキー・日付・行のずらし）、site（本物の site.yml・Fatal）、markdown（front matter・見出し・目印の対と位置・コードの中を読まない）、pages（docs/ と stubs/・生成物・置き場所・front matter の誤りの行・BOM と CRLF・同じ id）、catalog（**check_catalog の読む層と同じ結果**：試験の目次と本物の目次で、ページ・値・行・merged・dropped・registry・ledger・chapters・YAML の誤りの行）、data（まとめ方・ドメイン・重なり・ない/壊れたファイル・keys.yml の節との一致・本物の data/ が読める） |
| `test_lib_schema.py` | 29 | 検査器の単体、keys.yml（本物に誤りがない・**design §3.3 の表とキーと並びが同じ**・書き方の誤り）、生成（語彙が site.yml から来る・ない語彙の注・同じ入力で同じ出力・Draft-07 のメタスキーマ）、**変えた入力 76 通り**（front matter 38・data 38）で誤りの場所が決めたとおりになり、**jsonschema（format も確かめる）と通る・通らないが一致**、**本物の目次の全ページを骨格の形にすると page.schema.json に通る**、make_schema.py の入口（--check・書く・注・終了コード）、**本物の schema/*.schema.json が作り直したものと同じ** |
| `test_lib_model.py` | 18 | Atlas（解決・anchor・グラフ・並び・同じ id・docs/ が stubs/ より先・公開は置き場所と stage の両方・期限の日を手で数えた値と照らす）、本物の目次で前提が先に来る並び、グラフの部品（乱択のグラフで総当たりと照らす） |
| `fixtures/lib/` | | schema/site.yml（本物の写しに §4 の1の語彙を足したもの）・docs/ のページ3つ・stubs/ の骨格のページ1つ・生成物・サイトのトップ・data/ の各ファイル。値はすべて試験用の作りもので、URL は example.* だけ |

## 2. 確かめたこと

- `uv run python -m unittest discover -s tests/tools`：285 件すべて OK（B2 の 86 件、check_catalog の 168 件、B3 の textlint の 31 件）
- 手元の `python3`（3.10.12・PyYAML 5.4.1・jsonschema 3.2.0）でも B2 の 86 件が OK（古い jsonschema の名前にも落とす）
- `uv run --with pyflakes python -m pyflakes`（B2 のコードと試験）：0 件
- `uv run python tools/make_schema.py --check`：5つとも最新。注は site.yml にない語彙の8行（§4 の1を足せば2行になる。一時フォルダで確かめた）
- `uv run python tools/check_catalog.py`：エラー0・警告3（比例則）で、前と同じ。§4 の1の語彙を足した site.yml でも同じ（一時フォルダで確かめた）
- 作った5つの schema は、jsonschema 4.26.0 の Draft-07 のメタスキーマに通る。小さな検査器も読める
- 本物の目次の357ページを骨格の形（keys.yml の catalog のキー23＋field・order・stage: stub・updated・guide と hub のほかは sources: []）にすると、page.schema.json に誤り0（小さな検査器と jsonschema の両方）
- lib の目次の読み方は、check_catalog.py と同じページ・同じ値・同じ行を返す（試験の目次と本物の目次）
- 版：uv run の Python 3.12.15・PyYAML 6.0.3・jsonschema 4.26.0（B1 の pyproject.toml の `pyyaml>=6.0.2`・`jsonschema>=4.23` で入ったもの）。B2 の依存はこれで足りる（jsonschema は試験の照らし合わせだけで使い、なければその試験を飛ばす）

## 3. 決めたこと（設計書に書いていない細部）

1. **キーの台帳の機械で読む形を schema/keys.yml に置いた**。design §3.3 の表と同じキー・同じ並び（試験と `--check` の注が照らす）。台帳が名指しする型と段階（symptom・feature・guide・hub・reviewed・done・stub・draft）は §3.3 の表の言葉のまま書き、site.yml にあるかを道具が確かめる（なければ注）。$id の頭は keys.yml の id_base（`https://raw.githubusercontent.com/yuukougun/claude-atlas/main/schema/`。push の後に編集器から引ける形）
2. **schema に入れるのは、機械で決まる誤りだけ**（型・書式・語彙・必須・台帳にないキー）。check_catalog で警告の規則（症状の signs 2つ以上・prevents 1つ以上・summary の長さと使わない語・wave の分野など）と、参照の解決・循環・逆転・ファイル名との一致は、検査の層に残し、keys.yml の note に書いた
3. **「型による」キー**（surfaces・principle・prevents・pitfalls・scenes・signs）は schema では任意にした。目次の実データで型ごとにそろっていない（例：concept 123 のうち principle を持つのは 119）ため、必須にすると骨格が通らない
4. **必須と「書かない」**：level は types_without_level のほかで必須・その型では書かない。routes は symptom で必須かつ空にしない・ほかの型では書かない。tracks は feature で必須かつ空にしない（目次の feature 88 はすべて空でない）。sources は guide・hub のほかで必須（空のリストは可。骨格は `sources: []`）。prerequisites は全ページで必須（空のリストは可）。verified・verified_with は reviewed・done で必須、**stub・draft では書かない**（draft のバッジは「未検証」。design §8.5・DR-10）。「書かない」は null も書かない（null を許すと必須のときの null も通るため）。verified_with は1つ以上のキー（claude_code・channel・models・app。app は平文）。order は0以上の整数
5. **台帳にないキーは誤り**（front matter も data も入れ子も additionalProperties: false）。search.boost などを使うときは keys.yml に足す
6. **日付は文字列のまま読む**（YAML の timestamp にしない）。2026-13-45 のような値で読むのが止まらず、schema の format: date で日本語の誤りにできる。時期（変わった時期・入った版の日など）は 2026・2026-10・2026-10-27 の形で、年だけの整数（`date: 2026`）も許す
7. **AI の利用の指定はドメインごと**（sources の domains の節）にした。design §6.8「新しいドメインは…確かめ、結果を sources に記録する」の読み。出典ごとに持つと同じドメインの結果を何百回も書くことになる。サブドメインは、いちばん長く一致するドメインの項目に当てる（`WebFetch(domain:*.<d>)` と同じ向き）。noai の null は「確かめられなかった」で、検査の層は未確認に数える
8. **data の形の細部**：facts は value か table のどちらか1つ。§9.1 の候補の表（面の属性・モデルと effort・プランと料金）は facts の table で持てる形にした。大会の規則と AI の成績（contest#4）は第一波の後なので、形が決まったら keys.yml に節を足す。names は facts.yml に置き、台帳の名前の変更の行は name で指して changed を持たない（DR-18。schema で強制）。台帳の why_then・how_to_find は任意にした（必須にすると埋め草が入る。検査の層の警告にする案）。features の page は必須（DR-15：facts.yml に移すときに決める）。数値の volatility は省くと site.yml の default_fact_volatility、それもなければ期限のいちばん短いもの（高）
9. **期限の日**（design §9.2）：数値には、本文の fact の目印が指す facts に加えて、**tracks が指す features も数える**（機能の属性のバッジとしてページに出るため）。verified のないページ（draft・stub）はページの分を数えない。作る層が目印のほかに書く数値（比較表など）は `expiry(page, extra_facts=…)` で足せる
10. **stub の置き場所**（2026-11-04 のメインの決定を受けて）：読む層の既定は docs/ と stubs/ をこの順に読む。同じ id のページ（docs/ と stubs/ の両方、二つの分野）は `Docs.duplicate_ids()` と `Atlas.duplicates` に出し、by_id は先に読んだ docs/ のほうを引く。**公開**は「docs/ にあり、stage が published_stages、held_back にない」。stubs/ に置けるのは `<field>/<id>.md` だけ（index.md・lists/・トップは置き場所の誤り）。置き場所と stage の食い違い（stubs/ に draft、docs/ に stub）は検査の層に任せた
11. **outdated_advice の書く人**（2026-11-04 のメインの決定）：keys.yml では「目次（執筆者は提案）」にした（執筆者が書くのは sections・stage・updated・sources だけ。design §10.2）。page.schema.json の description にも出る
12. **目印の読み方**：1行の HTML のコメント。フェンスと行の中のコードの中は読まない。gen:end には begin と同じ名前を書く（design §8.4 の形）。fact:end・link:end の名前は省ける（書くなら begin と同じ）。種類の違う目印は入れ子にしてよく、同じ種類の入れ子は誤り
13. **小さな検査器を写した**（jsonschema に頼らない）。誤りを日本語と x-message で出し、場所を行に直せるため。jsonschema は試験で同じ結果になるかを照らすのに使う。partial-date は独自の format 名なので、ほかの検査器では pattern だけが効く（月と日の範囲は pattern にも入れた）
14. **生成物の書き方**：JSON を表示の幅 120 で詰め、値だけのリストは折り返す。同じ入力からいつも同じ文字列（design §8.4）

## 4. 提案（ほかの担当のファイル・設計書）

1. **site.yml に語彙を足す**（メイン）。足したら `uv run python tools/make_schema.py` を流して schema/*.schema.json を commit する。試験の置き場所の site.yml には同じものを足してある。check_catalog は知らないキーを読まないので、目次の検査は変わらない（確かめた）

   ```yaml
   # data の語彙（design §9.1・§3.3）
   fact_statuses: [確認済み, 未確認]                 # 数値（facts・features・names）の状態
   default_fact_volatility: 高                       # 数値の volatility の既定（design §9.2「既定は高」）
   source_kinds: [公式文書, 公式ブログ, CHANGELOG, リリースノート, 実践者, 研究, 報道]   # 出典の種類（design §9.1）
   advice_statuses: [撤回, 置換, 条件付き]            # 古くなった助言の状態（design §9.1・research/00 §5）
   maturities: [GA, beta, research preview, experimental]   # 機能の成熟度（requirements §5.2。6b で一次資料の表記を見て直す）
   enforcements: [お願い, 鍵]                         # 機能の強制力（D14）
   channels: [latest, stable]                        # verified_with の channel（design §3.3）
   published_stages: [draft, reviewed, done]         # 公開する段階（design §8.4）
   ```

   load_timings（読み込みの時期）と context_costs（コンテキストのコスト）は、6b で一次資料（Extend Claude Code の比較の列）の表記を見て足す。それまでは空でない文字列かだけを見る
2. **設計書**（メイン）：§3.3 に「道具が読む形は schema/keys.yml（キーを変えるときは両方を直し、make_schema.py を流す）」と、outdated_advice の書く人（メインが直すと聞いた）。§9.1 に、AI の利用の指定をドメインごと（sources の domains）にしたこと、前回の点検を data/inspection.yml に置くこと、名称の表は facts.yml の names、面やモデルで違う値は facts の table。§8.2 の構成に schema/keys.yml・data/inspection.yml・stubs/ を足す
3. **CI と check_all.py**（B1・2段目）：毎回の検査に `uv run python tools/make_schema.py --check` を入れる（front matter の検査の前に）
4. **縛り**（B4）：schema/*.schema.json は生成物なので、H2（生成物を手で書き換えない）の deny の範囲に入れる（直すのは keys.yml か site.yml）。H1 の「sources で断るドメインがすべて deny にあるか」は `atlas.data.noai_domains()` と settings.json の deny を照らせば作れる
5. **2段目の検査の層**：読む層の Problem の種類（YAML・形・front matter・目印・置き場所・設定）を検査の名前に写す。schema の誤りは `line_at(page.raw, issue.path)` で行にする。検査の層に残した規則（keys.yml の note）：id とファイル名、field とフォルダ、chapter が目次の chapters にあるか、sections の anchor が見出しにあるか、置き場所と stage（stubs/ に draft 以上、docs/ に stub）、同じ id のページ、tracks・outdated_advice・sources・names.feature・features.page の解決、sources.d のファイル名がページの id か、出典のドメインが domains にあるか、table の列と cells のキーの対応、台帳の why_then・how_to_find の空、check_catalog の警告の規則（signs・prevents・summary・wave など）
6. **骨格の道具**（6c）：`load_ledger(ROOT).catalog_keys()` の23キーを目次から写し、field（ファイルの分野）・order（pages の並び。試験では10刻みにした）・stage: stub・updated・sources: []（guide・hub のほか）を足して `stubs/<field>/<id>.md` に書けば、page.schema.json に通る（試験で確かめた形）。目次の読み方は `lib.catalog.load_catalog`
7. **6b の担当**：雛形の冒頭に書き方を置いた。features の id と題名の元は planning/catalog/features.yaml（題名と note は仮のもの）。page（主のページ）は必須

## 5. 確かめていないこと

- 2段目の作る層・検査の層から実際に使ったときの使い勝手（API はこれから使われる。足りないものは読む層に足す）
- 目印の読み方が、これから作る gen_site.py の書き方と合うか（design §8.4 の書き方に合わせただけ）
- 見出しは字下げ3つまでを読む（kyopro-atlas と同じ）。タブや囲みの中に書いた見出しの anchor は読まないので、sections の anchor をそこに置くと見落とす
- 編集器（VS Code の YAML の拡張など）で page.schema.json を使えるか（$id の URL は push の前なので引いていない）
- maturities などの語彙の値（requirements §5.2 の案を写しただけで、一次資料の表記を確かめていない）
- Zensical の front matter の読み方との違い（MkDocs と同じ規則で分けた）
- 全ページの本文を書いた後の読む速さ（試験は小さな置き場所と、本文のない目次の357ページだけ）
- 止められた操作：なし。使用量：担当の側では数えていない
