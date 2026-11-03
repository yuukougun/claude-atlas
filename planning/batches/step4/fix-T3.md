# 工程4 T3：目次の検査に routes と第一波の内訳を足す（tools/check_catalog.py）

- 版：2026-11-04
- 担当：T3（[README.md](README.md) の2段目）
- 書いたもの：`tools/check_catalog.py`・`tests/tools/test_check_catalog.py`・`tests/tools/fixtures/small/` の4ファイル・`schema/site.yml`（first_wave の項目だけ）・`planning/catalog/README.md`・この報告。目次の分野のファイルは読んだだけ。git の操作と Web は使っていない
- 材料：[design-review](../../design-review.md) の DR-01〜DR-04（特に DR-02）、[tool-T1.md](../step3/tool-T1.md)・[tool-T2.md](../step3/tool-T2.md)、設計書第2版（D1）の §2.3・§3.1・§3.3・§4.1・§5.3・§10.1（読んだだけ）、メインの追加の指示3つ（§5）
- 置き換えの手順：道具・site.yml・README は scratchpad の写しで作って試験を通し、同じフォルダの一時ファイルに写してから名前を変えて置き換えた（書きかけの状態は一度も見えない）。順は site.yml（前の道具は first_wave を読まないので無害）→ 道具 → README。置き換えの前後で、F1〜F6 が流している本物の目次のエラーは前の道具と同じ5件（§3）

## 1. 足した検査と数え方、変えたファイル

### 1.1 routes の形

型が symptom のページだけが持てる任意のキー。`routes: [{cause: <値>, to: [<id か id#anchor>, …]}]`。cause は site.yml の prevents か pitfalls の値、to は1件以上。道具は PAGE_SHAPE に `routes`（マッピングのリスト）、PART_SHAPES に `{cause: 文字列, to: 文字列のリスト}` を足し、形・必須・知らない項目の検査をほかのキーと同じ仕組みで当てる。参照の解決は前提・関連と同じ `Catalog.resolve()`。

### 1.2 検査

重さは指示の案のまま（変えたものはない）。「足した」は指示の一覧になく私が足したもの（理由は §1.4）。

| 検査 | 重さ | 見るもの | |
| --- | --- | --- | --- |
| routes（新） | エラー | symptom でないページの routes。cause の to が空 | 指示 |
| 語彙（既存に足した） | エラー | routes の cause が site.yml の prevents・pitfalls にない | 指示 |
| 参照（既存に足した） | エラー | routes の to が解決しない（存在しない id、merged・dropped の候補、`id#anchor` の anchor が相手の sections にない、空の id） | 指示 |
| 必須・形（既存に足した） | エラー | routes の要素に cause・to がない。routes がリストでない、要素がマッピングでない、cause が文字列でない、to がリストでない | 足した |
| 症状の routes（新） | 警告 | 症状のページに routes がない（空のリストも） | 指示 |
| routes の重なり（新） | 警告 | 同じページで cause が重なる。routes の先が同じページの prerequisites か related にもある（ページの id で比べる）。1つの cause の to に同じ id が2回ある（足した） | 指示・足した |
| routes の数（新） | 警告 | 1つの cause の to が4件以上 | 指示 |
| 症状の前提（新） | 警告 | 症状のページの前提の type が concept・guide・hub でない | 指示 |
| routes と原因（新） | 警告 | routes の cause が、そのページの prevents・pitfalls にない。prevents・pitfalls の原因に routes がない | 足した |
| 未処理の候補（既存に足した） | 警告 | routes の to が、ファイルはあるのに処理されていない registry の候補 | 足した |
| 入ってくる道（既存を変えた） | 警告 | routes の先も入ってくる道に数える | 足した |
| 知らない項目（既存に足した） | 警告 | routes の要素の知らない項目 | 足した |
| wave（既存に足した） | 警告 | 入口の分野（site.yml の entry_fields）のページと症状のページに wave: 1 がない | メインの指示3に合わせて足した |
| 設定（既存に足した） | 警告 | site.yml の first_wave がない・マッピングでない・routes の値が none・first・all でない・named が文字列のリストでない・知らない項目。named の id がページを指していない、named の anchor がない。規則が名指しする concept・guide・hub が site.yml の types にない | 足した |

