# write.md：what-not-to-delegate（執筆）

## 書いたファイル
- `docs/delegate/what-not-to-delegate.md`（`stubs/delegate/` から `mv`）。雛形・図・`data/sources.d/` は作っていない（目次の templates なし、新しい出典なし）
- front matter で変えたキー：`stage`（stub→draft）、`updated`（2026-11-05）、`sources`（既存の id 9 件）、`sections`（`what-it-prevents` を 1 節足した。既存の 4 つは不変）

## 必ず持つものの対応
- 冒頭の要点（最初の項目は「何が分かるか」）：冒頭の囲み
- `principle`（握る）を本文で名指す：`what-it-prevents`（握る原理の説明と four-principles#hold）。導入文でも触れた
- `prevents`（確かめていない）：`what-it-prevents`（2 段落目）
- `pitfalls`（預けすぎる・やめられない）：`what-it-prevents`（箇条 2 つ）
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：`what-humans-hold` と `what-to-delegate`（何を握り何を任せるか、事例）→ `verifiable-axis`（なぜ。検証器が問題を定義する）→ `what-it-prevents`（何に効くか）→ `who-adopted`（誤解：考察は人間にしかできない）→ 関連はテンプレート。「何が起きるか」は独立の節にせず `what-it-prevents` の冒頭と事例で持つ

## メインに判断してほしいこと
- `who-adopted` の AtCoder World Tour Finals 2026 の記述は、束の報道 2 件の題名と材料の要約だけに基づく（根拠：弱）。研究資料 25 P1 を読んでいないので、記述が材料と合うか確認してほしい。合わなければ該当の箇条を削る
- 事例の人名（Kaggle 1 位の参加者・Unagi 等）は出していない（第三者の扱い）。書き方の方針（第三者）1 に照らして問題ないか

## 提案
```yaml
frontmatter: []
```
- 用語集・prh・data への提案はなし

## 検査の結果
- 1 回目（書いた後）：エラー 0・警告 10。判断例の（a）（b）、読点、助詞の重複、長文などを直した
- 2 回目（直した後）：エラー 0・警告 3（`に` の重複 2 件、`も` の重複 1 件。94・104・105 行）。意味を損なう直しになるため残した。誤検出ではなく、メインか検証の担当が直してよい

## 確かめていないこと
- 事例の数値・主張（ICFP 2025、AHC056・AHC058、Kaggle、Battlecode、CSAW、Vaccaro、Sleesman）は束の写しのとおりに書き、一次資料を開いて照合していない（Web の取得は 0 回）
- 根拠の印は束の「根拠」欄に合わせた。Battlecode は束で「中」としたが、参加チーム自身の振り返りとして「弱」に下げた
- 「本番環境の制約」の説明文は材料の 1 行に基づく短い記述で、出典の裏付けは取っていない
- 人間の上位勢を AI が上回ったという報道の内容（上の判断してほしいこと）
- link の `decide-when-to-quit` は準備中表示（公開前）。生成後の表示は未確認

## 使用量
- 道具の呼び出し：約 12 回（Read 3、Bash 7、Write 2 を含む）。Web の取得：0 回
