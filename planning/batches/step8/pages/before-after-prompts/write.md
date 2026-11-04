# write.md：before-after-prompts

## 書いたファイル
- docs/prompting/before-after-prompts.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を [cc-docs-best-practices, api-docs-prompting-best-practices]（既存の id）、sections に guards・procedure・by-surface・check・when-it-fails を足した。既存の 4 anchor は変えず、節も外していない）
- snippets/before-after-prompts/audit-my-request.md と .expect.yaml（送る前の依頼文を 4 観点で点検させる prompt）
- snippets/before-after-prompts/rewrite-frame.md と .expect.yaml（4 種類の足しものを欄にした枠）
- data/sources.d/before-after-prompts.yml は作っていない（出典は既存 id で足りた）

## 必ず持つものの対応
- 冒頭の要点：冒頭の `!!! abstract "要点"`（前提は four-specifics）
- 手順：#procedure（各段に「印」を付けた 4 段）
- 確かめる・縛るのページへの道：#guards（say-what-you-want#two-layers、state-the-scope#two-layers、verification-ladder#verbal-checks、brief-a-new-colleague#colleague-test）、#verification（verification-ladder#verbal-checks）。front matter の related にも verification-ladder#verbal-checks と state-the-scope がある
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：#guards → #procedure → 例の 4 節 → #check（確かめ方）→ #when-it-fails（失敗したとき）
- level：整える（front matter のまま）

## メインに判断してほしいこと
- 本文の例（バグ修正・要約・外れ値・リファクタ・移行調査など）はこのページ用に作った例で、動作は未確認。出典は公式 Best practices の「Instead of / Try」の考え方だけ
- 「アプリで Claude が自分でコードを実行できるか」は書かず、「確かめていない」と書いた
- 目次の備考にある「30 例程度は目安」に従い、例は 9 組にとどめた

## 提案
- なし（用語集・prh・data・front matter の直しの提案はない）

## 検査の結果
- check_page.py 1 回目：エラー 0・警告 5（gen の目印が同じ行にあるもの 3、textlint の助詞 2）。直して 2 回目：エラー 0・警告 0

## 確かめていないこと
- 例文を実際の Claude に送った結果（snippets の expect は動作の確認前の記録）
- アプリでのコード実行の有無、API のタブで書いた `<documents>` と JSON の形の出力が実際にそうなるか
- ページの表示（mkdocs のビルド）。link の目印の生成は gen_site が済ませた

## 使用量
- 道具の呼び出し：約 12 回。Web の取得：0 回
