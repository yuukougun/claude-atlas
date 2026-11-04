# experiment-log 執筆報告

## 書いたファイル
- docs/eval/experiment-log.md（stubs から mv。stage: draft、updated: 2026-11-05。front matter は sections に3節〔not-progress-file・check・when-it-fails〕を足し、sources に既存の id を6件入れた）
- snippets/experiment-log/ledger-entry.md・.expect.yaml（目次の templates 案：実験台帳の1件分。閾値・回数は例と明記）
- snippets/experiment-log/ask-to-log.md・.expect.yaml（足した雛形：実行前の欄だけを埋めさせる依頼）
- data/sources.d/experiment-log.yml は書いていない（sources の id は data/sources.yml に全部あった）

## メインに判断してほしいこと
- 雛形は Write ではなく Bash の heredoc で書いた（内容は同じ）。
- 提案者ごとの当たりの率の比較は「（推論・実践例なし）」を付け、採否の基準にしないと書いた（目次 notes の指示）。

## 提案
- 数値の提案なし。本文に変わりやすい数値は書かず、Fishtest の再挑戦の上限は「おおむね数回」とした（4〜5回を fact にするなら proposals が要る）。
- front matter の変更提案なし。

## 検査の結果
- 1回目：エラー0・警告5。直して2回目：エラー0・警告2。
- 残した警告：no-doubled-joshi（「に」の重複）が2件（122行・159行付近）。読みにくさは小さいと判断した。

## 確かめていないこと
- 雛形（台帳・依頼）は動かしていない。EXP-014 の数値（400 ケース、4 回など）は例で、実測ではない。
- 事実の中身は束の写しに基づき、一次資料は開いていない（Web の取得 0 回）。Fishtest・infrastructure-noise・Kaggle 事例・研究ノートの勧めは束の要約からの記述。
- 「重複をClaudeに調べさせると名前違いを見落とす」「commit 履歴で後付けを確かめる」は実務上の助言で、出典はない。
- 分かりやすさ・事実の検証は未実施。

## 使用量
- 道具の呼び出し：約12回（読み3、Bash 6、Write 1、check 2）。Web の取得：0回。
