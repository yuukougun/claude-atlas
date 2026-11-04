# 工程6a 2段目 V（見た目）の報告

- 担当：V（2026-11-04）
- 指示：[brief-build.md](brief-build.md) の §1〜§3・§5、[brief-build2.md](brief-build2.md)（全部。受け持ちは §1 の V の行、要点は §3 の V）、[README.md](README.md) の「1段目の報告への判断」
- 書いたもの：`overrides/`（main.html・assets/css/・assets/js/ の3つ・assets/vendor/ の写しと SOURCES.txt）・`tests/site/`（試験2つ・Node.js の試験の道具・試験用のページ）・この報告。B1 の骨組み（冒頭とフッターの文・partials/source.html・mermaid-local.js・Mermaid の写し）は変えていない
- git と gh の操作はしていない。kyopro-atlas は読んだだけ（写して直した）。Web は npm のレジストリ（版と tarball の確かめ）だけに使った
- 作る層 G の途中の出力（tools/gen/pages_out.py・pagebits.py・config.yml と、生成した nav.yml。10:00〜10:15 ごろに読んだ）に合わせた

## 1. 作ったファイルと中身の要約

| ファイル | 中身 |
| --- | --- |
| `overrides/main.html` | B1 の骨組みに足した。冒頭の帯（announce）は変えていない。**ページ上部**（front matter に id のあるページ。題の h1 の直後、冒頭の要点の前）：下書きの帯（stage が draft。文は DR-10 の「下書き・未検証」）、期限切れの注意書きの枠（隠しておき JS が出す）、バッジの列（レベル・型・面・原理・成熟度・強制力・変わりやすさ・確認日と版・段階）。**ページ下部**：「知識マップでこのページの前後を見る」、段階と更新日、「このページの誤りを報告する」（トップのほかの全ページ）。nav_title のあるページの見出しを front matter の title に戻す（kyopro-atlas #91 の直し）。CSS と JS は styles・scripts のブロックで読む |
| `overrides/assets/css/ca.css` | 接頭辞 ca-。バッジ・帯・注意書き・ページ下部（G の `div.ca-page-links` を、見出しを左・項目を右に並べる）・最後の行・知識マップ・絞り込みの欄・指の 44px・狭い画面の表（kyopro-atlas #55 の写し）。色は Material の変数と --ca-* だけ。外の url() なし |
| `overrides/assets/js/expiry.js` | 期限切れの注意書き。期限の日（`data-ca-expires`。G の `extra.ca.expires` の値をテンプレートが出す）とブラウザの今日を比べ、過ぎていれば日付を入れて出す（当日はまだ。tools/lib の Expiry.expired と同じ）。data 属性がなければ pages.json を1回だけ読んで引く。読めなくても止まらない |
| `overrides/assets/js/filter.js` | kyopro-atlas の filter.js を写して直した。照合の規則 `window.CAMatch`（NFKC・大文字小文字・カタカナとひらがな・区切りの記号）と、表の行（か箇条書き）を絞る欄 `<div class="ca-filter">`。言い換えの組はコードに持たず、欄の `data-ca-synonyms`（JSON）か `CAMatch.addSynonyms` で足す。例の文は `data-ca-placeholder` |
| `overrides/assets/js/map.js` | kyopro-atlas の map.js を写して直した。G の `<div class="ca-graph" data-graph="…">` に graph.json（G の nodes・edges の形。pages と prerequisites・routes の形も読む）を描く。分野ごと（`data-field` か、辺のある最初の分野）・焦点（`?focus=`。祖先と子孫、関連の囲み）・全体（分野）の表示。辺は前提（実線の灰）と振り分け（破線の橙）で、たどるときは両方を使う。色の段は graph.json の levels の順。進捗の塗り分け（理解の記録）と頻度の並べ替えは外した |
| `overrides/assets/vendor/cytoscape-3.34.4/` | cytoscape.min.js（約 435KB）と LICENSE（MIT）。地図のあるページでだけ読む |
| `overrides/assets/vendor/cytoscape-dagre-4.0.1/` | cytoscape-dagre.min.js（dagre 3.0.0 と graphlib 4.0.1 を内蔵）と LICENSE・LICENSE.dagre・LICENSE.graphlib |
| `overrides/assets/vendor/SOURCES.txt` | 上の2つの出所（tarball の URL・sha512・写したファイル・sha256・版の理由）を足した |
| `tests/site/test_site_parts.py` | 試験 29 件（下の §2.1） |
| `tests/site/test_site_parts_browser.py` | 試験 8 件。`CA_CHROME` があるときだけ動く（B1 の test_site_browser.py と同じ形） |
| `tests/site/js/parts_harness.cjs` | expiry.js・filter.js・map.js の DOM の要らない部分を Node.js で動かして結果を JSON で返す（試験から呼ぶ） |
| `tests/site/fixtures/parts/` | 試験用のページ 11（トップ・案内・地図・逆引き・用語集・概念・機能・判断・症状・一覧2）と、G の出力の形をまねた pages.json・graph.json・nav.yml（extra.ca あり）・nav-plain.yml（extra なし） |

