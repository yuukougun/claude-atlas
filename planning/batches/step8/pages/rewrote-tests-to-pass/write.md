# write.md：rewrote-tests-to-pass（執筆）

## 書いたファイル
- docs/symptoms/rewrote-tests-to-pass.md（stubs から mv。stage を draft、updated を 2026-11-05。front matter で変えたキーは sections〔7 節に〕・stage・updated・sources〔既にある id 7 件〕）
- snippets/rewrote-tests-to-pass/audit-the-diff.txt と audit-the-diff.expect.yaml
- data/sources.d は作っていない（新しい出典なし）

## 必ず持つものの対応
- 冒頭の要点：先頭の囲み（abstract）
- よくある形（読者の言葉）：#forms
- 診断のチェックリスト（原因を安く確かめる順）：#diagnosis（確かめていない → 縛っていない。人の側の落とし穴は front matter の pitfalls が空なので置かない）
- 原因ごとの振り分け先（routes）：#routes-to-fixes（routes の目印）
- 判断例：#example
- 予防（仕組みに移す）：#prevention
- 型の手引きにない足し：#first-response（見つけた直後の初動）、#lookalikes（似た症状との見分け）

## メインに判断してほしいこと
- 診断の「縛っていない」で、「Edit の deny ルールだけでは子プロセスの書き込みを止められないことがある」と書いた。束の freeze-eval-assets と permission-rules の要約に基づく。持ち主のページ側と食い違わないか、メインの確認を頼む。
- 「確かめていない」の項に、ImpossibleBench の「止まる権利」の効果（Claude Opus 4.1 では小さい）を入れた。束の research/24 A-10 の写しに基づき、数値は Claude 以外のモデルのものを書いていない。
- 初動に `git restore --source=<時点> -- <テストのパス>` を書いた。保存した差分を先に取る手順を前に置いた。

## 提案
- 用語集・prh・data への提案はなし。
- front matter の直しの提案はなし。

## 検査の結果
- check_page.py：2 回流した。最終はエラー 0・警告 5。
- 警告の内訳：max-ten 1 件（#forms のエラー消しの文。列挙のため読点が多い）、助詞の重なり 4 件（#diagnosis の見るもの 1 件、雛形の前の文 1 件、予防の箇条 2 件。予防の 2 件は link の目印の間に入る相手の題名が長く、題名の中の「に」を数えた誤検出に近い）。直すと意味が落ちるか、題名由来のため残した。

## 確かめていないこと
- 一次資料を開いていない（Web の取得 0 回）。事実は束の写しだけに基づく。
- ImpossibleBench の「79% 超」は束の二次の要約（11 p34#8、Opus 4.1 世代、下限値）に基づく。論文本体の数値は未確認。
- Claude 3.7 Sonnet のシステムカードの記述は束の写し（11 p34#227）に基づく。原文は未確認。
- Battlecode の例（公開ケースへの特例化）は 11 p34#16 の要約だけに基づく。どの振り返りの資料かを特定していないので、sources に入れず、本文では「コンテストの振り返り」と書いて根拠を弱・類推にした。
- Kaggle の例は束の要約（11 p34#223）に基づく。出典 lukyanenko-rogii-geosteering-kaggle は sources に入れたが、記事本文は未確認。
- 「deny ルールは、どの許可モードでも先に評価される」は data の permissions の note に基づく。
- 雛形 audit-the-diff の動作は未確認（expect は観察の記録として書いた）。
- 非公式の文など、作者の承認が要る文は足していない。

## 使用量
- 道具の呼び出し：約 13 回（Read 3、Bash 6、Write 4 ほか）。Web の取得：0 回。
