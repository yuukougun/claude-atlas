# 報告：執筆（instructions-ignored）

- 手引きの版：共通 2026-11-04 第1版・型（symptom）2026-11-04 第1版

## 1. 書いたファイル

- `docs/symptoms/instructions-ignored.md`（`stubs/` から `mv`。front matter で変えたキーは `sections`〔forms・examples・prevention を足した。diagnosis は変えず〕・`stage`〔draft〕・`updated`〔2026-11-04〕・`sources`〔空から 11 件〕）
- `docs/img/instructions-ignored/two-layers.svg`（目次の図の案「お願いと鍵の二層」。static）
- `snippets/instructions-ignored/claude-md-command-rule.md` と `.expect.yaml`（claude-md 種。目次の templates は「なし」だが、二層の「お願いの側」の例として 1 つ足した。動作は確かめていない）
- `planning/batches/step7/pages/instructions-ignored/facts-proposal.yml`（数値の提案 2 件）
- `data/sources.d/instructions-ignored.yml` は作っていない（出典は全部 `data/sources.yml` にあった）

## 5. メインに判断してほしいこと

- **signs の表記**：prh が本文の「skill」を「スキル」に直させる。signs「作った skill が使われない」と本文（「作ったスキルが使われない」）が食い違う。signs を直すか、読者の言葉として prh に例外を置くか、決めてほしい（下の提案 2）。
- **compare の表が 9 列**（機能・面・成熟度・強制力・読み込みの時期・コンテキストのコスト・圧縮で残るか・入った版・確認日）で、スマホで横に広い。列を選べる指定（例：`gen:begin compare 強制力 読み込みの時期 圧縮で残るか`）が道具にあるとよい。表は残した（お願いと鍵の差を 1 枚で見せるため）。
- **面のタブ**：診断の 3 項目それぞれに「アプリ」「Claude Code」のタブを置いた（番号つきの項目の中に入れ子）。textlint はタブの中の段落を検査しないので、空白と助詞は自分で読んで確かめた。描画は未確認。
- **束の材料の足し方**：症状の型の束に、公式の Troubleshoot 節（memory）と Troubleshooting 節（skills）、sub-agents の「What loads at startup」を足すと、Web の取得が要らなくなる。今回はこの 3 つと組織の指示の記事で Web を 5 回取得した。
- 公開の約束・方針に当たる文は書いていない（§18）。

## 6. 提案

```yaml
frontmatter:
  - {id: instructions-ignored, key: related, before: [emphasis-words, hook-vs-skill, request-lock-table, hooks-basics, block-with-exit-2, where-to-put-instructions, init-and-first-claude-md, forgot-after-compaction, replies-in-english, repeating-the-same-explanation, inconsistent-japanese-style, isolate-with-safe-mode, lock-side-effects, six-causes], after: [emphasis-words, hook-vs-skill, request-lock-table, hooks-basics, block-with-exit-2, where-to-put-instructions, init-and-first-claude-md, forgot-after-compaction, replies-in-english, repeating-the-same-explanation, inconsistent-japanese-style, isolate-with-safe-mode, lock-side-effects, six-causes, not-what-i-meant, forgets-in-long-chats], reason: "目次の level_evidence が、会話の中の指示が守られないときの振り分け先に挙げている。本文の診断の節で指した。"}
  - {id: instructions-ignored, key: signs, before: [{type: symptom, text: 作った skill が使われない}], after: [{type: symptom, text: 作ったスキルが使われない}], reason: "prh が本文の skill をスキルに直させるため、signs と本文の表記を揃える。別案は prh の例外。"}
```

- 用語集：読んでいない。「お願い」「鍵」「圧縮」が未収録なら足す。定義は本文の初出の括弧に書いた（お願い＝Claude が読んで判断する指示、鍵＝毎回必ず効く制御、圧縮＝長い会話を要約に置き換えること）。
- data：facts が空で目印が使えない。推奨の長さ（200 行）と `/doctor prompt-audit` の最低の版（2.1.283）を `facts-proposal.yml` に出した。サブフォルダの CLAUDE.md などの 1 ファイルの文字数の上限（窓の大きさとモデルで違う。2.1.309 以降）は表の形になるため出していない。claude-md-loading-order の担当が table で出すのがよい。
- claude-md-loading-order への材料：AGENTS.md は、CLAUDE.md が作業ディレクトリかその上にあると読まれない（公式 memory の「My AGENTS.md isn't loading」）。本文には入れなかった。
- catalog：templates が「なし」のままなので、この雛形（`claude-md-command-rule`）を反映するか決めてほしい。

## 7. 検査の結果

- `gen_site.py --page instructions-ignored`：成功。`check_pages.py --page instructions-ignored`：エラー 0・警告 0。
- `npx textlint docs/symptoms/instructions-ignored.md` と `npm run lint:text`（自分のページ）：指摘 0。`check_svg.py --page`：0。`check_templates.py --page`：エラー 0・警告 0。
- 初回の textlint はエラー 3・警告 14 だった。算用数字の前後の空白、skill → スキル、助詞の重なりを直して 0 にした。signs と同じ読者の言葉「書いたのに」も助詞の重なりに当たったため、「書いたが」に変えた。

## 8. 確かめていないこと

- 一次資料で確かめた（2026-11-04 に取得）：公式の memory・skills・sub-agents の文書と、組織の指示の記事。診断のうち Claude Code の項目の多くはこれに基づく。
- 確かめていない：アプリのタブの「置き場所ごとに効く範囲が違う」「プロジェクトの指示はそのプロジェクトのチャットにだけ効く」は research/27 §3.2 と目次の要約による。権限ルールの限界（パスの書き方が合わず当たらないルール・子プロセスに効かない場合）は目次の permission-rules の要約による。
- 確かめていない：フック・権限・rules・スキルの圧縮の扱いのうち memory と skills に書かれていない分は、束の data の note（確認済み）による。hooks-guide・permissions の文書は開いていない。
- 開いていない：実践者の記事 3 件（束の要約による。（根拠：弱）を付けた）、Best practices の現行の版（強調の扱いは束の台帳の行による）。
- 未確認：WSL・Linux 以外の OS と IDE の拡張。図と表の描画（ライト・ダーク・幅 390px）。雛形の動作。読んでいない：用語集、clarity のチェックリスト（指示の 3 つだけを読んだ）。
- 版に依存する記述（`/context all`・`/status` の警告・`Loaded` の行・InstructionsLoaded・`/doctor prompt-audit`）は、版を本文に書いていない。

## 9. 使用量

- 道具の呼び出しは約 47 回（Bash 約 27・Web の取得 5・Read 7・Write 6・Edit 1・ToolSearch 1）。Web の取得は 5 回（memory・skills〔2 回〕・sub-agents・組織の指示）。所要時間は計っていない。
