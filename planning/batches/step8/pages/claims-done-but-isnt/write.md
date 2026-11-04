# write.md：claims-done-but-isnt

## 書いたファイル
- `docs/symptoms/claims-done-but-isnt.md`（stubs から mv。stage を draft、updated を 2026-11-05、sources に既存の 6 件、sections に forms・routes-to-fixes・lookalikes・example・prevention を追加。既存の diagnosis は維持）
- `snippets/claims-done-but-isnt/ask-for-basis.txt` と `.expect.yaml`（目次の templates は「なし」。診断で根拠を出させる依頼を足した）
- 新しい出典ファイル（`data/sources.d/`）は作っていない。sources の 6 件は `data/sources.yml` に既存

## 必ず持つものの対応
- 診断のチェックリスト（原因を安く確かめる順。人の側の落とし穴も）：`#diagnosis`（見えていない → 確かめていない → 預けすぎる。先頭に事実での確定）
- 原因ごとの振り分け先（routes）：`#routes-to-fixes`（`gen:begin routes`）
- 要点 → よくある形 → 判断例 → 予防：`#forms`・`#example`・`#prevention`
- 古くなった助言（add-double-check）：`#prevention` で台帳の行を link
- 検索の打ち切り・起動失敗の例：`#diagnosis` の 1 番目から evidence-not-reports#tool-output へ

## メインに判断してほしいこと
- `#forms` に、実践者の記事 2 件（データ分析のコンテストの記事、静的解析の道具を使わなかった記事）の事例を、名指しなしで載せた。sources には両方を入れたので、参考の節に題名が出る。名指ししない方針（目次の notes）に合うか確認してほしい
- 事例（issue の 2 件）は、版の番号を書かず、モデル名と日付だけにした

## 提案
```yaml
proposals:
  - fact: {id: claude-code-search-truncation-fix, title: 検索が時間切れで途中までしか返さないのを全部とみなす不具合を直した版, value: v2.1.317, sources: [cc-changelog], checked: 2026-11-05, status: 要確認}
    used_in: [claims-done-but-isnt#forms]
  - fact: {id: claude-p-startup-failure-exit-code-fix, title: 起動に失敗しても終了コード 0 で終わる不具合を直した版, value: v2.1.314, sources: [cc-changelog], checked: 2026-11-05, status: 要確認}
    used_in: [claims-done-but-isnt#forms]
```
- 本文は版の数字なしで読めるように書いた。承認されたら `#forms` の最後の項目に fact の目印を置く

## 検査の結果
- 2 回流した。エラー 0。警告 6 → 3
- 残した警告 3 件：46 行（要点の「何ができるか」の「が」）、62 行（issue の事例文の「が」）、74 行（link の題名が入った生成文の「に」）。いずれも文の短縮で意味が落ちる、または生成文が原因

## 確かめていないこと
- 事例の数値と日付・モデル名は、束の写し（research/05・11）を信頼した。一次の issue は開いていない
- 雛形 ask-for-basis の動作（expect）は試していない
- link の `outdated-advice-ledger#add-double-check` の節が存在するかは、check の通過のみで確認した
- 面ごとのタブは使わなかった（面に固有の手順がないため）

## 使用量
- 道具の呼び出し 9 回前後・Web の取得 0 回