### 1.1 テンプレートが読む値（`config.extra.ca`。G が nav.yml に書く）

| キー | 使い方 | G の出力 |
| --- | --- | --- |
| `levels` | レベルのバッジの色の段（ca-lv-1〜5） | ある |
| `types`・`surfaces`・`stages`（`labels` の下でも読む） | 型・面・段階の表示名。ないものはバッジを出さない | ある |
| `lists` | {front matter のキー: 一覧のページ（lists/by-level.md）}。バッジを一覧の節（値を小文字にして空白を - にした anchor。G の list_anchor と同じ）へのリンクにする | ある |
| `expires` | {ページの id: 期限の日}。ページ上部の `data-ca-expires`（値のないページは空）。ないときは JS が pages.json を読む | ある |
| `badges` | {ページの id: {maturity, enforcement}}。成熟度と強制力のバッジ | ある |
| `pages_json` | pages.json の置き場所（`data-ca-pages-json`） | ある |
| `report_template` | 誤りの報告を Issue のテンプレートの欄（page-title・page-url・page-verified・page-updated）に入れて開く。なければ題と本文だけ | ない（§4 の8） |

名指しのページは id で nav.pages から引く（how-to-use：帯と注意書きのリンク先の節 stage・freshness と、その節の題。knowledge-map：地図へのリンク）。nav にないときはリンクにしない。

## 2. 確かめたこと

### 2.1 試験

`uv run python -m unittest discover -s tests/site`（B1 の試験と同じ置き場所）：

| 条件 | 結果 |
| --- | --- |
| `CA_CHROME`（Chrome for Testing 146 の chrome-headless-shell）あり | **66 件すべて OK**（B1 の 29 件と V の 37 件） |
| `CA_CHROME` なし | 56 件 OK・10 件は飛ぶ（ブラウザの試験。B1 の2件と V の8件） |

V の試験の中身：

