# write.md：tasks-and-schedules-in-the-app

## 書いたファイル
- `docs/app/tasks-and-schedules-in-the-app.md`（stub から移して draft に）。front matter の変更：`sections` に 3 節を足した（what-it-prevents・compare・outdated-advice。既存の 4 節はそのまま）、`sources` に既存の id 6 つ（hc-cowork-start・hc-cowork-surfaces・hc-cowork-schedule・hc-cowork-and-chat・hc-cowork-safety・hc-release-notes）、`stage: draft`、`updated: 2026-11-05`
- 雛形 2 つ：`snippets/tasks-and-schedules-in-the-app/task-request.{md,expect.yaml}`（目次の案）、`scheduled-task-request.{md,expect.yaml}`（足した。無人で走る依頼の型。safety: true）
- `data/sources.d/` は作っていない（出典は data/sources.yml に全部ある）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力・読み込みの時期など）：要点の「成熟度」の `feature maturity` の目印（anchor なし、冒頭）。強制力は data の app-tasks に値がなく、目印を置けないため、要点の「止められるもの」と `what-it-prevents` の文で、頼み方の文は境界でなく許したフォルダ・コネクタ・権限モードが境界と書いた
- `tracks`（app-tasks）：front matter に既存。本文は冒頭の目印で参照
- level：front matter に既存（任せる。what-not-to-schedule は回す）
- 構成の目安：要点（冒頭）→ 使いどころ（what-it-prevents）→ 最小の使い方（ask-for-results・where-it-runs。面が app 1 つだけなのでタブは置かない）→ 雛形（ask-for-results・what-not-to-schedule）→ 効かない場面・落とし穴（what-it-prevents）→ 比べる相手（compare）→ 古くなった助言（outdated-advice）

## メインに判断してほしいこと
- 強制力：data の features app-tasks に `enforcement` がない。型の手引きは要点に強制力を求める。値を足すかの判断（足すなら「お願い」が近いが、権限モードやフォルダ許可は鍵に当たるので、1 値に丸めにくい）
- 面のタブ：surfaces が app だけなので省いた

## 提案
```yaml
frontmatter: []
facts: 該当なし（変わりやすい値は本文に書かず、プラン名・日付・頻度の細目は出典で確かめる書き方にした）
glossary:
  - {term: 定期タスク, note: "Scheduled tasks の訳として本文で使った。用語集にあれば表記を合わせる"}
  - {term: 信頼境界, note: "Use Claude Cowork safely の trusted boundary の訳として使った"}
```

## 検査の結果
- 1 回目：エラー 0・警告 2（助詞「が」「で」の重複）。直して 2 回目：エラー 0・警告 0

## 確かめていないこと
- クラウドのタスクが使えるコネクタ（クラウド側）の範囲。表では「ローカルのコネクタ（MCP）」の行だけを置いた
- 「接続したフォルダはクラウドのセッションから届く」は Use Claude Cowork safely の記述に基づく。Desktop が開いている間という条件の細部は未確認
- 雛形 2 つの動作（expect）は未確認
- 頻度の選択肢（毎時・毎日・毎週・平日・手動）と作り方 3 通りは hc-cowork-schedule（取得日 2026-11-05）による。承認モードの中身は記事にないため書いていない
- link の目印の表示（題名と節名）は生成後の表記を目で確かめていない

## 使用量
- 道具の呼び出し：約 14 回、Web の取得：2 回（hc-cowork-schedule・hc-cowork-safety）
