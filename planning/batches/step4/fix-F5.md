# 工程4 目次の直し：F5（verify・eval・enforce）

- 担当：F5（共通の指示は [brief-fix.md](brief-fix.md)）
- 日付：2026-11-04
- 書いたファイル：`planning/catalog/verify.yaml`・`eval.yaml`・`enforce.yaml`、この報告
- 変えたページ：34ページのうち30（notes の末尾に「（2026-11-04 工程4：…）」を付けた）。id と既存の anchor は変えていない

## 1. DR-19 の行ごとの扱い

| 記号 | 変えたページ | 中身 | しなかったときの理由 |
| --- | --- | --- | --- |
| a | verify：define-done・fact-checking・checking-citations・protect-tests・second-opinion-from-another-model・suspect-too-good-results／eval：verifier-defines-problem・felt-vs-measured・verifier-three-conditions・check-the-metric・selection-pressure・experiment-log・measure-the-upper-bound／enforce：move-judgment-into-scripts・permission-rules・when-to-lock（ほかに evidence-not-reports・checking-unattended-runs・freeze-eval-assets は notes だけ） | 症状のページが振り分ける困りごとの言い換えを外すか、狭い場面か goal に書き換えた（§2）。対処のページどうしの近い文（R1-06 の型）は、1つの問いなら同じ文にそろえ、そうでなければ場面を書き分けた | 残した sign の理由は §2 の末尾 |
| b | なし | — | 受け持ちのページに「古い記事のやり方が通じない」型の一般的な sign はない（signs を「記事」「古い」「前は」で見た） |
| d | eval：insights-and-usage-review／enforce：sandboxing・managed-settings-enforcement（notes） | §3 | — |
| e | enforce：freeze-eval-assets・lock-side-effects | 推移的な前提2件を related に移した（§4） | — |
| h | enforce：hook-recipes（R1-13）・sandboxing（R1-14）／verify：independent-review（R1-15） | R1-13：節 redirect-commands「決めたコマンドへ誘導する（pip の代わりに uv など）」・goal「pip ではなく uv のように、決めたコマンドを必ず使わせたい」・雛形（決めていないコマンドを止め、決めたコマンドを理由とともに返すフック。safety: false）を足し、summary に「決めたコマンドへの誘導」を入れた。根拠は 03 Q8 F6・T4、01 F-1、research/28 #6（if の Bash の判定は best-effort なので拒否ルールと組む）。R1-14：節 containers「コンテナ（Docker・devcontainer）との使い分け」と goal「Docker や devcontainer の中で Claude Code を動かすべきか決めたい」を足した（根拠は 05 4-6 の公式の Security、04 Q3）。別名は §3 のとおり外した。R1-15：goal「AI が書いたコードに脆弱性がないか見させたい」と節 security-review を足し、tracks に security-review（new_features に足した）を入れた（01 J-2） | — |
| k | verify：own-generated-code | 「採る前に説明させて確かめる手順」に絞った：前提に how-much-understanding-to-keep（related から移した。循環しない）、type を concept から recipe、summary を書き直し、線引きと「説明できない・直せない」の signs を外して手順の goal と situation にし、節 gate の題名を「自分の言葉で言い直してから採る」に、explain を「処理の流れと入力の端を説明させる」に改め、節 check-explanation「説明を実際の動きと照らす」を足した（related に unfaithful-reasoning・evidence-not-reports） | — |
| q | verify：verification-ladder・evidence-not-reports | F3 が prompting の does-double-check-work を verification-ladder（節 verbal-checks）にまとめたので（メインからも連絡を受けた）、その題名と別名（「念のため確認して」は効くか・double-check して）を aliases に移し、節 verbal-checks（もとからある anchor）の題名を「「確かめて」と書き足すことの今」から「「念のため確認して」と書き足すより、確かめる手段を渡す」に改めた（models の2ページがこの節を指す）。自分のファイルの参照（verification-ladder・evidence-not-reports の related）を外し、verification-ladder の related に model-quirks を足した。notes の末尾は「（2026-11-04 工程4：DR-19 q。F3 が does-double-check-work をまとめた）」 | F3 の案の「節 verbal-checks の level を整えるに」は採らない（design §3.1 の5：節の level はページの level 以上） |
| v | eval：insights-and-usage-review | /usage の内訳の読み方は cost の what-uses-up-limits#find-what-uses-it を持ち主にし、related の2番目に置いた。節 usage-breakdown は削るものを選ぶ判断だけにする（notes） | — |
| c・f・g・i・j・l・m・n・o・p・r・s・t・u・w・x | なし | — | 受け持ちのページが対象でない。j と t は相手が受け持ちのページ（felt-vs-measured、what-auto-mode-stops#when-blocked・lock-side-effects）を指すだけで、anchor もあるので、こちらに変更は要らない |
| DR-17（見せ方） | independent-review・lock-side-effects・hook-recipes・measure-changes・diffs-humans-must-read・sandboxing・stop-hooks・checking-unattended-runs | notes に「見せ方：」を書いた（制作の工程4の見直しの記録、state/blocks.log、制作の .claude/settings.json の H2・H3、検証ノートなど）。diffs-humans-must-read の C-22 の題材は演習の案なので、制作の環境で作り再構成と書く形に直した（design §6.10） | — |
| DR-07（参考） | sandboxing・managed-settings-enforcement | sandboxing：WSL2 ではサンドボックスの中から Windows の実行ファイルを起動でき、止めるには seccomp のフィルタが要ること（research/28 #37、R4-8）と、雛形に failIfUnavailable と Windows の経路の期待を入れること。managed-settings-enforcement：管理設定の雛形は「この環境で試せない雛形」に当たること（R4-7） | — |