- **テンプレート（MkDocs）**：試験用のページを本物の overrides/ と mkdocs.yml（site_url だけ替える）で `--strict` ビルドし、ページ上部が h1 の直後で要点の前にあること、見出しが front matter の title（nav_title・& を含む題）、帯は draft だけ、注意書きの枠（隠す・`data-ca-expires`・`data-ca-pages-json`）、型ごとのバッジの並びと値（レベルの段の class・一覧への anchor・面の順・確認日と版・title のモデルと点検の日・未検証・段階）、地図へのリンクは辺のあるページだけ、最後の行（段階・更新日）と報告の URL の引数、id のないページ（トップは報告のリンクも出さない）、CSS と JS の読み込みの順
- **extra のない nav**：ビルドが止まらない、型・面・段階・成熟度のバッジを出さない、レベルは色の段なし（ca-lv-0）でリンクにしない、報告は本文に書く形
- **Zensical**（zensical の組があるとき）：同じページを `zensical build --strict` し、部品（見出し・帯・注意書き・バッジ・リンク先・最後の行・報告の URL）が MkDocs と同じ（相対の URL は解いて比べる）
- **静的**：CSS と JS に外の URL がない、`localStorage` などの端末への保存と進捗の部品の語がない、テンプレートの式で Python のメソッドを呼ばない、冒頭の文、写しの sha256 が SOURCES.txt と一致し map.js が読む版がある、古い版が残っていない
- **色**：レベルの段（ライトとダーク）の明るさの単調さ・背景に近い端の 2:1・段の中の字の 4.4:1、帯と注意書きの字の 4.5:1、振り分けの辺の 3:1（WCAG の式を試験に持つ）
- **JS の中身**（Node.js があるとき）：期限の比べ方（当日はまだ、形の違う日付は比べない）、照合の規則（全角・ハイフン・カタカナ・言い換え・送り仮名・同じ組を二度足さない）、graph.json の読み方（G の形、ページの形、ない id・自分・重なり・#anchor・6段目以上・空）
- **ブラウザ**（`CA_CHROME`）：期限の日が過ぎたページだけに注意書きが出る（data 属性・pages.json・pages.json が読めない・HTML に書く形）、地図の3つの表示と関連の囲み・振り分けの辺・`?focus=` で開く・instant navigation で移った先でも描く・地図のないページは Cytoscape.js と graph.json を読まない、絞り込み（言い換え・全角・2語・当たらない語・語を消す・`?filter=`・要点の前へ移る・最後の行は隠さない）、幅 390px のライトとダークで横にはみ出さずレベルの色が配色どおり、どの場面も外のサイトへの問い合わせ0件・JS のエラー0件

### 2.2 描画（手元の Chrome 146、幅 390px と 1280px、ライトとダーク。スクリーンショットを見た）

- バッジの列は折り返して収まる。帯（琥珀）と期限切れの注意書き（赤）、ページ下部（G の前提・次に読む・関連、「準備中」の平文）、最後の行が崩れない
- 知識マップ：分野ごと（外の分野の前は破線の枠、先の分野は「→」の点）と焦点の表示（振り分けの辺は破線の橙）が描ける
- 規模：ページ 360・辺 602 の作りもののサイトで、ビルドは 2.67 秒（V の部品を外したテンプレートでは 2.29 秒）。分野ごとの表示は読める倍率で描ける。全体（分野）の表示は、作りものの辺が乱数で全分野をつなぐため、線の塊になった（本物の辺で見直す。§5）
- 日本語のフォントがこの WSL にないので、字は豆腐になる（B1 と同じ）。見たのは並びと大きさだけ

### 2.3 ビルド

- 本物のリポジトリ（G が生成した nav.yml と docs/index.md）で `uv run mkdocs build --strict` が通る（B1 の BuiltSiteTest も通る）。トップには V の部品を出さない
- 試験用のページで MkDocs 1.6.1＋Material 9.8.0 と Zensical 0.0.74 の両方が `--strict` を通る（Zensical は「No issues found」）

### 2.4 版と写し（2026-11-04、npm の公式レジストリ）

| もの | 結果 |
| --- | --- |
| cytoscape | latest は 3.34.4（2026-10-15 公開）。tarball の sha512 がレジストリの integrity と一致 |
| cytoscape-dagre | latest は 4.0.1。tarball の sha512 が一致。min.js は kyopro-atlas の写しと同じ中身。内蔵の dagre 3.0.0・graphlib 4.0.1 は版の文字列で確かめ、それぞれの tarball（sha512 一致）の LICENSE を写した |

### 2.5 色の決め方（dataviz の方法。validate_palette.js で確かめた）

- レベルは順序のある5段なので、1つの色相（文書化された青の段）の明るさの段にした。ライト（背景 #fff）は 250・350・450・550・650 の段、ダーク（slate の背景 ≒ #1e2129）は向きを返して 550〜150 の段（600 の段はダークの背景に 1.99:1 で 2:1 に足りなかった）。`--ordinal` の検査がライトとダークの両方で通る
- 段の中の字は APCA で読みやすい方（黒か白）。WCAG ではいちばん低い段で 4.42
- 振り分けの辺は分類の色の2番目（橙。ライト 3.20:1・ダーク 4.14:1）。前提の辺は灰の実線で、線の形でも分かり、凡例を出す

