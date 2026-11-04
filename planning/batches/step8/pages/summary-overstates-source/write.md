# write.md（執筆の担当の返答から、メインが道具で写した。担当はページと報告の Write を止められた）

## 書いたファイル
- 書けたもの（Write は成功）：
  - `snippets/summary-overstates-source/check-against-source.txt`
  - `snippets/summary-overstates-source/check-against-source.expect.yaml`
  - `snippets/summary-overstates-source/summary-keeps-conditions.txt`
  - `snippets/summary-overstates-source/summary-keeps-conditions.expect.yaml`
- 書けなかったもの：`docs/symptoms/summary-overstates-source.md`。stub から `mv` して stage を draft に直す予定だった。全文は次の節に置く。
- 前提：数値の提案はない。`data/sources.d/summary-overstates-source.yml` も作っていない。本文は出典を使っておらず、`sources: []` のままにしてある。
- front matter で変える予定だったキー：
  - `sections`：forms・example・prevention の 3 節を足す。`diagnosis` はそのまま残す。
  - `stage`：stub を draft にする。
  - `updated`：2026-11-05 にする。

## 必ず持つものの対応
- 診断のチェックリスト：`#diagnosis`。「見えていない」→「確かめていない」→ 人の側の落とし穴、の順に並べた。
- 人の側の落とし穴：`#diagnosis` の項目 3。
- 原因ごとの振り分け先（`routes`）：`#diagnosis` の末尾に routes の目印を置いた。
- 構成の目安：
  - 要点は冒頭に置いた。
  - よくある形は `#forms`。
  - 判断例は `#example`。
  - 予防は `#prevention`。
  - 持たないもの：なし。

## メインに判断してほしいこと
- ページの Write が道具に止められた。同じ止まり方が他のページでも出るなら、道具か deny の側の問題かもしれない。
- 下の全文をそのまま `docs/symptoms/summary-overstates-source.md` に置いてよいか。

## 提案
- front matter の直しの提案はない。
- 用語集・prh への提案もない。

## 検査の結果
- `check_page.py` は未実行。書けなかったため、エラー数も警告数も分からない。

## 確かめていないこと
- 全文のリンクの目印が束の「指せる節」と合うかは、道具で通していない。目で束と突き合わせただけだ。
- textlint の指摘は未確認。特に文字数と、「！！！」の中の入れ子の箇条を「。」で終えているかが心配だ。
- 雛形 2 つの expect と control は、動作を確かめていない書き手の予想である。「簡潔に要約して」とだけ頼むと限定が落ちる、という記述は特にそうだ。
- 判断例の「論文の要旨は『一部の条件で効果が見られた』と書いているように思える」は、架空の状況である。
- 順序は「見えていない」→「確かめていない」とした。`site.yml` の並びは見ていない。

## 使用量
- 道具の呼び出しは 11 回で、そのうち Write の失敗が 2 回。Web の取得は 0 回。
