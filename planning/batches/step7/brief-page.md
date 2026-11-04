# 工程7（試作）：1ページを書き、確かめ、直す担当への共通の指示

- 版：2026-11-04 v1
- 対象のページと役割の割り当ては [README.md](README.md) にある

## 1. 背景

claude-atlas は、Claude 全般を使いこなすための、辞書として引く日本語の教材である。リポジトリは `/home/yuuki/projects/kyopro2/claude-atlas`。今日は 2026-11-04。いまは試作（工程7）で、型ごとに1ページを書き、確かめ、直す。試作の目的は、手引き・チェックリスト・道具・設計が実際のページで回るかを確かめ、直すべき所を見つけることである。

## 2. 読むもの（役割に関わらず）

- 執筆の手引き：`planning/guides/common.md`（全部）と、そのページの型の手引き（`planning/guides/<型>.md`）
- そのページの front matter（`stubs/<field>/<id>.md`、執筆の後は `docs/<field>/<id>.md`）と、目次の項目（`planning/catalog/<field>.yaml` の同じ id。materials・templates・visual・notes）
- 出典の手がかり：`planning/batches/step6/data/wave1-sources.yml`（第一波のページごとの出典の id）、`data/sources.yml`・`data/facts.yml`・`data/outdated-advice.yml`
- 決定：`planning/decisions.md`（新しい日付が優先）。設計：`planning/design.md`（手引きが名指しする節）

## 3. 置き場所（ページの id を <id>、分野を <field> とする）

- ページ：執筆の担当が `stubs/<field>/<id>.md` を `docs/<field>/<id>.md` へ移し（`mv`。git は使わない）、stage を draft にして書く。試作のページは公開から外してある（tools/gen/config.yml の held_back）
- 雛形：`snippets/<id>/`（design §8.7。期待は `<名前>.expect.yaml`）。図：`docs/img/<id>/`。ページごとの出典：`data/sources.d/<id>.yml`
- 報告：`planning/batches/step7/pages/<id>/` の下に、役割ごとに `write.md`・`verify-fact.md`・`verify-clarity.md`・`verify-render.md`・`fix.md`・`recheck.md`。数値の提案は `facts-proposal.yml`（手引き §21 の形）
- 目印の中身は `uv run python tools/gen_site.py --page <id>` で書く。検査は `uv run python tools/check_pages.py --page <id>` と `npm run lint:text`（自分のページの指摘だけを見る。ほかの担当が同時にほかのページを書いている）

## 4. 役割

- **執筆**：手引きのとおりに書く。終える前に手引き §20 の検査を流す。報告は `write.md`（手引き §21 の形。§9 の使用量は、分かる範囲で道具の呼び出しの数と時間）
- **検証**（事実・分かりやすさ・描画のどれか）：そのページと、執筆の報告を読み、チェックリスト（`planning/checklists/common.md` と、自分の観点のもの：`fact.md`・`clarity.md`・`render.md`）で確かめる。ページは直さない。指摘の表（番号｜重さ〔直す・直したほうがよい・軽い〕｜場所｜問題｜根拠｜直し方の案）を報告に書く。事実の検証は、主張ごとに一次資料を開いて照らし、数値の提案のファイルも照らす。描画の検証は、一時のフォルダにリポジトリを写し（`docs/`・`stubs/`・`data/`・`schema/`・`tools/`・`overrides/`・`mkdocs.yml`・`nav.yml`・`pyproject.toml`・`uv.lock`）、写しの `tools/gen/config.yml` の held_back からそのページを外して `uv run python tools/gen_site.py --root <写し>`、`uv run mkdocs build -f <写し>/mkdocs.yml -d <写し>/site`、`uv run python tools/render_pages.py <写し>/site --page <id>` を流して見る（リポジトリの site/ には書かない）
- **直し**：3つの検証の報告の指摘をすべて扱う。直したら手引き §20 の検査を流す。報告は `fix.md`（指摘ごとに、直したこと・直さなかった理由）
- **確かめ直し**：直しの差（直しの報告と、検証の報告の指摘）を確かめる。指摘が残っていなければ stage を reviewed にし、`verified`（今日の日付）と `verified_with` を書く（design §3.3・DR-10）。残っていれば reviewed にせず、残った指摘を報告 `recheck.md` に書く

## 5. 守ること

- 書いてよいのは §3 の置き場所の、自分のページのものと、自分の報告だけ。ほかのページ・共有のファイル（用語集・prh.yml・data/ の3つのファイル・catalog・手引き・チェックリスト・schema・tools）は直さず、報告の「提案」に書く
- git と gh の操作をしない（制作の印があるので、書き込みは止められる。読むだけはよい）
- 一次資料を開く前に、新しいドメインは `uv run python tools/check_noai.py <URL>` で確かめる。`.claude/settings.json` の deny にあるドメインは開かない（止められたら回り込まない）
- 変わりやすい値を本文に手で書かない（数値の目印と、数値の提案を使う）。事実を記憶で書かない
- 公開の約束・方針・ライセンスに関わる文は、作者の承認が要る（手引き §18）。案を報告の「メインに判断してほしいこと」に書く
- 第三者を否定的な文脈で名指ししない
