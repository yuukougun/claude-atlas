# write.md：permission-modes-overview

## 書いたファイル
- docs/cli/permission-modes-overview.md（stub から移して draft。front matter は sections に switch・templates・limits・compare・outdated を足し、sources と updated を入れた。ほかは変えていない）
- snippets/permission-modes-overview/start-in-manual.json と .expect.yaml
- planning/batches/step8/pages/permission-modes-overview/facts-proposal.yml

## 必ず持つものの対応
- 機能の属性のバッジ（強制力）：要点の「強制力」の行（feature enforcement の目印）。ほかの属性はテンプレートが出す
- tracks（permission-modes・auto-mode）：front matter のまま。本文は modes・defaults が持つ
- 要点→使いどころ：#modes（守りを先に置く箇条を含む）
- 最小の使い方（面のタブ）：#switch（Claude Code のタブ。surfaces は claude-code だけ）
- 雛形：#templates（start-in-manual）
- 効かない場面・落とし穴：#limits
- 比べる相手：#compare（comparison のページは未確認のため、表で関連ページを指した）
- 古くなった助言：#outdated（台帳の 2 行を link で指した）
- level（整える）：front matter のまま

## メインに判断してほしいこと
- 既定の開始モード（対話は auto、-p は Manual）の値は、目印がないため本文に手で書かず、台帳の行を指した。facts-proposal.yml の 2 件を採用するなら、#defaults に fact の目印を置く
- 緩める側の雛形（acceptEdits や auto の settings）は、守りを先に置く方針で載せなかった

## 提案
- planning/batches/step8/pages/permission-modes-overview/facts-proposal.yml（既定の開始モード 2 件）

## 検査の結果
- 1 回目：エラー 1（auto mode の表記）・警告 4。2 回目：エラー 0・警告 1（助詞の連続）。その警告は直したが、直した後の再実行はしていない

## 確かめていないこと
- 雛形の動作、Shift+Tab で回るモードの順（版と設定で変わるため書かなかった）、acceptEdits の対象コマンド（research/01 C-1 の写しによる）、VS Code の設定名（research/26 による。動作は未確認）
- ledger の anchor（approve-everything-first・yolo-skip-permissions）が docs/changes/outdated-advice-ledger.md にあることは見た

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
