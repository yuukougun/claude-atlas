# felt-vs-measured 執筆報告

## 書いたファイル
- docs/eval/felt-vs-measured.md（stubs から mv。stage: draft、updated: 2026-11-05）
- snippets/felt-vs-measured/effect-log.md と effect-log.expect.yaml（kind: other）
- docs/img/felt-vs-measured/gap.svg（予想・体感・実測の図。400x230）
- front matter で変えたキー：sections（`what-you-keep`「人が握るもの」を `why` と `what-to-record` の間に追加）、sources（既存の 4 件）、stage、updated。data/sources.d は足していない（出典は全部 data/sources.yml にある）

## 必ず持つものの対応
- 冒頭の要点：先頭の `!!!` の要点（根拠の強さの項を足した）
- 判断例（状況・迷う候補・選んだもの・理由）：`#what-you-keep`（節の中の `!!! example`）
- level：front matter の `level: 整える`
- 構成の目安（要点→何が起きるか→なぜ→判断例→握るもの→確かめ方）：`#evidence`→`#why`→`#what-you-keep`（握るものの後に判断例）→`#what-to-record`。判断例は握るものの直後に置いた

## メインに判断してほしいこと
- 節 `what-you-keep` を足した（既存の anchor は変えていない）。足さず `why` か `what-to-record` に畳む案もある
- Bastani（PNAS 2025）は、束の出典が RePEc の書誌ページのみ。本文の 48%・17% は research/24 の写しが「17%下が…」で切れており、「対照群と比べた値」は手元の材料では確かめていない

## 提案
```yaml
sources:
  - note: pnas-bastani-2025-genai-learning の URL を PNAS 本体（doi 10.1073/pnas.2422633122）に差し替えるか追加する案。書誌ページでは数値を直接確かめられない
frontmatter: []
```
- 用語集・prh・data への提案はなし。数値の提案（facts-proposal.yml）もなし（研究の結果は固定の記録として本文に書いた）

## 検査の結果
- 1 回目：エラー 0・警告 2（「一つ」→「1 つ」、助詞「は」の連続）。直した
- 2 回目：エラー 0・警告 0

## 確かめていないこと
- 本文の研究の数値は束の写し（00・05・11・research/24）に基づく。METR の原文・追試（57 人・800 課題超）・PNAS の論文は開いていない（Web の取得 0 回）
- `#why` の仕組みの 4 点は推論で、印を付けた。研究が直接示したのは、ずれがあることだけ
- 雛形 effect-log は動作を確かめていない（表の雛形で、実行するものではない）
- 図 gap.svg の見た目は、ブラウザで描画を見ていない
- 判断例の「2 週間」「中央値」は例であり、根拠のある推奨値ではない

## 使用量
- 道具の呼び出し：約 14 回（Read 2、Bash 8、検査 2、報告 1 ほか）。ページは 1 回の書き込み（heredoc）。Web の取得 0 回
