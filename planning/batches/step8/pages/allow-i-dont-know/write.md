# write: allow-i-dont-know

## 書いたファイル
- docs/prompting/allow-i-dont-know.md（stub から移動。front matter は sections に what-it-targets・limits を足し、sources に既存の 5 id を入れ、stage を draft、updated を 2026-11-05 にした）
- snippets/allow-i-dont-know/escape-hatch.txt・.expect.yaml、source-only.txt・.expect.yaml
- 新しい出典はなし（sources は data/sources.yml にある id のみ。data/sources.d/allow-i-dont-know.yml は作っていない）

## 必ず持つものの対応
- 原理・原因に関わる：`#what-it-targets`（principle 「確かめる」、prevents 「確かめていない」「見えていない」を名指し）
- `principle` の名指し：`#what-it-targets`
- `prevents` の名指し：`#what-it-targets`（「見えていない」は `#source-only` でも）
- `pitfalls`：front matter に pitfalls のキーがない。代わりに落とし穴を `#limits` に置いた
- level を持つ（使う）：front matter。要点の最初は「何が分かるか」
- 型の構成（技法）：Before/After は `#escape-hatch`、何が変わる・なぜ効くかは `#what-it-targets`、効かない場面・やりすぎは `#limits`

## メインに判断してほしいこと
- 「ある報告に〜偽の flag を大量に提出した」（調査 11 の p34#205）は、束に出典 URL がなく、束の出典の一覧にもない。（根拠：弱・単発・版依存）として出典なしで書いた。元の出典を確かめて足すか、削るか
- 競技の実践者の指摘は chokudai の記事（sources に入れた）。個人名は本文に出していない

## 提案
```yaml
frontmatter:
  - {id: allow-i-dont-know, key: pitfalls, before: null, after: [言葉の許可だけを頼りにする, やりすぎて答えられることまで断らせる], reason: "型の必ず持つものに pitfalls があるため。値の形は schema 次第"}
```

## 検査の結果
- 1 回目：エラー 0・警告 7（助詞の重なり・文の長さ）。直して 2 回目：エラー 0・警告 4（助詞「に」「も」「は」の重なり）。残した警告は読みやすさを損ねないと判断
- 生成で link・snippet の間が埋まった

## 確かめていないこと
- 雛形の動作（新しいセッションでの試行）。expect は観察の予想
- 「条件に応じた『推測：』の印の付き方」「分かれば答えられることも書かせる」は実験していない（後者は「推論・実践例なし」と明記）
- 公式の文書の記述は束の写しに基づき、原文を再度開いていない。Anthropic の解釈可能性研究の対象モデルの名は束にないので書かず、「その研究のモデル」とした
- Claude Code の `CLAUDE.md` への書き方の記述は一般論で、効き目は試していない

## 使用量
- 道具の呼び出し 約 10 回（Read 2、Bash 5、Write 5 など）、Web の取得 0 回