## 2. 言い換えの重なり（a）で直した sign（前 → 後）

括弧は重なっていた症状のページ（または近い文の対処のページ）。

| ページ | 前 | 後 |
| --- | --- | --- |
| define-done | symptom「「完了しました」と言うのに、頼んだ状態になっていない」（claims-done-but-isnt） | 外した |
| define-done | symptom「途中で止まるか、頼んでいない所まで広げるかのどちらかになる」（keeps-stopping・does-more-than-asked） | 外し、goal「どのコマンドがどう返れば完了かを、依頼に書いて渡したい」を足した |
| fact-checking | symptom「「そんなファイルはない」と言い切られたが、本当か分からない」（claims-done-but-isnt。例の本体は evidence-not-reports#tool-output） | goal「渡した資料に書いてあることだけで答えさせたい」 |
| fact-checking | symptom「要約に、原文にない言い切りが混ざっている」（summary-overstates-source） | goal「要約が原文に書いてあるとおりかを照らしたい」 |
| checking-citations | symptom「出典はあるのに、その文献に書いてある内容と合わない」（plausible-falsehoods） | goal「挙げられた文献が、その主張を本当に支えているか確かめたい」 |
| protect-tests | symptom「特定の入力のときだけ正しい値を返すコードになっていた」（rewrote-tests-to-pass） | goal「テストを書き換えずに直すよう、依頼の段階で伝えたい」 |
| protect-tests | goal「テストや採点のファイルを Claude に触らせたくない」（freeze-eval-assets と近い） | 「テストや採点のスクリプトを、Claude に書き換えさせたくない」（freeze-eval-assets と同じ文にして束ねる） |
| own-generated-code | symptom「マージしたコードを、自分で説明できない」（learning-with-ai。F1 が how-much-understanding-to-keep に寄せた） | 外した（k） |
| own-generated-code | symptom「障害が起きたとき、AI が書いた部分を自分で直せない」（how-much-understanding-to-keep） | 外した（k）。goal「マージする前に、生成されたコードのどこが分かっていないかを洗い出したい」と situation「大事な処理を書き換えたコードを、Claude から受け取った」を足した |
| second-opinion-from-another-model | situation「Claude と何度やっても行き詰まっている」（going-in-circles）と goal「重要な変更を、別の系統のモデルにも見てもらいたい」 | goal「行き詰まったときや重要な変更で、別の系統のモデルの意見も聞きたい」（2つを1つに） |
| second-opinion-from-another-model | symptom「複数の AI が同意したので正しいと思ったが、違っていた」（caves-when-pushed） | goal「別のモデルと意見が一致したとき、それをどこまで信じてよいか知りたい」 |
| suspect-too-good-results | symptom「急に何倍も速くなったと報告された」（recipes の performance-tuning と近い） | 「桁違いに速くなったと報告されたが、本当か怪しい」（performance-tuning と同じ文にして束ねる） |
| verifier-defines-problem | symptom「テストは全部通るのに、欲しかったものになっていない」（misses-broken-evaluation・claims-done-but-isnt） | 「テストに書いた条件だけが満たされ、書かなかった意図は抜けていた」 |
| felt-vs-measured | symptom「前より賢くなくなった気がする」（seems-less-capable の題名。R1-04） | goal「良くなった・悪くなったという自分の感じを、どこまで信じてよいか知りたい」 |
| verifier-three-conditions | symptom「手元の評価では勝つのに、本番では効かない」（付表A の4） | 「手元で試した入力と、本番の入力の傾向が違っていた」 |
| check-the-metric | symptom「手元のスコアは良いのに、本当の目的では悪い」（付表A の3） | 「上げさせた指標が、本当に上げたかったものとずれていた」 |
| selection-pressure | symptom「改善を重ねてスコアは上がったのに、新しい入力では伸びない」（R1-07） | 「いちばん点の良かった版を選んだのに、新しい入力では平凡だった」 |
| experiment-log | symptom「前に失敗した案を、また試していた」（context の keep-failure-lessons・going-in-circles） | 「前に効かなかった改善案を、気づかずにまた試していた」 |
| measure-the-upper-bound | symptom「「これ以上は改善できません」と言われた」（付表A の7） | goal「「これ以上は改善できない」と言われたとき、本当かを数字で確かめたい」 |
| move-judgment-into-scripts | symptom「同じ作業なのに、毎回結果が少しずつ違う」（plausible-falsehoods の「同じ質問をするたびに答えが変わる」） | 「同じ集計なのに、頼むたびに数字が少しずつ違う」 |
| permission-rules | symptom「拒否のルールに書いたのに、そのファイルを読まれた」（sandboxing の近い文、secrets-exposed） | 「拒否のルールに書いたのに、下のフォルダにある同じ名前のファイルは読まれた」（節 path-rules。11 第4節 #21） |
| when-to-lock | situation「同じ注意を何度も繰り返している」（repeating-the-same-explanation・instructions-ignored。メインの連絡を受けて判断した） | 外した。F4 も extend の when-to-add-what の同じ文を goal「繰り返している注意や手順を、どの仕組みに移すか決めたい」に替えた。goal の形はそれと basics の request-vs-lock とこのページの「例外なく守らせたい規則がある」で足りるので、新しい goal は足さない。「同じ注意を二回した」は鍵に移す合図として summary と節 signals に残す |

