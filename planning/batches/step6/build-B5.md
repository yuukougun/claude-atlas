# 工程6a 1段目：B5（手引きとチェックリスト）の報告

- 担当：B5。共通の指示は [brief-build.md](brief-build.md)（2026-11-04 v1）
- 書いたもの：planning/guides/・planning/checklists/・tests/guides/（試験の置き場所は自分で決めた。§3.1 の1）・この報告
- 手本：../kyopro-atlas の planning/style-guide.md と planning/checklists/（読むだけ。変えていない）

## 1. 作ったファイルと中身の要約

| ファイル | 中身 |
| --- | --- |
| `planning/guides/README.md` | 手引きとチェックリストの一覧、渡し方、直し方（F16 の3点を含む8つの決まり）、見本の表（型ごとの枠だけ。工程7で埋める） |
| `planning/guides/common.md` | 執筆の共通の手引き（22節）：読者、書いてよいものと直してよい4つのキー、冒頭、見出し、文体と用語、判断、見せ方、根拠の印、変わりやすい値、リンクの目印、出典、雛形、図と表、書かないもの、第三者、大会の規則、安全の既定、承認の要る文、段階、検査、報告の形、見本 |
| `planning/guides/<型>.md`（concept・feature・symptom・comparison・recipe・judgment・ledger・guide・hub） | 型ごとに3節：用途と必ず持つもの（design §2.2）、構成の目安（design §6.3）、型に固有の注意 |
| `planning/checklists/common.md` | 検証の共通の決まり：4つの観点の表（design §10.2）、見方、指摘の形、段階の移し方（reviewed と verified を書く人）、報告の形 |
| `planning/checklists/fact.md` | 事実・出典・鮮度（F1〜F11） |
| `planning/checklists/template.md` | 雛形の動作（T1〜T10） |
| `planning/checklists/clarity.md` | 分かりやすさ（U1〜U10） |
| `planning/checklists/render.md` | 図と描画（G1〜G7） |
| `tests/guides/test_guides.py` | 14件の試験（README §3 の直し方のうち、機械で見られるもの） |

作りの要点：

- **今有効な規則だけを置く**。決定のたびに、その規則が書いてある所を書き換える形にした。各「## 」の節の頭に「元：」の行（写した設計書・要件・決定の場所）を置き、設計書が変わったら節の番号で探せるようにした。kyopro-atlas の「〜で決めたこと」を末尾に足す形（research/20 の I1）は作らず、試験が見出しの「決めたこと」と本文の「こちらを優先」を止める
- **検査の名前**：印は「（検査：<名前>）」と「（作る予定：<名前>）」の2つ。名前は道具の名前か `check_pages.py「<検査の名前>」`（check_catalog.py の @check の名前の付け方にそろえた）。今ある検査は check_noai.py・textlint・mkdocs build --strict・H1〜H3。印は検査 15、作る予定 53
- **チェックリストを4つの観点に合わせる**：design §10.2 の観点に1つずつ。共通のこと（指摘の形・段階・報告）は checklists/common.md に1回だけ書いた
- 型の手引きには、§6.3 の目安と型に固有の注意だけを書き、共通の規則は「共通の手引き §N」で指した。語彙の値は写さず、site.yml のキー（principles・prevents・template_kinds など）を名指した
- 見本は、置き場所（README §4 の表。見本は試作のページそのもので、写しを作らない）と「構成をまねない」（共通の手引き §22）だけを書いた

## 2. 確かめたこと

