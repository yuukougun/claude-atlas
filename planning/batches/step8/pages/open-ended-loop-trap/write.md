# write.md：open-ended-loop-trap（concept・delegate）

## 書いたファイル
- docs/delegate/open-ended-loop-trap.md（stubs から mv）。front matter：stage を draft、updated を 2026-11-05、sections に why・what-it-affects・misconceptions の 3 節を足した（既存の 2 節は変えず）
- 雛形・図・出典ファイルは作っていない（目次の templates はなし。図の案は対比の表で代えた。sources は [] のまま）

## 必ず持つものの対応
- 用途（なぜそうなるか）：#why（選択圧の仕組みへ）・#closed-vs-open（違い）
- 冒頭の要点のほかに、principle・prevents・pitfalls を本文で名指して結び付ける：#what-it-affects（握る・確かめる／確かめていない／やめられない・体感を信じる）
- level あり・要点の最初は「何が分かるか」：冒頭の囲みの 1 項目め
- 構成の目安（原理・仕組み）：要点 → 何が起きるか（#closed-vs-open の判断例、#longer-is-not-better の事例）→ なぜ（#why）→ 何に効くか（#what-it-affects）→ 誤解（#misconceptions）→ 関連（テンプレートが出す）
- 比喩付きの図：置いていない。同じ仕組みの比喩の一覧に合うものがなく、図の案（対比）は #closed-vs-open の表で代えた

## メインに判断してほしいこと
- 研究の事例（頭打ち・CTF・ISUCON・DrivenData）は、束の写しだけに基づく。出典が sources にないので、本文では実験名・数値（CTF の問数や順位など）を省き、DrivenData の「9 日間・12 位から 7 位」だけ載せた。一次資料を足して sources に載せるか、載せずに残すかを決めてほしい
- 根拠の印：調査資料では頭打ちの実験が「強（単独の実験）」だが、カード §6 の定義（RCT・大規模）に合わせて（根拠：中）にした
- 図：対比の表で代えた。SVG の図が要るなら別の担当で

## 提案
```yaml
frontmatter:
  - {id: open-ended-loop-trap, key: sources, before: [], after: [（頭打ちの実験・DrivenData・ISUCON の一次資料）], reason: "事例の根拠を sources に載せるため。出典の id は一次資料を確かめてから"}
```

## 検査の結果
- check_page.py を 2 回流した（書き終えた後・直した後）。エラー 0。警告 2 が残る：82 行目（「が」の重なり）、96 行目（link の題名が長く、「に」が重なると数えられる誤検出に近い）。直すと文の意味が崩れるか、link の題名が原因なので残した

## 確かめていないこと
- 事例の対象のモデル・版・年（資料の写しにない）
- 自己リンク（#misconceptions の open-ended-loop-trap#longer-is-not-better）が意図どおりに生成されたか
- 事例の数値と順位の正しさ（束の写しのみ）

## 使用量
- 道具の呼び出し 11 回前後。Web の取得 0 回
