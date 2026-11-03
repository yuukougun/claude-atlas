# 工程3 I5：verify・eval・enforce の目次の統合の報告

- 担当：I5（2026-11-04）
- 書いたもの：[planning/catalog/verify.yaml](../../catalog/verify.yaml)・[eval.yaml](../../catalog/eval.yaml)・[enforce.yaml](../../catalog/enforce.yaml)
- 従ったもの：[brief-integrate.md](brief-integrate.md)（M1〜M11）、catalog/README.md、design §2〜§4・§6.2、schema/site.yml。材料は `state/step3-integrate/I5-input.md`（A 40項目・B 8行）
- 変えたページは18（verify 6・eval 3・enforce 9）。どのページも notes の末尾に「（2026-11-04 統合：<番号>）」を足した
- ページの追加・統合・削除・分野の移動はしていない。id と anchor の変更・削除もない（anchor を2つ足した）。priority・level・wave も変えていない

## 1. 材料 A の各項目の扱い

「確かめた」は 2026-11-04 の作業中に確かめた時点の状態。ほかの分野のファイルは同時に書き換わっている。

| 番号 | 扱い | 変えたページ・確かめたこと・反映しない理由 |
| --- | --- | --- |
| basics#2 | 反映した | enforce/when-to-lock の notes：節 spoken-rules-fade では、圧縮で残るもの・消えるものの一覧を繰り返さず what-survives-compaction を指す（一覧はそこに一本化）。context・symptoms の部分は対象外 |
| basics#5 | 取り込み済みを確かめた | protect-tests と verifier-three-conditions の前提に reward-hacking（必須・任せる）がある。段の逆転なし。sycophancy は independent-review・instructing-reviewers・model-based-grading の related にある |
| basics#8 | 取り込み済みを確かめた | fact-checking（使う）の前提は why-hallucinations（使う）だけで、nondeterminism・summary-overgeneralization は related |
| surfaces#4 | 取り込み済みを確かめた | visual-checks → browser-control。ほかの分野の主張12件（product-map・make-slides・using-ides など）もすべて入っている |
| models#4 | 取り込み済みを確かめた | felt-vs-measured → suspected-degradation。ほかの分野の主張15件もすべて入っている |
| prompting#5 | 反映した | verify/define-done の related に ask-for-outcomes を足した。define-done → four-specifics、evidence-not-reports → does-double-check-work は元からある |
| prompting#8 | 取り込み済みを確かめた | measure-changes の notes に、プロンプトや指示を変えたときの小さな eval を例にすると書いてある。prompting の4ページ（prompt-patterns・before-after-prompts・refine-in-conversation・share-targets-and-bounds）は measure-changes を related に持つ |
| context#6 | 反映した | when-to-lock の notes に分担を書いた（約束の置き場所の判断全般は promises-after-compaction、会話で言った禁止を拒否ルールとフックに移す判断は節 spoken-rules-fade）。promises-after-compaction と compact-and-auto-compact はこの節を指している |
| cli#8 | 反映した | permission-rules と what-auto-mode-stops は前提に permission-modes-overview を元から持つ。モードを扱う protected-paths（節 protected）と managed-settings-enforcement（節 disable-modes）の related にも足した |
| extend#1 | 取り込み済みを確かめた | when-to-lock は what-to-put-in-claude-md#what-to-leave-out を指している。受け持ちの3ファイルに、まとめられた id（what-to-leave-out-of-claude-md・commands-became-skills など）への参照はない |
| extend#4 | 反映した | eval/measure-changes に節 compare-skills（仕組みにする。スキルの有り無しを新しいセッションで比べる。skill-creator・claude plugin eval）を足し、materials に 01 D-2、related に writing-skills#evaluate、tracks に plugin-eval（eval.yaml の new_features）を入れた。extend の writing-skills は節 evaluate から measure-changes へ案内している |
| extend#11 | 取り込み済みを確かめた | M1 で決まった。受け持ちの題名に英語の表記の残りはない。summary の残り1件（measure-changes の skill）を直した（§3） |
| verify#1 | 対象外 | safety（I6）。確かめた時点で vetting-extensions の related に looks-are-not-quality が入っていた |
| verify#2 | 取り込み済みを確かめた | claims-done-but-isnt（前提 define-done・evidence-not-reports）・plausible-falsehoods（前提 fact-checking）・summary-overstates-source（前提 checking-citations）・rewrote-tests-to-pass（related protect-tests）・permission-to-stop（related protect-tests）。台帳 add-double-check は verification-ladder と does-double-check-work が持つ |
| verify#3 | 取り込み済みを確かめた | protect-tests の前提 reward-hacking、fact-checking → read-specs-yourself、visual-checks・looks-are-not-quality → frontend-design・make-slides、suspect-too-good-results → audit-ml-pipelines、own-generated-code の notes の書き分け |
| verify#4 | 反映しない | second-opinion-from-another-model は任意のまま。根拠が中〜弱で、書くかは初版の後に需要を見て決める（今決めることはない） |
| eval#1 | 取り込み済みを確かめた | test-the-verifier と experiment-log の wave: 1 はある（M10。変えていない）。2ページの notes に「wave を付けていない」とメインの追記が並んで食い違っていたので、経緯が一続きに読めるように書き直し、eval.yaml の頭の注記に計6を書いた |
| eval#2 | 対象外 | symptoms（I7）。確かめた時点で seems-less-capable はあり、felt-vs-measured を related に持つ。misses-broken-evaluation は measure-changes を related に持つ（#by-stratum ではないが、参照のエラーはない） |
| eval#3 | 対象外 | models（I2）。確かめた時点で suspected-degradation の前提に felt-vs-measured、after-switching-models の前提に measure-changes が入っていた（段と優先度は合う）。これで felt-vs-measured（整える）と measure-changes（任せる）は段を上げられなくなった |
| eval#4 | 取り込み済みを確かめた | measure-changes の節 terms・graders、related の batch-api-basics・keep-replies-in-japanese#measure、別名「プロンプトの評価（eval）入門」、verifier-three-conditions の前提 reward-hacking、test-the-verifier → add-tests、differential-testing → search-code-checklist |
| enforce#2 | 取り込み済みを確かめた | 受け持ちの部分（when-to-lock の節 spoken-rules-fade と merged）はある。ほかの分野は、promises-after-compaction・compact-and-auto-compact が節を、what-survives-compaction・forgot-after-compaction がページを指す（どちらも参照のエラーはない） |
| enforce#3 | 取り込み済みを確かめた | protect-tests・verifier-three-conditions・lockbox-and-holdout → freeze-eval-assets。protect-tests の notes に分担がある |
| enforce#4 | 取り込み済みを確かめた | managed-settings-enforcement → org-managed-settings-and-mcp#delivery（anchor はある）。受け持ちで bypassPermissionsDisabled は notes の注意書きにだけある |
| enforce#5 | 対象外 | extend（I4）。確かめた時点で hook-vs-skill → hooks-basics、writing-subagents・what-subagents-dont-inherit → hook-recipes#subagent-only が入っていた |
| enforce#6 | 対象外 | japanese（I3）。確かめた時点で textlint-hook の前提に hooks-basics、related に writing-safe-hooks が入っていた |
| enforce#7 | 対象外 | symptoms（I7）。確かめた時点で instructions-ignored → when-to-lock（前提）、forgot-after-compaction → when-to-lock、wrong-amount-of-approvals → what-auto-mode-stops・lock-side-effects、keeps-stopping → lock-side-effects はあった。stuck-in-a-check-loop → stop-hooks#avoid-loops と keeps-stopping → what-auto-mode-stops はまだなかった（§5 の連絡） |
| enforce#8 | 対象外 | cli（I4）。確かめた時点で permission-modes-overview → what-auto-mode-stops・permission-rules、settings-layers → managed-settings-enforcement が入っていた |
| enforce#9 | 反映しない | sandboxing の level は decisions 2026-11-03「安全の既定の勧め方」のとおり任せるのまま。sandboxing を前提にするページ（freeze-eval-assets・where-bypass-is-ok）に段の逆転はない |
| safety#3 | 対象外 | delegate（I6）。確かめた時点で headless-basics・five-questions-before-delegating → where-bypass-is-ok、parallel-with-worktrees → sandboxing はあった。github-actions-with-claude・cloud-schedules → where-bypass-is-ok、goal-until-done → sandboxing はまだなかった（§5 の連絡） |
| safety#4 | 対象外 | app（I2）。確かめた時点で permission-modes-in-the-app の related に what-auto-mode-stops、前提に lethal-trifecta が入っていた。what-auto-mode-stops は元から permission-modes-in-the-app を related に持つ |
| delegate#7 | 取り込み済みを確かめた | 列挙の22ページすべてが delegate のページを前提か related に持つ（受け持ちでは checking-unattended-runs・verification-ladder・verifier-defines-problem・selection-pressure・experiment-log・what-auto-mode-stops・sandboxing） |
| judgment#1 | 取り込み済みを確かめた | own-generated-code の notes（出荷の基準と、学ぶ手順の learning-with-ai の書き分け）と related の learning-with-ai |
| japanese#4 | 反映した | enforce/stop-hooks の related に keep-replies-in-japanese#stop-hook を足した。hook-recipes → textlint-hook は元からある |
| japanese#8 | 取り込み済みを確かめた | measure-changes → keep-replies-in-japanese#measure |
| recipes#2 | 取り込み済みを確かめた | test-the-verifier → add-tests。verifier-three-conditions は任せるのまま（bisect-regressions・build-test-harness が前提にする） |
| recipes#3 | 取り込み済みを確かめた | verify#3 と同じ4件 |
| recipes#5 | 取り込み済みを確かめた | move-judgment-into-scripts → bisect-regressions、freeze-eval-assets → build-test-harness |
| team#3 | 取り込み済みを確かめた | 列挙の20ページすべてが team のページを指す。managed-settings-enforcement → org-managed-settings-and-mcp#delivery、long-team-competitions の前提 separate-roles、four-principles → ai-amplifies-organizations |
| contest#3 | 取り込み済みを確かめた | differential-testing の notes（A-9 後半は search-code-checklist）と related。evaluators-by-format の前提 verifier-three-conditions、running-contest-experiments の前提 experiment-log・selection-pressure と related の measure-changes#by-stratum |
| symptoms#13 | 反映した | verify/evidence-not-reports に節 tool-output（道具の出力も確かめる：途中で切れた検索・失敗を成功として返す起動。research/22 #18・#24）を足し、related に blames-the-tools を足した。claims-done-but-isnt と blames-the-tools はこのページを前提にしているので related には置けない。本文の診断からこの節へ案内できる |

