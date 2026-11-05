# write.md：choosing-automation（comparison・delegate）

## 書いたファイル

- `docs/delegate/choosing-automation.md`（stubs から mv。stage を draft、updated を 2026-11-05、sources と sections を足した）
- 雛形・図・`data/sources.d/choosing-automation.yml` は作っていない（目次の templates が空で、新しい出典もないため。sources は data/sources.yml にある id だけ）

## 必ず持つものの対応

- 比較の表（`compare` の目印）：`compare`（面・成熟度。tracks の 6 機能から道具が作る。軸の表は `axes` に手書き）
- 判断例：`examples`（判断例 3 つ。夜間のテスト→claude -p／PR のレビュー→GitHub Actions／自作ツール→Agent SDK）
- 構成の目安の「組み合わせ方」：`combine`（確かめ方もここに畳んだ）
- level：front matter の「回す」のまま
- 古くなった助言（台帳）：`outdated`

## メインに判断してほしいこと

- 軸の表の「Desktop の予定のタスク」の課金の経路を「未確認」にした。束と data にサブスクリプションの要否の記述が曖昧だったため
- 軸の表は、動く場所・触れられるもの・課金の経路を手書きにした（data の属性ではなく、プランの名前も数値も書いていない）。道具で作れる属性に直せるなら、data への属性の追加を検討してほしい

## 提案

- 数値の提案なし
- front matter の追加なし（sections は載せた 5 節のみ）

## 検査の結果

- 1 回目：エラー 0・警告 6（sentence-length 4、no-doubled-joshi 2）
- 直した後の 2 回目：エラー 0・警告 4（no-doubled-joshi 4）。残りは、生成された link の題名の助詞と隣り合う誤検出が主（48・104・116 行）
- 2 回目の後に 147 行の「と」の重なりを「・」に直した。この直しは検査を流していない

## 確かめていないこと

- 軸の表の各セル（クラウドの予定のタスクが新しい clone で動く点、GitHub Actions の `prompt` の有無による動き、Agent SDK の課金の経路）は、束の材料と data の note に基づく。一次資料は開いていない
- Desktop の予定のタスクの課金の経路
- GitHub Actions が置いた鍵の種類で経路が決まるという書き方は、束の J-2 の認証の列挙からの読みで、公式の課金の説明では確かめていない
- 他 OS・IDE 拡張の動作

## 使用量

- 道具の呼び出し：約 14 回（Read 4、Bash 7、Write 2、Edit 0）。Web の取得：0 回
