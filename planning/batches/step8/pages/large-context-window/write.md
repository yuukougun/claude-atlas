# write.md：large-context-window（執筆）

## 書いたファイル
- docs/models/large-context-window.md（stubs から mv。stage を draft、updated を 2026-11-05、sections に effects・misconceptions を足した、sources に cc-docs-best-practices・cc-docs-context-window・api-docs-context-windows を入れた）
- 雛形・図・data/sources.d は作っていない（目次の templates と visual が「なし」）

## 必ず持つものの対応
- 原理・原因（principle 見せる／prevents 散らかっている）を名指して結ぶ：#effects
- level 整える・要点の最初は「何が分かるか」：冒頭の要点の囲み
- 何が起きるか（具体的な場面）：#what-to-stop（古い決まりの見直し）と #what-to-keep（判断例）
- なぜそうなるか：#cost-of-long-context と #effects（理由は attention-budget#effects へ link。図は置かなかった）
- 誤解：#misconceptions
- 関連：テンプレートが出す
- pitfalls は空なので名指しなし

## メインに判断してほしいこと
- 窓の大きさ・長い入力の単価・トークナイザーの差は数値の目印を使わず、current-models へ link して本文から外した（束に facts の id がなかったため）。目印にしたければ facts への追加が要る
- outdated-advice-ledger#save-context-for-200k と #subagents-to-save-context の link を置いた（束の指せる節の一覧にない。check_page は通った）
- 図は置かなかった（比喩は文章で広い机と送り直す受験者を使った）

## 提案
- なし

## 検査の結果
- check_page.py を 2 回流した。最後はエラー 0・警告 2（no-doubled-joshi：48 行目の「に」と 83 行目の「に」）。48 行目は「…今も守っていないか見直したい」を含む文、83 行目は link の題名（「新しい会話を始めるタイミング › …」）が入った文で、題名を道具が書くため直しにくい。誤検出に近いので残した

## 確かめていないこと
- 事実は束の写しに基づく。一次資料は開いていない（Web の取得 0）
- API 欄の「圧縮の機能が別にある」は data の compaction の note にある api-compaction の記述に基づき、公式の Context windows は読んでいない
- アプリの自動の要約（code execution 有効時）は調査資料 02 の確認日 2026-10-29 の記述で、現行の公式で再確認していない
- Claude Code 以外の OS・IDE の動作は未確認と書いた

## 使用量
- 道具の呼び出し 9 回（Read 3、Bash 4、Write 2）、Web の取得 0
