# write.md：harness-over-model（執筆）

## 書いたファイル

- `docs/models/harness-over-model.md`（stubs から mv。stage draft、updated 2026-11-05）
- front matter で変えたキー：`sections`（`what-it-prevents`・`misconceptions` を足した。既存の 3 節は変えていない）、`sources`（data/sources.yml にある 4 つの id を足した）、`stage`、`updated`
- 雛形・図・`data/sources.d/harness-over-model.yml`・`facts-proposal.yml` は作っていない（目次の templates は「なし」。新しい出典も数値の提案もなし）

## 必ず持つものの対応

- どの原理・どの原因に関わるか（`principle`・`prevents`・`pitfalls` を本文で名指し）：`what-it-prevents`（確かめる・見せる／合っていない・確かめていない／体感を信じる）
- level 任せる → 守りを先に置く：`what-it-prevents` の末尾の段落（verifier-defines-problem#loops-amplify・verification-ladder#four-steps）
- 要点の最初は「何が分かるか」：冒頭の囲み
- 構成（何が起きるか→なぜ→何に効くか→誤解→関連）：`when-harness-matters`（何が起きるか）→ `what-is-harness`（仕組み）→ `compare-with-your-eval` → `what-it-prevents` → `misconceptions`。関連はテンプレート。比喩付きの図は置いていない（理由は下の「確かめていないこと」）

## メインに判断してほしいこと

- 手元の 2 件の一次資料（DrivenData、Anthropic の記事）を Web で確かめた。調査資料 11・10 の要約は「差の多くはハーネスに帰せられた」だが、DrivenData の記事は Claude Code と Codex の差をモデルとハーネスに切り分けておらず、ハーネスの根拠は別のツールの成績が大きく下がったことだった。本文は記事に合わせて「切り分けていない」と書いた。目次の備考・調査資料の要約を直すか、判断してほしい
- 本文に Claude Code（Opus 4.5）と Codex（GPT 5.2 Codex）の名前を、研究の時点の固定の記録として書いた（card §7 の末尾の扱い）。第三者のツール名の扱いとして問題ないか確認してほしい
- 目印を使わない固定の記録（モデル名・費用や時間は数値を書かず）にした。フルハーネスの費用と時間は本文に書いていない

## 提案

```yaml
frontmatter: []
```

- 用語集 `harness` の行は「モデルのまわりでツールを動かし、モデルが見る文脈を管理する層」。本文の定義はこれに合わせた。変更の提案はない
- prh：「system prompt」は システムプロンプト、「harness engineering」は ハーネスエンジニアリングに直した（prh の指摘どおり）

## 検査の結果

- 書き終えた後：エラー 3・警告 5（prh の表記 3 件）。直した後：エラー 0・警告 3
- 残した警告 3 件（no-doubled-joshi）：冒頭の囲みの「何が分かるか」は summary と一致させるために残した。残り 2 件は、直せば文が不自然になるため（1 件は費用の文、もう 1 件は判断例の理由）

## 確かめていないこと

- 比喩付きの図は作っていない（このページは仕組みの図より、事例と比べ方が本体のため。要るなら検証の担当か次の波で判断）
- 図・雛形・動作確認はない。ページの他の章に出てくる link の節（`id#anchor`）は束の「指せる節」だけを使い、各ページの本文との意味の一致までは見ていない
- DrivenData の競技ごとの順位の数字は本文に書いていない（記事の表は Web の取得 1 回で見た要約のみ）。Anthropic の記事の費用・時間も同様
- 「ミスのたびに書き戻す実践」は調査資料 03 W5 の写しに基づく。個人名は出していない。元の記事は開いていない
- Claude Code のアプリ以外の IDE 拡張の挙動は扱っていない

## 使用量

- 道具の呼び出し：約 18 回（Read 2・Bash 7・Write 2・Web 2・ToolSearch 1 ほか）、Web の取得：2 回、check_page：2 回
