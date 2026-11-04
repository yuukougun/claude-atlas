`expenses/inbox/receipts/` の領収書（画像と PDF）と `expenses/inbox/statement.csv`（カードの明細）から、今月の経費の一覧を作ってほしい。

- `expenses/out/expenses-YYYY-MM.csv` に、日付・店名・金額・区分・領収書のファイル名・明細との照合（一致・明細なし・領収書なし）の列で出す。
- 区分は `expenses/categories.md` の区分表から選ぶ。当てはまらないものは「要確認」にする。
- 読み取りに自信がない値は、推測で埋めずに空にして、備考に理由を書く。
- 合計は暗算せず、スクリプト（`expenses/out/sum_check.py`）で計算し、明細の合計と並べて報告する。
- 氏名と口座の情報は、`inbox/` に置く前に伏せてある。伏せた箇所を推測で復元しない。
