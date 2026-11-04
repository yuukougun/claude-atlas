# write.md：insights-and-usage-review（執筆）

## 書いたファイル

- docs/eval/insights-and-usage-review.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に cc-docs-costs・cc-docs-commands を足した）
- sections を 5 つ足した（when・minimal・pitfalls・compare・outdated）。既にある 2 つの anchor は変えていない
- snippets/insights-and-usage-review/ の triage-insights-report と list-cut-candidates（各 .md と .expect.yaml）

## 必ず持つものの対応

- 機能の属性のバッジ：テンプレートが出す（本文には書かない）。比べる相手の節 `#compare` に `compare` の目印（既定の列）を置いた
- `tracks`：front matter に [insights, usage] がある。本文では `#minimal`（2 つの道具の使い方）と `#compare` が指す
- 構成の目安：使いどころ `#when` → 最小の使い方 `#minimal` → 雛形 `#insights-as-drafts` と `#usage-breakdown` の末尾 → 効かない場面・落とし穴 `#pitfalls` → 比べる相手 `#compare` → 古くなった助言 `#outdated`
- 強制力：data の features に属性がないため目印が使えない。要点に「なし」と文で書いた（下の判断を参照）
- 面のタブ：surfaces が claude-code だけなので置かず、`#minimal` に Claude Code の機能と書いた
- level：front matter の「任せる」のまま

## メインに判断してほしいこと

- data の features（insights・usage）に強制力がない。「なし」を足せば、要点の文を `feature enforcement` の目印にできる。足すかの判断をお願いしたい
- 要点の強制力の行は手書きの「なし」。`/usage` の推奨を自動で適用する操作がある版もあり（01 M）、見るだけの間は「なし」と書いた。適用の操作は版の数値を書かず「用意されている版もある」とだけ書いた

## 提案

```yaml
frontmatter: []
```

- 用語集・prh・data の提案はなし

## 検査の結果

- check_page.py：1 回目 エラー 0・警告 9（助詞の重複・文の長さ）→ 直した後 エラー 0・警告 0

## 確かめていないこと

- コマンドの実際の動作（`/insights` の報告の出る場所と形、`/usage` の推奨の自動適用の操作）は実機で確かめていない。出典は束の写し（costs・commands を引く調査資料）だけ
- 月に 1 回ほどの目安（p56#95）は、根拠：弱として書いた。出典の元の確認はしていない
- 「記録に出ない摩擦は見えない」「分析は見落としも誇張もありうる」は推論で、そう印を付けた
- 雛形 2 つは動作を試していない
- `outdated-advice-ledger#slash-cost-and-stats` の節が実在するかは check_page の通過のみで確認した
- アプリ・API・ほかの OS と IDE 拡張での動作は未確認（本文にもそう書いた）

## 使用量

- 道具の呼び出し：約 12 回。Web の取得：0 回
