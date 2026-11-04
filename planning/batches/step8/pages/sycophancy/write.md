# write.md：sycophancy（迎合）

## 書いたファイル
- `docs/basics/sycophancy.md`（stubs から移した。stage を draft、updated を 2026-11-05、sections を 4 節、sources を 8 件にした。ほかのキーは変えていない）
- `docs/img/sycophancy/why-agree.svg`（迎合が生まれる流れの図）
- 雛形・`data/sources.d` はなし（目次の templates は「なし」。sources は既存の id だけ）

## 必ず持つものの対応
- 冒頭の要点（最初の項目は「何が分かるか」）：冒頭の囲み
- 原理 `principle: 確かめる`：#effects（「確かめる（原理）」）
- 原因 `prevents: 確かめていない`：#effects（「確かめていない（Claude 側の原因）」）
- 落とし穴 `pitfalls: 同意を根拠にする`：#effects（「同意を根拠にする（人の側の落とし穴）」）
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：#what-happens・#why・#effects・#misconceptions。関連はテンプレートの page-links
- 図：#why（比喩は使っていない。一覧の比喩に合うものがなく、規範の節だけ「お願い」で request-vs-lock を指した）

## メインに判断してほしいこと
- 研究の数値（49%・N=2405 は Science 公刊版）の出典に arxiv-2510-01395 を使ったが、これは査読前の版（実験 2 本・N=1604・「50%」）。公刊版の出典を sources に足すか。
- Constitution の「外交的に誠実であれ」は束の日本語の写しに基づく趣旨の記述。原文の確認はしていない。

## 提案
- sources の追加（任意）：Cheng ほか Science 2026-03-26 の公刊版
- 本文は変わりやすい値を使っていない。facts-proposal はなし

## 検査の結果
- 書いた後：エラー 0・警告 2。直した後：エラー 0・警告 1
- 残した警告：46 行目の「が」の重複（no-doubled-joshi）。1 文に主語と対象の「が」が入る。直しの検査を使い切ったので残した

## 確かめていないこと
- Web を開いていない。研究の数値は束の写し（11 と research/24）のまま。SycEval の数値は 24 の B-44 で確認済みの範囲
- Kim と Khashabi の主張は要旨の範囲。Truth Decay の旧世代 Claude Haiku という書き方は束の記述のまま
- 「確信を込めて押すほど折れやすい」は束の実践の指摘で、根拠：弱と付けた
- 「この傾向が無いと確かめた研究は材料に見つかっていない」は、束の範囲だけで言っている

## 使用量
- 道具の呼び出し：約 14 回（Read 2・Bash 7・Write 3 ほか）。Web の取得：0