## 3. 決めたこと（設計書に書いていない細部）

1. **CSS と JS は overrides/main.html の styles・scripts のブロックで読む**（mkdocs.yml は2段目の誰の受け持ちでもないため）。順は mermaid-local.js（extra_javascript）の後に expiry・filter・map
2. **ページ上部は h1 の直後に置く**（design §6.4「要点の上のバッジの列」）。Material の content.html が出す `<h1>題</h1>` を探して後ろに入れ、見つからない（本文に h1 を書いた）ときは本文の前に置く
3. **語彙の表示名はテンプレートに書かない**。G の `extra.ca` から読み、ないものは出さない（型・面・段階のバッジ、レベルの色の段、一覧へのリンク）。下書きの帯の文「下書き・未検証」は DR-10 の決まった文なのでテンプレートに書いた
4. **バッジ**：レベル（色の段・一覧へのリンク）、型、面（front matter の順）、原理（一覧があればリンク）、成熟度と強制力（G の badges の値をそのまま。どのページに何を出すかは G が決める）、変わりやすさ、確認日と版（`2026-11-03・Claude Code 2.1.317（stable）`。モデルと点検の日〔checked〕は title。verified がなければ「未検証」）、段階（reviewed・done だけ。draft は帯）
5. **期限切れの注意書き**：テンプレートが枠（「確認の期限切れ」「このページの確認の期限（日付）を過ぎている。」と how-to-use#freshness へのリンク）を隠して出し、JS が日付を入れて出す。文はテンプレートにあるので、JS が動かないときは出ない。期限の日の当日は出さない
6. **帯と注意書きのリンクの文**は、how-to-use の front matter の sections の題（「段階・下書きの帯・「準備中」の題名」「確認日と期限切れの注意書き」）を使う。how-to-use が公開されるまではリンクを出さない
7. **知識マップへのリンク**は、前提か routes の辺が公開しているページとの間にあるページだけに出す（辺のないページの焦点の表示は点1つになるため）。G のページ下部の目印の中には入れない
8. **誤りの報告**：GitHub の新しい Issue（題「誤りの報告：<題名>」、本文に題名・URL・確認日〔draft は未検証〕・更新日）。labels などの引数は付けない（権限のない人が開くと 404。kyopro-atlas と同じ）。**サイトのトップには出さない**（トップは決定の最小の文だけにする。brief-build §3）。生成の分野の入口と一覧には出す
9. **知識マップ**：辺の2種類（前提・振り分け）を同じにたどる（症状のページの前は前提、先は振り分けの先）。始めの分野は地図の div の `data-field`、なければ辺のある最初の分野（分野の id を書かない）。関連は配置に使わず、焦点の表示で囲みに出す（比例則の守りのページがここに見える）。「ページ」欄は題名・短い題名・別名・id で探す
10. **絞り込みの欄**：言い換えの組をコードに持たない（kyopro-atlas は手法の組を直書きしていた）。単位の名は「行」（表）と「項目」（箇条書き）
11. **Cytoscape.js は 3.34.4**（kyopro-atlas の 3.34.3 の後の patch。latest）
12. **Zensical の違い**：`page.is_homepage` がない（Zensical の base.html の title でも空になる）ので、トップは URL が空のページとしても見る。ページ自身への相対の URL を `././` と書く（MkDocs は `./`。同じ所を指す）
13. **持ち込まなかったもの**：進捗の部品（理解の記録・読みたいページの記録・記録の書き出し）、節のレベルの印（design §3.1 の5 で任意。使うと決まったら足す）、準備中の帯（stub はビルドに入らない）、404 のページ（受け持ちの外）

## 4. 提案

**作る層 G へ**

