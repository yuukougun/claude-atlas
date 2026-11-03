# 工程3 T1：目次の検査の道具（tools/check_catalog.py）

- 版：2026-11-04
- 担当：T1（[README.md](README.md) の1段目）
- 書いたもの：`tools/check_catalog.py`・`tests/tools/test_check_catalog.py`・`tests/tools/fixtures/small/`・この報告。ほかのファイルは変えていない。git の操作と Web は使っていない

## 1. 作ったもの

| ファイル | 中身 |
| --- | --- |
| `tools/check_catalog.py` | 目次の検査（1,760行。標準ライブラリと PyYAML だけ。Python 3.10.12・PyYAML 5.4.1 で確かめた） |
| `tests/tools/test_check_catalog.py` | 試験114（unittest） |
| `tests/tools/fixtures/small/` | 試験用の小さな目次。エラーも警告も出ない形にした。`schema/site.yml` は本物の写し、`planning/catalog/README.md` は道具が読むところ（§3 の visual の kind、§4.7 の templates の kind、§5 の表）だけの抜き書き。`registry.yaml`（候補12・台帳1）と7分野のファイル（10ページ）。eval のファイルはわざと置かない（まだない分野の扱いを試すため） |

### 1.1 構造（設計書 §8.3）

- **読む層**：`load_catalog(root)` が site.yml・registry.yaml・分野のファイル・機能の id の表を読み、`Catalog`（`Vocab`・`Registry`・`FieldFile`・`Page`・`Entry`）にする。YAML は SafeLoader を広げ、マッピングの始まりの行（出力の行番号になる）と、同じキーが2回あること（PyYAML は黙って後のものを取る）を記録する。参照の解決は `Catalog.resolve()` の1か所だけで行う（§1.3）
- **検査**：`@check(名前, 重さ)` で関数を登録する（31：エラー10・警告21）。重さは登録のときに決まり、関数は指摘（ファイル・行・ページ・内容・関わる分野）を返すだけ。`-h` の末尾にある検査の一覧は、登録と各関数の docstring から作る
- **出力**：`format_issue`（1件1行）・`format_stats`（集計）・`summary_line`（件数）
- **語彙をコードに書かない**：値の語彙はすべて site.yml から読む。コードにあるのは次の3つだけ
  - 目次の形（キーと値の形の表。README §2・§3）
  - 規則が名指しする語彙：`symptom` の型とサイン、`feature` の型。必須は site.yml の priorities の最初、入口は fields の最初とした。名指しした語彙が site.yml から消えると「設定」の警告が出る
  - 規則の数：前提4・related 20・summary 2文・症状のサイン2

### 1.2 使い方

```text
python3 tools/check_catalog.py                   全分野を検査する
python3 tools/check_catalog.py --field symptoms  その分野に関わる指摘だけを出す（読むのと参照の解決は全体で行う）
python3 tools/check_catalog.py --stats           集計も出す
python3 tools/check_catalog.py -q                警告を出さない（件数だけ出す）
python3 tools/check_catalog.py --root DIR        DIR/schema/site.yml と DIR/planning/catalog/ を読む（試験用）
```

- 終了コード：0＝エラーなし（警告だけなら 0）、1＝エラーあり（`--field` のときは、その分野に関わるエラーで決める）、2＝検査できない（site.yml が読めない、`--field` の分野が site.yml にない）
- 出力の1行は「重さ: ファイル:行: ページの id: [検査] 内容」。行は、ページのマッピングの始まり（`- id:` の行）。ページに関わらない指摘は id を `-` に、id のないページは `(pages の N 番目)` にする
- 並び順：エラーを先に、警告を後に出す。それぞれの中は、ファイル（registry → site.yml の fields の順）→ 行の順
- `--field` で出すのは、その分野が「関わる分野」に入る指摘
  - 分野をまたぐ指摘（id の重複・循環・必須の前提・未処理の候補・registry の分野との食い違い）は、関わる分野のどれで流しても出る
  - 設定の不足、registry.yaml や features.yaml が読めないこと、分野の id でない名前のファイルは、どの分野で流しても出る

