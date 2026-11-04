# 工程6a B3：書き方の検査（textlint と prh）

- 版：2026-11-04
- 担当：B3（[README.md](README.md) の 6a 1段目）。共通の指示は [brief-build.md](brief-build.md)
- 書いたもの：`package.json`・`package-lock.json`・`.textlintrc.json`・`prh.yml`・`tools/textlint_targets.py`・`tests/tools/test_textlint_targets.py`・`tests/tools/test_textlint_rules.py`・この報告。`npm install` で `node_modules/` ができた（.gitignore にあり、追跡しない）。試しの文と一時の設定は scratchpad に置いた。docs/ と、ほかの担当のファイルは読んだだけ
- 手本：`../kyopro-atlas` の `package.json`・`.textlintrc.json`・`prh.yml`・`tools/textlint_targets.py`・`.github/workflows/check.yml`・`docs/guide/glossary.md`・`planning/style-guide.md`・`tools/gen_site.py`（読んだだけ。変えていない）
- 材料：design §3.3・§6.2・§7・§8.1〜§8.6・§10.1・§10.5、decisions 2026-11-04（工程5の回答）、research/27 §3.1・§3.4・§4 P11、research/20、brief-integrate.md の M1、catalog/start.yaml の glossary の項目、schema/site.yml
- git と gh は使っていない。Web は npm の登録簿（版の確かめ・取得）だけ。止められた操作はない

## 1. 作ったファイルと中身

| ファイル | 中身 |
| --- | --- |
| `package.json` | textlint と規則6つを版の固定で持つ（§2.1）。`engines.node` は `>=22`。スクリプトは `lint:text`（`uv run python tools/textlint_targets.py --run`）と `lint:text:fix`（同じく `-- --fix`） |
| `package-lock.json` | npm 11.19.1 で作った（lockfileVersion 3、388 個） |
| `.textlintrc.json` | 手本と同じ組（コメントで外す filter、prh、半角と全角の間の空白、コードの前後の空白、preset-ja-technical-writing を だ・である調 にして、誤検出の多いものを警告か無効に）。手本の `allows: ["典型90"]` は分野の語なので外した。prh を空白の規則より前に置く（§3.3） |
| `prh.yml` | 規則 54（§3.5）。区分は、割れている3語 5・公式の日本語版の多数派 37・製品とファイルの名前 2・ひらがなで書く語 10。正規表現の規則 36 にはすべて specs（計 95）。冒頭に、用語集から作る決まりと書き方・外し方、末尾に入れなかった語と理由 |
| `tools/textlint_targets.py` | 対象の一覧を出す。`--run` で textlint をかける（§3.2） |
| `tests/tools/test_textlint_targets.py` | 13件。一覧に入るもの・除くもの、site.yml から段と分野を読むこと、終了コード、`--run` の受け渡し（偽の textlint で）、本物のリポジトリ |
| `tests/tools/test_textlint_rules.py` | 18件。静的な試験 9（設定の決まり・版の固定と lock・prh.yml の形・正規表現のエスケープ）と、textlint を動かす試験 9（§2.2） |

試験の場所は `tests/tools/`（`uv run python -m unittest discover -s tests/tools` で一緒に流れる）。textlint を動かす試験は `node_modules/.bin/textlint` がないと飛ぶ。環境変数 `REQUIRE_TEXTLINT=1` のときは飛ばさずに失敗にする。

## 2. 確かめたこと

### 2.1 版（npm の登録簿、2026-11-04）

| パッケージ | 固定した版 | 登録簿の最新と公開日 |
| --- | --- | --- |
| textlint | 15.8.0 | 15.8.0（2026-08-01）。engines は node >=20.18.0 |
| textlint-rule-prh | 6.1.1 | 6.1.1（2026-10-16）。依存の prh ^6.1.0 |
| （prh。推移的） | 6.1.0 | 6.1.0（2026-08-29）。**engines は node >=22** |
| textlint-rule-preset-ja-technical-writing | 12.0.2 | 12.0.2（2025-01-02） |
| textlint-rule-ja-space-between-half-and-full-width | 3.0.4 | 3.0.4（2026-10-17） |
| textlint-rule-ja-space-around-code | 3.0.4 | 3.0.4（2026-10-17） |
| textlint-filter-rule-comments | 1.3.0 | 1.3.0（2026-01-03） |

