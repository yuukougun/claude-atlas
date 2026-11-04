# write.md：tidy-the-desk（執筆）

## 書いたファイル
- docs/context/tidy-the-desk.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に cc-docs-best-practices・cc-docs-commands・cc-docs-context-window・cc-docs-how-claude-code-works・cc-docs-sub-agents・hc-context-window・hc-usage-limits を追加）
- sections に 2 節を足した：`effect`（何に効くか（見せる・散らかっている））、`misconceptions`（よくある誤解と意見の幅）。既にある 4 つの anchor は変えていない
- 雛形なし（目次の templates が「なし」）、data/sources.d の新規ファイルなし（出典は既存の id だけ）、図は本文中の Mermaid 1 つ

## 必ず持つものの対応
- どの原理・どの原因に関わるか：`#effect`（原理「見せる」と原因「散らかっている」を名指し。pitfalls は空なので名指しなし）
- level を持つ：front matter の level は「整える」。要点の最初の項目は「何が分かるか」にした
- 構成の目安（要点 → 何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：要点（冒頭）→ `#four-actions`（何が起きるか／図）→ `#why-now`（なぜ）→ `#effect`（何に効くか）→ `#in-the-app`・`#examples` → `#misconceptions`（誤解）→ 関連（テンプレートが出す）

## メインに判断してほしいこと
- 「任せる」のアプリでの手段は、束に材料がなく確かめていない。「別のチャットで調べて結論だけ持ち帰る手作業」を（推論・実践例なし）の印付きで 1 文だけ書いた。不要なら削る
- 節の題 `{#four-actions}` の「四つの動作」は、既存の title を変えなかった（カード §4 の「四つ」の警告は出なかった）

## 提案
- 用語集・prh・data・front matter への提案なし
- 数値の提案なし（本文に数値・既定値・版を書いていない。idle compaction の条件は compact-and-auto-compact#idle-compaction へ送った）

## 検査の結果
- 1 回目：エラー 0・警告 2（no-doubled-joshi の「が」2 件）。直した
- 2 回目は流していない：直しの途中で警告が 1 件（「も」）残ると分かり、文を書き換えただけで、再実行は上限の 2 回を守るため未実施。メインの一括の検査で確かめてほしい

## 確かめていないこと
- 3 つ目の修正文の textlint の結果（上記）
- link の目印の中身（目印は空で置き、check_page.py が埋めた。未公開のページは「準備中」で出る）
- Claude Code の `/rewind` を Esc 2 回でも開く点は 03 Q3（英語圏の実践者の記述）に基づく。公式の文書では確かめていない
- 「Best practices の 2026 年 10 月下旬の改稿」の時期は束の台帳の行（approx）による。Web の取得はしていない
- アプリ・その他の OS・IDE 拡張の動作は未確認

## 使用量
- 道具の呼び出し：約 10 回（Read 3、Bash 6、Write 2）。Web の取得：0 回
