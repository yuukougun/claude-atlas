# 工程6（土台作り）のバッチ

設計書（[../../design.md](../../design.md)）の §8〜§10 に従って、サイト・道具・縛りの土台を作る。工程は 6a（土台）→ 6b（data の初版）→ 6c（骨格）。終わりの条件は design §10.1 の表にある。

- 始めの作業（2026-11-04 済み）：planning/ の実名の検索（N1。[names-N1.md](names-N1.md)）、GitHub の公開のリポジトリ yuukougun/claude-atlas の作成と push
- 担当は報告をファイルに書いてから終える。止まったときは、報告のない担当だけを同じ割り当てで流し直す（その担当が書いたファイルだけを最後の commit に戻してから）
- 担当は git の操作をしない。commit と push はメインが行う。担当が書くのは、割り当てたファイルと自分の報告だけ
- 共通の指示は [brief-build.md](brief-build.md)

## 6a 1段目（並列。書くファイルが重ならないように分けた）

| 担当 | 書くもの | 報告 | 状態 |
| --- | --- | --- | --- |
| B1 | サイトと CI：`pyproject.toml`・`uv.lock`・`.python-version`・`mkdocs.yml`・`nav.yml`（仮）・`docs/index.md`・`overrides/`（テンプレートの骨組みと、冒頭とフッターの文）・`.github/workflows/`・`README.md`・`LICENSE`・`LICENSE-docs` | `build-B1.md` | 完了（ビルド・試験29件。Pages を有効にし、空のサイトを公開した） |
| B2 | 読む層と data：`tools/lib/`・`schema/page.schema.json` を作る道具・`schema/` の data の schema・`data/` の空の雛形・`tests/tools/` の読む層の試験 | `build-B2.md` | 完了（読む層・make_schema・data の雛形。試験は全体285件） |
| B3 | 書き方の検査：`package.json`・`package-lock.json`・`.textlintrc.json`・`prh.yml`・`tools/textlint_targets.py` と試験 | `build-B3.md` | 完了（prh 54規則・試験31件） |
| B4 | 縛り：`CLAUDE.md`・`.claude/settings.json`・`.claude/hooks/`・`.claude/README.md`・hooks の試験 | `build-B4.md` | 完了（H1〜H4・試験47件。H2 がこのセッションに効くことを確かめた） |
| B5 | 手引きとチェックリスト：`planning/guides/`（共通の手引きと型ごとの手引きの第1版）・`planning/checklists/`（検証の4つの観点） | `build-B5.md` | 完了（手引き11・チェックリスト5・試験14件） |

### 1段目の報告への判断（2026-11-04 メイン）

| 点 | 判断 |
| --- | --- |
| stub の置き場所（B1 の提案7） | docs/ の外の `stubs/<field>/<id>.md` に置き、draft にするときに docs/ へ移す（design §8.5）。試作のページは exclude_docs で外し、nav にも載せない（B1 の提案3） |
| outdated_advice を執筆者が書くか（B5 の1） | 書かない。目次が書き、執筆者は提案する（design §3.3 を §10.2・§12 に合わせた） |
| まだ形のない目印（B5 の2） | 2段目の作る層とともに決める（症状の振り分けの表・比較表・機能の属性・雛形の折りたたみ） |
| 安全とデータの雛形の扱い（B5 の3） | 執筆者は本文に雛形の目印を置く。道具は、動作確認を通った雛形だけを目印の間に写し、通っていないものは「動作確認の後に載せる」と書く。骨格の後の safety の印は `snippets/<id>/<名前>.expect.yaml` に持つ |
| 台帳の行を指す形（B5 の4） | 台帳のページは行ごとに anchor（台帳の id）を持ち、ほかのページは `outdated-advice-ledger#<台帳の id>` で指す |
| 検証ノートの試し方（B5 の5） | 試作の始めに作る見せ方の一覧（planning/shows.md）と工程7の指示で決める |
| H3 で許す git（B4） | 読むだけのサブコマンドを広く許す形（B4 の一覧）でよい。DR-08 の「status・diff・log・show」は例 |
| lychee を手元で動かすこと（B1） | 取得が自動モードで止められたので、回り込まない。外部リンクの検査は CI（週1回）で動かして確かめる |

## 6a 2段目（1段目の後、並列）

共通の指示は [brief-build2.md](brief-build2.md)（1段目の指示との差分と、担当どうしの受け渡しの形）。

| 担当 | 書くもの | 報告 | 状態 |
| --- | --- | --- | --- |
| G | 作る層：`tools/gen/`・`gen_site.py`・生成物（nav.yml・分野の入口・一覧・llms.txt・サイト用のデータ・目印の中身）と試験 | `build-G.md` | 完了（gen_site.py と生成物、目印の中身。試験71件） |
| C | 検査の層：`tools/checks/`・`check_pages.py`・`check_templates.py`・`check_all.py`・`render_pages.py`・`check_svg.py`・CI の check.yml・deny の追加と試験 | `build-C.md` | 完了（check_pages.py 55種ほか、check_all.py 13段。試験は tools 454・site 66・hooks 52件） |
| V | 見た目：`overrides/` の部品・CSS・JS（バッジ・下書きの帯・期限切れの表示・前提と次に読む・知識マップ・絞り込み）と試験 | `build-V.md` | 完了（帯・注意書き・バッジ・CSS と JS・地図の写し。試験66件） |

