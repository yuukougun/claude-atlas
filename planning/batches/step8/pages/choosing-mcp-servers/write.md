# write.md：choosing-mcp-servers（feature・extend）

## 書いたファイル
- docs/extend/choosing-mcp-servers.md（stage: draft、updated: 2026-11-05。front matter の直し：`sections` に 10 節、`sources` に 6 件、`stage`、`updated`）
- snippets/choosing-mcp-servers/vet-candidate.md と vet-candidate.expect.yaml（入れる前に見極めさせる依頼。目次の templates は「なし」だが、4 つの問いを使える形にするため足した）
- data/sources.d/choosing-mcp-servers.yml は触っていない（新しい出典なし。`sources` は data/sources.yml の既存の id だけ）
- stub は前の作業で docs へ移ってあった（stubs/ に残りなし）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力・読み込みの時期など）：冒頭の要点の「強制力」の項目（`feature enforcement`・`maturity`・`load_timing` の目印）。コンテキストのコストは `#cost`（`feature context_cost`）
- `tracks`：front matter に `tracks: [mcp]`（stub のまま）
- level：front matter に `level: 任せる`
- 1機能1ページ・公式の網羅をしない：`#questions` が基準の骨格。設定キーやコマンドの網羅は置いていない
- 構成の目安（使いどころ）：`#questions`・`#gap`（どの原因を防ぐかは `#questions` で「見えていない」「境界がない」を名指し）
- 最小の使い方：`#keep-small`（surfaces が claude-code のみなので、タブは置かない）
- 雛形：`#keep-small` の vet-candidate
- 効かない場面・落とし穴：`#limits`
- 比べる相手：`#compare`
- 古くなった助言：持たない（束に台帳の行がなく、`outdated_advice` なし）

## メインに判断してほしいこと
- 第三者サーバーの名前の表（`#examples`）：成熟度は「未確認」、確認日は出典の記事の日付（2026-06-29）と本文に書いた。DR-17 は「成熟度と確認日を添える」とあるが、各サーバーを確かめていないため。名前の表を残すか、確かめる担当を付けるかを決めてほしい
- ページの題材が第三者の名前を出す（推薦ではない旨を本文に明記）。公開の約束や方針の文は置いていない

## 提案
- front matter、用語集、data への提案はない

## 検査の結果
- 1 回目：エラー 0・警告 9。直した後の 2 回目：エラー 0・警告 4
- 残した警告：sentence-length 2 件（88 行と 128 行。出典の記事題名のリンクと、link の目印が生成する長い題名が文字数に入るため）。no-doubled-joshi 2 件（94 行の「に」と 119 行の「が」。生成された link の題名の助詞を数えたもので、本文側の直しで消えなかった）

## 確かめていないこと
- 例の表の各サーバーの存在・提供元・成熟度（記事の一覧の写しのみ。Web の取得なし）
- Tool Search で消費がどこまで減るかは、束の通り未確認
- Claude Code の WSL・Linux 以外の OS と IDE 拡張の動作
- 雛形の動作（実際に Claude に出して、表が返るか）

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