試験用の目次に3か所の誤りを入れて流した例：

```text
エラー: planning/catalog/basics.yaml:5: request-vs-lock: [循環] 前提が循環している: request-vs-lock → instructions-ignored → request-vs-lock
エラー: planning/catalog/enforce.yaml:5: hooks-basics: [語彙] type の「featur」が語彙にない（concept・feature・symptom・comparison・recipe・judgment・ledger・guide・hub）
警告: planning/catalog/symptoms.yaml:62: done-but-not-done: [症状の prevents] symptom のページの prevents が空（防ぐ・診断する原因を1つ以上書く）
エラー 2 件（語彙 1・循環 1）、警告 1 件（症状の prevents 1）（分野のファイル 7・ページ 10 を読んだ）
```

`--stats` の例（試験用の目次。分野の行は一部を省いた）：

```text
集計（分野ごと。ページは分野のファイルの pages を数える）:
  start（入口と地図）: 1 ページ｜優先度 必須 1｜レベル なし 1｜型 guide 1｜registry の候補 1（採る 1）
  eval（評価と実験）: ファイルなし｜registry の候補 1
  symptoms（症状辞典）: 2 ページ｜優先度 必須 2｜レベル 整える 1・任せる 1｜型 symptom 2｜registry の候補 4（採る 2・まとめた 1・採らない 1）
  計: 10 ページ｜優先度 必須 6・推奨 4｜レベル 整える 4・任せる 1・仕組みにする 2・回す 1・なし 2｜型 concept 3・feature 3・symptom 2・ledger 1・guide 1｜registry の候補 12（採る 9・まとめた 1・採らない 1）
第一波: 4 ページ（wave: 1 が 3、前提でたどって届くもの 1）｜start 1・basics 1・symptoms 1・changes 1
必須: 6 ページ
```

- 分野の担当の進み具合が見えるように、registry の候補の内訳（採る・まとめた・採らない・ほかの分野・未処理）も出す
- 第一波は wave: 1 のページから prerequisites をたどって数える。分野のファイルがまだない候補に当たったら、「前提でたどれない候補」として id を出す（まだ数えられない分）

### 1.3 参照の解決

| 指す先 | 扱い |
| --- | --- |
| 分野のファイルにあるページの id | 解決する。related の `id#anchor` は、相手の sections に anchor があるかも確かめる |
| registry の候補で、その分野のファイルがまだない（か読めない） | 指摘しない（ファイルができてから確かめる）。比例則では registry の分野で数える |
| registry の候補で、その分野のファイルはあるが、pages・merged・dropped のどこにもない | 警告（未処理の候補） |
| merged・dropped にした候補 | エラー（参照）。まとめた先を案内する |
| どこにもない id | エラー（参照） |

## 2. 検査の一覧

右の列の「頼まれた」は指示の一覧にあったもの、「足した」は私が足したもの。足した理由は §4.2。

### 2.1 エラー（終了コード 1）