### 2段目の報告への判断（2026-11-04 メイン）

| 点 | 判断 |
| --- | --- |
| 注意書きと誤りの報告のリンクの文（V） | 工程7の終わりの、作者への頼み（方針の文の承認）に入れる。ページを公開するのは第一波（8a）からなので、承認はその前に済む |
| 大会の規則の表の形（G） | data の初版（6b）で、大会の規則の数値の形とともに決める |
| 波から公開を外す一覧（G） | いまは手で書く。第一波（8a）の前に、wave と routes から道具が出す形にする |
| 手引きの「作る予定」の印（C の提案1） | 道具ができた21種46か所を「検査」に書き換えた（メイン）。残り11か所は、道具ができたときに書き換える |
| 担当の逸脱（C） | 読むだけの git status を1回、uv sync で外れた Zensical を戻した（メインが Zensical 0.0.74 で動くことを確かめた） |

## 6a 3段目：つなぐ（2026-11-04）

| 確かめること | 結果 |
| --- | --- |
| 空のサイトのビルドとデプロイ | 済み。GitHub Pages（公開元は GitHub Actions）で https://yuukougun.github.io/claude-atlas/ に出た。冒頭とフッターの文を確かめた |
| CI の検査 | 済み。GitHub 上で ci（試験と目次の検査・サイトのビルド・公開）が通る。手元の check_all.py は13段が通る |
| hooks が担当にも効くか | サブエージェント（Agent の道具）で済み。制作の印 state/production を置き、担当の読むだけの git は通り、書き込みの git は理由の文つきで止められ、state/blocks.log に担当の id つきで残った。メインの git は止められない。ワークフローの担当は、試作（工程7）で最初にワークフローを使うときに確かめる（効かなければ、バッチの始めと終わりの HEAD を比べる） |
| 制作の権限モード | auto モード（このセッションの今のモード）。ワークフローのスクリプトの置き場所は、試作で最初に使うときに、.claude/ への書き込みで確認が出るかを見て決める |
| 手元の Chrome と日本語のフォント | Chrome は puppeteer の chrome-headless-shell 146（render_pages.py が自分で見つける）。日本語のフォントは、Windows の Noto Sans JP・Noto Serif JP を ~/.local/share/fonts にリンクした（sudo も取得もしない。消せば戻る）。CI の描画の検査には、試作で fonts-noto-cjk を入れる |
| 描画の検査 | 手元で空のサイトに流し、エラー0件・警告0件 |

## 6b data の初版（並列）

共通の指示は [brief-data.md](brief-data.md)。担当は data/ を直接書かず、`data/<担当>.yml` の下書きに書く。メインがまとめ、別の担当が出典と照らす。

| 担当 | 受け持ち | 報告 | 状態 |
| --- | --- | --- | --- |
| D1 | features（Claude Code の機能） | `data-D1.md` | 完了（Claude Code の機能65件、すべて確認済み。読み込みの時期とコンテキストのコストの語彙を提案） |
| D2 | features（アプリ・API・プランと上限・組織） | `data-D2.md` | 完了（下書きと報告はそろっている。終わりの返答の前に、使用量のためにメインが止めた） |
| D3 | 古くなった助言の台帳（37行）と、名称と旧名 | `data-D3.md` | 完了（流し直した。台帳37行すべて確認済み・names 19・sources 62） |
| D4 | 第一波のページの一次資料の sources と domains、ページごとの sources の一覧 | `data-D4.md` | 完了（流し直した。sources 368・domains 143。出典の一覧ができた第一波のページ134／136） |

### data のまとめ（2026-11-04 メイン）

- 4人の下書きを data/ にまとめた：機能117・名称19・出典534（URL で重なりを除き、5つの id を寄せた）・ドメイン151・台帳37行
- robots.txt で Anthropic のクローラにサイト全体を禁じる10ドメインを、AI の利用を断るドメインと同じに扱った（decisions 2026-11-04「工程6b」）。出典19件を外し、H1 の deny・check_noai.py・外部リンクの検査の除外に入れた
- 出典と照らす担当：E1（機能の属性。23件）・E2（台帳・名称・出典。16件）。直しは DF（Sonnet 5.5・max effort。`fix-DF.md`）、直しの確かめは E3（Opus。11件、直す0。`verify-E3.md`）。台帳の状態を見直す6行の案（fix-DF.md §5.1）は作者の承認に回した
- robots.txt の扱い：Anthropic のクローラを名前で禁じるドメインだけを外す（decisions 2026-11-04「robots.txt の * の組」）。外したのは11ドメイン（media.defcon.org を足した）

工程6は 2026-11-04 に完了した（check_all.py の13段が通り、GitHub 上の CI も通る）

## 6c 骨格（2026-11-04 済み）

担当 K1 の `tools/make_skeleton.py` で、目次から全357ページの骨格を `stubs/<field>/<id>.md` に作った。data の主のページが骨格を指すので、data のまとめと同じ commit にした。以後は front matter が正（目次は凍結）。check_all.py の13段が通る
