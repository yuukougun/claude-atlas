# write.md：lockbox-and-holdout（執筆）

## 書いたファイル
- docs/eval/lockbox-and-holdout.md（stubs から mv。stage は draft）。front matter で変えたキー：`sections`（what-happens・what-it-affects・misconceptions を足した。既存 3 つの anchor は不変）、`sources`（arxiv-2605-21384・cc-docs-permissions・cc-docs-sandboxing。いずれも data/sources.yml に既存）、`stage`、`updated`
- docs/img/lockbox-and-holdout/three-tiers.svg（三層の図。400x290、文字はテキスト、枠線の太さと破線で区別）
- snippets/lockbox-and-holdout/score-only-request.{md,expect.yaml}（prompt）、tier-layout.{txt,expect.yaml}（other）。目印の組は本文に置いた
- data/sources.d/lockbox-and-holdout.yml は作っていない（出典がすべて既存のため）

## 必ず持つものの対応
- 冒頭の要点の最初の項目が「何が分かるか」：冒頭の要点の囲み
- 原理 `principle`（縛る・握る）を本文で名指す：#what-it-affects（縛る・握るの 2 項目）。#keep-out-of-reach の「お願いと鍵」も縛るに関わる
- 原因 `prevents`（縛っていない・確かめていない）を本文で名指す：#what-it-affects（「縛っていない」「確かめていない」の項目）
- `pitfalls` を名指す：持たない。front matter の pitfalls が空のため
- 構成の目安（要点→何が起きるか→なぜ（図）→何に効くか→誤解→関連）：#what-happens → #three-tiers（図・なぜ 2 つ隠すか）→ #scores-only → #keep-out-of-reach → #what-it-affects → #misconceptions → 関連はテンプレート

## メインに判断してほしいこと
- 三層の定義：材料は「入力を開発用・検証用・ロックボックスの三層」「hold-out は人が持ち点数だけ返す」「ロックボックスは節目にだけ見る」まで。「検証用＝点数だけ返す、ロックボックス＝点数も返さず選ぶために使わない」の線引きは、材料と選択圧の考え方から書いた設計である。本文では「実践者の運用に機械学習の考え方を当てはめた（根拠：中・類推）」と書いた。要否の確認を願う
- 「点数だけでも問い合わせを重ねると合わせ込める（類推）」は材料にない。選択圧のページの考え方からの類推として書いた
- 「月単位の定期確認にとどめる（根拠：弱）」は、材料の「月 1 回程度」を数字なしで書いた。数値の提案にするかは任せる

## 提案
```yaml
frontmatter: []
```
- 用語集：「ロックボックス」「hold-out」の追加を提案。hold-out＝作る途中の調整では使わず取り置く検証用データ、ロックボックス＝その中で人だけが持ち節目にだけ開ける最後の層
- freeze-eval-assets のページで、設定の雛形（`data/holdout/` の Read deny と sandbox `denyRead`）を持つ。このページは置き場所と考え方だけを書き、そこを指した

## 検査の結果
- 1 回目：エラー 0・警告 2（no-doubled-joshi 1、sentence-length 1）。直して 2 回目：エラー 0・警告 1（no-doubled-joshi、冒頭の導入）
- 2 回目の後に、残った警告の文を直した（「調整に使わずに」→「調整では使わず」）。確かめ直していない（検査は 2 回まで）

## 確かめていない
- 雛形 2 つの動作（Claude が依頼どおり点数を人に頼む形で止まるか）は未確認
- `sandbox.filesystem.denyRead` と、権限ルールのパス記法は、公式の sandboxing・permissions の文書（2026-11-05 に取得）で確かめたが、雛形には載せていない（freeze-eval-assets を指す）
- SpecBench の数値（約 43〜48 ポイント、97%・0%）は束の写しに基づく。論文本体は開いていない。97%・0% の例は「Claude 以外のモデル」とだけ書き、名前は出していない
- 「フックとローカルの MCP サーバーはサンドボックスの外で動く」は research/23 #5 に基づく
- WSL・Linux 以外の OS と IDE 拡張の動作は未確認

## 使用量
- 道具の呼び出し：約 19 回。Web の取得：2 回（sandboxing・permissions の公式文書）
