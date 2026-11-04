# write.md：headless-basics

## 書いたファイル
- docs/delegate/headless-basics.md（stubs から移動。stage を draft、updated を 2026-11-05。front matter で変えたのは sections〔使いどころ・最小の使い方・雛形・効かない場面・比べる相手・古くなった助言を追加、既存 5 節は保持〕・sources〔既存 id 7 件〕・stage・updated）
- snippets/headless-basics/limited-run.sh と limited-run.expect.yaml
- planning/batches/step8/pages/headless-basics/facts-proposal.yml

## 必ず持つものの対応
- 機能の属性のバッジ（強制力・読み込みの時期など）：テンプレートが出す。本文は要点の `#` 強制力の項（`feature permission-modes/enforcement`）と、導入の成熟度（`feature headless/maturity`）。headless 自身に強制力の属性はないので、権限モードの値を指した
- tracks：front matter（headless・permission-modes）のまま。節 `#permissions`・`#output-and-exit-codes` が本体
- 構成の目安（要点→使いどころ→最小の使い方→雛形→効かない場面→比べる相手→古くなった助言）：`#when`・`#minimal`・`#templates`・`#pitfalls`・`#compare`・`#outdated`。目次の 5 節は `#minimal` と `#templates` の間に置いた
- 1機能1ページ・level：回す（front matter のまま）

## メインに判断してほしいこと
- 数値の提案 3 件（facts-proposal.yml）。取り込めば、`#permissions` の既定の変遷と `--permission-prompts none` の版、`#output-and-exit-codes` の「直った版」に fact の目印を置ける。いまは版を書かず「公式で確かめる」と書いた
- 要点の「強制力」は、headless に強制力の属性がないため permission-modes の値（鍵）を指した。属性の持たせ方に別の決まりがあれば直す

## 提案
- 用語集：特になし

## 検査の結果
- `check_page.py headless-basics`：1 回目はエラー 1・警告 5（skill→スキル、冗長表現、文の長さ、助詞の重なり）。直した後の 2 回目は エラー 0・警告 0

## 確かめていないこと
- `--max-turns`・`--max-budget-usd` に達したときの終了コードと出力（公式の取得では分からなかった。本文に「確かめていない」と書いた）
- 雛形（limited-run.sh）の実行。`dontAsk` と `--allowedTools` の組での動きは、公式の文書の記述に基づく
- `auto` の連続ブロックで `-p` が止まらない点は、束の research/23（Permission modes、2026-11-03）に基づく。変わった版は未確認
- 古い版の不具合（終了コード・入れ子・理由を言わず止まる）は、束の research/22 に基づき、版を本文に書いていない
- Windows とほかの OS の動作

## 使用量
- 道具の呼び出し 19 回ほど、Web の取得 2 回（code.claude.com の headless・cli-reference）