- 手本の固定の版は、どれもいまの最新と同じだった。`engines.node` は prh の要件に合わせて `>=22` にした（手本は `>=20.18.0`）
- `npm install --ignore-scripts` で 388 個。install のスクリプトを持つ依存はない（lock の hasInstallScript が0）。lock の写しを scratchpad で `npm ci` して、同じ 388 個の名前と版の木になった
- `npm audit`：moderate が3件（textlint 15.8.0 の推移的な依存の glob と minimatch。GHSA-3g3m-2fjr-6pw4・GHSA-g3hv-75wg-m249）。直す案は textlint を 14.0.5 に下げる（大きい版の後退）しかないので、入れたままにした。道具にはファイルの名前を直接渡し、信用できない glob は渡さない
- 手元は Node 24.22.1・npm 11.19.1・uv 0.13.5。`uv run` は B1 の pyproject で Python 3.12.15・PyYAML 6.0.3

### 2.2 試験と、textlint の動き

- `uv run python -m unittest discover -s tests/tools`：199件 OK（受け持ちの31件と、check_catalog の168件）。`REQUIRE_TEXTLINT=1` でも OK。textlint の場所を消した形で、textlint を動かす2つの組が飛ぶこと、`REQUIRE_TEXTLINT=1` では失敗になることも確かめた
- `npm run lint:text`：いまの対象は B1 の `docs/index.md` だけで、0件で通る
- textlint を動かして確かめた動き（試験に入れた）
  - front matter（aliases に揺れた表記があっても）・`<!-- textlint-disable -->` で囲んだ別名の行・インラインコード・コードの塊・リンクの文字・`<!-- textlint-disable prh -->` の中は検査されない
  - 見出し・表のセル・太字・斜体（`checkEmphasis`）は prh が見る
  - `textlint --fix` を1回流すと、prh の置き換えの後に空白の規則が空白を足す（「のプランモードで」→「の plan mode で」）。設定の prh を後ろに回すと、1回では空白が直らないことを scratchpad で確かめた（並びが効く）
  - 本文の です・ます はエラー、半角と全角の間・コードの前後の空白の欠けはエラー、120字を超える文は警告で、警告だけなら終了コード 0
  - prh.yml の specs が外れると、textlint が読み込みで止まり 0 で終わらない
  - **いまの限界**：タブ（`=== "…"`）・囲み（`!!! …`）・折りたたみ（`??? …`）の中で、空行の後の字下げした段落は、Markdown の字下げのコードとして読まれ、検査されない（手本も同じ限界で、手引きに「自分で確かめる」と書いていた）。この形を試験 `test_known_gap_…` に残した（直したら落ちる）。直し方は §4 の P3
- textlint は引数がないと使い方を出して 0 で終わる。手本の `textlint $(python3 tools/textlint_targets.py)` は、一覧が空のときや一覧の道具が落ちたときに、黙って通る（§3.2）

### 2.3 prh の規則の当たり方（誤検出の見当）

- 目次の題名・要約・sign の 1629 の文に prh だけをかけた：指摘は7件で、すべて sign（読者の言葉）が英語の機能名を使ったもの（「作った skill が使われない」など）。M1 では sign は変えなくてよく、front matter は検査されないので、いまは問題にならない（生成物に写るときは §4 の P2）。題名と要約には指摘がなかった
- design.md・research/27・research/28 にかけた：指摘の多くは、設計書が英語の名前（hooks・sandbox・front matter など）で書いているための、M1 に沿った指摘だった。誤検出として、API の名前の「Skills API」、2語の「plugin marketplace」（別々に直すと和文の間に空白が残る）、2語目が大文字の英語の題名（「Permission Modes」）が見つかったので、規則を直して specs と試験に足した。英語の公式のページの題名（「Hooks reference」）は直してしまうので、prh.yml の冒頭に「リンクにするか日本語版の題名で書く」と書いた

## 3. 決めたこと（設計書に書いていない細部）

### 3.1 版と依存

- 版は `^` を付けずに固定し、lock と合うことを試験で確かめる。Node は textlint だけに使う（design §8.1）

### 3.2 対象の一覧（`tools/textlint_targets.py`）

- 対象は docs/ の手書きの Markdown のうち、骨格の段でないもの。骨格の段は site.yml の `stages` の最初（いまは stub）として読み、段の名前を直書きしない。分野の入口 `docs/<field>/index.md` の field は site.yml の `fields` から読む。`docs/lists/` は design §8.2 の置き場所として道具に持つ
- 公開から外した試作のページ（draft 以上）は対象に入れる（試作の終わりの条件が「試作のページで書き方の検査が0件」のため）。front matter が読めないページと stage のないページは、警告を出して対象に入れる（検査を広く取る。形の誤りは front matter の検査が見る）
- 手書きのページの中の生成部分（gen の目印の間）は、この道具では外さない（§4 の P2）
- `--run` で、Python が対象を決めてから textlint を呼ぶ。対象がなければ textlint を呼ばずに 0、textlint がなければ 2（「npm ci を流す」と出す）、ほかは textlint の終了コードを返す。`--` の後ろは textlint に渡す（`--fix` など）。npm のスクリプトはこれを `uv run` で呼ぶので、`lint:text` には uv と Node の両方が要る
- 読む部分（site.yml と front matter の stage）は小さく自前で持った。B2 の読む層とは並列で作ったため（§4 の P4）

