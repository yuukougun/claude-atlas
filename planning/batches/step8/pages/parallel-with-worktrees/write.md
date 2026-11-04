# write.md：parallel-with-worktrees（執筆）

## 書いたファイル
- docs/delegate/parallel-with-worktrees.md（stubs から移した。front matter の変更：`sections` を 2 から 6 に増やした〔when・minimal・pitfalls・compare を足した。既存の per-worktree-setup・cleanup は維持〕、`sources` に cc-docs-worktrees・cc-changelog・cc-docs-changelog、`stage` を draft、`updated` を 2026-11-05）
- snippets/parallel-with-worktrees/worktreeinclude.txt と worktreeinclude.expect.yaml（safety: true）
- data/sources.d は作っていない（出典 3 つは data/sources.yml に既にある）

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す。本文には成熟度と入った版を `feature worktrees/maturity`・`worktrees/since` の目印で `#when` に置いた。強制力は data に値がないため目印を置かず、要点に手書きの 1 行（値の名前は書かない）
- tracks：front matter の `tracks: [worktrees]`（変更なし）
- level：front matter の `level: 仕組みにする`（変更なし）
- 使いどころ（どの原因を防ぐか）：#when
- 最小の使い方：#minimal（面は claude-code だけなのでタブにしていない）
- 雛形：#per-worktree-setup（worktreeinclude）
- 効かない場面・落とし穴：#pitfalls
- 比べる相手：#compare
- 古くなった助言：台帳に行がないので持たない。#compare の末尾に 1 行だけ書いた

## メインに判断してほしいこと
- 要点の「強制力」：data の worktrees に enforcement の属性がなく、`feature` の目印を使えなかった。手書きで「鍵ではない」と書いた。facts に enforcement を足すか（下の提案）、手書きのままでよいか
- 比例則の守りは使いどころに link で置いた（humans-set-the-parallel-limit#guards-before-widening・protecting-secrets#keep-out・sandboxing#when）。secrets の `.worktreeinclude` 雛形が safety の確認を通ってから載せる、という目次の備考に沿い、雛形は safety: true にして載せた。確認の担当に回すか

## 提案
```yaml
frontmatter: []
facts_to_check:
  - 「分岐元の既定（worktree.baseRef の fresh/head のどちらが既定か）」は本文に書かず省いた。fact 化するなら下記
proposals:
  - fact: {id: worktree-base-ref-default, title: worktree.baseRef の既定値, value: "fresh（リモートの既定ブランチから切る）", sources: [cc-docs-worktrees], checked: 2026-10-29, status: 要確認}
    used_in: [parallel-with-worktrees#minimal]
  - fact: {id: worktree-sandbox-resume-fix-version, title: "claude -p --resume / --continue で入った worktree に sandbox の保護がかかるようになった版", value: "2.1.314（調査 research/22 #7 による）", sources: [cc-changelog], checked: 2026-11-05, status: 要確認}
    used_in: [parallel-with-worktrees#pitfalls]
  - fact: {id: worktree-block-writes-setting-version, title: permissions.blockWritesOutsideWorkingDirectories が入った版, value: "2.1.314（research/22 #4 による）", sources: [cc-changelog], checked: 2026-11-05, status: 要確認}
    used_in: [parallel-with-worktrees#pitfalls]
  - features_attribute: {id: worktrees, enforcement: なし, reason: "作業場所を分けるだけで、ほかのセッションの書き込みを禁じる鍵でもお願いでもない。値の選び方は main が判断"}
glossary: []
```

## 検査の結果
- check_page.py を 2 回流した。エラー 0。警告 6（すべて textlint の no-doubled-joshi）
- 警告 2 件（58 行・118 行）は、道具が link の目印の間に入れる長い題名（「〜 › 〜」）が一文に数えられる誤検出。残りの 3 件（136・137 行の「が」）は、太字の見出しと文中の「が」が近いもの。読みは通るため残した

## 確かめていないこと
- 一次資料を開いていない（Web の取得 0）。本文の挙動は束の調査資料（01 E-6〔確認日 2026-10-29〕・04 H・22 #4・22 #7）に依る
- `.worktreeinclude` が「gitignore 済みで、かつ一覧に当たるファイル」だけを写す、という説明は E-6 の要約に依る。雛形のコメントの「写す対象」の言い方が公式の挙動と一致するかは、動作を確かめていない
- 分岐元 `fresh`・`head` の意味、自動削除の条件、EnterWorktree・ExitWorktree が止まる条件は調査資料の要約のまま。`worktree-<名前>` のブランチが worktree 削除後に残るかは書かなかった
- DB・ポートの衝突とディスクの消費は、二次の経験談（04 H）とその常識的な説明に依る。根拠の印は弱にした
- `batch-and-p-loops` との併用の可否は、このページでは確かめていないと本文に書いた
- macOS・Windows ネイティブ・IDE 拡張での動作は未確認（本文にもそう書いた）

## 使用量
- 道具の呼び出し：約 20 回。Web の取得：0 回