- **routes の先に当てない規則**：レベルの逆転・必須の前提は、前提だけを見る。routes は数えない（試験で確かめた。§2）。比例則は、この報告の後のメインの判断で、症状のページに限って routes の先も守りのページに数えるように直した（§6）
- 検査は39（エラー11・警告28）。-h の一覧に全部出る

出力の例（試験用の目次に誤りを入れたもの）：

```text
エラー: planning/catalog/enforce.yaml:5: hooks-basics: [routes] routes は type が symptom のページだけが持つ（このページは feature。ほかのページへの道は related に書く）
エラー: planning/catalog/symptoms.yaml:6: instructions-ignored: [参照] routes（縛っていない）の to の「hooks-basics#nothing」: hooks-basics の sections に anchor「nothing」がない（あるのは exit-codes）
エラー: planning/catalog/symptoms.yaml:72: done-but-not-done: [routes] routes（確かめていない）の to が空（振り分け先のページを1件以上書く）
警告: planning/catalog/symptoms.yaml:6: instructions-ignored: [routes と原因] prevents の「散らかっている」に routes がない（その原因の中心の対処を routes に書く。対処のページがない原因なら、notes に書く）
警告: planning/catalog/symptoms.yaml:6: instructions-ignored: [routes の重なり] routes の先「permissions-deny」が related にもある（related から外す。related には、routes にない近いページだけを置く）
警告: planning/catalog/symptoms.yaml:6: instructions-ignored: [routes の数] routes（縛っていない）の to が 4 件（中心の対処を 3 件までにする。ほかは related に置く）
警告: planning/catalog/symptoms.yaml:72: done-but-not-done: [症状の前提] 前提「outdated-advice-ledger」の type が ledger（症状のページの前提は、診断を読むのに要る concept・guide・hub のページだけにする。対処のページは routes に置く）
```

### 1.3 第一波の数え方

site.yml に足した項目（コメントに「工程5でユーザーに確かめる（仮）」）：

```yaml
first_wave:
  routes: first                   # routes の先を種に、none：入れない・first：各 cause の to のうち最初の必須の先・all：全部
  named: [default-safety-settings]   # 名指しで入れる正本（安全の早見表）
```

- **第一波は閉包**（メインの指示2）：核（wave: 1 のページ）と、核の症状のページの routes の先と、named のページを種にし、そこから prerequisites でたどって届くページをすべて入れる（routes の先の前提、named の前提も含む）
- **routes**（メインの指示1）：`first` は各 cause の to のうち、最初の必須（site.yml の priorities の最初）の先。必須の先がない cause からは入れない。`all` は優先度を問わず全部。`none` は入れない
- **内訳**：核 → 前提でたどって届くもの → routes から → named から の順に足したときに、新しく増えるページの数。「routes から」は routes の先と、その前提でたどって新しく届くページ。「named から 0」は、named の正本がほかの道でもう入っていることを示す
- `--stats` の第一波の行（試験用の目次）：

```text
第一波: 8 ページ（wave: 1 が 4、前提でたどって届くもの 2、routes から 1、named から 1）｜start 1・basics 1・verify 1・enforce 1・delegate 1・symptoms 2・changes 1
  routes の数え方ごとの第一波（site.yml の first_wave の routes。いまは first）: none 7・first 8・all 9
  必須の先がない cause（first ではそこから入れない）: 1（うち、first で先がどれも第一波に入らないもの 1）｜done-but-not-done（確かめていない）
```

- `--field X --stats` は、全体でたどってから X のページを数え、内訳と none・first・all の数を X と全体の両方で出す。必須の先がない cause は全体の数と一覧

### 1.4 決めた点

