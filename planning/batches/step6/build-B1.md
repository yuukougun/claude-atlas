# 工程6a 1段目 B1（サイトと CI）の報告

- 担当：B1（2026-11-04）
- 指示：[brief-build.md](brief-build.md) の §4 の B1、[README.md](README.md) の表の B1 の行
- 終わりの条件：`uv run mkdocs build --strict` が通る → **通った**（終了コード 0、WARNING・ERROR は0件）

## 1. 作ったファイルと中身の要約

| ファイル | 中身 |
| --- | --- |
| `.python-version` | `3.12` |
| `pyproject.toml` | 依存：mkdocs==1.6.1・mkdocs-material==9.8.0・pymdown-extensions==12.3・pyyaml>=6.0.2・jsonschema>=4.23。`requires-python = "==3.12.*"`。Zensical は `[dependency-groups] zensical = ["zensical==0.0.74"]`（既定の `uv sync` では入らない）。`[tool.uv] package = false` |
| `uv.lock` | `uv lock` で作った（40 パッケージ。zensical の組を含む） |
| `mkdocs.yml` | `INHERIT: nav.yml`、site_url `https://yuukougun.github.io/claude-atlas/`、repo_url、フッターの文（`copyright`）、theme（material・ja・`font: false`・custom_dir overrides・機能の一覧・ライトとダーク）、プラグインは search だけ（kyopro-atlas の日本語の separator の設定 C）、markdown 拡張（kyopro-atlas の組から arithmatex と snippets を外したもの）、validation を warn（`--strict` で失敗）、extra_javascript に `assets/js/mermaid-local.js` |
| `nav.yml` | 仮の手書き（`nav: [index.md]`）。2段目から gen_site.py が生成し、未公開のページを `exclude_docs` に書く前提の注釈 |
| `docs/index.md` | 見出しと2文（「Claude 全般を使いこなすための、辞書として引く日本語の教材。いまは土台を作っている段階で、ページはまだない。」） |
| `overrides/main.html` | 冒頭：announce の帯に「この辞典は Anthropic の公式の教材ではない。」。content のブロックに、2段目が足す所の印（バッジ・帯・期限切れ／前提・次に読む・関連・段階と更新日・誤りの報告） |
| `overrides/partials/source.html` | Material 9.8.0 の同じ部品の写しから `data-md-component="source"` だけを外したもの（テーマが GitHub の API を読まないように） |
| `overrides/assets/js/mermaid-local.js` | Mermaid の写しを、図を描くときに初めて読む小さな JS（下の §3 の2） |
| `overrides/assets/vendor/mermaid-11.17.2/` | `mermaid.min.js`（約 3.6MB）と `LICENSE`（MIT）。npm の tarball から手を加えずに写した |
| `overrides/assets/vendor/SOURCES.txt` | 写しの出所・sha512（レジストリの integrity）・sha256・版の系列を選んだ理由 |
| `.github/workflows/ci.yml` | push・pull request・手動で動く。job は `site`（`uv sync --locked` → `uv run mkdocs build --strict`、main のときだけ upload-pages-artifact）・`tools`（tests/ の tools・site・hooks〔python3 と uv run の両方〕・guides の試験と check_catalog.py）・`deploy`（`needs: [site, tools]`、main のときだけ、configure-pages → deploy-pages、`github-pages` の environment、`concurrency: pages` で取り消さない） |
| `.github/workflows/zensical.yml` | push（docs・overrides・設定・lock・このファイルが変わったとき）と手動。`uv sync --locked --group zensical` → `uv run --group zensical zensical build --strict` を `continue-on-error`、失敗は `::warning` に出す |
| `.github/workflows/links.yml` | 週1回（月曜 3:37 JST）と手動。lychee-action v2.9.0（lychee v0.24.2）で docs/**/*.md・data/**/*.yml・README.md を確かめる。atcoder.jp・codeforces.com（サブドメインと大文字を含む）とサイト自身を除く。`--verbose` で転送を出す。0件でも失敗にしない |
| `README.md` | 1行の説明と「この辞典は Anthropic の公式の教材ではない。」、サイトの URL、状態、リポジトリの中身の表、手元でサイトを見るコマンド、フックと権限の設定は [.claude/README.md](../../../.claude/README.md) へのリンク、ライセンス（© 2026 yuukougun・CC BY 4.0・MIT・同梱の Mermaid） |
| `LICENSE` | MIT（Copyright (c) 2026 yuukougun。kyopro-atlas と同じ本文） |
| `LICENSE-docs` | CC BY 4.0 の告知。kyopro-atlas の形にそろえ、対象（docs/ の本文と図）と対象でないもの（コードと雛形・そのほかのファイルは MIT、同梱の Mermaid、他者のもの）、表示の仕方、CC のリンク、英語の要約 |
| `tests/site/test_site_config.py` | 試験 27 件（設定・上書き・写し・版の固定・ワークフロー・ビルドしたサイトが外の資源を読まないこと） |
| `tests/site/test_site_browser.py` | 試験 2 件。環境変数 `CA_CHROME` に Chrome の実行ファイルを指定したときだけ動く（ないときは飛ぶ）。§2.4 のブラウザでの確かめを再現する |

