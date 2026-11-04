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

## 6a 2段目（1段目の後）

作る層（`tools/gen/`・`gen_site.py`）、検査の層（`tools/checks/`・`check_pages.py`・`check_templates.py`・`render_pages.py`・`check_svg.py`・`check_all.py`）、見た目（`overrides/` の CSS と JS：バッジ・下書きの帯・期限切れの表示・前提と次に読む・知識マップ・絞り込み）。1段目の報告を見て割り当てる。

## 6a 3段目：つなぐ

空のサイトのビルドとデプロイ（GitHub Pages）、CI の検査、hooks がワークフローの担当にも効くかの確かめ、制作の権限モード、手元の Chrome と日本語のフォント。

## 6b・6c

data の初版（一次資料で確かめ、別の担当が照らす）と、骨格（目次から全ページの stub を作る）。6a の後に割り当てる。