1. **routes の誤りの置き場所**：cause の語彙・to の解決・cause と to の有無・形は、既存の「語彙」「参照」「必須」「形」に足した（ほかのキーと同じ文と同じ解決で出る）。新しい「routes」のエラーは、症状でないページの routes と空の to だけ
2. **type がない・語彙にないページの routes**は「routes」のエラーにしない（type のエラーが出る。症状のページのつもりかもしれない）。`routes: null` は書いていないのと同じ
3. **重なりはページの id で比べる**（routes の `hooks-basics#exit-codes` と related の `hooks-basics` は重なり）。1つの cause の to の中の重複は書いたとおりの文字で比べる（ページとその節は別。related と同じ扱い）。別の cause に同じページがあるのはよい
4. **routes と原因を足した**：DR-02 の「原因ごとに中心の対処」と、設計書 §6.3 の診断の節（原因ごとの対処へのリンク）・§8.3 の症状の原因別の表が、prevents・pitfalls と routes の対応を前提にするため。routes と prevents の両方がある症状のページだけを見る（prevents が空なら「症状の prevents」だけ、routes がなければ「症状の routes」だけが出る）。語彙にない cause は見ない。site.yml の prevents か pitfalls が読めなければ、この検査をしない
5. **入ってくる道に routes を数えた**：routes の先には診断の節から道がある。数えないと、F7 が related から routes へ移したときに、症状のページからしか指されていない対処のページに当たらない警告が出る
6. **比例則に routes を数えない**（指示のとおり。設計書第2版 §3.1 の4も「関連に持ち」で routes を挙げない）。この結果は §4 の1。→ メインの判断で、症状のページは routes の先も数えるように直した（§6）
7. **症状の前提**：分野のファイルにある前提のページだけを見る（ファイルのまだない分野の候補は registry の type が見当なので見ない）。前提の type が語彙にないときは、そのページのエラーに任せる。関わる分野は症状のページの分野だけ（直すのは症状のページ）
8. **first の必須**：ページなら page の priority、分野のファイルにまだない候補・処理されていない候補なら registry の priority（見当）。存在しない id や merged・dropped の候補は必須に数えない。site.yml の priorities が読めないときは、最初の先を取る
9. **routes の種は核の症状のページだけ**（メインの指示2の閉包）。routes の先から入った症状のページの routes はたどらない。症状でないページの routes（エラー）もたどらない。いまの目次では症状のページはすべて wave: 1 なので、結果は変わらない
10. **named**：id か id#anchor。anchor がなければ「設定」の警告（ページは数える）。存在しない id・まとめた候補は「設定」の警告にして数えない。ファイルのまだない分野の候補は、たどれない候補に出す
11. **first_wave がないとき**：「設定」の警告を出し、routes を none、named を空として数える（工程3の数え方）
12. **必須の先がない cause**：数え方によらず、核の症状のページの routes を見る。first のときに先がどれも第一波に入らないもの（本当に「準備中」になる枝）の数も出す。先がほかの道で第一波に入っていれば、準備中にはならないため
13. **wave の規則を足した**：README §4.6 の2（メインの指示3）を検査に入れた。入口の分野は site.yml の entry_fields、症状のページは type で決める（分野の名前をコードに書かない）。核の分野のページだけを見る。いまの目次では0件

### 1.5 変えたファイル

| ファイル | 変えたこと |
| --- | --- |
| `tools/check_catalog.py` | §1.2 の検査（新しく6、既存に足したもの9。レベルの逆転・必須の前提・比例則は、routes を見ないことを説明に書いただけ）、`FirstWave`・`first_wave`・`format_first_wave`、site.yml の first_wave を読む `read_first_wave`、補助の `route_label`・`route_refs`・`route_seeds`・`target_priority`。前の T1・T2 の検査は、§1.2 の「既存に足した」ところのほかは変えていない（2,130行） |
| `tests/tools/test_check_catalog.py` | 試験39を足した（§2）。T1・T2 の試験8つを、試験用の目次と出力の変更に合わせて直した（§2.2。消した試験はない） |
| `tests/tools/fixtures/small/` | `schema/site.yml` に first_wave（named は試験用の目次の parallel-sessions）。`symptoms.yaml` の2ページに routes、instructions-ignored の related を routes にないページに、done-but-not-done に wave: 1（§4.6 の2）。`enforce.yaml` と `registry.yaml` の permissions-deny を必須に（first が推奨の先を飛ばすのを見せるため）。エラーも警告も出ない形のまま |
| `schema/site.yml` | first_wave の項目だけ（コメントと空行を含む8行を足した） |
| `planning/catalog/README.md` | 冒頭の骨格を「工程6c」に、版の行、§3 の例に routes、§4.4 の6（症状のページの前提と routes。DR-02）、§4.6 の2（設計書 §5.3 に合わせた）と3（第一波の数え方）、§6（新しい検査と、T2 の推移的な前提・逆引きの重複、routes の検査の表）。ほかの規則は変えていない |

## 2. 試験の数と結果

