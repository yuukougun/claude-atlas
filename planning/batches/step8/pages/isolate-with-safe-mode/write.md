# write.md：isolate-with-safe-mode

## 書いたファイル

- `docs/cli/isolate-with-safe-mode.md`（stubs から mv。stage は draft。front matter で変えたキー：`sections`〔when・usage・templates・limits・alternatives を足した。既存の what-is-disabled・compare はそのまま〕、`sources`、`stage`、`updated`）
- `snippets/isolate-with-safe-mode/compare-steps.md`（＋ `.expect.yaml`）、`clean-config.sh`（＋ `.expect.yaml`）
- `data/sources.d/isolate-with-safe-mode.yml`（中身は `sources: []`。出典 `cc-docs-debug-your-config` は claude-md-vs-rules-skill 側の sources.d に既にあったため、重複を避けて空にした）

## 必ず持つものの対応

- 機能の属性のバッジ：テンプレートが出す（本文には書いていない）。強制力の行は置かなかった（下の「メインに判断してほしいこと」1）
- `tracks`：front matter の `tracks: [safe-mode]`（変更なし）
- 構成の目安：使いどころ `#when`／最小の使い方 `#usage`（面のタブは surfaces が claude-code だけなので置かない）／雛形 `#templates`／効かない場面・落とし穴 `#limits`／比べる相手 `#alternatives`／古くなった助言：台帳の行がないので置かない（outdated_advice なし）
- level：任せる（変更なし）

## メインに判断してほしいこと

1. 強制力：data の safe-mode の機能に `enforcement` の値がない。本文の要点では手書きを避け、「止められるもの」の 1 行にした。data に値が入れば `feature safe-mode/enforcement` の目印に替えられる
2. 公式の挙動の記述（外れるもの・管理の方針）は debug-your-config 1 回の取得と束の research による。`--bare` との違いは束の data の note にある範囲（認証が通常どおり）だけを書いた

## 提案

```yaml
proposals:
  - fact: {id: safe-mode-enforcement, title: "--safe-mode の強制力", value: "なし（読み込みを止めるだけ）", sources: [cc-docs-cli-reference], checked: 2026-11-05, status: 要確認}
    used_in: [isolate-with-safe-mode#what-is-disabled]
```

## 検査の結果

- 1 回目：エラー 2（出典 id・URL の重複）・警告 7。出典の重複を空にして、textlint の警告を直した
- 2 回目：エラー 0・警告 2（52 行目の読点 4 つ以上、214 行目の助詞「が」の重なり）。直さず残した（検査を 2 回使い切ったため）

## 確かめていないこと

- 環境変数が `--safe-mode` で無視されるか（本文に「確かめていない」と書いた）
- ステータスライン・LSP・自動メモリが外れる点は束の data の note による。自分では動かしていない
- 雛形 2 つは動かしていない（クリーンな設定フォルダの起動を含む）
- 断られたときの案内（research/26）は束の写しによる。cc-docs-errors を自分では開いていない
- 「古い版では使えない」と「`-p` で壊れた設定が黙って飛ばされる」は research の写しによる

## 使用量

- 道具の呼び出し：約 14 回、Web の取得：1 回（debug-your-config）