数：反映した 7・反映しない 2・対象外 9・取り込み済みを確かめた 22（計40。メインへ回した A の項目はない）。

## 2. 材料 B の行の扱い（M2）

| # | 項目 | 扱い |
| --- | --- | --- |
| 36 | 毎回フォーマッタをかけさせたい | 足さない。hook-recipes に同じ意味の「編集のたびにフォーマッタをかけさせたい」がある（向く先は受け持ちの1ページだけなので、文はそろえていない） |
| 37 | `.env` や migrations を絶対に触らせたくない | permission-rules：同じ意味の「`.env` や特定のフォルダを絶対に触らせたくない」を項目の文に置き換えた。block-with-exit-2：同じ文を足した（拒否ルールで足りないとき、理由と代わりの手段を返して止める側）。2ページを同じ文にして、逆引きで1項目に並ぶようにした |
| 38 | テストが通るまで終わらせたくない | 足さない。verification-ladder と stop-hooks に同じ文がある |
| 46 | 自分の目で全部レビューする時間がない | independent-review には同じ文がある。diffs-humans-must-read に同じ文を足した（situation）。元の「差分が大きすぎて、全部は読めない」は、量の困りごとで時間の困りごとと別の入口なので残した |
| 47 | 見た目の崩れを確かめさせたい | 足さない。visual-checks に同じ文がある |
| 48 | CLAUDE.md を変えて良くなったか知りたい | measure-changes に同じ文がある。felt-vs-measured には足さない。項目に直接答えるのは測り方の measure-changes で、felt-vs-measured はその前提（measure-changes から前提でたどれる） |
| 49 | 調査結果の出典を確かめたい | 足さない。checking-citations に同じ文がある |
| 51 | auto mode に任せて大丈夫か | what-auto-mode-stops：同じ意味の situation「auto モードに任せて大丈夫か不安」を、表の種類の goal「auto モードに任せて大丈夫か」に直した。sandboxing：同じ文を足した（auto モードは安全を保証しないので、任せる段階ではサンドボックスで囲う） |

