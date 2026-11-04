# write.md：before-opening-unknown-repos（執筆）

## 書いたファイル

- `docs/safety/before-opening-unknown-repos.md`（stubs から mv。stage を draft、updated を 2026-11-05。sections に guards・steps・verify・when-it-fails を足した。既存の 4 つの anchor は変えていない。sources に既存の id を 6 つ置いた）
- `snippets/before-opening-unknown-repos/` に open-checklist.md（目次の templates の案）・list-auto-run-files.sh・trust-probe.json と、それぞれの `.expect.yaml`
- `data/sources.d/` のファイルは新しい出典がないので書いていない

## 必ず持つものの対応

- 手順：`#steps`（6 段。各段に「確かめ」）
- 確かめる・縛るのページへの道：`#guards`（protecting-secrets・permission-rules・where-bypass-is-ok）。front matter の prerequisites に prompt-injection-in-practice・permission-rules。related に vetting-extensions・sandboxing ほか
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：`#guards` → `#files-to-check`・`#trust`・`#headless`・`#isolate`（手順の材料）→ `#steps` → `#verify` → `#when-it-fails`
- level：front matter に「任せる」あり

## メインに判断してほしいこと

- 先に整える守りの 2 は、「プロジェクトの deny と ask は信頼と関係なく効く」（research/28 #19）から、自分の側の deny を先に置く、と読んだ。自分の（ユーザーの）deny が信頼の前から効くかは束に明記がないので、本文では書き分けていない
- `#isolate` の「手元の認証情報を持ち込まない」は、where-bypass-is-ok#requirements の中身を見ずに一般論として書いた。そのページの条件と食い違うなら直す
- `#files-to-check` の表の `.vscode/` は、Check Point の推奨に名前があるだけで、動作は未確認と本文に書いた

## 提案

- front matter の直しの提案はなし
- 数値の提案（facts-proposal.yml）はなし。年月は研究の記録として書いた（修正の月は 2025-08・09・12。Check Point の記事の日付）

## 検査の結果

- `check_page.py` は 2 回流した。最終はエラー 0・警告 5
- 警告は ja-technical-writing/no-doubled-joshi の 5 件（54・153・155・172・184 行）。桁の位置が、link の目印が展開した題名（例「権限ルールとサンドボックスの二重にする」）の内側で、題名の助詞を数えていると見える。本文の文は 1 回の直しで短くしたが、残った。誤検出として残した
- 1 回目に出た snippet の YAML の警告（backtick で始まる値）は直した

## 確かめていないこと

- 雛形 3 つは動かしていない。trust-probe.json の SessionStart フックの書式（`hooks` の入れ子）は記憶に基づくので、公式の文書で確かめていない
- 対話で信頼を受け入れずに閉じたときの画面の選択肢の名前は、本文で書いていない
- 修正の月（2025-08・09・12）と「後の 2 つは信頼の確認より前」は、束の 05 4-3 の写しによる。原典の記事は開いていない
- `.claude/` の下のスキルやサブエージェントの定義が非対話でどう扱われるかは、research/28 #30 の写しのままで、一次資料は開いていない
- WSL・Linux 以外の OS と IDE 拡張の動作は未確認

## 使用量

- 道具の呼び出し：約 16 回（Read 4・Bash 6・Write 8 を含む。check_page は 2 回）。Web の取得：0 回
