# write.md：create-and-review-prs（執筆）

## 書いたファイル

- docs/recipes/create-and-review-prs.md（stubs から移した。stage は draft、updated は 2026-11-05）
- front matter で変えたキー：`sections`（guards-first・verify-overall・when-it-fails の 3 節を足した。既存の 3 つの anchor は変えず）、`sources`（既存の id 2 つ）、`stage`、`updated`
- snippets/create-and-review-prs/ に 3 つ：risk-request（prompt）・pr-template（other）・address-request（prompt）と、それぞれの expect.yaml
- data/sources.d/create-and-review-prs.yml は作っていない。使った出典 2 つ（cc-docs-common-workflows・claude-dev-blog-solving-code-review-anthropic）が data/sources.yml に既にあるため

## 必ず持つものの対応

- 手順：risks-before-submitting（4 段）・pr-description・address-review（5 段）。各段に終わりの印を付けた
- 確かめる・縛るのページへの道：guards-first（working-with-git・independent-review・own-generated-code・diffs-humans-must-read・risk-tiered-approval などへ）。front matter の prerequisites 4 つも要点の「前提」に並べた
- level：front matter の `任せる`（変えていない）
- 構成の目安：要点 → guards-first → 手順（risks-before-submitting・pr-description・address-review）→ verify-overall → when-it-fails

## メインに判断してほしいこと

- 公開の約束や方針の文は入れていない。pr-template の「AI の使用」の欄は、開示の求め方がチームや場で違うため、disclosure-and-provenance#four-points を指すだけにした
- 目次の visual は「なし」なので図は置いていない

## 提案

- 提案はなし（front matter・用語集・data への変更案なし）。数値の提案も、変わりやすい値を本文に書いていないため、なし

## 検査の結果

- `check_page.py` を 2 回流した。1 回目：エラー 0・警告 4（snippet の目印が 1 行に置かれていなかった 3 件と、textlint の助詞「に」の重複 1 件）。2 回目：エラー 0・警告 1（助詞の重複）
- 2 回目の後に、助詞の重複の文を直した（61 行目）。直した後の検査は流していない（回数の決まりのため）。ほかの警告は目印を 2 行に分けて解消済み

## 確かめていないこと

- `gh pr create` の PR がセッションに紐づくことと `claude --from-pr <番号>` の再開は、束にある公式の Common workflows の要約によるもので、実際には試していない
- 雛形 3 つの動作は試していない（expect.yaml は期待を書いただけ）
- Claude Code チームのレビュー運用は、束の research/25 の写しによる。原典の blog は開いていない。引用した原文の一文は束の写しのとおり
- 助詞を直した 61 行目の textlint の結果。「往復の上限（2 回など）」は例で、根拠のある数ではないと本文に書いた
- 本文の判断例の「文言だけの変更は人の承認が要らない段」は、この辞典の推奨ではなく、チームの規則がある場合の例として書いた

## 使用量

- 道具の呼び出し：約 14 回（Read 3、Bash 6、Write 8 ほか）。Web の取得は 0 回
