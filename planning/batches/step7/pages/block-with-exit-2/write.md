# write.md：block-with-exit-2

## 書いたファイル
- docs/enforce/block-with-exit-2.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に cc-docs-hooks・cc-docs-hooks-guide・cc-docs-permissions・cc-docs-features-overview を入れた。sections に when・templates・limits を足した）
- snippets/block-with-exit-2/ に block-migrations-exit2.py・block-migrations-json.py・register-hook.json と各 expect.yaml（目次の templates の案 1 つを exit 2 と JSON の 2 つに分け、登録の設定を足した）
- data/sources.d は新設なし（出典は既存の id のみ）

## メインに判断してほしいこと
- 要点の「強制力」は `feature enforcement` の目印で出している（config.yml の表示名は「強制力」だが、属性名は enforcement）。カードの書き方（`feature <属性>`）と表示名がずれて見える
- 公式の hooks reference を開いていないので、束の写し（research/28 #13・#15・#16）だけに基づく。exit 2 以外の非 0 が「止めない」になる点は束の F-1 に基づく

## 提案
```yaml
frontmatter:
  - {id: block-with-exit-2, key: signs, before: ["`.env` や migrations を絶対に触らせたくない"], after: [".env や migrations を絶対に触らせたくない"], reason: "check_page の平文の欄の警告（signs にバッククォート）"}
```

## 検査の結果
- 1 回目：エラー 2（prh：拒否ルール→deny ルール、hook→フック）・警告 7。2 回目（直した後）：エラー 0・警告 3
- 残した警告：signs のバッククォート（front matter は直せないので上の提案）／sentence-length 1 件・助詞「が」の重複 1 件（判断例の囲みの中の文。読みやすさは保てているので残した）

## 確かめていないこと
- 雛形のスクリプトと登録の設定を実際に動かしていない（Claude Code 上で止まることも未確認）
- 「exit 2 と JSON を混ぜると exit 2 が勝つ」「deny の理由が Claude に見える」は束の写しによる。最新の公式文書と照合していない
- `permissionDecisionReason` を事実の形で書く勧めは推論（本文に印を付けた）。実際に Claude が回り込まなくなるかは未検証
- Windows・macOS・IDE 拡張の動作は未確認（本文にもそう書いた）
- 判断例の中・タブの中の字下げ段落は textlint が検査しないため、目で読んだだけ

## 使用量
- 道具の呼び出し 約 16 回（Read 2、Bash 7、Write 7）／Web の取得 0
