# write.md：checkpoints-and-rewind

## 書いたファイル
- docs/cli/checkpoints-and-rewind.md（stub から mv。front matter：sections に use-cases・how-to・compare を足した／stage draft／updated 2026-11-05／sources に cc-docs-checkpointing・cc-docs-best-practices・cc-docs-commands）
- snippets/checkpoints-and-rewind/try-then-rewind.md と .expect.yaml
- docs/img/checkpoints-and-rewind/restorable.svg（戻せる・戻せないの図。実線と点線で区別）
- data/sources.d は新しい出典がないので作っていない
- facts-proposal.yml（保持の数・期間と summary の直しの提案）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが tracks（checkpoints）から出す。本文は要点の「強制力」に手書きで「なし（戻す手段）」と書いた。data の checkpoints に enforcement がないため目印は使っていない
- tracks：front matter の tracks: [checkpoints]
- 1機能1ページ・節の分け方：#use-cases #how-to #what-is-restored #summarize #with-git #compare
- level：front matter（整える）
- 構成の目安：要点→#use-cases（防ぐ原因）→#how-to→雛形（#use-cases 内）→#what-is-restored（落とし穴）→#compare。古くなった助言は台帳の行がないので置かない

## メインに判断してほしいこと
- 公式は、Claude が先にファイル編集の道具で触ったファイルへの、その後の Bash の変更は戻ると書く。summary の「Bash で変えたファイル…は戻らない」は不正確なので、直す案を facts-proposal.yml に書いた。目次の「Bash での変更は戻らない」も同様
- 「強制力」を目印にせず手書きにした件（data の checkpoints に enforcement を足すか、手書きのままでよいか）

## 提案
- 数値：facts-proposal.yml の 2 件（100 件・約 30 日）。本文は数字なしで読める形にしてあり、used_in の節に目印を置く
- front matter：summary の直し（同ファイル）

## 検査の結果
- 1回目：エラー 0・警告 5。直した後の 2回目：エラー 0・警告 2（図の代替テキストの文長、終了すると戻る会話の「が」）。そのあと 2 件を直したが、検査は規定の 2 回なので再実行していない

## 確かめていないこと
- 直した後の 2 件の警告が消えたか（未実行）
- 動作は試していない（公式の文書 Checkpointing による）。IDE 拡張の checkpoints は動作未確認と本文に書いた
- 雛形の expect は、実際に Claude が指示どおりシェルを使わないかを観察していない

## 使用量
- 道具の呼び出し 約 20 回、Web の取得 1 回（cc-docs-checkpointing）
