# write.md：hooks-basics（執筆）

## 書いたファイル
- docs/enforce/hooks-basics.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を 6 件、sections に 5 節を足した。既存の 3 節の anchor は変えていない）
- snippets/hooks-basics/format-after-edit.json・.expect.yaml、log-hook-input.json・.expect.yaml
- data/sources.d は作らず（使った出典はすべて既存の id）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力）：冒頭の要点の「強制力」（feature enforcement の目印）。ほかの属性はテンプレートのバッジ列
- tracks：front matter の `tracks: [hooks]`（変更なし）
- 1機能1ページ・系統は節に分ける：events（イベント）・locations（置き場所）・deterministic（ハンドラ）
- level：front matter の `level: 仕組みにする`（変更なし）
- 構成の目安：要点（冒頭）→ 使いどころ #when → 最小の使い方（面のタブ）#minimal → 雛形 #minimal（節内に 2 つ）→ 効かない場面・落とし穴 #limits（と症状の #not-running）→ 比べる相手 #compare
- 古くなった助言：持たない（台帳の行がない。束の 4 にも「なし」）

## メインに判断してほしいこと
- 図は Mermaid の流れ図 1 つ（#events）。SVG は作らなかった
- front matter の sections を、本文の順に並べ替えた（既存 3 節の相対順は同じ）。問題なら戻す

## 提案
```yaml
proposals:
  - fact: {id: hook-event-count, title: フックのイベントの数, value: 33, sources: [cc-docs-hooks], checked: 2026-11-05, status: 要確認}
    used_in: [hooks-basics#events]
  - fact: {id: hook-handler-types, title: フックのハンドラの種類（command・http・mcp_tool・prompt・agent）, value: 5, sources: [cc-docs-hooks], checked: 2026-11-05, status: 要確認}
    used_in: [hooks-basics#deterministic]
  - fact: {id: hook-monitor-min-version, title: Bash に当てたフックが Monitor のシェルにも走る最低の版, value: 2.1.314, sources: [cc-docs-changelog], checked: 2026-11-05, status: 要確認}
    used_in: [hooks-basics#limits]
  - fact: {id: hook-agent-id-min-version, title: フックの入力に agent_id が付く最低の版, value: 2.1.69, sources: [cc-docs-changelog], checked: 2026-11-05, status: 要確認}
    used_in: [hooks-basics#locations]
```
- 4 件とも値は research/28 #1・#22 と research/22 #5 の写し。本文は数字なしで読める形にしてあり、承認後に目印を足す

## 検査の結果
- check_page.py を 2 回流した。1 回目はエラー 3（prh：Hooks reference・front matter）。直して 2 回目はエラー 0・警告 4
- 警告 4 は no-doubled-joshi（「に」「で」の重なり）。文を短くすると意味が薄れるため、残した

## 確かめていないこと
- 2 つの雛形の動作（jq・prettier・ログの書き込み。`hook_event_name` と `tool_name` のフィールド名は記憶ではなく束にない。雛形は動作未確認で載せた）
- SessionStart・Notification・SessionEnd・FileChanged・PreCompact などの各イベントが起きるタイミングと用途は、束の材料（research/01・27）と一般的な理解による。個々の公式の記述は見ていない
- スキルの front matter のフックの効く範囲（動く間だけか）。表では「動く間」と書いたが、束にはサブエージェントの分しかない
- 管理の設定・クラウドのセッションの扱いは research/27 の写しによる
- Web の取得はしていない

## 使用量
- 道具の呼び出し 約 14 回（読み 6・書き 4・検査 2・補助 2）／Web の取得 0
