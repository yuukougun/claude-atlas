# when-ai-is-unavailable 執筆の報告

## 書いたファイル
- `docs/cost/when-ai-is-unavailable.md`（stub から移した。stage は draft。updated は 2026-11-05）
- front matter で変えたキー：`sections`（cause・misconceptions を足した。既存の 3 つは不変）・`sources`（既にある id の 5 つ：hc-usage-limits・hc-claude-code-plan・hc-wrap-up-allowance・cc-docs-interactive-mode・cc-docs-settings-reference）・`stage`・`updated`
- `snippets/when-ai-is-unavailable/no-ai-runbook.md` と `no-ai-runbook.expect.yaml`（目次の「AI が止まったときの手順書の雛形」。kind: other、safety: false）
- `data/sources.d/when-ai-is-unavailable.yml` は作っていない（新しい出典なし）

## 必ず持つものの対応
- 冒頭の要点（最初の項目は「何が分かるか」）：ページ冒頭の囲み
- どの原理・どの原因に関わるか（`principle: 握る`・`pitfalls: 預けすぎる` を本文で名指す）：{#cause}。`prevents` は空なので、原因は名指さず、その理由を同節に 1 文で書いた
- 型の構成の目安（何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：{#kinds}（何が起きるか）→ {#minimum-without-ai}・{#fallbacks}（なぜ・どう備えるか）→ {#cause}（何に効くか）→ {#misconceptions}（誤解）。関連は page-links の目印
- level（任せる）：front matter のとおり。比例則の守りは {#minimum-without-ai} と {#fallbacks} の Claude Code のタブ（progress-files#guards を指す）

## メインに判断してほしいこと
- 障害の事例（2026-08-16 の報道）は、備考の指示どおり使っていない。日付を一次資料で確かめれば足せる
- 「公式の稼働状況の情報」へのリンクは、URL を確かめていないので手書きのリンクにしていない。status 系の出典を data に足すかどうか
- {#fallbacks} の「API は、プランの枠とは別の経路」は、link 先の usage-credits-basics#vs-api-credits と facts の note（API キーでは Wrap-Up Allowance・自動の継続が効かない）に基づく書き方で、API の上限の中身は書いていない

## 提案
- front matter・用語集・data への提案は、なし

## 検査の結果
- 1 回目：エラー 0・警告 8。直した後（2 回目）：エラー 0・警告 5
- 残した警告 5：no-doubled-joshi（助詞「に」「が」）4 件と max-ten（読点 4 つ）1 件。すべて文の自然さを損なわずには直しにくい箇所で、誤検出ではないが重くない（検証の担当が見てよい）

## 確かめていないこと
- 本文の事実は、束の写し（data の features・research 22 #26・#36・調査資料）に基づく。一次資料は開いていない（Web の取得は 0 回）
- 「続けた作業でも許可の確認は出る」「API キー・背景のセッション・`-p` では自動の継続が使えない」は、束の写しのとおりで、実機では試していない
- 雛形の動作は確かめていない（空欄を埋める手順書の雛形で、動作の確認は要らない種類）
- 「大会中に AI の上限や障害に当たった参加記は見つからなかった」は、research 10 第23章の記述に基づく
- Desktop・ほかの OS・IDE 拡張の動作は未確認（本文にも Claude Code のタブで書いた）

## 使用量
- 道具の呼び出し：約 14 回（Read 2、Bash 5、Write 3、Edit 6 を含む）。Web の取得：0 回
