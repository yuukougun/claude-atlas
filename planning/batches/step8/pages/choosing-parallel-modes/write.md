# write.md：choosing-parallel-modes

## 書いたファイル
- docs/delegate/choosing-parallel-modes.md（stubs から mv。stage: draft、updated: 2026-11-05）
- snippets/choosing-parallel-modes/ask-for-mode-choice.md と .expect.yaml（目次の templates は「なし」。選択肢と推奨案を出させる依頼の型を足した）
- front matter で変えたキー：sources（既存 id 12 件）、sections（compare・combine・how-to-check を足した。既存 3 つの anchor は不変）、stage、updated
- data/sources.d/choosing-parallel-modes.yml は作っていない（使った出典がすべて data/sources.yml にあった）

## 必ず持つものの対応
- 比較の表（compare の目印）：#compare
- 判断例：#who-coordinates（調査 3 件を手元の実装と並べる）・#same-files（同じモジュールを触る 2 案）
- 構成の目安（要点 → 表 → 選び方 → 組み合わせ方）：#compare → #who-coordinates・#same-files・#expect-to-discard → #combine
- 確かめ方の節（共通の手引き §6）：#how-to-check
- level：front matter の「仕組みにする」のまま
- 古くなった助言（台帳 2 行）：#who-coordinates で link

## メインに判断してほしいこと
- 「1〜2 割は捨てる」を自己申告・根拠：弱で #expect-to-discard に置いた。個人の構成として標準にはしていない。実在の人物の名は出していない。この扱いでよいか
- 「3〜4 本ほど」の上限の声も経験則として置いた。数値の目印にすべきか

## 提案
```yaml
frontmatter: []
facts: []
```
- 用語集・prh への提案はなし。prh は subagents → サブエージェント、agent teams → エージェントチームを要求するので本文はそれに従った。agent view と workflows は原文のまま

## 検査の結果
- 1 回目：エラー 13（すべて prh の表記）・警告 3。直して 2 回目：エラー 0・警告 1
- 残した警告 1：#expect-to-discard の「助詞 と が二回」。「〜と語ったと報じられている」の引用の形で、言い換えると意味が曖昧になるので残した

## 確かめていないこと
- 公式の agents 文書は開いていない。表の「調整する者」「向く作業」と「`claude agents`・`/tasks`・`/workflows`」は、束の材料（research/01 E-2、確認日 2026-10-29）と、つながるページの要約による
- Projects の「向く作業」は束の data の説明からの言い換えで、公式の説明そのままではない
- 「触らない作業は worktree を分けない」は準備の手間からの推論で、公式の文言ではない
- 雛形は動作を確かめていない

## 使用量
- 道具の呼び出し：約 12 回（Read 4、Write 3、Bash 5。check_page 2 回）。Web の取得：0
