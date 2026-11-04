# write.md：insists-on-mistakes

## 書いたファイル
- `docs/symptoms/insists-on-mistakes.md`（stubs から mv。front matter は sections〔5 節を足した〕・sources・stage draft・updated 2026-11-05 を変更）
- `snippets/insists-on-mistakes/show-evidence.md`・`show-evidence.expect.yaml`（目次の templates は「なし」。分かりやすさのために足した prompt の雛形）
- `data/sources.d/` は作っていない（出典は data/sources.yml に既にある 2 件だけを使った）

## 必ず持つものの対応
- 診断のチェックリスト（六つの原因を安く確かめる順。人の側の落とし穴を含む）：`#diagnosis`（`prevents` の 3 つ。人の側は同節の末尾の段落）
- 原因ごとの振り分け先（`routes`）：`#routes`（routes の目印）
- 構成の目安の「よくある形」：`#forms`／判断例：`#examples`／予防：`#prevent`
- 追加：実物を見せる頼み方の雛形：`#show-evidence`

## メインに判断してほしいこと
- 事例（存在しないバグを擁護し、履歴の検索で撤回）は、他社のモデルの単独の経験談なので、モデル名を出さず「根拠：弱」にした。lukyanenko-kaggle-antigravity-s6e7 の「The bug that never existed」の節を WebFetch で確かめた（書き手が実際の行を見せ、エージェントが履歴を検索して誤記がなかったと確認）。出典は sources に入れたが、本文に書き手の名は出していない。
- 「人の側の落とし穴」は、束に五つの中身がなく、six-causes#human-side を指すだけにして、本文に「違うとだけ返すと手がかりがない」を（推論・実践例なし）で 1 つ置いた。多すぎれば削ってよい。

## 提案
- 数値の提案、front matter の提案、用語集・prh への提案は、なし。

## 検査の結果
- 1 回目：エラー 0・警告 1（no-doubled-joshi、が の重なり）→ 文を直した。2 回目：エラー 0・警告 0。

## 確かめていないこと
- cc-issue-46940 の内容（失敗が残るのに分母を変えて全部通過と報告）は、束の調査資料の写しによる。issue の原文は開いていない（数値は本文に書かなかった）。
- 判断例は、この辞典の作例で、実機では試していない。雛形の expect は動作を確かめていない。
- Claude Code 以外の面（app）での手順の違いは書いていない（タブは使わなかった）。IDE 拡張・他の OS の動作は未確認。
- 生成された routes の表・雛形の描画は目で見ていない（check_page.py の通過のみ）。

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：1 回。