### 3.3 textlint の設定

- 手本のまま引き継いだ（design §6.2 の だ・である調 と空白の決まりに合う）。外したのは分野の語の `allows` だけ
- 規則の並びは prh → 半角と全角の間 → コードの前後 → preset。並びは `--fix` の結果に効くので、試験で守る

### 3.4 prh の規則の作り方（用語集から作る決まりとの関係）

- 用語集のページ（start の glossary）を正とし、prh.yml は用語集の表から作る（design §6.2）。用語集の本文はまだないので、この版は design §6.2・research/27 §3.1 の表・M1・decisions 2026-11-04 から作った初めの版である。対応は、用語集の表の1行（正規形・本文で使ってよい別の書き方・直す表記）＝ prh の規則1つ（expected・patterns）。規則を足すときは表にも行を足す（手本と同じ決まり）。用語集を書くときに、この版の54の規則を表に写してから、表を正にする（§4 の P5）
- 規則の元
  - 割れている3語（5）：plan mode（plan モード・プランモードなどを直す）・effort（努力レベル）・allow ルール／ask ルール／deny ルール（許可ルール・確認ルール・拒否ルール）。effort レベルは公式の多数派の言い方なので直さない
  - 公式の日本語版の多数派（37）：research/27 §3.1 の表の英語の名前を、和文の中で使ったときに直す（subagent → サブエージェント、hooks → フック、sandbox → サンドボックスなど）。表の少数の表記（オートモード・編集を受け入れるモード・プロジェクト指示）も直す。表から組み立てたもの（hook event → フックイベント、plugin marketplace → プラグインマーケットプレイス、カタカナの揺れのコンテクスト・ウインドウ・メモリー・システムリマインダ・チームメート・コネクター）と、目次の題名から取ったもの（permission rules → 権限ルール）がある
  - 製品とファイルの名前（2）：Claude Code と CLAUDE.md の大文字と小文字（design §6.2 の「原文のまま」）
  - ひらがなで書く語（10）：手本の汎用の規則を写した（すべて・できる・または など）。planning/ の文書もこの書き方だった（数えた例：すべて 241・全て 11、できる 514・出来る 0）。claude-atlas の文書と目次の sign が「但し書き」を使うので、「但し」は「但し書き」を除いて直す。手本の「出来(る|ない|た|て|れば|ず)」は「出来なかった」を拾わないので「出来(る|な|た|て|れ|ず)」にした
- 英語の名前を和文の語に直す規則は、前後の形を1つにそろえた：識別子・パス・コマンド・URL の一部（前後が英数字・`_`・`-`・`.`・`/` など）と、かっこやかぎかっこにじかに接した英語（「サブエージェント（subagent）」のように初出に英語を添える書き方。research/27 §4 P11）は直さない。和文に挟まれた空白は一緒に取る（preset には全角どうしの間の空白を見る規則がないため、残すと拾えない）
- 固有の名前は個別に外した：Agent Skills（標準）・Skills API と memory tool と compaction と MCP connector（API の名前。M1 で英語のまま）・hooks module（Mods）・`claude plugin`（コマンド）・単数の大文字の Skill（道具の名前）・アプリの Auto（権限モード）・Claude Code の Projects
- 和文の語を英語に直す規則（plan mode など）は空白を足さない。空白は半角と全角の間の規則が指摘し、`--fix` で続けて直る（手本は一部の規則を2つに分けて空白を足していたが、前と後ろの両方に要るので4つに分かれ、表から機械的に作りにくい）
- 規則ごとに `prh:` の文（理由と用語集の節：split-terms・translation-policy・same-names-across-surfaces。どれも目次の glossary の sections にある anchor）を付け、指摘に添えて出す
- 入れなかったものは prh.yml の末尾に理由付きで置いた（compaction・memory・Projects・Research・connector・classifier・session などの英語、アプリの Auto、公式の資料に出てこない表記〔エフォート・計画モードなど〕、数えていない長音〔サーバー／サーバ など〕、「努力」単独、「Claudeの指示」）

### 3.5 試験の決まり

- 正規表現の規則には specs を付ける（試験で確かめる）。prh は `u` の旗を付けるので、`\#` `\:` `\@` のような不要なエスケープは読み込みで落ちる。これを Node なしの試験で先に見る
- 同じ pattern を2つの規則に置かない（試験で確かめる）

## 4. 提案（ほかの担当のファイル・設計書）

