# write.md：when-to-start-fresh

## 書いたファイル
- docs/context/when-to-start-fresh.md（stub から移動。front matter：stage を draft、updated を 2026-11-05、sources に 4 件、sections に why・what-it-prevents・misconceptions を足した）
- snippets/when-to-start-fresh/restart-request.md と .expect.yaml（新しい会話の最初に貼る引き継ぎの依頼）
- facts-proposal.yml（数値の提案 1 件）

## 必ず持つものの対応
- 原理・原因・落とし穴の名指し：`#what-it-prevents`（見せる／散らかっている／やめられない）
- level（使う）と、要点の最初が「何が分かるか」：冒頭の囲み
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：`#why`（場面と比喩）→ `#what-it-prevents` → `#misconceptions` → 関連はテンプレート。合図の節（`#signals`）を先頭に置いた（辞典として引く用途を優先）

## メインに判断してほしいこと
- 「訂正が重ねて失敗したら /clear」の回数は、カード §7 に従い本文に書かず、`facts-proposal.yml` で数値の提案にした。本文は「回数の目安は公式を見る」。fact が入ったら `#signals` を目印に差し替えてよい
- 図は Mermaid（流れ図）。catalog の visual の案どおり

## 提案
- 数値：facts-proposal.yml の `clear-after-failed-corrections`

## 検査の結果
- 1 回目：エラー 0・警告 5。直した後：エラー 0・警告 2（残り：L86 助詞「が」の重なり、L100 読点 4 つ以上）。直した後の追加の検査は流していない。誤検出ではなく、読めるので残した

## 確かめていないこと
- 新しいチャットを始める操作の細部、アプリの記憶機能の挙動（本文で「未確認」と書いた）
- 「/clear でファイルの変更は戻らない」「CLAUDE.md は新しい会話でも読まれる」は一般的な動作で、束の資料では直接確かめていない
- `/clear 名前` の形は束の 05 1-11（Best practices の写し）による。Web は取得していない
- 雛形の動作

## 使用量
- 道具の呼び出し：約 12 回、Web の取得：0 回