試験の場所は `tests/site/`（`uv run python -m unittest discover -s tests/site`）にした。

## 2. 確かめたこと

### 2.1 版（2026-11-04、公式の配布元）

| もの | 確かめた所 | 結果 |
| --- | --- | --- |
| mkdocs-material | PyPI の JSON | 最新 9.8.0（2026-10-24）、Python 3.11 以上、依存に `mkdocs<2,>=1.6` |
| mkdocs | PyPI | 安定版の最新は 1.6.1。2.0 は dev1〜dev6 だけ |
| pymdown-extensions | PyPI | 最新 12.3（2026-10-14） |
| zensical | PyPI | 最新 0.0.74（2026-10-30）。依存の zensical-ui は 0.0.41 に固定されている |
| pyyaml・jsonschema | PyPI | 6.0.3・4.26.0（lock の版） |
| mermaid | npm のレジストリ | latest は 12.3.0。Material 9.8.0 が読む 11 系の最新は 11.17.2（2026-08-25）。tarball の sha512 がレジストリの integrity と一致 |
| actions/checkout・configure-pages・upload-pages-artifact・deploy-pages | GitHub の releases とタグ | v7（=v7.0.1）・v6（=v6.0.0）・v5（=v5.0.0）・v5（=v5.0.1）。`actions/` は大きい版のタグで書いた |
| astral-sh/setup-uv | GitHub の releases とタグ | v10.3.3（2026-10-28）＝ `68559e99cc807c1eb7e9238fd43a15bba460eec2`。大きい版のタグ（v10）がないので SHA で固定 |
| lycheeverse/lychee-action | GitHub のタグと action.yml | v2.9.0 ＝ `e7477775783ea5526144ba13e8db5eec57747ce8`、既定の lychee は v0.24.2。lychee 0.24.0 の release の本文に「Show redirects & remaps」、0.23 に「転送の詳細は verbose のときだけ」 |

### 2.2 ビルド（手元、Python 3.12.15・uv 0.13.5）

- `uv lock --check` が通り、CI と同じ手順（`uv sync --locked` → `uv run mkdocs build --strict`、試験の tests/tools 199 件・tests/site 29 件〔Chrome の2件と zensical の1件は飛ぶ〕・tests/hooks 47 件〔python3 3.10.12 と uv run の両方〕・tests/guides 14 件、check_catalog.py のエラー0・警告3、`uv sync --locked --group zensical` → `uv run --group zensical zensical build --strict`）がすべて通った（件数は報告を書いた時点。ほかの担当の試験は書きかけのことがある）
- Zensical 0.0.74 の `--strict` も「No issues found」。冒頭の帯・フッター・source の上書き・mermaid-local.js が Zensical の出力にも入る
- Material 9.8.0 はビルドのたびに保守の終わり（2027-05-05）の知らせを出すが、`--strict` を止めない。CI では `NO_MKDOCS_2_WARNING=1` で消した
- 幅 390px のライトとダークのスクリーンショットで、冒頭の帯・ヘッダー・フッターが収まることを見た（字の形は §5 の6）

### 2.3 INHERIT と exclude_docs（作業用の写しのサイトで。リポジトリには残していない）

nav.yml に `nav` と `exclude_docs`（`/a/stub.md` など）を書き、mkdocs.yml から INHERIT で読んだ。