| 検査 | 見るもの | |
| --- | --- | --- |
| YAML | YAML が読めない（行と列を出す）。同じキーが2回ある | 頼まれた。同じキーは足した |
| 形 | 値の形（リストのところが文字列、マッピングでない、wave が 1 でない、safety が真偽値でない、最上位がマッピングでない、など） | 足した（README §6 の「YAML の形」） |
| 必須 | ページの id・title・type・priority・summary・volatility と、型による level（site.yml の types_without_level にない型は要る）。ファイルの field・pages、registry の pages・ledger、registry の候補の id・field・title、ledger の id・title、merged の id・into、dropped・new_features の id、signs の type・text、sections の title・anchor、templates の name・kind、visual の kind・text | 頼まれた。要素の中の項目は足した |
| 語彙 | type・level・priority・volatility・surfaces・principle・prevents・pitfalls・scenes、signs の type、visual と templates の kind。ほかに sections の level と、registry の候補の field・type・priority・level | 頼まれた。sections と registry は足した |
| id の書式 | `^[a-z0-9]+(-[a-z0-9]+)*$`。ページ・registry の候補・ledger・merged・dropped・new_features・features.yaml の id と、sections の anchor | 頼まれた。ページ以外は足した |
| id の重複 | ページの id（分野をまたいで）、registry と ledger の id、ページと merged・dropped の間、ページの中の anchor | 頼まれた。ページ以外は足した |
| 分野とファイル名 | field がファイル名と違う。分野の id でない名前の .yaml がある | 頼まれた。後者は足した |
| 参照 | §1.3 のエラー。merged の into も見る | 頼まれた |
| 循環 | 前提の循環。強連結成分で見つけ、1つの循環につき1件、道筋を出す。自分自身を前提にするものも | 頼まれた |
| 前提と関連の重複 | 同じページが prerequisites と related の両方にある（related の `id#anchor` もページとして比べる）。同じリストに同じ id が2回ある | 頼まれた。2回は足した |

### 2.2 警告（終了コードは変えない）

| 検査 | 見るもの | |
| --- | --- | --- |
| 参照の書き方 | prerequisites に `id#anchor` がある。related に自分自身がある | 足した |
| 未処理の候補 | §1.3 の警告 | 足した |
| レベルの逆転 | 前提の level がページより上の段（site.yml の levels の順） | 頼まれた |
| 必須の前提 | 必須のページの前提が必須でない | 頼まれた |
| 比例則 | site.yml の proportional_rule の levels のページが、guard_fields の分野のページを前提にも関連にも持たない。guard_fields の分野のページは除く | 頼まれた |
| 入ってくる道 | どのページの prerequisites・related にも出てこない。入口の分野（start）は除く | 頼まれた |
| summary | site.yml の summary_max_chars より長い、site.yml の summary_banned_words を使っている、3文以上ある | 頼まれた。文の数は足した |
| 症状の signs | symptom のページで、type が symptom のサインが2つ未満 | 頼まれた |
| 症状の prevents | symptom のページの prevents が空 | 頼まれた |
| 機能の tracks | feature のページの tracks が空 | 頼まれた |
| tracks の id | 機能の id の表（features.yaml か README §5）にも、どの分野のファイルの new_features にもない | 頼まれた |
| outdated_advice の id | registry の ledger にない | 頼まれた |
| registry の候補 | 分野のファイルがあるのに、その pages・merged・dropped のどこにもない。registry の分野と違う分野のファイルにある。merged・dropped の id が registry にない | 頼まれた。後の2つは足した |
| registry にない id | ページの id が registry になく、「新規」の印もない | 頼まれた |
| 前提と関連の数 | prerequisites が5つ以上。related が21件以上 | 頼まれた。related は足した |
| id の分野名 | id が自分の分野の名前で始まる | 足した（C0 の提案） |
| 知らない項目 | README §2・§3 の形にない項目 | 足した |
| 章 | chapter がファイルの chapters にない。ページのない章がある | 足した |
| level の付け方 | level を持たない型のページに level がある。sections の level がページより下の段 | 足した |
| wave | 核の分野でないページに wave: 1 がある。核の分野のファイルに wave: 1 のページがない | 足した |
| 設定 | 検査の材料が足りない（registry.yaml がない、site.yml に語彙がない、機能の id の表がない、など）。足りない分の検査はしない | 足した |

## 3. 試験の結果

```text
$ cd /home/yuuki/projects/kyopro2/claude-atlas && python3 -m unittest discover -s tests/tools
..................................................................................................................
----------------------------------------------------------------------
Ran 114 tests in 3.100s

OK
```

