# consistent-politeness 執筆の報告

## 書いたファイル

- docs/japanese/consistent-politeness.md（stubs から mv。stage を draft、updated を 2026-11-05。sections に guards・failure を足した。sources に 7 件〔cc-docs-memory・cc-docs-output-styles・hc-personalization・hc-skills-what・hc-styles-to-skills・zenn-yuki-a01e472d・jinrai-claude-japanese〕を足した）
- snippets/consistent-politeness/style-instruction.md と .expect.yaml（目次の templates の案。claude-md）
- snippets/consistent-politeness/count-endings.md と .expect.yaml（足した雛形。文末を数えさせる依頼。prompt）
- data/sources.d/consistent-politeness.yml は作っていない（出典は既存の id だけ）

## 必ず持つものの対応

- 冒頭の要点：冒頭の囲み（要点・前提）
- 手順：#specify（1 段目）→ #example（2 段目）→ #where（3 段目）→ #lint（4 段目）。各段の終わりに「確かめ」を置いた
- 先に整える守り（確かめる・縛る）：#guards（お願いの層と仕組みの層の分け方、lint に任せる範囲）
- 確かめ方（全体）：#check
- 失敗したとき（症状ページへ振り分け）：#failure
- 確かめる・縛るのページへの道：本文の link で textlint-hook（#guards・#lint・#failure）・measure-changes（#check）・align-japanese-output（#guards・#lint）。front matter の related にも textlint-hook・measure-changes がある
- level：整える（front matter にあり）

## メインに判断してほしいこと

- なし（公開の約束・方針の文は入れていない）

## 提案

- 用語集・prh・data への提案はなし
- 数値の提案はなし（変わりやすい値は本文に書いていない）

## 検査の結果

- check_page.py：1 回目 エラー 0・警告 6（長い文・助詞の重複）→ 直して 2 回目 エラー 0・警告 0

## 確かめていないこと

- 雛形 2 つの動作（文体が実際に揃うか、grep で数える依頼が期待どおり動くか）は試していない
- 「理由を添えると境目で判断しやすい」「手本の文体が指定と違うと引かれる」「Claude に目で数えさせると間違う」は推論で、本文に（推論・実践例なし）か「この辞典の推奨」と書いた
- 根拠：弱の 3 か所（です・ます調を明示しないと揺れる、部位で文体を分ける設定、textlint のフック連携）は束の写し（04 Q3）だけに基づく。原典の記事は開いていない
- Styles の移行後にメニューが残るかは未確認（本文は台帳へ指すだけで断定していない）
- 出力スタイルが書かせるファイルの文体にどこまで効くかは、束にない。「ファイルの規約は CLAUDE.md、応答の調子は出力スタイル」は output-style-modes#vs-claude-md の要約に基づく推奨として書いた
- link 先の output-style-modes・where-to-put-instructions などの節は、束の「指せる節」にあるものだけを使った。公開前のページは、生成で「準備中」と出る

## 使用量

- 道具の呼び出し：約 12 回（Read 3、Bash 4、Write 6、うち検査 2 回）。Web の取得 0 回
