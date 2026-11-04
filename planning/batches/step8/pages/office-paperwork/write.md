# write.md：office-paperwork

## 書いたファイル

- `docs/recipes/office-paperwork.md`（stub から移した。stage を draft、updated を 2026-11-05）
  - front matter で変えたキー：`sections`（末尾に `check`「全体の確かめ方」・`troubleshoot`「うまくいかないとき」を足した。既存の 5 節の anchor はそのまま）、`sources`（cc-docs-skills・hc-skills-what・hc-skills-use。束の data の項目が挙げる既存の id）、`stage`、`updated`
- `snippets/office-paperwork/`：`weekly-report-request`（prompt）・`expense-list-request`（prompt。safety: true）・`chores-repo-layout`（other。目次の templates の案。拡張子 .txt）・`weekly-report-skill`（skill）。それぞれ `.expect.yaml` つき
- 出典の新規ファイル（`data/sources.d/office-paperwork.yml`）は作っていない

## 必ず持つものの対応

- 手順：`#human-ai-human`（3 段 + 各段の終わりの確かめ）、`#grow-procedures`（会話→手順ファイル→スキルの 3 段）、`#work-folder`（フォルダの作り方）
- 確かめる・縛るのページへの道：front matter の `prerequisites`（entrusted-data・default-safety-settings）と `related`。本文では要点の「前提」、`#work-folder`（default-safety-settings#by-stage・permission-modes-overview）、`#private-data`（entrusted-data・where-your-data-goes・protecting-secrets）、`#grow-procedures`（権限の設定で縛る）、`#check`
- level：front matter の `level: 任せる`。`#grow-procedures` と `#chores-repo` は `仕組みにする`（既存のまま）
- 構成の目安の対応：要点 → 先に整える守り（`#work-folder`・`#private-data`）→ 手順（`#human-ai-human`・`#grow-procedures`・`#chores-repo`）→ 確かめ方（`#check`）→ 失敗したとき（`#troubleshoot`）。節の並びは目次の sections の順を保ったので、守りの節が手順の節より後になる。`#human-ai-human` の冒頭で守りの節を先に指している

## メインに判断してほしいこと

- 節の並び：手順の節（human-ai-human）が、守りの節（work-folder・private-data）より先にある。目次の sections の順を変えないために保った。守りを先にするなら、並べ替えの許可がほしい
- `#work-folder` に「確認が出る既定のまま始める」と書いた（モードの具体名は書かず、段階の判断は default-safety-settings#by-stage に任せた）。decisions 2026-11-03「安全の既定の勧め方」と矛盾しないかの確認がほしい
- アプリのスキル（page: skills-in-the-app）は、束の「指せる節」にないので link していない。本文は「アプリ側の設定は面ごとに違うので公式の文書で確かめる」とした

## 提案

- 数値の提案：なし（本文に変わりやすい値を書いていない）
- front matter の提案：なし
- 用語集・prh：なし

## 検査の結果

- 書き終えた後：エラー 0・警告 14。直した後：エラー 0・警告 10
- 直したもの：expect.yaml の YAML の誤り（コロンを含む then を引用符で囲んだ）、max-ten 2 件、no-doubled-joshi の一部
- 残した警告 10 件（すべて no-doubled-joshi）：大半は link の目印の間に道具が入れる題名（「… › …」）に含まれる「に」や、「…にある」と連なる所で、題名は書き手が変えられない。`#chores-repo`・`#private-data` などの文の途中の「に」の重なりも含む。意味は崩れないので残した

## 確かめていないこと

- 雛形の動作（Claude Code での実行）。どれも動かしていない
- `disable-model-invocation: true` の挙動は束の data の note による。実機では見ていない
- アプリで添付ファイルとコネクタが境界になるという書き方、Claude Code が起動したフォルダを作業の範囲の起点にするという書き方は、公式の文書を開いて確かめていない（束と一般の理解による）
- Windows・macOS と IDE 拡張の動作は、本文で未確認とした
- 一次資料の Web 取得は行っていない

## 使用量

- 道具の呼び出し：約 20 回（Read 4・Bash 5・Write 10・Edit 6 ほか）。Web の取得：0 回