- 試験は検査ごとに書いた。`@covers` で記録し、`test_every_check_has_a_test` が、登録した31の検査すべてに試験があることを確かめる
- 多くの試験は、試験用の目次を一時フォルダに写して1か所だけ変え、出る指摘（検査とページの組）が期待とちょうど同じかを見る。ほかの指摘が出ないことも、これで確かめている
- 語彙を site.yml から読んでいることは、site.yml を変えると結果が変わることで確かめた（型を足す・変わりやすさの値を消す・summary の字数と使わない語・比例則の段・入口の分野・level を持たない分野・visual の kind）
- 循環を見つける部分（Tarjan）と、循環の道筋は、乱数で作った300のグラフで総当たりの結果と比べた
- CLI：終了コード（0・1・2）、出力の行の形、`--field` で選ぶ指摘、`-q`、`--stats`、`-h`（検査の一覧が全部出る）を確かめた
- 本物のファイルを読めることも確かめた：schema/site.yml（「設定」の警告が出ない）と catalog/README.md（§5 の表から機能の id 78、visual と templates の kind）
- 本物のリポジトリで流しても落ちないこと（終了コードが 0 か 1 で、Traceback が出ない）を試験に入れた。この報告の時点で planning/catalog/ にあるのは README.md と registry.yaml だけで、`python3 tools/check_catalog.py --stats` はエラー0・警告0だった（候補378・台帳35を読み、registry の中の語彙・id の書式と重複・必須の項目・自分の分野の名前の頭を見た）
- 書きかけの状態も試した。scratchpad に本物の registry と書きかけの enforce.yaml（2ページと merged 1つ）を置いて `--field enforce` で流した
  - 自分の分野の未処理の候補12は「registry の候補」の警告になった
  - まだない分野（basics）の候補への参照は、指摘されなかった
  - 同じファイルのまだ書いていない候補への参照は「未処理の候補」の警告になった
  - エラーは0

## 4. 設計の文書と合わなかった点・決めた点

### 4.1 文書の間の食い違い（提案）

1. **visual と templates の kind の語彙が site.yml にない**（README §3・§4.7 の文にだけある）。道具は site.yml の `visual_kinds`・`template_kinds` を読み、なければ README の「kind は a・b・c」の書き方から読む。提案：site.yml に `visual_kinds: [static, mermaid, dynamic]` と `template_kinds: [settings, hook, skill, subagent, claude-md, prompt, other]` を足す。足せば README の文を読まなくなる
2. **level を持たないもの**：design §3.1 の規則2は「start・guide・hub・ledger は level を持たない」で、start は分野。README §4.3-2 と site.yml の types_without_level は ledger・guide・hub（型）だけ。道具は site.yml に従い、型で決める。いまの registry は、C0 が start の候補を guide か hub にしたので、どちらの読みでも食い違わない。start の分野のページを型によらず level なしにするなら、site.yml に `fields_without_level: [start]` を足せば道具はそれを読む
3. **summary に使わない語**：design §5.3 は「このページ・ここ・扱う・紹介する」、README §4.5-3 と site.yml は「このページ・ここでは・扱う・紹介する・まとめる」。道具は site.yml に従う。提案：design §5.3 を site.yml に合わせる
4. **入ってくる道で除く分野（start）**：site.yml に入口の分野を示すキーがない。道具は site.yml に `entry_fields` があればそれを、なければ fields の最初の分野（start）を除く
5. **道具の層の置き場所**：design §8.3 は読む層を `tools/lib/` に、検査を `tools/checks/` に置く。書いてよいファイルが1つなので、1つのファイルの中で層に分けた（区切りの見出しを付け、読む層の入口は `load_catalog`、検査の登録は `CHECKS`）。土台作り（工程6）で、check_pages.py・gen_site.py と読む層を分け合うときに `tools/lib/` へ移すとよい
6. **features.yaml の形が決まっていない**：道具は次のどの形でも読む。features.yaml があれば README §5 の表より優先する（両方を合わせはしない）。メインが features.yaml を作るときは、このどれかの形にする
   - id の文字列のリスト
   - `{id: …}` のリスト
   - それらを面ごとの見出しの下に置いたマッピング（`features:` の下でもよい）
   - id をキーにしたマッピング

