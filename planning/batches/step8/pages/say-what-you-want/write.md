# say-what-you-want 執筆の報告

## 書いたファイル
- `docs/prompting/say-what-you-want.md`（stubs から移した。stage draft、updated 2026-11-05。front matter で変えたキー：sections に what-changes・why・templates・effects・limits を足した、sources に api-docs-prompting-best-practices と api-docs-prompting-opus-5 を入れた）
- `snippets/say-what-you-want/rewrite-negatives.md` と `.expect.yaml`（prompt。禁止を 3 区分に振り分けて書き換えさせる依頼）
- `data/sources.d/say-what-you-want.yml` は作っていない（出典は既存の 2 件だけ）

## 必ず持つものの対応
- 冒頭の要点（何が分かるか）：冒頭の要点の囲み
- principle（見せる・縛る）：effects（「見せる」「縛る」を名指し）
- prevents（見えていない・縛っていない）：effects（原因を名指し）。why でも「見えない行き先」として触れた
- pitfalls：front matter に pitfalls がない。落とし穴に当たる内容は limits
- 技法の構成（例 → 何が変わるか → なぜ効くか → 効かない場面）：rewrite → what-changes → why → limits
- 要点 2 の二層（requirements §6.7 の 4 行目）：two-layers

## メインに判断してほしいこと
- 本文の「禁じた語が文脈に載る」は公式の説明ではなく、推論と明記した。残すか削るか
- two-layers の「フックが止めるときに返す文は Claude に届く」は、Claude Code のフックの仕様（exit 2 の stderr）に基づく。束にはない記憶による記述なので、確かめてほしい
- 「開発の例」の `docker compose` と test 用データベースは、例として置いた架空の設定

## 提案
- front matter の提案：なし
- 用語集・prh への提案：なし

## 検査の結果
- 書き終えた後：エラー 0・警告 4。直した後：エラー 0・警告 1
- 残した警告：本文 89 行目（禁じた語の箇条）の助詞「に」の重なり。誤検出ではないが、意味を変えずに直す案が出なかったので残した

## 確かめていないこと
- 公式の出典（Prompting best practices・Prompting Claude Opus 5）は、束の写し（確認日 2026-10-29）に基づく。Web は取得していない
- 雛形の動作（Claude が 3 区分に振り分けるか）は試していない
- 「何が変わるか」の 3 点は、公式の記述と一般的な経験則に基づく。この辞典では測っていない
- アプリの面で禁止を仕組みで止める手段は「未確認」と書いた

## 使用量
- 道具の呼び出し：約 12 回。Web の取得：0 回
