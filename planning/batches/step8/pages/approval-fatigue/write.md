# approval-fatigue 執筆の報告

## 書いたファイル
- docs/safety/approval-fatigue.md（stub から移動。front matter は sections に check を足し、sources に 6 件、stage を draft、updated を 2026-11-05 にした）
- snippets/approval-fatigue/narrow-allow-and-ask.json と .expect.yaml（settings。狭い allow と ask）
- data/sources.d/approval-fatigue.yml は作っていない（出典はすべて data/sources.yml にある id を使った）

## 必ず持つものの対応
- 判断例（状況・迷う候補・選んだもの・理由）：keep-prompts（`!!! example` の中）
- 構成の目安（何が起きるか・なぜ・判断例・握るもの・確かめ方）：why（何が起きるか・なぜ）／keep-prompts（判断例・握るもの）／check（確かめ方）
- level：front matter の level: 整える（変更なし）

## メインに判断してほしいこと
- 93%・97%・13.6% は「研究の結果は固定の記録」（カード §7 の最後）として、研究名・日付・出所を添えて本文に書いた。目次の notes は「数値は数値ファイルに出典の日付付きで置く」とあるので、data/facts.yml に置いて目印にする道を選ぶなら、本文の該当 3 か所（why）を直す
- 「サンドボックスで自動許可を有効にすると、囲いの中の Bash は Manual でも確認なしに実行される（例外あり）」は 05 1-10 の写し（cc-docs-sandboxing を引く）に基づく。今日の一次資料では確かめていない

## 提案
- 数値の提案はなし。
- front matter の変更の提案はなし。

## 検査の結果
- 1 回目：エラー 0・警告 5。直した後（2 回目）：エラー 0・警告 2
- 残した警告：approval-fatigue.md の助詞「で」（reduce-prompts の 3 番の項目。生成されたリンク題名を含む長い 1 文）と、助詞「が」（check の「止められた操作を見直す」）。どちらも読みやすさを損なわないと判断した（誤検出ではなく軽い警告）

## 確かめていないこと
- auto モードの設定の読み先（`~/.claude/settings.json` のみ。プロジェクトの設定は読まない）、ask ルールが auto モードでも必ず確認を出すこと、`/auto-mode-setup`、`claude auto-mode config` は cc-docs-auto-mode-config を 2026-11-05 に 1 回読んで書いた（Web の取得 1 回）
- 雛形の動作は試していない
- 「習慣になる」という仕組みは類推で、Claude Code の利用者での検証はない
- 93%・97% の値は 2 つの記事の記述を調査資料（research/23）経由で写した。記事の原文は読み直していない
- Windows ネイティブ・IDE 拡張の動作は未確認

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：1 回
