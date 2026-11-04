# write.md：loop-and-scheduling（執筆）

## 書いたファイル
- docs/delegate/loop-and-scheduling.md（stubs から mv。stage を draft、updated を 2026-11-05。sources に cc-docs-scheduled-tasks・cc-docs-desktop-scheduled-tasks・cc-docs-routines・cc-docs-commands を入れた。sections に templates・pitfalls・compare を足した）
- snippets/loop-and-scheduling/scheduled-prompt.md と .expect.yaml（目次の templates の案：定期タスクの依頼文）
- snippets/loop-and-scheduling/loop-watch.md と .expect.yaml（足した：/loop で見張る依頼）
- data/sources.d/loop-and-scheduling.yml は作っていない（出典はすべて data/sources.yml にあった）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力・読み込みの時期など）：テンプレートが出すバッジと、`#where-to-run` の `compare` の目印。強制力は data の loop・scheduled-tasks に値がないので、`feature` の目印は使わず、要点に「繰り返しと起動だけを担い、守らせる条件は強制しない」と一言書いた
- tracks（loop・scheduled-tasks）：front matter のとおり。本文は `#loop`（loop）と `#where-to-run`（scheduled-tasks）
- level（仕組みにする）：front matter のまま
- 構成の目安：要点（冒頭）→ 使いどころ（`#loop` 冒頭、`#where-to-run`）→ 最小の使い方（`#loop` の書き方の表、`#success-and-results`）→ 雛形（`#templates`）→ 効かない場面・落とし穴（`#pitfalls`）→ 比べる相手（`#compare`）。古くなった助言は台帳の行がなく、置かなかった
- 1機能1ページ・密接な系統は節に分ける：`#loop`・`#where-to-run`・`#success-and-results`

## メインに判断してほしいこと
- 目次の notes は、アプリのタスクと定期実行を「タブではなくリンクで送る」とあるので、面のタブは置かず、`tasks-and-schedules-in-the-app#where-it-runs` へのリンクにした。front matter の surfaces に app があるのと、Desktop scheduled tasks がアプリ（Claude Code Desktop）で動くことの整理は、メインの判断に任せる
- `compare` の目印は、tracks の 2 機能の属性をそのまま出す。scheduled-tasks はクラウドとDesktop の両方を指す項目なので、表の読み方に誤解が出ないか、生成後に見てほしい

## 提案
数値の提案（本文には数字を書かず、公式の文書で確かめるよう促した。used_in の節に目印を置ける）。出典は cc-docs-scheduled-tasks（確認 2026-11-05、WebFetch 1 回）。

```yaml
proposals:
  - fact: {id: loop-recurring-expiry-days, title: セッション内の繰り返しの失効までの日数, value: 7, sources: [cc-docs-scheduled-tasks], checked: 2026-11-05, status: 確認済み}
    used_in: [loop-and-scheduling#loop]
  - fact: {id: loop-max-tasks-per-session, title: 1 セッションに置ける予定のタスク数の上限, value: 50, sources: [cc-docs-scheduled-tasks], checked: 2026-11-05, status: 確認済み}
    used_in: [loop-and-scheduling#loop]
  - fact: {id: loop-min-interval, title: /loop の最小の間隔, value: 1 分, sources: [cc-docs-scheduled-tasks], checked: 2026-11-05, status: 確認済み}
    used_in: [loop-and-scheduling#where-to-run]
  - fact: {id: loop-self-paced-interval-range, title: 間隔を省いた /loop で Claude が選ぶ間隔の範囲, value: 1 分から 1 時間, sources: [cc-docs-scheduled-tasks], checked: 2026-11-05, status: 確認済み}
    used_in: [loop-and-scheduling#loop]
  - fact: {id: desktop-scheduled-task-min-interval, title: Desktop の予定のタスクの最小の間隔, value: Claude が設定すると 1 分、フォームでは 1 時間, sources: [cc-docs-scheduled-tasks, cc-docs-desktop-scheduled-tasks], checked: 2026-11-05, status: 確認済み}
    used_in: [loop-and-scheduling#where-to-run]
  - fact: {id: cloud-scheduled-task-min-interval, title: クラウドの予定のタスクの最小の間隔, value: 1 時間, sources: [cc-docs-scheduled-tasks], checked: 2026-11-05, status: 確認済み}
    used_in: [loop-and-scheduling#where-to-run]
```

用語集の提案：なし。front matter の提案：なし。

## 検査の結果
- 1 回目：エラー 0・警告 5（助詞の重なり）。直したあとの 2 回目：エラー 0・警告 1（`#success-and-results` 末尾の段落の助詞）。その 1 件は「にある」を「を読む」に替えて直したが、再検査はしていない（回数の決め）

## 確かめていないこと
- 雛形 2 つは動かしていない（動作の確認は別の担当）。Esc と取り消しの区別、`--resume` で戻る範囲は公式の文書（cc-docs-scheduled-tasks）の記述に基づく
- ほかの OS・IDE 拡張・アプリでの /loop の動作は未確認
- 面ごとの権限の既定（クラウドは auto モードが既定、Desktop はタスクごと、/loop はセッションを引き継ぐ）は公式の比較表を 1 回見ただけで、routines と desktop-scheduled-tasks の本文は開いていない
- 生成後の `compare` の表と link の表示は、最終の描画で見ていない

## 使用量
- 道具の呼び出し：約 15 回。Web の取得：1 回（scheduled-tasks）
