# path-scoped-rules 執筆報告

## 書いたファイル
- docs/extend/path-scoped-rules.md（stub から移した。stage は draft、updated は 2026-11-05。front matter で変えたのは sections〔6 節を足した〕・sources〔cc-docs-memory・cc-docs-features-overview-ja・cc-docs-context-window・claude-blog-steering-code-skills-hooks。すべて既存の id〕・stage・updated）
- snippets/path-scoped-rules/api-rule.md と .expect.yaml（目次の案）、check-loaded.md と .expect.yaml（足した）
- planning/batches/step8/pages/path-scoped-rules/facts-proposal.yml
- stubs/extend/path-scoped-rules.md は移したので削除した。data/sources.d は、新しい出典がないので作っていない

## 必ず持つものの対応
- 機能の属性のバッジ：テンプレートが出す。要点の「強制力」は `#`（冒頭の要点、feature の目印）、読み込みの時期・コスト・圧縮で残るかは `#after-compaction`（compare の目印）
- tracks（rules）：front matter。属性の表が `#after-compaction`
- 1機能1ページ・節に分ける：`#when`・`#minimal`・`#templates`・`#after-compaction`・`#limits`・`#compare`・`#outdated`
- level：front matter（任せる）
- 構成の目安：要点（冒頭）→ 使いどころ `#when` → 最小の使い方（面のタブ。面は claude-code の 1 つ）`#minimal` → 雛形 `#templates` → 効かない場面・落とし穴 `#limits` → 比べる相手 `#compare` → 古くなった助言 `#outdated`。`#after-compaction` は目次の指定の節

## メインに判断してほしいこと
- 古くなった助言：この機能の台帳の行がないので、台帳は指さず、`#outdated` に束の注記にある「CLAUDE.md は再注入される」の言い切りと、`@import` でコンテキストが減るという説明の 2 つを短く書いた。後者は束の調査資料（Serverworks の記事）が根拠で、公式の文書では確かめていない。台帳に行を足すか、`#outdated` の 2 点目を外すかを決めてほしい
- 面のタブは claude-code の 1 つだけ（surfaces がその 1 面のため）。1 面だけのタブを残すか、外すかを決めてほしい

## 提案
- 数値：facts-proposal.yml に、必要なときに読み込まれるファイルの文字数の上限を 1 件（used_in は path-scoped-rules#limits）。本文はこの数字なしで読めるので、目印は置いていない。承認後に目印を足す
- 用語集：新しい語の提案なし

## 検査の結果
- check_page.py を 2 回流した。1 回目はエラー 3・警告 6（「frontmatter」の表記と、助詞「に」の重なり）。直して 2 回目はエラー 0・警告 0

## 確かめていないこと
- 公式の memory のページ（1 回取得）で paths の書き方・引き金・シンボリックリンク・上限・フロントマターの失敗時の挙動を確かめた。ほかの面（IDE 拡張・ほかの OS）の動作は確かめていない
- 引き金より前の作業に規約が入っていないことがある、という文は推論（本文に「推論・実践例なし」と書いた）
- `/context all` が条件付きの rules を一覧に出すかは確かめていない（本文に未確認と書いた）
- 雛形は動かしていない。`paths` の相対の基準・`~/.claude/rules/` の扱いは公式の文書の記述のとおりで、実機では試していない
- 取り込み（@import）でコンテキストが減らない件は公式で確かめていない（上記）

## 使用量
- 道具の呼び出し 約 17 回、Web の取得 1 回（code.claude.com の memory）
