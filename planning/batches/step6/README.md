# 工程6（土台作り）のバッチ

設計書（[../../design.md](../../design.md)）の §8〜§10 に従って、サイト・道具・縛りの土台を作る。工程は 6a（土台）→ 6b（data の初版）→ 6c（骨格）。終わりの条件は design §10.1 の表にある。

- 始めの作業（2026-11-04 済み）：planning/ の実名の検索（N1。[names-N1.md](names-N1.md)）、GitHub の公開のリポジトリ yuukougun/claude-atlas の作成と push
- 担当は報告をファイルに書いてから終える。止まったときは、報告のない担当だけを同じ割り当てで流し直す（その担当が書いたファイルだけを最後の commit に戻してから）
- 担当は git の操作をしない。commit と push はメインが行う。担当が書くのは、割り当てたファイルと自分の報告だけ
- 共通の指示は [brief-build.md](brief-build.md)

## 6a 1段目（並列。書くファイルが重ならないように分けた）

| 担当 | 書くもの | 報告 | 状態 |
| --- | --- | --- | --- |
| B1 | サイトと CI：`pyproject.toml`・`uv.lock`・`.python-version`・`mkdocs.yml`・`nav.yml`（仮）・`docs/index.md`・`overrides/`（テンプレートの骨組みと、冒頭とフッターの文）・`.github/workflows/`・`README.md`・`LICENSE`・`LICENSE-docs` | `build-B1.md` | 実行中 |
| B2 | 読む層と data：`tools/lib/`・`schema/page.schema.json` を作る道具・`schema/` の data の schema・`data/` の空の雛形・`tests/tools/` の読む層の試験 | `build-B2.md` | 実行中 |
| B3 | 書き方の検査：`package.json`・`package-lock.json`・`.textlintrc.json`・`prh.yml`・`tools/textlint_targets.py` と試験 | `build-B3.md` | 実行中 |
| B4 | 縛り：`CLAUDE.md`・`.claude/settings.json`・`.claude/hooks/`・`.claude/README.md`・hooks の試験 | `build-B4.md` | 実行中 |
| B5 | 手引きとチェックリスト：`planning/guides/`（共通の手引きと型ごとの手引きの第1版）・`planning/checklists/`（検証の4つの観点） | `build-B5.md` | 実行中 |

## 6a 2段目（1段目の後）

作る層（`tools/gen/`・`gen_site.py`）、検査の層（`tools/checks/`・`check_pages.py`・`check_templates.py`・`render_pages.py`・`check_svg.py`・`check_all.py`）、見た目（`overrides/` の CSS と JS：バッジ・下書きの帯・期限切れの表示・前提と次に読む・知識マップ・絞り込み）。1段目の報告を見て割り当てる。

## 6a 3段目：つなぐ

空のサイトのビルドとデプロイ（GitHub Pages）、CI の検査、hooks がワークフローの担当にも効くかの確かめ、制作の権限モード、手元の Chrome と日本語のフォント。

## 6b・6c

data の初版（一次資料で確かめ、別の担当が照らす）と、骨格（目次から全ページの stub を作る）。6a の後に割り当てる。
