# write.md：effort-levels

## 書いたファイル
- `docs/models/effort-levels.md`（stub から移して draft。front matter は `sections` に pitfalls・compare・outdated-advice を足し、`sources` に既存の id 7 件、`stage: draft`、`updated: 2026-11-05`）
- `snippets/effort-levels/model-effort-settings.json`＋`.expect.yaml`（目次の templates の案。settings）
- `snippets/effort-levels/low-effort-subagent.md`＋`.expect.yaml`（足した雛形。subagent）
- `planning/batches/step8/pages/effort-levels/facts-proposal.yml`

## 必ず持つものの対応
- 機能の属性のバッジ：冒頭の要点の「成熟度」（`feature maturity` の目印）。強制力は data の effort に属性がなく目印にできないため、「何を止められるか：何も止めない」の文で書いた（下の判断を参照）
- tracks：effort・adaptive-thinking（front matter のまま。節は levels と thinking-toggle）
- 構成の目安（使いどころ）：levels（判断例つき）・pitfalls ／ 最小の使い方（面のタブ）：how-to-set・thinking-toggle ／ 雛形：how-to-set・subagents-and-org-limits ／ 効かない場面・落とし穴：pitfalls ／ 比べる相手：compare ／ 古くなった助言：outdated-advice（budget-tokens の台帳を link）
- level：整える（front matter のまま）

## メインに判断してほしいこと
- 節 defaults-by-surface に、数値ファイルの「モデル × 面」の表がまだ無い（facts に effort の表がない）。`fact-table` の目印はない id で止まるため置けず、本文は値なしの説明にした。facts-proposal.yml の `effort-default-by-model-surface` を反映したら、節の「各モデルの既定の値は、変わりやすいので…」の段落の直前に `<!-- gen:begin fact-table effort-default-by-model-surface --><!-- gen:end fact-table effort-default-by-model-surface -->` を置き、その段落は表を指す文に直してほしい
- data の effort に `enforcement` 属性がない。要点の「強制力」の目印を置けなかった。値を足すか（effort は設定で、お願い・鍵のどちらにも当たらない可能性がある）、型の必ず持つものの扱いを決めてほしい
- 本文の「新しい版」としか書いていない 2 か所（modelSettings、別モデルのサブエージェント）は、facts-proposal.yml の版の 2 件を反映すれば、目印で版を書ける

## 提案
- facts-proposal.yml：既定の effort の表 1 件（research/23 §3.2 の写し。Claude Code の列は 2026-11-05 に Model configuration と照合）、版の fact 2 件
- 用語集：新しい語の提案はなし。front matter の他のキーの直しもなし

## 検査の結果
- `check_page.py effort-levels`：1 回目 エラー 0・警告 3（助詞「が」の重複。3 文を書き直した）、2 回目 エラー 0・警告 0

## 確かめていないこと
- スニペットの動作は未確認（雛形に「動作を確かめていない」旨が付く）。`modelSettings` のモデルの名前の書き方は公式の例（`claude-opus-5-5`）に従った。サブエージェントの `effort` が `/agents` にどう表示されるかは未確認
- アプリの画面の項目名（Low／Extra high など）は Help Center の記述による。画面そのものは見ていない。日本語の画面が「努力」と出るかも未確認
- 別モデルのサブエージェントの段（CHANGELOG 由来）は 2026-11-03 の research/22 の記録で、原文を今回開いていない
- Windows・macOS・IDE 拡張での動作は確かめていない
- 参考文献の節（sources から道具が作る）の中身は見ていない

## 使用量
- 道具の呼び出し：約 20 回。Web の取得：3 回（Model configuration・Settings reference・Effort）