- **試験**：`uv run python -m unittest discover -s tests/guides` で 14件 OK（Python 3.12.15。B1 の pyproject の PyYAML）。pyproject ができる前に `uv run --no-project --python 3.12 --with pyyaml python -m unittest discover -s tests/guides` でも通した
- **試験が誤りを見つけるか**：共通の手引きに8通りの誤り（末尾に「b1 で決めたこと」の節、ない節への参照、ない道具を「検査：」、ある道具を「作る予定：」、設計書にない節、決定にない項目、方針の番号の誤り、印の中の説明）を一時的に入れ、どれも期待した試験が落ちることを確かめてから元に戻した（戻した後も 14件 OK）
- **textlint**（B3 の設定。scratchpad の見本のページで）：共通の手引き §3 の冒頭の形で、別名の行の「plan モード」は検査されず、本文の「plan モード」は prh のエラーになる。囲みの中の判断例も検査される。和文に接するインラインコードの前後と、数と和文の間の空白の欠けはエラーで、全角の句読点と括弧の隣は空白なしで通る（共通の手引き §5 に書いた）。`npx textlint <ファイル>` がリポジトリの根から動く
- **記法**（B1 の mkdocs.yml の markdown_extensions で、scratchpad に小さなサイトを作ってビルド）：`!!! abstract "要点"`・`!!! example "判断例：…"`・`## … {#diagnosis}`・面のタブ・目印のコメント（囲みの中の箇条、段落の中）が描け、目印は HTML のコメントで残る。本文に `#` がないと、題名（title）から h1 が出る。テーマの上書き（overrides）は入れずに試した
- **並行の担当のファイル**（読むだけ）：B2 の schema/keys.yml・sources.schema.json・facts.schema.json・tools/lib/markdown.py、B3 の .textlintrc.json・prh.yml・package.json・tools/textlint_targets.py・報告、B4 の .claude/settings.json、B1 の mkdocs.yml・overrides/main.html・報告を読み、出典のファイルの形（sources と domains）、数値の提案の形、目印の対の決まり（gen:end に同じ名前）、別名の行の外し方、textlint の流し方、検査の印の今の状態をそれに合わせた
- **B3 の報告の P6**（B5 への提案）：流し方（npx と npm run lint:text）、エラー0と警告の扱い、`--fix`、別名の行の外し方、英語の題名はリンクにすること、原文は引用にすること、囲み・タブ・折りたたみの中の空行の後の段落は自分で確かめること、prh と用語集の変更は提案にすること。すべて共通の手引き §2.3・§5・§20 に入れた
- Web は使っていない

## 3. 決めたこと

### 3.1 設計書に書いていない細部

