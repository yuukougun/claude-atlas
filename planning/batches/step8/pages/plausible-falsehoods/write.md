# write.md：plausible-falsehoods

## 書いたファイル
- docs/symptoms/plausible-falsehoods.md（stubs から mv。stage を draft に、updated を 2026-11-05 に、sources に api-docs-reduce-hallucinations を、sections に forms・to-fixes・examples・prevent を足した。diagnosis は変えず）
- 雛形・図・data/sources.d は無し（目次の templates が無く、出典は既存の id だけで足りた）

## 必ず持つものの対応
- 診断のチェックリスト（六つの原因を安く確かめる順。人の側の落とし穴）：#diagnosis（Claude 側は prevents の 2 原因を 5 項目で、人の側は末尾の段落で「同意を根拠に数えない」を疑う）
- 原因ごとの振り分け先（routes）：#to-fixes（gen:begin routes）
- 型の構成の目安：要点（冒頭）→ #forms → #diagnosis → #to-fixes → #examples → #prevent

## メインに判断してほしいこと
- sections に 4 節を足した（forms・to-fixes・examples・prevent）。routes の目印は、stub では diagnosis の中だったが、to-fixes に分けた
- 「Claude Code」タブは、束に claude-code の根拠がないため、手元のファイルを読ませて引用させるという一般的な書き方にとどめた。確かめが要れば指示がほしい
- 判断例 2 つ目の「揃った場合も原文で確かめるまで採用しない」は、固有の出典がなく筆者の推論。fact-checking#best-of-n の持ち主ページと食い違わないか確かめてほしい

## 提案
- なし（数値は本文に書いていない）

## 検査の結果
- 1 回目：エラー 0・警告 3。直した後：エラー 0・警告 1
- 残した警告：no-doubled-joshi（「に」）が「予防」の 1 つ目の箇条に出る。原因は link の目印で生成される行き先の題名（「分からない」と言ってよいと伝える › …）で、手では直せない誤検出と見ている

## 確かめていないこと
- 行き先ページ（準備中のもの）の本文との内容の食い違い
- outdated-advice-ledger#lower-temperature と nondeterminism#temperature-advice の表示（check の参照検査は通った）
- 一次資料は開いていない。本文の事実は束の材料（reduce-hallucinations の要約）だけに基づく。TechCrunch の訴訟の例は、第三者を名指しするため使っていない

## 使用量
- 道具の呼び出し：読み 2、Bash 5、Write 2（ページ・本文の再生成後は Bash で一部直し）、検査 2。Web の取得 0
