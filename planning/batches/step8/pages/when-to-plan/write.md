# when-to-plan 執筆の報告

## 書いたファイル
- docs/cli/when-to-plan.md（stubs から mv。stage: draft、updated: 2026-11-05）
- front matter で変えたキー：`sections`（how-to・limits・compare の 3 節を足した。既存の when・review・after-approval の anchor はそのまま）、`sources`（[cc-docs-permission-modes, cc-docs-context-window]。どちらも data/sources.yml にある id）、`stage`、`updated`
- snippets/when-to-plan/ask-for-plan.md と ask-for-plan.expect.yaml（計画だけを頼む依頼。kind: prompt）
- data/sources.d/when-to-plan.yml は作っていない（出典は既存の id だけ）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力）：冒頭の要点の「強制力」（`feature enforcement` の目印）。ほかの属性は本文に手で書かず、テンプレートのバッジに任せた
- `tracks`（plan-mode）：front matter の tracks にある。節は特に持たない
- level：front matter（整える）
- 構成の目安：使いどころ `#when`（防ぐ原因は「見えていない」を名指し）／最小の使い方 `#how-to`（雛形 ask-for-plan を含む）／計画の読み方と直し方 `#review`／計画を承認した後 `#after-approval`／効かない場面・落とし穴 `#limits`／比べる相手 `#compare`
- 面のタブ：持たない（surfaces が claude-code だけのため）
- 古くなった助言：持たない（outdated_advice が空で、台帳の行がない）

## メインに判断してほしいこと
- 「diff を一文で説明できるなら計画を省いてよい」は、本文で「公式の文書では確かめられていない、この辞典の経験則」と明記して使った。現行の Best practices を取得して確かめたが、plan mode にもこの文にも触れる箇所がなかった（束の notes のとおり）。不要なら `#when` の該当の段落を削る
- 計画の承認後の選択肢の表示文（`Yes, and use auto mode` など）を原文のまま載せた（permission-modes、確認日 2026-11-04）。版や設定で変わるので「文言は版や設定で変わる」と添えた

## 提案
```yaml
frontmatter: []
```
- 用語集・prh への提案はなし。ただし「bypass permissions」が prh で「権限」への置き換えに当たるため、本文では `bypassPermissions`（コードの書式）で書いた。ページの別の箇所で「bypass permissions」を平文で書く場合の扱いを、用語集で決めてほしい
- 数値の提案はなし（facts-proposal.yml は作っていない）

## 検査の結果
- `check_page.py` を 4 回流した：1 回目（エラー 6・警告 9）、2 回目（直しの script が途中で止まったのに検査が続けて流れた。直し前と同じ）、3 回目（エラー 1・警告 4）、4 回目（最終：エラー 0・警告 1）。決まりの 2 回を超えた
- 残した警告：`no-doubled-joshi`（助詞「に」の重複。106 行目の link の題名が間に入る文で、題名は道具が書くため直しにくい。文として読めるので残した）

## 確かめていないこと
- VS Code の拡張での計画のレビュー（Markdown の文書で開く・行コメント）は research/26 の写しに基づく。動作は試していない。版の条件は本文に書かず、using-ides を指した
- 直接編集（`Ctrl+G`）した計画が Claude にどう伝わるかは確かめていない（本文にその旨を書いた）
- `showClearContextOnPlanAccept` で承認した後に、計画の中身が実装側へどう渡るかは確かめていない（本文にその旨を書いた）
- 圧縮の後に plan mode の計画がディスクから入れ直されることは、束の写し（research/23）と data の note による。入った版は書いていない
- 調べのシェルのコマンドの確認の出方（auto モードが使えるか・`useAutoModeDuringPlan` で変わる）は、permission-modes の取得の文面による。本文は権限モードのページへ回した
- 判断例 2 つは、この辞典の作例（実在の事例ではない）
- WSL・Linux 以外の OS と IDE 拡張の動作は未確認

## 使用量
- 道具の呼び出し：約 16 回。Web の取得：2 回（best-practices、permission-modes）
- 作業中に、検査の流す回数が決まりの 2 回を超えた（上の「検査の結果」のとおり）
