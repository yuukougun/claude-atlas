# write.md：protected-paths（feature・enforce）

## 書いたファイル
- docs/enforce/protected-paths.md（stubs から移した。stub は削除。stage を draft、updated を 2026-11-05。sections に when・templates・pitfalls・compare を足し、sources に cc-docs-permissions・cc-docs-permission-modes・cc-docs-settings-reference・cc-changelog を入れた）
- snippets/protected-paths/block-writes-outside.json と .expect.yaml
- 数値の提案：facts-proposal.yml（planning/batches/step8/pages/protected-paths/）

## 必ず持つものの対応
- 機能の属性のバッジ（強制力）：冒頭の要点の「強制力」（`gen feature enforcement`）
- tracks：front matter（permissions・permission-modes）。変更なし
- 1機能1ページ・節に分ける：#protected・#critical-rm・#outside-working-directory
- level：任せる（front matter）
- 構成の目安：使いどころ #when → 最小の使い方（面のタブ。Claude Code のみ）#outside-working-directory → 雛形 #templates → 効かない場面 #pitfalls → 比べる相手 #compare
- 古くなった助言：台帳の行がない（outdated_advice なし）ので節を置かない

## メインに判断してほしいこと
- 外を閉じるキーの版の下限（v2.1.314）を本文に書けないので、数値の提案にした。採用されたら本文の「版の下限は数値ファイルに置く（提案済み）」を目印に置き換える
- 「提案済み」という文が、採用後は古くなる

## 提案
- data/facts.yml：facts-proposal.yml（used_in：protected-paths#outside-working-directory）
- 用語集：critical paths（重要な場所への rm/rmdir の保護）・protected paths の追加を提案

## 検査の結果
- check_page.py 2回：エラー 0・警告 4
- 警告 4 は、link の目印の中身（長い題名）が展開された行の文の長さと助詞の重複で、本文の文は短い。誤検出として残した

## 確かめていないこと
- 公式の permission-modes の後半（20,000 字弱）と settings-reference のキーの詳細（既定値・例外の全リスト）は読んでいない
- auto と bypassPermissions での critical paths の rm の個別の動き（公式の該当部分が取得で切れた）。本文は「allow では通せない」「acceptEdits では確認が出る」「auto の分類器は審査しない」だけに絞った
- EnterWorktree・ExitWorktree が使えなくなる点と、リポジトリの設定で入れられるが利用者の設定を外せない点は、調査資料 22 #4 による。公式で再確認していない
- 雛形の動作、macOS・Windows・IDE 拡張の動き
- `blockReadsOutsideWorkingDirectories` の版の下限と既定値

## 使用量
- 道具の呼び出し：約 15 回。Web の取得：2 回（permission-modes、settings-reference）
