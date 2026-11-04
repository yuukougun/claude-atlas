# write.md：research-and-reports（調べものとレポート）

## 書いたファイル

- `docs/recipes/research-and-reports.md`（stubs から mv。stage を draft、updated を 2026-11-05 に）
- front matter で変えたキー：`sections`（guard・steps・when-it-fails を足した。既存の 3 つの anchor は変えていない）・`sources`（hc-research・hc-web-search・hc-projects-what・hc-artifacts・hc-cowork-and-chat。すべて data/sources.yml にある既存の id）・`stage`・`updated`
- 雛形：`snippets/research-and-reports/research-request.{txt,expect.yaml}`（問い・範囲・出典の条件を決めた依頼。目次の案にはなく、分かりやすさのため足した）、`snippets/research-and-reports/facts-vs-inference.{txt,expect.yaml}`（目次の templates の案：書かれていることと推測を分け、原文の引用を添えた表）
- `data/sources.d/research-and-reports.yml` は作っていない（新しい出典なし）

## 必ず持つものの対応

- 手順：`#steps`（5 段と各段の確かめの目安）。個々の段は `#define-the-question`（1・3）、`#app-or-claude-code`（2）、`#check-sources`（4）
- 確かめる・縛るのページへの道：`#guard`（checking-citations#steps・knowledge-cutoff#why・fact-checking#guard）、`#check-sources`（fact-checking・summary-overgeneralization・read-specs-yourself・second-opinion-from-another-model）、`#when-it-fails`（plausible-falsehoods・doesnt-know-latest など）。front matter の前提に checking-citations、関連に fact-checking を持つ
- level：整える（front matter のまま）
- 構成の目安（要点 → 先に整える守り → 手順 → 確かめ方 → 失敗したとき）：冒頭の囲み → `#guard` → `#steps`・`#define-the-question`・`#app-or-claude-code` → `#check-sources` → `#when-it-fails`

## メインに判断してほしいこと

- Claude Code の面：web 検索・取得の動作は束の材料になく、記憶で書かなかったため「未確認」と書いた。必要なら Claude Code の担当ページ（または一次資料）での確認後に書き足す
- `compare` の表は tracks の 4 機能から生成される。表の列が読み手に合うかは生成後に見てほしい
- 台帳 `outdated-advice-ledger#cowork-separate-app` の link は、app-or-claude-code の節の末尾に置いた

## 提案

- front matter・用語集・data への提案はない。数値の提案もない（数値を本文に書いていない）

## 検査の結果

- 2 回流した（書いた後・直した後）。エラー 0。警告は 7 件から 3 件に減った
- 残した警告 3 件（いずれも textlint の no-doubled-joshi。助詞の重複で、リンクの目印の間に道具が題名を入れた長い一文のため。意味が曖昧にならないので残した）：51 行（`#guard` の導入）・53 行・156 行

## 確かめていないこと

- 雛形 2 つの動作（動作を確かめていない旨は道具が書く）
- 事実の正しさは、束の材料（data の features・台帳の行・つながるページの要約）に基づく。一次資料は開いていない（Web の取得 0 回）
- Claude Code での web 調査、リサーチの起動条件・プラン別の差は、本文では持ち主のページ（using-research など）に任せた
- 直しの 1 回は python による文字列置換で行った（Edit の代わり）

## 使用量

- 道具の呼び出し：約 12 回（Read 3・Bash 6・Write 5）。Web の取得：0 回
