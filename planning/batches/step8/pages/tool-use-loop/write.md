# write.md：tool-use-loop

## 書いたファイル
- docs/api/tool-use-loop.md（stubs から移した。stage は draft、updated 2026-11-05）
- planning/batches/step8/pages/tool-use-loop/facts-proposal.yml
- front matter で変えたキー：sections（round-trip・what-it-helps・misconceptions を足した。既存 3 つの anchor は変えず）・sources（5 件、すべて data/sources.yml にある id）・stage・updated
- 雛形・図ファイルなし。図は本文の Mermaid（sequenceDiagram）。雛形を置かない理由：API キーが要り試せないため（カード §10）。data/sources.d は新しい出典がないので書かず

## 必ず持つものの対応
- 要点の最初が「何が分かるか」：冒頭の囲み（abstract）
- level（仕組みにする）：front matter。本文で名指しはしない
- principle「縛る」「見せる」を名指し：#what-it-helps（縛る×縛っていない、見せる×縛っていない、縛る×境界がない）
- prevents「縛っていない」「境界がない」を名指し：#what-it-helps
- pitfalls：front matter に値なし（持たない）
- 構成（要点 → 何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：#round-trip（例と図）→ #client-and-server → #forcing → #who-runs-the-loop → #what-it-helps → #misconceptions →（関連は page-links）。「なぜ」の比喩付きの図は、比喩を使わず往復の図にした（新しい比喩を作らないため）

## メインに判断してほしいこと
- 表示の確認：#client-and-server の compare 表（成熟度 入った版）は、2 機能が同じページを指すため、表の機能名のリンクが自分のページへの自己リンクになる。許容か、表を外すかを判断してほしい

## 提案
- 数値・既定値（facts-proposal.yml）：tool_choice の既定値（auto）と、強制が使えないモデルの表。本文は両方とも値を書かず、「auto のとき」「モデルによっては」の形にした。目印を置く場所は used_in に書いた
- 用語集：「システムプロンプト」を prh が要求する（system prompt は書けない）ので本文ではそれに従った。tool_use・tool_result・tool runner を用語として足すかは判断してほしい（本文では原文のままバッククォートか平文）

## 検査の結果
- check_page.py を 2 回流した。1 回目：エラー 2（system prompt の表記）・警告 8。直した後：エラー 0・警告 6
- 残した警告 6：no-doubled-joshi（助詞の重なり）。文は意味が通り、分けると冗長になるため残した

## 確かめていないこと
- 公式の Define tools・Server tools・Stop reasons の文書は開いていない（Web 取得 1 回：Tool use overview のみ）。pause_turn と、server tool と client tool が同じ並列の呼び出しに混ざる扱いは、束の data の note と overview の記述からで、文書で確かめていない
- 「モデルによって強い表現が過剰な呼び出しを招く」は束の 02 §4-11（確認日 2026-10-29）からで、api-docs-prompting-best-practices を開いていない
- tool_choice の any・tool の 400 エラーが、いまどのモデルで起きるかは確かめていない（本文に書かず、提案の要確認にした）
- strict の保証の範囲（引数の型・必須項目まで）の詳細、tool runner の停止制御の細部は確かめていない

## 使用量
- 道具の呼び出し：約 22 回（Web の取得 1 回、check_page.py 2 回）
