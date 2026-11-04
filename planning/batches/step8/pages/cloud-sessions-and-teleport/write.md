# write.md：cloud-sessions-and-teleport（feature・cli）

## 書いたファイル
- `docs/cli/cloud-sessions-and-teleport.md`（stubs から mv。stage は draft）
  - front matter で変えたキー：`sections`（limits・compare・outdated の 3 節を足した）、`sources`（既存の id 5 つ）、`stage`（draft）、`updated`（2026-11-05）
- `snippets/cloud-sessions-and-teleport/cloud-task-plan.md`・`.expect.yaml`（計画ファイルの雛形。prompt）
- `snippets/cloud-sessions-and-teleport/cloud-repo-settings.json`・`.expect.yaml`（リポジトリに置く deny ルール。settings・safety true）
- `data/sources.d/` のファイルは作らなかった（出典は既にある id だけ。cc-docs-cloud-environments は別ページの sources.d が足したもの）

## 必ず持つものの対応
- 機能の属性のバッジ：冒頭の要点「成熟度」の行（`feature maturity` の目印、anchor なし）。強制力は持たない（下の「メインに判断してほしいこと」1）。ほかの属性のバッジはテンプレートが出す
- `tracks: [cloud-sessions]`：front matter に既にある（変えていない）
- 1 機能 1 ページ・節に分ける：`#what-to-send`・`#settings`・`#teleport`・`#limits`・`#compare`・`#outdated`
- level（任せる）：front matter に既にある
- 構成の目安の各項
  - 要点：冒頭の囲み
  - 使いどころ（どの原因を防ぐか）：`#what-to-send`（境界がない。先に整えるものの小節）
  - 最小の使い方：`#what-to-send` の「最小の使い方」の小節（面が claude-code だけなのでタブは置かない）
  - 雛形：`#what-to-send`（cloud-task-plan）と `#settings`（cloud-repo-settings）
  - 効かない場面・落とし穴：`#limits`
  - 比べる相手：`#compare`
  - 古くなった助言：`#outdated`（台帳の行 code-on-the-web-remote を link で指した）

## メインに判断してほしいこと
1. `cloud-sessions` の features に「強制力」の属性がない（束の data は maturity のみ）。feature 型は要点に強制力を足す決まりだが、手で書くと決まりに反するので、成熟度だけにした。属性の追加を data で判断してほしい
2. 本文の、クラウドが読むもの・読まないものの表は、公式の文書（settings・cloud-environments。確認日 2026-11-05）の写しの要約で、手書きである。変わりやすいので、data の機能の項目に載せるか、現状のまま確認日付きの本文にするかを判断してほしい
3. 使えるプラン（Pro・Max・Ultra・Team・Enterprise の席）は変わりやすい値として本文に書かず、公式へのリンクにした。数値ファイルにプランの項目があれば、目印に替えられる

## 提案
```yaml
frontmatter: []
facts: []
```
- 用語集：「teleport」の項目を足すなら「クラウドのセッションを手元の端末に取り込む操作」の定義が要る（本文は導入で短く定義した）
- 入れ子の `claude -p` の不具合（CHANGELOG v2.1.317）は、版を手で書かない決まりで、版なしで書いた。入った版を data に置くなら、`used_in: [cloud-sessions-and-teleport#limits]`

## 検査の結果
- `check_page.py` を 2 回流した。1 回目はエラー 2（prh：hook・subagent）・警告 8、2 回目はエラー 0・警告 6
- 残した警告 6：no-doubled-joshi が 6 件（51 行目と 181 行目は、link の目印の中の題名が入った長い文で、道具が書く部分を含む）。ほかは読みやすさを優先して残した（130・225・229・230 行目）

## 確かめていないこと
- クラウドのセッションで実際に deny ルールが効くか、雛形が動くかは試していない（雛形は動作未確認の旨を道具が書く）
- 公式の文書の内容は、Web で 3 回（claude-code-on-the-web・settings・cloud-environments）読んだ時点のもの。Projects のスレッドや複数リポジトリのセッションの扱いは、公式へのリンクにとどめた
- Auto-fix、`/web-setup`、Desktop からクラウドへ送る操作、self-hosted 環境は、概念か一文だけで、手順は書いていない
- WSL・Linux 以外の OS の動作は未確認（本文にも書いた）
- ネットワークのアクセスレベル（既定が制限されること）は、公式の一文を要約した。レベル名は書いていない

## 使用量
- 道具の呼び出し：約 22 回。Web の取得：3 回（いずれも code.claude.com。check_noai.py で noai の指定がないことを確かめた）
