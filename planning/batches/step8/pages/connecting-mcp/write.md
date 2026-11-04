# write.md：connecting-mcp（執筆）

## 書いたファイル
- docs/extend/connecting-mcp.md（stub から移動。stage を draft、updated を 2026-11-05、sources を 6 件、sections を 4 から 9 に増やした。既存の 4 つの anchor は変えていない）
- snippets/connecting-mcp/team-mcp.json・team-mcp.expect.yaml、readonly-db.json・readonly-db.expect.yaml
- docs/img/connecting-mcp/scopes.svg（スコープの図）
- facts-proposal.yml（このフォルダ）
- data/sources.d/connecting-mcp.yml は作っていない（使った出典は全て data/sources.yml にある）

## 必ず持つものの対応
- 機能の属性のバッジ：冒頭の要点（成熟度・読み込みの時期は `feature` の目印）と、{#minimal} のコンテキストのコスト（`feature context_cost`）
- 強制力：data の mcp に enforcement の属性がないため、目印を使わず、要点に文で書いた（「何も止めない。止めるのは権限・管理設定の側」）。下の判断の 1 を参照
- tracks：front matter の `tracks: [mcp]`（変更なし）
- 使いどころ（防ぐ原因）：{#use}
- 最小の使い方（面のタブ）：{#minimal}（アプリ・Claude Code のタブ）、{#desktop} にもタブ
- 雛形：{#scopes}（team-mcp）・{#credentials}（readonly-db）
- 効かない場面・落とし穴：{#limits}
- 比べる相手：{#compare}（mcp-or-cli ほか）
- 古くなった助言：{#outdated}（台帳 mcp-sse-transport を link）
- level：任せる（変更なし）

## メインに判断してほしいこと
1. 型の手引きは要点に強制力の属性を求めるが、mcp の項目に enforcement がない。値を足すなら「お願い」でも「鍵」でもなく、どう分類するかの決めが要る。足りなければこのままでよい
2. 目次の「図の案（static）」に沿って SVG を 1 枚付けた（スコープ 3 種の表と重なる内容）。不要なら外してよい

## 提案
- 数値の提案：facts-proposal.yml（MCP の出力の警告と上限。調査資料 01 G-1 の値で、一次資料では今回確かめていない。status は要確認とした。本文は数字なしで読める）
- 用語集・prh・front matter の提案はなし

## 検査の結果
- 書き終えた後：エラー 0・警告 10。直した後：エラー 0・警告 4
- 残した警告 4 件はすべて助詞「が・に」の重複（no-doubled-joshi）で、誤検出に近い。意味が通る形のため残した

## 確かめていないこと
- 一次資料は公式の MCP の文書の 1 回の取得（先頭 100000 字まで。残りの約 55000 字は未読）で確かめた。スコープ・優先順・`${VAR}` の展開・承認・`-p` の扱い・オプションの順序・SSE の扱いはこれによる
- `/mcp reconnect all` の対応する版、承認待ちの表示の細部は、版を書かずに「公式で確かめる」とした
- 権限ルールの書き方（mcp__ の形）、MCP の出力の警告と上限の値、Desktop の記述（調査資料 26 の写しのまま）、tool search が働かない環境は、今回の取得では確かめていない
- 雛形 2 件は動かしていない。readonly-db の `@bytebase/dbhub` は公式の文書の例で、パッケージの現状は未確認
- Windows のネイティブと IDE 拡張の動きは未確認と本文に書いた

## 使用量
- 道具の呼び出し：約 12 回（Read 2、Bash 6、Write 2〜、WebFetch 1、ToolSearch 1）。Web の取得：1 回
