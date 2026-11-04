# write.md：agent-view-and-background

## 書いたファイル
- `docs/delegate/agent-view-and-background.md`（stubs から移した。stage は draft、updated は 2026-11-05）
- `snippets/agent-view-and-background/background-task-prompt.txt` と `.expect.yaml`（目次の templates は「なし」。分かりやすさのために 1 つ足した）
- front matter で変えたキー：`sections`（節を 6 つ足した。既存の 2 つの anchor は変えず、順を使いどころ→守り→使い方→雛形→cross-session→落とし穴→比較→古い助言にした）、`sources`（既存の 5 つの id）、`stage`、`updated`

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す。本文では `#compare` の `compare 成熟度 入った版` の表と、導入の `feature agent-view/maturity`
- `tracks`：front matter の `tracks: [agent-view, cross-session-messaging]`（束の data と同じ。変えていない）
- 要点（強制力のバッジ）：data の機能に `enforcement` がないため目印を置かず、要点の「止められるもの」に、画面は縛らず権限とフックで先に置く、と書いた（冒頭の要点）
- 使いどころ（どの原因を防ぐか）：`#what-fits`（確かめていない）と `#guards-first`
- 最小の使い方（面のタブ）：`#minimal`（「Claude Code」のタブ 1 つ。surfaces が claude-code だけのため）
- 雛形：`#templates`
- 効かない場面・落とし穴：`#pitfalls`
- 比べる相手：`#compare`（`choosing-parallel-modes#compare` を link）
- 古くなった助言：`#outdated`（`outdated-advice-ledger#tmux-agent-orgs`）
- level：front matter の `level: 仕組みにする`（変えていない）

## メインに判断してほしいこと
- 要点の「強制力」：features の agent-view・cross-session-messaging に `enforcement` の値を足すか、この型でも強制力の行を省いてよいかを決めてほしい。いまは文章で代えた
- 本文の「確認 2026-11-05」は、公式の agent-view と cross-session-messaging の文書を今日取得して確かめたことによる。data の checked は 2026-11-04 のまま

## 提案
```yaml
frontmatter: []
proposals:
  - fact: {id: agent-view-worktree-delete, title: "agent view で消すと worktree も消える（未コミットの変更があっても。未 push のコミットがあると消せない）", value: "挙動の記述", sources: [cc-docs-agent-view], checked: 2026-11-05, status: 確認済み}
    used_in: [agent-view-and-background#pitfalls]
```
上の提案は任意。本文は目印なしで挙動を文章で書き、「確認 2026-11-05」を付けた。`features` の note に入れる案でもよい。用語集への追加の提案はなし。

## 検査の結果
- 1 回目：エラー 0・警告 3（助詞の重複）。2 回目：エラー 0・警告 1（71 行目の「に」の重複）。2 回目の後に 71 行目を「背景へ投げる前に」に直したが、再検査はしていない（流す回数の上限のため）

## 確かめていないこと
- 雛形の動作（実機で背景に投げていない）
- キー操作（`Space` でのぞく・`Enter` で入る・`←` で出る）は本文に書かず、変わりうるとだけ書いた。`claude agents`・`claude --bg`・`/background` は束と公式の文書の写し
- cross-session messaging の idle の知らせの版と、既定の保留の挙動は公式の文書の要約で、実機では未確認
- WSL 以外の OS と IDE 拡張の動作

## 使用量
- 道具の呼び出し：約 14 回。Web の取得：2 回（code.claude.com の agent-view と cross-session-messaging。ドメインは公式で、check_noai は流していない）
