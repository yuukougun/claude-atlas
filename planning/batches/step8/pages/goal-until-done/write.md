# goal-until-done 執筆の報告

## 書いたファイル
- docs/delegate/goal-until-done.md（stub から移し、stage: draft、updated: 2026-11-05。front matter の変更は sections に 6 節を足し、sources を埋めた）
- snippets/goal-until-done/stop-condition.txt・.expect.yaml、run-unattended.sh・.expect.yaml
- data/sources.d は足していない（使った出典はすべて既存の id）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す（本文には書かない）。要点の「強制力」は鍵でない旨を文で書いた（data の note が強制力を書かないとするため）
- tracks：front matter の `tracks: [goal]`
- level：front matter の `level: 仕組みにする`
- 構成の目安：使いどころ `#when`・最小の使い方（面のタブ）`#minimal`・雛形 `#templates`・効かない場面・落とし穴 `#pitfalls`・比べる相手 `#compare`・古くなった助言 `#outdated`

## メインに判断してほしいこと
- 雛形 run-unattended は `--max-turns`・`--max-budget-usd` の効き方を手元で確かめていない（台帳の記述に基づく）。載せてよいか
- 「比べる相手」は comparison ページが束になかったので、箇条で書いた

## 提案
```yaml
frontmatter:
  - {id: goal-until-done, key: related, before: [...], after: [..., how-usage-limits-work], reason: "利用上限の節から、上限の主のページ（auto-continue・wrap-up-allowance の page）を指したい。束の指せる節にないので本文ではリンクしていない"}
proposals:
  - fact: {id: goal-condition-max-chars, title: /goal の条件の長さの上限, value: 4000, unit: 文字, sources: [cc-docs-goal], checked: 2026-11-05, status: 確認済み}
    used_in: [goal-until-done#writing-conditions]
  - fact: {id: goal-idle-checkins-max, title: /goal の席が空いている間の確認の呼びかけの回数の上限（v2.1.246 以降）, value: 3, unit: 回, sources: [cc-docs-goal], checked: 2026-11-05, status: 確認済み}
    used_in: [goal-until-done#evaluator-reads-conversation]
  - fact: {id: goal-auto-retry-max, title: /goal の自動の再試行の回数（過負荷・切断。超えると一時停止。v2.1.269 以降）, value: 3, unit: 回, sources: [cc-docs-goal], checked: 2026-11-05, status: 確認済み}
    used_in: [goal-until-done#at-usage-limits]
  - fact: {id: goal-checkin-minutes, title: 背景の作業を待つときの最初の確認の間隔（CLAUDE_CODE_GOAL_CHECKIN_MINUTES で変更）, value: 30, unit: 分, sources: [cc-docs-goal], checked: 2026-11-05, status: 確認済み}
    used_in: [goal-until-done#evaluator-reads-conversation]
  - fact: {id: auto-continue-max, title: 利用上限での自動の継続の回数の上限（/goal も同じ）, value: 3, unit: 回, sources: [cc-docs-interactive-mode, cc-changelog], checked: 2026-11-05, status: 確認済み}
    used_in: [goal-until-done#at-usage-limits]
```
本文は上の数値を書かない形にしてあり、目印を置く場所は used_in のとおり（目印は提案が通ってから足す）。

## 検査の結果
- 1 回目：エラー 1（存在しない name 目印）・警告 15。2 回目（直した後）：エラー 0・警告 9
- 残した警告：no-doubled-joshi 7 と sentence-length 2。うち 72・155・246 行は道具が生成したリンクの題名を含む行（誤検出に近い）。ほかは文を短くすれば消せる軽いもの

## 確かめていないこと
- 公式の goal の文書は 1 回だけ読んだ（2026-11-05）。入った版・数値は data と調査資料に頼った
- run-unattended の外枠の旗の名前と、条件の上限と外枠のどちらが先に効くか（推論）
- 「会話が長くなる」「外のループは毎回新しい会話」の対比は一般的な理解で、公式の記述ではない
- ISUCON の事例は Azure SRE エージェントのもので、`/goal` への当てはめは類推と書いた
- 判定のモデルを変える環境変数の副作用は公式の警告に基づく（試していない）
- Windows・macOS・IDE 拡張の動作は未確認と書いた
- 雛形は動かしていない。textlint が見ない囲み内の字下げ段落は自分で読んだ

## 使用量
- 道具の呼び出し：約 20 回。Web の取得：1 回（code.claude.com/docs/en/goal）
- 雛形は Write でなく Bash のヒアドキュメントで置いた
