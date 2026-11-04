# write.md：instructing-reviewers

## 書いたファイル
- docs/verify/instructing-reviewers.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を 4 件、sections に example・effects・limits を足した）
- snippets/instructing-reviewers/review-request-exhaustive.{md,expect.yaml}（目次の templates の案）
- snippets/instructing-reviewers/review-filter-pass.{md,expect.yaml}（選別の依頼。分かりやすさのために足した）
- data/sources.d は書いていない（sources は既存の id だけ）

## 必ず持つものの対応
- どの原理に関わるか（`principle`：確かめる）：`#effects`
- どの原因に関わるか（`prevents`：確かめていない）：`#effects`
- `pitfalls`：空のため名指しなし
- level（仕組みにする）：front matter。要点の最初の項目は「何が分かるか」
- 技法の構成（頼み方の例 Before/After → 何が変わるか → なぜ効くか → 効かない場面・やりすぎ）：`#example`（Before/After と足したもの）、`#exhaustive-then-filter`・`#hide-your-view`・`#per-finding`（何が変わるか・なぜ効くか）、`#limits`

## メインに判断してほしいこと
- 「保守的に」「重大なものだけ」で報告が減る話は、公式の Opus 5 向けの文書を出典（api-docs-prompting-opus-5）にしたが、文書は開いていない（束の写しによる）。モデル名・世代は本文に書かず「新しい世代のモデル」とした。モデル別の傾向の数値ファイルがあれば、目印で書き足したい

## 提案
- 該当なし（front matter の sources だけ自分で書いた）

## 検査の結果
- check_page 2 回：エラー 0、警告 2（textlint の no-doubled-joshi。「と」「に」の重なり。直しの 1 回目に 3 件を Bash の置換で直した。残りは読みを損なわないため、検証の担当の判断に任せる）

## 確かめていないこと
- 公式の文書（Opus 5 向けの指針）と arXiv の要旨を開いていない。束の写しと調査資料の訂正（B-40）に従った
- 「穴を探せ」の指摘が付きやすい話の出どころ（公式か解説か）が束で曖昧。出典は api-docs-prompting-opus-5 に寄せた
- 雛形は動かしていない。確信度が自己申告で当たりやすさと合う保証がない、という注意は一般の推論で、研究の裏付けはない
- p56#8（判定・理由・修正案まで求めると率が上がる）は一次資料が束にないため本文に入れていない。p56#19（確信度・影響・実験を付けさせる）は根拠の印を付けずに技法として書いた

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