### 4.2 決めた点

1. **比例則**：README §4.3-4 は「任せる幅を広げる内容のものは」と内容で絞る。道具は内容を判断できないので、指示のとおり site.yml の proportional_rule の levels のページをすべて見る
   - guard_fields の分野のページ自身は除いた（確かめる・縛るページが、別の確かめる・縛るページを持つ必要はない）
   - まだファイルのない分野の候補は、registry の分野で数える
   - extend（「仕組みにする」のページが多い）などで警告が多くなりそう。多すぎるなら、notes に「比例則：対象外（理由）」と書いたページを除く、などの印を決めるとよい（提案。いまは作っていない）
2. **未処理の候補を、エラーでなく警告にした**（§1.3）：並列で書いている間は、ほかの担当のファイルが書きかけでも「エラーを0にする」を守れるようにするため。最後まで未処理のまま残る候補は、相手の分野の「registry の候補」の警告と対になって出るので、見落とさない
3. **registry.yaml がないとき**：まだない分野の候補と、存在しない id を区別できない。どちらも「参照」のエラーにし、「設定」の警告で知らせる
4. **prerequisites の `id#anchor`** は警告にした（design §3.2 は related にだけ `id#anchor` を許す）。前提としては、ページへの参照として扱う
5. **「新規」の印**：ページの notes に「新規」があればよい。ファイルの notes か registry の notes に、その id と「新規」が一緒にあってもよい
6. **registry の候補の検査に足したもの**
   - 候補が registry の分野と違う分野のファイルにあるときも警告にした（移したなら registry を直すか、open_issues の提案にする）
   - merged・dropped の id が registry にないときも警告にした（綴りを誤ると、本当の候補が未処理のまま残るため）
7. **registry の候補の必須**：id・field・title だけにした。type・priority・level は見当なので、書いてあるときに語彙だけを確かめる
8. **id の分野名**（足した）：C0 の提案（registry-C0.md §5 の1）のとおり、自分の分野の名前で始まる id だけを警告にする。basics の `context-rot` は指摘しない。いまの registry に当たる id はない
9. **ほかに足した検査**（§2 の「足した」）：作った理由は次のとおり
   - 知らない項目：綴りを誤ると、その項目の検査が素通りになる
   - 章：chapter はナビゲーションの小見出しになる
   - level の付け方：design §3.1 の5
   - wave：README §4.6 の2
   - summary の文の数：README §4.5 の3
   - related の数：README §4.4 の5
   - 参照の書き方：related に自分自身を書いても意味がない
10. **入ってくる道**：まだファイルのない分野があるうちは、その分野からの参照を数えられない。警告の文にそのことを書き添える。merged の into は入ってくる道に数えない
11. **終了コード 2**：site.yml が読めないなど、検査そのものができないときは、エラーあり（1）と分けた
12. **summary の字数**：前後の空白を除き、`len()`（文字の数。全角と半角を区別しない）で数える

## 5. 確かめていないこと

- **本物の分野のファイルでは流していない**（この時点ではまだない）。分野の担当の書き方が README §3 の例とずれたときに、形の検査がどれだけ当たるかは、ファイルがそろってから分かる。分野の担当が `--field` で流して道具の不具合に当たれば、その担当の報告に出る
- 23分野がそろったときの警告の量（特に比例則と入ってくる道）が、目で見て扱える量か
- Python 3.12（設計書 §8.1 で固定する版）では流していない（3.10.12 だけ）。3.10 にない書き方は使っていない
- 次の文章の規則は検査していない（textlint と型ごとの規則に任せる想定）
  - summary に変わりやすい値を書かない（README §4.5-3）
  - だ・である調
  - aliases に題名と同じ語を入れない
  - 半角英数字と全角文字の間の空白
- materials・level_evidence・notes の中身と、工程2で訂正・注記が付いた主張を根拠にしていないか（README §4.5-5）は検査していない
- design §8.6 の CI（GitHub Actions）にはつないでいない（工程6）
