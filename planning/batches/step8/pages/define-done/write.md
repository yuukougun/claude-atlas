# define-done 執筆報告

## 書いたファイル
- `docs/verify/define-done.md`（stubs から mv。stage: draft、updated: 2026-11-05）
- `snippets/define-done/request.txt` と `.expect.yaml`（開発向け）、`request-writing.txt` と `.expect.yaml`（文章向け）
- front matter で変えたキー：`sections`（before-after・by-surface・templates・what-it-helps・misreadings を足した。既存 3 つの anchor は不変）、`sources`（6 件。すべて既存の id）、`stage`、`updated`。新しい出典はなく、`data/sources.d/define-done.yml` は作っていない

## 必ず持つものの対応
- どの原理・どの原因に関わるか（principle 確かめる・見せる／prevents 確かめていない・見えていない）：`what-it-helps`（要点の「関わる原理と原因」にも）
- level を持つ（整える）：front matter。要点の最初の項目は「何が分かるか」
- pitfalls：front matter が空（`[]`）のため、名指す対象なし
- 構成の目安（何が起きるか→なぜ→何に効くか→誤解→関連）：`why-it-stops`（起きること・なぜ）→`what-it-helps`→`misreadings`→page-links（関連）。技法の面は `before-after`（Before/After）・`what-to-include`・`stop-and-report`

## メインに判断してほしいこと
- 目次の備考どおり、アプリ・API は「形式・分量・合格の基準」として `by-surface` のタブに置いた。アプリで何が実行できるかは束に材料がなく、断定を避けて「限られる」と書いた
- `outdated-advice-ledger#keep-going-dont-be-lazy` を link で指した（カード §11 の形。束の指せる節の一覧にはない）

## 提案
なし（用語集・data・front matter の他キーへの提案はなし）

## 検査の結果
- 1 回目：エラー 0・警告 6。直して 2 回目：エラー 0・警告 1
- 残した警告：`define-done.md:218` の sentence-length（129）。C コンパイラの記事のリンク題名（英語）が長く、文を切ると記事への言及が分かれるため残した。誤検出に近い

## 確かめていないこと
- 本文の事実は束の写し（Best practices・Issue 2 件・C コンパイラの記事の要旨）に基づく。一次資料は開いていない（Web の取得 0 回）
- Issue #64286 の「3 件」は束の写しの「xlsx テスト 3 件」による。#46940 の件数も束による
- Before/After の例と判断例は説明用に作った。Claude で試していない。雛形 2 つも動作は未確認
- Opus 5 のガイドの「double-check を外す」の言い方は束 6.1 の要約による
- IDE 拡張・他 OS での動作は扱っていない

## 使用量
- 道具の呼び出し：約 12 回（Read 4・Bash 6・Write 5 ほか）。Web の取得：0 回
