# write.md：resume-and-branch（執筆）

## 書いたファイル
- docs/cli/resume-and-branch.md（stubs から mv。stage を draft、updated を 2026-11-05、sources に cc-docs-sessions・cc-docs-commands・cc-docs-data-usage・cc-docs-best-practices・cc-changelog・cc-docs-changelog を足した）
- front matter の sections：use-cases・pitfalls・compare・outdated を足した（既存の resume・branch・naming はそのまま）
- snippets/resume-and-branch/session-commands.sh（+ .expect.yaml）：命名・再開・分岐のコマンド集（kind: other）
- snippets/resume-and-branch/branch-request.md（+ .expect.yaml）：分岐した先で別案を試す依頼（kind: prompt）
- data/sources.d は作っていない（出典は既存の id だけ）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが tracks の sessions から出す（本文に手書きなし）
- tracks：front matter の `tracks: [sessions]`
- 1機能1ページ・節に分ける：#use-cases・#resume・#branch・#naming・#pitfalls・#compare・#outdated
- level：front matter の `level: 整える`
- 構成の目安の対応：要点（冒頭）→ 使いどころ #use-cases → 最小の使い方 #resume・#branch・#naming（面は claude-code 1 つだけなのでタブなし）→ 雛形 #resume（session-commands）・#branch（branch-request）→ 効かない場面 #pitfalls → 比べる相手 #compare → 古くなった助言 #outdated
- 強制力：data の sessions に enforcement の属性がないため、要点に feature の目印は置いていない（下の提案）

## メインに判断してほしいこと
- 要点に「強制力」を置いていない。sessions の機能に enforcement の値がない（操作であり、お願い・鍵のどれにも当てはめにくい）。属性を足すか、このページでは省くかを決めてほしい
- 「ブランチ名・セッション名を揃える」（11 の p34#195）には（根拠：弱）を付けた。強さの判定が違えば直してほしい
- #pitfalls の「分岐が分けるのは会話であって、ファイルではない」は、公式が会話の複製と書いていることからの読み（この辞典の読み、と本文に明記）。公式にファイルの扱いの明記はなく、確かめる担当がいれば試してほしい

## 提案
```yaml
frontmatter:
  - {id: resume-and-branch, key: sections, before: [resume, branch, naming], after: [use-cases, resume, branch, naming, pitfalls, compare, outdated], reason: "型の構成の目安（使いどころ・落とし穴・比べる相手・古くなった助言）に合わせて節を足した。既存の anchor は変えていない"}
```
- 数値の提案はなし（保持期間は既存の local-transcript-cleanup-days を目印で指した）
- 用語集：「ピッカー（セッションの一覧）」は本文で「セッションの一覧（ピッカー）」と 1 回だけ書いた。追加は要らないと考える

## 検査の結果
- 1 回目：エラー 3（ワークツリー → worktree）・警告 3
- 直した後の 2 回目：エラー 0・警告 1（113 行付近の no-doubled-joshi「が」。「保存された会話だけが 5 時間の利用枠をどれだけ使うかの割合で…」の文。意味が通るので残した）

## 確かめていないこと
- コマンドと動作は公式の Manage sessions（code.claude.com/docs/en/sessions、2026-11-05 に取得）に基づく。実機では試していない
- デスクトップアプリ・VS Code 拡張・claude.ai/code の動作は未確認（本文にもそう書いた）
- 分岐した先と本筋が同じ作業ツリーを共有する点は読みで、実機の確認なし
- 雛形の動作は未確認

## 使用量
- Web の取得：1 回（code.claude.com/docs/en/sessions）
- 道具の呼び出し：約 20 回（Read 2 + 手引き 1 + Bash 8 前後 + Write 7 + WebFetch 1 + ToolSearch 1。Write 1 回は引数の誤りで失敗）
