# 報告：執筆（claude-md-vs-rules-skills-styles）

- 手引きの版：共通 2026-11-04 第1版・型（comparison）2026-11-04 第1版
- 書かなかった見出し（範囲を越えたこと・止められた操作）は、なしのため省いた

## 1. 書いたファイル

- `docs/extend/claude-md-vs-rules-skills-styles.md`（stub から移して draft にした）。front matter で変えたキーは `sections`（6 節：table・how-to-choose・combine・verify・reach・similar-names）・`sources`（10 件）・`stage`（draft）・`updated`（2026-11-04）
- 構成：要点 → 比較の表（生成）と表の補足 → 選び方（軸 3 つ・問い 6 つ・判断例 5）→ 組み合わせ方（雛形 4）→ 読み込まれたかの確かめ方 → 届く範囲の違い → 名前が似た別の機能。図は置いていない（目次の visual なし）
- 雛形：`snippets/claude-md-vs-rules-skills-styles/` の `claude-md-root.md`・`rules-testing.md`・`skill-release.md`・`output-style-dearu.md` と、それぞれの `.expect.yaml`。`.expect.yaml` には `title` のほかに `features` を付けた（gen が読む項目。付けないと「要る最低の版」が tracks の最大の 2.0.64 になり、CLAUDE.md や出力スタイルの雛形に当てはまらない）
- `data/sources.d/claude-md-vs-rules-skills-styles.yml`：`cc-docs-cloud-environments` を新設。ほかの出典は既存の id（Steering ブログは `claude-blog-steering-code-skills-hooks`）

## 5. メインに判断してほしいこと

1. 比較の表が 9 列で、面と成熟度は 4 行とも同じ値である。幅 390px で広くなる見込みなので、全行同じ列を省くか、列を選べるようにするか決めてほしい（描画は未確認）。
2. rules の「圧縮で残るか」が表で「未確認」になる。本文で理由を補った。表の言葉を「場合による」にするか、rules を `paths` の有無で 2 機能に分けるか決めてほしい。
3. claude.ai の Styles は、告知日（2026-06-01）と「2026-11-04 時点で元の記事が読めない」ことだけを書き、メニューが今も出るかは「確かめていない」とした。research/26 は 2026-11-03、`sources.yml` の note は 2026-11-04 と日付が違う。本文は後者に合わせた。
4. Steering ブログの取得結果の要約は「`paths` 付きの rules も圧縮で入れ直される」と読める。memory 文書の本文と data の note は「要約に消えて読み直される」と書く。本文は後者に従い、ブログは rules の圧縮の根拠に使っていない。ブログの原文は確かめていない。
5. 節を目安の 4 つより多い 6 つにした（確かめ方・届く範囲・似た機能を足した）。薄いと見るなら、確かめ方は選び方の末尾、似た機能は組み合わせ方の末尾に畳める。

## 6. 提案

```yaml
frontmatter:
  - {id: claude-md-vs-rules-skills-styles, key: related, before: [output-style-modes#vs-claude-md, what-to-put-in-claude-md, where-to-put-instructions, extensions-at-a-glance, request-lock-table, using-auto-memory, hook-vs-skill, when-to-add-what, keep-replies-in-japanese], after: [output-style-modes#vs-claude-md, what-to-put-in-claude-md, where-to-put-instructions, extensions-at-a-glance, request-lock-table, using-auto-memory, hook-vs-skill, when-to-add-what, keep-replies-in-japanese, what-subagents-dont-inherit, skills-in-the-app#migrated-styles], reason: "本文の「届く範囲の違い」と「名前が似た別の機能」で指しているため（任意）"}
```

- 用語集（語・定義・anchor の案）
  - 出力スタイル：Claude Code で、セッション全体の役割・口調・応答の形を変える指示。claude.ai の Styles とは別の機能（`definitions`）
  - Styles（claude.ai）：アプリで応答の調子と形式を選ぶ機能。2026-06-01 にスキルへの移行が告知された。Claude Code の出力スタイルとは別（`same-names-across-surfaces`）
  - fork：親の会話とシステムプロンプトを丸ごと引き継いで分かれるサブエージェント。出力スタイルが効く（`definitions`）
- 道具（tools/gen の compare）：全行が同じ値の列を省く。値が null のときの言葉を、属性ごとに「場合による」などへ変えられるようにする
- 手引き：型の手引き（comparison）の目安に「確かめ方」を足すか決める（共通 §6 の「どう確かめるか」と目安に差がある）。共通 §5 に「四つ・一つ・二つ」は textlint の警告になるので「4 つ」と書く、と一言足すと迷わない
- 数値の提案：なし（変わりやすい値は手で書いていない。組み込みの出力スタイルの名前と数は書かず、output-style-modes に任せた）

## 7. 検査の結果

- `gen_site.py --page`：目印を埋め、`--check` で差なし
- `check_pages.py --page`：エラー 0・警告 0
- `check_templates.py --page`：エラー 0・警告 0
- `npx textlint`：最初は警告 10（四つ・一つ・二つの数字と、助詞の「に」の重なり）。直して 0。`npm run lint:text` でこのページの指摘は 0
- `render_pages.py`：流していない（メインが流す）

## 8. 確かめていないこと

- 雛形 4 本は実機で読み込ませていない（道具が「動作を確かめていない雛形」と書く）。日本語の description でスキルの呼び出しの制御が変わらないかも未確認
- `/context all` の「Memory files」に rules が出るかは確かめていない。本文は CLAUDE.md に限って書いた
- WSL 以外の OS と、IDE 拡張・デスクトップアプリでの動作は確かめていない。本文は CLI を基準にし、ほかの面は書いていない
- 読んだ一次資料：output-styles・memory・settings・cloud-environments は本文を読んだ。skills・sub-agents・Steering ブログは取得ツールの要約だけで、skills と sub-agents は末尾の約 15% を読んでいない
- deny ルールで `.env` を止める範囲（Bash 経由で読む場合など）は確かめていない。判断例は「deny ルールかフック」と書くにとどめ、強さは request-lock-table に任せた

## 9. 使用量

- 道具の呼び出しは約 85 回（Read 8・Write 1・Edit 21・Bash 約 44・WebFetch 7・ToolSearch 1。write.md の書き込みを除く）。Web の取得は 8 回（WebFetch 7・curl 1）
- かかった時間は計っていない。ファイルの更新時刻からは約 30 分
