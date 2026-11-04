# write.md：ask-for-options

## 書いたファイル
- `docs/prompting/ask-for-options.md`（stub から移した。front matter の変更：`sections` に why・limits を足した、`stage` を draft、`updated` を 2026-11-05）
- `snippets/ask-for-options/`：`options-recommend`・`question-role`・`critique-own-idea`（各 `.txt` と `.expect.yaml`）。目次の templates の案は critique-own-idea。残り 2 つは分かりやすさのために足した
- 出典のファイル（`data/sources.d/ask-for-options.yml`）は作っていない。`sources` は空のまま（下の「メインに判断してほしいこと」）

## 必ず持つものの対応
- 冒頭の要点（最初は「何が分かるか」）：冒頭の囲み
- どの原理に関わるか（`principle`：握る・見せる）：`why`（「握る」「見せる」の項）
- どの原因に関わるか（`prevents`：見えていない）：`why`（「見えていない」の項）
- `pitfalls`（同意を根拠にする・みんなの案になる）：`why`（それぞれの項）
- level（整える）：front matter
- 技法の構成（頼み方の例 → 何が変わるか → なぜ効くか → 効かない場面）：`choose`（Before/After と足したもの）→ `ideate`・`critique` → `why` → `limits`

## メインに判断してほしいこと
- `sources` が空：束に出典の一覧がなく、材料は調査資料と、実務家の tip（（根拠：弱）で本文に付けた）。公式の文書で裏付けられるなら、出典の追加を頼みたい
- 本文の（類推）は束の C-14（実践・類推）に基づく。強さの付け方に異論があれば直してほしい

## 提案
- 用語集・prh・data への提案なし。front matter の他のキーの変更もなし

## 検査の結果
- 1 回目：エラー 0・警告 4（signs と同じ「一つの案」・助詞の重なり 3 件）。直して 2 回目：エラー 0・警告 1（助詞の重なり、行 156）。その後その文を 1 か所直したが、再検査は決まりにより流していない

## 確かめていないこと
- 雛形 3 つの動作（expect は未確認の予測）
- 本文の「実務家が紹介している」型は、束の写しの要約。原文の記事は開いていない
- 判断例は作者が作った例で、実在の事例ではない
- Claude の返答が実際に案を 1 つしか出さない頻度は測っていない

## 使用量
- 道具の呼び出し：約 20 回。Web の取得：0 回
