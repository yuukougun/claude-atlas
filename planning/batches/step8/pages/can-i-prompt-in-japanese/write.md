# write.md：can-i-prompt-in-japanese（concept・japanese）

## 書いたファイル

- `docs/japanese/can-i-prompt-in-japanese.md`（stub から mv。stage は draft）
- front matter で変えたキー：`sections`（`effects`・`misconceptions` を末尾に足した）、`sources`（既にある 8 件の id）、`stage`（draft）、`updated`（2026-11-05）
- `snippets/can-i-prompt-in-japanese/request-with-identifiers.md`・`.expect.yaml`（prompt。目次の templates は「なし」。識別子を原文のまま書く Before/After の After に要る）
- `snippets/can-i-prompt-in-japanese/claude-md-japanese.md`・`.expect.yaml`（claude-md）
- `data/sources.d/can-i-prompt-in-japanese.yml` は作らない（出典はすべて既存の id）

## 必ず持つものの対応

- 冒頭の要点の最初の項目が「何が分かるか」：冒頭の囲み（最初の `##` より前）
- どの原理・どの原因に関わるか（`principle`＝見せる、`prevents`＝見えていない を本文で名指す）：`#effects`
- `pitfalls`：front matter に無いので持たない（束の front matter に pitfalls のキーがない）
- 構成の目安（技法寄り：頼み方の例 → 何が変わるか → なぜ効くか → 効かない場面・やりすぎ）：頼み方の例 `#keep-original`（Before/After）、何が変わるか `#keep-original`、なぜ効くか `#effects`、効かない場面の限り `#evaluation`、誤解 `#misconceptions`、関連はテンプレート（page-links）
- level を持つ：front matter `level: 使う`
- 根拠の強さの印と、旧い世代・類推の明示：`#evaluation`、`#claude-md`、`#tokens`

## メインに判断してほしいこと

- 公式の多言語の表（Multilingual support）は、束の材料（旧世代の Sonnet 4.5 と Haiku 4.5 の旧い値）から更新され、Global-MMLU で Fable 5.1・Opus 5.5・Sonnet 5.5・Haiku 5.5 の日本語の値が載っている（Web を 1 回取得して確認）。本文は、モデル名と数値を手で書かず、「現行のどのモデルでも英語に近い。小さいモデルほど差がやや開く」と定性で書いた。下の提案の fact を採用するなら、`#evaluation` に表の目印を置ける
- research/27 #12 の「Sonnet 4.5 が 96.8%、Haiku 4.5 が 93.5%」は、公式の表に載らなくなったので本文に使っていない。目次の notes と summary（「比べたデータはない」は作業の指示に限る）は、このままで食い違わない
- `thinking-words` 節は、版の数字を書かず、「以前は CHANGELOG に記録があり効く時期があった」と書いた（台帳の行に版があるため）。台帳の行へは link で指した

## 提案

```yaml
proposals:
  - fact: {id: multilingual-global-mmlu-japanese, title: "公式の多言語の評価（Global-MMLU）で、英語を 100% とした日本語の成績（モデルごと）", value: "Fable 5.1 98.7%・Opus 5.5 99.2%・Sonnet 5.5 98.4%・Haiku 5.5 97.4%", sources: [api-docs-multilingual-support], checked: 2026-11-05, status: 確認済み}
    used_in: [can-i-prompt-in-japanese#evaluation]
    note: 最大の effort・adaptive thinking・zero-shot。1 ポイント未満の差は測定の揺れ、と公式が注記。表は 1 つの値に丸めず、モデルごとの表（fact-table）にしてほしい
```

## 検査の結果

- 1 回目：エラー 0・警告 5。直した後の 2 回目：エラー 0・警告 2
- 残した警告：`no-doubled-joshi`（41 行目の要点の「いつ引くか」、166 行目の `#effects` の 1 文）。signs の言い回しと文の自然さを優先した。直すなら読点か語の入れ替えで足りる
- 直しの 1 回は、Write でなく Bash の python で文の置換をした（brief の「ページは Write」に反する。小さな語の置換 4 か所）

## 確かめていないこと

- アプリでの CLAUDE.md 相当（指示・プロジェクト）と、アプリで「熟考」が効くかは確かめていない（本文は Claude Code の話に限り、アプリは未確認と書いた）
- 「訳した識別子では対象が見えない」「日本語の CLAUDE.md の保守は読む人で選ぶ」は、実機で比べていない推論。雛形の expect は観察用で、合否にしない
- 実践者の記事（入江・仁頼・SSD Nodes）は、束の写しからの要約で、本文を読み直していない
- token counting が API だけの機能であること（アプリと Claude Code に無い）は束の data（surfaces: api）による。Claude Code に別の数え方があるかは確かめていない
- link の行き先（`outdated-advice-ledger#think-hard-keywords`）は、台帳の行の id を data から推した。check_page で通った

## 使用量

- 道具の呼び出し：約 20 回。Web の取得：1 回（Multilingual support）
