# 工程6：土台を作る担当への共通の指示

- 版：2026-11-04 v1
- 担当ごとの受け持ちは [README.md](README.md) の表にある

## 1. 背景

claude-atlas は、Claude 全般を使いこなすための、辞書として引く日本語の教材のサイトである（MkDocs と Material for MkDocs。GitHub Pages で公開）。リポジトリは `/home/yuuki/projects/kyopro2/claude-atlas`（GitHub の yuukougun/claude-atlas。公開）。今日は 2026-11-04。

設計（工程3・4）とユーザーの承認（工程5）が終わり、いまは土台作り（工程6a）である。ページの本文はまだ書かない。あなたは、サイト・道具・縛りの土台の一部を作る。

## 2. 最初に読むもの

1. `planning/design.md`：§8（技術構成）全部と §9（鮮度）、§10.5（CLAUDE.md と縛り）、§3.3（front matter とキーの台帳）、§6.2（文体と用語）、§7（横断のページ）。受け持ちに関わる節は README の表とこの指示の §4 にもある
2. `planning/decisions.md`（2026-11-03・2026-11-04 の決定。特に「hooks と permissions」「公開する段階」「作者の表記と URL」「ライセンス」「工程5（決定の提示）の回答」）
3. `schema/site.yml`（語彙）、`planning/catalog/README.md`（目次の形。front matter の元）
4. 手本：`../kyopro-atlas`（同じ作者の教材。**読むだけ。ファイルを変えない・コミットしない・書き込まない**）。設計 §8.3 のとおり、汎用の部品は写して直し、分野や段階の名前の直書きは持ち込まない。kyopro-atlas の反省は `planning/research/20-kyopro-atlas-retrospective.md` にある

## 3. 守ること

- 書いてよいのは、README の表で割り当てたファイルと、自分の報告（`planning/batches/step6/build-<担当>.md`）だけ。ほかの担当と同じファイルを書かない。ほかのファイルへの変更が要るときは、報告に「提案」として書く
- **git の操作をしない**（読むだけのものも使わない）。`gh` も使わない
- Python の道具は Python 3.12 で動かす（`uv run`。design §8.1・DR-16）。PyYAML などは pyproject の依存にする。hooks だけは、標準のライブラリだけの `python3` で動く形にする（読者の環境でも動くため。design §10.5 の決まり5）
- 語彙（分野・型・段階など）をコードに直書きしない。`schema/site.yml` から読む
- 試験を書き、通してから終える（`uv run python -m unittest discover -s tests/tools` など。受け持ちの試験の場所は自分で決めて報告に書く）
- Web は、依存の取得（PyPI・npm）と、版の確かめ（公式の配布元）にだけ使う。AI の利用を断るサイト（atcoder.jp・codeforces.com など）は開かない
- 秘密（トークン・API キー）をファイルに書かない。環境に `ANTHROPIC_API_KEY` があっても使わない
- 第三者を否定的な文脈で名指ししない
- サイトに出る文（冒頭・フッター・トップ・README の説明）は、決定にある最小の文だけにする（decisions 2026-11-04「決定の一覧の承認」の補足）。それより多い方針の文は作者の承認の後に足すので、書かない

## 4. 担当ごとの要点

- **B1 サイトと CI**：Material 9.8 系と MkDocs 1.6.1 を固定（design §8.1。版は配布元で確かめて固定する）。`theme.font: false`、Mermaid は写しを置く（外のサイトから読まない。§8.5）。プラグインは search だけ。KaTeX は入れない。site_url は https://yuukougun.github.io/claude-atlas/。nav は `nav.yml`（いまは仮の手書き。後で道具が生成し、stub を `exclude_docs` に書く。INHERIT で効くかを確かめて報告する）。冒頭とフッターの文は決定の最小の文。CI は design §8.6 の表のうち、いま作れるもの（ビルド・Zensical の試験ビルド・外部リンクの週1回）の骨組みと、デプロイ（GitHub Actions で Pages。必須の検査の後）。終わりの条件：`uv run mkdocs build --strict` が通る
- **B2 読む層と data**：front matter・catalog・data・site.yml を読み、ページのモデルを作る（design §8.3 の読む層）。`tools/check_catalog.py` の読む層の作りが参考になる（写すか、共通にするかは報告に書く）。`schema/page.schema.json` はキーの台帳（§3.3）と site.yml から作る道具にする（DR-16）。data の schema（facts・sources・sources.d・outdated-advice。§9.1 と DR-11・DR-18）と、空の data のファイル
- **B3 書き方の検査**：textlint と prh（design §6.2・§8.6）。kyopro-atlas の `.textlintrc.json`・`prh.yml`・`tools/textlint_targets.py`・`package.json` を手本にする。prh の初めの規則は、design §6.2 と research/27 §3.1 の表（公式の日本語版の多数派）と、工程5の決定（plan mode・effort・allow／ask／deny ルールは英語のまま）。用語集のページ（start の glossary）を正とし、prh はそこから作る決まりなので、いまは初めの版として作り、作り方を報告に書く
- **B4 縛り**：design §10.5 の H1〜H4 と5つの決まり、DR-08（強制は deny、hook は理由と記録、担当の git は読むだけ、制作の印 `state/production` があるときだけ働く縛り、H4 は check_templates.py の中へ移す前提で hook は知らせるだけ）。`.claude/settings.json` の permissions と hooks、hook のスクリプト（標準のライブラリだけ）、`.claude/README.md`（何が入っていて何をするか・読者の環境で何が動き何が動かないか・依存が欠けたときにどうなるか）、hook の試験（入力の JSON を与えて出力を確かめる）。CLAUDE.md は短く、推測できないことだけ（§10.5 の中身）。hook の入力の形（agent_id など）は research/28 を見る
- **B5 手引きとチェックリスト**：執筆の共通の手引きと型ごとの手引きの第1版、検証の4つの観点のチェックリスト（design §6・§10.2、DR-12 の F16 の3点）。見本のページは試作（工程7）で決めるので、手引きには置き場所だけを作る

## 5. 報告の形（`planning/batches/step6/build-<担当>.md`）

1. 作ったファイルと中身の要約
2. 確かめたこと（試験・ビルド・版の確かめの結果）
3. 決めたこと（設計書に書いていない細部をどう決めたか）
4. 提案（ほかの担当のファイル・設計書への変更）
5. 確かめていないこと

最後の返答（メインへの報告）は300字まで。
