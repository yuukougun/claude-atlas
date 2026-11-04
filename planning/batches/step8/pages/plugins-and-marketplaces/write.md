# write.md：plugins-and-marketplaces（執筆）

## 書いたファイル
- `docs/extend/plugins-and-marketplaces.md`（stub から mv。stage draft、updated 2026-11-05）。front matter で変えたキー：`sections`（使いどころ・最小の使い方・効かない場面と落とし穴・比べる相手を足した。既存の before-install・team-marketplace はそのまま）、`sources`、`stage`、`updated`
- 雛形：`snippets/plugins-and-marketplaces/` の `team-marketplace`・`minimal-plugin`・`project-settings`（各 .json と .expect.yaml）。目次の templates の「marketplace.json と最小の plugin.json」を 2 つに分けた
- 図：`docs/img/plugins-and-marketplaces/bundle.svg`
- 出典：`data/sources.d/plugins-and-marketplaces.yml`（cc-docs-plugins-org を足した。code.claude.com は確かめ済みのドメイン）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力・読み込みの時期など）：冒頭の要点の「読み込みとコスト」（`feature plugins/load_timing`・`context_cost`・`maturity`）。強制力は data の plugins に値がないので目印を置かず、「止めるもの」に文で書いた（下の提案）
- `tracks`（plugins・marketplaces）：front matter に維持。本文は #when-to-use（両方の説明）と #team-marketplace（marketplaces）
- level（仕組みにする）：front matter に維持
- 構成の目安（要点 → 使いどころ → 最小の使い方 → 雛形 → 効かない場面 → 比べる相手 → 古くなった助言）：#when-to-use → #minimal（面のタブ：アプリ・Claude Code）→ #before-install → #team-marketplace（雛形 3 つ）→ #limits → #compare。古くなった助言は、台帳の行がない（束に outdated_advice なし）ので節を置かなかった
- 比例則：配る前の守りは #before-install を #team-marketplace の前に置き、#team-marketplace の先頭でも守りを先に示した

## メインに判断してほしいこと
- 強制力の目印：data の plugins には enforcement がない。「なし」を足すなら提案のとおり。足したら要点に `feature plugins/enforcement` を入れたい
- 逆に、クラウドのセッションでプラグインが動くかは、束（research/01・27）が「ローカルの設定のプラグインは読まない」「プラグインは読み込まれない」と書くのに対し、公式の org ページ（2026-11-05 に取得）は、クラウドでのリポジトリの設定の扱いを面ごとの別の節に任せている。本文は「ローカルで入れたものは届かない。リポジトリの設定の場合は未確認」と書いた。data に確認済みの値を足せるなら足したい

## 提案
```yaml
frontmatter: []
proposals:
  - feature_patch: {id: plugins, add: {enforcement: なし}}
    reason: プラグインは束ねて配るだけで、止める力を持たない。要点の「止めるもの」と合わせる
    sources: [cc-docs-plugins-overview]
glossary:
  - {term: マーケットプレイス, note: プラグインの一覧（marketplace.json）を持つカタログ。ストアではない。用語集になければ追加}
```

## 検査の結果
- 1 回目：エラー 0・警告 3。直した後：エラー 0・警告 2（no-doubled-joshi の「に」が 2 件。`#before-install` の 1 文目と #team-marketplace の末尾近くの文。意味を変えずに分けにくく、残した）
- 検査は規定の 2 回を使い切った

## 確かめていないこと
- 雛形の動作は確かめていない。`plugin.json` は name と description だけの最小にしたが、必須の項目は公式の manifest のページで確かめていない（marketplace の一覧の必須は公式で確認した）
- 同期の下限の版：公式同士が食い違う（Help Center が v2.1.273 以上、CHANGELOG が 2.1.275）ので、本文に書かず plugins-in-the-app を指した
- アプリのプラグインの画面は展開中（2026-10-29 から）。本文は「名前が変わる途中」と書くだけにした
- Windows・macOS と IDE 拡張の動作

## 使用量
- 道具の呼び出し：約 25 回、Web の取得：2 回（create-marketplace、org）
