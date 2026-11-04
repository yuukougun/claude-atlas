# write.md：choose-what-to-read

## 書いたファイル
- docs/context/choose-what-to-read.md（stubs から mv。stage: draft、updated: 2026-11-05、sources に cc-docs-common-workflows・cc-docs-large-codebases・cc-docs-interactive-mode・cc-docs-context-window・anthropic-eng-building-c-compiler を追加、sections に effects を追加）
- snippets/choose-what-to-read/point-with-at.{md,expect.yaml}・trim-test-output.{md,expect.yaml}
- facts-proposal.yml

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle 見せる／prevents 見えていない・散らかっている）：effects
- pitfalls：空のため名指しなし（front matter が空）
- level 整える：front matter。要点の最初は「何が分かるか」：冒頭
- 構成（技法）：Before/After は point-or-search、何が変わる・なぜ効く は effects、効かない場面・やりすぎは caveats

## メインに判断してほしいこと
- アプリでの扱い（添付など）は束に材料がなく「未確認」と書いた。調べる担当が要るか。

## 提案
- 数値：facts-proposal.yml（@ で全文が入る上限。本文は数字なしで、目印を置く場所は caveats）。
- 前提・related の front matter は変更なし。

## 検査の結果
- 1 回目：エラー 3（hook の表記）・警告 2。直した後：エラー 0・警告 1（no-doubled-joshi「に」、caveats の 1 文。直し回数の上限のため残した）

## 確かめていないこと
- @ の挙動（ディレクトリは一覧、MCP リソース）は束の写しに基づく。一次資料を開いていない
- 「出力は会話に残り毎ターン読み直される」「Large codebases の記述」は調査資料の写しによる。cc-docs-context-window の本文は未確認
- 実務家の一致（根拠：中）と C コンパイラの事例は p34#123 の写しによる
- 雛形の動作は未確認

## 使用量
- 道具の呼び出し 約 10 回、Web の取得 0
