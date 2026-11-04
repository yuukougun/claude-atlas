# 工程7（試作）：1ページを書き、確かめ、直す担当への共通の指示

- 版：2026-11-04 v2（v1 から：材料の束を読む、事実と出典の検証と確かめ直しを置かない、雛形は動作を確かめていなくても載せる、報告を短くする。decisions 2026-11-04 の「事実と出典の検証」「ページの確かめ方」「雛形の動作確認」「執筆の担当が開く一次資料」）
- 対象のページと役割の割り当ては [README.md](README.md) にある

## 1. 背景

claude-atlas は、Claude 全般を使いこなすための、辞書として引く日本語の教材である。リポジトリは `/home/yuuki/projects/kyopro2/claude-atlas`。今日は 2026-11-04。いまは試作（工程7）で、型ごとに1ページを書き、確かめ、直す。試作の目的は、手引き・道具・設計が実際のページで回るかと、1ページの使用量を確かめることである。

**使用量を抑える**：読むのは §2 の3つのファイルだけにする。ほかのファイルを探して小分けに読まない（道具の呼び出しの数がそのまま使用量になる）。

## 2. 読むもの（3つ）

1. そのページの材料の束：`state/packets/<id>.md`（道具 `tools/make_packet.py` が作った。ページの front matter・つながるページの題名と要約・目次の materials と notes・data の該当の項目・出典の一覧・調査資料の該当の節の写し）
2. 執筆の手引き：`planning/guides/common.md`（全部）
3. そのページの型の手引き：`planning/guides/<型>.md`

束にないことが要るときだけ、ほかのファイルや一次資料を開く。一次資料（Web）は、束にないことと、変わりやすい値を数値の提案にするときだけ開く。開く前に、新しいドメインは `uv run python tools/check_noai.py <URL>` で確かめる（`.claude/settings.json` の deny にあるドメインは開かない）。

## 3. 置き場所（ページの id を <id>、分野を <field> とする）

- ページ：執筆の担当が `stubs/<field>/<id>.md` を `docs/<field>/<id>.md` へ移し（`mv`。git は使わない）、stage を draft にして書く。試作のページは公開から外してある（tools/gen/config.yml の held_back）
- 雛形：`snippets/<id>/<名前>.<拡張子>` と `<名前>.expect.yaml`（title と、安全とデータの雛形なら `safety: true`）。本文には `<!-- gen:begin snippet <id>/<名前> -->` 〜 `<!-- gen:end snippet <id>/<名前> -->` を置く。動作を確かめていなくても雛形は載せる（道具が確かめていないことを書く）。目次の templates の案を基本に、分かりやすさのために要る雛形は足してよい
- 図：`docs/img/<id>/`。ページごとの出典：`data/sources.d/<id>.yml`
- 報告：`planning/batches/step7/pages/<id>/` の下に `write.md`・`verify-clarity.md`・`fix.md`。数値の提案は `facts-proposal.yml`（手引き §21 の形）
- 目印の中身は `uv run python tools/gen_site.py --page <id>` で書く。検査は `uv run python tools/check_pages.py --page <id>` と `npm run lint:text`（自分のページの指摘だけを見る）

## 4. 役割

- **執筆**（Sonnet）：手引きのとおりに書く。終える前に `gen_site.py --page <id>`・`check_pages.py --page <id>`・`npm run lint:text` を流し、自分のページの指摘を0にする
- **分かりやすさの検証**（Sonnet。書いた本人とは別）：ページを読み、`planning/checklists/clarity.md` で確かめる。ページは直さない。指摘の表（番号｜重さ〔直す・直したほうがよい・軽い〕｜場所｜問題｜直し方の案）を `verify-clarity.md` に書く。事実の正しさは確かめなくてよい（事実と出典の検証は置かない）
- **直し**（Sonnet）：`verify-clarity.md` の指摘をすべて扱い、直したら執筆と同じ検査を流す。`fix.md` に指摘ごとの扱いを書く

描画・書き方・参照の検査は、メインが道具でまとめて流す。

## 5. 報告の形（短く）

`write.md` と `fix.md` は、手引き §21 の見出しのうち、書くことのあるものだけを、1項目1〜3行で書く。front matter のほかのキーの直しは §21 の YAML の形で提案する。§9 の使用量は、道具の呼び出しの数が分かれば書く。

## 6. 守ること

- 書いてよいのは §3 の置き場所の、自分のページのものと、自分の報告だけ。共有のファイル（用語集・prh.yml・data/ の3つのファイル・catalog・手引き・チェックリスト・schema・tools）は直さず、報告の「提案」に書く
- git と gh の操作をしない（制作の印があるので、書き込みは止められる）
- 変わりやすい値を本文に手で書かない（数値の目印と、数値の提案を使う）。事実を記憶で書かず、束の材料か一次資料に基づいて書く
- 公開の約束・方針・ライセンスに関わる文は、作者の承認が要る（手引き §18）。案を報告の「メインに判断してほしいこと」に書く
- 第三者を否定的な文脈で名指ししない
