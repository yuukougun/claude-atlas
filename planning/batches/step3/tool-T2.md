# 工程3 T2：目次の検査に警告を2つ足す（tools/check_catalog.py）

- 版：2026-11-04
- 担当：T2（[README.md](README.md) の1段目。3段目の後に流した）
- 書いたもの：`tools/check_catalog.py`・`tests/tools/test_check_catalog.py`・この報告。`tests/tools/fixtures/` は変えていない（試験の中で写しを変える）。目次（planning/catalog/）は読んだだけ。git の操作と Web は使っていない
- 材料：[tool-T1.md](tool-T1.md)、catalog/README §4.4 の1・§4.5 の4、設計書 §8.6 の「参照」の行、統合の担当の提案（integrate-I1.md §5 の2、integrate-I4.md §5 の2、integrate-I7.md §5 の1）

## 1. 足した検査と、変えたファイル

### 1.1 足した検査

| 検査 | 重さ | 見るもの |
| --- | --- | --- |
| 推移的な前提 | 警告 | ページの prerequisites のうち、同じページのほかの前提から前提をたどって届くもの（README §4.4 の1「推移的に届くものは書かない」）。どの前提から届くかを道筋で出す |
| 逆引きの重複 | 警告 | 症状のページ（type が symptom）の signs の文と、空白と記号を除いて同じ文が、ほかのページの signs にある（README §4.5 の4）。ほかのページの側に出し、どの症状のページのどの文と同じかを添える |

出力の例。上の2行はいまの目次から、3行目は試験用の目次の対処のページに症状のページの文を足したもの：

```text
警告: planning/catalog/enforce.yaml:532: lock-side-effects: [推移的な前提] 前提「when-to-lock」は、ほかの前提「block-with-exit-2」からたどって届く: block-with-exit-2 → hooks-basics → when-to-lock（推移的に届く前提は書かない。要るなら related に移す）
警告: planning/catalog/recipes.yaml:568: office-paperwork: [推移的な前提] 前提「where-your-data-goes」は、ほかの前提「entrusted-data」「default-safety-settings」からたどって届く: entrusted-data → where-your-data-goes、default-safety-settings → where-your-data-goes（推移的に届く前提は書かない。要るなら related に移す）
警告: planning/catalog/enforce.yaml:5: hooks-basics: [逆引きの重複] signs の「CLAUDE.md に書いたのに守られない」が、症状のページ instructions-ignored の sign「CLAUDE.md に書いたのに守られない」と同じ（逆引きで同じ困りごとが二か所に出る。対処のページには、より狭い場面の困りごとか、やりたいことの形で置く）
```

### 1.2 作り（T1 の決まりに合わせた点）

- どちらも `@check(名前, 重さ)` で登録した1検査1関数。指摘は `at(ページ, 内容, 関わる分野)` で返し、重さは登録で決まる。`-h` の一覧には docstring の最初の段落が出る
- 並び：「推移的な前提」は「必須の前提」の後に、「逆引きの重複」は「症状の signs」の後に置いた（前提を見る検査と、signs を見る検査をそれぞれ並べるため）。検査は33（エラー10・警告23）になった
- 語彙をコードに書いていない。症状のページは T1 の規則の定数 `SYMPTOM_TYPE` で決める（site.yml の types にあるかは、T1 の読む層が確かめている）。記号は文字の一覧を書かず、Unicode の分類で決める（§1.4 の3）。案内の文にも語彙の値を書かない（goal ではなく「やりたいこと」と書いた）
- 読む層は変えていない。補助の関数は検査の層に置いた：`prerequisite_targets`（前提の指す先のページの id）・`reached_from`（前提をたどる幅優先の探索）・`path_to`（道筋）・`sign_key`（文を比べる形）

### 1.3 推移的な前提で決めた点

1. **id#anchor**：ページの id（# の前）で比べる。同じページを2回書いたもの（`a` と `a#x`）は1つにまとめてから比べる（2回あること自体は「前提と関連の重複」のエラーが出す）
2. **たどる範囲**：分野のファイルにあるページの prerequisites をたどる。ファイルのまだない分野の候補や存在しない id も、ほかのページの前提に書いてあれば「届いた」とするが、その先はたどらない。いまの目次では前提の471件がすべてページに解決するので、この扱いで結果は変わらない
3. **循環**：一度見た id は二度たどらないので止まる。循環の中の2ページを両方とも前提にしたページには、互いに届くので2件出る（循環そのものは「循環」のエラー）
4. **そのページ自身を通る道は数えない**：P の前提 Y が P を前提にしている（P → Y → P の循環）と、P のほかの前提がすべて Y から届くように見える。これは循環のせいなので数えない
5. **関わる分野**：そのページの分野だけにした。直すのはそのページの prerequisites で、道筋の途中のページは直さなくてよい
6. **related は見ない**：推移的に届くページを related に置くのはよい（README §4.4 の1は prerequisites の規則）
7. **1件の単位**：（ページ, 届く前提）の組。2つ以上の前提から届くときは、1件に道筋を並べる。道筋は最短のもの

### 1.4 逆引きの重複で決めた点

