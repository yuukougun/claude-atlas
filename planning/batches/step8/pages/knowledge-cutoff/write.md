# write.md：knowledge-cutoff（concept・basics）

## 書いたファイル
- docs/basics/knowledge-cutoff.md（stubs から mv。stage を draft、updated を 2026-11-05、sections を 4 節、sources を 6 件に）
- 雛形・図・data/sources.d は置かない（出典は既存の id だけで足りた。目次の templates と visual も「なし」）

## 必ず持つものの対応
- 冒頭の要点（最初の項目は「何が分かるか」）：abstract 囲み（level は使う）
- どの原理・原因に関わるか：`#what-helps`（principle「見せる」・prevents「見えていない」を名指し。pitfalls は front matter に無いので該当なし）
- 何が起きるか（例）：`#what-happens`
- なぜそうなるか：`#why`（図はなし。比喩も使わず、学習の終わりと日付が外にあることの 2 点で説明）
- 誤解：`#misconceptions`
- 関連：テンプレートが出す（page-links）

## メインに判断してほしいこと
- 「なぜ」の節に図（比喩付き）を置かなかった。目次の visual が「なし」で、cutoff には手持ちの比喩の一覧に合うものがないため。必要なら図の案を足す
- 面のタブの Claude Code は、材料の束に根拠がないので「日付を渡しているかは確かめていない」と書いた。調べる担当がいれば埋めたい

## 提案
```yaml
proposals:
  - fact: {id: model-knowledge-cutoffs, title: モデルごとの reliable knowledge cutoff と training data cutoff（別々の欄で持つ）, value: "現行のモデルは両方とも 2026年6月（research/26 #12・§3.7）。古いモデルは差がある（例：Opus 4.6 は reliable が 2025年5月、training が 2025年8月）。モデルごとの表にする", sources: [api-docs-models-overview, hc-up-date-training-data], checked: 2026-11-05, status: 要確認}
    used_in: [knowledge-cutoff#why]
```
- 本文は日付なしで読める形にした。fact の id が data に入ったら、`#why` の「各モデルの日付は…載っている」の所に `fact-table` か `fact` の目印を置ける
- 用語集に reliable knowledge cutoff・training data cutoff を足す案（本文では表で短く定義した）

## 検査の結果
- 1 回目：エラー 0・警告 3（arabic-kanji-numbers「二つ」、no-doubled-joshi 2 件）
- 直した後：エラー 0・警告 1。残りは `#why` 末尾の文の「に」の重複で、link の目印の間に入る題名（「…得になる訓練」）の「に」を数えたもの。直す回数を使い切ったので残した

## 確かめていないこと
- 面ごとの日付の渡され方（アプリ・Claude Code が会話に日付を入れるか）は束になく、確かめていない
- アプリの web 検索が「最新の情報が要る質問で自動で検索する」挙動は、data の note（要るときに Claude が検索する）に基づく。日本語版の画面は未確認
- 「公式のモデル別の指針」3 つ（日付を渡す・検索で確かめる・名前を知っていても現状は別）は束の 6.4 の写しによる。原文は開いていない
- 「新しいモデルでも空白がある」「自己申告は推測を含む」は一般的な性質として書いた。出典の裏づけは束の範囲にない
- ページの描画の見た目は見ていない

## 使用量
- 道具の呼び出し 13 回ほど（Read 3、Bash 6、Write 2、Edit 0）・Web の取得 0 回