- **P1（B1・CI。`.github/workflows/ci.yml`）**：いまの `tools` の job は Node を入れずに tests/tools を流すので、textlint を動かす試験9件が飛ぶ。`actions/setup-node`（Node 24、npm のキャッシュ）と `npm ci` を `uv sync --locked` の後に足し、試験の手順に `REQUIRE_TEXTLINT: "1"` を付け、書き方の検査の手順 `npm run lint:text` を足す（design §8.6 の「書き方：毎回」）。`lint:text` は `uv run` を呼ぶので、uv のある同じ job に置く。2段目の `tools/check_all.py` からは `tools/textlint_targets.py --run` を呼ぶ
- **P2（2段目の作る層）**：手書きのページの生成部分（`<!-- gen:begin … -->`〜`<!-- gen:end … -->`）と別名の行は、作る層が `<!-- textlint-disable -->`〜`<!-- textlint-enable -->` で囲む（手本の gen_site.py と同じ）。目次の題名・別名・sign（英語の機能名を含む。§2.3 の7件）と、出典の英語の題名を写すため。段落の中の数値の目印（fact）は、作る層が書く文を空白の決まりに合わせる
- **P3（2段目。textlint の手元の plugin）**：§2.2 の限界は、Markdown を読む前に、タブ・囲み・折りたたみの印の行の頭（`=== `・`!!! `・`??? ` の4字）を同じ長さの `-   `（箇条書きの印と空白3つ）に置き換えると直る。中身が箇条書きの続きとして読まれ、検査される。字数を変えないので、行と列と `--fix` の位置は元のファイルのまま。scratchpad で、置き換えた文を標準入力で流して、タブ・入れ子の囲み・折りたたみの中の揺れが、元のファイルの行と列で指摘されることを確かめた。`???+`（5字）は別の扱いが要る。plugin の置き場所（例：`tools/textlint/` か `file:` の依存）と `.textlintrc.json` の plugins はメインが割り当てる。手元のパスを textlint が読めるかは、resolver のソースを読んだだけで、動かしていない
- **P4（B2・読む層）**：`tools/textlint_targets.py` の site.yml と front matter の読み方は小さく自前で持った。`tools/lib/` ができたら、読む層のページのモデル（stage）と語彙に置き換える。生成物のパスの一覧（`docs/lists/`・`docs/<field>/index.md`）は作る層の設定に1か所で持ち、この道具と B4 の H2（生成物の deny）がそこを読むようにすると、二か所に持たずに済む
- **P5（メイン・用語集と目次）**：用語集のページに、手本の canonical-forms のような「正規形・本文で使ってよい別の書き方・直す表記」の表と、表記の規則（ひらがなで書く語と「但し書き」の例外、英語を添えるときのかっこの書き方）を置く。目次の glossary の sections に、この表の節がない（いまは translation-policy・own-terms・split-terms・same-names-across-surfaces・definitions）ので、節を足すか translation-policy に入れるかを決める。表は `<!-- textlint-disable prh -->` で囲む。後で検査の層に「用語集の表と prh.yml が対応しているか」の検査を作ると、「prh は用語集から作る」が機械で確かめられる
- **P6（B5・手引き）**：共通の手引きに、textlint の流し方（`npx textlint docs/<field>/<id>.md`、または `npm run lint:text`）、エラーは0・警告は誤検出なら残してよい、`--fix` の使い方、別名の行の外し方、英語のページの題名はリンクにする・原文の引用は `>` にする、P3 が入るまではタブ・囲み・折りたたみの中の空行の後の段落は自分で確かめる、を書く。prh.yml と用語集の変更は報告に「提案」として書く
- **P7（設計書）**：§8.1 の「Node.js は textlint だけに使う」に、要る版（Node 22 以上。prh 6.1.0 の要件）を足す。§8.6 の「書き方」の行の方法に `npm run lint:text`（`tools/textlint_targets.py --run`）を書く

## 5. 確かめていないこと

- 本物のページでの誤検出の割合（ページがまだない）。見当は planning/ の文と目次の文だけで付けた
- research/27 で数えた29ページの外の、公式の日本語版の表記。表から組み立てた規則（フックイベント・プラグインマーケットプレイス・カタカナの揺れ）と、目次の題名から取った規則（権限ルール）は、公式の文書で数えていない
- 用語集の節の anchor（`prh:` の文が指す split-terms など）が、用語集を書いた後もこの名前のままか
- P3 の plugin を textlint が手元のパスから読めるか。`???+` の扱い
- CI での textlint（いまの CI は流していない）。Node 22 での動き（Node 24.22.1 だけで試した）。Windows と macOS
- 作る層の目印（gen・fact・link）と textlint の関わり（作る層がまだない）
- `npm audit` の3件が、この使い方で実際に効くか（勧告の題名を読んだだけ）

## 6. 使用量の目安

- 道具の呼び出し：約80回（Bash が大半、Read・Write・Edit）
- Web：npm の登録簿の照会が約10回、`npm install` 1回、scratchpad での `npm ci` 2回