1. **比べる文**：症状のページの signs は type を問わずすべて。ほかのページの signs も type を問わない（type が違っても、同じ文は逆引きで二か所に出る）。いまの目次では、症状のページの signs の105文はすべて type が symptom
2. **ほかのページ**
   - 症状のページの中の同じ文どうしは比べない
   - 症状のページでないページどうしの同じ文は指摘しない。統合の担当が、逆引きで1項目に並べるためにわざとそろえたものがある（いまの目次に13組。例：「長い作業を明日も続けたい」が resume-and-branch・handoff-documents・progress-files の3ページ）
   - 症状のページどうしで同じ文があれば、両方のページに出す（どちらから見ても相手が「ほかのページ」なので）。案内の文は「どちらの症状のページで受けるかを決める」にした。いまの目次にはない
3. **比べる形**（`sign_key`）
   - NFKC で全角と半角をそろえる（「ＣＬＡＵＤＥ．ｍｄ」と「CLAUDE.md」を同じにする）。NFKC は指示になかったので足した点。外しても、いまの目次の結果（0件）は変わらない
   - Unicode の分類が句読点（P）・記号（S）・区切り（Z）・制御など（C）の文字を除く。指示の「」『』、。・,.!?！？（）() と、半角と全角の空白・タブ・改行は、すべてこれに入る
   - 長音「ー」と「々」は文字なので残す。大文字と小文字はそろえない
4. **言い換えは見ない**：README §4.5 の4は言い換えも重ねないとするが、この検査が見るのは空白と記号を除いて同じ文だけ（§4）
5. **関わる分野**：ほかのページの分野と、当たった症状のページの分野（symptoms）。`--field symptoms` でも出る
6. **1件の単位**：ほかのページの sign 1つ。1つの文が2つ以上の症状のページに当たったら、1件に全部を並べる

### 1.5 変えたファイル

| ファイル | 変えたこと |
| --- | --- |
| `tools/check_catalog.py` | 検査2つと補助の関数4つ、`import unicodedata` を足した（いまは1,848行）。T1 の検査と出力は変えていない |
| `tests/tools/test_check_catalog.py` | 試験14を足した（§2）。T1 の `TestCounts.test_prerequisites` の前提の組を替えた。もとの組（completion-check・fact-check・request-vs-lock・hooks-basics・permissions-deny）は fact-check → completion-check と hooks-basics → request-vs-lock で推移的に届き、新しい警告が出るため。互いに届かない5つ（fact-check・done-but-not-done・hooks-basics・permissions-deny・instructions-ignored）にした。試験のねらい（4つまではよく、5つで警告）は変えていない |
| `tests/tools/fixtures/` | 変えていない |

## 2. 試験の数と結果

```text
$ cd /home/yuuki/projects/kyopro2/claude-atlas && python3 -m unittest discover -s tests/tools
................................................................................................................................
----------------------------------------------------------------------
Ran 128 tests in 4.332s

OK
```

試験は128（T1 の114に14を足した）で、すべて通る（Python 3.10.12・PyYAML 5.4.1）。足した試験：

| 試験 | 見るもの | 結果の形 |
| --- | --- | --- |
| TestTransitivePrerequisites.test_reached_through_another_prerequisite | 1段で届く前提。内容の文・重さ・関わる分野（そのページの分野だけ）・出力の行の形 | 見つかる |
| 〃 test_path_over_pages_from_two_prerequisites | 2段の道筋と、2つの前提から届くもの（1件に道筋を並べる） | 見つかる |
| 〃 test_anchor_is_compared_by_page_id | id#anchor をページの id で比べる（そのページの前提と、道筋の途中のページの前提の両方） | 見つかる |
| 〃 test_candidate_without_field_file | ファイルのまだない分野の候補（verifier-basics）にも届く | 見つかる |
| 〃 test_cycle_does_not_stop_the_check | 循環の中の2ページを両方とも前提にしても止まり、2件出る | 見つかる |
| 〃 test_prerequisites_that_do_not_reach_each_other | 同じページを前提にする2ページは互いに届かない。related は見ない | 見つからない |
| 〃 test_path_through_the_page_itself_is_not_counted | そのページ自身を通る道は数えない（循環のエラーだけが出る） | 見つからない |
| TestGraph.test_reached_from_on_random_graphs | 乱数で作った300のグラフ（循環あり、キーにない id あり）で、届く id と最短の道を総当たりと比べる。avoid を通らない | 補助の関数 |
| TestReverseIndexOverlap.test_symptom_sentence_on_another_page | 同じ文。内容の文・重さ・関わる分野（enforce と symptoms。verify では出ない）・出力の行の形 | 見つかる |
| 〃 test_spaces_and_symbols_are_ignored | 空白と記号だけが違う文。type が goal でも当たる | 見つかる |
| 〃 test_two_symptom_pages_and_another_page | 症状のページどうし（両方に出る）と、2つの症状のページに当たる文（1件に並べる） | 見つかる |
| 〃 test_narrower_sentences_and_non_symptom_pages_are_fine | より狭い場面の困りごと（README の例）と、症状のページでないページどうしの同じ文 | 見つからない |
| 〃 test_same_symptom_page_is_not_compared | 症状のページの中にある、記号だけが違う同じ文 | 見つからない |
| 〃 test_sign_key | 比べる形。指示の記号と空白をすべて除く・全角と半角・長音と「々」は残す・違う文は違う | 補助の関数 |

