# write.md：cloud-schedules（クラウドの定期タスク）

## 書いたファイル

- `docs/delegate/cloud-schedules.md`（stubs から移した。stage を draft に、updated を 2026-11-05 に、sources を 6 件に、sections を 7 節に）
- `snippets/cloud-schedules/pr-review-task.md`・`.expect.yaml`、`alert-fire-task.md`・`.expect.yaml`
- `data/sources.d/cloud-schedules.yml`（`sources: []`。使った出典は既存の id だけ）
- front matter で変えたキー：`sections`（triggers・least-privilege に 5 節を足した）・`stage`・`updated`・`sources`（cc-docs-routines・cc-docs-scheduled-tasks・cc-docs-feature-availability・cc-docs-claude-code-on-the-web・cc-docs-commands・cc-changelog）

## 必ず持つものの対応

- 冒頭の要点（強制力）：冒頭の囲み「強制力」の項目。値は手書き（下の「メインに判断してほしいこと」1）
- 機能の属性のバッジ：テンプレートが出す（本文に書かない）。成熟度は `#top` の導入で feature の目印を使った
- `tracks`：front matter の `tracks: [scheduled-tasks, cloud-sessions]`。表は `#compare`
- 構成の目安：使いどころ（どの原因を防ぐか）＝`#triggers`・`#least-privilege`（縛る・境界がない）と `#success-and-results`（確かめる・確かめていない）／最小の使い方＝`#triggers`（`/schedule`。面は claude-code の 1 つだけなのでタブは置かない）／雛形＝`#templates`／効かない場面・落とし穴＝`#pitfalls`／比べる相手＝`#compare`／古くなった助言＝`#outdated`
- level：front matter の `level: 回す`

## メインに判断してほしいこと

1. 強制力：data の features の scheduled-tasks に enforcement 属性がない。冒頭は手書きで「起動を担うだけ。依頼文の指示はお願い、止められるのは権限の側（保護ルール・ネットワーク・連携先）」とした。属性を足すなら値は「お願い」（依頼文）と「鍵」（保護ルール・環境）の混在で、1 つに決めにくい
2. 3 節以外（success-and-results・templates・pitfalls・compare・outdated）を sections に足した。anchor は既存の 2 つを変えていない
3. `#compare` の `compare` の目印は、scheduled-tasks と cloud-sessions の属性の表になる。比較として弱ければ外してよい

## 提案

```yaml
proposals:
  - fact: {id: scheduled-tasks-min-interval, title: クラウドの定期タスクの最小の間隔（cron の 1 時間より短い間隔は拒否）, value: 1 時間, sources: [cc-docs-routines], checked: 2026-11-05, status: 確認済み}
    used_in: [cloud-schedules#triggers]
  - fact: {id: scheduled-tasks-hourly-cap, title: 定期タスクの実行・GitHub イベントの 1 時間あたりの上限（タスクごと・アカウントごと）, value: 公式の usage and limits の節で確認が要る（値は未取得）, sources: [cc-docs-routines], checked: 2026-11-05, status: 要確認}
    used_in: [cloud-schedules#triggers, cloud-schedules#pitfalls]
  - fact: {id: scheduled-tasks-github-lapse, title: GitHub の接続が切れたとき実行を飛ばす期間と、その後に止まるまでの期間, value: 72 時間, sources: [cc-docs-routines], checked: 2026-11-05, status: 確認済み}
    used_in: [cloud-schedules#pitfalls]
  - fact: {id: scheduled-tasks-schedule-warning-version, title: /schedule が頼んでいない連携先に警告を出すようになった版, value: 2.1.317, sources: [cc-changelog], checked: 2026-11-04, status: 確認済み（research/22 #27）}
    used_in: [cloud-schedules#least-privilege]
  - fact: {id: scheduled-tasks-run-history-question-version, title: /schedule で実行の履歴を尋ねられる版（GitHub の起動を CLI から足せる版は 2.1.225）, value: 2.1.227, sources: [cc-docs-routines], checked: 2026-11-05, status: 確認済み}
    used_in: [cloud-schedules#success-and-results]
  - fact: {id: scheduled-tasks-plans, title: クラウドの定期タスクが使えるプラン, value: Pro・Max・Ultra・Team・Enterprise, sources: [cc-docs-routines], checked: 2026-11-05, status: 確認済み}
    used_in: [cloud-schedules#triggers]
frontmatter: []
```

数値は本文に書いていない（すべて「公式で確かめる」の形）。上の提案が通れば、目印に置き換えられる。

## 検査の結果

- 2 回流した。最後は エラー 0・警告 5（すべて textlint の no-doubled-joshi。1 文が長く「か」「が」「で」「に」が重なる箇所：64・84・86・103・179 行）
- 警告は残した。1 回目の 7 件から 2 件を直し、検査の回数の上限のため再度は流していない。文を短く分ければ消える

## 確かめていないこと

- 公式の routines の文書（1 回の取得）と束の材料だけに基づく。雛形 2 件の動作は確かめていない（expect の条件と観察を書いた）
- 手元の CLI 以外（Desktop の Code タブ）での作り方、WSL 以外の OS は未確認
- 公式の文書の usage and limits の節は読んでいない。上限・間隔の数値は提案に「未取得」と書いた
- 「/schedule で頼んでいない連携先が付くと警告が出る」は research/22 の写し（版 v2.1.317）で、公式の文書では見ていない
- 冒頭の「強制力」の言い方は、作者の方針に関わる断定ではないが、data にない値の手書きである

## 使用量

- 道具の呼び出し 約 22 回（Read 4、Bash 8、Write 6、Edit 6、検査 2 を含む）、Web の取得 1 回（code.claude.com/docs/en/routines）