| 場合 | MkDocs 1.6.1 | Zensical 0.0.74 |
| --- | --- | --- |
| nav.yml の exclude_docs | **効く**。stub のページは作られず、検索の索引にも入らない。`mkdocs serve` でも 404 | **効く**（INHERIT も nav も読む）。stub は作られない |
| 公開のページから外したページへの手書きのリンク | INFO だけで `--strict` を通り、HTML には `../stub/` のリンクが残る（公開で 404。R4-1 と同じ） | `--strict` で止まる（「page does not exist」） |
| 外したページを nav にも載せる | INFO だけで通り、ナビゲーションに 404 のリンクが残る | 未確認 |
| mkdocs.yml にも exclude_docs を書く | nav.yml の値を丸ごと上書きする（合わさらない）。外れなかったページが nav にないので omitted_files の警告で `--strict` が止まる | 未確認 |
| stub を docs/ の外に置く（設計 §8.1 の比べる案） | 手書きのリンクが「not found」の WARNING になり、`--strict` で止まる | `--strict` で止まる |
| INHERIT を重ねた別の設定（`INHERIT: mkdocs.yml` と `exclude_docs: ""`） | stub も含めて作れる（nav にないので `--strict` なしで使う） | 未確認 |

### 2.4 外から読まない（design §8.5）

- Material 9.8.0 と Zensical 0.0.74 の bundle を読んだ：Mermaid は `typeof mermaid=="undefined"` のときだけ unpkg.com（Material は mermaid@11、Zensical は mermaid@12）から読み、そのあとは `mermaid.initialize` を1回と `mermaid.render` だけを呼ぶ。ヘッダーのリポジトリのリンクに `data-md-component="source"` があると、`api.github.com` へ星・フォークの数と最新の版を問い合わせる。ResizeObserver の polyfill は ResizeObserver がないブラウザでだけ unpkg.com から読む（いまの主なブラウザにはある）
- 手元の Chrome for Testing 146（`~/.cache/puppeteer` の chrome-headless-shell）で、127.0.0.1 のほかの名前を引けなくして開き、NetLog の URL を見た（外へは実際には出ない）：

| 開いたもの | 外への問い合わせ | Mermaid の写し | 図 |
| --- | --- | --- | --- |
| 図のないページ → instant navigation で図のページ → もう一つの図のページ（MkDocs の出力） | 0 件 | 図のページで初めて読んだ | 2 ページとも描かれた |
| 同じ（Zensical の出力） | 0 件 | 同じ | 同じ |
| 図のページを直接 | 0 件 | 読んだ | 描かれた |
| 図のないトップだけ | 0 件 | 読まない | — |
| 対照：mermaid-local.js を外した版 | `https://unpkg.com/mermaid@11/dist/mermaid.min.js` | — | 描かれない |
| 対照：source の上書きを外した版 | `api.github.com/repos/yuukougun/claude-atlas` と `/releases/latest` | — | — |

- この確かめを `tests/site/test_site_browser.py` に残した（`CA_CHROME=<chrome-headless-shell のパス> uv run python -m unittest discover -s tests/site` で 2 件とも通った）
- ビルドしたサイトの HTML（script・資源の link・img など）と CSS に外の URL がないことは、`test_site_config.py` が毎回確かめる

### 2.5 そのほか

- README.md と docs/index.md に B3 の textlint（`.textlintrc.json` と prh.yml）を当てて、指摘0件（はじめは hooks・permissions の語と「が」の重なりで4件出たので、「フックと権限の設定（`hooks` と `permissions`）」に直した）。B3 のファイルは変えていない
- links.yml の除外の正規表現を Python で当てて、atcoder.jp・img.atcoder.jp・大文字の AtCoder.jp・m1.codeforces.com を除き、notatcoder.jp・code.claude.com を除かないことを見た（試験にも入れた）

## 3. 決めたこと（設計書に書いていない細部）

