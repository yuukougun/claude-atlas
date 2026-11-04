# write.md：ai-ideas-are-everyones

## 書いたファイル
- docs/judgment/ai-ideas-are-everyones.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を既存 id の 8 件、sections に check を追加）
- 雛形・図・data/sources.d は作っていない（目次の templates が「なし」。出典は data/sources.yml の既存 id だけを使った）

## 必ず持つものの対応
- 判断例（状況・迷う候補・選んだもの・理由）：#when-difference-matters（「判断例：企画コンペに出す案を決める」）
- level：front matter の level: 整える（本文では扱わない）
- 構成の目安：要点（冒頭）→ 何が起きるか #outputs-converge・#looks-vs-value → なぜ（人の側の仕組み。#outputs-converge の末尾と #looks-vs-value の終わりに短く）→ 判断例 #when-difference-matters → 握るもの #routine-vs-specific → 確かめ方 #check

## メインに判断してほしいこと
- 10.7% は工程2で確かめていないため本文に書かなかった（原論文の science.org は check_noai で断る指定あり）。代わりに「作品どうしが似通った」とだけ書いた。原論文を出典にできない件（11 第4節 #55 の指示）をどうするか
- 「なぜ（人の側の仕組み）」は独立の節にせず、既存 sections の中に短く入れた。分けたほうがよければ節の追加を判断してほしい

## 提案
- front matter の直しの提案はなし
- 用語集・prh への提案：なし

## 検査の結果
- 書き終えた後：エラー 0・警告 4（no-doubled-joshi 3、arabic-kanji-numbers 1）
- 直した後：エラー 0・警告 1（62 行目「が」の重複。「…良く見えても、実行後に価値が目減りすることがある」で、検査は 2 度目の「が」を拾った。誤検出ぎみで、意味を変えないため残した）

## 確かめていないこと
- qiita-kmat67916008-73e303 と -7aaa41 のどちらの記事に「いつもやること／そのコンペだからやること」があるかは確かめていない（束は p12#125 の要約のみ）。両方を sources に入れた
- Si らの実験で使われたモデルと世代は束にないため書かなかった。本文は「NLP 分野の研究」「当時の」とも書かずに結果だけを述べている
- Zenn の事例（Kaggle 金メダル）の記述は 10 第6章の要約に基づく。原記事は開いていない
- AHC072 のまとめサイト経由の声は、11 #54 に従い使っていない
- 数値は研究結果の固定の記録として書いた（facts の提案なし）

## 使用量
- 道具の呼び出し：約 14 回（Read 2、Bash 8、Write 2、check_page 2 回を含む）。Web の取得：0（check_noai の確認 2 回のみ）