```text
$ cd /home/yuuki/projects/kyopro2/claude-atlas && python3 -m unittest discover -s tests/tools
.......................................................................................................................................................................
----------------------------------------------------------------------
Ran 167 tests in 6.201s

OK
```

試験は167（T2 の128に39を足した）で、すべて通る（Python 3.10.12・PyYAML 5.4.1）。§6 の直しの後は168で、すべて通る。`test_every_check_has_a_test` は新しい6検査も見ている。

### 2.1 足した試験（見つかる場合と見つからない場合）

| 検査・数え方 | 見つかる | 見つからない |
| --- | --- | --- |
| routes（エラー） | test_routes_on_a_page_that_is_not_a_symptom・test_empty_to | test_symptom_pages_and_pages_without_a_known_type（routes: null、type が語彙にない） |
| 語彙（cause） | test_route_cause_vocabulary | test_pitfalls_can_be_routed_and_empty_prevents_is_left_to_its_check（pitfalls の値の cause） |
| 参照（to） | test_route_targets_are_resolved（存在しない id・まとめた候補・anchor・空の id） | test_route_to_candidate_without_field_file_is_not_flagged |
| 形・必須・知らない項目 | test_route_shapes・test_route_without_cause_or_to・test_unknown_key_in_routes | 試験用の目次（エラーなし） |
| 未処理の候補 | test_route_to_unprocessed_candidate | 試験用の目次 |
| 入ってくる道 | test_routes_count_as_incoming（routes からも外すと出る） | 同（routes だけから入るページは出ない） |
| 当てない規則 | test_rules_for_prerequisites_do_not_apply_to_routes（同じページを前提に置くと出る） | 同（routes に上の段・推奨の先を置いても出ない）。比例則の試験は §6 |
| 症状の前提 | test_prerequisite_that_is_not_a_concept | test_concept_guide_and_hub_are_fine（guide・hub・症状でないページ・type が語彙にない前提） |
| 症状の routes | test_symptom_page_without_routes（キーなし・空） | test_routes_are_not_asked_of_other_pages |
| routes と原因 | test_cause_that_the_page_does_not_diagnose・test_cause_without_routes（prevents・pitfalls） | test_pitfalls_can_be_routed_and_empty_prevents_is_left_to_its_check（prevents が空・語彙なし） |
| routes の重なり | test_same_cause_and_same_target_twice・test_route_target_also_in_prerequisites_or_related（anchor の両向き） | test_same_page_in_two_causes_is_fine |
| routes の数 | test_four_targets_for_one_cause（4件） | 同（3件） |
| wave（入口と症状の全ページ） | test_every_entry_and_symptom_page_needs_wave・test_wave_must_be_1 | 同（entry_fields を変えると start は問わない） |
| 設定（first_wave） | test_missing_first_wave・test_bad_values・test_named_must_point_to_a_page・test_named_anchor・test_named_types_must_be_in_vocabulary | test_real_site_yml（本物の site.yml で0件） |
| first（最初の必須） | test_fixture・test_first_takes_only_the_first_required_target・test_priority_of_a_candidate_without_field_file_comes_from_registry | 同（推奨の先しかない cause から入れない） |
| none・first・all | test_routes_modes | |
| 閉包（routes・named の前提） | test_closure_takes_prerequisites_of_routes_and_named | |
| routes の種は核の症状のページだけ | test_routes_are_taken_only_from_core_symptom_pages | 同（核でない症状・routes から入った症状・症状でないページの routes） |
| 内訳の順（named は増えた分） | test_named_counts_only_what_it_adds | |
| たどれない候補 | test_unresolved_candidates・test_follows_prerequisites_transitively | 同（none では routes の先を数えない） |
| --stats の行 | test_stats・test_stats_for_one_field | test_stats_without_lacking_causes（0件、先がほかの道で入るもの） |

### 2.2 直した既存の試験

- test_bad_anchor・test_ref_to_merged_candidate・test_page_and_its_section_in_related_are_not_duplicates：試験用の目次の instructions-ignored の related にあった hooks-basics#exit-codes・permissions-deny を routes に移したので、related に置いて試していたものを routes か done-but-not-done で試すようにした（ねらいは同じ）
- test_wave_must_be_1：wave: 2 の how-to-use に、新しい wave の規則の警告も出る
- test_stats・test_stats_for_one_field・TestFirstWave の2つ：第一波の行の形と数が変わった

### 2.3 試験が誤りを捕まえるか