1. **冒頭の文は Material の announce の帯に置いた**。全ページの一番上に出て、ページ上部（2段目のバッジ・帯）と場所を取り合わない。閉じるボタン（announce.dismiss）は付けない。トップのページの本文には繰り返さなかった
2. **Mermaid は「代わり」を置いて写しを遅れて読む**：図は目次で約14ページだけなので、写し（約 3.6MB、gzip で約 1MB）を全ページで読むのをやめた。図のあるページで、ページを開いたときと instant navigation で移ったときの両方で働くことを §2.4 で確かめた。テーマが initialize と render のほかを呼ぶようになると図は描かれない（外へは読まない）ので、テーマの bundle の呼び出しを試験で見張る（版を上げたときに気づく）
3. **Mermaid の版は 11.17.2**：Material 9.8.0 が読む系列（@11）に合わせた。Zensical 0.0.74 は @12 を読むが、試験ビルドでも 11 の写しで図が描けた
4. **GitHub の API を読まないようにした**：design §8.5 が名指しするのはフォントと Mermaid だが、同じ趣旨（読者のブラウザから外へ問い合わせない）なので、ヘッダーのリポジトリのリンクから問い合わせの印だけを外した。星の数などは出なくなる
5. **Zensical は uv の dependency-groups で固定**：上の依存と同じ uv.lock で解くので、試験ビルドの pymdown-extensions などが本番のビルドと同じ版になる（kyopro-atlas の `uvx` の形では別の版になりうる）。上げるときは `uv lock --upgrade-package zensical`
6. **`requires-python = "==3.12.*"`**：設計の「3.12 で固定」に合わせ、lock も 3.12 だけで解く
7. **デプロイを ci.yml の中に置いた**：`needs: [site, tools]` で「必須の検査の後」を表せるため（kyopro-atlas は検査とデプロイが別のワークフローで、デプロイが検査を待たなかった）。configure-pages は公開の job に置いたので、Pages の設定がなくても「サイトのビルド」の結果は分かる
8. **CI の必須の検査に、いまある試験（tests/ の tools・site・hooks・guides）と目次の検査を入れた**：設計 §8.8 の「必須の検査」（§8.6 の毎回の検査）のうち、いま動くもの。hooks の試験は、試験のファイルの「動かし方」のとおり python3 と uv run の両方で流す。目次の検査は骨格（6c）の後に外す（ci.yml の注釈に書いた）
9. **第三者の action は SHA で固定**（setup-uv・lychee-action）、`actions/` は大きい版のタグ。checkout は `persist-credentials: false`
10. **外部リンクの対象に data/**/*.yml を足した**：出典の URL の転送と切れを点検で見るため（design §6.8・§9.4 の6）。まだないファイルで落ちないよう `--skip-missing`、入力の前に `--`
11. **フッターの CC BY 4.0 と MIT を、GitHub の LICENSE-docs と LICENSE へのリンクにした**。文は決定のまま。Material の「Made with Material for MkDocs」はテーマの既定のまま残した（消すなら `extra.generator: false`）
12. **markdown 拡張**：kyopro-atlas の組から arithmatex（KaTeX を入れない）と snippets（取り込みの記法を使わない。design §6.9）を外した。betterem は入れない。`content.tabs.link` を足した（面のタブを一緒に切り替える）
13. **トップの文**：説明1文と状態1文だけ。三つの入口・症状辞典と台帳への道（design §7）は、ページができてから足す
14. **LICENSE-docs**：kyopro-atlas の形（決定「kyopro-atlas と同じ形」）で、雛形は MIT（決定の「コード・雛形・そのほかのファイル」）、同梱の Mermaid はそれぞれのライセンス、と書いた

## 4. 提案

**メインへ（設定。担当の範囲の外）**

1. **GitHub Pages の公開元を「GitHub Actions」にする**（必須。しないと ci.yml の `deploy` の configure-pages が止まる）。Settings → Pages → Build and deployment → Source を「GitHub Actions」。コマンドなら `gh api -X POST repos/yuukougun/claude-atlas/pages -f build_type=workflow`（すでに Pages があるときは `-X PUT repos/yuukougun/claude-atlas/pages -f build_type=workflow`）。公開元を Actions にすると作られる `github-pages` の environment（main からの公開を許す既定）をそのまま使う。ほかのリポジトリの設定（Actions の権限など）は既定のままでよい（ワークフローが permissions を書いている）
2. CI について（3段目のつなぎ）：tests/hooks と tests/guides は、報告を書いた時点のファイルの「動かし方」のとおりに ci.yml の `tools` の job に入れた。B4・B5 が試験の置き場所や流し方を変えたら、この手順も直す（試験のないフォルダを `unittest discover` で流すと終了コード 5 で止まる）。B3 の textlint の job（Node・`npm ci`・`npm run lint:text`）はまだ入れていない。のちに `tools/check_all.py` にまとめる

**2段目の作る層・検査の層の担当へ**