1. graph.json のノードに `aliases` を足す（地図の「ページ」欄で別名・旧名から探せる。map.js はあれば使う）
2. 逆引き・用語索引のページの生成の部分に、絞り込みの欄 `<div class="ca-filter"></div>` を置く（箇条書きなら `data-ca-units="li"`、節を絞るなら `data-ca-sections="<## の id …>"`）。言い換えの組は用語集（と prh.yml）から `data-ca-synonyms='[["plan mode","プランモード","plan モード"], …]'` に書ける
3. 知識マップの生成の部分の div に、始めの分野 `data-field="<分野の id>"` を書ける（書かなければ辺のある最初の分野）
4. ページ下部（page-links）に地図へのリンクは足さない（テンプレートが出す）。`extra.ca.lists` の anchor の作り方（値を小文字・空白を -）を変えるときは、テンプレートも合わせる
5. design §8.5 は強制力を「feature の」バッジとしている。G の badges は tracks を持つどの型のページにも強制力を出すので、feature だけにするかを G とメインで決める（テンプレートは badges のとおりに出す）

**検査の層 C へ**

6. render_pages.py に、`test_site_parts_browser.py` の PROBE の見方を入れると全ページで確かめられる：地図のページで `div.ca-graph` に地図が描かれ（`caMap` がある・状況の行に「表示できなかった」がない）、JS のエラーがない、幅 390px のライトとダークで横にはみ出さない（`scrollWidth <= innerWidth`）。ダークは `--blink-settings=preferredColorScheme=0` で開ける

**メインへ（設定・設計・承認）**

7. **期限切れの注意書きの文**（「確認の期限切れ」「このページの確認の期限（日付）を過ぎている。」）と、**誤りの報告のリンクの文**（「このページの誤りを報告する」と title）を、作者の承認（how-to-use の節 freshness・report と同じ回。design §6.1 の8）に入れるかを決める。いまは事実だけの最小の文にした
8. Issue のテンプレート `.github/ISSUE_TEMPLATE/page-error.yml`（design §9.5。欄の id は page-title・page-url・page-verified・page-updated、種類に「情報が古い」）を作り、`extra.ca.report_template: page-error.yml` を mkdocs.yml の extra に書く（INHERIT で nav.yml の extra.ca と合わさる）。それまでは題と本文を入れた空の Issue を開く
9. design §8.5 に書き足す：CSS と JS は overrides/main.html で読む（extra_css・extra_javascript に書かない）、テンプレートが読む `extra.ca` のキー（§1.1）、期限の日は `data-ca-expires` で渡し pages.json は予備、レベルの色の決め方（§2.5）、地図の辺の見せ分け、トップには報告のリンクを出さないこと
10. CI：`tests/site` の ScriptLogicTest は Node.js を使う（GitHub の ubuntu-latest にはある）。ZensicalTest は zensical の組があるときだけ動くので、zensical.yml に `uv run --group zensical python -m unittest tests.site.test_site_parts` を足すと、Zensical で部品が同じかを CI でも見られる
11. 知らせ：作業の途中（10:03）に、共有の `.venv` に zensical の組が入った（V は入れていない。V の Zensical の確かめは別の環境〔scratchpad〕と、入った後の `.venv` で行った）。だれかが `uv sync` で組を外すと、ZensicalTest は飛ぶ

## 5. 確かめていないこと

1. **G の本物の生成物**：G の pages.json・graph.json・一覧は、この報告の時点でリポジトリになかった（nav.yml だけ）。G のコード（pages_out.py・pagebits.py）の形をまねた試験用のデータで確かめた
2. **日本語のフォントでの見た目**：字の幅で折り返しが変わりうる。手元の Chrome と日本語のフォントは3段目で決める
3. **ほかのブラウザと指の操作**：Safari（iOS）・Firefox・Android の Chrome、ピンチ・長押し・ダブルタップは試していない（kyopro-atlas の map.js の操作をそのまま写した）
4. **知識マップの全体（分野）の表示の読みやすさ**：本物の辺（分野をまたぐ前提と振り分け）で見直す。23 分野が線の塊になるなら、辺の細さの段や表示の既定を直す
5. **GitHub の Issue の開き方**：テンプレートがないときの `template=` の扱いと、欄への入り方は GitHub の上で試していない（いまは template を付けない形）
6. **読み上げ**（スクリーンリーダー）と印刷の見た目
7. **Zensical の新しい版**（0.1.0 は 2026-11-05 予告。B1 の §4 の9）での部品の一致
8. 使用量は数えていない。止められた操作はない