1. **置き場所と名前**：手引きは planning/guides/ に README.md（メインが使う一覧と直し方）・common.md・`<型>.md`。型の手引きの名前は site.yml の types の id と同じにし、ページの type から機械的に選べるようにした。チェックリストは planning/checklists/ に common.md と fact.md・template.md・clarity.md・render.md。試験は tests/guides/（B2 の tests/tools/ と分けた）
2. **元と印の書き方**：各節に「元：」の行。検査の印は上の2つの形。どちらも試験が形と参照の先を確かめる
3. **執筆者が直すキー**：sections・stage・updated・sources の4つ（design §10.2 と、工程5で承認された §12 の8）。§3.3 と keys.yml の outdated_advice の「目次・執筆者」とは食い違う（3.2 の1）
4. **sections**：title は見出しに合わせて直してよい。既にある節（骨格で写した節を含む）の anchor を変えず、節も外さない（ほかのページの `id#anchor` と routes が指すため）
5. **stage**：書き終えられなかったら stub のまま報告する（draft は公開されるため）
6. **冒頭**：要点の囲みは `!!! abstract "要点"`（requirements §5.3 の「kyopro-atlas の要点の囲みを引き継ぐ」）。前提の行は prerequisites を全部リンクの目印で並べ、ないときは「なし」。「何ができるか」の1文目は summary と同じ規則（design §5.3）、「いつ引くか」に機能名を答えとして書かない
7. **見出し**：H1 を書かない、平文にする、波かっこを書かない（kyopro-atlas の手引き §2.3 の python-markdown の記録を写した）
8. **根拠の印の形**：（根拠：強）（根拠：中）（根拠：弱）（類推）（根拠：強・類推）（推論・実践例なし）。公式の文書で確かめた機能の挙動には付けない
9. **判断例の形**：`!!! example "判断例：…"` に4行（状況・迷う候補・選んだもの・理由）。折りたたまない
10. **面のタブ**：名前と順はアプリ・Claude Code・API で、surfaces にある面だけ（B1 の content.tabs.link で、同じ名前のタブがページの中で一緒に切り替わる）
11. **変わりやすい値**：requirements §6.1 と design §6.7 を、手で書かないものの一覧にした（モデルの世代の名前、research preview の機能の名前、第三者のツールの成熟度を含む）
12. **リンク**：ふつうはリンクの目印。手書きは相手が draft 以上のときだけ。用語集の語は、ページで最初に出たときの1回だけ指す
13. **数値の提案のファイル**：指示がなければ報告と同じフォルダの `facts-<ページの id>.yml`。形は `proposals: [{fact: <data/facts.yml の facts の1項目>, used_in: [<id>#<anchor>]}]`（fact をそのまま写せるように、使う場所を外に出した）
14. **front matter の提案の YAML**：`frontmatter: [{id, key, before, after, reason}]`（design の「id・キー・前・後・理由」）
15. **報告の形**：執筆は9つ、検証は7つの見出しで固定。書くことのない見出しも「なし」と書き、確かめていないことは空にしない。使った手引きの版を書く
16. **作者の承認の要る文**：承認の前は本文に入れず、案を報告に書く（draft は公開されるため）。ほかのページに、約束の文と注意書き（安全を保証しない・法的な助言ではない）を足さない
17. **文書にない回避方法**：本文にも、報告にも、検証の指摘にも方法を書かない（報告も公開のリポジトリに残るため）
18. **検証の段階**：重さは必須・推奨。解決は「必須は直った、推奨は直ったか直さない理由がある」。そのページに当てたすべての観点の解決を確かめた検証役が reviewed にし、同時に verified・verified_with を書く（B2 の schema が stub と draft の verified を禁じていることと合う）。verified の日と版は、事実・出典・鮮度の検証役の報告から取る
19. **雛形の実機の確認**：雛形の動作の検証役が行う。執筆者は指示があるときだけ
20. **SVG の決まり**（文字はテキスト、viewBox と同じ比、背景を白、幅は 400 程度）：kyopro-atlas の手引き §8 から写した（check_svg.py も写すため）。試作で確かめる
21. **症状の診断の節の生成の目印**：名前を `routes` にした（案。B2 の読む層は gen の名前を問わない）
22. **試験が「作る予定：」の書き換えを求める条件**：.py の道具はファイルと引数（`--live` など）があり、検査の名前が `check("<名前>"` の形で tools/ の下に登録されていたら「できた」とみなす。textlint は `.textlintrc*`、mkdocs は mkdocs.yml、H1〜H4 は .claude/settings.json、lychee は workflows の中の語で見る

### 3.2 決めきれなかった点（5件）

1. **outdated_advice を執筆者が書くか**：design §3.3（と B2 の keys.yml）は「目次・執筆者」、§10.2 と §12 の8は「執筆者が書くのは sections・stage・updated・sources だけ」。手引きは §10.2・§12 に従い、提案にさせた。どちらに合わせるかはメインが決める
2. **まだ形のない目印**：症状の振り分け（案は `routes`）、比較の表、機能の属性（feature の要点の強制力）、雛形の折りたたみ。手引きには「作る層とともに決める」と書いた
3. **安全とデータの雛形の扱い**：確認の前に本文に目印を置くか（置いて道具が写さないのか、置かないのか）と、骨格の後に safety の印をどこに持つか（catalog は凍結される）。手引きは「確認を通るまで本文に載せない」とだけ書いた
4. **台帳の行を指す形**：feature の「古くなった助言」から台帳の行へのリンク（行の anchor）。手引きは「台帳のページで指す」とだけ書いた
5. **検証ノートの試し方**：誰が、どの道具で試すか。shows.md と工程7の指示が決める。手引きには切り離しと安全の決まりだけを書いた

## 4. 提案

