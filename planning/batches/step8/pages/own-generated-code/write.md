# write.md：own-generated-code（recipe・verify）

## 書いたファイル
- docs/verify/own-generated-code.md（stub から移動。stubs 側は rm）。front matter で変えたキー：sections（guards・overall-check・when-it-fails を足した。既存の 3 anchor は変えず）、sources（既存 id 2 つ：anthropic-research-ai-assistance-coding-skills・rustc-dev-guide-llm-guidance-reviewing）、stage（draft）、updated（2026-11-05）
- snippets/own-generated-code/explain-before-adopting.md と .expect.yaml（目次の templates の案）
- snippets/own-generated-code/run-the-edges.md と .expect.yaml（足した雛形：説明の入力の端を実行で照らす依頼）
- data/sources.d/ は書いていない（既存の source id だけを使った）

## 必ず持つものの対応
- 手順：#explain（説明させる）→ #check-explanation（実行で照らす）→ #gate（言い直して採る）。各段に「終わった印」か手順を置いた
- 確かめる・縛るのページへの道：前提 how-much-understanding-to-keep（冒頭の要点・#gate・#when-it-fails）。#guards・#check-explanation・#overall-check から diffs-humans-must-read・independent-review・evidence-not-reports・looks-are-not-quality・unfaithful-reasoning を指す
- level（任せる）：front matter のまま
- 構成の目安（要点 → 守り → 手順 → 確かめ方 → 失敗したとき）：#guards → #explain〜#gate → #overall-check → #when-it-fails

## メインに判断してほしいこと
- #gate の Rust コンパイラ開発ガイドの規約の文は、束の材料（11 の p56#43）に基づく。Web は取得していない。本文は「ガイドの版で変わりうる」と付けた
- #when-it-fails の Anthropic の研究の数値（50%・67%・52 人・各 4 人ほど）は束の research/24 A-13 の写し。本文に手で書いた（研究の固定の記録として、common §9 の扱い）

## 提案
- なし（facts・用語集・prh・front matter の他のキーの提案はない）

## 検査の結果
- 1 回目：エラー 0・警告 7。直して 2 回目：エラー 0・警告 5
- 残した警告：no-doubled-joshi の 3 件（53・149 行はリンクの題名に含まれる「に」、168 行は「当てる範囲が広すぎる」の文）と、141 行の「に」。130 行は判断例の見出し「変更を実行で照らすか」の dict6 指摘。いずれも内容に問題はないと判断。検査は規定の 2 回に達したので、これ以上は流していない

## 確かめていないこと
- 雛形 2 つの動作（実際に Claude へ出して返答を見ていない）。雛形は動作未確認のまま載せた
- Rust ガイドと Anthropic の研究の記述を、一次資料で開いて確かめていない（束の写しによる）
- 生成後の見た目（gen_site の出力は check_page が流した結果のみ）
- 窓口のない面（アプリ・API）の動作。surfaces は claude-code のみ

## 使用量
- 道具の呼び出し：約 12 回。Web の取得：0 回
