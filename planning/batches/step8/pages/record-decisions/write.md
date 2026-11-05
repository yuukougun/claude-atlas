# write.md：record-decisions（recipe・team）

## 書いたファイル
- docs/team/record-decisions.md（stubs から mv。stage を draft、updated を 2026-11-05、sections を 5 節追加）
- snippets/record-decisions/ に 3 雛形：adr-template・weekly-update・claude-md-pointer（各 .md と .expect.yaml）
- data/sources.d/record-decisions.yml は作っていない（sources は空のまま。下の「メインに判断してほしいこと」）

## 必ず持つものの対応
- 要点（冒頭）：冒頭の abstract
- 手順：steps（各段に「確かめ」付き）
- 確かめる・縛るページへの道：front matter の prerequisites（handoff-documents）と related。本文は guards（separate-roles#against-sycophancy・what-to-put-in-claude-md#what-to-leave-out）、when-it-fails（keep-failure-lessons・postmortems・experiment-log・separate-roles ほか）
- level：任せる（front matter のまま）
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：guards → steps → template → check → when-it-fails

## メインに判断してほしいこと
- sources が空。束に出典がなく、材料は調査資料 11 の「根拠：中」の 2 行だけ。ADR の由来や公式の説明には触れず、手順は「この辞典の推奨」の形で書いた。確認の節の基準には（根拠：弱）を付けた。出典を足すなら別途一次資料が要る
- 内容が approx 「新メンバー役が CLAUDE.md と ADR だけで作業できるか」を確かめの基準にした（材料 6.2 に沿う）。調査資料側の「根拠：中」を弱にしたのは、出典が束になく確認できないため
- 面のタブ（アプリ／Claude Code）は置かなかった。手段が面で分かれる所がなく、アプリ側の動作は確認できないため

## 提案
- なし（用語集・prh・data への提案なし）

## 検査の結果
- 1 回目：エラー 0・警告 4（no-doubled-joshi）。2 回目：エラー 0・警告 2
- 残した警告：36 行目の要点の「何ができるか」は summary と同じ文で、食い違わせない規則のため直していない。50 行目（"からも"）は直した後の検査の回数が尽きて未確認の直し

## 確かめていないこと
- 3 つの雛形の動作（expect は未確認）。CLAUDE.md の指す先が Claude に守られるかは観察で、確実ではない
- 判断例と確かめ方の Claude への頼み方は、実際に流していない
- 事実の外部確認（Web の取得は 0 回）

## 使用量
- 道具の呼び出し：約 12 回、Web の取得 0 回