3. gen_site.py は、外したページを nav に**載せない**（MkDocs は INFO だけで通し、ナビゲーションに 404 のリンクが残る。§2.3）。`gen_site.py --check` か check_pages.py で「nav と exclude_docs が重ならない」を確かめるとよい。`exclude_docs` は nav.yml だけに書く（mkdocs.yml に書くと丸ごと上書きになる。tests/site がこれを止める）
4. 描画の検査（render_pages.py）に、`test_site_browser.py` の方式（`--host-resolver-rules` で外の名前を引けなくし、NetLog に外の URL がないことを見る）を入れると、全ページで「外から読まない」を確かめられる。Mermaid の図のページを足したら、図が描かれること（`div.mermaid` があり `pre.mermaid` が残らない）も見る
5. 工程7の「stub を含めた試しのビルド（公開しない）」には、`INHERIT: mkdocs.yml` と `exclude_docs: ""` の別の設定で作る形が使える（§2.3。nav.yml を変えずに済む）

**設計書へ（メインが判断）**

6. §8.5 の「INHERIT で exclude_docs が効くかは土台作りで確かめる」を、確かめた結果（MkDocs 1.6.1 と Zensical 0.0.74 の両方で効く。mkdocs.yml に同じキーを書かない。外したページを nav に載せない）に書き換える
7. §8.1 の「stub を docs/ の外に置く形と比べる」の材料：exclude_docs の形では、手書きのリンクで stub を指すと MkDocs は止めず Zensical だけが止める。docs/ の外に置く形なら、MkDocs の `--strict` も止める（check_pages.py の役の一部を MkDocs が受け持つ）が、draft にするときにファイルを移す手間と、`mkdocs serve` で stub を見られないことは同じ。どちらでも Zensical の `--strict` は止めるので、Zensical の試験ビルドが未公開のページへの手書きのリンクの見張りを兼ねる
8. §8.5 の「外から読まない」に、ヘッダーのリポジトリのリンク（GitHub の API）を足す（§3 の4）
9. Zensical 0.1.0 は 2026-11-05 に出る予告（research/28 #50）。土台作りの終わりの評価で、版を上げて（`uv lock --upgrade-package zensical`）tests/site と試験ビルドを流す。tests/site は Zensical の bundle の Mermaid の呼び出しも見張る

**B2 へ（依存）**

10. pyproject の依存に PyYAML と jsonschema を入れた。ほかに要る依存があれば提案してほしい（pyproject.toml と uv.lock は B1 の受け持ち）

## 5. 確かめていないこと

1. **GitHub の上での動き**：ワークフローは手元で同じコマンドを流し、YAML の形と action の版を確かめただけで、GitHub Actions では動かしていない（デプロイ・configure-pages・upload-pages-artifact v5・Pages の公開・concurrency の式）。actionlint もかけていない
2. **lychee を手元で動かしていない**：lychee v0.24.2 の実行ファイルを公式の releases から取って `--dump` で引数を確かめようとしたが、自動モードの判定で止められた（外から取った実行ファイルを動かす操作）。回り込まず、固定した版の README（引数の一覧）と lychee-action の action.yml・entrypoint.sh を読んで書いた。`--skip-missing` と glob が何にも当たらないときの動き、`--verbose` での転送の出方、YAML から URL を拾う働きは未確認
3. **Zensical の日本語の検索**：Zensical は search の lang と pipeline を無視する（research/28 #57）。評価の基準の「日本語の検索で決めた語が引ける」は、ページができてから
4. Zensical で、外したページを nav に載せた場合・mkdocs.yml にも exclude_docs を書いた場合・INHERIT を重ねた設定（§2.3 の表の未確認の欄）
5. ダークモードでの Mermaid の図の色、印刷、Material の検索の日本語の質（どれも図とページができてから。描画の検査の担当）
6. **日本語のフォント**：この WSL には日本語のフォントがなく（`fc-list :lang=ja` が空）、スクリーンショットの字は豆腐になった。レイアウトだけを見た。手元の Chrome と日本語のフォントは3段目で決める
7. Chrome の新しい headless（`google-chrome --headless`）で `test_site_browser.py` が動くか。試したのは chrome-headless-shell 146 だけ。CI では `CA_CHROME` がないので飛ぶ
8. README のリポジトリの中身の表の `data/`・`schema/` の説明は設計 §8.2 のとおりに書いた。B2 の実際のファイルとは照らしていない。README から指す `.claude/README.md` は B4 が書くもので、この報告の時点ではまだない（`.claude/settings.json` はある）
9. CI の tests/hooks の試験は、GitHub の runner の python3（ubuntu-latest の 3.12）で流れる。手元で流したのは WSL の python3 3.10.12 と uv の 3.12
