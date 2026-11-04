# write.md：verification-ladder（執筆）

## 書いたファイル
- `docs/verify/verification-ladder.md`（stub から移した。front matter の変更：`sections` に what-it-prevents・misconceptions を足した、`sources` に 5 件〔既存の id〕、`stage` を draft、`updated` を 2026-11-05）
- `snippets/verification-ladder/give-a-check.md`・`give-a-check.expect.yaml`（prompt。確かめる手段と終わりの条件を渡す依頼）
- `docs/img/verification-ladder/four-steps.svg`（四段の図）
- `data/sources.d/` は作っていない（使った出典はすべて data/sources.yml にある）

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle・prevents・pitfalls の名指し）：`#what-it-prevents`（「確かめる」「縛る」と、原因「確かめていない」「縛っていない」を名指し。pitfalls は空なので書かない）
- level を持つ（任せる）：front matter。要点の最初は「何が分かるか」（冒頭の囲み）
- 構成の目安（技法寄り）：要点 → `#four-steps` → 頼み方の例 Before/After は `#verbal-checks` → 何が変わるか（同節の After の注記）→ なぜ効くか・効かない場面は `#what-it-prevents` → 誤解は `#misconceptions` → 関連はテンプレート。`#choose-step` に選び方と判断例

## メインに判断してほしいこと
- 目次の図の案は「上るほどお願いから鍵に近づく」だが、段 2（/goal）は判定がモデルで、段 4 は別の目なので、鍵に近づく一本の軸にならない。図は段ごとに「お願い・モデルが判定・鍵・別の目」と書き分けた
- モデルの名前（Opus 5 など）は変わりやすい値なので本文に書かず、台帳 `outdated-advice-ledger#add-double-check` と `model-quirks#official-guidance` を指した

## 提案
- なし（front matter の他のキー、用語集、data への提案はない）。`/goal` の条件の字数上限は束の data にないため書かず、goal-until-done 側に任せた

## 検査の結果
- `check_page.py verification-ladder`：1 回目 エラー 2・警告 2（subagent の表記、「四つ」、助詞の連続）を直し、2 回目 エラー 0・警告 0

## 確かめていないこと
- 雛形 give-a-check の動作（動作確認はしていない。expect は観察の形で書いた）
- Best practices の 4 段階は束の調査資料（2026-11-03 確認）に基づき、原文は開いていない。本文の「2026-11-03 に確かめた版」は手書きの日付
- WSL・Linux 以外の OS と IDE 拡張での動作は書いていない（未確認）
- 用語集の語の初出リンクは付けていない（用語集を読んでいない）

## 使用量
- 道具の呼び出し：約 12 回、Web の取得：0 回
