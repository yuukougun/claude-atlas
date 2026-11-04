# write.md：check-billing-path

## 書いたファイル
- docs/cost/check-billing-path.md（stubs から mv。front matter の変更：sources に 7 件、sections に cause・misconceptions を足した、stage を draft、updated を 2026-11-05）
- snippets/check-billing-path/check-no-api-key.sh と .expect.yaml（safety: true。値を出さず、有無とファイル名だけを出す）
- data/sources.d/check-billing-path.yml（`sources: []`。使った出典はすべて data/sources.yml に既にある）

## 必ず持つものの対応
- どの原理・原因に関わるか（principle 確かめる・prevents 合っていない）：#cause（six-causes と four-principles を指して名指す）
- level（任せる）：front matter。要点の最初は「何が分かるか」
- 構成の目安（要点 → 何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：冒頭の導入と #api-key-in-env（何が起きるか）、#how-the-path-is-chosen（なぜ）、#cause（何に効くか）、#misconceptions（誤解）。関連はテンプレート
- pitfalls：空なので名指しなし

## メインに判断してほしいこと
- 節「経路が決まる順」の 2（`ANTHROPIC_AUTH_TOKEN`）と 4（`apiKeyHelper`）の課金先は、束の材料にないので「確かめていない」と書いた。一次資料で確かめるなら追記する
- 対象のプランと月の額は本文に書かず、公式の記事への link にした。数値の提案（下）が data に入ったら fact-table か fact の目印に替える

## 提案
```yaml
proposals:
  - fact: {id: api-credits-eligible-plans-and-amounts, title: プランに付く月の API credits の対象と額, value: "Max・Ultra・Team が対象（額は Max 100 ドル、Ultra 200 ドル、Team は席ごとの額の合算で月 500 ドルまで）。Free・Pro・Enterprise は対象外", sources: [hc-api-credits], checked: 2026-11-04, status: 確認済み}
    used_in: [check-billing-path#monthly-api-credits]
  - fact: {id: api-key-env-p-mode-uses-key-without-confirmation, title: ANTHROPIC_API_KEY があるとき claude -p は確認なしにその鍵を使う, value: "変数があれば必ずその鍵を使い、Console の組織に API の従量の料金がかかる。対話では最初に一度確認が出る", sources: [cc-docs-authentication, hc-claude-code-plan], checked: 2026-11-04, status: 確認済み}
    used_in: [check-billing-path#api-key-in-env]
  - fact: {id: auth-precedence-order, title: Claude Code の認証の優先順位, value: "クラウドの提供元 > ANTHROPIC_AUTH_TOKEN > ANTHROPIC_API_KEY > apiKeyHelper > CLAUDE_CODE_OAUTH_TOKEN > profile と federation > /login", sources: [cc-docs-authentication], checked: 2026-11-04, status: 確認済み}
    used_in: [check-billing-path#how-the-path-is-chosen]
```
本文の該当箇所は今は地の文（確認日は 2026-11-04 と手書き）。上の fact が入ったら目印に替える。

## 検査の結果
- check_page.py を 2 回流した。エラー 0。警告 1：105 行目の助詞「に」の重複（no-doubled-joshi）。意味が取れるので残した

## 確かめていないこと
- 優先順位・環境変数の挙動・API credits の使える範囲は、束の材料（research/26、research/22、2026-11-04 確認）に基づく。この回は Web を取得して再確認していない
- スクリプトを実際に動かしていない（雛形の expect は未実行）。VS Code の拡張など WSL・Linux の CLI 以外の面は未確認
- 表の「Agent SDK を鍵で動かす」「VS Code の拡張・GitHub Actions」の行は、束の記述（CLI を包む面に効く）に基づく

## 使用量
- 道具の呼び出し：約 16 回。Web の取得：0 回