**M2 の3つ目（症状の項目を対処のページに重ねない）**：00 §4 の症状の33項目と同じ文が、受け持ちの対処のページに4つあったので外した。どれも、症状のページが前提か related でそのページを指している。

| 外したページ | 外した sign | その文を持つ症状のページ |
| --- | --- | --- |
| verify/evidence-not-reports | 「全部通りました」と言うが、信用できない（#44） | claims-done-but-isnt（前提にこのページ） |
| verify/fact-checking | 同じ質問で毎回答えが違う（#8） | plausible-falsehoods（前提にこのページ。症状のページの文は補ってある） |
| verify/checking-citations | もっともらしいが、出典が怪しい（#6） | plausible-falsehoods（related にこのページ） |
| verify/protect-tests | テストのほうを書き換えて通された（#45） | rewrote-tests-to-pass（related にこのページ） |

外した後も、4ページとも signs は2つ以上ある。文の違う近い困りごとは残した（§5 の2）。

## 3. 題名を変えたページ

なし。

- summary：measure-changes の「skill」を「スキル」にした（M1）。ほかの summary と題名に、M1 の表で揃える英語の表記は残っていなかった
- aliases：permission-rules に permission rules・allow ルール・ask ルールを足した（M1 の「aliases に「allow ルール」「deny ルール」など」。deny ルール・許可ルール・確認ルール・拒否ルールは元からある）
- permission-rules の題名「権限ルール（allow・ask・deny）」は変えていない。権限は M1 どおりで、括弧の allow・ask・deny は設定のキー（原文のまま書くもの）。ルールの呼び名は summary で M1 の仮の表記（許可・確認・拒否のルール）になっている。題名にキーを残せば、工程5で仮の訳語が変わっても題名を直さずに済む（§7 の迷った点）

