# write.md：claude-md-loading-order（feature・extend）

## 書いたファイル
- docs/extend/claude-md-loading-order.md（stubs から mv。stage: draft）。front matter で変えたキー：`sections`（7 節を足した。既存の monorepo・after-compaction は anchor を変えず残した）、`sources`（cc-docs-memory・cc-docs-context-window）、`stage`、`updated`
- snippets/claude-md-loading-order/claude-local.md と .expect.yaml（kind: claude-md）
- snippets/claude-md-loading-order/exclude-other-teams.json と .expect.yaml（kind: settings）
- data/sources.d/claude-md-loading-order.yml は書かない（新しい出典なし）

## 必ず持つものの対応
- 要点の強制力のバッジ：冒頭の要点の「強制力」行（`feature enforcement` の目印）
- 機能の属性のバッジ（テンプレートが出す）と `tracks`：front matter の `tracks: [claude-md, rules]`、比較の表は #compare
- 1機能1ページ・密接な系統は節に分ける：#order（階層）・#import・#monorepo・#after-compaction
- level：front matter の `level: 任せる`
- 使いどころ（どの原因を防ぐか）：#when
- 最小の使い方（面のタブ）：#usage。surfaces が claude-code だけなので、タブは置かなかった
- 雛形：#templates（2 つ）
- 効かない場面・落とし穴：#limits
- 比べる相手：#compare（compare の表と rules・設定・自動メモリへの link。comparison 型のページは related にない）
- 古くなった助言：台帳の行がない（束の outdated_advice なし）ので節を置かなかった

## メインに判断してほしいこと
- 一次資料として code.claude.com/docs/en/memory を 1 回開いた（Web の取得 1 回）。/context all の Memory files、/memory、Loaded の行、InstructionsLoaded フック、claudeMdExcludes の例、CLAUDE.local.md の worktree の注意、サブフォルダの CLAUDE.md の大きさの上限は、束になくこの文書から書いた
- 木の図は SVG ではなく code ブロックの文字の木にした（visual 案は static の図）。SVG が要るなら別の担当へ

## 提案
```yaml
proposals:
  - fact: {id: claude-md-import-max-hops, title: "@import の入れ子の段数の上限", value: "4 段（ホップ）", sources: [cc-docs-memory], checked: 2026-11-05, status: 確認済み}
    used_in: [claude-md-loading-order#import]
  - fact: {id: claude-md-on-demand-size-limit, title: "後から読まれるサブフォルダの CLAUDE.md・rules のファイル単位の大きさの上限（コンテキストの大きさごと）", value: "200K のコンテキストで 40,000 字（ほかは公式の文書の表）", sources: [cc-docs-memory], checked: 2026-11-05, status: 要確認}
    used_in: [claude-md-loading-order#limits]
```
- 上の 2 つは本文では数字を書かず、used_in の場所に目印を足せる。段数は調査資料 01 A-1 から、大きさの上限は公式の文書から
- front matter・用語集・prh の提案はなし

## 検査の結果
- 1 回目：エラー 0・警告 13（snippet の目印が文の中、(a)(b) の英字、助詞の重複）。直した
- 2 回目：エラー 0・警告 5（助詞 "に"・"は"・"で" の重複 5 件）。残りは、生成された link の題名が入った行にあり、原文は短くした。確定の誤検出かは見ていない
- 2 回目の後に 1 か所を直した（自動メモリの行の文末）。その後は流していない

## 確かめていないこと
- 作業ディレクトリより上の階層の CLAUDE.md が、圧縮の後にどうなるか（公式の表はプロジェクト直下の分しか書かない。本文でもそう書いた）
- クラウドのセッションの記述は調査資料 27 §3.2 による。公式の文書そのものは開いていない
- claudeMdExcludes の雛形のパターン（`**/other-team/...`）は、公式の例に倣って作った。動かして確かめていない。`.claude/CLAUDE.md` の行と rules の行は公式の例にない形で、一致するかは未確認
- 用語集の語の最初の 1 回の link は、用語集を見ていないので付けていない
- WSL・Linux 以外の OS と IDE 拡張の動作

## 使用量
- 道具の呼び出し：約 14 回、Web の取得 1 回