- 試験が誤りを捕まえるかを、道具をわざと壊した写し（scratchpad）で確かめた。6通りとも、ねらった試験が落ちた
  - 自分を通る道を数える → test_path_through_the_page_itself_is_not_counted と test_reached_from_on_random_graphs
  - NFKC を外す → test_sign_key
  - 空白だけを除く → test_sign_key と test_spaces_and_symbols_are_ignored
  - 同じ症状のページの文とも比べる → ほぼすべて（症状のページが自分の文に当たる）
  - anchor を付けたまま比べる → test_anchor_is_compared_by_page_id
  - ページに解決した前提だけをたどる → test_candidate_without_field_file
- T1 の `test_every_check_has_a_test`（登録した検査すべてに試験がある）と `test_help`（`-h` に全部の検査が出る）は、足した2つも見ている

## 3. いまの目次に流した結果

```text
$ python3 tools/check_catalog.py -q
エラー 0 件、警告 39 件（推移的な前提 35・比例則 4）。-q で出していない（分野のファイル 23・ページ 361 を読んだ）
```

足す前はエラー0・警告4（比例則4。3段目の結果と同じ）。新しい警告は、**推移的な前提が35件（32ページ）、逆引きの重複が0件**。

推移的な前提の分野ごとの内訳（指摘の出るページの分野）：

| 分野 | 件 | ページ |
| --- | --- | --- |
| symptoms | 18 | 15 |
| delegate | 5 | 5 |
| recipes | 5 | 5 |
| enforce | 2 | 2 |
| app・contest・extend・japanese・safety | 各1 | 各1 |
| 計 | 35 | 32 |

- I7 が自分のスクリプトで数えた数（integrate-I7.md §5 の1：symptoms 15ページ18件・recipes 5・delegate 5・enforce 2・app・contest・extend・japanese・safety 各1）と、ページも前提もちょうど合う
- 道筋の段数：44の道筋のうち、1段で届くもの35・2段6・3段2・4段1。2つ以上の前提から届くものが9件。例：dynamic-workflows の permission-rules は choosing-parallel-modes から3段（→ humans-set-the-parallel-limit → five-questions-before-delegating → permission-rules）、performance-tuning の evidence-not-reports は differential-testing から4段。何段かたどる道筋の3つ（この2つと、instructions-ignored の where-instructions-sit）は、YAML を別に読んで前提を確かめた
- **外しても第一波は変わらない**：35件の前提をすべて prerequisites から外した写しで流すと、第一波は125ページのまま（同じページの集合）で、各ページから前提でたどって届くページも変わらず、ほかの検査の指摘も新しく出なかった（比例則・入ってくる道を含む）。工程4の直しでは、外したものを related に移すかだけを決めればよい（instructions-ignored の related はいま20件で上限なので、移すならほかを外す）
- 逆引きの重複が0件であることは、別の書き方（正規表現で指示の記号と空白だけを除き、NFKC を使わない）でも確かめた。比べたのは、症状のページの105文と、ほかのページの signs の802文（goal 383・symptom 281・situation 138）。3段目の README の結果（症状のページの sign と同じ文が対処のページにあるものは0件）と合う
- `--field symptoms` では警告18（推移的な前提18）。新しい2つの検査はそれぞれ数ミリ秒で、道具全体は約1.1秒

## 4. 確かめていないこと

- **言い換えの重なりは見つけない**：README §4.5 の4は「同じ文も、言い換えも」重ねないとするが、この検査は空白と記号を除いて同じ文だけを見る。意味の近い組（3段目の README の「似た組（9組）」、integrate-I1.md §7 の2に挙げた組など）は見つけない。似ている度合いで見る案は作っていない（当たらない指摘が多くなりそうなため）
- 大文字と小文字だけが違う文（「claude.md」と「CLAUDE.md」）は同じにしていない。いまの目次にそういう組があるかは数えていない
- 症状のページどうしの同じ文は、いまの目次にない。両方に出す扱い（§1.4 の2）がよいかは、出たときに見直す
- 推移的な前提の35件を、それぞれ外すべきかは見ていない。I7 は、症状のページは原因ごとの対処の中心を前提に並べてよいと README に例外として書く案（integrate-I7.md §5 の1の (b)）も出している。例外にするなら型か分野で除けるが、いまは作っていない（決めるのはメイン）
- 表示の行は、ほかの検査と同じくページの始まりの行（`- id:` の行）。sign や前提の行は出さない（T1 の決まり）
- Python 3.12 では流していない（3.10.12 だけ）。3.10 にない書き方は使っていない
- ページが500を超えたときの速さは測っていない（前提が2つ以上のページごとに、前提の数だけ幅優先でたどる。いまの361ページで数ミリ秒）
- 設計書 §8.6 の front matter の検査（工程6）には、まだ移していない
