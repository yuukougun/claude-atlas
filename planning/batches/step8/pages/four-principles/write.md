# four-principles 執筆報告

## 書いたファイル
- docs/start/four-principles.md（stub から移動。stage draft、updated 2026-11-05）
- docs/img/four-principles/proportional-rule.svg（比例則の図。目次の visual 案）
- front matter の変更：`sections` に overview（4 つの原理の一覧）・from-trouble（うまくいかないときの引き方）を足した（既存の anchor は不変）、`sources` に既存の 6 件（cc-docs-best-practices・cc-docs-how-claude-code-works・anthropic-eng-effective-context-engineering-ai・claude-blog-steering-code-skills-hooks・arxiv-2506-09050・vasconcelos-2023-explanations-overreliance）、stage、updated

## 必ず持つものの対応
- 型 guide は冒頭の要点のほかに必ず持つものがない。要点の囲み（前提は「なし」）のみ。構成は自由（表とリンクが本体）：overview・from-trouble の表、by-surface のタブ

## メインに判断してほしいこと
- ALE-Bench の数値（1167→1264→1879、上位 6.8%）は research/24 B-32 で確かめ済みの範囲だけを、研究名・年・モデル付きで本文に書いた（根拠：中、類推を併記）。置いてよいか確認してほしい
- 「握る」は公式の分類でなく辞典の提案と本文で明記した。AI Fluency（4D）は構成に使わず、本文でも触れていない

## 提案
- なし（数値の提案も、front matter の他キーの提案もなし）

## 検査の結果
- 1 回目：エラー 2（前提の書き方、sandbox の表記）・警告 6。直した後：エラー 0・警告 2
- 残した警告 2：no-doubled-joshi（131 行の「に」、136 行の判断例の「に」）。文意は明確なので残した

## 確かめていないこと
- 面ごとの手段（タブ）の個々の機能名は、束の材料（00 §2 の表）の写しで、一次資料で再確認していない
- 握るの節の「参加者の報告は線引きにほぼ収束」「AI 支援の RCT でデバッグの差が最大」は材料の要約に基づき、原文を開いていない
- 図 SVG の表示は目で確かめていない
- リンク先のページは多くが準備中で、節の中身との整合は未確認

## 使用量
- 道具の呼び出し 約 11 回、Web の取得 0 回
