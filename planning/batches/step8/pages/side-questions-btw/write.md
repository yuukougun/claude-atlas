# write.md：side-questions-btw（執筆）

## 書いたファイル
- `docs/context/side-questions-btw.md`（stubs から mv。stage draft、updated 2026-11-05）
- `snippets/side-questions-btw/btw-questions.md` と `.expect.yaml`（prompt）
- front matter で変えたキー：sections（when・minimal・pitfalls を足し、which は残した）、sources（cc-docs-interactive-mode・cc-docs-commands。どちらも data/sources.yml にある）、stage、updated。data/sources.d は作っていない（新しい出典なし）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力・読み込みの時期など）：冒頭の要点の「強制力」（なし。手書き）と `#which` の `compare 成熟度 コンテキストのコスト` の目印。強制力の値が data の btw にないため、バッジは成熟度・コンテキストのコスト・確認日になる
- `tracks`：btw。`#which` の compare が使う
- 1機能1ページ：btw のみ
- level：整える（front matter のまま）
- 構成の目安：使いどころ `#when`／最小の使い方（面のタブ）`#minimal`／雛形（`#minimal` の末尾）／効かない場面・落とし穴 `#pitfalls`／比べる相手 `#which`／古くなった助言は台帳の行がないので置かない

## メインに判断してほしいこと
- 数値ファイルの btw に `enforcement` がない。要点の「強制力」は「なし」と手で書いた（insights-and-usage-review と同じ流儀）。データに足すなら下の提案を参照

## 提案
```yaml
proposals:
  - fact: {id: btw/enforcement, title: /btw の強制力, value: なし, sources: [cc-docs-interactive-mode], checked: 2026-11-05, status: 確認済み}
    used_in: [side-questions-btw#when]
```
（data/facts.yml の features の btw に `enforcement: なし` を足す案。道具の形に合わせて直してください）

## 検査の結果
- 1回目：エラー 0・警告 5（助詞「に」「も」の重複）。直した後の2回目：エラー 0・警告 1（49 行目の「に」の重複。誤検出に近いが未対応）

## 確かめていないこと
- 本文の挙動は公式の interactive-mode（Side questions with /btw）で確かめた（2026-11-05 取得）。実機では試していない
- 文脈の外の一般知識を /btw で聞いたときの答え方は未確認。本文は「文脈にあることを聞く」使い方に限った
- 推測で答える恐れ（pitfalls の「道具を使えない」）は（推論）と付けた。キャッシュが冷えたときの費用は公式に書きがなく、書いていない
- VS Code 拡張のパネル、ほかの IDE 拡張と WSL・Linux 以外の OS の動きは未確認と本文に書いた。版の数字（入った版・キー操作の版）は本文に書いていない
- tidy-the-desk・when-to-start-fresh などへの link の節は束の「指せる節」から選んだ。リンク先の本文は読んでいない

## 使用量
- 道具の呼び出し：約 14 回（Web の取得 1 回）
