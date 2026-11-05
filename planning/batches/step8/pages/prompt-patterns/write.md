# write.md：prompt-patterns

## 書いたファイル
- docs/prompting/prompt-patterns.md（stubs から移動。stage: draft、updated: 2026-11-05。front matter で変えたキー：sections〔guards・procedure・check・when-it-fails を足した〕・sources〔4 件〕・stage・updated）
- snippets/prompt-patterns/ の research-request・review-request・plan-request・bug-report・draft-review-improve（各 .md と .expect.yaml）
- snippets/prompt-patterns/analysis-request.md は Write が道具に止められ、書けていない（.expect.yaml は書いた）。中身は最後の返答に載せた

## 必ず持つものの対応
- 手順：procedure（各段に確かめ方）
- 確かめる・縛るのページへの道：guards（four-specifics・before-after-prompts#guards・instructing-reviewers）・check（measure-changes）・when-it-fails（repeating-the-same-explanation ほか）。front matter の prerequisites と related にも同じ
- level：整える（front matter のまま）
- 構成の目安（要点→守り→手順→確かめ方→失敗したとき）：guards→procedure→型の 5 節→check→when-it-fails。official-tools は末尾

## メインに判断してほしいこと
- analysis-request.md の Write が止められた。メインが最後の返答の中身から作る必要がある
- 型の骨の「別のセッションに下書きを貼る」「基準を Claude 任せにすると下書きに合わせやすい」は束の材料にない実践上の助言。根拠の印は付けていない。必要なら弱める

## 検査の結果
- 1 回目：エラー 0・警告 10。直した後：エラー 0・警告 3
- 残した警告：analysis-request の雛形がない（上記）。助詞「に」の重なり 2 件（57 行目はリンク展開文字の誤検出に近く、164 行目は直さず）

## 確かめていないこと
- 雛形の動作は試していない
- 面ごとのタブの手段（アプリのプロジェクトの指示・Claude Code のスキル・API の雛形化）は一般的な説明で、各面の最新の画面は確かめていない
- 公式の文書の内容は束の写しに基づく。元の URL は開いていない

## 使用量
- 道具の呼び出し：約 25 回。Web の取得：0 回
