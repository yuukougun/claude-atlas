# write.md：build-on-results（執筆）

## 書いたファイル
- `docs/context/build-on-results.md`（`stubs/context/build-on-results.md` は削除＝移動）
- `snippets/build-on-results/refine-from-result.md`・`.expect.yaml`
- front matter で変えたキー：`sections`（`what-to-show`・`effect`・`misconceptions` を足した。既存 2 節の anchor は不変）・`stage`（draft）・`updated`（2026-11-05）・`sources`（`arxiv-2506-09050`。data/sources.yml にある id）
- `data/sources.d/build-on-results.yml` は作っていない（新しい出典がなく、既存 id だけで足りるため）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（`principle`＝見せる・確かめる、`prevents`＝見えていない）：`#effect`（1 段落目で名指し）。`pitfalls` は空なので該当なし
- level：front matter が「整える」。要点の最初の項目は「何が分かるか」
- 構成の目安（技法）：要点 → 頼み方の例（Before/After）＝`#regenerate-or-refine` → 何が変わるか＝同節の After 注記と `#what-to-show` → なぜ効くか＝`#regenerate-or-refine`（独立試行になる説明と ALE-Bench）・`#effect` → 効かない場面・やりすぎ＝`#effect`・`#misconceptions` → 関連（テンプレートが出す）
- /clear・巻き戻しとの両立（目次の中心）：`#with-clear`

## メインに判断してほしいこと
- 11 の注記にある「分野04（prompting）に置く案」は採らず context のまま書いた（目次の決定どおり）。refine-in-conversation とは `#effect` の「依頼の言い方がずれている」で結んだ
- 目次の「訂正が 2 回失敗したら /clear」という数字は、変わりやすい規則の値になりうるので本文に書かず、「訂正を重ねても直らないとき」と言い換えた

## 提案
- 用語集・prh・data への提案はなし。front matter の他キーの直しもなし

## 検査の結果
- `check_page.py` を 2 回流した。最終はエラー 0・警告 2
- 残した警告：67 行目の max-ten（5 項目の並べ立てで、読点を減らすと列挙が読みにくい）。154 行目の no-doubled-joshi（link の目印の間に道具が入れた相手の題名「頼み方は一回で決めない（会話で詰める）」に起因し、本文側の文ではない）
- 1 回目の警告 6 件のうち 4 件は文を分けて直した。直しの Edit は Bash の python で行った（Write でなく）

## 確かめていないこと
- ALE-Bench の数値（40 問・4 時間の逐次改善で 400 点以上・150 回の独立生成との比較が 6 問）は、調査資料 11a の S7（arXiv 2506.09050v2 の本文と一致とある）に基づき、一次資料は開いていない。「4 時間ほど」と「評価した全モデル」の言い方は、調査資料の要約の写し
- 論文が評価したモデルに Claude が含まれるかは確かめていない（本文は「当時の o3 や Gemini 2.5 Pro など」と、調査資料で確認できたものだけを書いた）
- API が会話の状態を持たない、アプリの添付、Claude Code の動作の記述は一般的な理解に基づき、各面の公式の文書では確かめていない。雛形は動かして確かめていない
- 判断例（悪化が続いた長い作業）は、この辞典が作った想定で、実例ではない

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：0 回
