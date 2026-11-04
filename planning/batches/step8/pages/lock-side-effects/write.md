# write.md：lock-side-effects

## 書いたファイル
- `docs/enforce/lock-side-effects.md`（stubs から mv。stage を draft。front matter の変更：`sections` に what-happens・why・effects・misconceptions を足した。`sources` に cc-docs-hooks-guide・cc-docs-permissions。`updated` 2026-11-05）
- `snippets/lock-side-effects/block-and-log.py` と `.expect.yaml`（強制上書きの push だけを止め、理由と代わりを返し、記録を残すフック）
- `snippets/lock-side-effects/review-blocks.md` と `.expect.yaml`（止めた記録を規則ごとに見直させる依頼）

## 必ず持つものの対応
- どの原理に関わるか（`principle`：縛る・握る）：`#effects`（「縛る」「握る」を定義して名指し）
- どの原因に関わるか（`prevents`・`pitfalls`）：空のため名指す原因はない。`#effects` で「特定の原因を防ぐページではなく、運用の副作用を扱う」と書き、症状ページ 3 つへつないだ
- 構成の目安（何が起きるか → なぜ → 何に効くか → 誤解 → 関連）：`#what-happens`・`#why`・`#effects`・`#misconceptions`・関連（テンプレート）。間に目次の 3 節（`#what-to-lock`・`#reason-and-alternative`・`#review-blocks`）
- level（仕組みにする）を持つ・要点の最初が「何が分かるか」：冒頭の要点

## メインに判断してほしいこと
- `prevents`・`pitfalls` が空。縛りすぎで起きやすい原因の名前を割り当てるかは、メインの判断
- 注釈付きのセッション記録（目次の見せ方 DR-17）は未作成。束に `state/blocks.log` の中身がないため、仮の記録を作らず、判断例（想定の例と明記）と記録 1 行の雛形で代えた。実際の記録から選んだ例を足すなら、メインが材料を渡す

## 提案
```yaml
glossary:
  - {term: 縛る, note: "規則を鍵（フックと権限ルール）に移すこと。本文 #effects で短く定義した。用語集にあるか未確認"}
  - {term: 握る, note: "何を任せ、何を人が決めるかを人が持つこと。同上"}
```
- 用語「回り込み」「止めすぎ」を用語集に足す案（本文で短く定義済み）

## 検査の結果
- 1 回目：エラー 1（prh：sandbox → サンドボックス）・警告 2。直して 2 回目：エラー 0・警告 1
- 残した警告：no-doubled-joshi「か」（「メインか担当か」の並列。誤検出と判断）

## 確かめていないこと
- 雛形のフック（`block-and-log.py`）は動かしていない。正規表現と `agent_id` の扱いは未検証
- 「縛る」「握る」の定義が用語集と合うか
- 束の材料（research/28・05）に基づく記述（`WebFetch` の拒否が `curl` に効かないこと、matcher の照合、事実の形で書く勧め、記録は `PreToolUse` で取る）は一次資料を開いていない
- 回り込みの頻度は研究がなく、本文で推論・弱い根拠と書いた

## 使用量
- 道具の呼び出し：約 12 回。Web の取得：0 回