道具をわざと壊した写し（scratchpad）24通りで流し、すべてで、ねらった試験が落ちた。例：比例則に routes を数える・入ってくる道に routes を数えない・first で優先度を問わず最初の先を取る・first で必須の先を全部入れる・核でないページの routes も種にする・routes と named の先の前提をたどらない・named を routes より先に数える・候補の優先度を registry から読まない・重なりを anchor 付きで比べる（最初の試験では落ちなかったので、試験を足した）・routes の anchor を確かめない・入口と症状の全ページの wave を見ない・cause の語彙を見ない。

## 3. いまの目次に流した結果

F1〜F6 が直している途中の目次（2026-11-04、この報告を書いた時点）。

```text
$ python3 tools/check_catalog.py -q --stats（抜き書き）
第一波: 127 ページ（wave: 1 が 61、前提でたどって届くもの 64、routes から 0、named から 2）｜start 10・basics 16・models 4・prompting 7・context 5・app 3・cli 3・verify 5・eval 8・enforce 6・safety 7・delegate 5・judgment 7・cost 1・japanese 6・symptoms 33・changes 1
  routes の数え方ごとの第一波（site.yml の first_wave の routes。いまは first）: none 127・first 127・all 127
  必須の先がない cause（first ではそこから入れない）: 0
必須: 174 ページ
エラー 5 件（参照 5）、警告 83 件（推移的な前提 23・比例則 3・症状の前提 24・症状の routes 33）。-q で出していない（分野のファイル 23・ページ 357 を読んだ）
```

- **エラー5件**は、symptoms.yaml の related が、ほかの担当がいまの直しでまとめたページ（curb-sycophancy-and-overtrust・lost-in-the-middle 2件・memory-faq・does-double-check-work）を指すもの。前の道具でも同じ5件が出る（routes の検査からは出ていない）。メインが後で直す種類のもの
- **新しい警告**：症状の routes 33件（症状のページ全部。routes はまだない）、症状の前提 24件（17ページ。前提の type が feature 11・recipe 8・judgment 4・comparison 1）。ほかの新しい検査は0件
- **第一波**：127ページ。前の道具の125（核61＋前提64）に、named の default-safety-settings とその前提の where-your-data-goes の2ページが足された。routes がまだないので、none・first・all は同じ127、必須の先がない cause は0
- `--field symptoms`：エラー5、警告75（推移的な前提18・症状の前提24・症状の routes 33）
- 本物の id で数え方を確かめるため、scratchpad の写しで instructions-ignored だけに routes（見えていない・散らかっている・縛っていない、各2〜3件）を書いて流すと、none 127・first 133・all 134 になり、instructions-ignored の警告は0件だった（目次には書いていない）

## 4. 確かめていないこと

1. **比例則と routes の食い違い**（→ メインが (a) に近い形に決め、症状のページに限って直した。§6）：比例則は routes を数えないので、F7 が守りのページ（verify・eval・enforce・safety）を related から routes へ移すと、level が任せる・仕組みにする・回すの症状のページ（いま11）に比例則の警告が出うる。routes の先を related に重ねると「routes の重なり」の警告になるので、どちらかが残る。メインが決めること：(a) 比例則に routes を数える（`check_proportional` の `page_refs(p)` を `[*page_refs(p), *route_refs(p)]` にする1行）、(b) 症状のページを比例則から外す（任せる幅を広げる内容のページではない）、(c) このままにして notes に理由を書く
2. **routes を書いた後の警告の量**：F7 がまだ routes を書いていないので、routes と原因・routes の重なり・routes の数・必須の先がない cause がどれだけ出るかは分からない。第一波の数（first・all）も F7 の後でないと出ない
3. **設計書との食い違い**（D1 の第2版。直すのはメインか D1）
   - §2.3 は第一波を「routes の各原因の先頭」と書くが、メインの指示1で first は「最初の必須の先」にした
   - §2.3 は正本を `default-safety-settings#by-stage` と書くが、site.yml は指示のとおり `default-safety-settings`（道具はどちらでも読み、anchor も確かめる）
   - §3.3 のキーの台帳は routes を「symptom は必須」とするが、道具はいま警告（指示のとおり。F7 の後にエラーへ上げられる）
