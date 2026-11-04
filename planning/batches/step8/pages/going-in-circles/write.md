# write.md：going-in-circles

## 書いたファイル
- docs/symptoms/going-in-circles.md（stubs から mv。stage を draft、updated を 2026-11-05、sections に forms・choose・routes・examples・prevention を追加、sources に cc-docs-best-practices と anthropic-research-code-expertise を設定）
- snippets/going-in-circles/restart-prompt.md と restart-prompt.expect.yaml（目次の templates は「なし」。分かりやすさのため 1 つ足した）
- planning/batches/step8/pages/going-in-circles/facts-proposal.yml

## 必ず持つものの対応
- 診断のチェックリスト（六つの原因を安く確かめる順。人の側の落とし穴を含む）：`#diagnosis`（見えていない・散らかっている・確かめていないの順、後に やめられない）
- 原因ごとの振り分け先（routes）：`#routes`（gen の routes の目印。front matter の routes は変えていない）
- 構成の目安の「よくある形」：`#forms`、「判断例」：`#examples`、「予防（仕組みに移す）」：`#prevention`
- 要点・導入：冒頭の囲み。前提は context-rot

## メインに判断してほしいこと
- 訂正の回数の目安（公式は 2 回）を、数値の提案にした。採用なら `#choose` の「さらに訂正を足さないよう勧める」の後に fact の目印を置く文へ直す（本文には数字を書いていない）
- 確認日付きの記述として「公式の Best practices（2026-11-05 に確認）」と書いた。確認は WebFetch 1 回（best-practices の /clear の節）

## 提案
- data/facts.yml：facts-proposal.yml のとおり（best-practices-clear-after-failed-corrections）

## 検査の結果
- 1 回目：エラー 0・警告 8。直した後の 2 回目：エラー 0・警告 2
- 残した警告：148 行（判断例の「理由」）の助詞「が」の重複、164 行（予防の箇条）の助詞「に」の重複。どちらも読みにくくはないと判断して残した（2 回の検査を使い切ったため）

## 確かめていないこと
- 雛形 restart-prompt の動作（expect は観察の記録）
- 経験談（処理の流れを説明させた例）は束の写しのみで、一次の記事は開いていない（根拠：弱と明記）
- Defects4J の幻覚の研究の数値は未確認のため本文に使っていない
- アプリでの巻き戻しの手順は rewind-dont-correct#how に任せ、ここでは確かめていない
- 本文は WSL・Linux の CLI 基準で、他の OS と IDE 拡張の動作は確かめていない

## 使用量
- 道具の呼び出し：約 14 回、Web の取得：1 回
