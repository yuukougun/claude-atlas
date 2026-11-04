# write.md：followed-injected-instructions（執筆）

## 書いたファイル
- docs/symptoms/followed-injected-instructions.md（stubs から mv。stage を draft、updated 2026-11-05）
- snippets/followed-injected-instructions/trace-origin.txt と trace-origin.expect.yaml（操作の出どころを洗い出させる依頼。目次の templates は「なし」。分かりやすさのために足した）
- front matter で変えたキー：sections（forms・examples・prevent を足した。diagnosis は据え置き）、sources（既存の 5 件：invariantlabs-mcp-github-vulnerability・meta-ai-practical-ai-agent-security・simonwillison-lethal-trifecta・cc-docs-permission-modes・cc-docs-best-practices）、stage、updated
- data/sources.d/followed-injected-instructions.yml は作っていない（新しい出典なし）

## 必ず持つものの対応
- 冒頭の要点：冒頭の `!!! abstract`（前提は data-vs-instructions）
- 診断のチェックリスト（六つの原因を安く確かめる順。人の側の落とし穴）：`#diagnosis`（0 先に止める → 1 出どころ → 2 縛っていない → 3 境界がない → 4 経路の仕掛け → 5 人の側の落とし穴）
- 原因ごとの振り分け先（routes）：`#diagnosis` の末尾の `gen:begin routes`
- 構成の目安：よくある形 `#forms`・判断例 `#examples`・予防（仕組みに移す）`#prevent`

## メインに判断してほしいこと
- 診断の順を、2 縛っていない → 3 境界がない とした（six-causes の並びの ④ → ⑥）。site.yml の並びを確認していない
- 「実例」の GitHub MCP の事例を（根拠：中）で本文に置いた。企業の一次の報告で、事例を名指しせず「研究者が報告した」と書いた。重すぎるなら削る

## 提案
- 用語集・prh・data・front matter への提案はなし

## 検査の結果
- check_page.py：1 回目 エラー 0・警告 2（冗長な表現・助詞の重なり）、直して 2 回目 エラー 0・警告 0

## 確かめていないこと
- `/permissions` で allow ルールと動作のモードを確かめる手順は、束の記述（names の項目）に基づく。画面の細部は未確認
- 「ずれたら即 Esc」は束の Best practices の写しに基づく。アプリの停止の操作は書いていない
- API の面のタブは、束に API 固有の材料がないので、一般的な言い方にとどめた
- 雛形 trace-origin は動かしていない（動作確認なし。返答は手がかりで証拠ではない旨を本文に書いた）
- 一次資料は開いていない。Rule of Two と GitHub MCP の事例は束の写しに基づく

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
