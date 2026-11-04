# write: claude-md-length

## 書いたファイル
- docs/extend/claude-md-length.md（stub から mv。stage を draft、updated を 2026-11-05。sections に when・prune-prompt・limits・compare・outdated を足した。sources に既存の id を 10 件入れた）
- snippets/claude-md-length/prune-prompt.md と prune-prompt.expect.yaml（目次の templates の案どおり）
- data/sources.d/claude-md-length.yml は作っていない（出典はすべて既存の id）

## 必ず持つものの対応
- 機能の属性のバッジ：冒頭の囲みの「強制力」に `gen feature enforcement`。バッジの列はテンプレートが出す
- tracks（claude-md）：front matter に持つ。属性の値は手で書いていない
- 1 機能 1 ページ・密接な系統は節：削る問い {#deletion-test}・/init の叩き台 {#init-draft}・チーム {#team} に分けた
- level：任せる（front matter のまま）
- 構成の目安：要点 → 使いどころ {#when} → 最小の使い方 {#deletion-test}（面は claude-code だけなのでタブなし）→ 雛形 {#prune-prompt} → 効かない場面 {#limits} → 比べる相手 {#compare} → 古くなった助言 {#outdated}

## メインに判断してほしいこと
- 本文で `claude-md-vs-rules-skills-styles` をページ単位で指した（related にない）。related への追加を提案する
- 「月 1 回の棚卸し」「681 行（Kaggle 3 位の自己申告）」「約 2.5k トークン（二次要約）」は根拠：弱として書いた。載せる程度の可否を見てほしい

## 提案
```yaml
frontmatter:
  - {id: claude-md-length, key: related, before: [init-and-first-claude-md, path-scoped-rules, how-skills-load, when-to-lock, emphasis-words, instructions-ignored, pruning-extensions, measure-changes, felt-vs-measured, after-switching-models, share-team-settings, claude-md-loading-order, inspect-context], after: [init-and-first-claude-md, path-scoped-rules, how-skills-load, when-to-lock, emphasis-words, instructions-ignored, pruning-extensions, measure-changes, felt-vs-measured, after-switching-models, share-team-settings, claude-md-loading-order, inspect-context, claude-md-vs-rules-skills-styles], reason: "比べる相手の節で指している"}
```
- 数値の提案はなし（200 行は claude-md-recommended-lines、版は doctor-prompt-audit-min-version を使った）

## 検査の結果
- 1 回目：エラー 3（prh の skill → スキル）・警告 2（500 行の目印外・助詞「で」の連続）。2 回目：エラー 0・警告 0

## 確かめていないこと
- 実際の動作（雛形のプロンプト、`/doctor` の出力）は試していない。ネイティブ Windows と IDE 拡張の動作は「未確認」と書いた
- 「@path の取り込みで常駐は減らない」は、束の research 写しに基づく。節の直接の指し先がなく、ページ単位で claude-md-loading-order を指した
- Kaggle・約 2.5k トークンの値は束の写しのまま。一次資料は開いていない

## 使用量
- 道具の呼び出し 11 回前後、Web の取得 0 回
