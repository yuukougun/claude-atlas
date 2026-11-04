# write.md：parallel-fatigue

## 書いたファイル
- docs/symptoms/parallel-fatigue.md（stubs から移動。stage を draft、updated を 2026-11-05、sections に forms・example・prevention を追加。diagnosis の anchor は変えず）
- 雛形・図・data/sources.d は無し（目次の templates・visual が空。新しい出典なし。sources は [] のまま）

## 必ず持つものの対応
- 要点の囲み：冒頭（最初の `##` の前）
- 診断のチェックリスト（原因を安く確かめる順。人の側の落とし穴も）：#diagnosis（確かめていない→合っていない→預けすぎる→体感を信じる）
- 原因ごとの振り分け先（routes）：#diagnosis の末尾の `routes` の目印
- よくある形（読者の言葉）：#forms
- 判断例：#example
- 予防（仕組みに移す）：#prevention

## メインに判断してほしいこと
- 診断の並びは front matter の prevents → pitfalls の順にした。site.yml の六つの原因の並びとの突き合わせはしていない
- 並列の疲労の数値は、目次の notes（research/21 P7）に従い使わなかった。研究・事例の数値も入れず、持ち主のページ（review-bottlenecks など）に任せた

## 提案
- なし

## 検査の結果
- check_page.py 1 回目：エラー 1・警告 5（前提の書き方、助詞の重複、「六つ」）。直して 2 回目：エラー 0・警告 0

## 確かめていないこと
- link 先の各ページの本文（未公開のものがある）。書いた紹介文が相手の中身と合うかは、束の要約だけで判断した
- `outdated-advice-ledger#tmux-agent-orgs` は束の「指せる節」にないが、カード §11 の指示に従って指した（道具の検査は通った）
- tmux の古い助言に対する「今の置き換え先」は台帳に任せ、本文では成熟度や版を書いていない
- 判断例は仮の状況であり、実測ではない

## 使用量
- 道具の呼び出し：約 8 回、Web の取得：0 回