途中で変えて戻したもの：checking-unattended-runs の situation は、F6 が where-bypass-is-ok をこちらの元の文「夜間や CI で、人が見ていない間に Claude を動かしている」にそろえたので、元の文のままにした（束ねる）。when-to-lock の goal「例外なく守らせたい規則がある」は、いったん emphasis-words の文にそろえたが、F3 があちらを「強調に頼らずに、大事な指示を守らせたい」に書き分けたので元に戻した。

同じ文で束ねるもの（1つの問いに、考え方と手段など複数の答えがある）：テストが通るまで終わらせたくない（verification-ladder・stop-hooks・delegate の goal-until-done）、`.env` や migrations を絶対に触らせたくない（permission-rules・block-with-exit-2）、auto モードに任せて大丈夫か（what-auto-mode-stops・sandboxing）、自分の目で全部レビューする時間がない（independent-review・diffs-humans-must-read）、テストや採点のスクリプトを…（protect-tests・freeze-eval-assets）、桁違いに速くなったと…（suspect-too-good-results・performance-tuning）、夜間や CI で…（checking-unattended-runs・where-bypass-is-ok）。

残した sign（その対処が直接の答えになる狭い場面か goal とみなした）：verification-ladder「「確かめて」と書いても、確かめずに終わる」（言葉で書き足した場面。節 verbal-checks）、evidence-not-reports の2文（件数が変わる・うまくいった場合だけ）、visual-checks「テストは通るのに、画面を開くと動かない」、checking-unattended-runs の2文（無人の場面）、looks-are-not-quality の2文（見た目の整った成果物）、when-to-lock の2文（catalog/README §4.5 の4の例）、what-auto-mode-stops「auto モードに操作を止められて…」、stop-hooks「Stop フックを入れたら…」、protected-paths「`.claude` や `.git` を…」、lockbox-and-holdout「見えているテストは通るのに、隠れたテストで…」（R1-07 の原因に固有の場面）、differential-testing「テストでは見つからない間違いが…」（評価の点ではなく正しさの誤り）、hook-recipes・permission-rules の goal（goal の形）。

