# fact-checking 執筆報告

## 書いたファイル
- `docs/verify/fact-checking.md`（stub から移した。stage: draft、updated: 2026-11-05、sources に api-docs-reduce-hallucinations・cc-changelog を足した）
- front matter の sections に guard・overall-check・when-it-fails を足した（既存 4 つの anchor は変更なし。順は guard が先頭）
- 雛形：`snippets/fact-checking/quote-each-claim`・`sources-only`・`summary-with-quotes`（各 .md と .expect.yaml）
- 目印の組（snippet 3・page-links・references）は空で置いた。`data/sources.d/fact-checking.yml` は新しい出典がないので作らない

## 必ず持つものの対応
- 手順：`#quotes`・`#sources-only`・`#best-of-n`・`#summaries`
- 確かめる・縛るのページへの道：`#guard`（allow-i-dont-know・doesnt-know-latest・handing-long-documents）、`#overall-check`（checking-citations・research-and-reports・using-research）。front matter の prerequisites（why-hallucinations）と related、冒頭の要点の前提
- level：使う（front matter 既存）
- 構成：要点 → `#guard` → 手順 4 節 → `#overall-check` → `#when-it-fails`

## メインに判断してほしいこと
- 要約の雛形の置き場所：A-16 後半は learning-with-ai が持つので、`#summaries` で link した。learning-with-ai を related に足すか判断してほしい（下の提案）
- 「3 回聞いて 2 回一致」の判断例と、「一致は正しさの保証でない」の文は私の推論で、（推論・実践例なし）を付けた。残すか判断してほしい

## 提案
```yaml
frontmatter:
  - {id: fact-checking, key: related, before: [..., citations-basics], after: [..., citations-basics, learning-with-ai, evidence-not-reports, claims-done-but-isnt], reason: "要約の表の使い方（learning-with-ai）と、「ない」と言い切られたとき（claims-done-but-isnt）の行き先を related から指せるようにする。いまは本文で学習の側だけ id で指し、後者は検索の打ち切りの例だけを書いた"}
```

## 検査の結果
- 1 回目：エラー 0・警告 2（助詞の重なり 2 件）。直したが、2 回目（`check_page.py` 計 2 回）の後に、残った 2 件の textlint 警告（1 文の読点が 4 つ以上・助詞の重なり）を、検査を流さずに文を分けて直した。最終の再検査はしていない
- 2 回目：エラー 0・警告 2（#guard の冒頭の文）。その後の直しは未検査

## 確かめていないこと
- 雛形 3 つの動作（実際に Claude へ出していない）。expect は予想
- アプリのタブの記述（資料を添付か貼る）・Claude Code のタブ（ファイルのパスを示す）の細部は、公式の面別の手順を確かめていない
- 「3 回聞いて 2 回一致」「同じ会話の続きで聞くと引きずられやすい」は推論。best-of-N を新しい会話で行うことの公式の記述は未確認
- 「外された主張が 0 件なら見直しが形だけの疑い」は私の経験則で、出典なし
- CHANGELOG の該当版は束の記述（v2.1.317）に基づき、版の数字は本文に書かず「CHANGELOG にある」とした。リンク先で再確認していない
- link の先の learning-with-ai が catalog にあるかは check の結果に依存（エラーは出なかった）

## 使用量
- 道具の呼び出し 約 12 回、Web の取得 1 回（Reduce hallucinations。書かれている内容が束の写しと一致することを確認）