4. 症状の前提で、ファイルのまだない分野の候補の type は見ていない（いまは全分野のファイルがあるので当たらない）
5. routes の先が「中心の対処」か、近い順か、言い換えで重なっていないかは見ない（中身の判断）
6. Python 3.12 では流していない（3.10.12 だけ。3.10 にない書き方は使っていない）
7. 生成の層（診断の節の目印・知識マップ・症状の原因別の表）が routes を読む部分はまだない（工程6a）

## 5. メインの追加の指示（3つ）の扱い

1. **first の意味**：各 cause の to のうち、最初の必須（site.yml の priorities の最初）の先にした。必須の先がない cause からは入れない。`--stats` に、必須の先がない cause の数と一覧（ページごとの cause）と、そのうち first で先がどれも第一波に入らないものの数を出す（§1.3・§1.4 の12）。all は優先度を問わず全部のまま
2. **閉包**：種を wave: 1・核の症状のページの routes の先・named にし、前提でたどれるページをすべて入れる（routes の先の前提、named の前提も含む）。指示を受ける前の版は、routes の先から入った症状のページの routes もたどっていたので、核の症状のページの routes だけを種にする形に直した（§1.4 の9。いまの目次では数は変わらない）
3. **README**：冒頭の「骨格（工程8a）」を「骨格（工程6c）」にした（README の工程の呼び名で第2版と違ったのはここだけ。工程2・工程3の呼び名は第2版と同じ）。§4.6 の2は指示の文にし、核の分野の一覧と「核でない分野には付けない」を括弧に残した。あわせて、wave の検査に「入口の分野のページと症状のページに wave: 1 がない」を足した（§1.4 の13。いまの目次では0件。F7 が足す新しい症状のページの付け忘れを捕まえる）

## 6. 追加の直し

§4 の1（比例則と routes の食い違い）へのメインの判断（2026-11-04）：症状のページでは、routes の先も比例則の守りのページとして数える（守りの分野のページが prerequisites・related・routes のどれかにあればよい）。理由は、症状のページは原因ごとに守りのページへ振り分けるので、routes の先が「次に読む」の中心になるため。直したのは `tools/check_catalog.py` と試験だけ。

- **道具**（`check_proportional`）：type が symptom のページは、prerequisites・related に加えて routes の to の先の分野も見る。まだファイルのない分野の候補は、前提・関連と同じく registry の分野で数える。症状のページへの警告の文は「前提にも関連にも routes にも持たない」にした。ほかのページの routes（それ自体がエラー）は数えない。-h の説明も直した
- **試験**（168。T3 の最初の報告の167に1を足した）
  - 見つかる：test_routes_of_symptom_pages_count_for_the_proportional_rule の後半（routes の先も守りの分野でないと出る。文も確かめる）、test_routes_of_other_pages_do_not_count（症状でないページの routes の先は数えず、比例則と routes のエラーが出る）
  - 見つからない：test_routes_of_symptom_pages_count_for_the_proportional_rule の前半（前提から verify を外しても、routes の enforce で満たす）と最後（routes の先が eval の候補でも満たす）
  - T1 の test_delegating_page_without_guard は、試験用の目次の done-but-not-done の routes の先（hooks-basics。enforce）が守りに数えられるようになったので、routes の先も守りでないページにした（ねらいは同じ）。§2.1 の表の「当てない規則」の行の比例則の試験（test_routes_do_not_count_for_the_proportional_rule）は、この試験に置き換えた
  - 道具を壊した写しで、3通りとも試験が落ちることを確かめた（症状のページでも routes を数えない・症状でないページの routes も数える・routes の先のまだない分野の候補を数えない）
- **いまの目次**：比例則の警告は3件のまま（agents-md・feature-to-api-mapping・prompt-caching-in-practice。どれも症状のページでない）。ほかの数は §3 と同じ（F7 はまだ routes を書いていない）
- **直していないもの（メインへ）**：catalog/README §4.4 の6の3つ目の箇条（この報告の §1.5 で私が書いたもの）に「比例則（§4.3 の4）の前提・関連にも数えない」とあり、いまの道具と食い違う。指示が道具と試験だけだったので直していない。直すなら「症状のページでは、routes の先も比例則（§4.3 の4）の守りのページに数える」に置き換える。設計書第2版 §3.1 の4（「関連に持ち」「前提にも関連にも持たないと、検査が警告する」）も、症状のページの routes を書いていない（D1 かメイン）
