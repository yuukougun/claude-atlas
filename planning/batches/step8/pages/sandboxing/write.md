# sandboxing 執筆報告

## 書いたファイル
- docs/enforce/sandboxing.md（stub から移動。stage draft、updated 2026-11-05。front matter の変更：sections を 5 → 10 に追加〔when・minimal・templates・pitfalls・compare を足し、既存 5 つの anchor は不変〕、sources に 5 件〔既存の id〕）
- snippets/sandboxing/enable-and-block-secrets.json と .expect.yaml（kind settings、safety true）
- docs/img/sandboxing/boundary.svg（内側と外側の図）
- facts-proposal.yml（既定の 2 件。本文には数値を書いていない。既定の挙動は文で書いたので、目印にするか判断を）
- data/sources.d は作らず（出典は既存の id のみ）

## 必ず持つものの対応
- 機能の属性のバッジ：冒頭の要点の「強制力」（`gen feature enforcement`）。ほかのバッジはテンプレートが出す
- tracks（sandbox）：front matter に既存
- 使いどころ（どの原因を防ぐか）：#when
- 最小の使い方（面のタブ）：#minimal（surfaces は claude-code だけ）
- 雛形：#templates
- 効かない場面・落とし穴：#pitfalls
- 比べる相手：#compare（comparison の default-safety-settings#by-stage へ link）
- 古くなった助言：持たない。台帳の行がこの機能にない（束に outdated_advice なし）
- level：任せる（既存）

## メインに判断してほしいこと
- default-reads・fail-if-unavailable の「既定」を本文で文として書いた。facts の目印にするなら facts-proposal.yml を採用してほしい
- 目次の「検証ノート（制作の WSL2 での実測）」は未実施のため書いていない

## 提案
- front matter は変更提案なし

## 検査の結果
- 1 回目：エラー 2（prh：拒否ルール、sandbox）→ 修正。警告 5
- 2 回目（直した後）：エラー 0・警告 2。残り：(1) 冒頭の囲みの文長（122）— 囲みの項目が長い。(2) 「最小の使い方」前後の助詞「に」の重複（line 64 の段落、リンク展開後の文）。誤検出ではなく読みの好みの範囲

## 確かめていないこと
- 雛形の動作（bubblewrap・socat が入っていない環境のため。expect は未観察）。`denyRead` の `~/.ssh` などのディレクトリ指定の挙動、`permissions.deny` の `Read(~/.ssh/**)` の書き方は公式の説明の範囲で書いた
- `denyRead: ["~/"]` と `allowRead: ["."]` の公式の例は動作未確認
- macOS・IDE 拡張・ネイティブ Windows の動作
- WSL2 で seccomp のフィルタが Windows の実行ファイルの起動を止めること（調査資料の記述のみ）
- 「コンテナの中ではフックや MCP が手元と別の環境で動く」は一般的な推論で、公式の文ではない
- クラスメソッドの発表の devcontainer の運用は、調査資料の要約のみ（本文では名指しせず根拠：弱）

## 使用量
- 道具の呼び出し：約 12 回、Web の取得：1 回（code.claude.com/docs/en/sandboxing）