1. **設計書 §3.3（メイン）**：3.2 の1を決め、§3.3 の outdated_advice の「書く人」か §10.2 を直す。B2 の keys.yml の writer も合わせる
2. **schema/site.yml（メイン）**：根拠の印の値（強・中・弱・類推・推論）を語彙に足すと、2段目の check_pages.py「根拠の印」が site.yml から読める。足したら、共通の手引き §8 の表を site.yml のキーを指す形にする
3. **2段目の検査の層**：手引きとチェックリストの印の名前（下の表）で登録するか、別の名前にしたら印を書き換える。登録すると tests/guides が「作る予定：」の書き換えを求めて落ちる（意図した動き。B1 は CI の tools の job に tests/guides を入れた）。書き換えはメインか、割り当てた担当が行う

   | 道具 | 印に使った名前 |
   | --- | --- |
   | check_pages.py | 形・執筆者のキー・sections・要点・要点の前提・別名の行・見出し・タブの面・根拠の印・facts の id・目印の外の数値・未公開のページへのリンク・sources の id・出典の URL の重なり・AI の利用の指定・断るドメインと deny・確認日・診断の順 |
   | gen_site.py | `--check`・`--page` |
   | check_templates.py | 引数なし（静的）・`--live` |
   | check_svg.py・render_pages.py | 道具の名前だけ |

   - 「執筆者のキー」「要点」「要点の前提」「見出し」「タブの面」「根拠の印」「診断の順」は design §8.6 の表にない、この手引きで足した検査の案（機械で見られる規則なので）。作らないと決めたら、印を外す
4. **2段目の作る層**：3.2 の2〜4の形を決めたら、型の手引き（symptom・comparison・feature）と共通の手引き §12 の該当の行を書き換える
5. **目次（メイン。骨格の前）**：sign の text にバッククォートがある3件（enforce の permission-rules・protected-paths・block-with-exit-2 の「`.env`」「`.claude`」「`.git`」）。キーの台帳は signs を平文とする
6. **B4（H2）**：deny は docs/llms.txt・docs/lists/**・docs/*/index.md で、nav.yml（2段目から生成）は入っていない。生成に切り替えるときに足すかを決める（共通の手引き §2.3 は、ナビゲーションを生成物に含めている）
7. **工程7の指示**：見本を決めたら README §4 の表に id を書く。検証の段階の決まり（検証の共通の決まり §4）が、ワークフローの形（4つの観点を並べるか、続けるか）と合うかを試作で確かめる

## 5. 確かめていないこと

- テーマの上書き（バッジ・下書きの帯・ページ下部）を入れた描画。2段目の前なので、記法は markdown_extensions だけで確かめた
- content.tabs.link で、同じ名前のタブが一緒に切り替わること
- 見出しの波かっこの不具合（kyopro-atlas の手引きの記録を写した。この版の python-markdown では試していない）
- SVG の決まりが、claude-atlas の CSS とダークモードで要るか（check_svg.py はまだない）
- B2・B3・B4 のファイルは作業中の版（2026-11-04 09:10 ごろ）を読んだ。後で変わると、出典と数値の形や、検査の印の状態（H1〜H3・textlint・mkdocs）が古くなる。印の状態は tests/guides が落ちて知らせる（担当が止まって最後の commit に戻されたときも、「検査：」の印で落ちる）
- 手引きの読みやすさ：執筆の担当に渡して書かせてはいない（試作で確かめる）
- 試験の「作る予定：」の検出は、検査の名前を `check("<名前>"` の形で登録する前提（check_catalog.py の形）。違う形で登録すると、書き換えを知らせない

## 6. 範囲を越えたこと

- 指示で禁じられた git を1回使った。B1 の pyproject を確かめるコマンドに、`git status --short` を出力を捨てる形（`head -0`）で混ぜてしまった（読むだけ。作業ツリーと履歴は変えていない）
- 作業用の確かめ（textlint の見本、小さなサイトのビルド、試験に誤りを入れる確かめ）は scratchpad で行い、リポジトリには残していない。試験で誤りを入れたのは自分の planning/guides/common.md だけで、元に戻した
