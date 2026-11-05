# write.md：share-targets-and-bounds（目標値・上界を伝える）

## 書いたファイル

- `docs/prompting/share-targets-and-bounds.md`（stub から mv。stage を draft、updated を 2026-11-05）
- front matter で変えたキー：`sections`（templates・why・limits を足した。targets・measure は元のまま）、`sources`（既存の 2 つの id）、`stage`、`updated`
- `snippets/share-targets-and-bounds/target-and-bound-request.md` と `.expect.yaml`
- 出典は既存の `data/sources.yml` の id のみで、`data/sources.d/` には書いていない

## 必ず持つものの対応

- どの原理・原因に関わるか（`principle`・`prevents` の名指し）：`#why`（見せる・確かめる／見えていない）。要点の「関わる原理と原因」にも置いた
- `pitfalls`：front matter に持たないため、名指しなし
- level：front matter の `level: 任せる`。要点の最初は「何が分かるか」
- 技法の構成：Before/After は `#targets`、何が変わるかも `#targets`、なぜ効くかは `#why`、効かない場面は `#limits`

## メインに判断してほしいこと

- Anthropic の記事（2026-01-21）を WebFetch 1 回で確かめた。公開前の Claude Opus 4.5 を Claude Code で動かした採用課題 v2 で、合格の基準に届いた後に止まり、達成できるサイクル数を伝えると回避策を見つけた。束の「未確認」は本文では原文で確認済みとして扱った。ただし材料の表の「未確認」の印を data 側で外すかは、メンが判断する
- 要点の「根拠の強さ」の項目は、カードの標準の形にない追加。不要なら外してよい

## 提案

なし（数値の提案も用語集への提案もなし）。

## 検査の結果

- `check_page.py` を 2 回流した。1 回目はエラー 1・警告 2（「限界です」の「です」が敬体と数えられた、助詞の重なり 2 件）。直して 2 回目はエラー 0・警告 0

## 確かめていないこと

- DrivenData の記事は束の写しだけで読み、原文を開いていない。使われたモデルも確かめていない
- 雛形の動作（Claude に出して試すこと）は未確認
- 上界を測る手順は measure-the-upper-bound の持ち主ページの内容と照合していない（骨子の 3 点のみ）。リンク先の節を指していない
- 他の OS・IDE 拡張での動作は扱っていない

## 使用量

- 道具の呼び出し：約 14 回。Web の取得：1 回