## 3. 別名の重なり（d）

- 外した：insights-and-usage-review の /cost・/stats（主は cli の usage-context-statusline。旧名の台帳 slash-cost-and-stats は outdated_advice に残す。DR-18）
- 足してから外した：sandboxing の devcontainer・Docker・コンテナ（R1-14）。F6 が同じ3語を where-bypass-is-ok に置き、理由（このページの OS のサンドボックスはコンテナではない。使い捨てのコンテナの雛形と sign「コンテナの中で Claude Code を無人で動かしたい」はあちら）も筋が通るので、重ならないようこちらから外した。節 containers と goal は残した
- 残した：own-generated-code の認知負債（表で主。F1 は how-much-understanding-to-keep から外した）。managed-settings-enforcement の managed settings・managed-settings.json・server-managed settings（表で主）
- 足した：verification-ladder の「「念のため確認して」は効くか」「double-check して」（q でまとめられた does-double-check-work の題名と別名。ほかのページと重ならない）

## 4. 外した前提（e）

- freeze-eval-assets の前提 permission-rules（sandboxing → permission-rules で届く）→ related の2番目へ
- lock-side-effects の前提 when-to-lock（block-with-exit-2 → hooks-basics → when-to-lock で届く）→ related の先頭へ（when-to-lock#what-not-to-lock）
- 足した前提：own-generated-code に how-much-understanding-to-keep（k）。新しい推移的な前提の警告は出ない（直す前後の全体の検査の差で確かめた）。前提の深さは own-generated-code が5段、それを前提にする recipes の create-and-review-prs が6段

## 5. まとめたページ・新しいページ・priority と level

- まとめたページ・新しいページ：なし。priority・level・wave を変えたページ：なし
- type を変えた：own-generated-code（concept → recipe。k で手順が本体になった）
- 受けたまとめ：prompting の does-double-check-work → verification-ladder（F3、q。§1 の q）
- 足した anchor：independent-review#security-review、own-generated-code#check-explanation、sandboxing#containers、hook-recipes#redirect-commands。題名だけ改めた節：own-generated-code#explain・#gate、verification-ladder#verbal-checks
- 足した雛形：hook-recipes の「決めていないコマンド（pip など）を止め、決めたコマンド（uv run など）を理由とともに返すフック」（hook、safety: false）
- new_features：security-review（/security-review。verify.yaml）

## 6. メインへ

