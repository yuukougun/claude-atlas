# write.md：too-much-project-knowledge（feature・app）

## 書いたファイル

- `docs/app/too-much-project-knowledge.md`（stubs から mv。stage を draft、updated を 2026-11-05。sections に pitfalls・compare を足した。sources に hc-projects-manage・hc-usage-limits・jinrai-claude-projects-guide を足した。いずれも既存の id）
- `snippets/too-much-project-knowledge/check-knowledge-use.txt` と `.expect.yaml`（kind: prompt。引用とファイル名を先に出させる依頼）
- `data/sources.d/` は新しい出典がないので書いていない

## 必ず持つものの対応

- 機能の属性のバッジ：テンプレートが出す。本文は導入で `feature projects/maturity` の目印だけ使った。強制力の属性は data の projects に値がなく、`feature` の目印を置いていない（本文では「ナレッジは読ませる仕組みではない」と一言書いた：#rag-mode の末尾の候補 3 つ、#pitfalls）
- `tracks`（projects）：front matter。既存どおり
- 1機能1ページ・節に分ける：#rag-mode、#curate、#pitfalls、#compare
- level（整える）：front matter。既存どおり
- 要点（強制力・確認日と版のバッジ）：冒頭の要点の囲み。バッジはテンプレート
- 使いどころ（どの原因を防ぐか）：#rag-mode（見えていない・散らかっている）、#curate の冒頭
- 最小の使い方（面のタブ）：surfaces が app だけなのでタブを置かない。手順は #curate
- 雛形：#rag-mode の `check-knowledge-use`
- 効かない場面・落とし穴：#pitfalls
- 比べる相手：#compare
- 古くなった助言：台帳の行が束にない（outdated_advice なし）ので置かない

## メインに判断してほしいこと

- 強制力の属性：projects の項目に enforcement がない。ナレッジは「使える状態にするだけ」と本文に書いたが、バッジの値は data 側の判断
- 本文は RAG mode の細部（切り替えの時点・表示・読まれる部分）を「確かめていない」と明示した。注記（materials の notes）に従った。公式の説明を追加で確かめるなら、hc-projects-manage の RAG の節の再確認が要る

## 提案

- 用語集：「RAG（mode）」を追加する案。本文では「資料の全体を毎回渡さず、質問に関係する部分を検索で取り出して渡す方式」の一般の意味を短く書き、Claude の実装は確かめていないと添えた
- front matter・数値の提案はなし

## 検査の結果

- `check_page.py` を 2 回流した。エラー 0。警告 4 を残した（直した後の再実行は上限のため流していない）
  - 42:42 no-doubled-joshi「が」：導入の段落。文の切り直しで直る見込み
  - 101:24 no-doubled-joshi「と」・101:5142 sentence-length(122)：判断例の囲み（囲みの中の字下げした行は textlint の数え方が長くなる）。理由の行を短くした後も残った
  - 122:492 no-doubled-joshi「に」：#compare の段落
- 4 件とも文体の警告で、事実や目印の誤りではない。検証の担当の直しに任せる

## 確かめていないこと

- RAG mode の切り替えの時点・画面表示・切り替え後に読まれる範囲・答えの質への影響。束の材料にも一次資料にもなく、Web も取得していない
- 無料プランでの扱い（公式は有料プランについてだけ書く）
- 雛形の動作（Claude が引用とファイル名を実際に返すか）。expect に観察として書いただけで、試していない
- `link` で指した long-chat-limits ページの節の中身（ページ単位で指した）
- 本文の「3 つの候補」のうち 1 つ目は（推論・実践例なし）と印を付けた

## 使用量

- 道具の呼び出し：Read 3、Bash 8、Write 4、Edit 4（概算）。Web の取得 0