## 4. 新しいページ、priority・level を変えたページ

なし（wave も変えていない。M10）。そのほかに変えたもの：

- 足した anchor：verify/evidence-not-reports#tool-output、eval/measure-changes#compare-skills（level 仕組みにする。ページは任せる）
- 足した機能の id：plugin-eval（claude plugin eval。eval.yaml の new_features。measure-changes の tracks）
- M3：enforce/request-lock-table の outdated_advice に styles-for-tone を足した（アプリの形式・文体の行のお願いの側に Styles を挙げない。notes に、いつもそろえるなら指示、場面ごとならスキルと書いた）。subagents-to-save-context に関わるページは受け持ちにない
- M6：enforce/sandboxing の related の default-safety-settings を default-safety-settings#by-stage にした（sandboxing の level の根拠が段階ごとの既定だから）
- M9：受け持ちに比例則の警告はない

## 5. メインへ

判断の要るもの（2件）：

1. **features.yaml に plugin-eval を足す**（eval.yaml の new_features）。01 D-2 の「スキルの有り無しを新しいセッションで比べる」公式の方法（skill-creator のプラグイン・`claude plugin eval`）を measure-changes の節 compare-skills の例にしたため。成熟度・版の下限・使える面は土台作りで確かめる
2. **M2 の「同じ文」の範囲**：文は違うが同じ困りごとを言う症状の sign が、受け持ちの対処のページに6組残る。M2 を「同じ困りごと」まで広げるなら、これらは対処のページから外すか goal の形に直す（指示があれば I5 が直す。工程4でもよい）。広げないなら今のままでよい（selection-pressure のほかは、症状のページがその対処のページを前提か related で指している）

