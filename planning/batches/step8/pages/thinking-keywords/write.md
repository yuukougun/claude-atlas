# write.md：thinking-keywords

## 書いたファイル
- docs/models/thinking-keywords.md（stub から移動。stage を draft、updated を 2026-11-05、sources を [cc-docs-model-config, cc-changelog, cc-docs-best-practices, hc-effort-settings] に。sections に pitfalls・compare を追加し、既存 3 つの anchor は不変）
- snippets/thinking-keywords/ultrathink-one-turn.md と .expect.yaml（prompt）、find-old-keywords.sh と .expect.yaml（other）
- planning/batches/step8/pages/thinking-keywords/facts-proposal.yml
- data/sources.d/thinking-keywords.yml は書いていない（新しい出典がないため）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力・成熟度など）：冒頭の「要点」（成熟度・強制力は feature の目印。入った版・面は #compare の compare 表）
- tracks（ultrathink・effort）：front matter に既にある。#compare の表が両方を並べる
- 1 機能 1 ページ・密接な系統は節に分ける：#plain-text-phrases・#ultrathink・#history
- level：front matter（整える）
- 構成の目安：使いどころ #ultrathink／最小の使い方（面のタブ）#ultrathink／雛形 #ultrathink・#history／効かない場面 #pitfalls／比べる相手 #compare／古くなった助言（台帳 think-hard-keywords への link と今どうするか）#history

## メインに判断してほしいこと
- ultrathink の機能の項目の `enforcement` が null で、冒頭の強制力が「—」と出る。「お願い」にする提案（下）を反映するか判断してほしい。

## 提案
- data/facts.yml の features の ultrathink に `enforcement: お願い`（プロンプトに指示を足す働きで、何も止めない）を足す
- 版・引き上げる先・対象モデルの数値は facts-proposal.yml。本文は数字なしで読めるようにしてあり、fact の目印は置いていない（反映後に #ultrathink へ置く）
- 台帳の行 think-hard-keywords への link は `outdated-advice-ledger#think-hard-keywords`。台帳の sections にこの anchor があるかは、check_page では通ったが、持つ anchor の一覧では確かめていない

## 検査の結果
- 1 回目：エラー 0・警告 5（block の目印を文の中に置いていた。1 行ずつに直した）。2 回目：エラー 0・警告 0

## 確かめていないこと
- アプリでの ultrathink の扱い（「未確認」と書いた）
- ultrathink が引き上げる条件の細部（束の調査資料の写しに基づく。一次資料は開いていない）
- 段階のキーワードが外れた時期、どの語がどの段に当たったか（束にも確認なしと書かれている）
- スニペットの動作（実機で試していない）

## 使用量
- 道具の呼び出し 11 回前後、Web の取得 0 回
