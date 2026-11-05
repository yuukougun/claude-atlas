# write.md：artifacts-as-apps（執筆）

## 書いたファイル
- docs/app/artifacts-as-apps.md（stubs から移動。stage draft、updated 2026-11-05）
- snippets/artifacts-as-apps/request-data-tool.txt・request-data-tool.expect.yaml（目次の templates の案 1 つ）
- front matter で変えたキー：`sections`（when・pitfalls・compare を足した。runtime・whose-account は変えず、when を先頭にした）、`sources`（[hc-artifacts]）、`stage`、`updated`
- data/sources.d/artifacts-as-apps.yml は作らない（hc-artifacts は既存。新しい出典なし）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力など）：冒頭の要点の「強制力」（`feature artifacts/enforcement` の目印）。そのほかの属性は冒頭のテンプレートが出す
- `tracks`：front matter の `tracks: [artifacts]`（束のとおり、変更なし）
- level：front matter の `level: 仕組みにする`
- 構成の目安：使いどころ `#when` → 最小の使い方 `#runtime`（対象の面がアプリだけなのでタブは置かない）→ 雛形 `#runtime` 内の snippet → 効かない場面・落とし穴 `#pitfalls` → 比べる相手 `#compare` → 古くなった助言：台帳の行がないので置かない
- 1機能1ページ・節に分ける：`#runtime`・`#whose-account` の 2 系統を節で分けた

## メインに判断してほしいこと
- 面のタブを置いていない（surfaces が app のみ。Claude Code と API は「未確認」と `#pitfalls` に書いた）
- 「Claude を呼ぶ処理は答えが 1 通りに決まらない部分だけに使う」は設計上の推論として `（推論・実践例なし）` を付けた

## 提案
facts-proposal.yml に数値の提案（保存の上限・使えるプラン）を書いた。本文には数値もプラン名も書いていない。目印を置く場所は `artifacts-as-apps#runtime`。

## 検査の結果
- 1 回目：エラー 0・警告 6。直した後の 2 回目：エラー 0・警告 3
- 残した警告 3 件（no-doubled-joshi）：69 行目はリンクの生成される題名に含まれる助詞に重なる。139・141 行目は直さず残した。いずれも文の意味は崩れていない

## 確かめていないこと
- 雛形の動作（実行していない）
- 公式の記事は Web で 1 回取得して確認した（2026-11-05）。legacy の公開と保存データの扱い、組織の管理者が接続を無効にできる点、承認が毎回要る接続の道具が使えない点は、その 1 回の取得の要約による。原文の一字ずつの照合はしていない
- 保存の上限・使えるプランの現在の値（facts に未登録）
- Claude Code・API・モバイルでの同じ動き

## 使用量
道具の呼び出し 12 回前後、Web の取得 1 回