| 対処のページの sign | 近い症状のページの sign |
| --- | --- |
| enforce/when-to-lock「CLAUDE.md に「〜しない」と書いたのに破られる」 | instructions-ignored「CLAUDE.md に書いたのに守られない」（00 §4 #29） |
| verify/define-done「「完了しました」と言うのに、頼んだ状態になっていない」 | claims-done-but-isnt「完了と報告されたのに動かない」 |
| verify/protect-tests「特定の入力のときだけ正しい値を返すコードになっていた」 | rewrote-tests-to-pass「特定の入力だけ通るように分岐を足された」 |
| eval/felt-vs-measured「前より賢くなくなった気がする」 | seems-less-capable「急に性能が落ちた気がする」（#62） |
| eval/verifier-three-conditions・check-the-metric・selection-pressure（手元の評価やスコアは良いのに、本番・本当の目的・新しい入力では効かない） | misses-broken-evaluation「手元のスコアは上がるのに本番で通用しない」（selection-pressure は指されていない） |
| eval/measure-the-upper-bound「「これ以上は改善できません」と言われた」 | wont-rethink-approach「少し試しただけで「これ以上は無理です」と言われる」 |

連絡（判断は要らない。ほかの担当の分野で、確かめた時点では入っていなかったもの。最後の全体の検査のときに見てほしい）：

- I7（symptoms）：stuck-in-a-check-loop → stop-hooks#avoid-loops、keeps-stopping → what-auto-mode-stops（enforce#7）。misses-broken-evaluation の measure-changes を measure-changes#by-stratum に（eval#2。今のままでもエラーはない）。claims-done-but-isnt・blames-the-tools の診断の本文から evidence-not-reports#tool-output へ案内できる（symptoms#13）
- I6（delegate）：github-actions-with-claude・cloud-schedules → where-bypass-is-ok、goal-until-done → sandboxing（safety#3）
- I4（extend、任意）：writing-skills の節 evaluate から measure-changes#compare-skills を指せる（extend#4）

## 6. 検査の結果

- `python3 tools/check_catalog.py --field verify`・`--field eval`・`--field enforce`：どれもエラー 0 件・警告 0 件（最後の実行は分野のファイル 23・ページ 361 を読んだ時点）。残した警告はない
- 全体（`python3 tools/check_catalog.py`）：エラー 0 件、警告 5 件（どれも比例則で、受け持ちの外。M9 の6件のうち1件はほかの担当が消していた）
- 受け持ちのページ数と内訳は変わらない（verify 17・eval 13・enforce 15）。その時点の第一波の数は verify 5・eval 8・enforce 6
- 手元の確認：変えた summary は120字以内（measure-changes 80字）。足した related で前提との重複・20件超えはない。足した sign に変わりやすい値・モデルとプランの名前はない

## 7. 確かめていないこと、迷った点

**確かめていないこと**

- 一次資料は開いていない（Web を使わない指示）。skill-creator と `claude plugin eval` の今の名前・使える面は 01 D-2（確認日 2026-10-29）による
- 逆引きを作る道具が、同じ文の sign を1項目にまとめるかは確かめていない。B の #37・#46・#51 で複数のページを同じ文にそろえたのは、まとめることを見込んだため
- ほかの分野の状態（§1 の「確かめた時点」）は、同時に書き換わっている

**迷った点**

1. **permission-rules の題名**：M1 の行に合わせて「権限ルール（許可・確認・拒否）」にする案もある。括弧が設定のキーなので原文のまま残した。メインが訳語に寄せると決めれば、題名を直し、元の題名を aliases に入れる
2. **#51 の文の表記**：00 §4 の文は「auto mode」だが、元からあった sign と題名に合わせて「auto モード」にした（M1 は signs を変えなくてよいとしており、変えてはいけないとはしていない）。「auto mode」は what-auto-mode-stops の aliases にある
3. **#48 を felt-vs-measured に置かないこと**：表は2ページを挙げるが、「直接答えるページ」を測り方の measure-changes だけとした。体感のずれを先に読ませたいなら felt-vs-measured にも同じ文を置く
4. **plugin-eval を tracks に入れたこと**：measure-changes は原理のレシピなので volatility は低のままにした。道具の名前や使える面が変わったときは tracks で点検に掛かる
5. **eval#1 の notes の書き直し**：メインの追記の文はそのまま残し、前の文（「wave を付けていない」）だけを経緯の文に直した。wave の値は変えていない
6. **open_issues**：受け持ちの3ファイルの open_issues は、2段目の記録として変えていない（扱いはこの報告に書いた）