1. **q の does-double-check-work**（F3 → verification-ladder）：別名を移し、節 verbal-checks の題名を改めた（§1）。models の2ページは F2 が verification-ladder#verbal-checks に替えた。最後の検査の時点で、symptoms の claims-done-but-isnt（F7）だけがまだ does-double-check-work を指し、検査のエラーになる。道具で verification-ladder#verbal-checks に直してほしい。F3 の「節 verbal-checks の level を整えるに」は design §3.1 の5に合わないので採らなかった。整えるの段から引く道が別名と逆引きで足りないなら、規則か段をメインが決める
2. **k の別名**：認知負債と「説明できないコードを出荷しない」は、k の後は線引きを持つ how-much-understanding-to-keep のほうが主に近い。fix-aliases.md の表に従って own-generated-code に残した。主を替えるなら、両方のファイルをそろえてほしい
3. **R1-14 の別名の主**：README は sandboxing の別名として割り当てたが、F6 の where-bypass-is-ok を主にして、こちらから外した（§3）。sandboxing を主にするなら、メインが移す
4. **managed settings の3語**：検査の時点で、team の org-managed-settings-and-mcp（F6）にまだ残っている
5. **束ねた文の相手**：相手の担当が文を変えると束ねが切れる。特に recipes の performance-tuning（F7 はまだ始めていない）と safety の where-bypass-is-ok。変えるなら suspect-too-good-results・checking-unattended-runs も合わせる必要がある
6. **new_features の security-review**：features.yaml にまとめてほしい。/security-review の別名は delegate の automated-pr-review にだけある
7. **R1-13 の困りごとの文**：「決めたコマンド（uv・pnpm など）を使わず別の方法で実行する」は、symptoms の instructions-ignored（F7）か extend の what-to-put-in-claude-md（F4）が持つ必要がある。hook-recipes は goal の形だけを持つ。F7 が routes を作るとき、その原因の振り分け先に hook-recipes#redirect-commands を使える。when-to-lock から situation「同じ注意を何度も繰り返している」を外したので、repeating-the-same-explanation で禁止の注意を繰り返している枝（いまの prevents は「見えていない」だけ）を受けるなら、振り分け先に when-to-lock#signals を置ける（ほかに使える anchor：what-auto-mode-stops#when-blocked・stop-hooks#avoid-loops・hook-recipes#filter-test-output・when-to-lock#spoken-rules-fade・evidence-not-reports#tool-output・verification-ladder#verbal-checks・measure-changes#by-stratum）
8. **q の add-tests**（F7）：pitfalls-of-ai-written-tests か test-the-verifier（どちらもこちら）にまとめるなら、まとめ先の別名と signs の受け入れは、メインが移すか、受け持ちに頼む
9. **DR-07 の注記**：managed-settings-enforcement の雛形（/etc の管理設定）は「この環境で試せない雛形」、sandboxing の雛形は failIfUnavailable と WSL2 の Windows の実行ファイルの経路を期待に入れる、と notes に書いた。DR-19 の外なので、要らなければ外してよい
10. **DR-17 の見せ方**：notes に書いたのは8ページ（§1）。題材の一覧を作るときに使える。題材の多くは、まだない制作の記録（state/blocks.log、工程4の見直しの記録の注釈）を前提にしている

## 7. 検査の結果

- `python3 tools/check_catalog.py --field verify`：エラー0・警告0（直す前もエラー0・警告0）
- `--field eval`：エラー0・警告0（直す前もエラー0・警告0）
- `--field enforce`：エラー0・警告0（直す前はエラー0・警告2。どちらも推移的な前提で、§4 で消した）
- 全体（最後に流した時点。357ページ）：エラー5（参照5）・警告26。指摘は受け持ちのファイルにない。エラー5件はすべて symptoms.yaml（F7 はまだ始めていない）にあり、ほかの担当のまとめ（lost-in-the-middle・memory-faq・does-double-check-work・curb-sycophancy-and-overtrust）を指す参照。こちらはページをまとめていないので、まとめたページを指す参照のエラーは0件
- 残した警告：なし

## 8. 確かめていないこと

- 言い換えの判断は、症状のページ33本と受け持ちのページの signs を、2字の重なりと difflib の比で並べ、上位と、R3 の付表A・R1-04〜R1-07 の束を目で見て決めた。比の低い言い換えは見落としがありうる
- 書き換えた sign が読者の打つ言葉かは、課題で引いて確かめていない（逆引きはまだ生成できない）
- /security-review、dev container、フックの if、WSL2 のサンドボックスの挙動は、調査資料（01 J-2・F-1、05 4-6、research/28 #6・#36・#37）で見ただけで、一次資料は開いていない（Web を開かない）
- 同時に動いている担当（F1・F3・F4・F6）のファイルは、検査の時点の状態を読んだだけ。後で変われば、束ねた文・別名の主・own-generated-code の前提の深さの前提が崩れうる。F7（symptoms・recipes）はまだ始めていない
