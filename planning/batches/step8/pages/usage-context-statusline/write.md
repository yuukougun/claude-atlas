# write.md：usage-context-statusline

## 書いたファイル
- docs/cli/usage-context-statusline.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に 5 件〔cc-docs-statusline・cc-docs-costs・cc-docs-commands・cc-changelog・cc-docs-context-window、すべて data/sources.yml にある〕、sections に pitfalls と outdated を足した）
- snippets/usage-context-statusline/statusline.sh と .expect.yaml、statusline-settings.json と .expect.yaml
- data/sources.d は新しい出典がないので作っていない

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す。本文は {#instruments} の compare 表（成熟度・コンテキストのコスト・入った版）と {#statusline} の feature 目印（statusline/context_cost）
- tracks（usage・statusline・context-window）：front matter。{#instruments} の表が 3 機能を並べる
- 使いどころ（どの原因を防ぐか）：{#instruments} の末尾の段落（原因：合っていない）と {#when}
- 最小の使い方：{#statusline}（面は claude-code だけなのでタブは置かない）
- 雛形：{#statusline} の 2 つ（statusline-settings・statusline）
- 効かない場面・落とし穴：{#pitfalls}
- 比べる相手：comparison のページがつながるページにないので置いていない。近い道具との切り分けは {#when} で link
- 古くなった助言：{#outdated}（台帳 slash-cost-and-stats を link）
- level：front matter（整える）のまま

## メインに判断してほしいこと
- {#instruments} の compare 表で context-window の行が「— / —」になる（data にコストと since がない）。表を外すか、data に値を足すか
- 5 時間の上限の呼び方（5-hour limit）は本文に書かず「短い周期の上限」とした。呼び方を本文に出すなら名前の fact が要る

## 提案
```yaml
proposals:
  - fact: {id: statusline-json-context-used-percentage, title: ステータスラインに渡る JSON の項目（文脈の使用率）, value: context_window.used_percentage, sources: [cc-docs-statusline], checked: 2026-11-05, status: 未確認}
    used_in: [usage-context-statusline#statusline]
  - fact: {id: statusline-json-five-hour-used-percentage, title: ステータスラインに渡る JSON の項目（5-hour limit の使用率）, value: rate_limits.five_hour.used_percentage, sources: [cc-docs-statusline], checked: 2026-11-05, status: 未確認}
    used_in: [usage-context-statusline#statusline]
```
- 上の値は束（research/01 I-2、research/11 p34#171）の写しで、公式の文書を直接開いて確かめていない。雛形のスクリプトだけがこの名前を使い、本文は名前を書いていない
- 用語集：「ステータスライン」を正とし、status line を別名にする案（束の notes が用語集で確かめるとしている）

## 検査の結果
- 書き終えた後：エラー 0・警告 2。直した後：エラー 0・警告 1
- 残した警告：本文 144 行（{#when} の先頭の項目）の no-doubled-joshi。助詞「に」の連続は、道具が書く link の間（節の題名）に由来し、手では直せない

## 確かめていないこと
- 雛形（スクリプトと設定）は動かしていない。jq の有無、`rate_limits` の項目が渡る条件（プラン・最初の返答の前後）、スクリプトが無いときの動きは未確認
- 公式の statusline・costs・commands の文書は開いていない（束の写しと data による）。/usage の内訳の項目や /context の表示は、持ち主のページに任せて書いていない
- IDE 拡張・Desktop・WSL 以外の OS での表示は未確認と書いた
- 判断例は作者の想定の場面で、実測の記録ではない

## 使用量
- 道具の呼び出し 約 13 回、Web の取得 0 回
