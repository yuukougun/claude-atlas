# give-reasons 執筆報告

## 書いたファイル
- docs/prompting/give-reasons.md（stubs から mv。stage を draft、updated を 2026-11-05、sources を [api-docs-prompting-best-practices]、sections に what-changes・why・templates・limits を足した）
- snippets/give-reasons/request-with-reason.txt と .expect.yaml、claude-md-rule.md と .expect.yaml
- data/sources.d は不要（出典は data/sources.yml に既にある id のみ）

## 必ず持つものの対応
- 原理「見せる」・原因「見えていない」の名指し：#why（pitfalls は front matter に無いので本文でも扱わない）
- 要点の最初が「何が分かるか」：冒頭の要点の囲み
- 技法の構成（Before/After → 何が変わるか → なぜ効くか → 効かない場面）：#tts-example → #what-changes → #why → #claude-md → #templates → #limits

## 提案
- front matter：sources に cc-docs-best-practices を入れていない（本文で使わなかったため）。束の出典一覧にあるので、足すかはメインの判断。

## メインに判断してほしいこと
- 「なぜ効くか」の内部の仕組みは公式にも無いので（推論・実践例なし）と明記した。この扱いでよいか。
- 判断例の「ですます調」の効果と「本番 DB」の例は、筆者が作った想定の例（公式の例は読み上げのみ）。

## 検査の結果
- 1 回目：エラー 0・警告 1（が の連続）→ 直した。2 回目：エラー 0・警告 0

## 確かめていないこと
- 雛形 2 つの動作（実機で未試験）。読み上げ以外の記号に理由が及ぶかは公式の例にも無く、確かめていない。
- 公式の指針の原文は開いていない（束の写しのみに基づく）。

## 使用量
- 道具の呼び出し 約 9 回、Web の取得 0 回
